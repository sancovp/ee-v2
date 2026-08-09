---
name: 0.5.5-understand-cleaning_schedule
description: [0.5.5] documented timeline specifying when and how each area or equipment item must be cleaned
---

# understand-cleaning_schedule

**CALL NUMBER:** `food_safety_and_compliance.cleaning_schedule : defined(1), facilities_and_equipment(1)`
**DEFINITION:** documented timeline specifying when and how each area or equipment item must be cleaned

Invoke this skill to understand `cleaning_schedule` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **bare_hand_contact_prevention** (d7): Food safety rule requiring gloves or utensils when handling ready-to-eat food.

### from `facilities_and_equipment`
- **probe_thermometer** (d9): oven safe thermometer with wire probe for monitoring roasting

### from `food_safety_and_compliance`
- **deep_cleaning_schedule** (d1): periodic thorough cleaning of equipment and areas beyond routine daily cleaning
- **end_of_shift_cleaning** (d1): required cleaning tasks performed at conclusion of each operational period
- **line_cleaning** (d1): sanitization of cooking line and service areas during and between meal periods
- **equipment_condition** (d2): physical state of kitchen equipment affecting sanitation and food safety
- **hood_vent_cleaning** (d2): regular maintenance of kitchen exhaust hoods and ductwork to prevent fire and grease buildup
- **refrigeration_coil_cleaning** (d2): maintenance of condenser coils for efficient operation of cooling equipment
- **sanitation_procedure** (d2): systematic cleaning and sanitizing protocols for kitchen surfaces and equipment
- **equipment_sanitizing** (d3): sanitization procedures specific to kitchen equipment and machinery
- **maintenance_record** (d3): documentation of equipment repairs and preventive maintenance activities
- **contact_time_requirement** (d3): duration sanitizer solution must remain on surface to achieve effective sanitization
- **sanitizer_concentration** (d3): level of sanitizer solution required to effectively kill pathogens on surfaces
- **surface_sanitizing** (d3): treatment of food contact surfaces to reduce microorganisms to safe levels
- **blender_sanitation** (d4): disassembly and sanitization procedures for blenders and food processors
- **slicing_equipment_sanitation** (d4): cleaning procedures for meat slicers deli slicers and similar equipment
- **chemical_concentration_verification** (d4): testing procedure to ensure cleaning chemicals are diluted to proper strength
- **sanitizer_test_strip** (d4): paper strip used to verify sanitizer solution is at proper concentration
- **prep_table_sanitation** (d4): cleaning and sanitizing of food preparation surfaces between tasks
- **cross_contamination_prevention** (d5): practices preventing transfer of harmful microorganisms from one surface or food to another
- **allergen_management** (d5): systematic approach to prevent allergic reactions through proper handling and labeling
- **record_keeping** (d5): maintenance of required documentation demonstrating compliance with regulations
- **color_coded_cutting_boards** (d6): cutting boards coded by color to prevent cross contamination between food types
- **glove_usage** (d6): use of disposable gloves to prevent bare hand contact with ready to eat foods
- **handwashing_procedure** (d6): proper technique for washing hands including duration soap use and drying
- **raw_meat_storage** (d6): designated storage area or method for uncooked meat products separate from ready to eat foods
- **allergen_training** (d6): specialized training for staff on identifying and properly handling food allergens

## CONSUMERS (what needs this)
`dumpster_area_sanitation`, `equipment_sanitizing`, `grease_trap_maintenance`, `hood_vent_cleaning`, `ice_machine_sanitation`, `refrigeration_coil_cleaning`, `sanitation_procedure`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
