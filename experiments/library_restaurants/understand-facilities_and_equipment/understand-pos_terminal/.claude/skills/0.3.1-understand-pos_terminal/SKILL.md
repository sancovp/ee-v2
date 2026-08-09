---
name: 0.3.1-understand-pos_terminal
description: [0.3.1] point of sale touch screen computer for orders and payments
---

# understand-pos_terminal

**CALL NUMBER:** `facilities_and_equipment.pos_terminal : technology_and_pos(167), finance_and_costing(16), front_of_house_service(1), reservations_and_seating(1), defined(1)`
**DEFINITION:** point of sale touch screen computer for orders and payments

Invoke this skill to understand `pos_terminal` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **text_notification_waitlist** (d4): A system that sends SMS messages to guests alerting them when their table is ready.

### from `facilities_and_equipment`
- **cash_drawer** (d1): locking compartment storing cash in register
- **credit_card_reader** (d1): card terminal for processing electronic payments
- **receipt_printer** (d1): printer for customer receipts
- **kitchen_display_system** (d3): digital screen displaying orders for kitchen staff
- **digital_menu_board** (d3): electronic screen displaying menu items and prices

### from `finance_and_costing`
- **food_cost_percentage** (d3): Cost of ingredients divided by food sales revenue
- **table_turnover_rate** (d3): Number of times tables are occupied per shift
- **average_check** (d4): Average total spent per table or party
- **food_cost_per_plate** (d4): Ingredient cost for single menu item
- **menu_price** (d4): Listed price for menu item
- **seat_turnover** (d4): Number of customers per seat per day
- **combo_meal_cost** (d5): Ingredient and labor cost of bundled meal deal
- **liquor_cost_percentage** (d5): Cost of spirits relative to spirit sales
- **portion_cost** (d5): Cost of one serving portion of item
- **plate_cost** (d6): Total cost of ingredients in finished dish
- **pour_cost** (d6): Cost of alcohol poured versus alcohol revenue
- **cook_time_cost** (d7): Labor cost of active cooking per item
- **plating_cost** (d7): Labor cost to assemble and plate finished dish
- **prep_time_cost** (d7): Labor cost of preparation work per item
- **recipe_cost** (d7): Total ingredient cost per recipe batch
- **ingredient_cost** (d8): Price paid for individual food ingredient

### from `front_of_house_service`
- **cash_handling** (d1): Counting and processing cash payments

### from `reservations_and_seating`
- **reservation_system** (d2): software or platform managing booking operations

### from `technology_and_pos`
- **audit_logging** (d1): Immutable record of all POS transactions and system activities for review
- **barcode_scanner** (d1): Optical scanner device to read product barcodes for inventory and ordering
- **batch_closing** (d1): Finalizing daily credit card transactions for deposit and reconciliation
- **cloud_pos** (d1): Internet based POS system storing data on remote servers with real time sync
- **comp_management** (d1): System for authorizing and tracking complimentary items and discounts
- **contactless_payment_reader** (d1): NFC enabled reader for Apple Pay Google Pay Samsung Pay and contactless cards
- **discount_application** (d1): POS function applying percentage or dollar off promotions to transactions
- **electronic_order_ticket** (d1): Digital version of paper order ticket transmitted from POS to kitchen
- **employee_permission_levels** (d1): Differentiated access rights for managers servers hosts versus owners
- **emv_chip_reader** (d1): Europay Mastercard Visa compliant card reader for chip card transaction security
- **end_of_day_reconciliation** (d1): Closing process comparing register totals to expected cash and card receipts
- **manager_override** (d1): Supervisor authentication required to execute restricted POS functions
- **network_stability** (d1): Reliable internet connectivity essential for cloud POS and online ordering operations
- **offline_mode** (d1): POS capability to process transactions without internet connectivity
- **on_premise_pos** (d1): Locally installed POS system running on premises server hardware
- **order_management** (d1): End to end process of capturing transmitting and fulfilling customer orders
- **payment_processing** (d1): Complete cycle of authorizing settling and depositing card transactions
- **pci_compliance** (d1): Payment Card Industry Data Security Standard requirements for card handling
- **pin_pad** (d1): Dedicated keypad device for customers to enter personal identification numbers
- **pos_api** (d1): Application programming interface allowing external apps to communicate with POS
- **pos_security** (d1): Safeguards protecting point of sale system from unauthorized access and fraud
- **pos_software** (d1): Application program that manages sales transactions inventory and customer data
- **real_time_sync** (d1): Instantaneous data synchronization across all connected devices and locations
- **refund_protection** (d1): Procedures and verification steps before returning money to customers
- **role_based_access_control** (d1): Security model granting system capabilities based on assigned job role

## CONSUMERS (what needs this)
`digital_tipping`, `electronic_signature`, `gift_card_system`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
