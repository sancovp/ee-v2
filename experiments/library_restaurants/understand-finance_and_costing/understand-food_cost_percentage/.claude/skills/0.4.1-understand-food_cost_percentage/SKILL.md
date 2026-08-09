---
name: 0.4.1-understand-food_cost_percentage
description: [0.4.1] Cost of ingredients divided by food sales revenue
---

# understand-food_cost_percentage

**CALL NUMBER:** `finance_and_costing.food_cost_percentage`
**DEFINITION:** Cost of ingredients divided by food sales revenue

Invoke this skill to understand `food_cost_percentage` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `finance_and_costing`
- **average_check** (d1): Average total spent per table or party
- **food_cost_per_plate** (d1): Ingredient cost for single menu item
- **menu_price** (d1): Listed price for menu item
- **combo_meal_cost** (d2): Ingredient and labor cost of bundled meal deal
- **liquor_cost_percentage** (d2): Cost of spirits relative to spirit sales
- **portion_cost** (d2): Cost of one serving portion of item
- **plate_cost** (d3): Total cost of ingredients in finished dish
- **pour_cost** (d3): Cost of alcohol poured versus alcohol revenue
- **cook_time_cost** (d4): Labor cost of active cooking per item
- **plating_cost** (d4): Labor cost to assemble and plate finished dish
- **prep_time_cost** (d4): Labor cost of preparation work per item
- **recipe_cost** (d4): Total ingredient cost per recipe batch
- **ingredient_cost** (d5): Price paid for individual food ingredient

## CONSUMERS (what needs this)
`analytics_reporting_dashboard`, `cost_analysis`, `cost_of_goods_sold`, `ingredient_level_inventory`, `inventory_management_system`, `menu_engineering`, `menu_engineering_software`, `portion_control_technology`, `prime_cost`, `recipe_costing_software`, `spoilage_tracking`, `unified_inventory`, `waste_logging`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
