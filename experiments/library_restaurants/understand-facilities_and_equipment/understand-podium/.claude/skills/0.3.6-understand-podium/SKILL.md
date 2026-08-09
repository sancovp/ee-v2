---
name: 0.3.6-understand-podium
description: [0.3.6] standing desk for host and cashier
---

# understand-podium

**CALL NUMBER:** `facilities_and_equipment.podium : technology_and_pos(73), reservations_and_seating(67), defined(21), staffing_and_roles(14), front_of_house_service(8), finance_and_costing(7)`
**DEFINITION:** standing desk for host and cashier

Invoke this skill to understand `podium` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **guest_complaint** (d2): A customer expressing dissatisfaction about food, service, or environment.
- **seating** (d3): Arrangement of tables and chairs for restaurant guests
- **table_management** (d3): Coordinating table assignments and service flow efficiently
- **text_notification_waitlist** (d3): A system that sends SMS messages to guests alerting them when their table is ready.
- **table_clearing** (d4): Removing dirty dishes and resetting tables after guests leave
- **table_resetting** (d4): Preparing clean tables with linens and place settings
- **plate_delivery** (d4): The service of bringing prepared food to the customer's table
- **order** (d4): A request for food or drinks from a customer or to a supplier
- **table_service** (d4): Servers bringing food and drinks directly to seated guests
- **tip_payout** (d4): The process of distributing earned tips to employees, often done daily or weekly.
- **anniversary_seating** (d4): Special reserved seating for customers celebrating restaurant anniversaries.
- **server_staff** (d5): Employees who take orders and serve food to customers
- **plating** (d5): The art of arranging and presenting food attractively on a plate
- **closing_reconciliation** (d5): Final cash and credit card accounting at end of business day.
- **tip_distribution** (d5): The method of allocating tips among servers, hosts, bussers, and other service staff.
- **curbside_delivery** (d5): Food service where orders are brought out to customers parked outside.
- **packaging** (d5): Materials used to wrap or contain food for takeout or delivery
- **takeout_order** (d5): Food prepared for customers to take home and eat
- **service_quality** (d6): Standard of customer service provided by staff
- **drink_refills** (d6): Additional servings of beverages provided free or at cost to guests.
- **table_maintenance** (d6): Ongoing cleaning and restocking of dining tables

### from `facilities_and_equipment`
- **table_number** (d3): numbered card or stand identifying table location
- **private_dining_room** (d3): enclosed room for exclusive group dining
- **host_stand** (d4): designated station for greeting and seating guests
- **coat_check** (d5): designated area with staff for storing guest coats
- **high_chair** (d5): boosted seat for infants and toddlers
- **credit_card_reader** (d5): card terminal for processing electronic payments
- **booster_seat** (d6): raised seat for young children at table
- **booth** (d6): upholstered bench style seating against a wall
- **banquette** (d6): long upholstered bench seating along a wall

### from `finance_and_costing`
- **corkage_fee** (d4): Charge for customer bringing own wine
- **table_turnover_rate** (d4): Number of times tables are occupied per shift
- **wine_cost_percentage** (d5): Cost of wine relative to wine sales
- **food_cost_percentage** (d5): Cost of ingredients divided by food sales revenue
- **average_check** (d5): Average total spent per table or party
- **seat_turnover** (d5): Number of customers per seat per day
- **pour_cost** (d6): Cost of alcohol poured versus alcohol revenue

### from `front_of_house_service`
- **bread_service** (d4): Offering fresh bread with butter upon seating
- **water_service** (d4): Initial water pour with proper glass placement and lemon optional
- **bread_basket_refill** (d5): Replenishing bread basket during meal
- **butter_service** (d5): Providing softened butter with bread course
- **olive_oil_dipping** (d5): Offering olive oil for artisan bread service
- **ice_level_maintenance** (d5): Ensuring adequate ice in beverages during service
- **water_refill** (d5): Replenishing water glass throughout dining experience
- **cash_handling** (d6): Counting and processing cash payments

### from `reservations_and_seating`
- **host** (d1): staff member who greets and seats incoming guests
- **maitre_d** (d1): senior hospitality professional managing front of house
- **reservation_book** (d1): physical ledger or digital log of all bookings
- **reservation_system** (d1): software or platform managing booking operations
- **front_door_staff** (d2): team personnel stationed at restaurant entrance
- **greeter** (d2): employee welcoming guests at entrance
- **seating_chart** (d2): visual diagram showing table positions and numbers
- **priority_seating** (d2): preferential table assignment for VIP or special guests
- **vip_room** (d2): premium private room for important or celebrity guests
- **waiting_area** (d3): lobby or lounge space for standing waiting guests
- **blocked_table** (d3): table marked unavailable for guest seating
- **capacity_chart** (d3): document showing maximum covers by table type and time
- **floor_plan** (d3): architectural layout showing all seating areas
- **reserved_table** (d3): table held exclusively for confirmed reservation
- **section** (d3): designated area of tables assigned to one server
- **table_formation** (d3): configuration of multiple tables pushed together for large groups
- **waitlist** (d3): list of guests awaiting an available table
- **comp_reservation** (d3): complimentary booking for celebrity or press
- **high_value_guest** (d3): frequent diner or important patron with priority seating
- **special_occasion** (d3): celebration event like birthday or anniversary noted on reservation
- **dietary_accommodation** (d3): special seating or menu adjustment for dietary needs
- **private_room** (d3): enclosed exclusive space for private dining groups
- **buzzer_system** (d4): paging device alerting waiting guests their table is ready
- **pager** (d4): handheld device given to guests on waitlist
- **standing_room** (d4): area where guests can be seated without fixed chairs

### from `staffing_and_roles`
- **captain** (d2): senior front of house lead who manages dining room service
- **host_hostess** (d2): staff member who greets guests, manages reservations, and seats diners
- **private_dining_manager** (d2): manager who handles private dining reservations and service
- **reservation_manager** (d2): staff who manages bookings and seating logistics
- **busser** (d3): staff who clears tables, resets dining areas, and assists servers
- **food_runner** (d3): staff who delivers food from kitchen to tables
- **server** (d3): waiter who takes orders, delivers food, and provides table service
- **expeditor** (d4): staff who coordinates orders between kitchen and servers
- **cashier** (d4): staff who processes guest payments and handles receipts
- **to_go_specialist** (d4): staff who prepares takeout orders and handles curbside service
- **trainee_server** (d4): new server learning service procedures under supervision
- **captain_server** (d5): senior server who leads service team and handles special requests
- **server_assistant** (d5): assistant who helps servers with drink refills and table maintenance
- **lead_server** (d6): experienced server who trains and mentors newer servers

### from `technology_and_pos`
- **customer_profiling** (d2): Building behavioral and preference data profiles for individual guests
- **customer_relationship_management_crm** (d2): Database tracking guest preferences purchase history and contact information
- **email_marketing_integration** (d2): Connection between POS data and email campaign platform for guest outreach
- **guest_seating_optimization** (d2): Algorithm matching party sizes and preferences to optimal available tables
- **opentable_integration** (d2): Two way sync between reservation platform and table management system
- **sms_marketing_integration** (d2): Link between restaurant system and text message marketing platform
- **waitlist_management_system** (d2): Digital tool tracking walk in guests and estimated seating wait times
- **digital_review_request** (d3): Automated prompt encouraging guests to rate experience on review platforms
- **feedback_tablet** (d3): Tablet device soliciting customer satisfaction ratings after meal
- **loyalty_program_software** (d3): System managing customer reward points punch cards and member tiers
- **personalized_recommendations** (d3): AI suggesting menu items based on individual customer taste preferences
- **saved_payment_methods** (d3): Secure storage of customer credit card information for faster future checkout
- **spending_history_tracking** (d3): Recording of past purchases to identify customer ordering patterns
- **targeted_promotions** (d3): Customized discounts or offers sent to specific customers based on their data
- **online_ordering_platform** (d3): Website or app enabling customers to place orders for pickup or delivery
- **opentable_reservation_sync** (d3): Automatic updating of availability across OpenTable and restaurant systems
- **table_management_system** (d3): Software coordinating table assignments seating flow and turn times
- **customer_wait_time_display** (d3): Screen showing estimated wait time for food preparation and pickup
- **digital_waitlist_app** (d3): Mobile interface allowing guests to join queue and receive text notifications
- **estimated_ready_time** (d3): Calculated time when order will be prepared for customer pickup or delivery
- **live_delivery_tracking** (d3): Customer facing map showing driver location and estimated arrival time
- **order_tracking** (d3): Real time status updates for customers monitoring their order progress
- **customer_loyalty_app** (d4): Branded mobile application tracking member rewards and personalized offers
- **payment_gateway** (d4): Merchant service bridging restaurant POS and payment processor networks
- **restaurant_app** (d4): Mobile application branded for the restaurant for ordering and engagement

## CONSUMERS (what needs this)
`host_stand`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
