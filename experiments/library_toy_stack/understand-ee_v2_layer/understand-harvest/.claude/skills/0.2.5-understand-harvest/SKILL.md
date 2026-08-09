---
name: 0.2.5-understand-harvest
description: [0.2.5] the cycle-end dump of emerged concepts and relations into the persistent KB
---

# understand-harvest

**CALL NUMBER:** `ee_v2_layer.harvest : map_layer(5)`
**DEFINITION:** the cycle-end dump of emerged concepts and relations into the persistent KB

Invoke this skill to understand `harvest` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `ee_v2_layer`
- **worklist** (d1): the prover-minted backlog: define (referenced-but-undefined), connect (orphans), reconcile (near-duplicates)

### from `map_layer`
- **map_prover** (d1): SWI-Prolog closed-world checker behind a typed construction boundary; the consistency typer for everything the seats emit
- **authority_split** (d2): seats author candidate facts only; the engine holds source facts; a seat can never witness itself
- **certificate** (d2): a replayable proof envelope over a construction: subject, payload, kappa, sha — monotone, never uncertifies
- **consistency_typing** (d2): the KB cannot become internally inconsistent: every emission passes the typer or its violations are named
- **soup_frontier** (d2): the named violations when a construction fails: dangling, orphan, ungrounded — the retry signal and the work queue

## CONSUMERS (what needs this)
`cycle`

---
*Projected from the `the_toy_stack` KB (51 concepts / 73 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
