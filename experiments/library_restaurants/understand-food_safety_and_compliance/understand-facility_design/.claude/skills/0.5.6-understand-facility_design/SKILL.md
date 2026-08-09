---
name: 0.5.6-understand-facility_design
description: [0.5.6] physical layout and construction features enabling effective cleaning and sanitation
---

# understand-facility_design

**CALL NUMBER:** `food_safety_and_compliance.facility_design : defined(3), facilities_and_equipment(2)`
**DEFINITION:** physical layout and construction features enabling effective cleaning and sanitation

Invoke this skill to understand `facility_design` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **air_quality** (d2): The condition of air in a restaurant including ventilation and cleanliness.
- **bare_hand_contact_prevention** (d3): Food safety rule requiring gloves or utensils when handling ready-to-eat food.
- **environment** (d6): The overall atmosphere and setting of the restaurant including decor and noise level.

### from `facilities_and_equipment`
- **three_compartment_sink** (d1): sink with three basins for washing rinsing sanitizing
- **probe_thermometer** (d5): oven safe thermometer with wire probe for monitoring roasting

### from `food_safety_and_compliance`
- **buffer_zone_requirement** (d1): specified distance between food preparation areas and potential contamination sources
- **cross_contamination_prevention** (d1): practices preventing transfer of harmful microorganisms from one surface or food to another
- **drain_maintenance** (d1): upkeep of floor drains to prevent backup and pest harborage
- **equipment_condition** (d1): physical state of kitchen equipment affecting sanitation and food safety
- **food_storage_standards** (d1): requirements for proper organization labeling and condition of stored food items
- **handwashing_station** (d1): designated area with soap hot water and drying facilities for proper hand hygiene
- **ventilation_system** (d1): air circulation and exhaust system maintaining air quality in food preparation areas
- **allergen_management** (d2): systematic approach to prevent allergic reactions through proper handling and labeling
- **color_coded_cutting_boards** (d2): cutting boards coded by color to prevent cross contamination between food types
- **glove_usage** (d2): use of disposable gloves to prevent bare hand contact with ready to eat foods
- **handwashing_procedure** (d2): proper technique for washing hands including duration soap use and drying
- **raw_meat_storage** (d2): designated storage area or method for uncooked meat products separate from ready to eat foods
- **condensate_drain_cleaning** (d2): service of refrigeration unit condensate collection and discharge systems
- **pest_control** (d2): measures to prevent and eliminate insects rodents and other pests from food establishment
- **equipment_sanitizing** (d2): sanitization procedures specific to kitchen equipment and machinery
- **maintenance_record** (d2): documentation of equipment repairs and preventive maintenance activities
- **chemical_storage** (d2): secure designated area for storing cleaning supplies and chemicals away from food
- **date_marking_procedure** (d2): labeling of prepared foods with preparation date to ensure timely use or disposal
- **fifo_rotation** (d2): first in first out inventory method ensuring older stock is used before newer stock
- **sanitation_procedure** (d2): systematic cleaning and sanitizing protocols for kitchen surfaces and equipment
- **contact_time_requirement** (d2): duration sanitizer solution must remain on surface to achieve effective sanitization
- **sanitizer_concentration** (d2): level of sanitizer solution required to effectively kill pathogens on surfaces
- **hood_vent_cleaning** (d2): regular maintenance of kitchen exhaust hoods and ductwork to prevent fire and grease buildup
- **allergen_training** (d3): specialized training for staff on identifying and properly handling food allergens
- **cross_contact_prevention** (d3): preventing transfer of allergen proteins between foods through equipment or surfaces

## CONSUMERS (what needs this)
`backflow_prevention`, `chemical_storage`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
