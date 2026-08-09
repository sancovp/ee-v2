---
name: 0.9.5-understand-waitlist
description: [0.9.5] list of guests awaiting an available table
---

# understand-waitlist

**CALL NUMBER:** `reservations_and_seating.waitlist : technology_and_pos(68), defined(21), staffing_and_roles(15), facilities_and_equipment(11), finance_and_costing(8), front_of_house_service(7)`
**DEFINITION:** list of guests awaiting an available table

Invoke this skill to understand `waitlist` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **guest_complaint** (d3): A customer expressing dissatisfaction about food, service, or environment.
- **seating** (d4): Arrangement of tables and chairs for restaurant guests
- **table_management** (d4): Coordinating table assignments and service flow efficiently
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
- **text_notification_waitlist** (d6): A system that sends SMS messages to guests alerting them when their table is ready.
- **service_quality** (d7): Standard of customer service provided by staff
- **drink_refills** (d7): Additional servings of beverages provided free or at cost to guests.
- **table_maintenance** (d7): Ongoing cleaning and restocking of dining tables

### from `facilities_and_equipment`
- **host_stand** (d2): designated station for greeting and seating guests
- **table_number** (d3): numbered card or stand identifying table location
- **coat_check** (d3): designated area with staff for storing guest coats
- **podium** (d3): standing desk for host and cashier
- **private_dining_room** (d4): enclosed room for exclusive group dining
- **booth** (d4): upholstered bench style seating against a wall
- **high_chair** (d6): boosted seat for infants and toddlers
- **booster_seat** (d7): raised seat for young children at table
- **banquette** (d7): long upholstered bench seating along a wall
- **credit_card_reader** (d8): card terminal for processing electronic payments
- **bar_stool** (d8): tall stool for bar and high top seating

### from `finance_and_costing`
- **corkage_fee** (d5): Charge for customer bringing own wine
- **wine_cost_percentage** (d6): Cost of wine relative to wine sales
- **pour_cost** (d7): Cost of alcohol poured versus alcohol revenue
- **table_turnover_rate** (d7): Number of times tables are occupied per shift
- **portion_cost** (d8): Cost of one serving portion of item
- **food_cost_percentage** (d8): Cost of ingredients divided by food sales revenue
- **average_check** (d8): Average total spent per table or party
- **seat_turnover** (d8): Number of customers per seat per day

### from `front_of_house_service`
- **bread_service** (d5): Offering fresh bread with butter upon seating
- **water_service** (d5): Initial water pour with proper glass placement and lemon optional
- **bread_basket_refill** (d6): Replenishing bread basket during meal
- **butter_service** (d6): Providing softened butter with bread course
- **olive_oil_dipping** (d6): Offering olive oil for artisan bread service
- **ice_level_maintenance** (d6): Ensuring adequate ice in beverages during service
- **water_refill** (d6): Replenishing water glass throughout dining experience

### from `reservations_and_seating`
- **buzzer_system** (d1): paging device alerting waiting guests their table is ready
- **called_ahead_list** (d1): waitlist maintained via telephone for early arrival
- **host** (d1): staff member who greets and seats incoming guests
- **pager** (d1): handheld device given to guests on waitlist
- **party_size** (d1): number of guests in a dining group
- **seating_manager** (d1): staff member coordinating guest flow and table assignment
- **text_alert** (d1): SMS notification when table is ready
- **wait_time_estimate** (d1): predicted delay before a table becomes available
- **waiting_area** (d1): lobby or lounge space for standing waiting guests
- **front_door_staff** (d2): team personnel stationed at restaurant entrance
- **greeter** (d2): employee welcoming guests at entrance
- **seating_chart** (d2): visual diagram showing table positions and numbers
- **maitre_d** (d2): senior hospitality professional managing front of house
- **table_allocation** (d2): process of assigning tables to arriving guests
- **table_turnover** (d2): rate at which tables become available for new guests
- **standing_room** (d2): area where guests can be seated without fixed chairs
- **blocked_table** (d3): table marked unavailable for guest seating
- **capacity_chart** (d3): document showing maximum covers by table type and time
- **floor_plan** (d3): architectural layout showing all seating areas
- **reserved_table** (d3): table held exclusively for confirmed reservation
- **section** (d3): designated area of tables assigned to one server
- **table_formation** (d3): configuration of multiple tables pushed together for large groups
- **priority_seating** (d3): preferential table assignment for VIP or special guests
- **reservation_book** (d3): physical ledger or digital log of all bookings
- **vip_room** (d3): premium private room for important or celebrity guests

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
- **mentor_server** (d8): experienced server who mentors newer service staff

### from `technology_and_pos`
- **customer_profiling** (d5): Building behavioral and preference data profiles for individual guests
- **customer_relationship_management_crm** (d5): Database tracking guest preferences purchase history and contact information
- **email_marketing_integration** (d5): Connection between POS data and email campaign platform for guest outreach
- **guest_seating_optimization** (d5): Algorithm matching party sizes and preferences to optimal available tables
- **opentable_integration** (d5): Two way sync between reservation platform and table management system
- **sms_marketing_integration** (d5): Link between restaurant system and text message marketing platform
- **waitlist_management_system** (d5): Digital tool tracking walk in guests and estimated seating wait times
- **payment_processing** (d6): Complete cycle of authorizing settling and depositing card transactions
- **digital_review_request** (d6): Automated prompt encouraging guests to rate experience on review platforms
- **feedback_tablet** (d6): Tablet device soliciting customer satisfaction ratings after meal
- **loyalty_program_software** (d6): System managing customer reward points punch cards and member tiers
- **personalized_recommendations** (d6): AI suggesting menu items based on individual customer taste preferences
- **saved_payment_methods** (d6): Secure storage of customer credit card information for faster future checkout
- **spending_history_tracking** (d6): Recording of past purchases to identify customer ordering patterns
- **targeted_promotions** (d6): Customized discounts or offers sent to specific customers based on their data
- **online_ordering_platform** (d6): Website or app enabling customers to place orders for pickup or delivery
- **opentable_reservation_sync** (d6): Automatic updating of availability across OpenTable and restaurant systems
- **table_management_system** (d6): Software coordinating table assignments seating flow and turn times
- **customer_wait_time_display** (d6): Screen showing estimated wait time for food preparation and pickup
- **digital_waitlist_app** (d6): Mobile interface allowing guests to join queue and receive text notifications
- **estimated_ready_time** (d6): Calculated time when order will be prepared for customer pickup or delivery
- **live_delivery_tracking** (d6): Customer facing map showing driver location and estimated arrival time
- **order_tracking** (d6): Real time status updates for customers monitoring their order progress
- **customer_loyalty_app** (d7): Branded mobile application tracking member rewards and personalized offers
- **payment_gateway** (d7): Merchant service bridging restaurant POS and payment processor networks

## CONSUMERS (what needs this)
`called_ahead_list`, `host_hostess`, `overbooking`, `seating_manager`, `walk_in`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
