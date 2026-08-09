---
name: 0.2.2-understand-spare_agent
description: [0.2.2] the agent whose operating loop is the sigil chain: intent, compress, release, emergence, selection, closure
---

# understand-spare_agent

**CALL NUMBER:** `app_layer_unverified.spare_agent : ee_v2_layer(9), map_layer(5)`
**DEFINITION:** the agent whose operating loop is the sigil chain: intent, compress, release, emergence, selection, closure

Invoke this skill to understand `spare_agent` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `app_layer_unverified`
- **orchestrator_chain** (d1): the runner of runs itself operates by the same chain: release = async dispatch, emergence = returned artifacts

### from `ee_v2_layer`
- **metacompiler** (d1): parses any chain-notation prompt into a kernel and runs it as a gated cycling KB compiler
- **curried_compiler** (d2): compile(kb, X, op): CEL context from the relative root of X, one seat, accrete, re-check — every agent is this curried
- **cycle** (d2): one walk of a kernel's nodes by fresh seats, ending in a harvest
- **kernel** (d2): a parsed recursive chain: named nodes with substeps plus a closure clause
- **relative_root** (d3): the least-fixed-point closure of everything X bundles from, walked to prims or to consumers, tagged by origin lib
- **fixpoint_meter** (d3): zero newly-accreted structure across a cycle = stabilized; the kernel's own closure clause, measured
- **harvest** (d3): the cycle-end dump of emerged concepts and relations into the persistent KB
- **chain_notation** (d3): the [Name]: N.Node: Na.step format — a prompt whose structure IS the program
- **worklist** (d4): the prover-minted backlog: define (referenced-but-undefined), connect (orphans), reconcile (near-duplicates)

### from `map_layer`
- **map_prover** (d4): SWI-Prolog closed-world checker behind a typed construction boundary; the consistency typer for everything the seats emit
- **authority_split** (d5): seats author candidate facts only; the engine holds source facts; a seat can never witness itself
- **certificate** (d5): a replayable proof envelope over a construction: subject, payload, kappa, sha — monotone, never uncertifies
- **consistency_typing** (d5): the KB cannot become internally inconsistent: every emission passes the typer or its violations are named
- **soup_frontier** (d5): the named violations when a construction fails: dangling, orphan, ungrounded — the retry signal and the work queue

## CONSUMERS (what needs this)
`spare_agent_cli`

---
*Projected from the `the_toy_stack` KB (57 concepts / 84 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
