---
name: 0.3.3-understand-host_stand
description: [0.3.3] designated station for greeting and seating guests
---

# understand-host_stand

**CALL NUMBER:** `facilities_and_equipment.host_stand : technology_and_pos(73), reservations_and_seating(67), defined(21), staffing_and_roles(14), front_of_house_service(8), finance_and_costing(7)`
**DEFINITION:** designated station for greeting and seating guests

Invoke this skill to understand `host_stand` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **guest_complaint** (d3): A customer expressing dissatisfaction about food, service, or environment.
- **seating** (d4): Arrangement of tables and chairs for restaurant guests
- **table_management** (d4): Coordinating table assignments and service flow efficiently
- **text_notification_waitlist** (d4): A system that sends SMS messages to guests alerting them when their table is ready.
- **server_staff** (d5): Employees who take orders and serve food to customers
- **table_clearing** (d5): Removing dirty dishes and resetting tables after guests leave
- **table_resetting** (d5): Preparing clean tables with linens and place settings
- **plate_delivery** (d5): The service of bringing prepared food to the customer's table
- **order** (d5): A request for food or drinks from a customer or to a supplier
- **table_service** (d5): Servers bringing food and drinks directly to seated guests
- **tip_payout** (d5): The process of distributing earned tips to employees, often done daily or weekly.
- **anniversary_seating** (d5): Special reserved seating for customers celebrating restaurant anniversaries.
- **plating** (d6): The art of arranging and presenting food attractively on a plate
- **closing_reconciliation** (d6): Final cash and credit card accounting at end of business day.
- **tip_distribution** (d6): The method of allocating tips among servers, hosts, bussers, and other service staff.
- **curbside_delivery** (d6): Food service where orders are brought out to customers parked outside.
- **packaging** (d6): Materials used to wrap or contain food for takeout or delivery
- **takeout_order** (d6): Food prepared for customers to take home and eat
- **service_quality** (d7): Standard of customer service provided by staff
- **drink_refills** (d7): Additional servings of beverages provided free or at cost to guests.
- **table_maintenance** (d7): Ongoing cleaning and restocking of dining tables

### from `facilities_and_equipment`
- **coat_check** (d1): designated area with staff for storing guest coats
- **podium** (d1): standing desk for host and cashier
- **table_number** (d3): numbered card or stand identifying table location
- **private_dining_room** (d4): enclosed room for exclusive group dining
- **high_chair** (d6): boosted seat for infants and toddlers
- **credit_card_reader** (d6): card terminal for processing electronic payments
- **booster_seat** (d7): raised seat for young children at table
- **booth** (d7): upholstered bench style seating against a wall
- **banquette** (d7): long upholstered bench seating along a wall

### from `finance_and_costing`
- **corkage_fee** (d5): Charge for customer bringing own wine
- **table_turnover_rate** (d5): Number of times tables are occupied per shift
- **wine_cost_percentage** (d6): Cost of wine relative to wine sales
- **food_cost_percentage** (d6): Cost of ingredients divided by food sales revenue
- **average_check** (d6): Average total spent per table or party
- **seat_turnover** (d6): Number of customers per seat per day
- **pour_cost** (d7): Cost of alcohol poured versus alcohol revenue

### from `front_of_house_service`
- **bread_service** (d5): Offering fresh bread with butter upon seating
- **water_service** (d5): Initial water pour with proper glass placement and lemon optional
- **bread_basket_refill** (d6): Replenishing bread basket during meal
- **butter_service** (d6): Providing softened butter with bread course
- **olive_oil_dipping** (d6): Offering olive oil for artisan bread service
- **ice_level_maintenance** (d6): Ensuring adequate ice in beverages during service
- **water_refill** (d6): Replenishing water glass throughout dining experience
- **cash_handling** (d7): Counting and processing cash payments

### from `reservations_and_seating`
- **front_door_staff** (d1): team personnel stationed at restaurant entrance
- **greeter** (d1): employee welcoming guests at entrance
- **host** (d1): staff member who greets and seats incoming guests
- **waiting_area** (d1): lobby or lounge space for standing waiting guests
- **seating_chart** (d2): visual diagram showing table positions and numbers
- **maitre_d** (d2): senior hospitality professional managing front of house
- **reservation_book** (d2): physical ledger or digital log of all bookings
- **reservation_system** (d2): software or platform managing booking operations
- **buzzer_system** (d2): paging device alerting waiting guests their table is ready
- **pager** (d2): handheld device given to guests on waitlist
- **standing_room** (d2): area where guests can be seated without fixed chairs
- **blocked_table** (d3): table marked unavailable for guest seating
- **capacity_chart** (d3): document showing maximum covers by table type and time
- **floor_plan** (d3): architectural layout showing all seating areas
- **reserved_table** (d3): table held exclusively for confirmed reservation
- **section** (d3): designated area of tables assigned to one server
- **table_formation** (d3): configuration of multiple tables pushed together for large groups
- **priority_seating** (d3): preferential table assignment for VIP or special guests
- **vip_room** (d3): premium private room for important or celebrity guests
- **table_status** (d4): current condition or availability state of a table
- **cover_count** (d4): number of guests to be seated
- **reserved_sign** (d4): marker indicating table is held for upcoming reservation
- **rotation_system** (d4): method for evenly distributing sections among servers
- **station** (d4): specific group of tables under one server's responsibility
- **four_top** (d4): table designed for four diners

### from `staffing_and_roles`
- **captain** (d3): senior front of house lead who manages dining room service
- **host_hostess** (d3): staff member who greets guests, manages reservations, and seats diners
- **private_dining_manager** (d3): manager who handles private dining reservations and service
- **reservation_manager** (d3): staff who manages bookings and seating logistics
- **busser** (d4): staff who clears tables, resets dining areas, and assists servers
- **food_runner** (d4): staff who delivers food from kitchen to tables
- **server** (d4): waiter who takes orders, delivers food, and provides table service
- **expeditor** (d5): staff who coordinates orders between kitchen and servers
- **cashier** (d5): staff who processes guest payments and handles receipts
- **to_go_specialist** (d5): staff who prepares takeout orders and handles curbside service
- **trainee_server** (d5): new server learning service procedures under supervision
- **captain_server** (d6): senior server who leads service team and handles special requests
- **server_assistant** (d6): assistant who helps servers with drink refills and table maintenance
- **lead_server** (d7): experienced server who trains and mentors newer servers

### from `technology_and_pos`
- **customer_profiling** (d3): Building behavioral and preference data profiles for individual guests
- **customer_relationship_management_crm** (d3): Database tracking guest preferences purchase history and contact information
- **email_marketing_integration** (d3): Connection between POS data and email campaign platform for guest outreach
- **guest_seating_optimization** (d3): Algorithm matching party sizes and preferences to optimal available tables
- **opentable_integration** (d3): Two way sync between reservation platform and table management system
- **sms_marketing_integration** (d3): Link between restaurant system and text message marketing platform
- **waitlist_management_system** (d3): Digital tool tracking walk in guests and estimated seating wait times
- **digital_review_request** (d4): Automated prompt encouraging guests to rate experience on review platforms
- **feedback_tablet** (d4): Tablet device soliciting customer satisfaction ratings after meal
- **loyalty_program_software** (d4): System managing customer reward points punch cards and member tiers
- **personalized_recommendations** (d4): AI suggesting menu items based on individual customer taste preferences
- **saved_payment_methods** (d4): Secure storage of customer credit card information for faster future checkout
- **spending_history_tracking** (d4): Recording of past purchases to identify customer ordering patterns
- **targeted_promotions** (d4): Customized discounts or offers sent to specific customers based on their data
- **online_ordering_platform** (d4): Website or app enabling customers to place orders for pickup or delivery
- **opentable_reservation_sync** (d4): Automatic updating of availability across OpenTable and restaurant systems
- **table_management_system** (d4): Software coordinating table assignments seating flow and turn times
- **customer_wait_time_display** (d4): Screen showing estimated wait time for food preparation and pickup
- **digital_waitlist_app** (d4): Mobile interface allowing guests to join queue and receive text notifications
- **estimated_ready_time** (d4): Calculated time when order will be prepared for customer pickup or delivery
- **live_delivery_tracking** (d4): Customer facing map showing driver location and estimated arrival time
- **order_tracking** (d4): Real time status updates for customers monitoring their order progress
- **customer_loyalty_app** (d5): Branded mobile application tracking member rewards and personalized offers
- **payment_gateway** (d5): Merchant service bridging restaurant POS and payment processor networks
- **restaurant_app** (d5): Mobile application branded for the restaurant for ordering and engagement

## CONSUMERS (what needs this)
`waiting_area`, `walk_in`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
