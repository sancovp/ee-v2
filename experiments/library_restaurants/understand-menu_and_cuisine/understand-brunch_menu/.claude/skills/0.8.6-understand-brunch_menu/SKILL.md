---
name: 0.8.6-understand-brunch_menu
description: [0.8.6] Menu for late morning meal combining breakfast and lunch
---

# understand-brunch_menu

**CALL NUMBER:** `menu_and_cuisine.brunch_menu : defined(28)`
**DEFINITION:** Menu for late morning meal combining breakfast and lunch

Invoke this skill to understand `brunch_menu` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **bloody_mary** (d1): A cocktail made with vodka tomato juice and various spices.
- **coffee** (d1): A brewed hot beverage made from roasted coffee beans.
- **mimosa** (d1): A brunch cocktail made with champagne and orange juice
- **eggs** (d2): Poultry products used in breakfast dishes, baking, and as ingredients.
- **tomato** (d2): A red fruit used as a vegetable in cooking, common in sauces, salads, and garnishes.
- **canadian_bacon** (d2): Back bacon from pork loin with a fat rim unlike regular bacon.
- **english_muffin** (d2): A round split bread commonly toasted and served with butter for breakfast.
- **hollandaise** (d2): A rich butter and egg yolk sauce with lemon juice, used for eggs Benedict
- **berries** (d2): Small juicy fruits including strawberries blueberries and raspberries.
- **maple_syrup** (d2): A sweet syrup made from maple tree sap, used as a pancake topping
- **cheese** (d2): A dairy product made by curdling milk and aging it.
- **ham** (d2): Pork from the hind leg of a pig, often cured, smoked, or salted
- **mushrooms** (d2): Edible fungi used in cooking for their savory umami flavor
- **onions** (d2): Bulb vegetables used extensively in cooking for flavor
- **peppers** (d2): Various Capsicum vegetables used in cooking for flavor and heat
- **spinach** (d2): Leafy green vegetable served cooked or raw in salads
- **butter** (d2): A dairy product made by churning cream used for cooking.
- **hot_dog** (d3): A cooked sausage served in a sliced bun with various condiments
- **lettuce** (d4): A leafy green vegetable used as a base for salads and sandwiches
- **onion** (d4): A bulb vegetable with a pungent flavor, used as a base in cooking
- **pickle** (d4): A cucumber preserved in vinegar or brine, used as a condiment
- **cajun_cuisine** (d4): Spicy Louisiana cooking style using roux and bold seasonings.
- **soul_food** (d4): African American comfort cuisine with roots in the South
- **southern_cuisine** (d4): Cooking style from the American South with comfort foods
- **chicken** (d4): Poultry meat prepared by roasting grilling or frying.

### from `menu_and_cuisine`
- **avocado_toast** (d1): Smashed avocado on toasted bread
- **bacon** (d1): Cured pork belly, fried crisp
- **biscuit_and_gravy** (d1): American breakfast of biscuits with sausage gravy
- **breakfast_burrito** (d1): Burrito filled with eggs, cheese, and breakfast meats
- **eggs_benedict** (d1): Poached eggs on English muffin with ham and hollandaise
- **french_toast** (d1): Bread dipped in egg and fried
- **hash_browns** (d1): Shredded potatoes fried until crispy
- **omelette** (d1): Eggs beaten and fried with fillings
- **pancakes** (d1): Flat round breakfast cakes made from batter
- **sausage_links** (d1): Ground meat in casing, grilled or fried
- **breakfast_menu** (d2): Morning menu with breakfast items
- **american_cuisine** (d2): Food native to the United States including burgers, BBQ, and fusion dishes
- **bbq_sauce** (d3): Sweet and tangy sauce for grilled meats
- **burger** (d3): Ground beef patty in a bun with various toppings
- **chicken_wings** (d3): Chicken wing sections, often fried and sauced
- **coleslaw** (d3): Shredded raw cabbage in creamy dressing
- **cornbread** (d3): Baked cornmeal bread, often slightly sweet
- **french_fries** (d3): Deep-fried strips of potato
- **grilled_chicken** (d3): Chicken cooked on a grill
- **mac_and_cheese** (d3): Pasta in creamy cheese sauce
- **medium** (d4): Meat cooked to 140-145F internal temperature
- **medium_well** (d4): Meat cooked to 150-155F internal temperature
- **well_done** (d4): Meat cooked to 160F or higher
- **side_dish** (d4): Secondary dish served alongside the main course
- **garlic_bread** (d5): Bread sliced and spread with garlic butter, toasted

## CONSUMERS (what needs this)
`chai_latte`, `eggs_benedict`, `mimosa`, `smoothie`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
