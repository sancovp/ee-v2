---
name: 0.6.2-understand-host_seating
description: [0.6.2] Process of guiding customers to their assigned table
---

# understand-host_seating

**CALL NUMBER:** `front_of_house_service.host_seating`
**DEFINITION:** Process of guiding customers to their assigned table

Invoke this skill to understand `host_seating` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `front_of_house_service`
- **high_chair_setup** (d1): Installing high chairs for young children
- **seating_preference_request** (d1): Asking about preferred seating location
- **table_turnover_efficiency** (d1): Clearing and resetting tables between seatings
- **wheelchair_accessibility** (d1): Ensuring proper space and access for wheelchairs
- **kid_friendly_service** (d2): Providing coloring menus crayons and child utensils

## CONSUMERS (what needs this)
`booth_preference_request`, `quiet_section_request`, `window_seat_request`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
