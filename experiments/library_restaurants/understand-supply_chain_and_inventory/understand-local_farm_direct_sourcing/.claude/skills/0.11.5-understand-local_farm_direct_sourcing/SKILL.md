---
name: 0.11.5-understand-local_farm_direct_sourcing
description: [0.11.5] buying directly from nearby farms to reduce food miles
---

# understand-local_farm_direct_sourcing

**CALL NUMBER:** `supply_chain_and_inventory.local_farm_direct_sourcing`
**DEFINITION:** buying directly from nearby farms to reduce food miles

Invoke this skill to understand `local_farm_direct_sourcing` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `supply_chain_and_inventory`
- **farm_to_table_procurement** (d1): direct purchasing programs connecting restaurants with local farms
- **food_miles_calculation** (d1): measuring distance ingredients travel from source to restaurant
- **implied_grower_relationships** (d1): implied relationship between restaurants and the farms that grow their produce
- **carbon_footprint_supply_tracking** (d2): environmental impact assessment of supply chain choices

## CONSUMERS (what needs this)
`raw_produce_procurement`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
