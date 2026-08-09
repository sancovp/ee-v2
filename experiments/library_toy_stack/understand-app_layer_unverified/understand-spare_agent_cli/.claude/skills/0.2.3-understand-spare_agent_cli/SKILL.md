---
name: 0.2.3-understand-spare_agent_cli
description: [0.2.3] the spare agent packed as a CLI so it can be projected into interface families
---

# understand-spare_agent_cli

**CALL NUMBER:** `app_layer_unverified.spare_agent_cli : ee_v2_layer(9), map_layer(5)`
**DEFINITION:** the spare agent packed as a CLI so it can be projected into interface families

Invoke this skill to understand `spare_agent_cli` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `app_layer_unverified`
- **spare_agent** (d1): the agent whose operating loop is the sigil chain: intent, compress, release, emergence, selection, closure
- **orchestrator_chain** (d2): the runner of runs itself operates by the same chain: release = async dispatch, emergence = returned artifacts

### from `ee_v2_layer`
- **metacompiler** (d2): parses any chain-notation prompt into a kernel and runs it as a gated cycling KB compiler
- **curried_compiler** (d3): compile(kb, X, op): CEL context from the relative root of X, one seat, accrete, re-check — every agent is this curried
- **cycle** (d3): one walk of a kernel's nodes by fresh seats, ending in a harvest
- **kernel** (d3): a parsed recursive chain: named nodes with substeps plus a closure clause
- **relative_root** (d4): the least-fixed-point closure of everything X bundles from, walked to prims or to consumers, tagged by origin lib
- **fixpoint_meter** (d4): zero newly-accreted structure across a cycle = stabilized; the kernel's own closure clause, measured
- **harvest** (d4): the cycle-end dump of emerged concepts and relations into the persistent KB
- **chain_notation** (d4): the [Name]: N.Node: Na.step format — a prompt whose structure IS the program
- **worklist** (d5): the prover-minted backlog: define (referenced-but-undefined), connect (orphans), reconcile (near-duplicates)

### from `map_layer`
- **map_prover** (d5): SWI-Prolog closed-world checker behind a typed construction boundary; the consistency typer for everything the seats emit
- **authority_split** (d6): seats author candidate facts only; the engine holds source facts; a seat can never witness itself
- **certificate** (d6): a replayable proof envelope over a construction: subject, payload, kappa, sha — monotone, never uncertifies
- **consistency_typing** (d6): the KB cannot become internally inconsistent: every emission passes the typer or its violations are named
- **soup_frontier** (d6): the named violations when a construction fails: dangling, orphan, ungrounded — the retry signal and the work queue

## CONSUMERS (what needs this)
`api2treeshell_projector`

---
*Projected from the `the_toy_stack` KB (57 concepts / 84 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
