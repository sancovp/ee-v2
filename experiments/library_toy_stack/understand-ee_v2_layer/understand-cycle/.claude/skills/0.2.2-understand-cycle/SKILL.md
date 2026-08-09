---
name: 0.2.2-understand-cycle
description: [0.2.2] one walk of a kernel's nodes by fresh seats, ending in a harvest
---

# understand-cycle

**CALL NUMBER:** `ee_v2_layer.cycle : map_layer(5)`
**DEFINITION:** one walk of a kernel's nodes by fresh seats, ending in a harvest

Invoke this skill to understand `cycle` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `ee_v2_layer`
- **fixpoint_meter** (d1): zero newly-accreted structure across a cycle = stabilized; the kernel's own closure clause, measured
- **harvest** (d1): the cycle-end dump of emerged concepts and relations into the persistent KB
- **worklist** (d2): the prover-minted backlog: define (referenced-but-undefined), connect (orphans), reconcile (near-duplicates)

### from `map_layer`
- **map_prover** (d2): SWI-Prolog closed-world checker behind a typed construction boundary; the consistency typer for everything the seats emit
- **authority_split** (d3): seats author candidate facts only; the engine holds source facts; a seat can never witness itself
- **certificate** (d3): a replayable proof envelope over a construction: subject, payload, kappa, sha — monotone, never uncertifies
- **consistency_typing** (d3): the KB cannot become internally inconsistent: every emission passes the typer or its violations are named
- **soup_frontier** (d3): the named violations when a construction fails: dangling, orphan, ungrounded — the retry signal and the work queue

## CONSUMERS (what needs this)
`metacompiler`

---
*Projected from the `the_toy_stack` KB (39 concepts / 53 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
