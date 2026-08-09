---
name: 0.4.1-understand-map_prover
description: [0.4.1] SWI-Prolog closed-world checker behind a typed construction boundary; the consistency typer for everything the
---

# understand-map_prover

**CALL NUMBER:** `map_layer.map_prover`
**DEFINITION:** SWI-Prolog closed-world checker behind a typed construction boundary; the consistency typer for everything the seats emit

Invoke this skill to understand `map_prover` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `map_layer`
- **authority_split** (d1): seats author candidate facts only; the engine holds source facts; a seat can never witness itself
- **certificate** (d1): a replayable proof envelope over a construction: subject, payload, kappa, sha — monotone, never uncertifies
- **consistency_typing** (d1): the KB cannot become internally inconsistent: every emission passes the typer or its violations are named
- **soup_frontier** (d1): the named violations when a construction fails: dangling, orphan, ungrounded — the retry signal and the work queue

## CONSUMERS (what needs this)
`harvest`

---
*Projected from the `the_toy_stack` KB (36 concepts / 44 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
