#!/usr/bin/env python3
"""stack_kb.py — THE COLLAPSE (Isaac, 2026-08-09): instead of building the
long-wise integration chain (agent→CLI→treeshell→substrates→skilltomes→
publishing) in code first, WRITE THE KB OF IT NOW, prove it FROM the KB
(fortification), and let the prover's worklist BE the build backlog — the
dogfooding feedback loop, shown. Code gets bound per-region only when the
RECOMPILATION LAW fires: "you only turn it into code when you need the LLMs
to output that stuff WITHOUT looking it up — that's when you re-compile a
new system. Reproduce with specialization."

The dump below is authored (the LLM writing the representation — that IS the
method); provenance is honest per-lib: local-verified systems vs
Isaac-described-only (treeshell internals — not cloned here). What the
authored dump references but fails to define, the prover mints as work.
"""
import sys
from pathlib import Path

sys.path.insert(0, "/home/ceo/repo/ee-v2/experiments")

from kb_tool import KB, derive_worklist                          # noqa: E402
from projector import project_library                            # noqa: E402

ROOT = Path(__file__).resolve().parent / "kb_toy_stack"

# lib → (verified_locally?, concepts {id: definition})
DUMP = {
 "ee_v2_layer": (True, {
  "metacompiler": "parses any chain-notation prompt into a kernel and runs it as a gated cycling KB compiler",
  "kernel": "a parsed recursive chain: named nodes with substeps plus a closure clause",
  "chain_notation": "the [Name]: N.Node: Na.step format — a prompt whose structure IS the program",
  "cycle": "one walk of a kernel's nodes by fresh seats, ending in a harvest",
  "harvest": "the cycle-end dump of emerged concepts and relations into the persistent KB",
  "fixpoint_meter": "zero newly-accreted structure across a cycle = stabilized; the kernel's own closure clause, measured",
  "curried_compiler": "compile(kb, X, op): CEL context from the relative root of X, one seat, accrete, re-check — every agent is this curried",
  "relative_root": "the least-fixed-point closure of everything X bundles from, walked to prims or to consumers, tagged by origin lib",
  "worklist": "the prover-minted backlog: define (referenced-but-undefined), connect (orphans), reconcile (near-duplicates)",
  "library_projection": "project the certified KB as understand-X skilltree skills; call number = home class colon facets = the dependency web",
  "understand_skill": "a loadable unit of competence: X plus its relative root, consistency-typed",
  "ee_journey": "the 72-node emergence-engine walk: dir-is-the-state, per-order horizon, gated emissions",
 }),
 "map_layer": (True, {
  "map_prover": "SWI-Prolog closed-world checker behind a typed construction boundary; the consistency typer for everything the seats emit",
  "certificate": "a replayable proof envelope over a construction: subject, payload, kappa, sha — monotone, never uncertifies",
  "soup_frontier": "the named violations when a construction fails: dangling, orphan, ungrounded — the retry signal and the work queue",
  "consistency_typing": "the KB cannot become internally inconsistent: every emission passes the typer or its violations are named",
  "authority_split": "seats author candidate facts only; the engine holds source facts; a seat can never witness itself",
 }),
 "skilltree_lib": (True, {
  "skilltree": "coordinate-addressed tree of skill dirs wired by Read-tool breadcrumbs, with validation and an FTS5 index",
  "skilltree_coordinate": "the hierarchical address of a node: root 0, child i = parent.i — the home class of the call number",
  "skilltree_rag": "build_index: one FTS5/BM25 table over every SKILL.md — retrieval returns ranked hits with shelf addresses",
  "skilltome": "skilltree.tome: fold a skilltree into a single tome document — the bound volume of a library",
 }),
 "treeshell_lib": (False, {
  "treeshell": "the tree REPL shell family (sancovp/heaven-tree-repl): navigable node-tree interfaces over agents and tools",
  "api2treeshell_projector": "treeshell's projector that lifts an API or CLI into a treeshell node family",
  "monoidal_substrate_projection": "treeshell's monoidal category system: project one shell across substrates compositionally",
 }),
 "publishing_lib": (False, {
  "scalable_publishing": "the sra-git publishing system: renders and distributes artifacts at scale from canonical sources",
 }),
 "app_layer": (False, {
  "toy_app": "the single public app that knows the whole stack and speaks the chain protocol — the neurosymbolic demonstration artifact",
  "spare_agent": "the agent whose operating loop is the sigil chain: intent, compress, release, emergence, selection, closure",
  "spare_agent_cli": "the spare agent packed as a CLI so it can be projected into interface families",
  "chain_protocol": "the human-interaction contract: state a desire, release, receive emergence, select branches, revise, re-enter",
  "orchestrator_chain": "the runner of runs itself operates by the same chain: release = async dispatch, emergence = returned artifacts",
  "reality_join": "the loop closes through the human's real desire in and real artifacts out — simulation and observable reality as one feedback chain",
 }),
 "law": (True, {
  "futamura_tower": "the projection ladder: specializing an interpreter to a program yields a compiler; specializing the specializer compounds",
  "recompilation_law": "bind a KB region to code only when its output is needed without lookup — reproduce with specialization",
  "dogfooding_loop": "run the system on its own design KB: proving the plan fortifies the plan and mints its backlog",
  "way_of_life_framework": "the usage discipline for agents distilled from the worked example: KBs first, compile on demand, worklists drained on heartbeats",
  "collapse_principle": "every planned integration is first a certified KB region, not code — the long-wise reification is skipped until the law fires",
 }),
}

# the integration edges — Isaac's sentence as relations
RELS = [
 # the toy contains/runs the stack
 ("toy_app", "metacompiler"), ("toy_app", "chain_protocol"),
 ("toy_app", "orchestrator_chain"), ("toy_app", "library_projection"),
 ("toy_app", "worklist"), ("toy_app", "reality_join"),
 ("spare_agent", "orchestrator_chain"), ("spare_agent", "metacompiler"),
 ("spare_agent_cli", "spare_agent"),
 # the treeshell projection chain
 ("api2treeshell_projector", "spare_agent_cli"),
 ("api2treeshell_projector", "treeshell"),
 ("monoidal_substrate_projection", "treeshell"),
 # the library/publishing chain
 ("library_projection", "understand_skill"),
 ("library_projection", "skilltree"),
 ("understand_skill", "relative_root"),
 ("skilltree", "skilltree_coordinate"), ("skilltree", "skilltree_rag"),
 ("skilltome", "skilltree"), ("scalable_publishing", "skilltome"),
 # the engine internals
 ("metacompiler", "kernel"), ("kernel", "chain_notation"),
 ("metacompiler", "cycle"), ("cycle", "harvest"),
 ("cycle", "fixpoint_meter"), ("harvest", "worklist"),
 ("curried_compiler", "relative_root"), ("metacompiler", "curried_compiler"),
 ("ee_journey", "metacompiler"),
 # MAP under everything
 ("harvest", "map_prover"), ("worklist", "soup_frontier"),
 ("map_prover", "certificate"), ("map_prover", "soup_frontier"),
 ("map_prover", "consistency_typing"), ("map_prover", "authority_split"),
 ("understand_skill", "certificate"),
 # the laws bind the plan
 ("recompilation_law", "futamura_tower"),
 ("collapse_principle", "recompilation_law"),
 ("dogfooding_loop", "collapse_principle"),
 ("way_of_life_framework", "dogfooding_loop"),
 ("way_of_life_framework", "chain_protocol"),
 ("toy_app", "way_of_life_framework"),
 # deliberately-referenced future pieces (children of the plan):
 ("toy_app", "meta_metacompiler"),          # the compiler ABOUT combining libs
 ("scalable_publishing", "grand_argument_kernel"),
 ("monoidal_substrate_projection", "substrate_family"),
]

if __name__ == "__main__":
    kb = KB("the_toy_stack", ROOT)
    for lib, (verified, concepts) in DUMP.items():
        tag = lib if verified else f"{lib}_unverified"
        for c, d in concepts.items():
            kb.add_concept(c, d, lib=tag)
    for s, t in RELS:
        kb.add_relation(s, t)
    kb.save()
    wl = derive_worklist(kb)
    print(f"KB: {wl['n_concepts']} concepts / {wl['n_relations']} relations "
          f"→ {wl['phase']}")
    print(f"THE BACKLOG (prover-minted): define={wl['define']} "
          f"connect={wl['connect']}")
    out, n = project_library(kb, ROOT.parent / "library_toy_stack", per_lib=8)
    print(f"LIBRARY: {out} ({n} understand-* skills)")
