"""brain.py — THE DURABLE BRAIN: grow-gyri + ask + the SES tower
(Isaac's picks, 2026-08-09: C then B).

A `KbcBrain` is a persistent organism over a KB:

    brain/
      tissue/<region>/          gyri — brain-agent from_dir chunk format
      neurodb (+.wal)           the kuzu ActivationGraph (salience, persists)
      asks/<slug>/lattice/      one MAP lattice per ask (proof, persists)
      asks/<slug>/report.json

THE OPERATIONS:
  * grow(atom)  — "open the brain and make yourself more gyri for xyz":
    if the atom is thin, expand it in the KB first (compile op); project its
    region as tissue; wire it into the activation graph. It is now fireable.
    Growth is proof-gated: expansion accretes only prover-checked structure.
  * ask(query) — the §19b loop over WHATEVER gyri exist: stimulus → the graph
    fires neurons numerically (never an agent's choice) → each fired region =
    one seat over its Membrane-rendered tissue → typed constructions admitted
    through one shared lattice (full repair ladder) → combine() →
    **THE SES TOWER (option B): promote → reify → the synthesizer emits the
    CROSS-TERRITORY construction (concepts of both + the relations that join
    them) → certified at SES depth 1** — the combination itself is PROVEN,
    not merely source-validated → teach: the prover teaches the graph
    (admitted → amplitude + hebbian; rung-4).

Deterministic-testable: every seat is injected; kuzu + swipl are real.
"""
from __future__ import annotations

import asyncio
import json
import re
import time
from collections import Counter
from pathlib import Path

from ._paths import ensure_deps
ensure_deps()

from map_v2 import (MapV2Lattice, MapV2Error, PrologTargetCompiler,  # noqa: E402
                    load_domain_manifest)

from .kb_tool import relative_root                                   # noqa: E402
from .compiler import compile as kbc_compile                         # noqa: E402
from .projector import project_brain_tissue                          # noqa: E402

DOM = Path(__file__).resolve().parent.parent \
    / "map_gate/domains/ee_ontology/domain.json"
MAX_ATTEMPTS = 3


def _slug(x: str) -> str:
    return re.sub(r"[^a-z0-9_]+", "_", x.strip().lower()).strip("_")[:48]


async def _run_seat(seat, prompt):
    out = seat.run(prompt)
    if asyncio.iscoroutine(out) or asyncio.isfuture(out):
        out = await out
    return out if isinstance(out, str) else str(out)


def _parse_two_part(out):
    """ANSWER: prose + JSONL construction lines."""
    from .kb_tool import parse_jsonl
    answer = out.split("ANSWER:", 1)[-1].split("{", 1)[0].strip()
    cs, rs = parse_jsonl(out)
    return answer, cs, rs


def _payload(subject, cs, rs):
    return {"kind": "ee_ontology", "subject": subject,
            "concepts": [{"kind": "concept", "id": c, "definition": d}
                         for c, d in cs.items()],
            "relations": [{"kind": "relation", "id": f"r{i}",
                           "source": s, "target": t}
                          for i, (s, t) in enumerate(rs)]}


class KbcBrain:
    def __init__(self, kb, root):
        from brain_agent.neuro import ActivationGraph
        self.kb = kb
        self.root = Path(root)
        (self.root / "tissue").mkdir(parents=True, exist_ok=True)
        (self.root / "asks").mkdir(exist_ok=True)
        self.graph = ActivationGraph(path=str(self.root / "neurodb"))

    # ── anatomy ──────────────────────────────────────────────────────────────
    def regions(self) -> list:
        return sorted(d.name for d in (self.root / "tissue").iterdir()
                      if d.is_dir())

    def _wire_region(self, region):
        g = self.graph
        g.add(region, kind="ref", amplitude=0.5)
        refs = set(self.regions()) | {region}
        members = set()
        for cid, _d, _l, depth in relative_root(self.kb, region,
                                                direction="both",
                                                max_nodes=60):
            if cid not in refs:            # never demote another gyrus's ref
                g.add(cid, kind="concept", amplitude=0.3)
            g.wire(cid, region, weight=max(0.2, 0.9 - 0.2 * depth))
            members.add(cid)
        for s, t in self.kb.relations:        # mirror the KB's own edges
            if s in members and t in members:
                g.wire(s, t, weight=0.6)
                g.wire(t, s, weight=0.4)

    async def grow(self, atom, seat_factory) -> dict:
        """GROW A GYRUS. Thin atom → expand in the KB first (proof-gated
        accretion); project tissue; wire the graph. Idempotent-ish: regrowing
        refreshes tissue + wiring."""
        atom = _slug(atom)
        report = {"atom": atom, "expanded": False}
        if atom not in self.kb.concepts:
            raise ValueError(f"{atom!r} is not a concept in the KB — dump or "
                             "define it first")
        deg = sum(1 for s, t in self.kb.relations if atom in (s, t))
        if deg < 3:                            # thin → open the region first
            v = await kbc_compile(self.kb, atom, "expand",
                                  lambda: seat_factory(f"expand_{atom}"))
            report.update(expanded=True, added_concepts=v["added_concepts"],
                          added_relations=v["added_relations"],
                          phase=v["phase"])
        project_brain_tissue(self.kb, [atom], self.root / "tissue")
        self._wire_region(atom)
        report["regions_now"] = self.regions()
        return report

    # ── cognition ────────────────────────────────────────────────────────────
    _STOP = frozenset("the a an of for to in on at is are was do does done "
                      "how what why my i me we you it this that while with "
                      "and or not no yes stay staying keep keeping get "
                      "ready".split())

    def _stimulus(self, query) -> dict:
        toks = set(re.findall(r"[a-z]+", query.lower())) - self._STOP
        stim = {}
        for c in self.kb.concepts:
            hit = len(set(c.split("_")) & toks)
            if hit:
                stim[c] = min(1.0, 0.5 + 0.25 * hit)
        stim = dict(sorted(stim.items(), key=lambda x: -x[1])[:12])
        # gyri are first-class addressable: a region whose NAME matches the
        # query always enters the stimulus (never lost to the cap)
        for r in self.regions():
            hit = len(set(r.split("_")) & toks)
            if hit:
                stim[r] = max(stim.get(r, 0.0), min(1.0, 0.5 + 0.25 * hit))
        return stim

    def _membrane_view(self, region, fired, budget=6000) -> str:
        from brain_agent.neuro import Membrane
        store = {}
        for f in sorted((self.root / "tissue" / region).glob("*.md")):
            body = f.read_text(encoding="utf-8")
            summary = (body.splitlines() or [""])[-1][:90]
            store[f.stem] = (summary, body)
        m = Membrane(store)
        m.set_firing(fired or set(store))
        return m.render(char_budget=budget)

    def _neuron_prompt(self, region, view, query):
        return (f"You are the {region} NEURON of a brain over "
                f"{self.kb.subject!r}. Your territory (salience-rendered):\n\n"
                f"{view}\n\nQUERY: {query}\n\nReply in TWO parts:\n"
                "ANSWER: <your territory's contribution, <=120 words>\n"
                "Then the typed construction your answer USED — JSONL, one "
                'per line:\n{"c": "<snake_case_id>", "d": "<definition, 8+ '
                'chars>"}\n{"r": ["<source_id>", "<target_id>"]}\n'
                "LAWS (machine-proven): every relation endpoint declared; "
                "every concept touches >=1 relation.")

    def _cross_prompt(self, query, certified, answers):
        blocks = []
        for region, p in certified.items():
            ids = ", ".join(c["id"] for c in p["concepts"][:12])
            blocks.append(f"[{region}] certified: {ids}\n"
                          f"  said: {answers.get(region, '')[:160]}")
        return ("You are the SYNTHESIZER at the next proof level. Unify the "
                f"certified territories for the query.\nQUERY: {query}\n\n"
                + "\n".join(blocks) +
                "\n\nReply in TWO parts:\nANSWER: <the unified answer, <=150 "
                "words>\nThen the CROSS-TERRITORY construction — re-declare "
                "the concepts you keep (from BOTH territories, with "
                "definitions) and add the relations that JOIN them across "
                "territories. Use EXACTLY this JSONL, one object per line, "
                'no other keys:\n{"c": "<snake_case_id>", "d": "<definition, '
                '8+ chars>"}\n{"r": ["<source_id>", "<target_id>"]}\n'
                "LAWS (machine-proven): closed + connected — ONE web, "
                "not two islands.")

    async def _admit(self, lat, node, subject, seat, prompt_fn, log):
        """The repair ladder: fill → compile; soup → retry/compute/revise;
        bounded. Returns (payload, answer) on ONT, (None, answer) on halt."""
        residue, answer, filled = None, "", False
        for attempt in range(1, MAX_ATTEMPTS + 1):
            prompt = prompt_fn()
            if residue:
                prompt += ("\n\nPROOF RESIDUE — your previous construction "
                           f"failed: {residue}. Fix exactly these; re-emit "
                           "BOTH parts.")
            answer, cs, rs = _parse_two_part(await _run_seat(seat, prompt))
            if not cs or not rs:
                residue = ("no typed construction parsed — emit the JSONL "
                           "lines exactly as specified, no fences")
                log(f"[residue] {node} attempt {attempt}: unparseable "
                    "construction")
                continue
            payload = _payload(subject, cs, rs)
            try:
                if not filled:
                    lat.fill_construction(node, payload)
                    filled = True
                else:
                    lat.retry(node)
                    lat.compute(node)
                    lat.revise_construction(node, payload)
            except Exception as e:          # PSC boundary (either error class)
                residue = f"psc: {str(e)[:300]}"
                continue
            lat.attach_observation(node, {"kind": "pass_witness",
                                          "subject": subject,
                                          "layer": 0, "pass_num": 1})
            packet = lat.compile(node)
            if packet.get("griess_phase") == "ont":
                log(f"[admit] {node}: ONT on attempt {attempt} "
                    f"({len(cs)}c/{len(rs)}r)")
                return payload, answer
            residue = [f for f in packet.get("frontier", [])
                       if "dangling" in f or "orphan" in f]
            log(f"[residue] {node} attempt {attempt}: {residue[:4]}")
        return None, answer

    async def ask(self, query, seat_factory, budget=2, log=print) -> dict:
        t0 = time.time()
        stim = self._stimulus(query)
        fired = [n for n, _p in self.graph.disclose(stim, budget=budget,
                                                    kind="ref")
                 if n in self.regions()]
        log(f"[fire] {fired} (of {len(self.regions())} regions)")
        if len(fired) < 2:
            return {"query": query, "fired": fired, "error":
                    "fewer than 2 neurons fired — grow more gyri or rephrase"}

        ask_dir = self.root / "asks" / f"{_slug(query)[:32]}_{int(t0)}"
        compiler = PrologTargetCompiler(load_domain_manifest(DOM))
        from ee_v2.map_gate.adapter import (EEOntologyAdapter,
                                            EEPassObservationAdapter)
        lat = MapV2Lattice(ask_dir / "lattice", compiler=compiler,
                          construction_adapter=EEOntologyAdapter(),
                          observation_adapter=EEPassObservationAdapter())
        subject = "brain_ask"
        lat.create(subject, "ee_ontology")
        res = lat.expand(subject, [f"n_{r[:24]}" for r in fired])
        node_of = dict(zip(fired, res["children"]))

        certified, answers = {}, {}
        for region in fired:
            node = node_of[region]
            lat.declare_kappa(node, "ee_conceptualization",
                              {"ontology_coherence": "closed + connected"})
            lat.compute(node)
            view = self._membrane_view(region,
                                       {c for c in stim
                                        if c in self.kb.concepts})
            payload, answer = await self._admit(
                lat, node, subject, seat_factory(region),
                lambda: self._neuron_prompt(region, view, query), log)
            answers[region] = answer
            if payload:
                certified[region] = payload

        if len(certified) < 2:
            return {"query": query, "fired": fired,
                    "certified": list(certified), "error":
                    "fewer than 2 neurons certified — no synthesis"}

        # combine with prover-driven staleness repair
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
                    node = reason["node"]
                    lat.retry(node)
                    lat.compute(node)
                    lat.revise_construction(node,
                                            certified[region_of[node]])
                    lat.attach_observation(node, {"kind": "pass_witness",
                                                  "subject": subject,
                                                  "layer": 0, "pass_num": 1})
                    assert lat.compile(node).get("griess_phase") == "ont"
        assert combined is not None
        log(f"[synth] combine() accepted {len(certified)} certified sources")

        # ── THE SES TOWER (option B): promote → reify → prove the synthesis ──
        lat.promote("final")
        r = lat.reify("final")
        ses_depth = r.get("ses_depth")
        lat.declare_kappa("final", "ee_conceptualization",
                          {"ontology_coherence":
                           "closed + connected ACROSS territories"})
        lat.compute("final")
        synth_seat = seat_factory("synthesizer")
        payload, final_answer = await self._admit(
            lat, "final", subject, synth_seat,
            lambda: self._cross_prompt(query, certified, answers), log)
        synthesis_proven = payload is not None
        if synthesis_proven:
            log(f"[tower] the synthesis ITSELF certified at SES depth "
                f"{ses_depth} — pattern_unproven is fixed")

        # ── TEACH: the prover is the teacher (rung-4) ────────────────────────
        self.graph.teach(stim, {r: 10.0 for r in certified})
        rs_ = list(certified)
        for i in range(len(rs_) - 1):
            self.graph.hebbian(rs_[i], rs_[i + 1])
        log("[teach] admitted → amplitude + hebbian (the prover taught)")

        report = {"query": query, "fired": fired,
                  "certified": {k: {"concepts": len(v["concepts"]),
                                    "relations": len(v["relations"])}
                                for k, v in certified.items()},
                  "synthesis_proven": synthesis_proven,
                  "ses_depth": ses_depth,
                  "final_answer": final_answer,
                  "neuron_answers": answers,
                  "secs": round(time.time() - t0, 1)}
        (ask_dir / "report.json").write_text(json.dumps(report, indent=2))
        return report


__all__ = ["KbcBrain"]
