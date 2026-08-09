---
name: 0.9.6-understand-seating_chart
description: [0.9.6] visual diagram showing table positions and numbers
---

# understand-seating_chart

**CALL NUMBER:** `reservations_and_seating.seating_chart : technology_and_pos(69), defined(21), staffing_and_roles(14), facilities_and_equipment(11), finance_and_costing(8), front_of_house_service(7)`
**DEFINITION:** visual diagram showing table positions and numbers

Invoke this skill to understand `seating_chart` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **server_staff** (d3): Employees who take orders and serve food to customers
- **anniversary_seating** (d7): Special reserved seating for customers celebrating restaurant anniversaries.
- **guest_complaint** (d8): A customer expressing dissatisfaction about food, service, or environment.
- **seating** (d9): Arrangement of tables and chairs for restaurant guests
- **table_management** (d9): Coordinating table assignments and service flow efficiently
- **text_notification_waitlist** (d9): A system that sends SMS messages to guests alerting them when their table is ready.
- **table_clearing** (d10): Removing dirty dishes and resetting tables after guests leave
- **table_resetting** (d10): Preparing clean tables with linens and place settings
- **plate_delivery** (d10): The service of bringing prepared food to the customer's table
- **order** (d10): A request for food or drinks from a customer or to a supplier
- **table_service** (d10): Servers bringing food and drinks directly to seated guests
- **tip_payout** (d10): The process of distributing earned tips to employees, often done daily or weekly.
- **plating** (d11): The art of arranging and presenting food attractively on a plate
- **closing_reconciliation** (d11): Final cash and credit card accounting at end of business day.
- **tip_distribution** (d11): The method of allocating tips among servers, hosts, bussers, and other service staff.
- **curbside_delivery** (d11): Food service where orders are brought out to customers parked outside.
- **packaging** (d11): Materials used to wrap or contain food for takeout or delivery
- **takeout_order** (d11): Food prepared for customers to take home and eat
- **service_quality** (d12): Standard of customer service provided by staff
- **drink_refills** (d12): Additional servings of beverages provided free or at cost to guests.
- **table_maintenance** (d12): Ongoing cleaning and restocking of dining tables

### from `facilities_and_equipment`
- **table_number** (d1): numbered card or stand identifying table location
- **host_stand** (d8): designated station for greeting and seating guests
- **high_chair** (d8): boosted seat for infants and toddlers
- **coat_check** (d9): designated area with staff for storing guest coats
- **podium** (d9): standing desk for host and cashier
- **private_dining_room** (d9): enclosed room for exclusive group dining
- **booster_seat** (d9): raised seat for young children at table
- **booth** (d10): upholstered bench style seating against a wall
- **banquette** (d10): long upholstered bench seating along a wall
- **credit_card_reader** (d11): card terminal for processing electronic payments
- **bar_stool** (d11): tall stool for bar and high top seating

### from `finance_and_costing`
- **corkage_fee** (d7): Charge for customer bringing own wine
- **wine_cost_percentage** (d8): Cost of wine relative to wine sales
- **pour_cost** (d9): Cost of alcohol poured versus alcohol revenue
- **table_turnover_rate** (d10): Number of times tables are occupied per shift
- **portion_cost** (d10): Cost of one serving portion of item
- **food_cost_percentage** (d11): Cost of ingredients divided by food sales revenue
- **average_check** (d11): Average total spent per table or party
- **seat_turnover** (d11): Number of customers per seat per day

### from `front_of_house_service`
- **bread_service** (d10): Offering fresh bread with butter upon seating
- **water_service** (d10): Initial water pour with proper glass placement and lemon optional
- **bread_basket_refill** (d11): Replenishing bread basket during meal
- **butter_service** (d11): Providing softened butter with bread course
- **olive_oil_dipping** (d11): Offering olive oil for artisan bread service
- **ice_level_maintenance** (d11): Ensuring adequate ice in beverages during service
- **water_refill** (d11): Replenishing water glass throughout dining experience

### from `reservations_and_seating`
- **blocked_table** (d1): table marked unavailable for guest seating
- **capacity_chart** (d1): document showing maximum covers by table type and time
- **floor_plan** (d1): architectural layout showing all seating areas
- **reserved_table** (d1): table held exclusively for confirmed reservation
- **section** (d1): designated area of tables assigned to one server
- **table_formation** (d1): configuration of multiple tables pushed together for large groups
- **table_status** (d2): current condition or availability state of a table
- **cover_count** (d2): number of guests to be seated
- **reserved_sign** (d2): marker indicating table is held for upcoming reservation
- **rotation_system** (d2): method for evenly distributing sections among servers
- **station** (d2): specific group of tables under one server's responsibility
- **four_top** (d2): table designed for four diners
- **rectangular_table** (d2): elongated table with longer length than width
- **round_table** (d2): circular dining table
- **six_top** (d2): table designed for six diners
- **two_top** (d2): table designed for two diners
- **party_size** (d3): number of guests in a dining group
- **seating_capacity** (d3): total number of seats available in the restaurant
- **square_table** (d3): table with four equal sides
- **tablecloth** (d3): fabric covering placed over dining table
- **off_peak** (d4): quieter periods with lower reservation demand
- **peak_hours** (d4): busiest dining periods with highest demand
- **reservation_limit** (d4): maximum number of bookings allowed per time slot
- **deposit_required** (d5): monetary payment needed to secure booking
- **overbooking** (d5): accepting more reservations than available seating capacity

### from `staffing_and_roles`
- **captain** (d8): senior front of house lead who manages dining room service
- **host_hostess** (d8): staff member who greets guests, manages reservations, and seats diners
- **private_dining_manager** (d8): manager who handles private dining reservations and service
- **reservation_manager** (d8): staff who manages bookings and seating logistics
- **busser** (d9): staff who clears tables, resets dining areas, and assists servers
- **food_runner** (d9): staff who delivers food from kitchen to tables
- **server** (d9): waiter who takes orders, delivers food, and provides table service
- **expeditor** (d10): staff who coordinates orders between kitchen and servers
- **cashier** (d10): staff who processes guest payments and handles receipts
- **to_go_specialist** (d10): staff who prepares takeout orders and handles curbside service
- **trainee_server** (d10): new server learning service procedures under supervision
- **captain_server** (d11): senior server who leads service team and handles special requests
- **server_assistant** (d11): assistant who helps servers with drink refills and table maintenance
- **lead_server** (d12): experienced server who trains and mentors newer servers

### from `technology_and_pos`
- **customer_profiling** (d8): Building behavioral and preference data profiles for individual guests
- **customer_relationship_management_crm** (d8): Database tracking guest preferences purchase history and contact information
- **email_marketing_integration** (d8): Connection between POS data and email campaign platform for guest outreach
- **guest_seating_optimization** (d8): Algorithm matching party sizes and preferences to optimal available tables
- **opentable_integration** (d8): Two way sync between reservation platform and table management system
- **sms_marketing_integration** (d8): Link between restaurant system and text message marketing platform
- **waitlist_management_system** (d8): Digital tool tracking walk in guests and estimated seating wait times
- **digital_review_request** (d9): Automated prompt encouraging guests to rate experience on review platforms
- **feedback_tablet** (d9): Tablet device soliciting customer satisfaction ratings after meal
- **loyalty_program_software** (d9): System managing customer reward points punch cards and member tiers
- **personalized_recommendations** (d9): AI suggesting menu items based on individual customer taste preferences
- **saved_payment_methods** (d9): Secure storage of customer credit card information for faster future checkout
- **spending_history_tracking** (d9): Recording of past purchases to identify customer ordering patterns
- **targeted_promotions** (d9): Customized discounts or offers sent to specific customers based on their data
- **online_ordering_platform** (d9): Website or app enabling customers to place orders for pickup or delivery
- **opentable_reservation_sync** (d9): Automatic updating of availability across OpenTable and restaurant systems
- **table_management_system** (d9): Software coordinating table assignments seating flow and turn times
- **customer_wait_time_display** (d9): Screen showing estimated wait time for food preparation and pickup
- **digital_waitlist_app** (d9): Mobile interface allowing guests to join queue and receive text notifications
- **estimated_ready_time** (d9): Calculated time when order will be prepared for customer pickup or delivery
- **live_delivery_tracking** (d9): Customer facing map showing driver location and estimated arrival time
- **order_tracking** (d9): Real time status updates for customers monitoring their order progress
- **customer_loyalty_app** (d10): Branded mobile application tracking member rewards and personalized offers
- **payment_gateway** (d10): Merchant service bridging restaurant POS and payment processor networks
- **restaurant_app** (d10): Mobile application branded for the restaurant for ordering and engagement

## CONSUMERS (what needs this)
`blocked_table`, `host`, `host_manager`, `reserved_table`, `table_allocation`, `walk_in`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
