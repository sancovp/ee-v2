#!/usr/bin/env python3
"""projector.py — PROJECT THE CERTIFIED KB AS A SKILLTREE LIBRARY
(Isaac, 2026-08-09: "project the algebras/webs to file *as skill files*,
call them understand-{x}, literally just use skilltree... layer them by
domain -> subdomain -> process... use some library science for notation").

Every certified region of the KB projects to an `understand-{x}` SKILL — a
self-contained, loadable unit of competence whose body is X + its RELATIVE
ROOT (the LFP import cone, its prims from other libs). skilltree shelves them:

    domain (root)  ->  subdomain (lib/facet)  ->  understand-{x} (process)

NOTATION (library science): skilltree's hierarchical coordinate IS the
Dewey-style HOME address (one shelf per skill); the cross-lib imports of the
relative root are RANGANATHAN FACETS (colon classification) — a concept lives
in ONE home class but imports facets from others, so the call number is

    <coord> <home-lib>.<x> : <facet-lib>(n), <facet-lib>(n), ...

i.e. THE CALL NUMBER AND THE DEPENDENCY WEB ARE THE SAME OBJECT. Navigation =
walk the tree; retrieval = skilltree's FTS5/BM25 index (build_index) — the
"production KB" (file projection + skilltree RAG) in seconds, no LLM calls.

All Isaac's machinery: skilltree (TreeNode/materialize/emit/build_index) +
kb_tool (KB/relative_root). The projector is pure glue.
"""
from __future__ import annotations

import sys
from collections import Counter, defaultdict
from pathlib import Path

from ._paths import ensure_deps
ensure_deps()

from skilltree import SkillTree, TreeNode, build_index          # noqa: E402
from skilltree.materialize import materialize                    # noqa: E402
from skilltree.cohere import emit                                # noqa: E402
from .kb_tool import KB, relative_root                            # noqa: E402


# ── the call number: home address + Ranganathan facets ───────────────────────
def facets_of(kb: KB, x: str, max_nodes: int = 200):
    """The cross-lib imports of x's relative root = its facets, with weights."""
    home = kb.lib.get(x)
    cone = relative_root(kb, x, direction="deps", max_nodes=max_nodes)
    counts = Counter(l for _, _, l, _ in cone if l and l != home)
    return home, cone, counts


def call_number(kb: KB, x: str):
    home, cone, fac = facets_of(kb, x)
    facet_str = ", ".join(f"{l}({n})" for l, n in fac.most_common())
    return f"{home or '?'}.{x}" + (f" : {facet_str}" if facet_str else ""), cone, fac


# ── one skill body ───────────────────────────────────────────────────────────
def skill_body(kb: KB, x: str) -> str:
    cn, cone, fac = call_number(kb, x)
    defn = kb.concepts.get(x, "«undefined — frontier»")
    consumers = sorted({s for s, t in kb.relations if t == x})[:20]
    by_lib = defaultdict(list)
    for cid, d, lib, depth in cone:
        by_lib[lib or "?"].append((cid, d, depth))
    lines = [
        f"# understand-{x}",
        "",
        f"**CALL NUMBER:** `{cn}`",
        f"**DEFINITION:** {defn}",
        "",
        "Invoke this skill to understand `" + x + "` down to its primitives. "
        "The RELATIVE ROOT below is the least-fixed-point closure of "
        "everything it bundles from — the full import cone, grouped by the "
        "lib each prim comes from. Projected from a prover-typed KB "
        "(MAP/SWI-Prolog consistency gate): every reference below resolves.",
        "",
        "## THE RELATIVE ROOT (the import cone, by lib)",
    ]
    for lib in sorted(by_lib):
        lines.append(f"\n### from `{lib}`")
        for cid, d, depth in by_lib[lib][:25]:
            lines.append(f"- **{cid}** (d{depth}): {d or '«undefined»'}")
    if consumers:
        lines += ["", "## CONSUMERS (what needs this)",
                  ", ".join(f"`{c}`" for c in consumers)]
    lines += ["", "---",
              f"*Projected from the `{kb.subject}` KB "
              f"({len(kb.concepts)} concepts / {len(kb.relations)} relations) "
              "— consistency-typed by MAP; the facet list after the colon IS "
              "the cross-lib dependency web.*"]
    return "\n".join(lines)


# ── the shelf: domain -> subdomain(lib) -> understand-{x} ────────────────────
def _stage(staging: Path, name: str, body: str) -> str:
    """skill_src is a SOURCE DIR containing a SKILL.md (materialize re-emits
    frontmatter + breadcrumbs itself) — stage each body as one."""
    d = staging / name
    d.mkdir(parents=True, exist_ok=True)
    (d / "SKILL.md").write_text(body, encoding="utf-8")
    return str(d)


def project_library(kb: KB, out_root, per_lib: int = 6):
    out_root = Path(out_root)
    staging = out_root.parent / f"_staging_{out_root.name}"
    deg = Counter()
    for s, t in kb.relations:
        deg[s] += 1
        deg[t] += 1
    libs = defaultdict(list)
    for c in kb.concepts:
        libs[kb.lib.get(c) or "core"].append(c)
    lib_nodes = []
    n_skills = 0
    for lib in sorted(libs):
        top = sorted(libs[lib], key=lambda c: -deg[c])[:per_lib]
        kids = []
        for x in top:
            kids.append(TreeNode(
                name=f"understand-{x}",
                description=(kb.concepts.get(x, "")[:110] or f"understand {x}"),
                skill_src=_stage(staging, f"understand-{x}",
                                 skill_body(kb, x))))
            n_skills += 1
        lib_nodes.append(TreeNode(
            name=f"understand-{lib}",
            description=f"the {lib} subdomain of {kb.subject} "
                        f"({len(libs[lib])} concepts)",
            skill_src=_stage(staging, f"understand-{lib}",
                             f"# understand-{lib}\n\nSubdomain shelf: the top "
                             f"{len(kids)} load-bearing concepts of `{lib}` "
                             f"in `{kb.subject}`. Descend to an "
                             "`understand-{x}` leaf for the full import cone."),
            children=kids))
    root = TreeNode(
        name=f"understand-{kb.subject}",
        description=f"the {kb.subject} library — every skill a certified "
                    "region of the KB; call number = home : facets",
        skill_src=_stage(staging, f"understand-{kb.subject}",
                         f"# understand-{kb.subject}\n\nTHE LIBRARY. domain "
                         "-> subdomain -> process; each leaf is "
                         "`understand-{x}` = X + its LFP relative root. The "
                         "coordinate is the home address; the facets after "
                         "the colon are the cross-lib dependency web."),
        children=lib_nodes)
    tree = SkillTree(root)
    out = materialize(tree, out_root, coords=True)
    emit(out)                              # cohere breadcrumbs + index
    return out, n_skills


# ── the SECOND render target: brain tissue (brain-agent from_dir format) ─────
def project_brain_tissue(kb, atoms, out_dir, cone_chunks: int = 8):
    """Project regions as BRAIN TISSUE: flat dirs of .md chunk files — exactly
    brain-agent's `from_dir` format (subdirs auto-adopt as sub-brains; no
    .claude nesting, no leading-dot names). One dir per atom = one gyrus:
    the atom's own chunk + its cone's top concepts as sibling chunks.
    Returns {atom: dir}."""
    from pathlib import Path
    out_dir = Path(out_dir)
    made = {}
    for atom in atoms:
        d = out_dir / atom
        d.mkdir(parents=True, exist_ok=True)
        cn, cone, _ = call_number(kb, atom)
        (d / f"{atom}.md").write_text(
            f"# {atom}\n\nCALL NUMBER: `{cn}`\n\n"
            f"{kb.concepts.get(atom, '«undefined»')}\n", encoding="utf-8")
        for cid, defn, lib, depth in cone[:cone_chunks]:
            (d / f"{cid}.md").write_text(
                f"# {cid}\n\n[{lib or '?'} · d{depth}] "
                f"{defn or '«undefined»'}\n", encoding="utf-8")
        made[atom] = str(d)
    return made
