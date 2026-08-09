"""mount.py — THE FUNCTOR (Isaac, 2026-08-09: "A that's good enough to be
Functor, then F: A -> AnyLikeB, then A-F->B naturally").

NOT a point-to-point join. `mount(host)` applies the whole compiler command
surface to ANY host that satisfies the (duck-typed) HOST PROTOCOL:

    host.seat_factory() -> seat with .run(prompt) (sync or async)
    host.state_root     -> Path-like dir (KBs + kernels live under it)
    host.emit(event)    -> optional; called with {"type", ...} dicts so a
                           host's faces can render compiler activity

It returns {command_name: async handler(args_str) -> str}. The host owns
dispatch (a terminal ladder, a tool wrapper, a department skill — whatever
that host's idiom is). OM is the first object this functor is applied to;
cave-teams / dark-factory are later objects of the SAME functor — the
integration is written once, here, host-agnostically.

State layout under host.state_root:
    kbs/<name>/            persistent KBs (kb_tool layout)
    kernels/<name>.txt     dropped-in chain prompts (the metacompiler eats)
    libraries/<kb_name>/   projected understand-* skilltrees
    current_kb             the current-KB pointer (mirrors a chat runtime's
                           current-conversation pointer — the two gauges'
                           twin cursors)
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from ._paths import ensure_deps
ensure_deps()

from .kb_tool import (KB, derive_worklist, work_session, relative_root,
                      root_context)
from .compiler import compile as kbc_compile
from .metacompiler import metacompile, run_chain
from .projector import project_library

HOST_PROTOCOL = ("seat_factory", "state_root")   # emit is optional


def _slug(x: str) -> str:
    return re.sub(r"[^a-z0-9_]+", "_", x.strip().lower()).strip("_")[:48]


class _Mounted:
    def __init__(self, host):
        for attr in HOST_PROTOCOL:
            if not hasattr(host, attr):
                raise TypeError(f"host lacks {attr!r} (HOST_PROTOCOL)")
        self.host = host
        self.root = Path(host.state_root)
        (self.root / "kbs").mkdir(parents=True, exist_ok=True)
        (self.root / "kernels").mkdir(exist_ok=True)
        (self.root / "libraries").mkdir(exist_ok=True)

    # ── plumbing ─────────────────────────────────────────────────────────────
    def _emit(self, **event):
        emit = getattr(self.host, "emit", None)
        if callable(emit):
            emit(event)

    def _cur_path(self) -> Path:
        return self.root / "current_kb"

    def current(self) -> str | None:
        p = self._cur_path()
        return p.read_text().strip() if p.exists() else None

    def kb(self, name: str | None = None) -> KB:
        name = name or self.current()
        if not name:
            raise ValueError("no current KB — /kb new <subject> or /kb use "
                             "<name> first")
        return KB(name, self.root / "kbs" / name).load()

    # ── the command surface ──────────────────────────────────────────────────
    async def kb_new(self, args: str) -> str:
        subject = args.strip()
        if not subject:
            return "usage: kb new <subject>"
        name = _slug(subject)
        kb = KB(subject, self.root / "kbs" / name)
        kb.save()
        self._cur_path().write_text(name)
        self._emit(type="kb_new", kb=name, subject=subject)
        return f"KB {name!r} created (subject: {subject}) — now current."

    async def kb_use(self, args: str) -> str:
        name = _slug(args)
        if not (self.root / "kbs" / name).exists():
            return f"no KB {name!r} — see: kb list"
        self._cur_path().write_text(name)
        return f"current KB = {name}"

    async def kb_list(self, args: str) -> str:
        cur = self.current()
        rows = []
        for d in sorted((self.root / "kbs").iterdir()):
            if d.is_dir():
                kb = KB(d.name, d).load()
                mark = "→" if d.name == cur else " "
                rows.append(f"{mark} {d.name}  ({len(kb.concepts)}c/"
                            f"{len(kb.relations)}r)")
        return "\n".join(rows) or "(no KBs yet — kb new <subject>)"

    async def kb_dump(self, args: str) -> str:
        kb = self.kb()
        facets = [f.strip() for f in args.split(",") if f.strip()] or [kb.subject]
        for f in facets:
            v = await kbc_compile(kb, f, "dump", self.host.seat_factory,
                                  lib=_slug(f))
        self._emit(type="kb_dump", kb=self.current(), facets=facets,
                   concepts=v["n_concepts"])
        return (f"dumped {len(facets)} facet(s) → {v['n_concepts']}c/"
                f"{v['n_relations']}r · phase={v['phase']} · "
                f"define={len(v['undefined'])} connect={len(v['orphan'])}")

    async def kb_work(self, args: str) -> str:
        wl = derive_worklist(self.kb())
        return (f"phase={wl['phase']} · {wl['n_concepts']}c/"
                f"{wl['n_relations']}r\n"
                f"define ({len(wl['define'])}): "
                + ", ".join(wl["define"][:15])
                + ("…" if len(wl["define"]) > 15 else "") + "\n"
                f"connect ({len(wl['connect'])}): "
                + ", ".join(wl["connect"][:15])
                + ("…" if len(wl["connect"]) > 15 else ""))

    async def kb_drain(self, args: str) -> str:
        parts = args.split()
        kind = parts[0] if parts else "define"
        budget = int(parts[1]) if len(parts) > 1 else 100
        r = await work_session(self.kb(), self.host.seat_factory,
                               budget=budget, do=(kind,))
        self._emit(type="kb_drain", kb=self.current(), kind=kind, did=r["did"])
        return (f"drained {kind}: did={r['did']} · "
                f"backlog define {r['before']['define']}→{r['after']['define']}"
                f" connect {r['before']['connect']}→{r['after']['connect']}")

    async def kb_root(self, args: str) -> str:
        atom = _slug(args)
        if not atom:
            return "usage: kb root <atom>"
        return root_context(self.kb(), atom, direction="both", max_nodes=40)

    async def kb_expand(self, args: str) -> str:
        atom = _slug(args)
        kb = self.kb()
        if atom not in kb.concepts:
            return f"{atom!r} is not a certified concept in the current KB"
        v = await kbc_compile(kb, atom, "expand", self.host.seat_factory)
        self._emit(type="kb_expand", kb=self.current(), atom=atom)
        return (f"expanded {atom}: +{v['added_concepts']}c/"
                f"+{v['added_relations']}r · phase={v['phase']}")

    async def kb_project(self, args: str) -> str:
        name = self.current()
        out, n = project_library(self.kb(),
                                 self.root / "libraries" / name)
        self._emit(type="kb_project", kb=name, skills=n)
        return f"library projected: {out} ({n} understand-* skills)"

    async def kernel_list(self, args: str) -> str:
        ks = sorted((self.root / "kernels").glob("*.txt"))
        return "\n".join(k.stem for k in ks) or "(no kernels — drop " \
            "<name>.txt chain files into kernels/)"

    async def kernel_run(self, args: str) -> str:
        parts = args.split(None, 1)
        if len(parts) < 2:
            return "usage: kernel run <name> <subject>"
        kname, subject = parts
        kp = self.root / "kernels" / f"{kname}.txt"
        if not kp.exists():
            return f"no kernel {kname!r} — see: kernel list"
        kernel = metacompile(kp.read_text())
        run_root = self.root / "kbs" / f"{_slug(subject)}__{_slug(kname)}"
        r = await run_chain(kernel, subject, self.host.seat_factory,
                            run_root, max_cycles=3)
        self._cur_path().write_text(run_root.name)
        self._emit(type="kernel_run", kernel=kname, subject=subject,
                   report=r)
        return (f"{kernel.name} × {subject!r}: {r['cycles']} cycle(s), "
                f"stabilized={r['stabilized']}\n"
                + "\n".join(f"  c{x['cycle']}: +{x['new_atoms']} atoms "
                            f"({x['kb']}, {x['phase']})" for x in r["rounds"])
                + f"\ncurrent KB = {run_root.name}")


def mount(host) -> dict:
    """Apply the functor: host ↦ {command: handler}. The host owns dispatch."""
    m = _Mounted(host)
    return {
        "kb new": m.kb_new, "kb use": m.kb_use, "kb list": m.kb_list,
        "kb dump": m.kb_dump, "kb work": m.kb_work, "kb drain": m.kb_drain,
        "kb root": m.kb_root, "kb expand": m.kb_expand,
        "kb project": m.kb_project,
        "kernel list": m.kernel_list, "kernel run": m.kernel_run,
    }


__all__ = ["mount", "HOST_PROTOCOL"]
