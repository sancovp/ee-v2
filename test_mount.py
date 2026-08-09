#!/usr/bin/env python3
"""THE FUNCTOR — deterministic proof (scripted host, real swipl via kb.check).

Asserted:
  * mount(host) rejects a host missing the protocol, accepts a duck-typed one;
  * the command surface runs end-to-end against a scripted seat: kb new →
    dump → work → drain define → root → expand → project · kernel run;
  * state lives under host.state_root (kbs/, kernels/, libraries/,
    current_kb) — the current-KB pointer moves like a chat runtime's
    current-conversation pointer;
  * events flow through host.emit so ANY host's faces can render activity;
  * the same functor applied to a SECOND host instance is fully independent
    (no shared globals — the precondition for mounting onto cave-teams /
    anything later).
"""
import asyncio
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, "/home/ceo/repo/ee-v2")

from ee_v2.kbc import mount, HOST_PROTOCOL                       # noqa: E402

MINI = ("[MiniLoop]: Ask→Answer: 1.Ask: 1a.pose the question 2.Answer: "
        "2a.answer it 2b.note one implication results=> Q→A→∞")


class Seat:
    def __init__(self, ledger):
        self.ledger = ledger

    def run(self, prompt):
        self.ledger["prompts"].append(prompt)
        if "MASS-ENUMERATE" in prompt or "EXPAND X" in prompt:
            return "\n".join([
                json.dumps({"c": "alpha", "d": "the first named thing"}),
                json.dumps({"c": "beta", "d": "the second named thing"}),
                json.dumps({"r": ["alpha", "beta"]}),
                json.dumps({"r": ["alpha", "gamma"]})])   # gamma undefined
        if "DEFINE each concept below" in prompt:
            return json.dumps({"c": "gamma", "d": "the third named thing"})
        if "HARVEST" in prompt:
            return "\n".join([
                json.dumps({"c": "motif", "d": "a recurring emerged image"}),
                json.dumps({"c": "anchor", "d": "what the motif binds to"}),
                json.dumps({"r": ["motif", "anchor"]})])
        return "# node artifact"


class Host:
    def __init__(self, root, ledger):
        self.state_root = root
        self.ledger = ledger
        self.events = []

    def seat_factory(self):
        self.ledger["seats"] += 1
        return Seat(self.ledger)

    def emit(self, event):
        self.events.append(event)


async def main(tmp):
    class Bad:
        pass
    try:
        mount(Bad())
        raise AssertionError("protocol not enforced")
    except TypeError as e:
        assert "seat_factory" in str(e)
    print(f"  protocol enforced ({HOST_PROTOCOL}) ✓")

    ledger = {"seats": 0, "prompts": []}
    host = Host(Path(tmp) / "hostA", ledger)
    cmds = mount(host)
    assert set(cmds) >= {"kb new", "kb dump", "kb work", "kb drain",
                         "kb root", "kb expand", "kb project",
                         "kernel list", "kernel run"}

    print(" ", await cmds["kb new"]("test kitchens"))
    assert (host.state_root / "current_kb").read_text() == "test_kitchens"
    out = await cmds["kb dump"]("")
    assert "define=1" in out, out                       # gamma undefined
    out = await cmds["kb work"]("")
    assert "gamma" in out
    out = await cmds["kb drain"]("define 10")
    assert "1→0" in out.replace(" ", "") or "'defined': 1" in out, out
    out = await cmds["kb root"]("alpha")
    assert "beta" in out and "gamma" in out             # the LFP cone
    out = await cmds["kb expand"]("alpha")
    assert "phase=" in out
    out = await cmds["kb project"]("")
    assert "understand-" in out
    print("  kb surface: new→dump→work→drain→root→expand→project ✓")

    (host.state_root / "kernels" / "miniloop.txt").write_text(MINI)
    out = await cmds["kernel run"]("miniloop a tiny question")
    assert "MiniLoop" in out and "cycle" in out
    assert (host.state_root / "current_kb").read_text().endswith("miniloop")
    print("  kernel surface: metacompiled chain ran; current-KB pointer "
          "moved ✓")

    kinds = [e["type"] for e in host.events]
    assert {"kb_new", "kb_dump", "kb_drain", "kb_expand", "kb_project",
            "kernel_run"} <= set(kinds), kinds
    print(f"  events flowed to the host's faces ({len(host.events)}) ✓")

    hostB = Host(Path(tmp) / "hostB", ledger)
    cmdsB = mount(hostB)
    await cmdsB["kb new"]("another world")
    assert (host.state_root / "current_kb").read_text() != "another_world"
    print("  second host fully independent (the functor precondition) ✓")


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as d:
        asyncio.run(main(d))
    print("MOUNT PASS — one functor, any host: the integration is written "
          "once, host-agnostically.")
