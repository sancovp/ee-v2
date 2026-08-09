---
name: 0.6.2-understand-skilltome
description: [0.6.2] skilltree.tome: fold a skilltree into a single tome document — the bound volume of a library
---

# understand-skilltome

**CALL NUMBER:** `skilltree_lib.skilltome`
**DEFINITION:** skilltree.tome: fold a skilltree into a single tome document — the bound volume of a library

Invoke this skill to understand `skilltome` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `skilltree_lib`
- **skilltree** (d1): coordinate-addressed tree of skill dirs wired by Read-tool breadcrumbs, with validation and an FTS5 index
- **skilltree_coordinate** (d2): the hierarchical address of a node: root 0, child i = parent.i — the home class of the call number
- **skilltree_rag** (d2): build_index: one FTS5/BM25 table over every SKILL.md — retrieval returns ranked hits with shelf addresses

## CONSUMERS (what needs this)
`scalable_publishing`

---
*Projected from the `the_toy_stack` KB (36 concepts / 44 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
