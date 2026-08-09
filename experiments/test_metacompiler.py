#!/usr/bin/env python3
"""metacompiler — deterministic proof (scripted seats, real swipl via kb.check).

Asserted:
  * the parser reads Isaac's chain notation structurally: SpareFractalCoreChain
    → 10 named nodes, 32 substeps, the summary spine, the results=> closure;
  * a cycle walks the nodes IN ORDER, one fresh seat per node + harvest,
    writes cycle{n}/{num}-{node}.md — THE DIR IS THE MEMO (wound one node file,
    rerun: exactly one seat runs);
  * harvest accretes into the persistent KB and the prover mints the worklist;
  * THE METER stops the chain: a cycle with zero new atoms = stabilized (the
    kernel's own 10c criterion, measured) — and a changing seat keeps cycling;
  * a second, differently-shaped chain parses too (the metacompiler is
    generic, not fitted to one kernel).
"""
import asyncio
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, "/home/ceo/repo/ee-v2/experiments")

from metacompiler import metacompile, run_chain                  # noqa: E402

CHAIN = Path(__file__).parent / "kernels/sparefractalcorechain.txt"

MINI = ("[MiniLoop]: Ask→Answer: 1.Ask: 1a.pose the question 2.Answer: "
        "2a.answer it 2b.note one implication results=> Q→A→∞")


class ScriptedSeat:
    """Node prompts → a doc; harvest prompts → JSONL from a script that can
    either repeat (→ fixpoint) or keep growing (→ budget stop)."""

    def __init__(self, ledger, grow=False):
        self.ledger, self.grow = ledger, grow

    def run(self, prompt):
        self.ledger["prompts"].append(prompt)
        n = len(self.ledger["prompts"])
        if "HARVEST" in prompt:
            k = self.ledger["harvests"] = self.ledger.get("harvests", 0) + 1
            i = k if self.grow else 1          # grow=False → identical dumps
            return "\n".join([
                json.dumps({"c": f"motif_{i}", "d": "a recurring motif image"}),
                json.dumps({"c": f"anchor_{i}", "d": "the anchor it binds to"}),
                json.dumps({"r": [f"motif_{i}", f"anchor_{i}"]})])
        return f"# artifact {n}\nnode output {n}"


def factory_of(ledger, grow=False):
    def factory():
        ledger["seats"] += 1
        return ScriptedSeat(ledger, grow)
    return factory


def test_parser():
    k = metacompile(CHAIN.read_text())
    assert k.name == "SpareFractalCoreChain"
    assert len(k.nodes) == 10, len(k.nodes)
    names = [n.name for n in k.nodes]
    assert names[0] == "IntentSeed" and names[-1] == "RecursiveClosure"
    assert sum(len(n.steps) for n in k.nodes) == 32
    assert k.summary.startswith("Desire")
    assert k.closure.endswith("∞")
    k2 = metacompile(MINI)
    assert [n.name for n in k2.nodes] == ["Ask", "Answer"]
    assert len(k2.nodes[1].steps) == 2
    print("  parser: 10 nodes/32 steps + closure from the chain text; a "
          "second chain shape parses too (generic) ✓")
    return k


def test_fixpoint_stop(k, root):
    ledger = {"seats": 0, "prompts": []}
    r = asyncio.run(run_chain(k, "test desire", factory_of(ledger),
                              root, max_cycles=5))
    assert r["stabilized"] is True
    assert r["cycles"] == 2                     # c1 accretes, c2 zero-delta
    assert r["rounds"][0]["new_atoms"] == 3
    assert r["rounds"][1]["new_atoms"] == 0
    # 2 cycles × (10 nodes + 1 harvest) = 22 seats
    assert ledger["seats"] == 22, ledger["seats"]
    # the prover minted a worklist on the accreted KB (real swipl ran)
    assert "worklist_define" in r["rounds"][0]
    print("  THE METER stops the chain: cycle2 zero-delta → stabilized "
          "(10c measured); 22 fresh seats; prover minted the worklist ✓")


def test_budget_stop_when_growing(k, root):
    ledger = {"seats": 0, "prompts": []}
    r = asyncio.run(run_chain(k, "test desire", factory_of(ledger, grow=True),
                              root, max_cycles=3))
    assert r["stabilized"] is False and r["cycles"] == 3
    assert all(x["new_atoms"] > 0 for x in r["rounds"])
    print("  a still-emerging ecology keeps cycling to budget "
          "(no false fixpoint) ✓")


def test_dir_is_the_memo(k, root):
    ledger = {"seats": 0, "prompts": []}
    asyncio.run(run_chain(k, "test desire", factory_of(ledger), root,
                          max_cycles=1))
    wound = Path(root) / "cycle1" / "4-release.md"
    wound.unlink()
    ledger2 = {"seats": 0, "prompts": []}
    asyncio.run(run_chain(k, "test desire", factory_of(ledger2), root,
                          max_cycles=1))
    # heal = the one wounded node + the cycle-end harvest re-runs; no more
    assert ledger2["seats"] == 2, ledger2["seats"]
    assert wound.exists()
    print("  the dir is the memo: wound one node → exactly 1 node seat + "
          "harvest re-run ✓")


def main():
    k = test_parser()
    with tempfile.TemporaryDirectory() as d:
        test_fixpoint_stop(k, d)
    with tempfile.TemporaryDirectory() as d:
        test_budget_stop_when_growing(k, d)
    with tempfile.TemporaryDirectory() as d:
        test_dir_is_the_memo(k, d)
    print("METACOMPILER PASS — any chain notation in, a gated cycling KB "
          "compiler out; fixpoint measured, never vibed.")


if __name__ == "__main__":
    main()
