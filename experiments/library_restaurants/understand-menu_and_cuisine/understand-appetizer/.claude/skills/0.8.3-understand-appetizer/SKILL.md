---
name: 0.8.3-understand-appetizer
description: [0.8.3] Small dish served before the main course to stimulate appetite
---

# understand-appetizer

**CALL NUMBER:** `menu_and_cuisine.appetizer : defined(50)`
**DEFINITION:** Small dish served before the main course to stimulate appetite

Invoke this skill to understand `appetizer` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `?`
- **vegetables** (d2): «undefined»

### from `defined`
- **cajun_cuisine** (d3): Spicy Louisiana cooking style using roux and bold seasonings.
- **soul_food** (d3): African American comfort cuisine with roots in the South
- **southern_cuisine** (d3): Cooking style from the American South with comfort foods
- **corn_on_cob** (d3): Whole corn kernels boiled or grilled on the cob, often buttered.
- **sauteed_greens** (d3): Leafy vegetables cooked quickly in hot pan with oil
- **sauteed_spinach** (d3): Spinach prepared by quick cooking in a hot pan
- **anchovies** (d3): Small salty fish often used as pizza topping or in sauces.
- **croutons** (d3): Toasted or fried cubes of bread used to top salads and soups.
- **parmesan** (d3): A hard Italian cheese used for grating over pasta and other dishes
- **avocado** (d3): A creamy green fruit used in dishes like guacamole and salads.
- **chicken** (d3): Poultry meat prepared by roasting grilling or frying.
- **egg** (d3): A single poultry product used in cooking, baking, or as a breakfast item.
- **cucumber** (d3): A cool refreshing vegetable often sliced in salads or pickled.
- **feta** (d3): A brined Greek cheese with tangy flavor, crumbled on salads and in dishes.
- **olives** (d3): Small fruits preserved in brine or oil, used as toppings or ingredients
- **bread** (d3): A baked food made from flour and water in many varieties.
- **gruyere** (d3): A nutty Swiss cheese often melted in sandwiches and gratins.
- **basil** (d3): An aromatic green herb commonly used in Italian and Thai cuisine.
- **bean_sprouts** (d3): Germinated beans used as a crunchy topping or ingredient in Asian dishes.
- **beef** (d3): Meat from cattle prepared by roasting grilling braising or other methods.
- **hoisin** (d3): A sweet and savory Chinese sauce made from soybeans, garlic, and spices
- **lime** (d3): A sour citrus fruit used for its juice and zest in cooking and drinks
- **rice_noodles** (d3): Noodles made from rice flour used in Asian dishes
- **sriracha** (d3): Spicy Thai chili sauce used as condiment
- **green_onion** (d3): An onion variety with edible green tops, used as garnish or in cooking.

### from `menu_and_cuisine`
- **breadbasket** (d1): Basket of bread served at the table
- **bruschetta** (d1): Toasted bread topped with tomatoes and basil
- **caprese_salad** (d1): Italian salad of tomatoes, mozzarella, and basil
- **dumplings** (d1): Small dough包裹 filled with meat or vegetables
- **guacamole** (d1): Mashed avocado dip with lime and cilantro
- **hummus** (d1): Creamy dip made from chickpeas and tahini
- **jalape_o_poppers** (d1): Stuffed jalapeño peppers, often breaded and fried
- **mozzarella_sticks** (d1): Breaded and fried mozzarella cheese sticks
- **nachos** (d1): Tortilla chips topped with cheese and toppings
- **onion_rings** (d1): Deep-fried breaded onion slices
- **salad** (d1): Cold dish of mixed vegetables, often with dressing
- **salsa** (d1): Mexican tomato-based condiment
- **soup** (d1): Liquid dish often served as starter, hot or cold
- **spring_rolls** (d1): Crispy cylindrical appetizer with vegetable or meat filling
- **tapas** (d1): Small Spanish dishes served with drinks
- **cornbread** (d2): Baked cornmeal bread, often slightly sweet
- **dinner_roll** (d2): Small round bread serving individual portions
- **focaccia** (d2): Italian flatbread with olive oil and herbs
- **garlic_bread** (d2): Bread sliced and spread with garlic butter, toasted
- **naan** (d2): Indian leavened oven-baked flatbread
- **pita_bread** (d2): Round flatbread with pocket
- **side_dish** (d2): Secondary dish served alongside the main course
- **caesar_salad** (d2): Salad with romaine, croutons, parmesan, and caesar dressing
- **cobb_salad** (d2): American composed salad with chicken, bacon, egg, and avocado
- **greek_salad** (d2): Salad with tomatoes, cucumbers, olives, and feta cheese

## CONSUMERS (what needs this)
`banquet_menu`, `buffet`, `catering_menu`, `combo_meal`, `sampler_platter`, `tasting_menu`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
