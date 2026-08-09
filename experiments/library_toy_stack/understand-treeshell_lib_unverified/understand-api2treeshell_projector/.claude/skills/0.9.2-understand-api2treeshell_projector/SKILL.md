---
name: 0.9.2-understand-api2treeshell_projector
description: [0.9.2] treeshell's projector that lifts an API or CLI into a treeshell node family
---

# understand-api2treeshell_projector

**CALL NUMBER:** `treeshell_lib_unverified.api2treeshell_projector : ee_v2_layer(9), map_layer(5), app_layer_unverified(3)`
**DEFINITION:** treeshell's projector that lifts an API or CLI into a treeshell node family

Invoke this skill to understand `api2treeshell_projector` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `app_layer_unverified`
- **spare_agent_cli** (d1): the spare agent packed as a CLI so it can be projected into interface families
- **spare_agent** (d2): the agent whose operating loop is the sigil chain: intent, compress, release, emergence, selection, closure
- **orchestrator_chain** (d3): the runner of runs itself operates by the same chain: release = async dispatch, emergence = returned artifacts

### from `ee_v2_layer`
- **metacompiler** (d3): parses any chain-notation prompt into a kernel and runs it as a gated cycling KB compiler
- **curried_compiler** (d4): compile(kb, X, op): CEL context from the relative root of X, one seat, accrete, re-check — every agent is this curried
- **cycle** (d4): one walk of a kernel's nodes by fresh seats, ending in a harvest
- **kernel** (d4): a parsed recursive chain: named nodes with substeps plus a closure clause
- **relative_root** (d5): the least-fixed-point closure of everything X bundles from, walked to prims or to consumers, tagged by origin lib
- **fixpoint_meter** (d5): zero newly-accreted structure across a cycle = stabilized; the kernel's own closure clause, measured
- **harvest** (d5): the cycle-end dump of emerged concepts and relations into the persistent KB
- **chain_notation** (d5): the [Name]: N.Node: Na.step format — a prompt whose structure IS the program
- **worklist** (d6): the prover-minted backlog: define (referenced-but-undefined), connect (orphans), reconcile (near-duplicates)

### from `map_layer`
- **map_prover** (d6): SWI-Prolog closed-world checker behind a typed construction boundary; the consistency typer for everything the seats emit
- **authority_split** (d7): seats author candidate facts only; the engine holds source facts; a seat can never witness itself
- **certificate** (d7): a replayable proof envelope over a construction: subject, payload, kappa, sha — monotone, never uncertifies
- **consistency_typing** (d7): the KB cannot become internally inconsistent: every emission passes the typer or its violations are named
- **soup_frontier** (d7): the named violations when a construction fails: dangling, orphan, ungrounded — the retry signal and the work queue

### from `treeshell_lib_unverified`
- **treeshell** (d1): the tree REPL shell family (sancovp/heaven-tree-repl): navigable node-tree interfaces over agents and tools

---
*Projected from the `the_toy_stack` KB (51 concepts / 73 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
