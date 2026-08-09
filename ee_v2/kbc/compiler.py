#!/usr/bin/env python3
"""compiler.py — THE ONE CURRIED COMPILER (Isaac, 2026-08-09).

The whole system is a single partially-evaluated call:

    compile(kb, X, op) = seat.run( CEL.inject( TEMPLATE[op],
                                               relative_root(kb, X) ) ) → ΔKB
                         then kb.check()  (the gauge re-mints the worklist)

Every agent IS this compiler, curried:
  compile(kb, region,   "dump")      → a facet-dumper
  compile(kb, concept,  "define")    → a definer      (root = its consumers)
  compile(kb, orphan,   "connect")   → a wirer        (root = its neighborhood)
  compile(kb, batch,    "reconcile") → a deduper       (cheap-LLM, ~100 at a time)
  compile(kb, concept,  "expand")    → a sub-KB builder (root = its deps)  ← REFLEXIVE
  compile(kb, None,     "pick")      → the CEO         (chooses the next X)

There is no second kind of thing. The two hard parts are already bound: the
context is ALWAYS CEL(template[op], relative_root(X)); the acceptance is ALWAYS
the prover (kb.check). Everything between is one call. This is the
worker-binding spectrum (rule-05) fully collapsed, and — because X may be
"compiler" itself — the D∞ ≅ [D∞→D∞] fixpoint (lfpoop/dinfinity.py) as running
code: a thing that emits specialized versions of itself.

Built on Isaac's real CEL (`cave_teams.context_engineering.inject_context`,
native = compose_context) and the kb_tool primitives — NOT a parallel stack.
"""
from __future__ import annotations

import asyncio
import sys

from ._paths import ensure_deps
ensure_deps()

from cave_teams.context_engineering import compose_context     # THE CEL surface
# (compose_context is CEL's stable native assembler; inject_context resolves to
#  SDNA's transport-coupled variant when heaven is present — different signature.)
from .kb_tool import (KB, relative_root, root_context,           # noqa: E402
                     parse_jsonl, reconcile_scan)

# ── the op table: template + which direction the relative root is walked ─────
# (direction encodes what "grounding X for this op" MEANS — deps for building,
#  consumers for defining-to-contract, both for wiring.)
OPS = {
    "dump": dict(dir="both", jsonl='{"c":"<id>","d":"<def 8+>"} or '
                 '{"r":["<src>","<dst>"]}',
                 task="MASS-ENUMERATE the concept space of X: dump every "
                      "concept + relation that makes sense (aim 80+). "
                      "Reference concepts other regions will define by natural "
                      "snake_case name."),
    "define": dict(dir="consumers", jsonl='{"c":"<id>","d":"<def 8+>"}',
                   task="DEFINE X coherently with its REFERENCERS (its "
                        "contract, shown as the relative root)."),
    "connect": dict(dir="both", jsonl='{"r":["<X>","<existing>"]}',
                    task="WIRE X to ONE closely-related EXISTING concept from "
                         "its neighborhood (the relative root)."),
    "expand": dict(dir="deps", jsonl='{"c":"<id>","d":"<def 8+>"} or '
                   '{"r":["<src>","<dst>"]}',
                   task="EXPAND X into its own sub-ontology: enumerate the "
                        "concepts + relations INSIDE X, grounded in the "
                        "primitives it already depends on (the relative root)."),
}


def build_context(kb, X, op):
    """CEL assembles the context. The ONLY substantive input is the relative
    root of X — everything else is the fixed op template."""
    spec = OPS[op]
    root = (root_context(kb, X, direction=spec["dir"])
            if X is not None else "(no X — operate on the worklist)")
    return compose_context({
        "SUBJECT": kb.subject,
        "OPERATION": f"{op}: {spec['task']}",
        "X": str(X),
        "RELATIVE ROOT OF X (the LFP closure — your grounding; "
        "«undefined» marks the frontier)": root,
        "OUTPUT": f"Reply ONLY JSONL, one object per line: {spec['jsonl']}. "
                  "No prose, no fences.",
    })


async def _run(seat_factory, ctx, tries=4, base=10):
    last = None
    for i in range(tries):
        try:
            import inspect
            out = seat_factory().run(ctx)
            if inspect.isawaitable(out):
                out = await out
            return out if isinstance(out, str) else str(out)
        except Exception as e:
            last = e
            await asyncio.sleep(base * (2 ** i))
    raise last


async def compile(kb, X, op, seat_factory, lib=None):
    """THE CURRIED COMPILER. One call = one agent = context(op,root(X)) → seat
    → accrete → re-check. Returns the gauge verdict (the re-minted worklist
    shape). Monotone: only adds/wires, never silently drops."""
    if op == "reconcile":                 # the cheap-LLM dedup op (special I/O)
        groups = await reconcile_scan(kb, seat_factory,
                                      batch=100, max_batches=X)
        for g in groups:
            for dup in g[1:]:
                kb.merge_ids(g[0], dup)
        kb.save()
        return {"op": op, "folded": sum(len(g) - 1 for g in groups),
                **kb.check()}

    ctx = build_context(kb, X, op)
    cs, rs = parse_jsonl(await _run(seat_factory, ctx))
    added = sum(kb.add_concept(c, d, lib=lib or (X if op == "expand" else op))
                for c, d in cs.items())
    for s, t in rs:
        if op == "connect" and not (s in kb.concepts and t in kb.concepts):
            continue                       # connect wires EXISTING only
        kb.add_relation(s, t)
    kb.save()
    return {"op": op, "X": X, "added_concepts": added, "added_relations": len(rs),
            **kb.check()}


# ── the full cycle, expressed as curries of the ONE compiler ─────────────────
async def cycle(kb, regions, seat_factory, connect_budget=40):
    """dump → (prover mints worklist) → define → connect — every step a curry
    of compile(). This whole function is just scheduling; the intelligence is
    the one compiler + the prover."""
    await asyncio.gather(*[compile(kb, r, "dump", seat_factory, lib=r)
                           for r in regions])
    v = kb.check()
    for X in v["undefined"]:
        await compile(kb, X, "define", seat_factory)
    v = kb.check()
    for X in v["orphan"][:connect_budget]:
        await compile(kb, X, "connect", seat_factory)
    return kb.check()


__all__ = ["compile", "build_context", "cycle", "OPS"]
