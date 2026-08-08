#!/usr/bin/env python3
"""ee-v2 — deterministic proof (NO API). What is asserted:

  * FROZEN PARITY: the 21 payloads byte-match emergence-engine's own
    PhasePrompts output (extraction, never paraphrase);
  * the engine lays the WHOLE structure (3 layers × 3 passes × (7 phases +
    1 emission) = 72 nodes) and the agent never touches a mkdir;
  * FRESH SEAT PER NODE — 72 instantiations, no shared context;
  * PROGRESSIVE DISCLOSURE — the first node sees no rules; later nodes see
    exactly the rules minted by completed passes; L1 nodes work on L0's P2
    emission (the recursion is REAL content, not a counter rollover);
  * emissions mint to the RULE-1 shape: P1→rules/, P2→skills/<n>/SKILL.md,
    P3→artifacts/;
  * THE DIR IS THE MEMO — delete one node file, rerun: exactly one seat runs;
  * THE TOWER — runs=2: run2's domain is run1's L2P3 closure.
"""
import json
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, "/home/ceo/repo/emergence-engine")   # parity source

from ee_v2.journey import Journey, PAYLOADS
from ee_v2.run import ee_run


class ScriptedSeat:
    """One fresh seat per node (the factory counts). Emission prompts get
    valid JSON; phase prompts get a marked document."""
    def __init__(self, ledger):
        self.ledger = ledger

    def run(self, prompt: str) -> str:
        self.ledger["prompts"].append(prompt)
        n = len(self.ledger["prompts"])
        if "Reply ONLY JSON" in prompt:
            kind = ("rule" if "ONE operational RULE" in prompt else
                    "skill" if "ONE SKILL" in prompt else "artifact")
            return json.dumps({"name": f"{kind}_{n}",
                               "content": f"<{kind.upper()}-{n} distilled>"})
        return f"# node artifact {n}\ncontent for seat {n}"


def make_factory(ledger):
    def factory():
        ledger["seats"] += 1
        return ScriptedSeat(ledger)
    return factory


def test_frozen_parity():
    from emergence_engine.core import PhasePrompts
    for p in (1, 2, 3):
        theirs = getattr(PhasePrompts, f"_get_pass{p}_prompts")("{domain}")
        ours = PAYLOADS[f"pass{p}"]
        assert {str(k): v for k, v in theirs.items()} == ours, f"pass{p} drift"
    print("  frozen parity: 21 payloads byte-match emergence-engine ✓")


def test_full_run_and_disclosure(root):
    ledger = {"seats": 0, "prompts": []}
    (j,) = ee_run("test kitchen design", make_factory(ledger), root, runs=1)
    # the engine laid everything; all 72 nodes done
    assert j.position() is None
    assert ledger["seats"] == 72                       # a fresh seat per node
    node_files = list(j.root.glob("L*/P*/[0-6]-*.md"))
    assert len(node_files) == 63
    assert len(list(j.root.glob("L*/P*/emission.json"))) == 9
    # RULE-1 shape: 3 rules, 3 skills, 3 artifacts
    assert len(list((j.root / "rules").glob("*.md"))) == 3
    assert len(list((j.root / "skills").glob("*/SKILL.md"))) == 3
    assert len(list((j.root / "artifacts").glob("*.md"))) == 3
    # progressive disclosure: node 1 sees NO standing rules...
    assert "STANDING RULES" not in ledger["prompts"][0]
    # ...but after L0P1's emission (prompt index 8 = 7 phases + 1 emission),
    # the very next node sees exactly that rule
    assert "STANDING RULES" in ledger["prompts"][8]
    assert "RULE-9 distilled".lower() not in ledger["prompts"][8].lower()
    assert "rule_8" in ledger["prompts"][8]            # the minted rule's name
    # the recursion is REAL: an L1 node's DOMAIN carries L0's P2 emission
    l1_first = ledger["prompts"][24]                   # after L0's 24 nodes
    assert "generator built at L0P2" in l1_first
    assert "SKILL-16 distilled" in l1_first            # L0P2's emission content
    print("  full run: 72 nodes · fresh seats · disclosure schedule · "
          "REAL layer recursion ✓")
    return j


def test_dir_is_the_memo(root):
    j = Journey(Path(root) / "run1", "ignored — resumes")
    target = j.node_path(1, 2, 3)
    target.unlink()                                    # wound one node
    ledger = {"seats": 0, "prompts": []}
    ee_run("ignored — resumes", make_factory(ledger), root, runs=1)
    assert ledger["seats"] == 1                        # exactly the wound heals
    assert j._done((1, 2, 3))
    print("  the dir is the memo: 1 deleted node → exactly 1 seat ran ✓")


def test_the_tower(root):
    ledger = {"seats": 0, "prompts": []}
    j1, j2 = ee_run("bootstrapping bakeries", make_factory(ledger),
                    root, runs=2)
    closure = j1.final_artifact()
    assert closure and closure in j2.domain            # run2 works run1's output
    assert j2.position() is None
    print("  the tower: run2's domain IS run1's L2P3 closure ✓")


def main():
    test_frozen_parity()
    with tempfile.TemporaryDirectory() as d:
        test_full_run_and_disclosure(d)
        test_dir_is_the_memo(d)
    with tempfile.TemporaryDirectory() as d:
        test_the_tower(d)
    print("EE-V2 PASS — the diagram is a chain, the dir is the state, "
          "disclosure is mechanical, the recursion is real, runs compose.")


if __name__ == "__main__":
    main()
