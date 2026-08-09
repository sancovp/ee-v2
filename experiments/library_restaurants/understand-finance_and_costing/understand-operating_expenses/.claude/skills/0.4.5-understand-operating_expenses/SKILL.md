---
name: 0.4.5-understand-operating_expenses
description: [0.4.5] Day to day costs of running restaurant
---

# understand-operating_expenses

**CALL NUMBER:** `finance_and_costing.operating_expenses`
**DEFINITION:** Day to day costs of running restaurant

Invoke this skill to understand `operating_expenses` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `finance_and_costing`
- **fixed_costs** (d1): Costs that remain constant regardless of volume
- **marketing_expense** (d1): Total spending on promotion and advertising
- **rent_payment** (d1): Monthly commercial lease payment
- **utility_costs** (d1): Combined monthly utilities expense
- **variable_costs** (d1): Costs that scale with sales volume
- **advertising_cost** (d2): Paid media advertising spending
- **loyalty_program_cost** (d2): Rewards program redemption expense
- **social_media_marketing_cost** (d2): Spending on social platform advertising
- **cam_charges** (d2): Common area maintenance charges from landlord
- **common_area_maintenance_fee** (d2): Proportional share of building maintenance costs
- **electricity_cost** (d2): Monthly electric bill total
- **gas_cost** (d2): Monthly natural gas or propane expense
- **water_cost** (d2): Monthly water and sewer bill

## CONSUMERS (what needs this)
`accountant_fee`, `legal_fee`, `net_profit`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
