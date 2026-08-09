"""heaven_tools.py — THE COMPILER AS AGENT-HELD CAPABILITY (issue onionmorph#3).

`make_kbc_tools(state_root, seat_factory=None)` returns HEAVEN TOOL CLASSES —
built with Isaac's own `make_heaven_tool_from_docstring` (schema from the
Google docstring, async-aware) — wrapping the SAME mounted command surface the
terminal drives, plus the durable brain (grow-gyri / ask). Hand the classes to
any heaven agent's `tools=[...]` and the agent operates the compiler itself:

    tools = make_kbc_tools("~/.onionmorph/kbc")
    MiniMaxRuntime(name="worker", tools=list(tools.values()), ...)

State binding: one workspace per factory call (a _Mounted over state_root +
a brain per KB under state_root/brains/<kb>, following the current-KB
pointer). kuzu law: one Database handle per path per process — brains are
cached in the closure. Seats for nested compiler work default to the stock
MiniMax runtime; inject `seat_factory(name)` to override.
"""
from __future__ import annotations

from pathlib import Path

from ._paths import ensure_deps
ensure_deps()

from .mount import _Mounted                                     # noqa: E402
from .kb_tool import derive_worklist                            # noqa: E402
from .brain import KbcBrain                                     # noqa: E402


def _default_seat_factory(name: str):
    from cave_teams.examples import MiniMaxRuntime
    return MiniMaxRuntime(name=f"kbc_{name}"[:24], tools=[],
                          system_prompt="", max_tokens=6000)


class _Host:
    def __init__(self, state_root, seat_factory):
        self.state_root = Path(state_root).expanduser()
        self._named = seat_factory or _default_seat_factory

    def seat_factory(self):
        return self._named("seat")


def make_kbc_tools(state_root, seat_factory=None) -> dict:
    """The factory: state_root ↦ {tool_name: BaseHeavenTool subclass}."""
    from heaven_base.make_heaven_tool_from_docstring import (
        make_heaven_tool_from_docstring)

    host = _Host(state_root, seat_factory)
    m = _Mounted(host)
    named = host._named
    brains: dict = {}                       # kb_name -> KbcBrain (kuzu law)

    def _brain() -> KbcBrain:
        name = m.current()
        if not name:
            raise ValueError("no current KB — kb_new or kb_use first")
        if name not in brains:
            brains[name] = KbcBrain(m.kb(), host.state_root / "brains" / name)
        return brains[name]

    # ── the capability functions (thin over the mounted handlers) ────────────
    async def kb_new(subject: str) -> str:
        """Create a new knowledge base for a subject and make it current.

        Args:
            subject (str): What the KB is about, e.g. "restaurant operations".
        """
        return await m.kb_new(subject)

    async def kb_use(name: str) -> str:
        """Switch the current knowledge base.

        Args:
            name (str): The KB name as shown by kb_list.
        """
        return await m.kb_use(name)

    async def kb_list() -> str:
        """List all knowledge bases with sizes; the arrow marks the current one."""
        return await m.kb_list("")

    async def kb_dump(facets: str = "") -> str:
        """Mass-enumerate concepts+relations into the current KB via LLM seats.

        Args:
            facets (str): Comma-separated facet names to dump in parallel;
                empty = one dump of the KB's own subject.
        """
        return await m.kb_dump(facets)

    async def kb_work() -> str:
        """Show the prover-minted worklist of the current KB: phase, size,
        and the define (referenced-but-undefined) and connect (orphan)
        backlogs."""
        return await m.kb_work("")

    async def kb_drain(kind: str = "define", budget: int = 100) -> str:
        """Drain worklist items of one kind through LLM seats.

        Args:
            kind (str): Which bucket — "define", "connect", or "reconcile".
            budget (int): Maximum items to drain this call.
        """
        return await m.kb_drain(f"{kind} {budget}")

    async def kb_root(atom: str) -> str:
        """Show an atom's relative root: the least-fixed-point closure of
        everything it bundles from, grouped by origin lib.

        Args:
            atom (str): The concept id to ground.
        """
        return await m.kb_root(atom)

    async def kb_expand(atom: str) -> str:
        """Expand a certified concept into its own sub-ontology (grounded in
        its relative root) and accrete it into the current KB.

        Args:
            atom (str): The certified concept id to expand.
        """
        return await m.kb_expand(atom)

    async def kb_project() -> str:
        """Project the current KB as a skilltree library of understand-*
        skills (call number = home class + dependency facets)."""
        return await m.kb_project("")

    async def kernel_list() -> str:
        """List the metacompiler kernels (chain-notation prompts) available."""
        return await m.kernel_list("")

    async def kernel_run(name: str, subject: str) -> str:
        """Run a metacompiled chain kernel over a subject: cycles of node
        walks + harvests into a persistent KB until the fixpoint meter reads
        stable or the budget ends.

        Args:
            name (str): Kernel name from kernel_list.
            subject (str): The subject to cycle the chain over.
        """
        return await m.kernel_run(f"{name} {subject}")

    async def brain_regions() -> str:
        """List the current KB's brain gyri (grown regions) and their count."""
        b = _brain()
        rs = b.regions()
        return f"{len(rs)} gyri: {', '.join(rs) or '(none — brain_grow first)'}"

    async def brain_grow(atom: str) -> str:
        """Grow a gyrus for a concept in the current KB's brain: thin atoms
        are proof-gated expanded first, then the region projects as tissue
        and wires into the activation graph — it becomes fireable.

        Args:
            atom (str): The concept id to grow a gyrus for.
        """
        r = await _brain().grow(atom, named)
        return (f"grown {r['atom']} (expanded={r['expanded']}) — "
                f"regions now: {', '.join(r['regions_now'])}")

    async def brain_ask(query: str) -> str:
        """Ask the current KB's brain: the graph fires matching gyri
        numerically, each answers over its tissue, constructions are
        prover-admitted, the synthesis is proven one level up (SES tower),
        and admitted use teaches the graph.

        Args:
            query (str): The question to ask the brain.
        """
        rep = await _brain().ask(query, named, log=lambda *_: None)
        if rep.get("error"):
            return f"[{rep['error']}] fired={rep.get('fired')}"
        return (f"fired={rep['fired']} · certified={list(rep['certified'])} "
                f"· synthesis_proven={rep['synthesis_proven']} "
                f"(SES {rep['ses_depth']}) · {rep['secs']}s\n\n"
                f"{rep['final_answer']}")

    def _syncify(afunc):
        """The canonical make_heaven_tool_from_docstring contract is SYNC
        functions (see heaven's dynamic-tool example). Our impls are async,
        so each wraps as a sync function running its own loop; heaven's
        sync path executes it via to_thread — the fresh loop lives in that
        thread. Converges with the intended usage, no upstream change."""
        import asyncio as _aio
        import functools

        @functools.wraps(afunc)
        def wrapper(*args, **kwargs):
            return _aio.run(afunc(*args, **kwargs))
        return wrapper

    fns = [kb_new, kb_use, kb_list, kb_dump, kb_work, kb_drain, kb_root,
           kb_expand, kb_project, kernel_list, kernel_run,
           brain_regions, brain_grow, brain_ask]
    return {f.__name__: make_heaven_tool_from_docstring(_syncify(f))
            for f in fns}


__all__ = ["make_kbc_tools"]
