---
name: 0.9.2-understand-reservation_system
description: [0.9.2] software or platform managing booking operations
---

# understand-reservation_system

**CALL NUMBER:** `reservations_and_seating.reservation_system : technology_and_pos(126), finance_and_costing(16), facilities_and_equipment(3), defined(1), front_of_house_service(1)`
**DEFINITION:** software or platform managing booking operations

Invoke this skill to understand `reservation_system` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **text_notification_waitlist** (d2): A system that sends SMS messages to guests alerting them when their table is ready.

### from `facilities_and_equipment`
- **credit_card_reader** (d4): card terminal for processing electronic payments
- **kitchen_display_system** (d5): digital screen displaying orders for kitchen staff
- **digital_menu_board** (d5): electronic screen displaying menu items and prices

### from `finance_and_costing`
- **table_turnover_rate** (d3): Number of times tables are occupied per shift
- **food_cost_percentage** (d4): Cost of ingredients divided by food sales revenue
- **average_check** (d4): Average total spent per table or party
- **seat_turnover** (d4): Number of customers per seat per day
- **food_cost_per_plate** (d5): Ingredient cost for single menu item
- **menu_price** (d5): Listed price for menu item
- **combo_meal_cost** (d5): Ingredient and labor cost of bundled meal deal
- **liquor_cost_percentage** (d5): Cost of spirits relative to spirit sales
- **portion_cost** (d6): Cost of one serving portion of item
- **plate_cost** (d6): Total cost of ingredients in finished dish
- **pour_cost** (d6): Cost of alcohol poured versus alcohol revenue
- **cook_time_cost** (d7): Labor cost of active cooking per item
- **plating_cost** (d7): Labor cost to assemble and plate finished dish
- **prep_time_cost** (d7): Labor cost of preparation work per item
- **recipe_cost** (d7): Total ingredient cost per recipe batch
- **ingredient_cost** (d8): Price paid for individual food ingredient

### from `front_of_house_service`
- **cash_handling** (d5): Counting and processing cash payments

### from `technology_and_pos`
- **customer_profiling** (d1): Building behavioral and preference data profiles for individual guests
- **customer_relationship_management_crm** (d1): Database tracking guest preferences purchase history and contact information
- **email_marketing_integration** (d1): Connection between POS data and email campaign platform for guest outreach
- **guest_seating_optimization** (d1): Algorithm matching party sizes and preferences to optimal available tables
- **opentable_integration** (d1): Two way sync between reservation platform and table management system
- **sms_marketing_integration** (d1): Link between restaurant system and text message marketing platform
- **waitlist_management_system** (d1): Digital tool tracking walk in guests and estimated seating wait times
- **digital_review_request** (d2): Automated prompt encouraging guests to rate experience on review platforms
- **feedback_tablet** (d2): Tablet device soliciting customer satisfaction ratings after meal
- **loyalty_program_software** (d2): System managing customer reward points punch cards and member tiers
- **personalized_recommendations** (d2): AI suggesting menu items based on individual customer taste preferences
- **saved_payment_methods** (d2): Secure storage of customer credit card information for faster future checkout
- **spending_history_tracking** (d2): Recording of past purchases to identify customer ordering patterns
- **targeted_promotions** (d2): Customized discounts or offers sent to specific customers based on their data
- **online_ordering_platform** (d2): Website or app enabling customers to place orders for pickup or delivery
- **opentable_reservation_sync** (d2): Automatic updating of availability across OpenTable and restaurant systems
- **table_management_system** (d2): Software coordinating table assignments seating flow and turn times
- **customer_wait_time_display** (d2): Screen showing estimated wait time for food preparation and pickup
- **digital_waitlist_app** (d2): Mobile interface allowing guests to join queue and receive text notifications
- **estimated_ready_time** (d2): Calculated time when order will be prepared for customer pickup or delivery
- **live_delivery_tracking** (d2): Customer facing map showing driver location and estimated arrival time
- **order_tracking** (d2): Real time status updates for customers monitoring their order progress
- **customer_loyalty_app** (d3): Branded mobile application tracking member rewards and personalized offers
- **payment_gateway** (d3): Merchant service bridging restaurant POS and payment processor networks
- **restaurant_app** (d3): Mobile application branded for the restaurant for ordering and engagement

## CONSUMERS (what needs this)
`api_integration`, `auto_cancellation`, `booking_confirmation`, `comp_reservation`, `email_marketing_integration`, `ghost_table`, `online_booking`, `online_reservation_platform`, `opentable_integration`, `podium`, `pos_api`, `pos_software`, `reservation`, `reservation_manager`, `restaurant_app`, `table_management_system`, `third_party_reservation`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
