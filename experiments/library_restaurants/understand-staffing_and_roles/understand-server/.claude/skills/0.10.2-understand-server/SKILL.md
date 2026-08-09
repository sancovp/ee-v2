---
name: 0.10.2-understand-server
description: [0.10.2] waiter who takes orders, delivers food, and provides table service
---

# understand-server

**CALL NUMBER:** `staffing_and_roles.server : defined(15), front_of_house_service(7), technology_and_pos(1)`
**DEFINITION:** waiter who takes orders, delivers food, and provides table service

Invoke this skill to understand `server` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **order** (d1): A request for food or drinks from a customer or to a supplier
- **table_service** (d1): Servers bringing food and drinks directly to seated guests
- **tip_payout** (d1): The process of distributing earned tips to employees, often done daily or weekly.
- **closing_reconciliation** (d2): Final cash and credit card accounting at end of business day.
- **tip_distribution** (d2): The method of allocating tips among servers, hosts, bussers, and other service staff.
- **plate_delivery** (d2): The service of bringing prepared food to the customer's table
- **curbside_delivery** (d2): Food service where orders are brought out to customers parked outside.
- **packaging** (d2): Materials used to wrap or contain food for takeout or delivery
- **takeout_order** (d2): Food prepared for customers to take home and eat
- **plating** (d3): The art of arranging and presenting food attractively on a plate
- **drink_refills** (d3): Additional servings of beverages provided free or at cost to guests.
- **table_maintenance** (d3): Ongoing cleaning and restocking of dining tables
- **service_quality** (d4): Standard of customer service provided by staff
- **table_clearing** (d4): Removing dirty dishes and resetting tables after guests leave
- **table_resetting** (d4): Preparing clean tables with linens and place settings

### from `front_of_house_service`
- **bread_service** (d4): Offering fresh bread with butter upon seating
- **water_service** (d4): Initial water pour with proper glass placement and lemon optional
- **bread_basket_refill** (d5): Replenishing bread basket during meal
- **butter_service** (d5): Providing softened butter with bread course
- **olive_oil_dipping** (d5): Offering olive oil for artisan bread service
- **ice_level_maintenance** (d5): Ensuring adequate ice in beverages during service
- **water_refill** (d5): Replenishing water glass throughout dining experience

### from `staffing_and_roles`
- **cashier** (d1): staff who processes guest payments and handles receipts
- **food_runner** (d1): staff who delivers food from kitchen to tables
- **to_go_specialist** (d1): staff who prepares takeout orders and handles curbside service
- **trainee_server** (d1): new server learning service procedures under supervision
- **expeditor** (d2): staff who coordinates orders between kitchen and servers
- **server_assistant** (d2): assistant who helps servers with drink refills and table maintenance
- **captain_server** (d3): senior server who leads service team and handles special requests
- **busser** (d3): staff who clears tables, resets dining areas, and assists servers
- **lead_server** (d4): experienced server who trains and mentors newer servers
- **mentor_server** (d5): experienced server who mentors newer service staff

### from `technology_and_pos`
- **payment_processing** (d2): Complete cycle of authorizing settling and depositing card transactions

## CONSUMERS (what needs this)
`assistant_server`, `captain`, `captain_server`, `expeditor`, `floor_manager`, `lead_server`, `service_supervisor`, `trainee_server`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
