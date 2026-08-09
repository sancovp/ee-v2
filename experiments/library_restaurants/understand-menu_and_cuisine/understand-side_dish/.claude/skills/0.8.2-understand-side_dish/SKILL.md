---
name: 0.8.2-understand-side_dish
description: [0.8.2] Secondary dish served alongside the main course
---

# understand-side_dish

**CALL NUMBER:** `menu_and_cuisine.side_dish : defined(28)`
**DEFINITION:** Secondary dish served alongside the main course

Invoke this skill to understand `side_dish` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **corn_on_cob** (d1): Whole corn kernels boiled or grilled on the cob, often buttered.
- **sauteed_greens** (d1): Leafy vegetables cooked quickly in hot pan with oil
- **sauteed_spinach** (d1): Spinach prepared by quick cooking in a hot pan
- **soul_food** (d2): African American comfort cuisine with roots in the South
- **southern_cuisine** (d2): Cooking style from the American South with comfort foods
- **hot_dog** (d3): A cooked sausage served in a sliced bun with various condiments
- **cheese** (d4): A dairy product made by curdling milk and aging it.
- **lettuce** (d4): A leafy green vegetable used as a base for salads and sandwiches
- **onion** (d4): A bulb vegetable with a pungent flavor, used as a base in cooking
- **pickle** (d4): A cucumber preserved in vinegar or brine, used as a condiment
- **tomato** (d4): A red fruit used as a vegetable in cooking, common in sauces, salads, and garnishes.
- **cajun_cuisine** (d4): Spicy Louisiana cooking style using roux and bold seasonings.
- **chicken** (d4): Poultry meat prepared by roasting grilling or frying.
- **berries** (d4): Small juicy fruits including strawberries blueberries and raspberries.
- **butter** (d4): A dairy product made by churning cream used for cooking.
- **maple_syrup** (d4): A sweet syrup made from maple tree sap, used as a pancake topping
- **canadian_bacon** (d6): Back bacon from pork loin with a fat rim unlike regular bacon.
- **english_muffin** (d6): A round split bread commonly toasted and served with butter for breakfast.
- **hollandaise** (d6): A rich butter and egg yolk sauce with lemon juice, used for eggs Benedict
- **ham** (d6): Pork from the hind leg of a pig, often cured, smoked, or salted
- **mushrooms** (d6): Edible fungi used in cooking for their savory umami flavor
- **onions** (d6): Bulb vegetables used extensively in cooking for flavor
- **peppers** (d6): Various Capsicum vegetables used in cooking for flavor and heat
- **spinach** (d6): Leafy green vegetable served cooked or raw in salads
- **bloody_mary** (d7): A cocktail made with vodka tomato juice and various spices.

### from `menu_and_cuisine`
- **coleslaw** (d1): Shredded raw cabbage in creamy dressing
- **french_fries** (d1): Deep-fried strips of potato
- **garlic_bread** (d1): Bread sliced and spread with garlic butter, toasted
- **mac_and_cheese** (d1): Pasta in creamy cheese sauce
- **mashed_potatoes** (d1): Boiled potatoes mashed with butter and milk
- **onion_rings** (d1): Deep-fried breaded onion slices
- **sauteed_mushrooms** (d1): Mushrooms cooked quickly in pan
- **american_cuisine** (d2): Food native to the United States including burgers, BBQ, and fusion dishes
- **bbq_sauce** (d3): Sweet and tangy sauce for grilled meats
- **biscuit_and_gravy** (d3): American breakfast of biscuits with sausage gravy
- **burger** (d3): Ground beef patty in a bun with various toppings
- **chicken_wings** (d3): Chicken wing sections, often fried and sauced
- **cornbread** (d3): Baked cornmeal bread, often slightly sweet
- **grilled_chicken** (d3): Chicken cooked on a grill
- **pancakes** (d3): Flat round breakfast cakes made from batter
- **breakfast_menu** (d4): Morning menu with breakfast items
- **bacon** (d4): Cured pork belly, fried crisp
- **medium** (d4): Meat cooked to 140-145F internal temperature
- **medium_well** (d4): Meat cooked to 150-155F internal temperature
- **well_done** (d4): Meat cooked to 160F or higher
- **eggs_benedict** (d5): Poached eggs on English muffin with ham and hollandaise
- **french_toast** (d5): Bread dipped in egg and fried
- **hash_browns** (d5): Shredded potatoes fried until crispy
- **omelette** (d5): Eggs beaten and fried with fillings
- **brunch_menu** (d6): Menu for late morning meal combining breakfast and lunch

## CONSUMERS (what needs this)
`buffet`, `catering_menu`, `coleslaw`, `combo_meal`, `cornbread`, `creamed_spinach`, `family_style`, `french_fries`, `garlic_bread`, `grilled_asparagus`, `mac_and_cheese`, `mashed_potatoes`, `onion_rings`, `roasted_vegetables`, `sauteed_greens`, `sauteed_mushrooms`, `steamed_broccoli`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
