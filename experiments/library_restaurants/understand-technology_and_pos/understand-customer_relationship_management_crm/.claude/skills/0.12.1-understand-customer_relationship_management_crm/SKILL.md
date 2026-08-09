---
name: 0.12.1-understand-customer_relationship_management_crm
description: [0.12.1] Database tracking guest preferences purchase history and contact information
---

# understand-customer_relationship_management_crm

**CALL NUMBER:** `technology_and_pos.customer_relationship_management_crm : finance_and_costing(16), facilities_and_equipment(3), reservations_and_seating(1), defined(1), front_of_house_service(1)`
**DEFINITION:** Database tracking guest preferences purchase history and contact information

Invoke this skill to understand `customer_relationship_management_crm` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **text_notification_waitlist** (d4): A system that sends SMS messages to guests alerting them when their table is ready.

### from `facilities_and_equipment`
- **credit_card_reader** (d4): card terminal for processing electronic payments
- **kitchen_display_system** (d5): digital screen displaying orders for kitchen staff
- **digital_menu_board** (d5): electronic screen displaying menu items and prices

### from `finance_and_costing`
- **food_cost_percentage** (d4): Cost of ingredients divided by food sales revenue
- **average_check** (d5): Average total spent per table or party
- **food_cost_per_plate** (d5): Ingredient cost for single menu item
- **menu_price** (d5): Listed price for menu item
- **table_turnover_rate** (d5): Number of times tables are occupied per shift
- **combo_meal_cost** (d6): Ingredient and labor cost of bundled meal deal
- **liquor_cost_percentage** (d6): Cost of spirits relative to spirit sales
- **portion_cost** (d6): Cost of one serving portion of item
- **seat_turnover** (d6): Number of customers per seat per day
- **plate_cost** (d7): Total cost of ingredients in finished dish
- **pour_cost** (d7): Cost of alcohol poured versus alcohol revenue
- **cook_time_cost** (d8): Labor cost of active cooking per item
- **plating_cost** (d8): Labor cost to assemble and plate finished dish
- **prep_time_cost** (d8): Labor cost of preparation work per item
- **recipe_cost** (d8): Total ingredient cost per recipe batch
- **ingredient_cost** (d9): Price paid for individual food ingredient

### from `front_of_house_service`
- **cash_handling** (d5): Counting and processing cash payments

### from `reservations_and_seating`
- **reservation_system** (d2): software or platform managing booking operations

### from `technology_and_pos`
- **customer_profiling** (d1): Building behavioral and preference data profiles for individual guests
- **digital_review_request** (d1): Automated prompt encouraging guests to rate experience on review platforms
- **email_marketing_integration** (d1): Connection between POS data and email campaign platform for guest outreach
- **feedback_tablet** (d1): Tablet device soliciting customer satisfaction ratings after meal
- **guest_seating_optimization** (d1): Algorithm matching party sizes and preferences to optimal available tables
- **loyalty_program_software** (d1): System managing customer reward points punch cards and member tiers
- **personalized_recommendations** (d1): AI suggesting menu items based on individual customer taste preferences
- **saved_payment_methods** (d1): Secure storage of customer credit card information for faster future checkout
- **sms_marketing_integration** (d1): Link between restaurant system and text message marketing platform
- **spending_history_tracking** (d1): Recording of past purchases to identify customer ordering patterns
- **targeted_promotions** (d1): Customized discounts or offers sent to specific customers based on their data
- **online_ordering_platform** (d2): Website or app enabling customers to place orders for pickup or delivery
- **customer_loyalty_app** (d2): Branded mobile application tracking member rewards and personalized offers
- **payment_gateway** (d2): Merchant service bridging restaurant POS and payment processor networks
- **restaurant_app** (d2): Mobile application branded for the restaurant for ordering and engagement
- **tokenization_payment** (d2): Replacing card numbers with secure tokens for storage and recurring billing
- **customer_wait_time_display** (d2): Screen showing estimated wait time for food preparation and pickup
- **digital_waitlist_app** (d2): Mobile interface allowing guests to join queue and receive text notifications
- **estimated_ready_time** (d2): Calculated time when order will be prepared for customer pickup or delivery
- **live_delivery_tracking** (d2): Customer facing map showing driver location and estimated arrival time
- **order_tracking** (d2): Real time status updates for customers monitoring their order progress
- **api_integration** (d3): Technical connection allowing different software systems to share data
- **digital_receipt** (d3): Electronic receipt sent via email or text instead of printed paper copy
- **menu_price_sync** (d3): Automated price updates across all platforms when POS menu pricing changes
- **mobile_ordering** (d3): Smartphone based system allowing customers to browse menu and place orders

## CONSUMERS (what needs this)
`allergen_filtering`, `customer_loyalty_app`, `digital_receipt`, `email_marketing_integration`, `feedback_tablet`, `loyalty_program_software`, `online_ordering_platform`, `online_reservation_platform`, `opentable_integration`, `opentable_reservation_sync`, `pos_api`, `pos_software`, `reservation_system`, `restaurant_app`, `restaurant_management_software`, `saved_payment_methods`, `sms_marketing_integration`, `targeted_promotions`, `waitlist_management_system`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
