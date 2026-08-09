---
name: 0.6.3-understand-to_go_packaging
description: [0.6.3] Packaging leftover food for takeout
---

# understand-to_go_packaging

**CALL NUMBER:** `front_of_house_service.to_go_packaging`
**DEFINITION:** Packaging leftover food for takeout

Invoke this skill to understand `to_go_packaging` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `front_of_house_service`
- **eco_friendly_packaging** (d1): Using compostable or recyclable takeout containers
- **heating_instructions** (d1): Providing reheating directions for leftovers
- **leftovers_packaging** (d1): Boxing uneaten portions for doggy bags
- **napkin_inclusion** (d1): Packing napkins with takeout orders
- **sauce_packet_inclusion** (d1): Adding extra sauce packets to takeout
- **spill_proof_packaging** (d1): Ensuring containers won't leak during transport
- **utensil_inclusion** (d1): Adding disposable utensils to takeout orders
- **curbside_pickup_service** (d2): Delivering takeout orders to customer vehicles
- **doggy_bag_offer** (d2): Asking if guests want leftovers packaged

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
