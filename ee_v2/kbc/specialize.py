"""specialize.py — THE SPECIALIZATION TOWER (Isaac, 2026-08-09/10):
"continually biject new agent code and tool code out of the graph into the
codebase and run it... each persona defines one level of granularity deeper
than the last... eventually they all become the same — every physical-thing
compiler comes from the atom compiler. The whole game is making the machine
repeatedly do that process."

THE BIJECTION (graph → code → graph):
  * mint_persona(kb, region, out_dir) — a certified region EMITS an agent:
    personas/<region>/persona.md (system prompt = its identity + its relative
    root, the certified territory) + loadout.json (its tool names) — CODE in
    the one-law sense (instructions; the connectors already exist). Returns a
    seat factory speaking as that persona.
  * deepen(kb, region, seat) — the persona defines ONE LEVEL DEEPER: expands
    frontier atoms of its own cone; harvests accrete back into the KB
    (proof-checked, worklist-minted). code → graph.
  * specialization_round(...) — mint + deepen across regions, teach the
    brain's graph on admitted growth. Repeat = the tower.

THE CONVERGENCE READOUT (the "they all become the same" conjecture, measured):
  basis(kb, regions) — the atoms shared by ≥k regions' cones. As towers
  descend, cones intersect in the same primitives; basis overlap RISING per
  round = the towers converging toward the one compiler at the next order.
  A readout, never a gate (§R discipline).
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

from ._paths import ensure_deps
ensure_deps()

from .kb_tool import relative_root, root_context                 # noqa: E402
from .compiler import compile as kbc_compile                     # noqa: E402
from .projector import call_number                               # noqa: E402

PERSONA_TOOLS = ["kb_work", "kb_drain", "kb_root", "kb_expand",
                 "brain_grow", "brain_ask"]


def mint_persona(kb, region: str, out_dir) -> dict:
    """GRAPH → CODE: emit the region's specialist as a persona dir."""
    d = Path(out_dir) / "personas" / region
    d.mkdir(parents=True, exist_ok=True)
    cn, cone, _ = call_number(kb, region)
    ground = root_context(kb, region, direction="deps", max_nodes=40)
    persona = (
        f"# {region} SPECIALIST\n\n"
        f"CALL NUMBER: `{cn}`\n\n"
        f"You are the specialist for `{region}` in the {kb.subject!r} "
        "knowledge system. Your CERTIFIED TERRITORY (the relative root — "
        "everything your concept bundles from):\n\n"
        f"{ground}\n\n"
        "YOUR JOB: define this territory ONE LEVEL OF GRANULARITY DEEPER "
        "than it currently is. Name the parts inside the parts. Every claim "
        "you emit is proof-checked; incoherence returns as named residue — "
        "repair it exactly. You never invent formats: emit exactly the "
        "JSONL construction schema you are given.\n")
    (d / "persona.md").write_text(persona, encoding="utf-8")
    (d / "loadout.json").write_text(json.dumps(
        {"region": region, "call_number": cn, "tools": PERSONA_TOOLS,
         "cone_size": len(cone)}, indent=2), encoding="utf-8")
    return {"region": region, "dir": str(d), "persona": persona}


def persona_seat_factory(minted: dict, base_seat_factory):
    """The persona speaks: same runtime, its emitted identity as the system
    prompt (the bijection's run-side — the code the graph emitted, running)."""
    def factory():
        return base_seat_factory(minted["region"], minted["persona"])
    return factory


def project_personas(kb, out_dir, min_degree: int = 3) -> dict:
    """THE STAFF IS A PROJECTION, NOT A DECISION (Isaac 2026-08-10): every
    region whose substance qualifies (degree >= min_degree) gets its persona
    minted/refreshed — deterministic, zero seats, total. The org chart is
    derived state; existence is free, RUNNING is what the doors/budget
    schedule. Returns {region: persona_dir}; stale personas are re-minted in
    place (the file follows the graph)."""
    deg = Counter()
    for s_, t_ in kb.relations:
        deg[s_] += 1
        deg[t_] += 1
    staff = {}
    for c in sorted(kb.concepts):
        if deg[c] >= min_degree:
            staff[c] = mint_persona(kb, c, out_dir)["dir"]
    return staff


def frontier_atoms(kb, region: str, k: int = 3) -> list:
    """Where the persona digs: the thinnest atoms of its own cone — named
    parts with the least structure under them (the granularity frontier)."""
    deg = Counter()
    for s, t in kb.relations:
        deg[s] += 1
        deg[t] += 1
    cone = [c for c, _d, _l, _dep in relative_root(kb, region,
                                                   direction="deps",
                                                   max_nodes=60)]
    cone.append(region)
    return sorted(cone, key=lambda c: deg[c])[:k]


async def deepen(kb, region: str, seat_factory, k: int = 2) -> dict:
    """CODE → GRAPH: the persona expands its frontier one level deeper."""
    before = (len(kb.concepts), len(kb.relations))
    targets = frontier_atoms(kb, region, k)
    phases = []
    for atom in targets:
        v = await kbc_compile(kb, atom, "expand", seat_factory,
                              lib=f"deep_{region[:20]}")
        phases.append(v["phase"])
    return {"region": region, "targets": targets, "phases": phases,
            "new_concepts": len(kb.concepts) - before[0],
            "new_relations": len(kb.relations) - before[1]}


def basis(kb, regions: list, k: int = 2) -> dict:
    """THE CONVERGENCE READOUT: atoms shared by >= k regions' cones."""
    membership = Counter()
    for r in regions:
        cone = {c for c, _d, _l, _dep in relative_root(kb, r,
                direction="deps", max_nodes=120)}
        cone.add(r)
        for c in cone:
            membership[c] += 1
    shared = sorted(c for c, n in membership.items() if n >= k)
    total = len(membership)
    return {"shared_atoms": shared, "shared": len(shared),
            "union": total,
            "overlap": round(len(shared) / total, 3) if total else 0.0}


async def specialization_round(kb, regions: list, base_seat_factory,
                               out_dir, brain=None, log=print) -> dict:
    """ONE TURN OF THE GAME: mint every region's specialist (graph→code),
    each deepens its territory (code→graph), the basis is re-read, admitted
    growth teaches the brain's graph. Repeat = the tower; the readout says
    when the towers meet."""
    b0 = basis(kb, regions)
    reports = []
    for region in regions:
        minted = mint_persona(kb, region, out_dir)
        seat = persona_seat_factory(minted, base_seat_factory)
        r = await deepen(kb, region, seat)
        reports.append(r)
        log(f"[deepen] {region}: +{r['new_concepts']}c/"
            f"+{r['new_relations']}r into {r['targets']} ({r['phases']})")
        if brain is not None and r["new_concepts"] > 0:
            brain.graph.teach({region: 1.0}, {region: 10.0})
    kb.save()
    b1 = basis(kb, regions)
    log(f"[basis] overlap {b0['overlap']} → {b1['overlap']} "
        f"({b1['shared']}/{b1['union']} shared atoms)")
    out = {"rounds": reports, "basis_before": b0, "basis_after": b1}
    (Path(out_dir) / "round_report.json").write_text(
        json.dumps(out, indent=2), encoding="utf-8")
    return out


__all__ = ["mint_persona", "persona_seat_factory", "deepen", "basis",
           "specialization_round", "frontier_atoms", "project_personas"]
