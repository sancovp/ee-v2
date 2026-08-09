---
name: 0.6.1-understand-menu_presentation
description: [0.6.1] Handing menus to customers with appropriate timing and style
---

# understand-menu_presentation

**CALL NUMBER:** `front_of_house_service.menu_presentation : food_safety_and_compliance(42), defined(1), facilities_and_equipment(1)`
**DEFINITION:** Handing menus to customers with appropriate timing and style

Invoke this skill to understand `menu_presentation` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **bare_hand_contact_prevention** (d4): Food safety rule requiring gloves or utensils when handling ready-to-eat food.

### from `facilities_and_equipment`
- **probe_thermometer** (d7): oven safe thermometer with wire probe for monitoring roasting

### from `food_safety_and_compliance`
- **cross_contamination_prevention** (d2): practices preventing transfer of harmful microorganisms from one surface or food to another
- **allergen_management** (d3): systematic approach to prevent allergic reactions through proper handling and labeling
- **color_coded_cutting_boards** (d3): cutting boards coded by color to prevent cross contamination between food types
- **glove_usage** (d3): use of disposable gloves to prevent bare hand contact with ready to eat foods
- **handwashing_procedure** (d3): proper technique for washing hands including duration soap use and drying
- **raw_meat_storage** (d3): designated storage area or method for uncooked meat products separate from ready to eat foods
- **allergen_training** (d4): specialized training for staff on identifying and properly handling food allergens
- **cross_contact_prevention** (d4): preventing transfer of allergen proteins between foods through equipment or surfaces
- **food_allergen_labeling** (d4): required disclosure of major food allergens present in menu items
- **gluten_free_protocol** (d4): specific procedures to prevent gluten contamination in gluten free designated preparation areas
- **cutting_board_condition** (d4): state of cutting boards including cleanliness wear and sanitization status
- **bloodborne_pathogen_protocol** (d4): procedures for safely handling blood and bodily fluids to prevent disease transmission
- **sanitizer_concentration** (d4): level of sanitizer solution required to effectively kill pathogens on surfaces
- **buffer_zone_requirement** (d4): specified distance between food preparation areas and potential contamination sources
- **customer_complaint_procedure** (d5): protocol for receiving documenting investigating and responding to customer complaints
- **training_record** (d5): documentation of food safety training completed by each employee
- **equipment_sanitizing** (d5): sanitization procedures specific to kitchen equipment and machinery
- **prep_table_sanitation** (d5): cleaning and sanitizing of food preparation surfaces between tasks
- **slicing_equipment_sanitation** (d5): cleaning procedures for meat slicers deli slicers and similar equipment
- **consumer_advisory** (d5): required disclosure informing customers of increased risk when ordering undercooked menu items
- **surface_sanitizing** (d5): treatment of food contact surfaces to reduce microorganisms to safe levels
- **first_aid_kit_requirements** (d5): specifications for maintaining adequate first aid supplies in food service areas
- **incident_documentation** (d5): records created during investigation of food safety complaint or illness outbreak
- **chemical_concentration_verification** (d5): testing procedure to ensure cleaning chemicals are diluted to proper strength
- **sanitizer_test_strip** (d5): paper strip used to verify sanitizer solution is at proper concentration

### from `front_of_house_service`
- **allergy_confirmation** (d1): Reconfirming food allergies with kitchen before service
- **child_menu_presentation** (d1): Offering separate menu for young diners
- **daily_special_announcement** (d1): Verbal description of chef's daily special offerings
- **dessert_menu_presentation** (d1): Offering dessert menu after entrees cleared
- **dietary_restriction_check** (d1): Confirming accommodations for special diets
- **gluten_free_accommodation** (d1): Preventing cross_contamination for celiac guests
- **vegan_accommodation** (d1): Verifying no animal products in dishes
- **vegetarian_accommodation** (d1): Ensuring proper preparation for vegetarian items
- **wine_list_presentation** (d1): Offering and explaining wine selection options
- **order_accuracy_check** (d2): Verifying order tickets match guest requests
- **quality_verification** (d3): Ensuring food temperature and presentation standards

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
