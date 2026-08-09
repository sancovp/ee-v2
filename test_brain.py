#!/usr/bin/env python3
"""THE DURABLE BRAIN — deterministic proof (scripted seats, real kuzu + swipl).

Asserted:
  * grow: a well-connected atom projects + wires WITHOUT expansion; a THIN
    atom triggers the proof-gated expand first (accretion into the KB);
  * ask: the graph fires the right neurons numerically; the repair ladder
    admits them (residue → ONT); combine accepts only certified sources;
  * THE SES TOWER: promote → reify → the cross-territory construction
    certifies at SES depth 1 — the synthesis ITSELF is proven;
  * teach: admitted regions' amplitudes RISE (read back from kuzu — the
    prover taught the graph);
  * grow-then-fire: a gyrus grown AFTER genesis fires on a matching query —
    "I added them and now it runs."
"""
import asyncio
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, "/home/ceo/repo/ee-v2")

from ee_v2.kbc import KB                                             # noqa: E402
from ee_v2.kbc.brain import KbcBrain                                 # noqa: E402


def make_kb(tmp) -> KB:
    kb = KB("espresso craft", Path(tmp) / "kb")
    eq = {"espresso_machine": "machine that brews espresso under pressure",
          "portafilter": "the handle basket holding the grounds",
          "grind_size": "fineness of the coffee grounds",
          "espresso_shot": "the extracted concentrated coffee"}
    tech = {"milk_steaming": "steaming milk into velvet microfoam",
            "milk_pitcher": "the jug used for steaming milk",
            "microfoam": "velvety steamed milk texture",
            "latte_art": "patterns poured with microfoam"}
    for c, d in eq.items():
        kb.add_concept(c, d, lib="equipment")
    for c, d in tech.items():
        kb.add_concept(c, d, lib="technique")
    kb.add_concept("water_filtration", "filtering brew water", lib="supply")
    for s, t in [("espresso_machine", "portafilter"),
                 ("portafilter", "grind_size"),
                 ("grind_size", "espresso_shot"),
                 ("espresso_shot", "espresso_machine"),
                 ("milk_steaming", "milk_pitcher"),
                 ("milk_pitcher", "microfoam"),
                 ("microfoam", "latte_art"),
                 ("latte_art", "milk_steaming"),
                 ("espresso_shot", "microfoam"),
                 ("milk_steaming", "microfoam"),
                 ("water_filtration", "espresso_machine")]:
        kb.add_relation(s, t)
    kb.save()
    return kb


class Seat:
    """Name-aware scripted seat: neuron first-attempt emits a dangling ghost
    (forcing one residue round); retries and the synthesizer emit clean."""

    def __init__(self, name, ledger):
        self.name, self.ledger = name, ledger

    def run(self, prompt):
        self.ledger.setdefault(self.name, []).append(prompt)
        core = f"{self.name[:8].rstrip('_')}_core"
        if "EXPAND X" in prompt:                       # the grow-expand op
            return "\n".join([
                json.dumps({"c": f"{core}_part", "d":
                            "an expanded part of this region"}),
                json.dumps({"r": [self.name, f"{core}_part"]})])
        good = "\n".join([
            json.dumps({"c": core, "d": "the core of this territory"}),
            json.dumps({"c": "shared_log", "d": "the record both keep"}),
            json.dumps({"r": [core, "shared_log"]})])
        if "SYNTHESIZER" in prompt:
            return ("ANSWER: unified across territories.\n" + "\n".join([
                json.dumps({"c": "unified_core",
                            "d": "the cross-territory unification"}),
                json.dumps({"c": "bridge_core",
                            "d": "what joins the territories"}),
                json.dumps({"r": ["unified_core", "bridge_core"]})]))
        if "PROOF RESIDUE" in prompt:
            return f"ANSWER: corrected contribution.\n{good}"
        return ("ANSWER: my territory's contribution.\n" + good + "\n"
                + json.dumps({"r": [core, "ghost"]}))   # dangling → residue


def amplitude(brain, name):
    r = brain.graph.conn.execute(
        "MATCH (c:Concept {name: $n}) RETURN c.amplitude", {"n": name})
    return r.get_next()[0] if r.has_next() else None


async def main(tmp):
    ledger = {}
    kb = make_kb(tmp)
    brain = KbcBrain(kb, Path(tmp) / "brain")
    seat = lambda name: Seat(name, ledger)             # noqa: E731

    # grow: connected atom (no expand) + thin-ish atom (expand fires)
    r1 = await brain.grow("espresso_machine", seat)
    assert not r1["expanded"], r1
    r2 = await brain.grow("milk_steaming", seat)
    assert brain.regions() == ["espresso_machine", "milk_steaming"]
    print(f"  grow: espresso (no expand) + milk_steaming "
          f"(expanded={r2['expanded']}) → 2 gyri ✓")

    # ask: both fire, residue arc, combine, THE TOWER, teach
    a0 = amplitude(brain, "espresso_machine")
    rep = await brain.ask("how do I get a great espresso shot with silky "
                          "milk microfoam?", seat, log=lambda *_: None)
    assert set(rep["fired"]) == {"espresso_machine", "milk_steaming"}, rep
    assert len(rep["certified"]) == 2
    assert rep["synthesis_proven"] is True
    assert rep["ses_depth"] == 1
    print("  ask: both neurons fired numerically · residue→ONT · "
          f"combine accepted · SYNTHESIS PROVEN at SES depth "
          f"{rep['ses_depth']} ✓")
    a1 = amplitude(brain, "espresso_machine")
    assert a1 > a0, (a0, a1)
    print(f"  teach: espresso_machine amplitude {a0:.2f}→{a1:.2f} "
          "(the prover taught the graph) ✓")

    # grow-then-fire: the §19 sentence
    r3 = await brain.grow("water_filtration", seat)
    assert r3["expanded"] is True                       # deg 1 → thin
    rep2 = await brain.ask("is water filtration hurting my espresso "
                           "machine?", seat, log=lambda *_: None)
    assert "water_filtration" in rep2["fired"], rep2
    assert rep2["synthesis_proven"] is True
    print("  grow-then-fire: water_filtration grown (expand fired), then "
          "FIRED on a matching ask, certified, synthesized ✓")

    # persistence on disk
    root = Path(tmp) / "brain"
    assert (root / "tissue/water_filtration").is_dir()
    assert list((root / "asks").iterdir())
    print("  durable: tissue + asks + neurodb persist under the brain dir ✓")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as d:
        asyncio.run(main(d))
    print("BRAIN PASS — grow-gyri under proof, numeric fire, proven "
          "synthesis (SES tower), prover-taught salience, all durable.")
