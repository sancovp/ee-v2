---
name: 0.12.6-understand-unified_inventory
description: [0.12.6] Single inventory database updated by all sales channels to prevent overselling
---

# understand-unified_inventory

**CALL NUMBER:** `technology_and_pos.unified_inventory : finance_and_costing(16), facilities_and_equipment(3), reservations_and_seating(1), defined(1), front_of_house_service(1)`
**DEFINITION:** Single inventory database updated by all sales channels to prevent overselling

Invoke this skill to understand `unified_inventory` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **text_notification_waitlist** (d7): A system that sends SMS messages to guests alerting them when their table is ready.

### from `facilities_and_equipment`
- **digital_menu_board** (d2): electronic screen displaying menu items and prices
- **kitchen_display_system** (d2): digital screen displaying orders for kitchen staff
- **credit_card_reader** (d5): card terminal for processing electronic payments

### from `finance_and_costing`
- **food_cost_percentage** (d1): Cost of ingredients divided by food sales revenue
- **average_check** (d2): Average total spent per table or party
- **food_cost_per_plate** (d2): Ingredient cost for single menu item
- **menu_price** (d2): Listed price for menu item
- **combo_meal_cost** (d3): Ingredient and labor cost of bundled meal deal
- **liquor_cost_percentage** (d3): Cost of spirits relative to spirit sales
- **portion_cost** (d3): Cost of one serving portion of item
- **table_turnover_rate** (d3): Number of times tables are occupied per shift
- **plate_cost** (d4): Total cost of ingredients in finished dish
- **pour_cost** (d4): Cost of alcohol poured versus alcohol revenue
- **seat_turnover** (d4): Number of customers per seat per day
- **cook_time_cost** (d5): Labor cost of active cooking per item
- **plating_cost** (d5): Labor cost to assemble and plate finished dish
- **prep_time_cost** (d5): Labor cost of preparation work per item
- **recipe_cost** (d5): Total ingredient cost per recipe batch
- **ingredient_cost** (d6): Price paid for individual food ingredient

### from `front_of_house_service`
- **cash_handling** (d8): Counting and processing cash payments

### from `reservations_and_seating`
- **reservation_system** (d5): software or platform managing booking operations

### from `technology_and_pos`
- **ingredient_level_inventory** (d1): Stock tracking broken down to individual ingredient components
- **inventory_alert_system** (d1): Automated notifications when stock reaches predetermined reorder points
- **inventory_management_system** (d1): Digital tool tracking stock levels ingredient usage and reorder alerts
- **menu_management_system** (d1): Software for creating editing pricing and organizing menu items and categories
- **online_ordering_aggregation** (d1): Consolidating orders from all digital channels into single kitchen view
- **recipe_level_inventory** (d1): Inventory system using menu item recipes to calculate ingredient needs
- **spoilage_tracking** (d1): Logging waste and expired product to identify loss patterns and causes
- **supplier_integration** (d1): Direct electronic connection between restaurant ordering and vendor systems
- **third_party_delivery_aggregation** (d1): Platform consolidating orders from multiple delivery apps into one screen
- **third_party_delivery_integration** (d1): Software connection linking restaurant POS to DoorDash UberEats Grubhub
- **waste_logging** (d1): Recording of discarded food and ingredients for cost analysis purposes
- **expiration_date_alert** (d2): Automated warning when product shelf life approaches spoilage threshold
- **menu_item_profitability** (d2): Analysis of revenue versus cost for each menu item offering
- **plate_cost_calculator** (d2): Program determining food cost per plate for menu pricing decisions
- **recipe_costing_software** (d2): Tool calculating true cost of each menu item based on ingredient quantities
- **inventory_forecasting** (d2): Algorithm predicting future stock needs based on sales trends and seasonality
- **reorder_point** (d2): Stock level threshold triggering purchase orders to suppliers
- **barcode_scanner** (d2): Optical scanner device to read product barcodes for inventory and ordering
- **demand_forecasting** (d2): Analysis predicting customer demand to optimize purchasing and staffing
- **food_storage_tracking** (d2): System managing ingredient locations and quantities in storage areas
- **inventory_count_scanner** (d2): Handheld barcode scanner for rapid physical inventory counts
- **predictive_analytics** (d2): Statistical techniques forecasting future outcomes based on historical data
- **allergen_filtering** (d2): Menu software blocking items containing specified allergens from display
- **dynamic_pricing** (d2): Real time price adjustments based on demand time of day and inventory levels
- **food_allergy_alert_system** (d2): Digital notification flagging orders containing guest allergy information

## CONSUMERS (what needs this)
`doordash_integration`, `grubhub_integration`, `inventory_management_system`, `kitchen_display_system`, `online_ordering_aggregation`, `online_ordering_platform`, `postmates_integration`, `third_party_delivery_aggregation`, `third_party_delivery_integration`, `uber_eats_integration`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
