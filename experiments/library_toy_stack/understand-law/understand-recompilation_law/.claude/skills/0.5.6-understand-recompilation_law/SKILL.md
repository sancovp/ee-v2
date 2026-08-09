---
name: 0.5.6-understand-recompilation_law
description: [0.5.6] bind a KB region to code only when its output is needed without lookup — reproduce with specialization
---

# understand-recompilation_law

**CALL NUMBER:** `law.recompilation_law`
**DEFINITION:** bind a KB region to code only when its output is needed without lookup — reproduce with specialization

Invoke this skill to understand `recompilation_law` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `law`
- **futamura_tower** (d1): the projection ladder: specializing an interpreter to a program yields a compiler; specializing the specializer compounds

## CONSUMERS (what needs this)
`collapse_principle`

---
*Projected from the `the_toy_stack` KB (57 concepts / 84 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
