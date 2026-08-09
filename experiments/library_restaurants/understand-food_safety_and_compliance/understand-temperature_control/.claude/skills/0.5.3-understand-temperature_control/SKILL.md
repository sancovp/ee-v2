---
name: 0.5.3-understand-temperature_control
description: [0.5.3] maintaining food at safe temperatures to inhibit pathogenic bacteria growth
---

# understand-temperature_control

**CALL NUMBER:** `food_safety_and_compliance.temperature_control : defined(2), facilities_and_equipment(1)`
**DEFINITION:** maintaining food at safe temperatures to inhibit pathogenic bacteria growth

Invoke this skill to understand `temperature_control` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **environment** (d3): The overall atmosphere and setting of the restaurant including decor and noise level.
- **bare_hand_contact_prevention** (d10): Food safety rule requiring gloves or utensils when handling ready-to-eat food.

### from `facilities_and_equipment`
- **probe_thermometer** (d1): oven safe thermometer with wire probe for monitoring roasting

### from `food_safety_and_compliance`
- **cold_holding_temperature** (d1): maximum temperature of 41°F or below for cold potentially hazardous foods
- **hot_holding_temperature** (d1): minimum temperature of 135°F or above for hot potentially hazardous foods
- **refrigeration_unit** (d1): equipment designed to maintain cold holding temperatures for food storage
- **temperature_log** (d1): documented record of temperatures for refrigeration hot holding and cooking operations
- **freezer_unit** (d2): equipment designed to maintain frozen state at 0°F or below for food preservation
- **ice_machine_sanitation** (d2): regular cleaning and sanitizing of ice making and dispensing equipment
- **thermometer_calibration** (d2): process of verifying thermometer accuracy against known reference temperature
- **thermometer_replacement_schedule** (d2): regular intervals for replacing thermometers to ensure accuracy
- **gasket_inspection** (d2): checking door seals and gaskets on refrigeration units for integrity and cleanliness
- **refrigeration_coil_cleaning** (d2): maintenance of condenser coils for efficient operation of cooling equipment
- **cleaning_schedule** (d3): documented timeline specifying when and how each area or equipment item must be cleaned
- **pest_infestation** (d3): presence of pests in quantities or locations posing contamination risk to food
- **record_keeping** (d3): maintenance of required documentation demonstrating compliance with regulations
- **maintenance_record** (d3): documentation of equipment repairs and preventive maintenance activities
- **deep_cleaning_schedule** (d4): periodic thorough cleaning of equipment and areas beyond routine daily cleaning
- **end_of_shift_cleaning** (d4): required cleaning tasks performed at conclusion of each operational period
- **line_cleaning** (d4): sanitization of cooking line and service areas during and between meal periods
- **closure_order** (d4): legal order requiring food establishment to cease operations due to health hazard
- **insect_evidence** (d4): presence of flies cockroaches beetles or other insects in food preparation areas
- **inspection_report** (d4): official documented record of findings from health department inspection
- **rodent_evidence** (d4): signs of rodent activity such as droppings gnaw marks or nesting materials
- **training_record** (d4): documentation of food safety training completed by each employee
- **equipment_condition** (d5): physical state of kitchen equipment affecting sanitation and food safety
- **hood_vent_cleaning** (d5): regular maintenance of kitchen exhaust hoods and ductwork to prevent fire and grease buildup
- **sanitation_procedure** (d5): systematic cleaning and sanitizing protocols for kitchen surfaces and equipment

## CONSUMERS (what needs this)
`critical_control_point`, `haccp_plan`, `hot_holding_temperature`, `standard_operating_procedure`, `time_as_public_health_control`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
