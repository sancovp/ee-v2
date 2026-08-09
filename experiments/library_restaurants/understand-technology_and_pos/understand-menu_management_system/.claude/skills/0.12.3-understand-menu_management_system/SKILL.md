---
name: 0.12.3-understand-menu_management_system
description: [0.12.3] Software for creating editing pricing and organizing menu items and categories
---

# understand-menu_management_system

**CALL NUMBER:** `technology_and_pos.menu_management_system : finance_and_costing(16), facilities_and_equipment(3), reservations_and_seating(1), defined(1), front_of_house_service(1)`
**DEFINITION:** Software for creating editing pricing and organizing menu items and categories

Invoke this skill to understand `menu_management_system` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **text_notification_waitlist** (d6): A system that sends SMS messages to guests alerting them when their table is ready.

### from `facilities_and_equipment`
- **digital_menu_board** (d1): electronic screen displaying menu items and prices
- **kitchen_display_system** (d2): digital screen displaying orders for kitchen staff
- **credit_card_reader** (d4): card terminal for processing electronic payments

### from `finance_and_costing`
- **food_cost_percentage** (d2): Cost of ingredients divided by food sales revenue
- **table_turnover_rate** (d3): Number of times tables are occupied per shift
- **average_check** (d3): Average total spent per table or party
- **food_cost_per_plate** (d3): Ingredient cost for single menu item
- **menu_price** (d3): Listed price for menu item
- **seat_turnover** (d4): Number of customers per seat per day
- **combo_meal_cost** (d4): Ingredient and labor cost of bundled meal deal
- **liquor_cost_percentage** (d4): Cost of spirits relative to spirit sales
- **portion_cost** (d4): Cost of one serving portion of item
- **plate_cost** (d5): Total cost of ingredients in finished dish
- **pour_cost** (d5): Cost of alcohol poured versus alcohol revenue
- **cook_time_cost** (d6): Labor cost of active cooking per item
- **plating_cost** (d6): Labor cost to assemble and plate finished dish
- **prep_time_cost** (d6): Labor cost of preparation work per item
- **recipe_cost** (d6): Total ingredient cost per recipe batch
- **ingredient_cost** (d7): Price paid for individual food ingredient

### from `front_of_house_service`
- **cash_handling** (d7): Counting and processing cash payments

### from `reservations_and_seating`
- **reservation_system** (d4): software or platform managing booking operations

### from `technology_and_pos`
- **allergen_filtering** (d1): Menu software blocking items containing specified allergens from display
- **dynamic_pricing** (d1): Real time price adjustments based on demand time of day and inventory levels
- **food_allergy_alert_system** (d1): Digital notification flagging orders containing guest allergy information
- **google_menu_integration** (d1): Syncing menu data with Google Business Profile for accurate search display
- **instagram_menu_link** (d1): Bio link directing social media followers to online menu or ordering page
- **menu_engineering_software** (d1): Analytics platform evaluating menu items by popularity and profitability matrix
- **menu_item_profitability** (d1): Analysis of revenue versus cost for each menu item offering
- **menu_label_printer** (d1): Device printing allergen and ingredient labels for individual plated dishes
- **menu_price_sync** (d1): Automated price updates across all platforms when POS menu pricing changes
- **order_confirmation_display** (d1): Screen showing customer order details for verification before submission
- **personalized_recommendations** (d1): AI suggesting menu items based on individual customer taste preferences
- **plate_cost_calculator** (d1): Program determining food cost per plate for menu pricing decisions
- **qr_code_ordering** (d1): System where customers scan QR codes to access digital menu and order
- **recipe_costing_software** (d1): Tool calculating true cost of each menu item based on ingredient quantities
- **yelp_menu_sync** (d1): Automatic updating of menu content displayed on Yelp business listing
- **customer_relationship_management_crm** (d2): Database tracking guest preferences purchase history and contact information
- **menu_item_screen** (d2): Image display of specific menu item for reference during food preparation
- **mobile_ordering** (d2): Smartphone based system allowing customers to browse menu and place orders
- **self_service_kiosk** (d2): Standing digital terminal for customers to browse menu and place orders independently
- **demand_forecasting** (d2): Analysis predicting customer demand to optimize purchasing and staffing
- **predictive_analytics** (d2): Statistical techniques forecasting future outcomes based on historical data
- **revenue_management** (d2): Strategic pricing and inventory control to maximize profit from available capacity
- **analytics_reporting_dashboard** (d2): Visual interface displaying key performance metrics and business intelligence
- **menu_optimization_algorithm** (d2): AI analyzing sales data to recommend profitable menu item decisions
- **contactless_payment_reader** (d2): NFC enabled reader for Apple Pay Google Pay Samsung Pay and contactless cards

## CONSUMERS (what needs this)
`allergen_filtering`, `digital_menu_board`, `dynamic_pricing`, `food_allergy_alert_system`, `google_menu_integration`, `pos_software`, `qr_code_ordering`, `recipe_level_inventory`, `restaurant_management_software`, `self_service_kiosk`, `unified_inventory`, `yelp_menu_sync`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
