---
name: 0.8.1-understand-skilltree
description: [0.8.1] coordinate-addressed tree of skill dirs wired by Read-tool breadcrumbs, with validation and an FTS5 index
---

# understand-skilltree

**CALL NUMBER:** `skilltree_lib.skilltree`
**DEFINITION:** coordinate-addressed tree of skill dirs wired by Read-tool breadcrumbs, with validation and an FTS5 index

Invoke this skill to understand `skilltree` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `skilltree_lib`
- **skilltree_coordinate** (d1): the hierarchical address of a node: root 0, child i = parent.i — the home class of the call number
- **skilltree_rag** (d1): build_index: one FTS5/BM25 table over every SKILL.md — retrieval returns ranked hits with shelf addresses

## CONSUMERS (what needs this)
`library_projection`, `skilltome`

---
*Projected from the `the_toy_stack` KB (51 concepts / 73 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
