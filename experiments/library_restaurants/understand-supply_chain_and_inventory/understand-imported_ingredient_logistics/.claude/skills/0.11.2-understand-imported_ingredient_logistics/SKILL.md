---
name: 0.11.2-understand-imported_ingredient_logistics
description: [0.11.2] managing customs, duties, and extended lead times for foreign goods
---

# understand-imported_ingredient_logistics

**CALL NUMBER:** `supply_chain_and_inventory.imported_ingredient_logistics`
**DEFINITION:** managing customs, duties, and extended lead times for foreign goods

Invoke this skill to understand `imported_ingredient_logistics` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `supply_chain_and_inventory`
- **currency_exchange_rate_impact** (d1): effect of exchange rates on imported ingredient costs
- **customs_duty_management** (d1): handling import tariffs and customs clearance for foreign products
- **import_permit_compliance** (d1): obtaining required permits for restricted imported ingredients
- **lead_time_expectations** (d1): time between placing an order and receiving delivery from vendors
- **implied_international_trade_compliance** (d2): implied connection to customs and trade regulation systems

## CONSUMERS (what needs this)
`asian_specialty_food_distributors`, `latin_ingredient_vendors`, `middle_eastern_ingredient_suppliers`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
