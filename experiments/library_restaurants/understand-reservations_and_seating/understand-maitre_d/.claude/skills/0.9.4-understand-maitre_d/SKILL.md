---
name: 0.9.4-understand-maitre_d
description: [0.9.4] senior hospitality professional managing front of house
---

# understand-maitre_d

**CALL NUMBER:** `reservations_and_seating.maitre_d : technology_and_pos(69), defined(21), staffing_and_roles(15), facilities_and_equipment(11), finance_and_costing(8), front_of_house_service(7)`
**DEFINITION:** senior hospitality professional managing front of house

Invoke this skill to understand `maitre_d` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **guest_complaint** (d1): A customer expressing dissatisfaction about food, service, or environment.
- **seating** (d2): Arrangement of tables and chairs for restaurant guests
- **table_management** (d2): Coordinating table assignments and service flow efficiently
- **table_clearing** (d3): Removing dirty dishes and resetting tables after guests leave
- **table_resetting** (d3): Preparing clean tables with linens and place settings
- **plate_delivery** (d3): The service of bringing prepared food to the customer's table
- **order** (d3): A request for food or drinks from a customer or to a supplier
- **table_service** (d3): Servers bringing food and drinks directly to seated guests
- **tip_payout** (d3): The process of distributing earned tips to employees, often done daily or weekly.
- **anniversary_seating** (d3): Special reserved seating for customers celebrating restaurant anniversaries.
- **plating** (d4): The art of arranging and presenting food attractively on a plate
- **closing_reconciliation** (d4): Final cash and credit card accounting at end of business day.
- **tip_distribution** (d4): The method of allocating tips among servers, hosts, bussers, and other service staff.
- **curbside_delivery** (d4): Food service where orders are brought out to customers parked outside.
- **packaging** (d4): Materials used to wrap or contain food for takeout or delivery
- **takeout_order** (d4): Food prepared for customers to take home and eat
- **text_notification_waitlist** (d4): A system that sends SMS messages to guests alerting them when their table is ready.
- **service_quality** (d5): Standard of customer service provided by staff
- **drink_refills** (d5): Additional servings of beverages provided free or at cost to guests.
- **table_maintenance** (d5): Ongoing cleaning and restocking of dining tables
- **server_staff** (d5): Employees who take orders and serve food to customers

### from `facilities_and_equipment`
- **private_dining_room** (d2): enclosed room for exclusive group dining
- **host_stand** (d3): designated station for greeting and seating guests
- **table_number** (d3): numbered card or stand identifying table location
- **coat_check** (d4): designated area with staff for storing guest coats
- **podium** (d4): standing desk for host and cashier
- **high_chair** (d4): boosted seat for infants and toddlers
- **booster_seat** (d5): raised seat for young children at table
- **booth** (d5): upholstered bench style seating against a wall
- **banquette** (d5): long upholstered bench seating along a wall
- **credit_card_reader** (d6): card terminal for processing electronic payments
- **bar_stool** (d6): tall stool for bar and high top seating

### from `finance_and_costing`
- **corkage_fee** (d3): Charge for customer bringing own wine
- **wine_cost_percentage** (d4): Cost of wine relative to wine sales
- **pour_cost** (d5): Cost of alcohol poured versus alcohol revenue
- **table_turnover_rate** (d5): Number of times tables are occupied per shift
- **portion_cost** (d6): Cost of one serving portion of item
- **food_cost_percentage** (d6): Cost of ingredients divided by food sales revenue
- **average_check** (d6): Average total spent per table or party
- **seat_turnover** (d6): Number of customers per seat per day

### from `front_of_house_service`
- **bread_service** (d3): Offering fresh bread with butter upon seating
- **water_service** (d3): Initial water pour with proper glass placement and lemon optional
- **bread_basket_refill** (d4): Replenishing bread basket during meal
- **butter_service** (d4): Providing softened butter with bread course
- **olive_oil_dipping** (d4): Offering olive oil for artisan bread service
- **ice_level_maintenance** (d4): Ensuring adequate ice in beverages during service
- **water_refill** (d4): Replenishing water glass throughout dining experience

### from `reservations_and_seating`
- **front_door_staff** (d1): team personnel stationed at restaurant entrance
- **host** (d1): staff member who greets and seats incoming guests
- **priority_seating** (d1): preferential table assignment for VIP or special guests
- **reservation_book** (d1): physical ledger or digital log of all bookings
- **vip_room** (d1): premium private room for important or celebrity guests
- **waiting_area** (d2): lobby or lounge space for standing waiting guests
- **greeter** (d2): employee welcoming guests at entrance
- **seating_chart** (d2): visual diagram showing table positions and numbers
- **waitlist** (d2): list of guests awaiting an available table
- **comp_reservation** (d2): complimentary booking for celebrity or press
- **high_value_guest** (d2): frequent diner or important patron with priority seating
- **special_occasion** (d2): celebration event like birthday or anniversary noted on reservation
- **reservation_system** (d2): software or platform managing booking operations
- **dietary_accommodation** (d2): special seating or menu adjustment for dietary needs
- **private_room** (d2): enclosed exclusive space for private dining groups
- **buzzer_system** (d3): paging device alerting waiting guests their table is ready
- **pager** (d3): handheld device given to guests on waitlist
- **standing_room** (d3): area where guests can be seated without fixed chairs
- **blocked_table** (d3): table marked unavailable for guest seating
- **capacity_chart** (d3): document showing maximum covers by table type and time
- **floor_plan** (d3): architectural layout showing all seating areas
- **reserved_table** (d3): table held exclusively for confirmed reservation
- **section** (d3): designated area of tables assigned to one server
- **table_formation** (d3): configuration of multiple tables pushed together for large groups
- **called_ahead_list** (d3): waitlist maintained via telephone for early arrival

### from `staffing_and_roles`
- **captain** (d1): senior front of house lead who manages dining room service
- **host_hostess** (d1): staff member who greets guests, manages reservations, and seats diners
- **private_dining_manager** (d1): manager who handles private dining reservations and service
- **reservation_manager** (d1): staff who manages bookings and seating logistics
- **busser** (d2): staff who clears tables, resets dining areas, and assists servers
- **food_runner** (d2): staff who delivers food from kitchen to tables
- **server** (d2): waiter who takes orders, delivers food, and provides table service
- **expeditor** (d3): staff who coordinates orders between kitchen and servers
- **cashier** (d3): staff who processes guest payments and handles receipts
- **to_go_specialist** (d3): staff who prepares takeout orders and handles curbside service
- **trainee_server** (d3): new server learning service procedures under supervision
- **captain_server** (d4): senior server who leads service team and handles special requests
- **server_assistant** (d4): assistant who helps servers with drink refills and table maintenance
- **lead_server** (d5): experienced server who trains and mentors newer servers
- **mentor_server** (d6): experienced server who mentors newer service staff

### from `technology_and_pos`
- **customer_profiling** (d3): Building behavioral and preference data profiles for individual guests
- **customer_relationship_management_crm** (d3): Database tracking guest preferences purchase history and contact information
- **email_marketing_integration** (d3): Connection between POS data and email campaign platform for guest outreach
- **guest_seating_optimization** (d3): Algorithm matching party sizes and preferences to optimal available tables
- **opentable_integration** (d3): Two way sync between reservation platform and table management system
- **sms_marketing_integration** (d3): Link between restaurant system and text message marketing platform
- **waitlist_management_system** (d3): Digital tool tracking walk in guests and estimated seating wait times
- **payment_processing** (d4): Complete cycle of authorizing settling and depositing card transactions
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

## CONSUMERS (what needs this)
`comp_reservation`, `front_of_house_manager`, `podium`, `reservation`, `seating_manager`, `table_allocation`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
