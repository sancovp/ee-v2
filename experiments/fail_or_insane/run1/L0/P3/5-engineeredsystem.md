# Pass 3 — Engineered System

# The Copper Beech Kitchen: Daily Workflow Generation System

## A Complete, Deployable Instance

---

# I. Executive Summary

## What This Document Is

This document presents **Pass 3: The Engineered System** for the Copper Beech Kitchen—a fully realized, deployable daily workflow generation system. Where Pass 1 established what workflow design *is* and Pass 2 designed a *system* for generating workflows, this document shows that system *operating* on a specific kitchen context to produce a specific daily workflow instance.

The Copper Beech Kitchen is a small farm-to-table restaurant serving dinner five nights per week. This document generates, configures, and deploys a complete daily workflow instance for **Saturday, April 15th**—a peak volume day with an expected 65 covers and 8:00 PM peak.

## The Generated Instance at a Glance

| Element | Saturday April 15th |
|---------|---------------------|
| **Expected Covers** | 65 |
| **Peak Hour** | 8:00 PM |
| **Staff on Duty** | 7 (full standard) |
| **Prep Window** | 10:00 AM – 4:30 PM |
| **Service Window** | 5:00 PM – 11:00 PM |
| **Menu Items Available** | 16 (2 items 86'd) |
| **Special Considerations** | Private party 7:00 PM (Table 12, 8 covers) |

---

# II. Kitchen Context Configuration

## II.A. Physical Layout Specification

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           COPPER BEECH KITCHEN                            │
│                         Saturday, April 15th                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────┐                                                     │
│   │   DRY STORAGE  │                                                     │
│   │    (8' × 10')  │                                                     │
│   │   Station D     │                                                     │
│   └────────┬────────┘                                                     │
│            │                                                                │
│   ┌────────┴────────┐           ┌────────────────────────────────────────┐│
│   │   WALK-IN       │           │           HOT LINE                     ││
│   │   REFRIGERATOR  │           │                                        ││
│   │    (8' × 10')   │           │   ┌─────────┐ ┌─────────┐ ┌─────────┐ ││
│   │   Station C     │           │   │  GRILL  │ │  SAUTÉ  │ │  FRYER  │ ││
│   └────────┬────────┘           │   │ Station │ │ Station │ │ Station │ ││
│            │                      │   │    A    │ │    B    │ │    C    │ ││
│   ┌────────┴────────┐           │   │(4 zones)│ │(6 burn) │ │(2 basket)│ ││
│   │   PREP STATION  │           │   └────┬────┘ └────┬────┘ └────┬────┘ ││
│   │    (10' × 6')   │           │        └──────────┴──────────┘        ││
│   │   Station E     │           │              │                       ││
│   └────────┬────────┘           │              ▼                       ││
│            │                      │        ┌─────────┐                    ││
│            │                      │        │  COMBI  │                    ││
│            │                      │        │  OVEN   │                    ││
│            │                      │        │ Station │                    ││
│            │                      │        │    F    │                    ││
│            │                      │        └────┬────┘                    ││
│            │                      └─────────────┼─────────────────────────┘│
│            │                                        │                      │
│            │                      ┌────────────────┴─────────────────┐    │
│            │                      │              THE PASS              │    │
│            │                      │           Station G               │    │
│            │                      └─────────────────────────────────┘    │
│            │                                   │                          │
│   ┌────────┴────────┐          ┌─────────────┴──────────────┐         │
│   │   COLD PREP     │          │      SERVICE AREA           │         │
│   │   STATION       │          │     (Server Pickup)         │         │
│   │   (6' × 5')    │          │                             │         │
│   │   Station H     │          └─────────────────────────────┘         │
│   └─────────────────┘                                                     │
│                                                                            │
│   ┌─────────────────┐          ┌────────────────────────────────────────┐│
│   │   DISH STATION  │          │          POT STATION                   ││
│   │    (8' × 6')   │          │           (6' × 4')                   ││
│   │   Station I     │          │          Station J                    ││
│   └─────────────────┘          └────────────────────────────────────────┘│
│                                                                            │
└─────────────────────────────────────────────────────────────────────────────┘

DIMENSIONS: 40' × 30' = 1,200 sq ft total (800 sq ft usable kitchen)
ZONES: Cold (walk-in, cold prep), Hot (hot line, combi), Service (pass), Support (dish, pot)
```

## II.B. Equipment Configuration for April 15th

| Station | Equipment | Capacity | Status | Notes |
|---------|-----------|----------|--------|-------|
| **A (Grill)** | Commercial Grill | 4 zones | OPERATIONAL | 15-min preheat required |
| **A (Grill)** | 4-Burner Range | 4 burners | OPERATIONAL | Backup for sauce work |
| **B (Sauté)** | 6-Burner Range | 6 burners | OPERATIONAL | Primary hot station |
| **C (Fry)** | Double Deep Fryer | 2 baskets | OPERATIONAL | Oil filtered AM |
| **F (Oven)** | Combi Oven | 2 racks | OPERATIONAL | Calibration verified |
| **H (Cold)** | Cold Well | 4 compartments | OPERATIONAL | Ice refreshed |
| **E (Prep)** | Reach-in Refrigerator | 2-door | OPERATIONAL | Stocked AM |
| **G (Pass)** | Heat Lamps | 8 plates | OPERATIONAL | Preheated 4:30 PM |

## II.C. Staff Configuration for April 15th

| Role | Name | Station Assignment | Special Notes |
|------|------|-------------------|---------------|
| **Chef de Cuisine** | Maria | Oversight / Expo Support | On premise all day |
| **Sous Chef** | James | Expo (Primary) | 2:00 PM – 11:30 PM |
| **Line Cook (Grill)** | David | Station A (Grill) | 3:00 PM – 11:00 PM |
| **Line Cook (Sauté)** | Chen | Station B (Sauté) | 3:00 PM – 11:00 PM |
| **Line Cook (Fry/Cold)** | Rosa | Station C/H (Fry/Cold) | 2:00 PM – 10:00 PM |
| **Prep Cook** | Michael | Station E (Prep) | 10:00 AM – 6:00 PM |
| **Dish/Utility** | Tony | Station I (Dish) | 4:00 PM – 11:00 PM |

**Coverage Backup Map:**
- Grill (David) → Backup by Chen, then James
- Sauté (Chen) → Backup by David, then James
- Fry/Cold (Rosa) → Backup by Michael, then James
- Expo (James) → Backup by Maria

---

# III. Menu Configuration for April 15th

## III.A. Available Menu Items

| Category | Item | Station | Difficulty | Expected Demand | Lead Time |
|----------|------|---------|------------|-----------------|-----------|
| **Appetizers** | | | | | |
| | Burrata Salad | H (Cold) | 1 | 12 | 15 min |
| | Roasted Beet Salad | H (Cold) | 2 | 8 | 20 min |
| | Fried Calamari | C (Fry) | 3 | 10 | 8 min |
| | Duck Confit Crostini | B (Sauté) | 3 | 6 | 10 min |
| **Entrées** | | | | | |
| | Grilled Ribeye (14 oz) | A (Grill) | 3 | 15 | 12 min |
| | Pan-Seared Salmon | B (Sauté) | 3 | 18 | 8 min |
| | Roasted Chicken | F (Combi) | 2 | 12 | 14 min |
| | **86'd: Braised Short Rib** | — | — | — | — |
| | Wild Mushroom Risotto | B (Sauté) | 4 | 10 | 18 min |
| | Grilled Vegetables | A (Grill) | 1 | 8 | 6 min |
| **86'd: Grilled Lamb Chop** | — | — | — | — |
| **Desserts** | | | | | |
| | Chocolate Torte | H (Cold) | 2 | 8 | 5 min |
| | Crème Brûlée | F (Combi) | 3 | 6 | 15 min |

## III.B. Special Considerations

**Private Party (Table 12):**
- 8 covers at 7:00 PM
- Pre-ordered menu: Ribeye (4), Salmon (2), Risotto (2)
- Modified timing required: All items must fire together
- Dedicated server assigned

**Allergen Table (Table 8):**
- 4 covers
- One guest with shellfish allergy
- Order: Salmon (modified), Vegetables (modified), no cross-contamination
- Double-check protocol required

---

# IV. Generated Prep Schedule

## Saturday, April 15th — Prep Schedule

**Prep Window:** 10:00 AM – 4:30 PM  
**Prep Cook:** Michael (with sous chef support as needed)  
**Supervision:** James (2:00 PM onward), Maria (as available)

### Phase 1: Long-Lead Items (10:00 AM – 1:00 PM)

| Time | Item | Quantity | Portion | Location | Station | Equipment | Completed |
|------|------|----------|---------|----------|---------|-----------|----------|
| 10:00 | Chicken stock | 2 gallons | — | Walk-in | E (Prep) | Combi (for aromatics) | ☐ |
| 10:30 | Demi-glace reduction | 1 quart | 2 oz portions | Reach-in | E (Prep) | 4-burner | ☐ |
| 11:00 | Risotto base | 3 portions | 6 oz | Walk-in | E (Prep) | 6-burner | ☐ |
| 11:30 | Mushroom duxelle | 8 portions | 1 oz | Walk-in | E (Prep) | Robot Coupe | ☐ |

### Phase 2: Standard Prep (1:00 PM – 3:30 PM)

| Time | Item | Quantity | Portion | Location | Station | Equipment | Completed |
|------|------|----------|---------|----------|---------|-----------|----------|
| 1:00 | Ribeye portions | 20 | 14 oz | Reach-in | E (Prep) | Scale | ☐ |
| 1:15 | Salmon portions | 24 | 6 oz | Reach-in | E (Prep) | Scale | ☐ |
| 1:30 | Herb butter | 32 portions | 1 tbsp | Reach-in | E (Prep) | Mixer | ☐ |
| 1:45 | Seasonal vegetables | 24 portions | 4 oz | Walk-in | E (Prep) | Cutting board | ☐ |
| 2:00 | Beet roasting | 12 beets | Halved | Walk-in | F (Combi) | Combi Oven | ☐ |
| 2:15 | Goat cheese preparation | 12 portions | 2 oz | Reach-in | E (Prep) | — | ☐ |
| 2:30 | Arugula, washed/spun | 24 portions | 2 oz | Cold well | H (Cold) | — | ☐ |
| 2:45 | Burrata plates | 16 portions | 1 ball | Cold well | H (Cold) | — | ☐ |
| 3:00 | Tomato concassé | 16 portions | 2 oz | Reach-in | E (Prep) | Cutting board | ☐ |
| 3:15 | Balsamic reduction | 1 pint | — | Reach-in | E (Prep) | 4-burner | ☐ |
| 3:30 | Calamari prep | 14 portions | 6 oz | Reach-in | E (Prep) | — | ☐ |
| 3:45 | Crostini toast | 16 slices | — | Reach-in | A (Grill) | Salamander | ☐ |

### Phase 3: Quick-Turn Prep (3:30 PM – 4:30 PM)

| Time | Item | Quantity | Portion | Location | Station | Equipment | Completed |
|------|------|----------|---------|----------|---------|-----------|----------|
| 3:30 | Risotto finishing portions | 12 | 6 oz | Walk-in | B (Sauté) | — | ☐ |
| 3:45 | Dessert plates | 14 portions | — | Cold well | H (Cold) | — | ☐ |
| 4:00 | Sauce cups (demi) | 24 cups | 2 oz | Station | A (Grill) | — | ☐ |
| 4:15 | Creme brulee (custard in) | 10 | — | F (Combi) | Combi Oven | ☐ |
| 4:25 | Final walk-in organization | — | — | Walk-in | E (Prep) | — | ☐ |
| 4:30 | PREP COMPLETE CHECKLIST | | | | | | | |

### Prep Complete Checklist

- [ ] All proteins portioned and in reach-in
- [ ] All vegetables prepped and in walk-in
- [ ] All sauces prepared and portioned
- [ ] Cold items in cold well with ice
- [ ] Station mise en place verified
- [ ] James notified: "Prep complete"
- [ ] Maria verifies final prep state

---

# V. Generated Station Configurations

## Saturday, April 15th — Station Setup Cards

### Station A: GRILL STATION

**Operator:** David  
**Backup:** Chen → James  
**Time:** 4:00 PM (setup begins)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     STATION A: GRILL STATION SETUP                          │
│                          Saturday, April 15th                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PRE-SERVICE SETUP (4:00 PM – 5:00 PM)                                     │
│  ═══════════════════════════════════                                       │
│                                                                             │
│  GRILL SETUP                                                               │
│  ├─── 4:00 ─── Pre-heat grill (15 minutes)                                │
│  ├─── 4:05 ─── Season grill surface                                        │
│  ├─── 4:15 ─── Verify temp (450°F target)                                 │
│  └─── 4:15 ─── Place clean cast iron plates                                │
│                                                                             │
│  MISE EN PLACE                                                             │
│  ├── Reach-in (Section 1):                                                 │
│  │   ├── Ribeye portions: 20 × 14 oz                                      │
│  │   └── Label with date, initials                                        │
│  │                                                                           │
│  ├── Reach-in (Section 2):                                                 │
│  │   ├── Seasonal vegetables: 24 portions                                  │
│  │   └── Label with date, initials                                        │
│  │                                                                           │
│  ├── Station Container:                                                     │
│  │   ├── Herb butter: 32 portions in 1/3 pan                               │
│  │   ├── Demi-glace: 24 sauce cups                                        │
│  │   ├── Maldon salt                                                       │
│  │   └── Black pepper (coarse)                                             │
│  │                                                                           │
│  └── Plate Warming:                                                         │
│      └── 12 dinner plates in drawer (150°F)                                 │
│                                                                             │
│  TOOLS CHECK                                                               │
│  ├── Spatula (long)                                                        │
│  ├── Tongs (2, different sizes)                                             │
│  ├── Fish spatula                                                          │
│  ├── Chef's knife                                                          │
│  ├── Cutting board (protein)                                                │
│  └── Instant-read thermometer                                              │
│                                                                             │
│  SERVICE PROTOCOL                                                          │
│  ══════════════════                                                        │
│                                                                             │
│  FIRING TIMES (relative to pickup call)                                     │
│  ├── Ribeye ──────────── Fire 12 minutes before                           │
│  ├── Vegetables ───────── Fire 6 minutes before                            │
│  ├── Chicken (Combi) ──── Notify F station at 15 min                      │
│  └── Salmon (if grill backup) ─ Fire 8 minutes before                     │
│                                                                             │
│  QUALITY CHECKPOINTS                                                       │
│  ├── Steak internal temp: 145°F (medium rare)                              │
│  ├── 2-minute rest before slicing                                          │
│  ├── Herb butter melted, pooled on steak                                   │
│  └── Vegetable char present, tender when pressed                           │
│                                                                             │
│  COMMUNICATION PROTOCOL                                                    │
│  ├── FIRE: "Ribeye [table], [modifications]"                              │
│  ├── STATUS: "Ribeye resting, [table]"                                     │
│  ├── UP: "Ribeye up, [table]"                                             │
│  └── SUPPORT: "Need backup on [item]"                                      │
│                                                                             │
│  SPECIAL INSTRUCTIONS                                                       │
│  ├── Table 12 (Private Party): Fire all ribeyes together                   │
│  │   └── 4 ribeyes at 7:48 PM (pickup 8:00 PM)                          │
│  └── Table 8 (Allergen): No grill cross-contamination                      │
│      └── Dedicated tongs, separate cutting board                            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Station B: SAUTÉ STATION

**Operator:** Chen  
**Backup:** David → James  
**Time:** 4:00 PM (setup begins)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     STATION B: SAUTÉ STATION SETUP                          │
│                          Saturday, April 15th                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PRE-SERVICE SETUP (4:00 PM – 5:00 PM)                                     │
│  ═══════════════════════════════════                                       │
│                                                                             │
│  BURNER SETUP                                                              │
│  ├── 4:00 ─── Turn on 6-burner range (all burners)                        │
│  ├── 4:05 ─── Place pans in position:                                     │
│  │          ├── Burners 1-2: Rondeau (large) for risotto                 │
│  │          ├── Burners 3-4: Large sauté pans (2)                         │
│  │          └── Burners 5-6: Medium sauté pans (2)                        │
│  └── 4:10 ─── Begin sauce work                                             │
│                                                                             │
│  MISE EN PLACE                                                             │
│  ├── Reach-in (Pull at 4:30):                                              │
│  │   ├── Salmon portions: 24 × 6 oz                                        │
│  │   ├── Risotto portions: 12 × 6 oz (pre-made base)                     │
│  │   └── Duxelle portions: 12 × 1 oz                                     │
│  │                                                                           │
│  ├── Station Shelf (above range):                                           │
│  │   ├── Olive oil (1 quart)                                              │
│  │   ├── Butter (1 lb, cold, cubed)                                       │
│  │   ├── White wine (1 bottle)                                             │
│  │   ├── Capers (4 oz)                                                     │
│  │   ├── Shallots (minced, 8 oz)                                          │
│  │   ├── Chicken stock (warm, in small pot)                                │
│  │   ├── Parmesan (grated, 8 oz)                                          │
│  │   └── Lemon (4, quartered)                                              │
│  │                                                                           │
│  ├── Cutting Board (finishing):                                             │
│  │   └── Gremolata (for short rib, if any)                                 │
│  │                                                                           │
│  └── Warming Drawer:                                                        │
│      └── Hold risotto at 150°F (max 30 min)                                │
│                                                                             │
│  TOOLS CHECK                                                               │
│  ├── Sauté pans (6 minimum)                                                │
│  ├── Rondeau (2, different sizes)                                            │
│  ├── Fish spatula                                                          │
│  ├── Spider strainer                                                        │
│  ├── Bench knife                                                          │
│  ├── Microplane (for parmesan)                                              │
│  └── Instant-read thermometer                                              │
│                                                                             │
│  SERVICE PROTOCOL                                                          │
│  ══════════════════                                                        │
│                                                                             │
│  FIRING TIMES (relative to pickup call)                                     │
│  ├── Risotto ──────────── Fire 18 minutes before                          │
│  │       └── Add stock gradually, stir constantly                           │
│  ├── Salmon ───────────── Fire 8 minutes before                             │
│  │       └── Score skin, start skin-side down                              │
│  ├── Duck Crostini ─────── Fire 10 minutes before                          │
│  │       └── Reheat confit, crisp skin                                     │
│  └── Vegetables (if backup) ─ Fire 5 minutes before                         │
│                                                                             │
│  QUALITY CHECKPOINTS                                                       │
│  ├── Salmon: 125°F internal, crispy skin, opaque flesh                     │
│  ├── Risotto: Creamy, al dente, proper seasoning                           │
│  │       └── "The wave test": should ripple when shaken                    │
│  └── Capers: Pan-fried until crispy                                        │
│                                                                             │
│  COMMUNICATION PROTOCOL                                                    │
│  ├── FIRE: "Risotto [table], [mods]"                                       │
│  ├── STATUS: "Risotto [table], 10 min"                                     │
│  ├── UP: "Salmon up, [table]"                                             │
│  └── SUPPORT: "Need pan" or "Need stock"                                   │
│                                                                             │
│  SPECIAL INSTRUCTIONS                                                       │
│  ├── Table 12 (Private Party): Risotto at 7:42 PM                           │
│  │   └── 2 portions, fire 18 min before (7:42 PM)                         │
│  └── Table 8 (Allergen): Salmon - NO capers (allergen)                     │
│      └── Substitute lemon butter sauce                                      │
│                                                                             │
│  RISOTTO SCHEDULE (during service)                                          │
│  ├── 5:30 ─── First risotto (if ordered)                                   │
│  ├── 6:00 ─── Check with James: project risotto needs                      │
│  ├── 6:30 ─── Project second wave                                          │
│  ├── 7:00 ─── Private party risotto firing window opens                     │
│  ├── 7:42 ─── FIRE: 2 risotto for Table 12                                 │
│  ├── 8:00 ─── Project peak risotto needs                                    │
│  └── Continuous ─── Monitor and adjust stock heat                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Station C/H: FRY & COLD STATION

**Operator:** Rosa  
**Backup:** Michael → James  
**Time:** 3:30 PM (cold setup), 4:30 PM (fry setup)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   STATION C/H: FRY & COLD SETUP                             │
│                          Saturday, April 15th                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  COLD SETUP (3:30 PM – 4:30 PM)                                             │
│  ════════════════════════════════                                           │
│                                                                             │
│  COLD WELL PREPARATION                                                     │
│  ├── 3:30 ─── Drain and refill with fresh ice                              │
│  ├── 3:35 ─── Temperature check: < 40°F                                    │
│  └── 3:35 ─── Verify drainage not clogged                                   │
│                                                                             │
│  WELL ORGANIZATION                                                          │
│  ├── Well 1: House salads (pre-plated base)                                 │
│  ├── Well 2: Dressings (4 squeeze bottles)                                  │
│  │       ├── balsamic
│  │       ├── herb vinaigrette
│  │       ├── lemon olive oil
│  │       └── blue cheese (separate)                                         │
│  ├── Well 3: Garnishes                                                      │
│  │       ├── microgreens
│  │       ├── shaved parmesan
│  │       ├── candied walnuts
│  │       └── heirloom tomatoes                                             │
│  └── Well 4: Cold appetizers & desserts                                     │
│          ├── burrata plates
│          └── dessert plates                                                 │
│                                                                             │
│  COLD MISE EN PLACE                                                         │
│  ├── 3:45 ─── Burrata: 16 portions, 1 ball each                            │
│  ├── 3:50 ─── Arugula: 24 portions, 2 oz, pre-tossed with oil            │
│  ├── 3:55 ─── Beets: 8 portions, sliced, with goat cheese                  │
│  ├── 4:00 ─── Dessert plates: 14, chilled                                   │
│  └── 4:15 ─── Final cold well check                                         │
│                                                                             │
│  FRY SETUP (4:30 PM)                                                        │
│  ═════════════════                                                         │
│                                                                             │
│  FRYER PREPARATION                                                          │
│  ├── 4:30 ─── Check oil level and quality                                   │
│  │          └── If dark or foamy: filter or change                          │
│  ├── 4:35 ─── Heat to 350°F (Basket 1 - general)                           │
│  ├── 4:40 ─── Heat to 375°F (Basket 2 - tempura)                            │
│  └── 4:45 ─── Verify temps stable                                           │
│                                                                             │
│  FRY MISE EN PLACE                                                          │
│  ├── 4:30 ─── Calamari: 14 portions, cleaned, floured                      │
│  │          └── Keep refrigerated until firing                              │
│  ├── 4:35 ─── Fries prep: pre-cut, portions ready                          │
│  ├── 4:40 ─── Seasoning station: sea salt, pepper, paprika                  │
│  └── 4:45 ─── Frying schedule posted                                       │
│                                                                             │
│  SERVICE PROTOCOL                                                           │
│  ══════════════════                                                        │
│                                                                             │
│  FIRING TIMES (relative to pickup call)                                     │
│  ├── Calamari ───────────── Fire 5 minutes before                          │
│  │       └── 350°F, 2 minutes, until golden                                │
│  ├── Fries (if ordered) ─── Fire 4 minutes before                          │
│  └── Cold apps ───────────── Fire on ticket (no advance)                    │
│      └── Burrata: plate immediately before service                          │
│                                                                             │
│  QUALITY CHECKPOINTS                                                       │
│  ├── Calamari: Golden color, not chewy                                       │
│  │       └── 2 minutes max in fryer                                        │
│  ├── Fries: Crisp exterior, fluffy interior                                 │
│  └── Cold items: < 40°F, fresh appearance                                  │
│                                                                             │
│  COMMUNICATION PROTOCOL                                                    │
│  ├── FIRE: "Calamari [table]"                                              │
│  ├── UP: "Calamari up, [table]"                                            │
│  ├── COLD: "Burrata up, [table]"                                           │
│  └── SUPPORT: "Need ice" or "Need backup fry"                               │
│                                                                             │
│  SPECIAL INSTRUCTIONS                                                       │
│  ├── Allergen Table (Table 8): Separate prep area                            │
│  │       └── No cross-contact with shellfish                                 │
│  └── Private Party (Table 12): No appetizers pre-ordered                     │
│      └── Standard firing only                                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Station F: COMBI OVEN STATION

**Operator:** Shared (Rosa coordinates)  
**Backup:** James → Maria  
**Time:** 1:00 PM (start), 4:00 PM (service prep)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     STATION F: COMBI OVEN SETUP                             │
│                          Saturday, April 15th                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PRE-SERVICE SETUP (1:00 PM – 5:00 PM)                                      │
│  ═══════════════════════════════                                            │
│                                                                             │
│  MORNING LOAD (1:00 PM – 2:30 PM)                                          │
│  ├── 1:00 ─── Preheat Combi: 350°F, Combi mode (steam + convection)         │
│  ├── 1:15 ─── Load beets: 12 whole beets, parchment-lined tray              │
│  │          └── Expected: 45-60 min at 350°F                              │
│  ├── 1:30 ─── Load chicken (10 portions):                                   │
│  │          └── 4:30 PM service ready                                      │
│  │                                                                           │
│  └── 2:15 ─── Beets complete? Check doneness (fork tender)                   │
│              └── If done: Remove, cool, store in walk-in                    │
│                                                                             │
│  AFTERNOON LOAD (4:00 PM – 5:00 PM)                                        │
│  ├── 4:00 ─── Crème brûlée custards (10)                                    │
│  │          └── 4:15 PM: Load, 325°F, Steam mode                           │
│  │          └── 4:45 PM: Check set (should jiggle slightly)                  │
│  │                                                                           │
│  ├── 4:30 ─── Pre-heat chicken: 400°F, Convection mode                    │
│  ├── 4:35 ─── Load 10 chicken portions                                      │
│  │          └── Expected: 25-30 min                                         │
│  └── 4:45 ─── Verify all loaded items                                       │
│                                                                             │
│  SERVICE PROTOCOL                                                          │
│  ══════════════════                                                        │
│                                                                             │
│  FIRING SCHEDULE                                                           │
│  ├── 5:30 ─── First chicken (if ordered)                                   │
│  ├── 6:00 ─── Check demand, pre-heat for second wave                       │
│  ├── 6:30 ─── Load second wave as needed                                    │
│  ├── 7:15 ─── Private party chicken (Table 12): No chicken ordered          │
│  │          └── Standard waves only                                         │
│  └── Continuous ─── Monitor custards for service                             │
│                                                                             │
│  HOLDING PROTOCOL                                                          │
│  ├── Chicken: Hold at 145°F in Combi (steam mode), max 30 min              │
│  │       └── After 30 min: Finish on stove or 86                           │
│  ├── Beets: Cool, portion, hold in walk-in                                 │
│  │       └── To station at service time                                     │
│  └── Custards: Refrigerate until service, torch before serving               │
│                                                                             │
│  COMMUNICATION PROTOCOL                                                    │
│  ├── LOADDED: "[Item] loaded, [time] ready"                               │
│  ├── READY: "Chicken ready, [qty]"                                         │
│  ├── PULL: "[Cook name] pulling [item]"                                    │
│  └── SUPPORT: "Need combi for [item]"                                      │
│                                                                             │
│  COMBI OVEN CAPACITY                                                        │
│  ├── Max simultaneous loads: 2 full sheet pans                              │
│  ├── Recovery time: 5 minutes between loads                                 │
│  └── Coordinate with James on timing                                        │
│                                                                             │
│  SPECIAL INSTRUCTIONS                                                       │
│  └── Private Party (Table 12): No chicken ordered                            │
│      └── Standard service only                                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Station G: EXPO/PASS

**Operator:** James (Primary), Maria (Support)  
**Time:** 4:30 PM (setup), 5:00 PM (service start)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     STATION G: EXPO/PASS SETUP                               │
│                          Saturday, April 15th                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  PRE-SERVICE SETUP (4:30 PM – 5:00 PM)                                      │
│  ═══════════════════════════════                                             │
│                                                                             │
│  PASS PREPARATION                                                           │
│  ├── 4:30 ─── Wipe down all surfaces with sanitizer                        │
│  ├── 4:30 ─── Turn on heat lamps (180°F)                                    │
│  ├── 4:35 ─── Verify all pickup shelves numbered (1-12)                     │
│  ├── 4:35 ─── Set up expo board:                                            │
│  │          ├── Marker (sharpie)                                            │
│  │          ├── Timer (master clock visible)                                 │
│  │          └── Pad for notes                                               │
│  └── 4:40 ─── Clear all tickets from previous service                      │
│                                                                             │
│  EQUIPMENT CHECK                                                            │
│  ├── Heat lamps: All 8 operational, 180°F                                   │
│  ├── Order rail: Clear, visible from all stations                           │
│  ├── Pickup shelves: Numbered, clean                                        │
│  └── All-day board: Cleared, ready                                          │
│                                                                             │
│  COMMUNICATION CENTER                                                        │
│  ├── 4:45 ─── Check in with all stations:                                  │
│  │          ├── "David, where are we?"                                      │
│  │          ├── "Chen, mise?"                                              │
│  │          ├── "Rosa, cold ready?"                                        │
│  │          └── "Michael, prep status?"                                    │
│  └── 4:50 ─── James to expo position, Maria available                       │
│                                                                             │
│  SERVICE PROTOCOL                                                            │
│  ══════════════════                                                         │
│                                                                             │
│  EXPO RESPONSIBILITIES                                                       │
│  ├── TIMING CONTROL                                                          │
│  │   ├── Call all tickets aloud: "[Table], [items], [mods]"              │
│  │   ├── Track all-day counts                                               │
