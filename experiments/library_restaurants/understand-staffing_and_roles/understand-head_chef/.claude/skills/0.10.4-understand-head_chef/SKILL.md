---
name: 0.10.4-understand-head_chef
description: [0.10.4] chef who runs daily kitchen operations and manages brigade
---

# understand-head_chef

**CALL NUMBER:** `staffing_and_roles.head_chef : reservations_and_seating(70), technology_and_pos(45), defined(33), facilities_and_equipment(10), front_of_house_service(7), finance_and_costing(5)`
**DEFINITION:** chef who runs daily kitchen operations and manages brigade

Invoke this skill to understand `head_chef` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **menu** (d1): A list of food and beverages offered by a restaurant
- **plating** (d2): The art of arranging and presenting food attractively on a plate
- **cleaning_supplies** (d2): Products used for cleaning and sanitizing the restaurant.
- **equipment_maintenance** (d2): Regular cleaning and servicing of kitchen equipment to ensure proper function.
- **quality_control** (d2): Process ensuring consistent food and service standards
- **service_quality** (d3): Standard of customer service provided by staff
- **plate_delivery** (d3): The service of bringing prepared food to the customer's table
- **order** (d3): A request for food or drinks from a customer or to a supplier
- **table_service** (d3): Servers bringing food and drinks directly to seated guests
- **tip_payout** (d3): The process of distributing earned tips to employees, often done daily or weekly.
- **food_cost** (d3): The expense of ingredients used to prepare menu items for the restaurant.
- **inventory** (d3): The complete stock of food, supplies, and materials a restaurant keeps on hand
- **drink_refills** (d4): Additional servings of beverages provided free or at cost to guests.
- **table_maintenance** (d4): Ongoing cleaning and restocking of dining tables
- **closing_reconciliation** (d4): Final cash and credit card accounting at end of business day.
- **tip_distribution** (d4): The method of allocating tips among servers, hosts, bussers, and other service staff.
- **curbside_delivery** (d4): Food service where orders are brought out to customers parked outside.
- **packaging** (d4): Materials used to wrap or contain food for takeout or delivery
- **takeout_order** (d4): Food prepared for customers to take home and eat
- **labor_cost** (d4): The total expense of employing workers including wages, benefits, and taxes
- **shift_schedule** (d4): Weekly timetable showing employee work hours
- **table_clearing** (d5): Removing dirty dishes and resetting tables after guests leave
- **table_resetting** (d5): Preparing clean tables with linens and place settings
- **hiring** (d5): The process of recruiting, interviewing, and employing staff for a restaurant
- **interview** (d5): A meeting to evaluate a job candidate's qualifications and fit for a position

### from `facilities_and_equipment`
- **dishwasher** (d3): high temperature door or conveyor dishwasher
- **host_stand** (d9): designated station for greeting and seating guests
- **high_chair** (d9): boosted seat for infants and toddlers
- **table_number** (d9): numbered card or stand identifying table location
- **coat_check** (d10): designated area with staff for storing guest coats
- **podium** (d10): standing desk for host and cashier
- **private_dining_room** (d10): enclosed room for exclusive group dining
- **booster_seat** (d10): raised seat for young children at table
- **booth** (d11): upholstered bench style seating against a wall
- **banquette** (d11): long upholstered bench seating along a wall

### from `finance_and_costing`
- **corkage_fee** (d8): Charge for customer bringing own wine
- **wine_cost_percentage** (d9): Cost of wine relative to wine sales
- **pour_cost** (d10): Cost of alcohol poured versus alcohol revenue
- **table_turnover_rate** (d11): Number of times tables are occupied per shift
- **portion_cost** (d11): Cost of one serving portion of item

### from `front_of_house_service`
- **bread_service** (d5): Offering fresh bread with butter upon seating
- **water_service** (d5): Initial water pour with proper glass placement and lemon optional
- **bread_basket_refill** (d6): Replenishing bread basket during meal
- **butter_service** (d6): Providing softened butter with bread course
- **olive_oil_dipping** (d6): Offering olive oil for artisan bread service
- **ice_level_maintenance** (d6): Ensuring adequate ice in beverages during service
- **water_refill** (d6): Replenishing water glass throughout dining experience

### from `reservations_and_seating`
- **station** (d2): specific group of tables under one server's responsibility
- **cover_count** (d3): number of guests to be seated
- **party_size** (d4): number of guests in a dining group
- **seating_capacity** (d4): total number of seats available in the restaurant
- **capacity_chart** (d5): document showing maximum covers by table type and time
- **floor_plan** (d5): architectural layout showing all seating areas
- **off_peak** (d5): quieter periods with lower reservation demand
- **peak_hours** (d5): busiest dining periods with highest demand
- **reservation_limit** (d5): maximum number of bookings allowed per time slot
- **table_formation** (d6): configuration of multiple tables pushed together for large groups
- **deposit_required** (d6): monetary payment needed to secure booking
- **overbooking** (d6): accepting more reservations than available seating capacity
- **priority_seating** (d6): preferential table assignment for VIP or special guests
- **quoted_wait** (d6): time given to walk-in guests before expected seating
- **split_shift** (d6): adjusting seating intervals to maximize covers
- **table_turnover** (d6): rate at which tables become available for new guests
- **wait_time_estimate** (d6): predicted delay before a table becomes available
- **time_slot** (d6): specific reserved time block for dining
- **four_top** (d7): table designed for four diners
- **rectangular_table** (d7): elongated table with longer length than width
- **round_table** (d7): circular dining table
- **six_top** (d7): table designed for six diners
- **two_top** (d7): table designed for two diners
- **credit_card_hold** (d7): placing a hold on card to guarantee reservation
- **waitlist** (d7): list of guests awaiting an available table

### from `staffing_and_roles`
- **chef_de_partie** (d1): station chef responsible for a specific area of kitchen production
- **expeditor** (d1): staff who coordinates orders between kitchen and servers
- **kitchen_steward** (d1): staff who manages kitchen supplies, cleaning, and sanitation
- **kitchen_supervisor** (d1): supervisor who oversees kitchen staff and quality
- **line_cook** (d1): cook working a specific station on the kitchen line during service
- **prep_cook** (d1): cook who prepares ingredients and performs prep work before service
- **sous_chef** (d1): second-in-command chef who assists executive chef and manages kitchen in their absence
- **commis_chef** (d2): junior chef still learning under senior chefs
- **captain_server** (d2): senior server who leads service team and handles special requests
- **food_runner** (d2): staff who delivers food from kitchen to tables
- **server** (d2): waiter who takes orders, delivers food, and provides table service
- **plongeur** (d2): dishwasher in French brigade kitchen system
- **apprentice_cook** (d2): entry level cook learning culinary fundamentals
- **trainee_cook** (d2): cook learning the trade under supervision
- **kitchen_manager** (d2): manager who oversees kitchen operations, inventory, and staff scheduling
- **lead_server** (d3): experienced server who trains and mentors newer servers
- **server_assistant** (d3): assistant who helps servers with drink refills and table maintenance
- **cashier** (d3): staff who processes guest payments and handles receipts
- **to_go_specialist** (d3): staff who prepares takeout orders and handles curbside service
- **trainee_server** (d3): new server learning service procedures under supervision
- **head_count_manager** (d3): staff who tracks attendance and labor hours
- **scheduling_manager** (d3): staff who creates and manages employee schedules
- **mentor_server** (d4): experienced server who mentors newer service staff
- **busser** (d4): staff who clears tables, resets dining areas, and assists servers
- **staffing_coordinator** (d4): staff who recruits and coordinates staffing needs

### from `technology_and_pos`
- **payment_processing** (d4): Complete cycle of authorizing settling and depositing card transactions
- **customer_profiling** (d9): Building behavioral and preference data profiles for individual guests
- **customer_relationship_management_crm** (d9): Database tracking guest preferences purchase history and contact information
- **email_marketing_integration** (d9): Connection between POS data and email campaign platform for guest outreach
- **guest_seating_optimization** (d9): Algorithm matching party sizes and preferences to optimal available tables
- **opentable_integration** (d9): Two way sync between reservation platform and table management system
- **sms_marketing_integration** (d9): Link between restaurant system and text message marketing platform
- **waitlist_management_system** (d9): Digital tool tracking walk in guests and estimated seating wait times
- **digital_review_request** (d10): Automated prompt encouraging guests to rate experience on review platforms
- **feedback_tablet** (d10): Tablet device soliciting customer satisfaction ratings after meal
- **loyalty_program_software** (d10): System managing customer reward points punch cards and member tiers
- **personalized_recommendations** (d10): AI suggesting menu items based on individual customer taste preferences
- **saved_payment_methods** (d10): Secure storage of customer credit card information for faster future checkout
- **spending_history_tracking** (d10): Recording of past purchases to identify customer ordering patterns
- **targeted_promotions** (d10): Customized discounts or offers sent to specific customers based on their data
- **online_ordering_platform** (d10): Website or app enabling customers to place orders for pickup or delivery
- **opentable_reservation_sync** (d10): Automatic updating of availability across OpenTable and restaurant systems
- **table_management_system** (d10): Software coordinating table assignments seating flow and turn times
- **customer_wait_time_display** (d10): Screen showing estimated wait time for food preparation and pickup
- **digital_waitlist_app** (d10): Mobile interface allowing guests to join queue and receive text notifications
- **estimated_ready_time** (d10): Calculated time when order will be prepared for customer pickup or delivery
- **live_delivery_tracking** (d10): Customer facing map showing driver location and estimated arrival time
- **order_tracking** (d10): Real time status updates for customers monitoring their order progress
- **customer_loyalty_app** (d11): Branded mobile application tracking member rewards and personalized offers
- **payment_gateway** (d11): Merchant service bridging restaurant POS and payment processor networks

## CONSUMERS (what needs this)
`executive_chef`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
