---
name: 0.4.3-understand-inventory_cost
description: [0.4.3] Total value of held food and beverage stock
---

# understand-inventory_cost

**CALL NUMBER:** `finance_and_costing.inventory_cost`
**DEFINITION:** Total value of held food and beverage stock

Invoke this skill to understand `inventory_cost` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `finance_and_costing`
- **bulk_discount** (d1): Price reduction for large quantity purchase
- **delivery_fee** (d1): Charge for vendor or distributor delivery
- **minimum_order_quantity** (d1): Minimum purchase amount required by vendor
- **vendor_relationship** (d1): Business arrangement with food supplier
- **wholesale_food_price** (d1): Bulk or distributor pricing for ingredients
- **food_price_inflation** (d2): Year over year increase in food costs

## CONSUMERS (what needs this)
`buffet_cost_per_head`, `cost_of_goods_sold`, `food_donation_cost`, `shrinkage`, `staff_meal_cost`, `supply_chain_cost`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
