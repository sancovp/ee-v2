---
name: 0.4.2-understand-plate_cost
description: [0.4.2] Total cost of ingredients in finished dish
---

# understand-plate_cost

**CALL NUMBER:** `finance_and_costing.plate_cost`
**DEFINITION:** Total cost of ingredients in finished dish

Invoke this skill to understand `plate_cost` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `finance_and_costing`
- **cook_time_cost** (d1): Labor cost of active cooking per item
- **plating_cost** (d1): Labor cost to assemble and plate finished dish
- **prep_time_cost** (d1): Labor cost of preparation work per item
- **recipe_cost** (d1): Total ingredient cost per recipe batch
- **ingredient_cost** (d2): Price paid for individual food ingredient
- **portion_cost** (d2): Cost of one serving portion of item

## CONSUMERS (what needs this)
`amuse_bouche_cost`, `bread_service_cost`, `catering_cost`, `combo_meal_cost`, `complimentary_item_cost`, `dish_cost`, `menu_engineering`, `prix_fixe_cost`, `tasting_menu_cost`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
