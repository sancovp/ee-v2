---
name: 0.8.4-understand-burger
description: [0.8.4] Ground beef patty in a bun with various toppings
---

# understand-burger

**CALL NUMBER:** `menu_and_cuisine.burger : defined(28)`
**DEFINITION:** Ground beef patty in a bun with various toppings

Invoke this skill to understand `burger` down to its primitives. The RELATIVE ROOT below is the least-fixed-point closure of everything it bundles from — the full import cone, grouped by the lib each prim comes from. Projected from a prover-typed KB (MAP/SWI-Prolog consistency gate): every reference below resolves.

## THE RELATIVE ROOT (the import cone, by lib)

### from `defined`
- **cheese** (d1): A dairy product made by curdling milk and aging it.
- **lettuce** (d1): A leafy green vegetable used as a base for salads and sandwiches
- **onion** (d1): A bulb vegetable with a pungent flavor, used as a base in cooking
- **pickle** (d1): A cucumber preserved in vinegar or brine, used as a condiment
- **tomato** (d1): A red fruit used as a vegetable in cooking, common in sauces, salads, and garnishes.
- **hot_dog** (d2): A cooked sausage served in a sliced bun with various condiments
- **cajun_cuisine** (d3): Spicy Louisiana cooking style using roux and bold seasonings.
- **soul_food** (d3): African American comfort cuisine with roots in the South
- **southern_cuisine** (d3): Cooking style from the American South with comfort foods
- **chicken** (d3): Poultry meat prepared by roasting grilling or frying.
- **berries** (d3): Small juicy fruits including strawberries blueberries and raspberries.
- **butter** (d3): A dairy product made by churning cream used for cooking.
- **maple_syrup** (d3): A sweet syrup made from maple tree sap, used as a pancake topping
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
- **american_cuisine** (d1): Food native to the United States including burgers, BBQ, and fusion dishes
- **bacon** (d1): Cured pork belly, fried crisp
- **coleslaw** (d1): Shredded raw cabbage in creamy dressing
- **french_fries** (d1): Deep-fried strips of potato
- **medium** (d1): Meat cooked to 140-145F internal temperature
- **medium_well** (d1): Meat cooked to 150-155F internal temperature
- **well_done** (d1): Meat cooked to 160F or higher
- **bbq_sauce** (d2): Sweet and tangy sauce for grilled meats
- **biscuit_and_gravy** (d2): American breakfast of biscuits with sausage gravy
- **chicken_wings** (d2): Chicken wing sections, often fried and sauced
- **cornbread** (d2): Baked cornmeal bread, often slightly sweet
- **grilled_chicken** (d2): Chicken cooked on a grill
- **mac_and_cheese** (d2): Pasta in creamy cheese sauce
- **pancakes** (d2): Flat round breakfast cakes made from batter
- **breakfast_menu** (d2): Morning menu with breakfast items
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
`american_cuisine`, `carryout_menu`, `combo_meal`, `kids_menu`, `lunch_menu`, `main_course`

---
*Projected from the `restaurants` KB (2849 concepts / 2428 relations) — consistency-typed by MAP; the facet list after the colon IS the cross-lib dependency web.*

_(leaf — this is an actual skill.)_
