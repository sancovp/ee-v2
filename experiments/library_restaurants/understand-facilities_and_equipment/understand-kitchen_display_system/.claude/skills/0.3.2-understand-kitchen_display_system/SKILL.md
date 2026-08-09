---
name: 0.3.2-understand-kitchen_display_system
description: [0.3.2] digital screen displaying orders for kitchen staff
---

# understand-kitchen_display_system

**CALL NUMBER:** `facilities_and_equipment.kitchen_display_system : technology_and_pos(126), finance_and_costing(16), reservations_and_seating(1), defined(1), front_of_house_service(1)`
**DEFINITION:** digital screen displaying orders for kitchen staff

Invoke this skill to understand `kitchen_display_system` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **text_notification_waitlist** (d7): A system that sends SMS messages to guests alerting them when their table is ready.

### from `facilities_and_equipment`
- **digital_menu_board** (d3): electronic screen displaying menu items and prices
- **credit_card_reader** (d5): card terminal for processing electronic payments

### from `finance_and_costing`
- **food_cost_percentage** (d2): Cost of ingredients divided by food sales revenue
- **average_check** (d3): Average total spent per table or party
- **food_cost_per_plate** (d3): Ingredient cost for single menu item
- **menu_price** (d3): Listed price for menu item
- **combo_meal_cost** (d4): Ingredient and labor cost of bundled meal deal
- **liquor_cost_percentage** (d4): Cost of spirits relative to spirit sales
- **portion_cost** (d4): Cost of one serving portion of item
- **table_turnover_rate** (d4): Number of times tables are occupied per shift
- **plate_cost** (d5): Total cost of ingredients in finished dish
- **pour_cost** (d5): Cost of alcohol poured versus alcohol revenue
- **seat_turnover** (d5): Number of customers per seat per day
- **cook_time_cost** (d6): Labor cost of active cooking per item
- **plating_cost** (d6): Labor cost to assemble and plate finished dish
- **prep_time_cost** (d6): Labor cost of preparation work per item
- **recipe_cost** (d6): Total ingredient cost per recipe batch
- **ingredient_cost** (d7): Price paid for individual food ingredient

### from `front_of_house_service`
- **cash_handling** (d8): Counting and processing cash payments

### from `reservations_and_seating`
- **reservation_system** (d5): software or platform managing booking operations

### from `technology_and_pos`
- **course_pacing_software** (d1): System managing timing between appetizer main course and dessert courses
- **doordash_integration** (d1): Direct POS connection to DoorDash platform for incoming delivery orders
- **electronic_order_ticket** (d1): Digital version of paper order ticket transmitted from POS to kitchen
- **expo_station_display** (d1): Screen at expeditor station showing plated items ready for service
- **food_allergy_alert_system** (d1): Digital notification flagging orders containing guest allergy information
- **grubhub_integration** (d1): Technical connection enabling seamless order flow from Grubhub to kitchen
- **kitchen_call_system** (d1): Audio system announcing order ready times to servers for pickup
- **kitchen_printer** (d1): Impact or thermal printer in prep areas producing order tickets for cooks
- **online_ordering_aggregation** (d1): Consolidating orders from all digital channels into single kitchen view
- **order_routing_system** (d1): Software directing orders to appropriate kitchen stations based on items
- **postmates_integration** (d1): POS link to Postmates delivery service for order fulfillment management
- **prep_station_display** (d1): Specialized screen showing orders for specific prep areas like grill or sauté
- **third_party_delivery_integration** (d1): Software connection linking restaurant POS to DoorDash UberEats Grubhub
- **ticket_times_display** (d1): Monitor showing elapsed time since each order was placed in kitchen
- **uber_eats_integration** (d1): System linking restaurant to UberEats with automatic order transmission
- **unified_inventory** (d1): Single inventory database updated by all sales channels to prevent overselling
- **third_party_delivery_aggregation** (d2): Platform consolidating orders from multiple delivery apps into one screen
- **allergen_filtering** (d2): Menu software blocking items containing specified allergens from display
- **menu_label_printer** (d2): Device printing allergen and ingredient labels for individual plated dishes
- **menu_management_system** (d2): Software for creating editing pricing and organizing menu items and categories
- **menu_price_sync** (d2): Automated price updates across all platforms when POS menu pricing changes
- **order_management** (d2): End to end process of capturing transmitting and fulfilling customer orders
- **delivery_management_software** (d2): Platform coordinating in house delivery drivers routes and ETAs
- **live_delivery_tracking** (d2): Customer facing map showing driver location and estimated arrival time
- **ingredient_level_inventory** (d2): Stock tracking broken down to individual ingredient components

## CONSUMERS (what needs this)
`doordash_integration`, `food_allergy_alert_system`, `grubhub_integration`, `kitchen_automation`, `menu_label_printer`, `online_ordering_aggregation`, `postmates_integration`, `third_party_delivery_aggregation`, `third_party_delivery_integration`, `uber_eats_integration`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
