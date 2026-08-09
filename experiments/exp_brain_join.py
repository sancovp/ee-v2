#!/usr/bin/env python3
"""THE BRAIN JOIN — first end-to-end run of §19/§19b (Isaac: "lets fucking do it").

One graph, three layers, one loop:

  1. TISSUE   — two certified KB regions project as brain-tissue dirs
                (kbc.project_brain_tissue = brain-agent's from_dir format).
  2. FIRE     — a kuzu ActivationGraph (brain-agent neuro) holds regions as
                refs + their cones as concepts; the QUERY becomes stimulus;
                `disclose()` picks which neurons fire. THE SYNTHESIZER NEVER
                SELECTS — attention is numeric (§19b / rule-05).
  3. NEURONS  — each fired region = one LLM seat over its tissue, rendered
                by brain-agent's Membrane (salience-disclosed, budget-bounded,
                honest boxes). Each answers AND emits a typed construction.
  4. ADMIT    — one shared MAP lattice: root expanded into the neuron nodes;
                each construction certifies (or its residue retries, bounded).
  5. SYNTH    — `lattice.combine("final", sources)` — an uncertified neuron
                CANNOT enter; then one synthesizer seat writes the FINAL prose
                from the certified payloads only.
  6. TEACH    — admitted outcomes (not self-scores) teach the graph: amplitude
                toward 1.0 for certified regions + hebbian between co-fired
                certified regions. THE RUNG-4 FIX: the prover is the teacher.

--selftest runs the whole loop with scripted seats (no LLM, real swipl+kuzu).
Live mode uses MiniMax seats on the restaurant KB.
"""
import asyncio
import json
import re
import sys
import time
from collections import Counter
from pathlib import Path

for _p in ("/home/ceo/repo/ee-v2", "/home/ceo/repo/map-v2",
           "/home/ceo/repo/cave-teams", "/home/ceo/repo/brain-agent",
           "/home/ceo/lcshim2"):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from ee_v2.kbc import KB, parse_jsonl, relative_root                # noqa: E402
from ee_v2.kbc.projector import project_brain_tissue                # noqa: E402
from ee_v2.map_gate.adapter import (EEOntologyAdapter,              # noqa: E402
                                    EEPassObservationAdapter)
from map_v2 import (MapV2Lattice, PrologTargetCompiler,             # noqa: E402
                    load_domain_manifest)
from brain_agent.neuro import ActivationGraph, Membrane             # noqa: E402

DOM = Path("/home/ceo/repo/ee-v2/ee_v2/map_gate/domains/ee_ontology/domain.json")
ROOT = Path(__file__).resolve().parent / "brain_join"
QUERY = ("how do I keep inventory accurate while staying ready for the "
         "health inspection?")
MAX_ATTEMPTS = 3


# ── 0. the KB (restaurants, lib-tagged, rebuilt from the cached dumps) ───────
def load_kb(tmp) -> KB:
    import glob
    kb = KB("restaurants", Path(tmp) / "kb")
    for f in sorted(glob.glob(str(Path(__file__).parent /
                                  "scale_dump/dump_*.jsonl"))):
        facet = f.split("dump_")[1].split(".jsonl")[0]
        cs, rs = parse_jsonl(open(f).read())
        for c, d in cs.items():
            kb.add_concept(c, d, lib=facet)
        for s, t in rs:
            kb.add_relation(s, t)
    prev = KB("restaurants", Path(__file__).parent / "kb_restaurants").load()
    for c, d in prev.concepts.items():
        kb.add_concept(c, d, lib="defined")
    for s, t in prev.relations:
        kb.add_relation(s, t)
    return kb


def pick_regions(kb, stim) -> list:
    """Two gyri from different libs: among the lib's top-degree concepts,
    the one whose cone overlaps the stimulus most (which gyri this demo
    brain HAS — tissue construction, not per-round attention)."""
    deg = Counter()
    for s, t in kb.relations:
        deg[s] += 1
        deg[t] += 1
    def overlap(c):
        cone = {x for x, _, _, _ in relative_root(kb, c,
                direction="both", max_nodes=60)}
        return len(cone & set(stim))
    cands = sorted(kb.concepts, key=lambda c: -deg[c])[:120]
    ranked = sorted(cands, key=lambda c: (-overlap(c), -deg[c]))
    first = ranked[0]
    second = next(c for c in ranked[1:]
                  if kb.lib.get(c) != kb.lib.get(first))
    return [first, second]


# ── 2. the graph: regions as refs, cones as concepts, query as stimulus ──────
def build_graph(kb, regions, path) -> ActivationGraph:
    """Regions as refs; their cones as concepts wired to the ref; PLUS the
    KB's real relations among graph members — the web the activation spreads
    through (the graph mirrors the KB, salience layer over meaning layer)."""
    g = ActivationGraph(path=str(path), reset=True)
    members = set()
    for r in regions:
        g.add(r, kind="ref", amplitude=0.5)
        for cid, _d, _l, depth in relative_root(kb, r, direction="both",
                                                max_nodes=60):
            g.add(cid, kind="concept", amplitude=0.3)
            g.wire(cid, r, weight=max(0.2, 0.9 - 0.2 * depth))
            members.add(cid)
    for s, t in kb.relations:                 # the KB's own edges, mirrored
        if s in members and t in members:
            g.wire(s, t, weight=0.6)
            g.wire(t, s, weight=0.4)
    return g


def stimulus_from_query(kb, query) -> dict:
    toks = set(re.findall(r"[a-z]+", query.lower()))
    stim = {}
    for c in kb.concepts:
        parts = set(c.split("_"))
        hit = len(parts & toks)
        if hit:
            stim[c] = min(1.0, 0.5 + 0.25 * hit)
    return dict(sorted(stim.items(), key=lambda x: -x[1])[:12])


# ── 3. a neuron: Membrane-rendered tissue + the task ─────────────────────────
def membrane_view(tissue_dir: Path, fired: set, budget=6000) -> str:
    store = {}
    for f in sorted(Path(tissue_dir).glob("*.md")):
        body = f.read_text(encoding="utf-8")
        summary = body.splitlines()[-1][:90] if body.splitlines() else ""
        store[f.stem] = (summary, body)
    m = Membrane(store)
    m.set_firing(fired or set(store))
    return m.render(char_budget=budget)


def neuron_prompt(region, tissue_view, query) -> str:
    return (f"You are the {region} NEURON of a restaurant brain. Your "
            f"territory (certified knowledge, salience-rendered):\n\n"
            f"{tissue_view}\n\nQUERY: {query}\n\n"
            "Reply in TWO parts:\n"
            "ANSWER: <your territory's contribution, <=120 words>\n"
            "Then the typed construction — the concepts+relations your answer "
            "USED (from your territory; you may add concepts your answer "
            "needs, with definitions). JSONL, one per line:\n"
            '{"c": "<snake_case_id>", "d": "<definition, 8+ chars>"}\n'
            '{"r": ["<source_id>", "<target_id>"]}\n'
            "LAWS (machine-proven): every relation endpoint must be a "
            "declared concept; every concept must touch >=1 relation.")


def synth_prompt(query, certified) -> str:
    blocks = []
    for region, payload in certified.items():
        cs = "; ".join(f"{c['id']}: {c['definition'][:60]}"
                       for c in payload["concepts"][:10])
        blocks.append(f"[{region}] certified concepts: {cs}")
    return ("You are the SYNTHESIZER. Compose ONE unified answer to the "
            f"query from the CERTIFIED neuron results only.\n\nQUERY: {query}"
            "\n\n" + "\n".join(blocks) +
            "\n\nFINAL (<=150 words, integrate both territories):")


# ── the run ──────────────────────────────────────────────────────────────────
async def run(seat_factory, tmp, log=print) -> dict:
    t0 = time.time()
    kb = load_kb(tmp)
    stim = stimulus_from_query(kb, QUERY)
    regions = pick_regions(kb, stim)
    log(f"[tissue] regions (gyri): {regions}")
    tissue = project_brain_tissue(kb, regions, Path(tmp) / "tissue")

    g = build_graph(kb, regions, Path(tmp) / "neurodb")
    fired = [n for n, _p in g.disclose(stim, budget=2, kind="ref")]
    log(f"[fire] stimulus={list(stim)[:6]}… → fired neurons: {fired}")
    assert fired, "no neuron fired — stimulus missed the graph"

    # one shared lattice: root expanded into the fired neurons
    compiler = PrologTargetCompiler(load_domain_manifest(DOM))
    lat = MapV2Lattice(Path(tmp) / "lattice", compiler=compiler,
                      construction_adapter=EEOntologyAdapter(),
                      observation_adapter=EEPassObservationAdapter())
    lat.create("kitchen_brain", "ee_ontology")
    res = lat.expand("kitchen_brain", [f"n_{r[:24]}" for r in fired])
    node_of = dict(zip(fired, res["children"]))   # parent.child names

    certified, answers, attempts_log, filled = {}, {}, {}, {}
    for region in fired:
        node = node_of[region]
        lat.declare_kappa(node, "ee_conceptualization",
                          {"ontology_coherence": "closed + connected"})
        lat.compute(node)
        view = membrane_view(tissue[region],
                             {c for c in stim if c in kb.concepts})
        residue = None
        for attempt in range(1, MAX_ATTEMPTS + 1):
            prompt = neuron_prompt(region, view, QUERY)
            if residue:
                prompt += ("\n\nPROOF RESIDUE — your previous construction "
                           f"failed: {residue}. Fix exactly these; re-emit "
                           "BOTH parts.")
            out = seat_factory and (seat_factory(region).run(prompt))
            out = await out if asyncio.iscoroutine(out) else out
            answers[region] = out.split("ANSWER:", 1)[-1].split("{", 1)[0].strip()
            cs, rs = parse_jsonl(out)
            payload = {"kind": "ee_ontology", "subject": "kitchen_brain",
                       "concepts": [{"kind": "concept", "id": c,
                                     "definition": d} for c, d in cs.items()],
                       "relations": [{"kind": "relation", "id": f"r{i}",
                                      "source": s, "target": t}
                                     for i, (s, t) in enumerate(rs)]}
            try:
                if not filled.get(node):
                    lat.fill_construction(node, payload)
                    filled[node] = True
                else:
                    lat.retry(node)                # soup → repairing/derive
                    lat.compute(node)              # derive → compute
                    lat.revise_construction(node, payload)
            except Exception as e:
                residue = f"psc: {e}"
                attempts_log.setdefault(region, []).append("psc_reject")
                continue
            lat.attach_observation(node, {"kind": "pass_witness",
                                          "subject": "kitchen_brain",
                                          "layer": 0, "pass_num": 1})
            packet = lat.compile(node)
            if packet.get("griess_phase") == "ont":
                certified[region] = payload
                attempts_log.setdefault(region, []).append("ONT")
                log(f"[admit] {region}: ONT on attempt {attempt} "
                    f"({len(cs)}c/{len(rs)}r)")
                break
            residue = [f for f in packet.get("frontier", [])
                       if "dangling" in f or "orphan" in f]
            attempts_log.setdefault(region, []).append(
                f"soup:{len(residue)}")
            log(f"[residue] {region} attempt {attempt}: {residue[:4]}")

    assert len(certified) >= 2, f"need >=2 certified neurons for combine; " \
                                f"got {list(certified)}"
    # COMBINE with staleness repair: later fills change the shared workspace,
    # staling earlier certificates. combine() names exactly the stale nodes;
    # each repairs through the sanctioned ladder (retry stale-ont → compute →
    # revise with the SAME certified payload → witness → compile) and combine
    # is retried — the prover's own rejection drives the fix, as everywhere.
    from map_v2 import MapV2Error

    def _refresh(node, payload):
        lat.retry(node)
        lat.compute(node)
        lat.revise_construction(node, payload)
        lat.attach_observation(node, {"kind": "pass_witness",
                                      "subject": "kitchen_brain",
                                      "layer": 0, "pass_num": 1})
        packet = lat.compile(node)
        assert packet.get("griess_phase") == "ont", f"refresh lost ONT: {node}"

    region_of = {node_of[r]: r for r in certified}
    combined = None
    for _ in range(3):
        try:
            combined = lat.combine("final",
                                   [node_of[r] for r in certified])
            break
        except MapV2Error as e:
            msg = str(e)
            if "combine_rejected" not in msg:
                raise
            for reason in json.loads(msg)["reasons"]:
                _refresh(reason["node"],
                         certified[region_of[reason["node"]]])
    assert combined is not None, "combine did not converge after repairs"
    log(f"[synth] combine() accepted {len(certified)} certified sources → "
        f"status={combined.get('status', 'combined')}")

    out = seat_factory("synthesizer").run(synth_prompt(QUERY, certified))
    final = await out if asyncio.iscoroutine(out) else out

    # 6. TEACH — the prover is the teacher (rung-4): admitted → amplitude up
    g.teach(stim, {r: 10.0 for r in certified})
    rs = list(certified)
    for i in range(len(rs) - 1):
        g.hebbian(rs[i], rs[i + 1])
    log("[teach] admitted regions amplified + hebbian co-fire wired "
        "(the prover taught the graph)")

    report = {"query": QUERY, "regions": regions, "fired": fired,
              "attempts": attempts_log,
              "certified": {r: {"concepts": len(p["concepts"]),
                                "relations": len(p["relations"])}
                            for r, p in certified.items()},
              "combined": True, "final_answer": final,
              "neuron_answers": answers,
              "secs": round(time.time() - t0, 1)}
    ROOT.mkdir(parents=True, exist_ok=True)
    (ROOT / "report.json").write_text(json.dumps(report, indent=2))
    return report


# ── seats ────────────────────────────────────────────────────────────────────
def live_seat_factory(name):
    from cave_teams.examples import MiniMaxRuntime
    return MiniMaxRuntime(name=f"neuron_{name}"[:24], tools=[],
                          system_prompt="", max_tokens=6000)


class ScriptedSeat:
    def __init__(self, name):
        self.name = name

    def run(self, prompt):
        if "SYNTHESIZER" in prompt:
            return "Both territories agree: track stock and log temperatures."
        good = "\n".join([
            json.dumps({"c": f"{self.name[:8]}_core",
                        "d": "the core concept of this territory"}),
            json.dumps({"c": "shared_log", "d": "the record both keep"}),
            json.dumps({"r": [f"{self.name[:8]}_core", "shared_log"]})])
        if "PROOF RESIDUE" in prompt:
            return f"ANSWER: corrected contribution.\n{good}"
        # first attempt: one dangling ref → forces one residue round
        bad = good + "\n" + json.dumps({"r": [f"{self.name[:8]}_core",
                                              "ghost"]})
        return f"ANSWER: my territory's contribution.\n{bad}"


async def selftest():
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        r = await run(lambda n: ScriptedSeat(n), d)
    assert r["combined"] and len(r["certified"]) == 2
    assert all("soup:1" in a and "ONT" in a for a in
               r["attempts"].values()), r["attempts"]
    print("SELFTEST PASS — fire→neurons→residue→admit→combine→teach, "
          "no LLM, real kuzu + swipl.")


async def live():
    import tempfile
    with tempfile.TemporaryDirectory() as d:
        r = await run(live_seat_factory, d)
    print(json.dumps({k: r[k] for k in ("fired", "attempts", "certified",
                                        "secs")}, indent=2))
    print("\nFINAL:", r["final_answer"][:600])


if __name__ == "__main__":
    asyncio.run(selftest() if "--selftest" in sys.argv else live())
