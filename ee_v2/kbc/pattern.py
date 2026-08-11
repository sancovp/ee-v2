"""pattern.py — THE CONFORMANCE GATE (Isaac 2026-08-11: "a KB of code patterns
so LLMs can fill out the geometries and figure out if they are staying in
pattern or not for different archis").

pattern-as-geometry-as-gate. A pattern's GEOMETRY is roles + structural
INVARIANTS (required / forbidden / forbidden_transitive edges over roles). An
architecture is checked by FILLING the geometry — binding real elements to
roles and declaring the real edges — and running the ee_pattern MAP gate:

    verdict = conformance(geometry, mapping)
    verdict["in_pattern"]   True  -> the architecture STAYS in the pattern
                            False -> it DRIFTED; verdict["drift"] NAMES where:
      {"forbidden": [(inv, from, to)],       a forbidden edge is present
       "forbidden_path": [(inv, from, to)],  a forbidden PATH exists (layered)
       "missing":  [(inv, from)],            a required edge is absent
       "malformed": [role]}                  a binding onto a phantom role

The geometry can be authored directly (a dict) or PROJECTED from a certified
pattern KB (geometry_from_kb) — the same KBs the dark floor grows. The fill is
the free-agent step (an LLM maps code -> roles); the gate is the bound step.
Same worker-binding spectrum as the rest of the stack; the residue is the
teacher.
"""
from __future__ import annotations

import tempfile
from pathlib import Path

from ._paths import ensure_deps
ensure_deps()

from map_v2 import (MapV2Lattice, PrologTargetCompiler,          # noqa: E402
                    load_domain_manifest)

DOM = Path(__file__).resolve().parent.parent \
    / "map_gate/domains/ee_pattern/domain.json"

_INV_KINDS = ("required", "forbidden", "forbidden_transitive")


def _atomize(names):
    """Real code elements are CamelCase (PaymentContext); Prolog atoms must be
    lowercase-first ^[a-z][a-zA-Z0-9_]*$. Build a stable name<->atom bijection
    (lowercase-first + sanitize; disambiguate collisions) so the gate runs on
    atoms and the residue maps back to the real names the LLM used."""
    import re
    to_atom, from_atom = {}, {}
    for n in names:
        if n in to_atom:
            continue
        a = re.sub(r"[^a-zA-Z0-9_]", "_", str(n))
        a = (a[:1].lower() + a[1:]) if a else "e"
        if not re.match(r"^[a-z]", a):
            a = "e_" + a
        base, k = a, 1
        while a in from_atom:
            k += 1
            a = f"{base}_{k}"
        to_atom[n], from_atom[a] = a, n
    return to_atom, from_atom


def _payload(subject, geometry, mapping, el2atom):
    roles = [{"kind": "role", "id": r} for r in geometry["roles"]]
    invs = []
    for i, inv in enumerate(geometry["invariants"]):
        invs.append({"kind": "invariant", "id": inv.get("id", f"inv{i}"),
                     "inv": inv["inv"], "relation": inv["relation"],
                     "source_role": inv["source_role"],
                     "target_role": inv["target_role"]})
    binds = [{"kind": "bind", "element": el2atom[e], "role": r}
             for e, r in mapping["bindings"]]
    edges = [{"kind": "edge", "relation": rel, "source": el2atom[s],
              "target": el2atom[t]}
             for rel, s, t in mapping.get("edges", [])]
    return {"kind": "ee_pattern", "subject": subject, "roles": roles,
            "invariants": invs, "bindings": binds, "edges": edges}


def _parse_residue(frontier, atom2el):
    import re
    def el(a):
        return atom2el.get(a.strip(), a.strip())
    drift = {"forbidden": [], "forbidden_path": [], "missing": [],
             "malformed": []}
    for f in frontier:
        m = re.match(r"drift_forbidden\(([^,]+),([^,]+),([^)]+)\)", f)
        if m:
            i, a, b = m.groups()
            drift["forbidden"].append((i.strip(), el(a), el(b)))
            continue
        m = re.match(r"drift_forbidden_path\(([^,]+),([^,]+),([^)]+)\)", f)
        if m:
            i, a, b = m.groups()
            drift["forbidden_path"].append((i.strip(), el(a), el(b)))
            continue
        m = re.match(r"drift_missing\(([^,]+),([^)]+)\)", f)
        if m:
            i, a = m.groups()
            drift["missing"].append((i.strip(), el(a)))
            continue
        m = re.match(r"malformed_role\(([^)]+)\)", f)
        if m:
            drift["malformed"].append(m.group(1).strip())
    return drift


def conformance(geometry: dict, mapping: dict, subject="conformance") -> dict:
    """Run one architecture MAPPING against a pattern GEOMETRY through the
    ee_pattern gate. Returns {in_pattern, phase, drift, n_bindings, n_edges}.

    geometry = {"roles": [role_id, ...],
                "invariants": [{"inv": required|forbidden|forbidden_transitive,
                                "relation": <edge type>, "source_role": r,
                                "target_role": r, "id": optional}, ...]}
    mapping  = {"bindings": [(element, role), ...],
                "edges":    [(relation, from_element, to_element), ...]}"""
    from ee_v2.map_gate.adapter import (EEPatternAdapter,
                                        EEPatternObservationAdapter)
    import re
    subj = re.sub(r"[^a-z0-9_]+", "_", subject.lower()).strip("_") or "conf"
    names = [e for e, _r in mapping["bindings"]]
    for _rel, s, t in mapping.get("edges", []):
        names += [s, t]
    el2atom, atom2el = _atomize(names)
    payload = _payload(subj, geometry, mapping, el2atom)
    with tempfile.TemporaryDirectory(prefix="patgate-") as td:
        comp = PrologTargetCompiler(load_domain_manifest(DOM))
        lat = MapV2Lattice(Path(td) / "l", compiler=comp,
                           construction_adapter=EEPatternAdapter(),
                           observation_adapter=EEPatternObservationAdapter())
        lat.create(subj, "ee_pattern")
        lat.declare_kappa(subj, "ee_conformance",
                          {"stays_in_pattern": "no forbidden + all required"})
        lat.compute(subj)
        lat.fill_construction(subj, payload)
        lat.attach_observation(subj, {"kind": "pattern_mapping_witness",
                                      "subject": subj})
        packet = lat.compile(subj)
    frontier = packet.get("frontier", [])
    return {"in_pattern": packet.get("griess_phase") == "ont",
            "phase": packet.get("griess_phase"),
            "drift": _parse_residue(frontier, atom2el),
            "n_bindings": len(mapping["bindings"]),
            "n_edges": len(mapping.get("edges", []))}


def geometry_from_kb(kb, roles: list, invariants: list) -> dict:
    """PROJECT a geometry from a certified pattern KB: the roles are concepts
    in the KB; the invariants are supplied as the structural constraints the
    KB certified (a later step mints these as ee_argument-style claims). v1
    validates that every named role + invariant endpoint is a real KB concept
    so a geometry can never reference an atom the KB never admitted."""
    known = set(kb.concepts)
    for r in roles:
        if r not in known:
            raise ValueError(f"role {r!r} is not a concept in the KB")
    for inv in invariants:
        if inv["inv"] not in _INV_KINDS:
            raise ValueError(f"bad invariant kind {inv['inv']!r}")
        for r in (inv["source_role"], inv["target_role"]):
            if r not in known:
                raise ValueError(f"invariant role {r!r} not in the KB")
    return {"roles": list(roles), "invariants": list(invariants)}


def drift_report(verdict: dict) -> str:
    """Human/LLM-readable rendering of a non-conformance verdict — the
    'you left the pattern HERE' message."""
    if verdict["in_pattern"]:
        return "IN PATTERN — the architecture conforms to the geometry."
    d = verdict["drift"]
    lines = ["DRIFTED OUT OF PATTERN:"]
    for inv, f, t in d["forbidden"]:
        lines.append(f"  forbidden edge present: {f} -> {t} (violates {inv})")
    for inv, f, t in d["forbidden_path"]:
        lines.append(f"  forbidden path present: {f} ~> {t} (violates {inv})")
    for inv, f in d["missing"]:
        lines.append(f"  required edge missing from {f} (violates {inv})")
    for r in d["malformed"]:
        lines.append(f"  binding onto undeclared role: {r}")
    return "\n".join(lines)


__all__ = ["conformance", "geometry_from_kb", "drift_report"]
