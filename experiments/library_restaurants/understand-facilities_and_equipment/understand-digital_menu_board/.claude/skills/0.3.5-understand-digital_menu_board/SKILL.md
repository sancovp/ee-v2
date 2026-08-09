---
name: 0.3.5-understand-digital_menu_board
description: [0.3.5] electronic screen displaying menu items and prices
---

# understand-digital_menu_board

**CALL NUMBER:** `facilities_and_equipment.digital_menu_board : technology_and_pos(126), finance_and_costing(16), reservations_and_seating(1), defined(1), front_of_house_service(1)`
**DEFINITION:** electronic screen displaying menu items and prices

Invoke this skill to understand `digital_menu_board` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **text_notification_waitlist** (d6): A system that sends SMS messages to guests alerting them when their table is ready.

### from `facilities_and_equipment`
- **kitchen_display_system** (d3): digital screen displaying orders for kitchen staff
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
- **menu_engineering_software** (d1): Analytics platform evaluating menu items by popularity and profitability matrix
- **menu_management_system** (d1): Software for creating editing pricing and organizing menu items and categories
- **customer_relationship_management_crm** (d2): Database tracking guest preferences purchase history and contact information
- **menu_item_screen** (d2): Image display of specific menu item for reference during food preparation
- **mobile_ordering** (d2): Smartphone based system allowing customers to browse menu and place orders
- **qr_code_ordering** (d2): System where customers scan QR codes to access digital menu and order
- **self_service_kiosk** (d2): Standing digital terminal for customers to browse menu and place orders independently
- **demand_forecasting** (d2): Analysis predicting customer demand to optimize purchasing and staffing
- **predictive_analytics** (d2): Statistical techniques forecasting future outcomes based on historical data
- **revenue_management** (d2): Strategic pricing and inventory control to maximize profit from available capacity
- **analytics_reporting_dashboard** (d2): Visual interface displaying key performance metrics and business intelligence
- **menu_item_profitability** (d2): Analysis of revenue versus cost for each menu item offering
- **menu_optimization_algorithm** (d2): AI analyzing sales data to recommend profitable menu item decisions
- **food_allergy_alert_system** (d2): Digital notification flagging orders containing guest allergy information
- **google_menu_integration** (d2): Syncing menu data with Google Business Profile for accurate search display
- **instagram_menu_link** (d2): Bio link directing social media followers to online menu or ordering page
- **menu_label_printer** (d2): Device printing allergen and ingredient labels for individual plated dishes
- **menu_price_sync** (d2): Automated price updates across all platforms when POS menu pricing changes
- **order_confirmation_display** (d2): Screen showing customer order details for verification before submission
- **personalized_recommendations** (d2): AI suggesting menu items based on individual customer taste preferences
- **plate_cost_calculator** (d2): Program determining food cost per plate for menu pricing decisions
- **recipe_costing_software** (d2): Tool calculating true cost of each menu item based on ingredient quantities
- **yelp_menu_sync** (d2): Automatic updating of menu content displayed on Yelp business listing

## CONSUMERS (what needs this)
`allergen_filtering`, `menu_management_system`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
