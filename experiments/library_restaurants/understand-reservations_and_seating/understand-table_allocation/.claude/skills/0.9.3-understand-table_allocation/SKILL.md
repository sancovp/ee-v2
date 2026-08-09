---
name: 0.9.3-understand-table_allocation
description: [0.9.3] process of assigning tables to arriving guests
---

# understand-table_allocation

**CALL NUMBER:** `reservations_and_seating.table_allocation : technology_and_pos(68), defined(21), staffing_and_roles(15), facilities_and_equipment(11), finance_and_costing(8), front_of_house_service(7)`
**DEFINITION:** process of assigning tables to arriving guests

Invoke this skill to understand `table_allocation` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **guest_complaint** (d2): A customer expressing dissatisfaction about food, service, or environment.
- **seating** (d3): Arrangement of tables and chairs for restaurant guests
- **table_management** (d3): Coordinating table assignments and service flow efficiently
- **anniversary_seating** (d3): Special reserved seating for customers celebrating restaurant anniversaries.
- **server_staff** (d3): Employees who take orders and serve food to customers
- **table_clearing** (d4): Removing dirty dishes and resetting tables after guests leave
- **table_resetting** (d4): Preparing clean tables with linens and place settings
- **plate_delivery** (d4): The service of bringing prepared food to the customer's table
- **order** (d4): A request for food or drinks from a customer or to a supplier
- **table_service** (d4): Servers bringing food and drinks directly to seated guests
- **tip_payout** (d4): The process of distributing earned tips to employees, often done daily or weekly.
- **plating** (d5): The art of arranging and presenting food attractively on a plate
- **closing_reconciliation** (d5): Final cash and credit card accounting at end of business day.
- **tip_distribution** (d5): The method of allocating tips among servers, hosts, bussers, and other service staff.
- **curbside_delivery** (d5): Food service where orders are brought out to customers parked outside.
- **packaging** (d5): Materials used to wrap or contain food for takeout or delivery
- **takeout_order** (d5): Food prepared for customers to take home and eat
- **text_notification_waitlist** (d5): A system that sends SMS messages to guests alerting them when their table is ready.
- **service_quality** (d6): Standard of customer service provided by staff
- **drink_refills** (d6): Additional servings of beverages provided free or at cost to guests.
- **table_maintenance** (d6): Ongoing cleaning and restocking of dining tables

### from `facilities_and_equipment`
- **table_number** (d1): numbered card or stand identifying table location
- **booth** (d2): upholstered bench style seating against a wall
- **private_dining_room** (d3): enclosed room for exclusive group dining
- **host_stand** (d4): designated station for greeting and seating guests
- **high_chair** (d4): boosted seat for infants and toddlers
- **coat_check** (d5): designated area with staff for storing guest coats
- **podium** (d5): standing desk for host and cashier
- **booster_seat** (d5): raised seat for young children at table
- **banquette** (d6): long upholstered bench seating along a wall
- **credit_card_reader** (d7): card terminal for processing electronic payments
- **bar_stool** (d7): tall stool for bar and high top seating

### from `finance_and_costing`
- **corkage_fee** (d3): Charge for customer bringing own wine
- **wine_cost_percentage** (d4): Cost of wine relative to wine sales
- **pour_cost** (d5): Cost of alcohol poured versus alcohol revenue
- **table_turnover_rate** (d6): Number of times tables are occupied per shift
- **portion_cost** (d6): Cost of one serving portion of item
- **food_cost_percentage** (d7): Cost of ingredients divided by food sales revenue
- **average_check** (d7): Average total spent per table or party
- **seat_turnover** (d7): Number of customers per seat per day

### from `front_of_house_service`
- **bread_service** (d4): Offering fresh bread with butter upon seating
- **water_service** (d4): Initial water pour with proper glass placement and lemon optional
- **bread_basket_refill** (d5): Replenishing bread basket during meal
- **butter_service** (d5): Providing softened butter with bread course
- **olive_oil_dipping** (d5): Offering olive oil for artisan bread service
- **ice_level_maintenance** (d5): Ensuring adequate ice in beverages during service
- **water_refill** (d5): Replenishing water glass throughout dining experience

### from `reservations_and_seating`
- **double_seating** (d1): scheduling two groups at same table time slot
- **floor_plan** (d1): architectural layout showing all seating areas
- **high_value_guest** (d1): frequent diner or important patron with priority seating
- **maitre_d** (d1): senior hospitality professional managing front of house
- **party_size** (d1): number of guests in a dining group
- **priority_seating** (d1): preferential table assignment for VIP or special guests
- **seating_capacity** (d1): total number of seats available in the restaurant
- **seating_chart** (d1): visual diagram showing table positions and numbers
- **seating_manager** (d1): staff member coordinating guest flow and table assignment
- **seating_sequence** (d1): order in which available tables are offered to guests
- **section** (d1): designated area of tables assigned to one server
- **station** (d1): specific group of tables under one server's responsibility
- **table_hopping** (d1): moving guests between tables during their visit
- **front_door_staff** (d2): team personnel stationed at restaurant entrance
- **host** (d2): staff member who greets and seats incoming guests
- **reservation_book** (d2): physical ledger or digital log of all bookings
- **vip_room** (d2): premium private room for important or celebrity guests
- **comp_reservation** (d2): complimentary booking for celebrity or press
- **special_occasion** (d2): celebration event like birthday or anniversary noted on reservation
- **capacity_chart** (d2): document showing maximum covers by table type and time
- **cover_count** (d2): number of guests to be seated
- **off_peak** (d2): quieter periods with lower reservation demand
- **peak_hours** (d2): busiest dining periods with highest demand
- **reservation_limit** (d2): maximum number of bookings allowed per time slot
- **blocked_table** (d2): table marked unavailable for guest seating

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
- **mentor_server** (d7): experienced server who mentors newer service staff

### from `technology_and_pos`
- **customer_profiling** (d4): Building behavioral and preference data profiles for individual guests
- **customer_relationship_management_crm** (d4): Database tracking guest preferences purchase history and contact information
- **email_marketing_integration** (d4): Connection between POS data and email campaign platform for guest outreach
- **guest_seating_optimization** (d4): Algorithm matching party sizes and preferences to optimal available tables
- **opentable_integration** (d4): Two way sync between reservation platform and table management system
- **sms_marketing_integration** (d4): Link between restaurant system and text message marketing platform
- **waitlist_management_system** (d4): Digital tool tracking walk in guests and estimated seating wait times
- **payment_processing** (d5): Complete cycle of authorizing settling and depositing card transactions
- **digital_review_request** (d5): Automated prompt encouraging guests to rate experience on review platforms
- **feedback_tablet** (d5): Tablet device soliciting customer satisfaction ratings after meal
- **loyalty_program_software** (d5): System managing customer reward points punch cards and member tiers
- **personalized_recommendations** (d5): AI suggesting menu items based on individual customer taste preferences
- **saved_payment_methods** (d5): Secure storage of customer credit card information for faster future checkout
- **spending_history_tracking** (d5): Recording of past purchases to identify customer ordering patterns
- **targeted_promotions** (d5): Customized discounts or offers sent to specific customers based on their data
- **online_ordering_platform** (d5): Website or app enabling customers to place orders for pickup or delivery
- **opentable_reservation_sync** (d5): Automatic updating of availability across OpenTable and restaurant systems
- **table_management_system** (d5): Software coordinating table assignments seating flow and turn times
- **customer_wait_time_display** (d5): Screen showing estimated wait time for food preparation and pickup
- **digital_waitlist_app** (d5): Mobile interface allowing guests to join queue and receive text notifications
- **estimated_ready_time** (d5): Calculated time when order will be prepared for customer pickup or delivery
- **live_delivery_tracking** (d5): Customer facing map showing driver location and estimated arrival time
- **order_tracking** (d5): Real time status updates for customers monitoring their order progress
- **customer_loyalty_app** (d6): Branded mobile application tracking member rewards and personalized offers
- **payment_gateway** (d6): Merchant service bridging restaurant POS and payment processor networks

## CONSUMERS (what needs this)
`dietary_accommodation`, `reservation`, `seating_manager`, `table_hopping`, `walk_in`, `wheelchair_accessible`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
