---
name: 0.10.1-understand-general_manager
description: [0.10.1] top manager with full responsibility for restaurant operations and profit
---

# understand-general_manager

**CALL NUMBER:** `staffing_and_roles.general_manager : reservations_and_seating(62), defined(46), technology_and_pos(31), facilities_and_equipment(8), front_of_house_service(7), finance_and_costing(2)`
**DEFINITION:** top manager with full responsibility for restaurant operations and profit

Invoke this skill to understand `general_manager` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **budget** (d1): A financial plan estimating income and expenses over a period.
- **firing** (d1): The kitchen process of cooking and plating orders during service.
- **hiring** (d1): The process of recruiting, interviewing, and employing staff for a restaurant
- **profit_loss** (d1): Financial statement tracking revenue versus expenses
- **interview** (d2): A meeting to evaluate a job candidate's qualifications and fit for a position
- **onboarding** (d2): The process of integrating and training new employees into a workplace
- **recruitment** (d2): Process of hiring staff for restaurant positions
- **food_cost** (d3): The expense of ingredients used to prepare menu items for the restaurant.
- **inventory** (d3): The complete stock of food, supplies, and materials a restaurant keeps on hand
- **labor_cost** (d3): The total expense of employing workers including wages, benefits, and taxes
- **shift_schedule** (d3): Weekly timetable showing employee work hours
- **bar_inventory** (d3): The stock of alcoholic beverages and supplies kept behind the bar.
- **drink_menu** (d3): A listing of available beverages including cocktails, soft drinks, and coffee.
- **liquor_cost** (d3): The expense of purchasing alcoholic beverages for a restaurant or bar
- **table_clearing** (d4): Removing dirty dishes and resetting tables after guests leave
- **table_resetting** (d4): Preparing clean tables with linens and place settings
- **seating** (d4): Arrangement of tables and chairs for restaurant guests
- **order** (d4): A request for food or drinks from a customer or to a supplier
- **table_service** (d4): Servers bringing food and drinks directly to seated guests
- **tip_payout** (d4): The process of distributing earned tips to employees, often done daily or weekly.
- **closing_checklist** (d4): A list of tasks staff complete at the end of service.
- **service_quality** (d4): Standard of customer service provided by staff
- **guest_complaint** (d4): A customer expressing dissatisfaction about food, service, or environment.
- **guest_feedback** (d4): Customer opinions about their dining experience, positive or negative.
- **quality_control** (d4): Process ensuring consistent food and service standards

### from `facilities_and_equipment`
- **dishwasher** (d4): high temperature door or conveyor dishwasher
- **cash_drawer** (d4): locking compartment storing cash in register
- **table_number** (d5): numbered card or stand identifying table location
- **private_dining_room** (d5): enclosed room for exclusive group dining
- **host_stand** (d6): designated station for greeting and seating guests
- **coat_check** (d7): designated area with staff for storing guest coats
- **podium** (d7): standing desk for host and cashier
- **high_chair** (d7): boosted seat for infants and toddlers

### from `finance_and_costing`
- **corkage_fee** (d6): Charge for customer bringing own wine
- **wine_cost_percentage** (d7): Cost of wine relative to wine sales

### from `front_of_house_service`
- **bread_service** (d4): Offering fresh bread with butter upon seating
- **water_service** (d4): Initial water pour with proper glass placement and lemon optional
- **bread_basket_refill** (d5): Replenishing bread basket during meal
- **butter_service** (d5): Providing softened butter with bread course
- **olive_oil_dipping** (d5): Offering olive oil for artisan bread service
- **ice_level_maintenance** (d5): Ensuring adequate ice in beverages during service
- **water_refill** (d5): Replenishing water glass throughout dining experience

### from `reservations_and_seating`
- **maitre_d** (d3): senior hospitality professional managing front of house
- **waitlist** (d4): list of guests awaiting an available table
- **seating_chart** (d4): visual diagram showing table positions and numbers
- **front_door_staff** (d4): team personnel stationed at restaurant entrance
- **host** (d4): staff member who greets and seats incoming guests
- **priority_seating** (d4): preferential table assignment for VIP or special guests
- **reservation_book** (d4): physical ledger or digital log of all bookings
- **vip_room** (d4): premium private room for important or celebrity guests
- **station** (d4): specific group of tables under one server's responsibility
- **reservation_system** (d5): software or platform managing booking operations
- **buzzer_system** (d5): paging device alerting waiting guests their table is ready
- **called_ahead_list** (d5): waitlist maintained via telephone for early arrival
- **pager** (d5): handheld device given to guests on waitlist
- **party_size** (d5): number of guests in a dining group
- **seating_manager** (d5): staff member coordinating guest flow and table assignment
- **text_alert** (d5): SMS notification when table is ready
- **wait_time_estimate** (d5): predicted delay before a table becomes available
- **waiting_area** (d5): lobby or lounge space for standing waiting guests
- **blocked_table** (d5): table marked unavailable for guest seating
- **capacity_chart** (d5): document showing maximum covers by table type and time
- **floor_plan** (d5): architectural layout showing all seating areas
- **reserved_table** (d5): table held exclusively for confirmed reservation
- **section** (d5): designated area of tables assigned to one server
- **table_formation** (d5): configuration of multiple tables pushed together for large groups
- **greeter** (d5): employee welcoming guests at entrance

### from `staffing_and_roles`
- **assistant_manager** (d1): manager who supports general manager and covers shifts
- **managing_partner** (d1): partner with management authority and operational responsibility
- **operations_manager** (d1): manager focused on operational efficiency and processes
- **owner_operator** (d1): owner who actively manages day-to-day restaurant operations
- **restaurant_manager** (d1): manager who oversees all front and back of house operations
- **staffing_coordinator** (d1): staff who recruits and coordinates staffing needs
- **duty_manager** (d2): manager on duty with authority during a specific period
- **floor_manager** (d2): manager who supervises dining room during service
- **shift_manager** (d2): manager who oversees specific shifts and staffing
- **front_of_house_manager** (d2): manager who oversees dining room, servers, and guest experience
- **kitchen_manager** (d2): manager who oversees kitchen operations, inventory, and staff scheduling
- **scheduling_manager** (d2): staff who creates and manages employee schedules
- **bar_manager** (d2): manager who oversees bar operations, inventory, and bar staff
- **busser** (d3): staff who clears tables, resets dining areas, and assists servers
- **captain** (d3): senior front of house lead who manages dining room service
- **host_hostess** (d3): staff member who greets guests, manages reservations, and seats diners
- **server** (d3): waiter who takes orders, delivers food, and provides table service
- **closing_manager** (d3): manager who oversees closing duties and night operations
- **opening_manager** (d3): manager who leads morning opening procedures and prep
- **captain_server** (d3): senior server who leads service team and handles special requests
- **host_manager** (d3): manager who oversees host team and reservations
- **service_supervisor** (d3): supervisor who manages service staff performance
- **head_count_manager** (d3): staff who tracks attendance and labor hours
- **kitchen_supervisor** (d3): supervisor who oversees kitchen staff and quality
- **prep_cook** (d3): cook who prepares ingredients and performs prep work before service

### from `technology_and_pos`
- **payment_processing** (d5): Complete cycle of authorizing settling and depositing card transactions
- **customer_profiling** (d6): Building behavioral and preference data profiles for individual guests
- **customer_relationship_management_crm** (d6): Database tracking guest preferences purchase history and contact information
- **email_marketing_integration** (d6): Connection between POS data and email campaign platform for guest outreach
- **guest_seating_optimization** (d6): Algorithm matching party sizes and preferences to optimal available tables
- **opentable_integration** (d6): Two way sync between reservation platform and table management system
- **sms_marketing_integration** (d6): Link between restaurant system and text message marketing platform
- **waitlist_management_system** (d6): Digital tool tracking walk in guests and estimated seating wait times
- **digital_review_request** (d7): Automated prompt encouraging guests to rate experience on review platforms
- **feedback_tablet** (d7): Tablet device soliciting customer satisfaction ratings after meal
- **loyalty_program_software** (d7): System managing customer reward points punch cards and member tiers
- **personalized_recommendations** (d7): AI suggesting menu items based on individual customer taste preferences
- **saved_payment_methods** (d7): Secure storage of customer credit card information for faster future checkout
- **spending_history_tracking** (d7): Recording of past purchases to identify customer ordering patterns
- **targeted_promotions** (d7): Customized discounts or offers sent to specific customers based on their data
- **online_ordering_platform** (d7): Website or app enabling customers to place orders for pickup or delivery
- **opentable_reservation_sync** (d7): Automatic updating of availability across OpenTable and restaurant systems
- **table_management_system** (d7): Software coordinating table assignments seating flow and turn times
- **customer_wait_time_display** (d7): Screen showing estimated wait time for food preparation and pickup
- **digital_waitlist_app** (d7): Mobile interface allowing guests to join queue and receive text notifications
- **estimated_ready_time** (d7): Calculated time when order will be prepared for customer pickup or delivery
- **live_delivery_tracking** (d7): Customer facing map showing driver location and estimated arrival time
- **order_tracking** (d7): Real time status updates for customers monitoring their order progress
- **customer_loyalty_app** (d8): Branded mobile application tracking member rewards and personalized offers
- **payment_gateway** (d8): Merchant service bridging restaurant POS and payment processor networks

## CONSUMERS (what needs this)
`area_manager`, `district_manager`, `franchise_manager`, `franchise_owner`, `managing_partner`, `owner_operator`, `regional_manager`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
