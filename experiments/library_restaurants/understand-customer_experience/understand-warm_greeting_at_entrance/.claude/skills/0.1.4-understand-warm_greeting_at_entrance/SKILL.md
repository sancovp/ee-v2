---
name: 0.1.4-understand-warm_greeting_at_entrance
description: [0.1.4] Friendly host acknowledgment upon arrival
---

# understand-warm_greeting_at_entrance

**CALL NUMBER:** `customer_experience.warm_greeting_at_entrance : front_of_house_service(3)`
**DEFINITION:** Friendly host acknowledgment upon arrival

Invoke this skill to understand `warm_greeting_at_entrance` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `customer_experience`
- **minimal_wait_time_for_seating** (d1): Short or well-managed time between arrival and being seated
- **thoughtful_table_assignment** (d1): Staff places guests at appropriate table based on party size and preferences
- **comfortable_waiting_area** (d2): Pleasant seating and atmosphere while waiting for table
- **waitlist_management** (d2): System handles parties fairly when busy
- **comfortable_seating** (d2): Chairs and booths provide adequate comfort for duration of meal
- **family_friendly_environment** (d2): Appropriate for children and families
- **romantic_atmosphere** (d2): Ambiance suitable for date night
- **booster_seat_availability** (d3): Booster seats available when needed
- **changing_table_in_restroom** (d3): Baby changing facilities provided
- **high_chair_availability** (d3): Sufficient high chairs for young children
- **kids_menu_variety** (d3): Children's options are appealing and varied
- **private_dining_options** (d3): Separate rooms available for private events
- **comfort_food_satisfaction** (d4): Classic dishes satisfy traditional cravings
- **food_quality_consistency** (d5): Same dishes taste same across different visits

### from `front_of_house_service`
- **table_ready_announcement** (d3): Calling out guest names when table is prepared
- **wait_time_estimation** (d3): Communication of expected wait duration during busy periods
- **waitlist_notification** (d3): Texting or calling guests when table is ready

## CONSUMERS (what needs this)
`seamless_reservation_system`, `staff_uniform_presentation`, `thank_you_gesture_on_exit`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
