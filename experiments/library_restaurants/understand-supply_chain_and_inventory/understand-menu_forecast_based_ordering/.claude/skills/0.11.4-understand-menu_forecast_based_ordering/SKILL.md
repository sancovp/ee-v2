---
name: 0.11.4-understand-menu_forecast_based_ordering
description: [0.11.4] ordering driven by predicted menu item sales volumes
---

# understand-menu_forecast_based_ordering

**CALL NUMBER:** `supply_chain_and_inventory.menu_forecast_based_ordering`
**DEFINITION:** ordering driven by predicted menu item sales volumes

Invoke this skill to understand `menu_forecast_based_ordering` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `supply_chain_and_inventory`
- **batch_cooking_schedules** (d1): production planning that determines ingredient batch requirements
- **event_catering_supply_stocking** (d1): preparing inventory levels for private events or banquets
- **holiday_demand_surge_ordering** (d1): preordering extra inventory for high-volume holiday periods
- **prep_sheet_ordering** (d1): ordering based on daily prep requirements from station prep lists
- **menu_special_ingredient_procurement** (d2): sourcing unique ingredients for limited-time menu offerings
- **supply_shortage_contingency_planning** (d2): strategies for maintaining operations when supplies unavailable

## CONSUMERS (what needs this)
`auto_reorder_point_calculation`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
