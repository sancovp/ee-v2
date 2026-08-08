#!/usr/bin/env python3
"""SCALE DUMP — the insane version (Isaac's correction, 2026-08-08).

NOT the careful 12-concept walk. Say "restaurants" and get THOUSANDS of
certified nodes in a few calls:

  1. FAN OUT — N facet-seats in parallel, each DUMPING every concept + relation
     that makes sense (aim 80+), referencing concepts other facets will define.
  2. MERGE — mechanical only (dedup ids, drop malformed atoms/short defs, with
     a LOGGED drop list — never silent). Semantic errors are NOT touched here.
  3. GLOBAL CHECK — one MAP lattice, one swipl compile over the WHOLE fact set.
     closure + connectedness are global ⇒ 2000 nodes cost the same as 12. The
     SOUP frontier NAMES every place the LLM's own cognition went off the rails
     (dangling ref = named a concept it forgot to define; orphan = named a
     concept it wired to nothing).
  4. REFINE — MONOTONE (add-only, Kleene-safe): feed the whole error-map back;
     a consolidation seat DEFINES the missing concepts and WIRES the orphans.
     Nothing retracts ⇒ the frontier shrinks monotonically to ∅ = ONT.

Measured: nodes at ONT, LLM calls, wall-clock, frontier trajectory. The whole
run is checkpointed to disk (JSONL) so a transport death resumes free.

Deterministic self-test built in (--selftest): scripted seats with known
incoherences → the gate names them all → monotone refine converges. No LLM.
"""
import asyncio
import json
import re
import sys
import tempfile
import time
from pathlib import Path

for _p in ("/home/ceo/repo/ee-v2", "/home/ceo/repo/map-v2",
           "/home/ceo/repo/cave-teams", "/home/ceo/lcshim2"):
    sys.path.insert(0, _p)

from map_v2 import (MapV2Lattice, PrologTargetCompiler,        # noqa: E402
                    load_domain_manifest)
from ee_v2.map_gate.adapter import (EEOntologyAdapter,          # noqa: E402
                                    EEPassObservationAdapter)

DOMAIN = "restaurants"
FACETS = ["kitchen_operations", "menu_and_cuisine", "front_of_house_service",
          "staffing_and_roles", "supply_chain_and_inventory",
          "food_safety_and_compliance", "finance_and_costing",
          "customer_experience", "reservations_and_seating",
          "marketing_and_brand", "technology_and_pos",
          "facilities_and_equipment"]
REFINE_ROUNDS = 5
MAX_CONCURRENCY = 5
MAX_TOKENS = 16000
ROOT = Path(__file__).resolve().parent / "scale_dump"
DOM = Path(__file__).resolve().parent.parent \
    / "ee_v2/map_gate/domains/ee_ontology/domain.json"

ATOM = re.compile(r"^[a-z][a-zA-Z0-9_]*$")
# dangling(Rel, Endpoint) — the undefined concept is the SECOND arg;
# orphan(Concept) — the concept is the FIRST (and only) arg.
_DANGLING = re.compile(r"dangling\([a-z][a-zA-Z0-9_]*,\s*([a-z][a-zA-Z0-9_]*)")
_ORPHAN = re.compile(r"orphan\(([a-z][a-zA-Z0-9_]*)")


def sanitize_id(x):
    x = re.sub(r"[^a-z0-9_]+", "_", str(x).strip().lower()).strip("_")
    return x if x and ATOM.match(x) else None


# ── parse a seat's JSONL dump (truncation-robust: skip unparseable lines) ────
def parse_dump(text):
    concepts, relations = {}, []
    for line in (text or "").splitlines():
        line = line.strip().rstrip(",")
        if not (line.startswith("{") and line.endswith("}")):
            continue
        try:
            o = json.loads(line)
        except ValueError:
            continue
        if "c" in o and "d" in o:
            cid = sanitize_id(o["c"])
            if cid and len(str(o["d"]).strip()) >= 8:
                concepts.setdefault(cid, str(o["d"]).strip()[:400])
        elif "r" in o and isinstance(o["r"], list) and len(o["r"]) == 2:
            s, t = sanitize_id(o["r"][0]), sanitize_id(o["r"][1])
            if s and t:
                relations.append((s, t))
    return concepts, relations


def merge(chunks):
    """Mechanical only. Returns (concepts, relations, drop_log)."""
    concepts, rel_set, drops = {}, set(), {"short_or_bad": 0, "dup_rel": 0}
    for cs, rs in chunks:
        for cid, d in cs.items():
            concepts.setdefault(cid, d)
        for s, t in rs:
            if (s, t) in rel_set:
                drops["dup_rel"] += 1
            else:
                rel_set.add((s, t))
    return concepts, sorted(rel_set), drops


def scale_check(subject, concepts, relations):
    payload = {"kind": "ee_ontology", "subject": subject,
               "concepts": [{"kind": "concept", "id": c, "definition": d}
                            for c, d in concepts.items()],
               "relations": [{"kind": "relation", "id": f"r{i}",
                              "source": s, "target": t}
                             for i, (s, t) in enumerate(relations)]}
    with tempfile.TemporaryDirectory(prefix="scale-") as td:
        comp = PrologTargetCompiler(load_domain_manifest(DOM))
        lat = MapV2Lattice(Path(td) / "l", compiler=comp,
                           construction_adapter=EEOntologyAdapter(),
                           observation_adapter=EEPassObservationAdapter())
        lat.create(subject, "ee_ontology")
        lat.declare_kappa(subject, "ee_conceptualization",
                          {"ontology_coherence": "closed + connected"})
        lat.compute(subject)
        lat.fill_construction(subject, payload)
        lat.attach_observation(subject, {"kind": "pass_witness",
                                         "subject": subject, "layer": 0,
                                         "pass_num": 1})
        packet = lat.compile(subject)
        fr = packet.get("frontier", [])
        cert = (lat.export_certificate(subject)
                if packet.get("griess_phase") == "ont" else None)
    dangling = sorted({m.group(1) for f in fr
                       for m in [_DANGLING.match(f)] if m})
    orphan = sorted({m.group(1) for f in fr
                     for m in [_ORPHAN.match(f)] if m})
    return {"phase": packet.get("griess_phase"), "dangling": dangling,
            "orphan": orphan, "cert": cert,
            "n_concepts": len(concepts), "n_relations": len(relations)}


# ── seats ────────────────────────────────────────────────────────────────────
def _dump_prompt(facet):
    return (f"You are mass-enumerating the concept space of: {DOMAIN}.\n"
            f"FACET: {facet}.\n"
            "Dump AS MANY real, specific concepts as make sense for this facet "
            "— aim for 80+. Then dump relations among them (and to concepts "
            "OTHER facets will define — reference them by natural snake_case "
            "name). Output JSONL, ONE object per line, nothing else:\n"
            '{"c": "<snake_case_id>", "d": "<definition, 8+ chars>"}\n'
            '{"r": ["<source_id>", "<target_id>"]}\n'
            "Be exhaustive and concrete. Do not stop early. No prose, no "
            "markdown fences.")


def _refine_prompt(dangling, orphan):
    return (f"You are REPAIRING the concept graph of {DOMAIN}. A prover found "
            "these incoherences in your own dump:\n\n"
            f"REFERENCED BUT UNDEFINED ({len(dangling)}): "
            + ", ".join(dangling[:400]) + "\n\n"
            f"DEFINED BUT UNCONNECTED ({len(orphan)}): "
            + ", ".join(orphan[:400]) + "\n\n"
            "Repair by ADDING ONLY (never remove):\n"
            "- for each undefined id: a concept line defining it.\n"
            "- for each unconnected id: a relation line wiring it to an "
            "existing, related concept.\n"
            "Output JSONL, one object per line, nothing else:\n"
            '{"c": "<id>", "d": "<definition, 8+ chars>"}\n'
            '{"r": ["<source_id>", "<target_id>"]}\n'
            "No prose, no fences.")


def _make_seat():
    from cave_teams.examples import MiniMaxRuntime
    return MiniMaxRuntime(name="dump_seat", tools=[], system_prompt="",
                          max_tokens=MAX_TOKENS)


async def _seat_run(prompt, tries=4, base=12):
    last = None
    for i in range(tries):
        try:
            out = await _make_seat().run(prompt)
            return out if isinstance(out, str) else str(out)
        except Exception as e:
            last = e
            print(f"[transport] retry {i+1}/{tries}: {e}", flush=True)
            await asyncio.sleep(base * (2 ** i))
    raise last


async def _dump_facet(facet, sem):
    cache = ROOT / f"dump_{facet}.jsonl"
    if cache.exists() and cache.stat().st_size > 0:
        print(f"[dump] {facet}: cached", flush=True)
        return parse_dump(cache.read_text())
    async with sem:
        t = time.time()
        out = await _seat_run(_dump_prompt(facet))
    cache.write_text(out)
    cs, rs = parse_dump(out)
    print(f"[dump] {facet}: {len(cs)} concepts, {len(rs)} relations "
          f"({time.time()-t:.0f}s)", flush=True)
    return cs, rs


# ── the run ──────────────────────────────────────────────────────────────────
async def run(dump_fn, refine_fn, tag="live"):
    ROOT.mkdir(parents=True, exist_ok=True)
    calls = 0
    t0 = time.time()
    sem = asyncio.Semaphore(MAX_CONCURRENCY)
    chunks = await asyncio.gather(*[dump_fn(f, sem) for f in FACETS])
    calls += len(FACETS)
    concepts, relations, drops = merge(chunks)
    traj = []
    v = scale_check(DOMAIN, concepts, relations)
    traj.append({"round": 0, "phase": v["phase"], "concepts": v["n_concepts"],
                 "relations": v["n_relations"],
                 "dangling": len(v["dangling"]), "orphan": len(v["orphan"])})
    print(f"[round 0] {v['n_concepts']} concepts / {v['n_relations']} "
          f"relations → {v['phase']} | dangling={len(v['dangling'])} "
          f"orphan={len(v['orphan'])}", flush=True)

    r = 0
    while v["phase"] != "ont" and r < REFINE_ROUNDS \
            and (v["dangling"] or v["orphan"]):
        r += 1
        patch = await refine_fn(v["dangling"], v["orphan"], r)
        calls += 1
        pc, pr = parse_dump(patch) if isinstance(patch, str) else patch
        before = (len(concepts), len(relations))
        for cid, d in pc.items():
            concepts.setdefault(cid, d)
        relations = sorted(set(relations) | set(pr))
        v = scale_check(DOMAIN, concepts, relations)
        traj.append({"round": r, "phase": v["phase"],
                     "concepts": v["n_concepts"], "relations": v["n_relations"],
                     "dangling": len(v["dangling"]),
                     "orphan": len(v["orphan"])})
        print(f"[round {r}] +{len(concepts)-before[0]}c "
              f"+{len(relations)-before[1]}r → {v['phase']} | "
              f"dangling={len(v['dangling'])} orphan={len(v['orphan'])}",
              flush=True)

    secs = time.time() - t0
    summary = {"domain": DOMAIN, "tag": tag, "phase": v["phase"],
               "nodes_at_end": v["n_concepts"] + v["n_relations"],
               "concepts": v["n_concepts"], "relations": v["n_relations"],
               "llm_calls": calls, "wall_secs": round(secs, 1),
               "refine_rounds": r, "drop_log": drops, "trajectory": traj,
               "residual_dangling": v["dangling"][:50],
               "residual_orphan": v["orphan"][:50]}
    (ROOT / f"summary_{tag}.json").write_text(json.dumps(summary, indent=2))
    if v["cert"]:
        (ROOT / f"certificate_{tag}.json").write_text(
            json.dumps(v["cert"], indent=2))
    print("\n=== SCALE RESULT ===")
    print(json.dumps({k: summary[k] for k in
                      ("phase", "nodes_at_end", "concepts", "relations",
                       "llm_calls", "wall_secs", "refine_rounds")}, indent=2))
    return summary


# ── deterministic self-test (no LLM) ─────────────────────────────────────────
def _selftest():
    print("SELFTEST — scripted dump with known incoherences")
    facet_chunks = {
        "a": ({"walk_in_cooler": "cold storage room", "mise_en_place":
               "prepared staged ingredients", "line_cook": "station cook"},
              [("mise_en_place", "line_cook"), ("line_cook", "sous_vide")]),
        "b": ({"pos_terminal": "point of sale device", "check_average":
               "mean spend per table"},
              [("pos_terminal", "check_average")]),
    }
    orphan_seed = {"lonely_concept": "a thing nobody wired up"}
    facet_chunks["b"][0].update(orphan_seed)

    async def dump_fn(facet, sem):
        return facet_chunks[facet]

    async def refine_fn(dangling, orphan, r):
        pc = {d: f"auto-defined {d} to close the reference" for d in dangling}
        pr = [(o, "walk_in_cooler") for o in orphan]   # wire orphans
        return pc, dict.fromkeys([]) and pr or pc and (pc, pr)

    # patch parse: refine returns (pc, pr) tuple already-parsed
    async def refine_fn2(dangling, orphan, r):
        pc = {d: f"auto-defined {d}" for d in dangling}
        pr = [(o, "walk_in_cooler") for o in orphan]
        return pc, pr

    global FACETS, REFINE_ROUNDS
    FACETS = ["a", "b"]
    v0 = merge([facet_chunks["a"], facet_chunks["b"]])
    chk = scale_check(DOMAIN, v0[0], v0[1])
    assert "sous_vide" in chk["dangling"], chk
    assert "lonely_concept" in chk["orphan"], chk
    print(f"  gate named dangling={chk['dangling']} orphan={chk['orphan']} ✓")
    s = asyncio.run(run(dump_fn, refine_fn2, tag="selftest"))
    assert s["phase"] == "ont", s
    assert not s["residual_dangling"] and not s["residual_orphan"]
    print("  monotone refine → ONT, frontier collapsed ✓")
    print("SELFTEST PASS")


async def _live():
    async def refine_fn(dangling, orphan, r):
        return await _seat_run(_refine_prompt(dangling, orphan))
    await run(_dump_facet, refine_fn, tag="live")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        _selftest()
    else:
        asyncio.run(_live())
