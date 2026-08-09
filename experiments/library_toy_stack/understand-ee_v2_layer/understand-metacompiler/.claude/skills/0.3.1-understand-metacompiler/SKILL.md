---
name: 0.3.1-understand-metacompiler
description: [0.3.1] parses any chain-notation prompt into a kernel and runs it as a gated cycling KB compiler
---

# understand-metacompiler

**CALL NUMBER:** `ee_v2_layer.metacompiler : map_layer(5)`
**DEFINITION:** parses any chain-notation prompt into a kernel and runs it as a gated cycling KB compiler

Invoke this skill to understand `metacompiler` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `ee_v2_layer`
- **curried_compiler** (d1): compile(kb, X, op): CEL context from the relative root of X, one seat, accrete, re-check — every agent is this curried
- **cycle** (d1): one walk of a kernel's nodes by fresh seats, ending in a harvest
- **kernel** (d1): a parsed recursive chain: named nodes with substeps plus a closure clause
- **relative_root** (d2): the least-fixed-point closure of everything X bundles from, walked to prims or to consumers, tagged by origin lib
- **fixpoint_meter** (d2): zero newly-accreted structure across a cycle = stabilized; the kernel's own closure clause, measured
- **harvest** (d2): the cycle-end dump of emerged concepts and relations into the persistent KB
- **chain_notation** (d2): the [Name]: N.Node: Na.step format — a prompt whose structure IS the program
- **worklist** (d3): the prover-minted backlog: define (referenced-but-undefined), connect (orphans), reconcile (near-duplicates)

### from `map_layer`
- **map_prover** (d3): SWI-Prolog closed-world checker behind a typed construction boundary; the consistency typer for everything the seats emit
- **authority_split** (d4): seats author candidate facts only; the engine holds source facts; a seat can never witness itself
- **certificate** (d4): a replayable proof envelope over a construction: subject, payload, kappa, sha — monotone, never uncertifies
- **consistency_typing** (d4): the KB cannot become internally inconsistent: every emission passes the typer or its violations are named
- **soup_frontier** (d4): the named violations when a construction fails: dangling, orphan, ungrounded — the retry signal and the work queue

## CONSUMERS (what needs this)
`automatability_test`, `ee_journey`, `spare_agent`, `toy_app`

---
*Projected from the `the_toy_stack` KB (57 concepts / 84 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
