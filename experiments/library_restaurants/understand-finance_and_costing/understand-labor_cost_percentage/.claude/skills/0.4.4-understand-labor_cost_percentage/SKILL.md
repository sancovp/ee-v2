---
name: 0.4.4-understand-labor_cost_percentage
description: [0.4.4] Total labor expenses as percentage of revenue
---

# understand-labor_cost_percentage

**CALL NUMBER:** `finance_and_costing.labor_cost_percentage`
**DEFINITION:** Total labor expenses as percentage of revenue

Invoke this skill to understand `labor_cost_percentage` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `finance_and_costing`
- **labor_hour_cost** (d1): Cost per hour of employee work
- **minimum_wage_expense** (d1): Cost of paying non tipped minimum wage staff
- **monthly_revenue** (d1): Total sales income for calendar month
- **tipped_wage_expense** (d1): Total cost of tipped employee wages
- **daily_revenue** (d2): Total sales income for one business day
- **tip_credit** (d2): Credit against minimum wage for tips received
- **tip_pool** (d2): Shared tips distributed among staff members
- **tip_reporting** (d2): Declared tip income for tax purposes
- **average_check** (d3): Average total spent per table or party
- **table_turnover_rate** (d3): Number of times tables are occupied per shift
- **combo_meal_cost** (d4): Ingredient and labor cost of bundled meal deal
- **liquor_cost_percentage** (d4): Cost of spirits relative to spirit sales
- **menu_price** (d4): Listed price for menu item
- **seat_turnover** (d4): Number of customers per seat per day
- **plate_cost** (d5): Total cost of ingredients in finished dish
- **pour_cost** (d5): Cost of alcohol poured versus alcohol revenue
- **cook_time_cost** (d6): Labor cost of active cooking per item
- **plating_cost** (d6): Labor cost to assemble and plate finished dish
- **prep_time_cost** (d6): Labor cost of preparation work per item
- **recipe_cost** (d6): Total ingredient cost per recipe batch
- **portion_cost** (d6): Cost of one serving portion of item
- **ingredient_cost** (d7): Price paid for individual food ingredient

## CONSUMERS (what needs this)
`cost_analysis`, `health_insurance_cost`, `payroll_tax`, `prime_cost`, `weekly_p_and_l`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
