#!/usr/bin/env python3
"""THE LANGUAGE AUTOMATON — deterministic proof (§24/§24b/§24c).
Scripted seats; REAL swipl (both domains) + REAL kuzu. One process, one
kuzu handle.

Asserted:
  T1 speak-without-LLM: a defined+asserted walk gate-mints at 0 calls → KNOWN
  T2 the ledger: the same walk is covered — no re-gate, still 0 calls
  T3 alphabet-mint: an undefined atom routes to a scoped define → KNOWN
  T4 candidate step: an unasserted kernel proposal is confirmed on the exact
     schema → asserted → certified
  T5 the negative wire: repeated mint failure → recorded → condemned →
     BULLSHIT at 0 calls; down-tune touched the graph (weights, not content)
  T6 articulation: unwarranted `because` → named residue → warranted DAG →
     ONT through the ee_argument domain → persisted skeleton
  T7 the adjoint demand: explain_bucket drops the articulated root; the
     worklist carries the explain bucket
  T8 operator rendering: the certified skeleton's `because` reaches render()
  T9 the kernel: a seeded walk samples the graph from its start
  T10 the meter: crystallization visible — the last statement cost 0 calls
"""
import asyncio
import json
import random
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, "/home/ceo/repo/ee-v2")

from ee_v2.kbc import KB, derive_worklist                        # noqa: E402
from ee_v2.kbc.automaton import Automaton                        # noqa: E402
from ee_v2.kbc.brain import KbcBrain                             # noqa: E402


class Seat:
    def __init__(self, ledger, name="seat", persona=""):
        self.ledger, self.name = ledger, name

    def run(self, prompt):
        self.ledger.append(self.name)
        if "phantom_flux" in prompt and "DEFINE" in prompt:
            return "i have no idea what that is"          # garbage → residue
        if "DEFINE" in prompt:
            return json.dumps({"c": "burr_set",
                               "d": "the paired cutting discs inside the "
                                    "grinder burr assembly"})
        if "the chain proposed the step" in prompt:
            return json.dumps({"r": ["espresso_machine", "milk_steamer"]})
        if "argument skeleton" in prompt:
            if "PROOF RESIDUE" in prompt:                  # warranted retry
                return "\n".join([
                    json.dumps({"a": ["because", "espresso_machine",
                                      "boiler"]}),
                    json.dumps({"a": ["since", "boiler",
                                      "pressure_gauge"]})])
            return json.dumps({"a": ["because", "espresso_machine",
                                     "boiler"]})           # no warrant → SOUP
        return ""


def build_kb(root) -> KB:
    kb = KB("test bistro", root)
    for c, d in {
        "espresso_machine": "the pressurized brewing appliance at the bar",
        "portafilter": "the handled basket that locks into the group head",
        "grinder": "the burr mill that doses and grinds the beans",
        "boiler": "the heated pressure vessel supplying brew water",
        "pressure_gauge": "the dial reading the boiler's live pressure",
        "milk_steamer": "the wand that textures milk with boiler steam",
        "water_pump": "the pump feeding line water into the boiler",
    }.items():
        kb.add_concept(c, d)
    for s, t in [("espresso_machine", "portafilter"),
                 ("espresso_machine", "boiler"),
                 ("espresso_machine", "grinder"),
                 ("espresso_machine", "water_pump"),
                 ("boiler", "pressure_gauge"),
                 ("portafilter", "burr_set")]:      # burr_set: UNDEFINED stub
        kb.add_relation(s, t)
    kb.save()
    return kb


async def main(tmp):
    ledger = []
    seat_factory = lambda n="seat", p="": Seat(ledger, n)      # noqa: E731
    kb = build_kb(Path(tmp) / "kb")
    brain = KbcBrain(kb, Path(tmp) / "brain")
    await brain.grow("espresso_machine", seat_factory)   # deg>=4: no expand
    # the kernel proposes what the KB never asserted (the candidate step):
    brain.graph.add("milk_steamer", kind="concept", amplitude=0.3)
    brain.graph.wire("espresso_machine", "milk_steamer", weight=0.9)
    auto = Automaton(kb, brain)

    # T1 — speak without an LLM: gate-mint at zero calls
    r1 = await auto.statement(
        path=["espresso_machine", "boiler", "pressure_gauge"])
    assert r1["verdict"] == "known" and r1["llm_calls"] == 0, r1
    assert len(auto.hyperedges()) == 1
    assert "pressurized brewing appliance" in r1["text"]
    print(f"  T1 spoke at 0 calls: {r1['text'][:74]}… ✓")

    # T2 — the ledger covers; no re-gate
    r2 = await auto.statement(
        path=["espresso_machine", "boiler", "pressure_gauge"])
    assert r2["verdict"] == "known" and r2["llm_calls"] == 0
    assert len(auto.hyperedges()) == 1
    print("  T2 ledger coverage: same walk KNOWN, still 0 calls, no new "
          "hyperedge ✓")

    # T3 — the alphabet-mint: undefined atom → routed define → KNOWN
    r3 = await auto.statement(path=["portafilter", "burr_set"],
                              seat_factory=seat_factory)
    assert r3["verdict"] == "known", r3
    assert r3["llm_calls"] >= 1 and "burr_set" in kb.concepts
    print(f"  T3 minted the alphabet: burr_set defined "
          f"({r3['llm_calls']} calls) → KNOWN ✓")

    # T4 — the candidate step: kernel proposal confirmed on exact schema
    r4 = await auto.statement(path=["espresso_machine", "milk_steamer"],
                              seat_factory=seat_factory)
    assert r4["verdict"] == "known", r4
    assert ("espresso_machine", "milk_steamer") in kb.relations
    print("  T4 unasserted step confirmed → asserted → certified ✓")

    # T5 — the negative wire: fail → fail → condemned at 0 calls
    r5a = await auto.statement(path=["boiler", "phantom_flux"],
                               seat_factory=seat_factory)
    assert r5a["verdict"] == "mint_failed", r5a
    r5b = await auto.statement(path=["boiler", "phantom_flux"],
                               seat_factory=seat_factory)
    assert r5b["verdict"] == "bullshit", r5b
    r5c = await auto.statement(path=["boiler", "phantom_flux"],
                               seat_factory=seat_factory)
    assert r5c["verdict"] == "bullshit" and r5c["llm_calls"] == 0, r5c
    q = brain.graph.conn.execute(
        "MATCH (c:Concept {name: $n}) RETURN c.amplitude",
        {"n": "phantom_flux"})
    amp = q.get_next()[0] if q.has_next() else None
    assert amp is not None and amp <= 0.2, amp
    assert "phantom_flux" not in kb.concepts        # content never polluted
    print(f"  T5 the wire: 2 recorded failures → condemned (0 calls), "
          f"amplitude {amp:.2f}, KB untouched ✓")

    # T6 — articulation: residue-driven, proven through ee_argument
    r6 = await auto.articulate("espresso_machine", seat_factory)
    assert r6["ok"] and r6["llm_calls"] == 2, r6
    assert len(auto.skeletons()) == 1
    print("  T6 articulate: unwarranted because → residue → warranted DAG "
          "→ ONT ✓")

    # T7 — the adjoint demand signal
    bucket = auto.explain_bucket()
    assert "espresso_machine" not in bucket and "boiler" in bucket
    wl = derive_worklist(kb, explain=bucket)
    assert wl["explain"] == bucket
    print(f"  T7 explain bucket: {bucket[:4]} (root dropped; worklist "
          "carries it) ✓")

    # T8 — operator rendering from the certified skeleton
    r8 = await auto.statement(path=["espresso_machine", "boiler"])
    assert r8["verdict"] == "known" and "because «boiler»" in r8["text"]
    print(f"  T8 operator render: {r8['text'][:80]}… ✓")

    # T9 — the kernel samples
    p9 = auto.walk("espresso_machine", temp=0.5, max_steps=4,
                   rng=random.Random(7))
    assert p9[0] == "espresso_machine" and len(p9) >= 2, p9
    print(f"  T9 kernel walk: {p9} ✓")

    # T10 — the meter: crystallization visible
    m = auto.meter()
    assert m["statements"] == 8 and m["verdicts"]["known"] == 5
    last = auto._read_jsonl(auto.log_path)[-1]
    assert last["llm_calls"] == 0
    print(f"  T10 meter: {m['statements']} statements, "
          f"{m['calls_per_statement']} calls/stmt overall, last5 "
          f"{m['last5']}, verdicts {m['verdicts']} ✓")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as d:
        asyncio.run(main(d))
    print("AUTOMATON PASS — the chain speaks certified walks without LLMs, "
          "names its failures, mints exactly the gap, condemns confirmed "
          "nonsense by weight (never content), and articulates hyperedges "
          "into proven argument DAGs.")
