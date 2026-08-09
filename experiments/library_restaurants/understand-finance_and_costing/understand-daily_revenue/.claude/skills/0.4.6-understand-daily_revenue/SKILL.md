---
name: 0.4.6-understand-daily_revenue
description: [0.4.6] Total sales income for one business day
---

# understand-daily_revenue

**CALL NUMBER:** `finance_and_costing.daily_revenue`
**DEFINITION:** Total sales income for one business day

Invoke this skill to understand `daily_revenue` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `finance_and_costing`
- **average_check** (d1): Average total spent per table or party
- **table_turnover_rate** (d1): Number of times tables are occupied per shift
- **combo_meal_cost** (d2): Ingredient and labor cost of bundled meal deal
- **liquor_cost_percentage** (d2): Cost of spirits relative to spirit sales
- **menu_price** (d2): Listed price for menu item
- **seat_turnover** (d2): Number of customers per seat per day
- **plate_cost** (d3): Total cost of ingredients in finished dish
- **pour_cost** (d3): Cost of alcohol poured versus alcohol revenue
- **cook_time_cost** (d4): Labor cost of active cooking per item
- **plating_cost** (d4): Labor cost to assemble and plate finished dish
- **prep_time_cost** (d4): Labor cost of preparation work per item
- **recipe_cost** (d4): Total ingredient cost per recipe batch
- **portion_cost** (d4): Cost of one serving portion of item
- **ingredient_cost** (d5): Price paid for individual food ingredient

## CONSUMERS (what needs this)
`credit_card_processing_fee`, `gift_card_redemption`, `gross_profit`, `monthly_revenue`, `revenue_per_seat`, `sales_tax`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
