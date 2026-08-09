---
name: 0.1.6-understand-thoughtful_table_assignment
description: [0.1.6] Staff places guests at appropriate table based on party size and preferences
---

# understand-thoughtful_table_assignment

**CALL NUMBER:** `customer_experience.thoughtful_table_assignment`
**DEFINITION:** Staff places guests at appropriate table based on party size and preferences

Invoke this skill to understand `thoughtful_table_assignment` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `customer_experience`
- **comfortable_seating** (d1): Chairs and booths provide adequate comfort for duration of meal
- **family_friendly_environment** (d1): Appropriate for children and families
- **romantic_atmosphere** (d1): Ambiance suitable for date night
- **booster_seat_availability** (d2): Booster seats available when needed
- **changing_table_in_restroom** (d2): Baby changing facilities provided
- **high_chair_availability** (d2): Sufficient high chairs for young children
- **kids_menu_variety** (d2): Children's options are appealing and varied
- **private_dining_options** (d2): Separate rooms available for private events
- **comfort_food_satisfaction** (d3): Classic dishes satisfy traditional cravings
- **food_quality_consistency** (d4): Same dishes taste same across different visits

## CONSUMERS (what needs this)
`warm_greeting_at_entrance`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
