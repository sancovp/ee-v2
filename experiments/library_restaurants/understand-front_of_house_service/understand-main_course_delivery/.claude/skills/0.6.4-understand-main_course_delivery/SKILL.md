---
name: 0.6.4-understand-main_course_delivery
description: [0.6.4] Presenting main dishes with proper timing and temperature
---

# understand-main_course_delivery

**CALL NUMBER:** `front_of_house_service.main_course_delivery`
**DEFINITION:** Presenting main dishes with proper timing and temperature

Invoke this skill to understand `main_course_delivery` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `front_of_house_service`
- **food_runner_service** (d1): Delivering food from kitchen to dining room
- **plate_warming** (d1): Heating plates before serving hot entrees
- **plating_verification** (d1): Checking plate presentation before guest delivery
- **sauce_application** (d1): Drizzling or applying sauces to plated dishes
- **silverware_replacement** (d1): Swapping utensils between courses appropriately
- **expo_station_coordination** (d2): Plating and quality checking before service
- **quality_verification** (d2): Ensuring food temperature and presentation standards
- **plate_clearing_pace** (d2): Removing finished plates with guest permission
- **order_accuracy_check** (d3): Verifying order tickets match guest requests

## CONSUMERS (what needs this)
`food_runner_service`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
