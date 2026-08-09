---
name: 0.12.2-understand-inventory_management_system
description: [0.12.2] Digital tool tracking stock levels ingredient usage and reorder alerts
---

# understand-inventory_management_system

**CALL NUMBER:** `technology_and_pos.inventory_management_system : finance_and_costing(16), facilities_and_equipment(3), reservations_and_seating(1), defined(1), front_of_house_service(1)`
**DEFINITION:** Digital tool tracking stock levels ingredient usage and reorder alerts

Invoke this skill to understand `inventory_management_system` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **text_notification_waitlist** (d8): A system that sends SMS messages to guests alerting them when their table is ready.

### from `facilities_and_equipment`
- **kitchen_display_system** (d2): digital screen displaying orders for kitchen staff
- **digital_menu_board** (d3): electronic screen displaying menu items and prices
- **credit_card_reader** (d6): card terminal for processing electronic payments

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
- **cash_handling** (d9): Counting and processing cash payments

### from `reservations_and_seating`
- **reservation_system** (d6): software or platform managing booking operations

### from `technology_and_pos`
- **barcode_scanner** (d1): Optical scanner device to read product barcodes for inventory and ordering
- **demand_forecasting** (d1): Analysis predicting customer demand to optimize purchasing and staffing
- **expiration_date_alert** (d1): Automated warning when product shelf life approaches spoilage threshold
- **food_storage_tracking** (d1): System managing ingredient locations and quantities in storage areas
- **ingredient_level_inventory** (d1): Stock tracking broken down to individual ingredient components
- **inventory_alert_system** (d1): Automated notifications when stock reaches predetermined reorder points
- **inventory_count_scanner** (d1): Handheld barcode scanner for rapid physical inventory counts
- **inventory_forecasting** (d1): Algorithm predicting future stock needs based on sales trends and seasonality
- **online_ordering_aggregation** (d1): Consolidating orders from all digital channels into single kitchen view
- **predictive_analytics** (d1): Statistical techniques forecasting future outcomes based on historical data
- **recipe_level_inventory** (d1): Inventory system using menu item recipes to calculate ingredient needs
- **reorder_point** (d1): Stock level threshold triggering purchase orders to suppliers
- **spoilage_tracking** (d1): Logging waste and expired product to identify loss patterns and causes
- **supplier_integration** (d1): Direct electronic connection between restaurant ordering and vendor systems
- **third_party_delivery_aggregation** (d1): Platform consolidating orders from multiple delivery apps into one screen
- **unified_inventory** (d1): Single inventory database updated by all sales channels to prevent overselling
- **waste_logging** (d1): Recording of discarded food and ingredients for cost analysis purposes
- **menu_item_profitability** (d2): Analysis of revenue versus cost for each menu item offering
- **plate_cost_calculator** (d2): Program determining food cost per plate for menu pricing decisions
- **recipe_costing_software** (d2): Tool calculating true cost of each menu item based on ingredient quantities
- **menu_price_sync** (d2): Automated price updates across all platforms when POS menu pricing changes
- **order_management** (d2): End to end process of capturing transmitting and fulfilling customer orders
- **labor_percentage_alerts** (d2): Notifications when payroll costs approach or exceed target percentages
- **menu_optimization_algorithm** (d2): AI analyzing sales data to recommend profitable menu item decisions
- **revenue_management** (d2): Strategic pricing and inventory control to maximize profit from available capacity

## CONSUMERS (what needs this)
`automated_food_prep`, `food_safety_tracking`, `food_storage_tracking`, `ingredient_level_inventory`, `pos_api`, `pos_software`, `recipe_costing_software`, `recipe_level_inventory`, `restaurant_management_software`, `spoilage_tracking`, `unified_inventory`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
