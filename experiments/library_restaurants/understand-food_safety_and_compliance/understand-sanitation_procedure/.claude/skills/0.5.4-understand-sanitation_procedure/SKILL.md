---
name: 0.5.4-understand-sanitation_procedure
description: [0.5.4] systematic cleaning and sanitizing protocols for kitchen surfaces and equipment
---

# understand-sanitation_procedure

**CALL NUMBER:** `food_safety_and_compliance.sanitation_procedure : defined(1), facilities_and_equipment(1)`
**DEFINITION:** systematic cleaning and sanitizing protocols for kitchen surfaces and equipment

Invoke this skill to understand `sanitation_procedure` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **bare_hand_contact_prevention** (d5): Food safety rule requiring gloves or utensils when handling ready-to-eat food.

### from `facilities_and_equipment`
- **probe_thermometer** (d7): oven safe thermometer with wire probe for monitoring roasting

### from `food_safety_and_compliance`
- **cleaning_schedule** (d1): documented timeline specifying when and how each area or equipment item must be cleaned
- **contact_time_requirement** (d1): duration sanitizer solution must remain on surface to achieve effective sanitization
- **equipment_sanitizing** (d1): sanitization procedures specific to kitchen equipment and machinery
- **sanitizer_concentration** (d1): level of sanitizer solution required to effectively kill pathogens on surfaces
- **surface_sanitizing** (d1): treatment of food contact surfaces to reduce microorganisms to safe levels
- **deep_cleaning_schedule** (d2): periodic thorough cleaning of equipment and areas beyond routine daily cleaning
- **end_of_shift_cleaning** (d2): required cleaning tasks performed at conclusion of each operational period
- **line_cleaning** (d2): sanitization of cooking line and service areas during and between meal periods
- **blender_sanitation** (d2): disassembly and sanitization procedures for blenders and food processors
- **slicing_equipment_sanitation** (d2): cleaning procedures for meat slicers deli slicers and similar equipment
- **chemical_concentration_verification** (d2): testing procedure to ensure cleaning chemicals are diluted to proper strength
- **sanitizer_test_strip** (d2): paper strip used to verify sanitizer solution is at proper concentration
- **prep_table_sanitation** (d2): cleaning and sanitizing of food preparation surfaces between tasks
- **equipment_condition** (d3): physical state of kitchen equipment affecting sanitation and food safety
- **hood_vent_cleaning** (d3): regular maintenance of kitchen exhaust hoods and ductwork to prevent fire and grease buildup
- **refrigeration_coil_cleaning** (d3): maintenance of condenser coils for efficient operation of cooling equipment
- **cross_contamination_prevention** (d3): practices preventing transfer of harmful microorganisms from one surface or food to another
- **allergen_management** (d3): systematic approach to prevent allergic reactions through proper handling and labeling
- **record_keeping** (d3): maintenance of required documentation demonstrating compliance with regulations
- **maintenance_record** (d4): documentation of equipment repairs and preventive maintenance activities
- **color_coded_cutting_boards** (d4): cutting boards coded by color to prevent cross contamination between food types
- **glove_usage** (d4): use of disposable gloves to prevent bare hand contact with ready to eat foods
- **handwashing_procedure** (d4): proper technique for washing hands including duration soap use and drying
- **raw_meat_storage** (d4): designated storage area or method for uncooked meat products separate from ready to eat foods
- **allergen_training** (d4): specialized training for staff on identifying and properly handling food allergens

## CONSUMERS (what needs this)
`end_of_shift_cleaning`, `handwashing_station`, `line_cleaning`, `norovirus_protocol`, `standard_operating_procedure`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
