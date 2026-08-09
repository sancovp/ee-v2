---
name: 0.3.8-understand-library_projection
description: [0.3.8] project the certified KB as understand-X skilltree skills; call number = home class colon facets = the depende
---

# understand-library_projection

**CALL NUMBER:** `ee_v2_layer.library_projection : skilltree_lib(3), map_layer(1)`
**DEFINITION:** project the certified KB as understand-X skilltree skills; call number = home class colon facets = the dependency web

Invoke this skill to understand `library_projection` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `ee_v2_layer`
- **understand_skill** (d1): a loadable unit of competence: X plus its relative root, consistency-typed
- **relative_root** (d2): the least-fixed-point closure of everything X bundles from, walked to prims or to consumers, tagged by origin lib

### from `map_layer`
- **certificate** (d2): a replayable proof envelope over a construction: subject, payload, kappa, sha — monotone, never uncertifies

### from `skilltree_lib`
- **skilltree** (d1): coordinate-addressed tree of skill dirs wired by Read-tool breadcrumbs, with validation and an FTS5 index
- **skilltree_coordinate** (d2): the hierarchical address of a node: root 0, child i = parent.i — the home class of the call number
- **skilltree_rag** (d2): build_index: one FTS5/BM25 table over every SKILL.md — retrieval returns ranked hits with shelf addresses

## CONSUMERS (what needs this)
`toy_app`

---
*Projected from the `the_toy_stack` KB (57 concepts / 84 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
