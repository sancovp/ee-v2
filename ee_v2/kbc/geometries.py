"""geometries.py — THE PATTERN GEOMETRY LIBRARY (Isaac 2026-08-11).

A curated set of canonical code/architecture pattern geometries — roles +
structural invariants — ready to feed the ee_pattern conformance gate. Each is
a checkable geometry (not prose): an LLM fills it with a real architecture and
`conformance()` proves in-pattern or names the drift. Source specs:
research fleet wf_cfad6a31 (Strategy, Layered, Hexagonal, Observer,
Repository, Pipes-and-Filters), stored as data in pattern_library.json.

    from ee_v2.kbc.geometries import geometry, list_patterns
    g = geometry("strategy")               # {roles, invariants, ...}
    conformance(g, my_architecture_mapping)

`transitive_deps=True` promotes forbidden `depends_on` invariants to
forbidden_transitive. COARSE: it promotes ALL of them, which is correct for
pure "no upward/outward dependency" constraints but WRONG for a pattern that
also has a direct-only skip-layer forbid (e.g. closed layered: "presentation
must not depend on domain DIRECTLY" is meant to be checked as a direct edge,
not transitively). Use per-pattern; the authored geometries default to direct
invariants, which the gate checks exactly as specified."""
from __future__ import annotations

import json
from pathlib import Path

_LIB = json.loads((Path(__file__).parent / "pattern_library.json").read_text())


def list_patterns() -> list:
    return sorted(_LIB)


def describe(name: str) -> dict:
    if name not in _LIB:
        raise KeyError(f"unknown pattern {name!r}; have {list_patterns()}")
    return _LIB[name]


def _atom(x: str) -> str:
    import re
    a = re.sub(r"[^a-zA-Z0-9_]", "_", str(x))
    a = (a[:1].lower() + a[1:]) if a else "x"
    return a if re.match(r"^[a-z]", a) else "x_" + a


def geometry(name: str, transitive_deps: bool = False) -> dict:
    """Return the {roles, invariants} geometry for `conformance()`. Ids and
    roles are atom-sanitized so any curated spec loads (e.g. a 'pipes-filters'
    slug can't leak a hyphen into a Prolog atom)."""
    p = describe(name)
    invs = []
    for iv in p["invariants"]:
        inv = {"id": _atom(iv["id"]), "inv": iv["inv"],
               "relation": _atom(iv["relation"]),
               "source_role": _atom(iv["source_role"]),
               "target_role": _atom(iv["target_role"])}
        if (transitive_deps and inv["inv"] == "forbidden"
                and inv["relation"] == "depends_on"):
            inv["inv"] = "forbidden_transitive"
        invs.append(inv)
    return {"roles": [_atom(r) for r in p["roles"]], "invariants": invs}


__all__ = ["list_patterns", "describe", "geometry"]
