---
name: 0.3.3-understand-worklist
description: [0.3.3] the prover-minted backlog: define (referenced-but-undefined), connect (orphans), reconcile (near-duplicates)
---

# understand-worklist

**CALL NUMBER:** `ee_v2_layer.worklist : map_layer(1)`
**DEFINITION:** the prover-minted backlog: define (referenced-but-undefined), connect (orphans), reconcile (near-duplicates)

Invoke this skill to understand `worklist` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `map_layer`
- **soup_frontier** (d1): the named violations when a construction fails: dangling, orphan, ungrounded — the retry signal and the work queue

## CONSUMERS (what needs this)
`emergent_repair`, `harvest`, `toy_app`

---
*Projected from the `the_toy_stack` KB (57 concepts / 84 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
