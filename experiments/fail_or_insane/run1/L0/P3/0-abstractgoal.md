# Daily Workflow Instance: The Copper Beech Kitchen

## Pass 3 — Concrete Workflow Instance

### A Complete Daily Workflow Specification for a Small Commercial Kitchen

---

# I. Kitchen Context Specification

## The Copper Beech Restaurant

**Profile**: A small farm-to-table restaurant in a mid-sized city, serving dinner 5 nights per week with 45 seats and an open kitchen concept.

**Service Hours**: 5:00 PM – 10:00 PM (last seating 9:00 PM)
**Average Cover Count**: 35-50 dinners on weeknights, 55-70 on weekends
**Average Ticket Time Target**: 14 minutes (appetizers), 18 minutes (entrées)

---

## II. Physical Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           THE COPPER BEECH KITCHEN                            │
│                              (Scale: 1" = 4')                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────┐                                                        │
│   │   DRY STORAGE  │                                                        │
│   │    (8' × 10')  │                                                        │
│   └────────┬────────┘                                                        │
│            │                                                                  │
│   ┌────────┴────────┐           ┌────────────────────────────────────────┐  │
│   │   WALK-IN       │           │           HOT LINE                    │  │
│   │   REFRIGERATOR  │           │                                        │  │
│   │    (8' × 10')   │           │   ┌─────────┐ ┌─────────┐ ┌─────────┐ │  │
│   │                 │           │   │  GRILL  │ │  SAUTÉ  │ │  FRYER  │ │  │
│   └────────┬────────┘           │   │  Station│ │  Station│ │  Station│ │  │
│            │                    │   │ (4 burn)│ │(6 burn) │ │(2 basket)│ │  │
│   ┌────────┴────────┐           │   └────┬────┘ └────┬────┘ └────┬────┘ │  │
│   │   PREP STATION  │           │        │          │          │        │  │
│   │    (10' × 6')   │           │        └──────────┴──────────┘        │  │
│   │  ┌───────────┐  │           │              │                        │  │
│   │  │  Reach-in │  │           │              ▼                        │  │
│   │  │  (2 door) │  │           │        ┌─────────┐                   │  │
│   │  └───────────┘  │           │        │ COMBI   │                   │  │
│   │                 │           │        │  OVEN   │                   │  │
│   └────────┬────────┘           │        │ (2 rack)│                   │  │
│            │                    │        └────┬────┘                   │  │
│            │                    └─────────────┼─────────────────────────┘  │
│            │                                     │                           │
│            │                    ┌────────────────┴─────────────────┐        │
│            │                    │              THE PASS           │        │
│            │                    │           (6' × 4')           │        │
│            │                    └────────────────────────────────┘        │
│            │                             │                                    │
│   ┌────────┴────────┐         ┌─────────┴─────────┐                       │
│   │   COLD PREP     │         │    SERVICE AREA    │                       │
│   │   STATION       │         │    (Server Pickup) │                       │
│   │   (6' × 5')     │         │                    │                       │
│   │  ┌───────────┐  │         └────────────────────┘                       │
│   │  │ Cold Well │  │                                                        │
│   │  └───────────┘  │                                                        │
│   └─────────────────┘                                                        │
│                                                                             │
│   ┌─────────────────┐         ┌────────────────────────────────────────┐   │
│   │   DISH STATION  │         │          POT STATION                  │   │
│   │    (8' × 6')    │         │           (6' × 4')                   │   │
│   └─────────────────┘         └────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

FLOW PATHS:
→→→ Raw material entry (delivery door, bottom)
↑↑↑ Prep to walk-in flow
⇢⇢⇢ Prep to line flow  
↑↑↑ Line to pass flow
→→→ Plated food to service flow
⇠⇠⇠ Return flow (dishes, equipment)
```

### Zone Classifications

| Zone | Location | Temperature | Primary Function |
|------|----------|-------------|------------------|
| **Cold Zone** | Walk-in, Reach-in, Cold Prep | 33-41°F | Storage, cold assembly |
| **Hot Zone** | Hot Line, Combi Oven area | Variable (150-500°F) | Active cooking |
| **Neutral Zone** | Prep Station, Pot Station | Ambient | Preparation, support |
| **Service Zone** | The Pass | Ambient + heat lamps | Quality check, handoff |
| **Support Zone** | Dry Storage, Dish Station | Ambient | Storage, cleanup |

---

## III. Equipment Inventory

### Cooking Equipment

| Equipment | Location | Capacity | Condition | Notes |
|-----------|----------|----------|-----------|-------|
| **6-Burner Range** | Sauté Station | 6 active burners | Good | Main heat source |
| **4-Burner Range** | Grill Station | 4 active burners + grill | Good | Shared flame |
| **Commercial Grill** | Grill Station | 24" × 24" | Good | Cast iron, requires 15-min preheat |
| **Double Deep Fryer** | Fry Station | 2 × 40-lb capacity | Good | Requires daily oil filter |
| **Combi Oven** | Hot Line (center) | 2 full-size sheet pans | Excellent | Steam + convection |
| **Salamander Broiler** | Above Grill | 24" × 18" | Good | Used for finishing, cheese melting |

### Preparation Equipment

| Equipment | Location | Capacity | Condition | Notes |
|-----------|----------|----------|-----------|-------|
| **Reach-in Refrigerator** | Prep Station | 2-door, pan-ready | Good | Line support |
| **Prep Tables** | Prep Station | 10 linear feet | Good | Stainless, clean |
| **Cutting Boards** | Prep Station | 6 color-coded | Good | Replace when grooved |
| **Robot Coupe** | Prep Station | Batch processor | Good | For purees, slicing |
| **Scale** | Prep Station | 50-lb capacity | Good | Legal for trade |

### Storage Equipment

| Equipment | Location | Capacity | Condition | Notes |
|-----------|----------|----------|-----------|-------|
| **Walk-in Refrigerator** | Back corner | 8' × 10' × 8' | Good | Main cold storage |
| **Dry Storage Shelving** | Dry Storage room | 80 square feet | Good | Labeled, FIFO enforced |
| **Freezer** | Dry Storage (attached) | 8' × 8' × 7' | Good | Long-term storage |

### Cleanup Equipment

| Equipment | Location | Capacity | Condition | Notes |
|-----------|----------|----------|-----------|-------|
| **Commercial Dishwasher** | Dish Station | 20 racks/hour | Good | Requires 180°F final rinse |
| **3-Compartment Sink** | Dish Station | Full-size | Good | Pot washing |
| **Pot Sink** | Pot Station | 2-compartment | Good | Large item cleaning |

---

## IV. Staff Profile

### Evening Shift (5 PM – 11 PM)

| Role | Name | Skills | Certifications | Cross-Training |
|------|------|--------|----------------|----------------|
| **Chef de Cuisine** | Maria | All stations, menu design, staff development | ServSafe Manager | — |
| **Sous Chef** | James | All stations, expo, expediting | ServSafe Manager | Prep, Grill |
| **Line Cook (Grill)** | David | Grill, Sauté (backup) | ServSafe | Sauté |
| **Line Cook (Sauté)** | Chen | Sauté, sauces, proteins | ServSafe | Grill |
| **Line Cook (Fry/Cold)** | Rosa | Fry, cold prep,garde manger | ServSafe | — |
| **Prep Cook** | Michael | All prep, batch cooking | ServSafe | Cold line |
| **Dishwasher/Utility** | Tony | Dish, pot washing, receiving | Basic food handler | — |

### Staffing Notes

- **Minimum Coverage**: 4 people (Chef, 2 line cooks, 1 support)
- **Standard Coverage**: 7 people (as listed above)
- **Peak Coverage**: 8 people (add server assistant during rush)
- **Cross-Training Map**:
  - James → Can cover any station
  - David → Can back up Sauté during slow periods
  - Chen → Can back up Grill during slow periods
  - Michael → Can assist cold line during service

---

## V. Menu Composition

### Current Menu (Spring Season)

#### Appetizers

| Item | Components | Primary Station | Equipment | Difficulty |
|------|------------|-----------------|-----------|------------|
| **Burrata Salad** | Fresh burrata, heirloom tomatoes, basil oil, balsamic | Cold | No cook | Low |
| **Roasted Beet Salad** | Beets, goat cheese, arugula, candied walnuts | Cold | Combi Oven | Low |
| **Fried Calamari** | Squid, spicy aioli, lemon | Fry | Deep Fryer | Medium |
| **Duck Confit Crostini** | Confit duck, pickled onions, arugula | Sauté/Cold | Range, no cook | Medium |
| **Soup du Jour** | Seasonal vegetable soup | Prep/Cold | Combi Oven | Low |

#### Entrées

| Item | Components | Primary Station | Equipment | Difficulty |
|------|------------|-----------------|-----------|------------|
| **Grilled Ribeye** | 14-oz prime ribeye, herb butter, seasonal vegetable | Grill | Grill, Range | Medium |
| **Pan-Seared Salmon** | Atlantic salmon, lemon caper sauce, asparagus | Sauté | Range | Medium |
| **Roasted Chicken** | Half chicken, natural jus, roasted root vegetables | Combi/Grill | Combi Oven, Grill | Low |
| **Braised Short Rib** | 12-hr braised beef, polenta, gremolata | Sauté | Range, Combi (reheat) | High |
| **Wild Mushroom Risotto** | Arborio rice, seasonal mushrooms, parmesan | Sauté | Range | High |
| **Grilled Vegetables** | Seasonal vegetables, chimichurri | Grill | Grill | Low |

#### Desserts

| Item | Components | Primary Station | Equipment | Difficulty |
|------|------------|-----------------|-----------|------------|
| **Chocolate Torte** | Flourless chocolate cake, raspberry coulis | Cold | Combi (reheat) | Low |
| **Crème Brûlée** | Vanilla custard, caramelized sugar | Cold | Combi Oven | Medium |
| **Seasonal Fruit Sorbet** | House-made sorbet, biscuit | Cold | No cook | Low |

### Demand Projections

| Day | Expected Covers | Peak Hour | Menu Complexity |
|-----|----------------|-----------|-----------------|
| Monday | 30-35 | 7:00 PM | Standard |
| Tuesday | 30-35 | 7:00 PM | Standard |
| Wednesday | 35-45 | 7:30 PM | Standard |
| Thursday | 40-50 | 7:30 PM | Moderate (+5 specials) |
| Friday | 55-65 | 7:00 PM, 8:00 PM | High |
| Saturday | 60-70 | 7:00 PM, 8:00 PM, 9:00 PM | High |

---

## VI. Station Configurations

### Station 1: Prep Station

**Location**: Northwest corner, adjacent to walk-in
**Primary Operator**: Prep Cook (Michael)
**Secondary Coverage**: Rosa, Sous Chef (James)

```
┌─────────────────────────────────────────────────────────────────┐
│                         PREP STATION                              │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                    REACH-IN REFRIGERATOR                  │  │
│   │   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐     │  │
│   │   │ Today's │ │ Sauces  │ │Proteins │ │ Produce │     │  │
│   │   │  Prep   │ │  &     │ │  &     │ │  &     │     │  │
│   │   │  Items  │ │Stocks   │ │Seafood  │ │  Herbs  │     │  │
│   │   └─────────┘ └─────────┘ └─────────┘ └─────────┘     │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                     PREP TABLE (10')                     │  │
│   │                                                          │  │
│   │   [CB] [CB] [CB] [CB] [CB] [CB]                        │  │
│   │   │Red│ │Grn│ │Yel│ │Blu│ │Wht│ │Brn│                  │  │
│   │   │Raw │ │Pro │ │Sta │ │All │ │Herbs│ │Cooked│          │  │
│   │   │Meat│ │duce│ │rch│ │ergen│ │bs│ │Veg│                 │  │
│   │                                                          │  │
│   │   ┌─────────┐                                           │  │
│   │   │ Robot   │   KNIFE ROLL:                              │  │
│   │   │ Coupe   │   • Chef's knife (10")                     │  │
│   │   │         │   • Paring knife (3.5")                    │  │
│   │   └─────────┘   • Serrated knife                         │  │
│   │                 • Filleting knife                        │  │
│   │                                                          │  │
│   │   SCALE ─────────── TRASH ─────────── COMPOST              │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│   FLOW: Walk-in → Reach-in → Prep Table → [Walk-in holding OR Line] │
└─────────────────────────────────────────────────────────────────┘

STATION CONFIGURATION:
├── MISE EN PLACE REQUIRED
│   ├── Cutting boards set up by type (color-coded)
│   ├── Containers labeled with date, item, initials
│   ├── Knife roll accessible
│   ├── Trash and compost containers accessible
│   └── Robot Coupe accessible with bowl installed
│
├── PRIMARY TASKS
│   ├── Vegetable prep (cutting, trimming, portioning)
│   ├── Protein prep (portioning, trimming, marinating)
│   ├── Sauce components (mother sauces, bases)
│   ├── Stock preparation
│   ├── Dough and batter preparation
│   └── Batch cooking (beans, grains, vegetables)
│
├── QUALITY CHECKPOINTS
│   ├── Portion sizes verified against standard
│   ├── Labeling complete (date, item, initials)
│   └── Temperature compliance (cold items < 40°F)
│
├── CLEANUP PROTOCOL
│   ├── Clean as you go (wipe surfaces between items)
│   ├── Color-coded boards washed immediately after use
│   └── Station cleared and sanitized before service
```

### Station 2: Grill Station

**Location**: Hot Line, left position
**Primary Operator**: Line Cook (David)
**Secondary Coverage**: Chen (Sauté backup), Sous Chef (James)

```
┌─────────────────────────────────────────────────────────────────┐
│                         GRILL STATION                             │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                    4-BURNER RANGE                        │  │
│   │   ┌────┐ ┌────┐ ┌────┐ ┌────┐                          │  │
│   │   │ B1 │ │ B2 │ │ B3 │ │ B4 │                          │  │
│   │   └────┘ └────┘ └────┘ └────┘                          │  │
│   │                                                          │  │
│   │   PRIMARY USE: Sauces, finishing, side dishes            │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                    COMMERCIAL GRILL                       │  │
│   │   ════════════════════════════════════                   │  │
│   │   ║                                           ║           │  │
│   │   ║           CAST IRON GRIDDLE              ║           │  │
│   │   ║            (24" × 24")                  ║           │  │
│   │   ║                                           ║           │  │
│   │   ════════════════════════════════════                   │  │
│   │                                                          │  │
│   │   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐      │  │
│   │   │ IRON #1 │ │ IRON #2 │ │ IRON #3 │ │ IRON #4 │      │  │
│   │   │ (steak) │ │(protein)│ │(veg)    │ │ (fish)  │      │  │
│   │   └─────────┘ └─────────┘ └─────────┘ └─────────┘      │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│   ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│   │ Salam-  │  │ HERB     │  │ SAUCE    │  │FINISHED │        │
│   │ ander    │  │ BUTTER   │  │ CUP      │  │  PLATE  │        │
│   │ BROILER  │  │ (melted) │  │ (4 qt)   │  │  SPACE  │        │
│   │          │  │          │  │          │  │         │        │
│   └─────────┘  └─────────┘  └─────────┘  └─────────┘        │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                     OVERHEAD RACK                          │  │
│   │   [Plates warm] [Sauces labeled] [Tools accessible]        │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│   FLOW: [From Walk-in] → [Grill] → [Rest/Sauce] → [Expo]       │
└─────────────────────────────────────────────────────────────────┘

STATION CONFIGURATION:
├── MISE EN PLACE REQUIRED
│   ├── Grill preheated (15 min before service)
│   ├── Cast iron plates in position and seasoned
│   ├── Salamander operational
│   ├── Herb butter prepared and in container
│   ├── Sauce cups filled (demi-glace, compound butter)
│   ├── Resting rack for proteins
│   ├── Spatulas, tongs, fish spatula, grill brush accessible
│   └── Plates warmed (in drawer or on pass)
│
├── PRIMARY TASKS
│   ├── Grilling proteins (ribeye, chicken, salmon)
│   ├── Grilling vegetables (seasonal, asparagus)
│   ├── Grilling fish (when not on sauté)
│   ├── Sauce finishing (compound butters, jus reductions)
│   ├── Salamander work (melting cheese, finishing)
│   └── Protein resting and slicing
│
├── QUALITY CHECKPOINTS
│   ├── Steak temperatures verified with thermometer
│   ├── Grill marks present and correct
│   ├── Proteins rested before slicing
│   └── Sauce consistency correct
│
├── TIMING COORDINATION
│   ├── Fire ribeye 12 min before pickup
│   ├── Fire chicken 14 min before pickup
│   ├── Fire salmon 8 min before pickup
│   └── Fire vegetables 6 min before pickup
```

### Station 3: Sauté Station

**Location**: Hot Line, center position
**Primary Operator**: Line Cook (Chen)
**Secondary Coverage**: David (Grill backup), Sous Chef (James)

```
┌─────────────────────────────────────────────────────────────────┐
│                        SAUTÉ STATION                              │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                    6-BURNER RANGE                         │  │
│   │   ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐            │  │
│   │   │ B1 │ │ B2 │ │ B3 │ │ B4 │ │ B5 │ │ B6 │            │  │
│   │   │L/R │ │L/R │ │Pan │ │Pan │ │Pan │ │Sau │            │  │
│   │   │    │ │    │ │1-2 │ │3-4 │ │5-6 │ │ces │            │  │
│   │   └────┘ └────┘ └────┘ └────┘ └────┘ └────┘            │  │
│   │                                                          │  │
│   │   L/R = Large rondeau    Pan = Sauteuse pan             │  │
│   │   Sau = Sauce work       All burners have standing area  │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                   PANTRY (6" from range)                 │  │
│   │   ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐          │  │
│   │   │ Small  │ │ Medium │ │ Large  │ │ Rondeau│          │  │
│   │   │ pans   │ │ pans   │ │ pans   │ │(tall)  │          │  │
│   │   │ 8-10"  │ │ 10-12" │ │ 12-14" │ │ 6-8 qt │          │  │
│   │   └────────┘ └────────┘ └────────┘ └────────┘          │  │
│   │                                                          │  │
│   │   PAN LADDERS: Stainless steel, accessible              │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│   ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│   │ WORKING │  │  FINISH │  │  HOLD    │  │ FINISHED│        │
│   │  SPACE  │  │  SPACE  │  │  SPACE  │  │  PLATE  │        │
│   │(cutting │  │(sauce   │  │(warming │  │  SPACE  │        │
│   │ board)  │  │ finishing│  │ drawer) │  │         │        │
│   └─────────┘  └─────────┘  └─────────┘  └─────────┘        │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                  ABOVE STATION SHELF                      │  │
│   │   [Oils] [Vinegars] [Flour] [Sugar] [Spices]            │  │
│   │   [Common aromatics] [Stock containers]                   │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│   FLOW: [From Walk-in/Reach-in] → [Sauté pans] → [Finish] → [Plate] │
└─────────────────────────────────────────────────────────────────┘

STATION CONFIGURATION:
├── MISE EN PLACE REQUIRED
│   ├── All pans cleaned, seasoned, accessible
│   ├── Pan ladders organized by size
│   ├── Stocks and mother sauces accessible
│   ├── Aromatics (mirepoix, garlic, shallots) prepped
│   ├── Oils and vinegars accessible
│   ├── Finishing salts and spices accessible
│   ├── Cutting board for finishing work
│   ├── Warming drawer at 150°F for hold
│   └── All pans at hand with equivalents accessible
│
├── PRIMARY TASKS
│   ├── Pan-searing proteins (salmon, scallops, duck)
│   ├── Sauce preparation and finishing (capers, cream, reductions)
│   ├── Risotto preparation (requires attention, timing)
│   ├── Short rib reheating and finishing
│   ├── Vegetable sautéing
│   └── Immediate plating coordination with expo
│
├── QUALITY CHECKPOINTS
│   ├── Pan temperature correct before adding protein
│   ├── Sauce season-to-taste at finish
│   ├── Protein internal temperature verified
│   └── Plate temperature correct
│
├── TIMING COORDINATION
│   ├── Fire risotto 18 min before pickup
│   ├── Fire short rib 12 min before pickup
│   ├── Fire salmon 8 min before pickup
│   └── Fire vegetables 5 min before pickup
│
├── SPECIAL CONSIDERATIONS
│   ├── RISOTTO: Requires constant stirring, add stock gradually
│   ├── SAUCES: Keep warm, do not boil, season at end
│   └── SHORT RIBS: Reheat gently, finish with gremolata
```

### Station 4: Fry/Cold Station

**Location**: Hot Line, right position (adjacent to Combi)
**Primary Operator**: Line Cook (Rosa)
**Secondary Coverage**: Michael (Prep backup), Sous Chef (James)

```
┌─────────────────────────────────────────────────────────────────┐
│                       FRY / COLD STATION                         │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                    DEEP FRYER                             │  │
│   │   ┌─────────────────────┐  ┌─────────────────────┐      │  │
│   │   │    BASKET #1       │  │    BASKET #2        │      │  │
│   │   │   [350°F oil]      │  │   [375°F oil]       │      │  │
│   │   │                    │  │                     │      │  │
│   │   │   FOR: Fries,      │  │   FOR: Calamari,    │      │  │
│   │   │        onion rings  │  │        tempura      │      │  │
│   │   └─────────────────────┘  └─────────────────────┘      │  │
│   │                                                          │  │
│   │   OIL QUALITY CHECK: Dark = filter, Foam = change       │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                     COLD WELL                              │  │
│   │   ┌───────┐ ┌───────┐ ┌───────┐ ┌───────┐               │  │
│   │   │ WELL 1│ │ WELL 2│ │ WELL 3│ │ WELL 4│               │  │
│   │   │Salads │ │Dressgs│ │Garnish│ │Cold   │               │  │
│   │   │       │ │       │ │       │ │Apps   │               │  │
│   │   │ 38°F  │ │ 38°F  │ │ 38°F  │ │ 38°F  │               │  │
│   │   └───────┘ └───────┘ └───────┘ └───────┘               │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                    COLD PREP SURFACE                       │  │
│   │   ┌─────────────────────────────────────────────────┐   │  │
│   │   │  REFRIGERATED PREP TABLE (optional)             │   │  │
│   │   │  OR Marble board for chocolate tempering        │   │  │
│   │   └─────────────────────────────────────────────────┘   │  │
│   │                                                          │  │
│   │   ┌─────────┐  ┌─────────┐  ┌─────────┐                │  │
│   │   │ PLATING │  │  FINISH │  │ FINISHED│                │  │
│   │   │  SPACE  │  │  SPACE  │  │  PLATE  │                │  │
│   │   │(salads) │  │(garnish)│  │  SPACE  │                │  │
│   │   └─────────┘  └─────────┘  └─────────┘                │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                   COMBI OVEN ACCESS                        │  │
│   │   Rosa is responsible for loading/unloading combi          │  │
│   │   during service when line is busy                         │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│   FLOW: [Cold: Walk-in] → [Cold Well] → [Plate] → [Expo]       │
│   FLOW: [Hot: Walk-in] → [Fryer] → [Drain] → [Plate] → [Expo]  │
└─────────────────────────────────────────────────────────────────┘

STATION CONFIGURATION:
├── MISE EN PLACE REQUIRED (COLD)
│   ├── Cold well filled with ice
│   ├── Salads washed, spun, ready (4 types rotating)
│   ├── Dressings accessible in squeeze bottles
│   ├── Garnishes prepared (microgreens, herbs, etc.)
│   ├── Cheese shaved (if needed)
│   ├── Bread for crostini (grilled)
│   └── Allergen-free options accessible
│
├── MISE EN PLACE REQUIRED (FRY)
│   ├── Fryer oil at correct temperature
│   ├── Basket correctly positioned
│   ├── Frying schedule (battered items together)
│   ├── Salt and seasoning accessible
│   ├── Drain rack and paper towels accessible
│   └── Fry thermometer calibrated
│
├── PRIMARY TASKS
│   ├── Frying appetizers (calamari, fries, tempura)
│   ├── Cold appetizer plating (salads, tartare)
│   ├── Garde manger items (cold appetizers, canapés)
│   ├── Dessert plating support
│   ├── Combi oven loading/unloading coordination
│   └── Ice supply maintenance
│
├── QUALITY CHECKPOINTS
│   ├── Oil temperature correct before frying
│   ├── Fried items golden and crispy
│   ├── Cold items cold and fresh
│   └── Allergens verified before plating
│
├── TIMING COORDINATION
│   ├── Fire fried appetizers 4-5 min before pickup
│   ├── Fire cold items on ticket (no advance)
│   └── Fire desserts 3 min before pickup
```

### Station 5: Expo/Pass

**Location**: Center of kitchen, facing service
**Primary Operator**: Sous Chef (James) + Chef de Cuisine (Maria)
**Secondary Coverage**: Any available line cook

```
┌─────────────────────────────────────────────────────────────────┐
│                           THE PASS                               │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                    HEAT LAMPS                             │  │
│   │   ════════════════════════════════════                    │  │
│   │   ║  [Plate 1] [Plate 2] [Plate 3] [Plate 4]  ║      │  │
│   │   ║  [Plate 5] [Plate 6] [Plate 7] [Plate 8]  ║      │  │
│   │   ════════════════════════════════════                    │  │
│   │                                                          │  │
│   │   TEMP: 180°F when operational                           │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                      EXPO TABLE                            │  │
│   │                                                          │  │
│   │   ┌─────────────────────────────────────────────────┐   │  │
│   │   │              ORDER RAIL                          │   │  │
│   │   │   [Ticket] [Ticket] [Ticket] [Ticket]         │   │  │
│   │   │    Table 4   Table 7   Table 2   Table 9       │   │  │
│   │   │     7:42      7:45      7:46      7:48         │   │  │
│   │   └─────────────────────────────────────────────────┘   │  │
│   │                                                          │  │
│   │   ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐      │  │
│   │   │ TABLET  │ │  TIMER  │ │ ALL DAY │ │ RUBBER  │      │  │
│   │   │(Expo    │ │ (Master │ │ BOARD   │ │ MATTING │      │  │
│   │   │ notes)  │ │ clocks) │ │         │ │         │      │  │
│   │   └─────────┘ └─────────┘ └─────────┘ └─────────┘      │  │
│   │                                                          │  │
│   │   ┌─────────────────────────────────────────────────┐   │  │
│   │   │  FINISHED PLATES (waiting for expo check)       │   │  │
│   │   │  [  ] [  ] [  ] [  ] [  ] [  ] [  ] [  ]      │   │  │
│   │   └─────────────────────────────────────────────────┘   │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│   ┌──────────────────────────────────────────────────────────┐  │
│   │                   SERVER PICKUP AREA                      │  │
│   │                                                          │  │
│   │   ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐    │  │
│   │   │ T1  │ │ T2  │ │ T3  │ │ T4  │ │ T5  │ │ T6  │    │  │
│   │   │     │ │     │ │     │ │     │ │     │ │     │    │  │
│   │   │ UP  │ │ WAIT │ │ UP  │ │ WAIT │ │ UP  │ │ WAIT │    │  │
│   │   └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘    │  │
│   │                                                          │  │
│   │   "T[table#] UP!" called when plate on shelf           │  │
│   └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│   FLOW: [All Stations] → [Expo Check] → [Heat Lamp] → [Server Pickup] │
└─────────────────────────────────────────────────────────────────┘

EXPO CONFIGURATION:
├── MISE EN PLACE REQUIRED
│   ├── All timers set and verified
│   ├── Expo tablet charged and functional
│   ├── Order rail clear and organized
│   ├── Heat lamps preheated
│   ├── Rubber matting clean
│   ├── Pickup shelves numbered
│   └── Sharpie for marking tickets
│
├── PRIMARY FUNCTIONS
│   ├── **TIMING CONTROL**: Ensure all items for a table fire together
│   ├── **QUALITY VERIFICATION**: Check every plate before service
│   ├── **ORDER COORDINATION**: