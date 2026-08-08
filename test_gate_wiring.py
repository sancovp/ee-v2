#!/usr/bin/env python3
"""THE GATE, WIRED — deterministic proof (scripted seats, REAL SWI-Prolog).

What is asserted (§R build order step 2):
  * a gated run completes with a CERTIFICATE per gated emission (6 = L0-2 ×
    P1-P2), the P2 seats receiving P1's certified concepts FROM THE ENGINE;
  * THE FIXPOINT METER counts newly-certified structure per pass — and
    detects Isaac's fixpoint (a seat emitting the same structure every layer
    reads zero-delta from L1P1 on);
  * THE RETRY LOOP: an incoherent first emission gets the PROOF RESIDUE fed
    back (naming the exact violations) and the corrected retry certifies;
  * P2 GROUNDING (the previously-untested ee_skill domain, end-to-end): an
    ungrounded step is named in the residue and the corrected retry passes;
  * FAIL-CLOSED HALT: persistent SOUP writes soup.json, the chain stops AT
    the node, NO emission file exists, position() is unchanged — and a rerun
    with a competent seat HEALS the same journey (soup cleared, cert minted).
"""
import json
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, "/home/ceo/repo/cave-teams")
sys.path.insert(0, "/home/ceo/repo/map-v2")
sys.path.insert(0, "/home/ceo/repo/ee-v2")

from ee_v2.journey import Journey
from ee_v2.run import ee_run
from ee_v2.map_gate.gate import MapGate

CERT_RE = re.compile(r"## P1-CERTIFIED CONCEPTS[^\n]*\n([a-z0-9_, ]+)")


def _certified_from_prompt(prompt: str):
    m = CERT_RE.search(prompt)
    return [c.strip() for c in m.group(1).split(",")] if m else []


def good_p1(n, fixed=False):
    a, b = ("alpha", "beta") if fixed else (f"alpha_{n}", f"beta_{n}")
    return {"name": f"rule_{n}", "content": f"<RULE-{n}>",
            "concepts": [{"id": a, "definition": "the first named thing"},
                         {"id": b, "definition": "the second named thing"}],
            "relations": [{"id": "r1", "source": a, "target": b}]}


def bad_p1(n):
    # dangling target (gamma undeclared) + orphan (beta in no relation)
    return {"name": f"rule_{n}", "content": f"<RULE-{n}>",
            "concepts": [{"id": "alpha", "definition": "the first thing"},
                         {"id": "beta", "definition": "the second thing"}],
            "relations": [{"id": "r1", "source": "alpha", "target": "gamma"}]}


class Seat:
    """One scripted seat per node/attempt. p1/p2 hooks decide coherence."""

    def __init__(self, ledger, p1=None, p2=None):
        self.ledger = ledger
        self.p1 = p1 or (lambda n, prompt: good_p1(n))
        self.p2 = p2 or (lambda n, prompt:
                         {"name": f"skill_{n}", "content": f"<SKILL-{n}>",
                          "steps": [{"id": f"do_{n}",
                                     "action": "apply the first to the second",
                                     "uses": _certified_from_prompt(prompt)[:1]
                                     or ["alpha"]}]})

    def run(self, prompt):
        self.ledger["prompts"].append(prompt)
        n = len(self.ledger["prompts"])
        if '"concepts"' in prompt:
            return json.dumps(self.p1(n, prompt))
        if '"steps"' in prompt:
            return json.dumps(self.p2(n, prompt))
        if "Reply ONLY JSON" in prompt:                       # ungated P3
            return json.dumps({"name": f"artifact_{n}",
                               "content": f"<ARTIFACT-{n}>"})
        return f"# node artifact {n}"


def factory_of(ledger, **hooks):
    def factory():
        ledger["seats"] += 1
        return Seat(ledger, **hooks)
    return factory


def test_gated_full_run_and_meter(root):
    ledger = {"seats": 0, "prompts": []}
    (j,) = ee_run("test kitchen design", factory_of(ledger), root,
                  runs=1, gate=MapGate())
    assert j.position() is None, "gated run must complete"
    certs = [(l, p) for l in (0, 1, 2) for p in (1, 2)
             if j.certificate(l, p)]
    assert len(certs) == 6, certs
    assert not list(j.root.glob("L*/P*/soup.json"))
    # the engine handed P2 its layer's certified ground
    p2_prompts = [p for p in ledger["prompts"] if '"steps"' in p]
    assert all("P1-CERTIFIED CONCEPTS" in p for p in p2_prompts)
    # the meter: unique structure per pass → every row adds new structure
    rows = j.fixpoint_meter()
    assert len(rows) == 6 and all(r["new"] > 0 for r in rows), rows
    assert rows[-1]["total_certified"] == sum(r["new"] for r in rows)
    print("  gated full run: 6 ONT certificates · engine-supplied P2 ground "
          "· meter counts fresh structure ✓")


def test_meter_detects_fixpoint(root):
    ledger = {"seats": 0, "prompts": []}
    (j,) = ee_run("stabilizing domain",
                  factory_of(ledger, p1=lambda n, pr: good_p1(n, fixed=True)),
                  root, runs=1, gate=MapGate())
    rows = {r["node"]: r["new"] for r in j.fixpoint_meter()}
    assert rows["L0P1"] > 0
    assert rows["L1P1"] == 0 and rows["L2P1"] == 0, rows
    print("  THE FIXPOINT METER: identical structure re-certified → "
          "zero-delta from L1P1 on (Isaac's measurement, mechanized) ✓")


def test_retry_feeds_residue(root):
    ledger = {"seats": 0, "prompts": []}

    def flaky_p1(n, prompt):
        return good_p1(n) if "PROOF RESIDUE" in prompt else bad_p1(n)

    (j,) = ee_run("retry domain", factory_of(ledger, p1=flaky_p1), root,
                  runs=1, gate=MapGate())
    assert j.position() is None
    retries = [p for p in ledger["prompts"] if "PROOF RESIDUE" in p]
    assert len(retries) == 3, len(retries)          # one per layer's P1
    assert "dangling(r1,gamma)" in retries[0], retries[0][-400:]
    assert "orphan(beta)" in retries[0]
    print("  retry loop: SOUP residue NAMES dangling(r1,gamma) + "
          "orphan(beta) in the retry prompt; corrected retry → ONT ✓")


def test_p2_grounding_residue(root):
    ledger = {"seats": 0, "prompts": []}

    def flaky_p2(n, prompt):
        uses = (_certified_from_prompt(prompt)[:1]
                if "PROOF RESIDUE" in prompt else ["not_a_concept"])
        return {"name": f"skill_{n}", "content": f"<SKILL-{n}>",
                "steps": [{"id": f"do_{n}",
                           "action": "apply something to something",
                           "uses": uses}]}

    (j,) = ee_run("grounding domain", factory_of(ledger, p2=flaky_p2), root,
                  runs=1, gate=MapGate())
    assert j.position() is None
    retries = [p for p in ledger["prompts"] if "PROOF RESIDUE" in p]
    assert retries and "ungrounded(" in retries[0], retries[0][-400:]
    assert "not_a_concept" in retries[0]
    print("  P2 grounding (ee_skill domain, first end-to-end): ungrounded "
          "use NAMED in residue; certified-ground retry → ONT ✓")


def test_fail_closed_halt_then_heal(root):
    ledger = {"seats": 0, "prompts": []}
    ee_run("halt domain", factory_of(ledger, p1=lambda n, pr: bad_p1(n)),
           root, runs=1, gate=MapGate())
    j = Journey(Path(root) / "run1", "ignored — resumes")
    assert j.position() == (0, 1, None), j.position()   # halted AT the node
    assert not j.node_path(0, 1, None).exists()          # NO emission file
    soup = json.loads(j.soup_path(0, 1).read_text())
    assert soup["attempts"] == 3
    assert any("dangling" in f for f in soup["frontier"])
    assert ledger["seats"] == 7 + 3                      # 7 phases + 3 tries
    # HEAL: same journey, competent seat
    ledger2 = {"seats": 0, "prompts": []}
    (j2,) = ee_run("ignored — resumes", factory_of(ledger2), root,
                   runs=1, gate=MapGate())
    assert j2.position() is None
    assert not j2.soup_path(0, 1).exists()
    assert j2.certificate(0, 1)
    print("  fail-closed halt: soup.json + position unchanged + chain "
          "stopped at the node; rerun HEALS the same journey ✓")


def main():
    for fn in (test_gated_full_run_and_meter, test_meter_detects_fixpoint,
               test_retry_feeds_residue, test_p2_grounding_residue,
               test_fail_closed_halt_then_heal):
        with tempfile.TemporaryDirectory() as d:
            fn(d)
    print("GATE WIRING PASS — the emission file exists only when PROVEN; "
          "residue drives retries; persistent SOUP halts fail-closed; the "
          "fixpoint meter reads stabilization off the certificates.")


if __name__ == "__main__":
    main()
