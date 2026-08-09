#!/usr/bin/env python3
"""metacompiler.py — DROP IN ANY RECURSIVE CHAIN, GET A KB COMPILER
(Isaac, 2026-08-09: "make the metacompiler that lets us just drop in any
prompt, and it gets turned into a compiler our way... make any KBs through
any recursive chain you can describe").

    kernel = metacompile(chain_text)          # parse the chain notation
    report = run_chain(kernel, subject, seat_factory, root)

The chain notation (Isaac's format):
    [Name]: summary: 1.Node: 1a.step 1b.step 2.Node: 2a.step ... results=> ...

Semantics compiled onto the proven machinery:
  * one CYCLE = walk the nodes in order — fresh seat per node, THE DIR IS THE
    STATE (cycle{n}/{num}-{node}.md; position = first missing file; resume
    free), context assembled by CEL: node prompt + the KB's relative root of
    the subject + the cycle so far.
  * cycle end = HARVEST: one seat dumps every motif (concept) + link
    (relation) that emerged, as JSONL → accreted into the persistent KB
    (kb_tool) → the prover mints the worklist (SOUP IS THE PRODUCT §11c).
  * THE METER decides recursion: a cycle that accretes ZERO new atoms has
    stabilized — the chain's own closure criterion ("repeat until the
    symbolic ecology stabilizes"), measured instead of vibed.

= §13's curried compiler with op GENERALIZED to a kernel: the metacompiler
turns prompts into ops. EE's frozen payloads are one kernel; any well-formed
chain is another; the engine does not change.
"""
from __future__ import annotations

import asyncio
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

for _p in ("/home/ceo/repo/ee-v2", "/home/ceo/repo/ee-v2/experiments",
           "/home/ceo/repo/map-v2", "/home/ceo/repo/cave-teams",
           "/home/ceo/lcshim2"):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from cave_teams.context_engineering import compose_context      # noqa: E402
from kb_tool import KB, parse_jsonl, root_context               # noqa: E402


# ── the kernel: a parsed chain ───────────────────────────────────────────────
@dataclass
class KernelNode:
    num: str
    name: str
    steps: list = field(default_factory=list)


@dataclass
class Kernel:
    name: str
    summary: str
    nodes: list = field(default_factory=list)
    closure: str = ""

    def node_filename(self, node: KernelNode) -> str:
        return f"{node.num}-{node.name.lower()}.md"


_HEAD = re.compile(r"^\s*\[([^\]]+)\]\s*:\s*")
_NODE = re.compile(r"(\d+)\.([A-Za-z_][A-Za-z0-9_]*)\s*:")
_STEP = re.compile(r"\d+[a-z]\.")


def metacompile(chain_text: str) -> Kernel:
    """Parse the chain notation into a Kernel. Deterministic — the prompt IS
    the program; the metacompiler just reads its structure."""
    m = _HEAD.match(chain_text)
    if not m:
        raise ValueError("not a chain: expected leading [Name]:")
    name = m.group(1).strip()
    rest = chain_text[m.end():]
    closure = ""
    if "results=>" in rest:
        rest, closure = rest.split("results=>", 1)
        closure = closure.strip()
    heads = list(_NODE.finditer(rest))
    if not heads:
        raise ValueError("chain has no numbered nodes")
    summary = rest[:heads[0].start()].strip().rstrip(":").strip()
    nodes = []
    for i, h in enumerate(heads):
        body = rest[h.end(): heads[i + 1].start() if i + 1 < len(heads)
                    else len(rest)]
        steps = [s.strip() for s in _STEP.split(body) if s.strip()]
        nodes.append(KernelNode(num=h.group(1), name=h.group(2), steps=steps))
    return Kernel(name=name, summary=summary, nodes=nodes, closure=closure)


# ── context assembly (CEL) ───────────────────────────────────────────────────
def node_context(kernel: Kernel, node: KernelNode, subject: str, kb: KB,
                 cycle_dir: Path, cycle_n: int) -> str:
    blocks = {
        "KERNEL": f"{kernel.name} — {kernel.summary}",
        "CYCLE": f"{cycle_n} · NODE {node.num}.{node.name}",
        "SUBJECT": subject,
        "THIS NODE'S STEPS (do them, in order)":
            "\n".join(f"{node.num}{chr(97+i)}. {s}"
                      for i, s in enumerate(node.steps)),
    }
    if kb.concepts:
        blocks["THE KB SO FAR (relative root of the subject — your ground)"] = \
            root_context(kb, subject, direction="both", max_nodes=40)
    prior = sorted(cycle_dir.glob("*.md"))
    if prior:
        blocks["THIS CYCLE SO FAR"] = "\n".join(
            f"--- {p.name} ---\n{p.read_text(encoding='utf-8')}"
            for p in prior)
    blocks["TASK"] = ("Produce this node's artifact as a complete markdown "
                      "document. Output ONLY the document.")
    return compose_context(blocks)


HARVEST_TASK = (
    "HARVEST this cycle: dump EVERY motif/concept that emerged (with a "
    "definition) and every link between them (and to concepts already in the "
    "KB). Output JSONL, one object per line, nothing else:\n"
    '{"c": "<snake_case_id>", "d": "<definition, 8+ chars>"}\n'
    '{"r": ["<source_id>", "<target_id>"]}\n'
    "Be exhaustive. No prose, no fences.")


def harvest_context(kernel: Kernel, subject: str, cycle_dir: Path,
                    cycle_n: int) -> str:
    return compose_context({
        "KERNEL": f"{kernel.name} — {kernel.summary}",
        "CYCLE": f"{cycle_n} · HARVEST (cycle end)",
        "SUBJECT": subject,
        "THE CYCLE'S ARTIFACTS": "\n".join(
            f"--- {p.name} ---\n{p.read_text(encoding='utf-8')}"
            for p in sorted(cycle_dir.glob("*.md"))),
        "TASK": HARVEST_TASK,
    })


# ── the runner ───────────────────────────────────────────────────────────────
async def _run_seat(seat_factory, prompt, tries=4, base=10):
    import inspect
    last = None
    for i in range(tries):
        try:
            out = seat_factory().run(prompt)
            if inspect.isawaitable(out):
                out = await out
            return out if isinstance(out, str) else str(out)
        except Exception as e:
            last = e
            await asyncio.sleep(base * (2 ** i))
    raise last


async def run_cycle(kernel: Kernel, subject: str, kb: KB, seat_factory,
                    root: Path, cycle_n: int) -> dict:
    cycle_dir = Path(root) / f"cycle{cycle_n}"
    cycle_dir.mkdir(parents=True, exist_ok=True)
    for node in kernel.nodes:                       # the walk; dir = the memo
        f = cycle_dir / kernel.node_filename(node)
        if f.exists() and f.read_text(encoding="utf-8").strip():
            continue
        out = await _run_seat(seat_factory,
                              node_context(kernel, node, subject, kb,
                                           cycle_dir, cycle_n))
        f.write_text(out, encoding="utf-8")
    harvest = await _run_seat(seat_factory,
                              harvest_context(kernel, subject, cycle_dir,
                                              cycle_n))
    (cycle_dir / "harvest.jsonl").write_text(harvest, encoding="utf-8")
    cs, rs = parse_jsonl(harvest)
    before = (len(kb.concepts), len(kb.relations))
    for c, d in cs.items():
        kb.add_concept(c, d, lib=f"{kernel.name.lower()}_c{cycle_n}")
    for s, t in rs:
        kb.add_relation(s, t)
    kb.save()
    chk = kb.check()                                # the prover mints the work
    new = (len(kb.concepts) - before[0]) + (len(kb.relations) - before[1])
    return {"cycle": cycle_n, "new_atoms": new,
            "kb": f"{len(kb.concepts)}c/{len(kb.relations)}r",
            "phase": chk["phase"], "worklist_define": len(chk["undefined"]),
            "worklist_connect": len(chk["orphan"])}


async def run_chain(kernel: Kernel, subject: str, seat_factory, root,
                    max_cycles: int = 5) -> dict:
    """Cycle until THE METER reads zero new atoms (the kernel's own
    stabilization criterion) or the budget runs out. The KB and every cycle's
    artifacts persist under root — resumable, accumulating, worklist-bearing."""
    root = Path(root)
    kb = KB(re.sub(r"[^a-z0-9_]+", "_", subject.lower()).strip("_")[:40] or
            "subject", root / "kb").load()
    rounds = []
    for n in range(1, max_cycles + 1):
        r = await run_cycle(kernel, subject, kb, seat_factory, root, n)
        rounds.append(r)
        if r["new_atoms"] == 0:
            break
    report = {"kernel": kernel.name, "subject": subject,
              "cycles": len(rounds),
              "stabilized": bool(rounds) and rounds[-1]["new_atoms"] == 0,
              "rounds": rounds}
    (root / "report.json").write_text(json.dumps(report, indent=2))
    return report


__all__ = ["metacompile", "run_chain", "run_cycle", "Kernel", "KernelNode"]
