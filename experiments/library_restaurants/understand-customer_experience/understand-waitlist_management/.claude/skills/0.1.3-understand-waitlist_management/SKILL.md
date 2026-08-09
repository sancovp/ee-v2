---
name: 0.1.3-understand-waitlist_management
description: [0.1.3] System handles parties fairly when busy
---

# understand-waitlist_management

**CALL NUMBER:** `customer_experience.waitlist_management : front_of_house_service(3)`
**DEFINITION:** System handles parties fairly when busy

Invoke this skill to understand `waitlist_management` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `front_of_house_service`
- **table_ready_announcement** (d1): Calling out guest names when table is prepared
- **wait_time_estimation** (d1): Communication of expected wait duration during busy periods
- **waitlist_notification** (d1): Texting or calling guests when table is ready

## CONSUMERS (what needs this)
`delay_communication`, `host_greeting`, `minimal_wait_time_for_seating`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
