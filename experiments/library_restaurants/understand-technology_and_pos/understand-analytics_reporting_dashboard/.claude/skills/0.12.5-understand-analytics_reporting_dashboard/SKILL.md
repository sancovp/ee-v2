---
name: 0.12.5-understand-analytics_reporting_dashboard
description: [0.12.5] Visual interface displaying key performance metrics and business intelligence
---

# understand-analytics_reporting_dashboard

**CALL NUMBER:** `technology_and_pos.analytics_reporting_dashboard : finance_and_costing(16)`
**DEFINITION:** Visual interface displaying key performance metrics and business intelligence

Invoke this skill to understand `analytics_reporting_dashboard` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `finance_and_costing`
- **food_cost_percentage** (d1): Cost of ingredients divided by food sales revenue
- **table_turnover_rate** (d1): Number of times tables are occupied per shift
- **average_check** (d2): Average total spent per table or party
- **food_cost_per_plate** (d2): Ingredient cost for single menu item
- **menu_price** (d2): Listed price for menu item
- **seat_turnover** (d2): Number of customers per seat per day
- **combo_meal_cost** (d3): Ingredient and labor cost of bundled meal deal
- **liquor_cost_percentage** (d3): Cost of spirits relative to spirit sales
- **portion_cost** (d3): Cost of one serving portion of item
- **plate_cost** (d4): Total cost of ingredients in finished dish
- **pour_cost** (d4): Cost of alcohol poured versus alcohol revenue
- **cook_time_cost** (d5): Labor cost of active cooking per item
- **plating_cost** (d5): Labor cost to assemble and plate finished dish
- **prep_time_cost** (d5): Labor cost of preparation work per item
- **recipe_cost** (d5): Total ingredient cost per recipe batch
- **ingredient_cost** (d6): Price paid for individual food ingredient

### from `technology_and_pos`
- **average_ticket_size** (d1): Mean dollar amount spent per customer check including all items
- **cost_accounting** (d1): Detailed tracking and allocation of all restaurant operating expenses
- **demand_forecasting** (d1): Analysis predicting customer demand to optimize purchasing and staffing
- **labor_cost_software** (d1): Analytics program tracking payroll expenses as percentage of revenue
- **menu_item_profitability** (d1): Analysis of revenue versus cost for each menu item offering
- **menu_optimization_algorithm** (d1): AI analyzing sales data to recommend profitable menu item decisions
- **performance_metrics_dashboard** (d1): Visual display of employee KPI data including sales efficiency and ratings
- **predictive_analytics** (d1): Statistical techniques forecasting future outcomes based on historical data
- **profit_margin_tracking** (d1): Real time monitoring of net profit margins by category and time period
- **revenue_management** (d1): Strategic pricing and inventory control to maximize profit from available capacity
- **sales_reporting** (d1): Analysis of revenue by category time period item and server performance
- **server_performance_tracking** (d1): POS reporting on individual server sales volume tips and table efficiency
- **hourly_rate_management** (d2): System handling different pay rates for various job roles and shifts
- **labor_hour_tracking** (d2): Recording of employee work time for scheduling and payroll purposes
- **labor_percentage_alerts** (d2): Notifications when payroll costs approach or exceed target percentages
- **overtime_tracking** (d2): Monitoring hours worked beyond standard thresholds triggering premium pay
- **staff_payroll_integration** (d2): Direct data flow from time tracking to payroll processing system
- **inventory_forecasting** (d2): Algorithm predicting future stock needs based on sales trends and seasonality
- **scheduling_forecast** (d2): AI predicting labor needs based on historical traffic and upcoming events

## CONSUMERS (what needs this)
`labor_cost_software`, `menu_engineering_software`, `pos_api`, `pos_software`, `restaurant_management_software`, `spoilage_tracking`, `tip_distribution_software`, `waste_logging`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
