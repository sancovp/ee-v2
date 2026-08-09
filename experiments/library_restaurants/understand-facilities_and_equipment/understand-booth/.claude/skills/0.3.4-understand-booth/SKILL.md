---
name: 0.3.4-understand-booth
description: [0.3.4] upholstered bench style seating against a wall
---

# understand-booth

**CALL NUMBER:** `facilities_and_equipment.booth : reservations_and_seating(8)`
**DEFINITION:** upholstered bench style seating against a wall

Invoke this skill to understand `booth` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `reservations_and_seating`
- **four_top** (d1): table designed for four diners
- **rectangular_table** (d1): elongated table with longer length than width
- **six_top** (d1): table designed for six diners
- **window_table** (d1): table positioned near exterior windows
- **round_table** (d2): circular dining table
- **square_table** (d2): table with four equal sides
- **tablecloth** (d2): fabric covering placed over dining table
- **two_top** (d2): table designed for two diners

## CONSUMERS (what needs this)
`outdoor_seating`, `table_hopping`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
