---
name: 0.8.1-understand-american_cuisine
description: [0.8.1] Food native to the United States including burgers, BBQ, and fusion dishes
---

# understand-american_cuisine

**CALL NUMBER:** `menu_and_cuisine.american_cuisine : defined(28)`
**DEFINITION:** Food native to the United States including burgers, BBQ, and fusion dishes

Invoke this skill to understand `american_cuisine` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **hot_dog** (d1): A cooked sausage served in a sliced bun with various condiments
- **cheese** (d2): A dairy product made by curdling milk and aging it.
- **lettuce** (d2): A leafy green vegetable used as a base for salads and sandwiches
- **onion** (d2): A bulb vegetable with a pungent flavor, used as a base in cooking
- **pickle** (d2): A cucumber preserved in vinegar or brine, used as a condiment
- **tomato** (d2): A red fruit used as a vegetable in cooking, common in sauces, salads, and garnishes.
- **cajun_cuisine** (d2): Spicy Louisiana cooking style using roux and bold seasonings.
- **soul_food** (d2): African American comfort cuisine with roots in the South
- **southern_cuisine** (d2): Cooking style from the American South with comfort foods
- **chicken** (d2): Poultry meat prepared by roasting grilling or frying.
- **berries** (d2): Small juicy fruits including strawberries blueberries and raspberries.
- **butter** (d2): A dairy product made by churning cream used for cooking.
- **maple_syrup** (d2): A sweet syrup made from maple tree sap, used as a pancake topping
- **corn_on_cob** (d3): Whole corn kernels boiled or grilled on the cob, often buttered.
- **sauteed_greens** (d3): Leafy vegetables cooked quickly in hot pan with oil
- **sauteed_spinach** (d3): Spinach prepared by quick cooking in a hot pan
- **canadian_bacon** (d4): Back bacon from pork loin with a fat rim unlike regular bacon.
- **english_muffin** (d4): A round split bread commonly toasted and served with butter for breakfast.
- **hollandaise** (d4): A rich butter and egg yolk sauce with lemon juice, used for eggs Benedict
- **ham** (d4): Pork from the hind leg of a pig, often cured, smoked, or salted
- **mushrooms** (d4): Edible fungi used in cooking for their savory umami flavor
- **onions** (d4): Bulb vegetables used extensively in cooking for flavor
- **peppers** (d4): Various Capsicum vegetables used in cooking for flavor and heat
- **spinach** (d4): Leafy green vegetable served cooked or raw in salads
- **bloody_mary** (d5): A cocktail made with vodka tomato juice and various spices.

### from `menu_and_cuisine`
- **bbq_sauce** (d1): Sweet and tangy sauce for grilled meats
- **biscuit_and_gravy** (d1): American breakfast of biscuits with sausage gravy
- **burger** (d1): Ground beef patty in a bun with various toppings
- **chicken_wings** (d1): Chicken wing sections, often fried and sauced
- **coleslaw** (d1): Shredded raw cabbage in creamy dressing
- **cornbread** (d1): Baked cornmeal bread, often slightly sweet
- **french_fries** (d1): Deep-fried strips of potato
- **grilled_chicken** (d1): Chicken cooked on a grill
- **mac_and_cheese** (d1): Pasta in creamy cheese sauce
- **pancakes** (d1): Flat round breakfast cakes made from batter
- **breakfast_menu** (d2): Morning menu with breakfast items
- **bacon** (d2): Cured pork belly, fried crisp
- **medium** (d2): Meat cooked to 140-145F internal temperature
- **medium_well** (d2): Meat cooked to 150-155F internal temperature
- **well_done** (d2): Meat cooked to 160F or higher
- **side_dish** (d2): Secondary dish served alongside the main course
- **eggs_benedict** (d3): Poached eggs on English muffin with ham and hollandaise
- **french_toast** (d3): Bread dipped in egg and fried
- **hash_browns** (d3): Shredded potatoes fried until crispy
- **omelette** (d3): Eggs beaten and fried with fillings
- **garlic_bread** (d3): Bread sliced and spread with garlic butter, toasted
- **mashed_potatoes** (d3): Boiled potatoes mashed with butter and milk
- **onion_rings** (d3): Deep-fried breaded onion slices
- **sauteed_mushrooms** (d3): Mushrooms cooked quickly in pan
- **brunch_menu** (d4): Menu for late morning meal combining breakfast and lunch

## CONSUMERS (what needs this)
`apple_pie`, `baked_beans`, `banana_cream_pie`, `bbq_sauce`, `beer`, `biscuit_and_gravy`, `brownie`, `buffalo_wings`, `burger`, `carrot_cake`, `cheesecake`, `cherry_pie`, `chicken_wings`, `chocolate_lava_cake`, `cobb_salad`, `coconut_cream_pie`, `cookie`, `corn_dog`, `cornbread`, `fried_chicken`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
