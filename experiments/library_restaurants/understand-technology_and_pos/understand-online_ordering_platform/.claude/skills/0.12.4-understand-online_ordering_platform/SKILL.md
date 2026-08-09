---
name: 0.12.4-understand-online_ordering_platform
description: [0.12.4] Website or app enabling customers to place orders for pickup or delivery
---

# understand-online_ordering_platform

**CALL NUMBER:** `technology_and_pos.online_ordering_platform : finance_and_costing(16), facilities_and_equipment(3), reservations_and_seating(1), front_of_house_service(1), defined(1)`
**DEFINITION:** Website or app enabling customers to place orders for pickup or delivery

Invoke this skill to understand `online_ordering_platform` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **text_notification_waitlist** (d4): A system that sends SMS messages to guests alerting them when their table is ready.

### from `facilities_and_equipment`
- **credit_card_reader** (d2): card terminal for processing electronic payments
- **kitchen_display_system** (d3): digital screen displaying orders for kitchen staff
- **digital_menu_board** (d3): electronic screen displaying menu items and prices

### from `finance_and_costing`
- **food_cost_percentage** (d2): Cost of ingredients divided by food sales revenue
- **average_check** (d3): Average total spent per table or party
- **food_cost_per_plate** (d3): Ingredient cost for single menu item
- **menu_price** (d3): Listed price for menu item
- **table_turnover_rate** (d4): Number of times tables are occupied per shift
- **combo_meal_cost** (d4): Ingredient and labor cost of bundled meal deal
- **liquor_cost_percentage** (d4): Cost of spirits relative to spirit sales
- **portion_cost** (d4): Cost of one serving portion of item
- **seat_turnover** (d5): Number of customers per seat per day
- **plate_cost** (d5): Total cost of ingredients in finished dish
- **pour_cost** (d5): Cost of alcohol poured versus alcohol revenue
- **cook_time_cost** (d6): Labor cost of active cooking per item
- **plating_cost** (d6): Labor cost to assemble and plate finished dish
- **prep_time_cost** (d6): Labor cost of preparation work per item
- **recipe_cost** (d6): Total ingredient cost per recipe batch
- **ingredient_cost** (d7): Price paid for individual food ingredient

### from `front_of_house_service`
- **cash_handling** (d3): Counting and processing cash payments

### from `reservations_and_seating`
- **reservation_system** (d2): software or platform managing booking operations

### from `technology_and_pos`
- **api_integration** (d1): Technical connection allowing different software systems to share data
- **customer_relationship_management_crm** (d1): Database tracking guest preferences purchase history and contact information
- **customer_wait_time_display** (d1): Screen showing estimated wait time for food preparation and pickup
- **digital_receipt** (d1): Electronic receipt sent via email or text instead of printed paper copy
- **email_marketing_integration** (d1): Connection between POS data and email campaign platform for guest outreach
- **estimated_ready_time** (d1): Calculated time when order will be prepared for customer pickup or delivery
- **menu_price_sync** (d1): Automated price updates across all platforms when POS menu pricing changes
- **mobile_ordering** (d1): Smartphone based system allowing customers to browse menu and place orders
- **order_tracking** (d1): Real time status updates for customers monitoring their order progress
- **payment_processing_gateway** (d1): Service that securely transmits payment data between merchant and processor
- **qr_code_ordering** (d1): System where customers scan QR codes to access digital menu and order
- **restaurant_app** (d1): Mobile application branded for the restaurant for ordering and engagement
- **saved_payment_methods** (d1): Secure storage of customer credit card information for faster future checkout
- **sms_marketing_integration** (d1): Link between restaurant system and text message marketing platform
- **targeted_promotions** (d1): Customized discounts or offers sent to specific customers based on their data
- **unified_inventory** (d1): Single inventory database updated by all sales channels to prevent overselling
- **backoffice_accounting_software** (d2): Financial program managing accounts payable receivable and general ledger
- **food_tech_platform** (d2): Comprehensive ecosystem of restaurant technology providers and tools
- **loyalty_program_software** (d2): System managing customer reward points punch cards and member tiers
- **opentable_integration** (d2): Two way sync between reservation platform and table management system
- **payment_gateway** (d2): Merchant service bridging restaurant POS and payment processor networks
- **pos_api** (d2): Application programming interface allowing external apps to communicate with POS
- **square_integration** (d2): Connection to Square payment ecosystem and associated restaurant tools
- **staff_payroll_integration** (d2): Direct data flow from time tracking to payroll processing system
- **supplier_integration** (d2): Direct electronic connection between restaurant ordering and vendor systems

## CONSUMERS (what needs this)
`api_integration`, `cloud_pos`, `email_marketing_integration`, `gift_card_system`, `pos_api`, `pos_software`, `saved_payment_methods`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
