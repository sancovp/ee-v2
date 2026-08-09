# Topology: The Copper Beech Kitchen Workflow System

## Pass 3 — Concrete Instance Network

### Specific Data Flows, Connections, and Integration Points

---

# I. Introduction: The Concrete Topology

## Purpose of This Document

While the previous documents established the *structure* of the Copper Beech Kitchen workflow system—its entities, configurations, and specifications—this document reveals the *topology*: the specific network of connections through which the system operates. It answers the question: **How do the components connect, and what data flows between them?**

The topology is the **living nervous system** of the workflow—the explicit pathways through which information moves, decisions propagate, and coordination occurs. Where the systems design showed what components exist, the topology shows how they relate.

## The Copper Beech Topology at a Glance

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                    THE COPPER BEECH KITCHEN WORKFLOW TOPOLOGY                       │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│    ┌─────────────────────────────────────────────────────────────────────────┐     │
│    │                     INPUT BOUNDARY                                         │     │
│    │                                                                          │     │
│    │   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐      │     │
│    │   │ Kitchen  │    │Equipment │    │  Staff   │    │  Menu    │      │     │
│    │   │ Layout   │    │Inventory │    │ Schedule │    │   &      │      │     │
│    │   │ (Visual) │    │ (Table)  │    │ (Shift)  │    │ Recipes  │      │     │
│    │   └────┬─────┘    └────┬─────┘    └────┬─────┘    └────┬─────┘      │     │
│    │         └───────────────┴───────────────┴───────────────┘              │     │
│    └─────────────────────────────────┬───────────────────────────────────────┘     │
│                                      │                                              │
│                                      ▼                                              │
│    ┌─────────────────────────────────────────────────────────────────────────┐     │
│    │                    KITCHEN CONTEXT REPOSITORY                             │     │
│    │                                                                          │     │
│    │   ┌──────────────────────────────────────────────────────────────┐      │     │
│    │   │              Context Database (PostgreSQL)                      │      │     │
│    │   │   • Physical Layout Graph                                     │      │     │
│    │   │   • Equipment Network                                          │      │     │
│    │   │   • Staff Profiles                                             │      │     │
│    │   │   • Menu & Recipe Library                                       │      │     │
│    │   └──────────────────────────────────────────────────────────────┘      │     │
│    └─────────────────────────────────┬───────────────────────────────────────┘     │
│                                      │                                              │
│                                      ▼                                              │
│    ┌─────────────────────────────────────────────────────────────────────────┐     │
│    │                    WORKFLOW GENERATION ENGINE                              │     │
│    │                                                                          │     │
│    │   ┌──────────────────────────────────────────────────────────────┐      │     │
│    │   │              Constraint Extraction Layer                      │      │     │
│    │   │   • Spatial Constraints    • Equipment Constraints          │      │     │
│    │   │   • Temporal Constraints   • Human Constraints             │      │     │
│    │   │   • Safety Constraints                                      │      │     │
│    │   └──────────────────────────────────────────────────────────────┘      │     │
│    │                              │                                         │     │
│    │                              ▼                                         │     │
│    │   ┌──────────────────────────────────────────────────────────────┐      │     │
│    │   │              Dependency Graph Builder                        │      │     │
│    │   │   • Recipe Dependencies     • Equipment Dependencies       │      │     │
│    │   │   • Timing Dependencies     • Skill Dependencies          │      │     │
│    │   └──────────────────────────────────────────────────────────────┘      │     │
│    │                              │                                         │     │
│    │                              ▼                                         │     │
│    │   ┌──────────────────────────────────────────────────────────────┐      │     │
│    │   │              Schedule & Configurator                        │      │     │
│    │   │   • Prep Schedule Generator                                │      │     │
│    │   │   • Station Configurator                                    │      │     │
│    │   │   • Role Assigner                                          │      │     │
│    │   └──────────────────────────────────────────────────────────────┘      │     │
│    │                              │                                         │     │
│    │                              ▼                                         │     │
│    │   ┌──────────────────────────────────────────────────────────────┐      │     │
│    │   │              Validation Suite                                │      │     │
│    │   │   • Hard Constraint Validator                                │      │     │
│    │   │   • Timing Feasibility Checker                              │      │     │
│    │   │   • Safety Compliance Verifier                              │      │     │
│    │   └──────────────────────────────────────────────────────────────┘      │     │
│    └─────────────────────────────────┬───────────────────────────────────────┘     │
│                                      │                                              │
│                                      ▼                                              │
│    ┌─────────────────────────────────────────────────────────────────────────┐     │
│    │                    OUTPUT BOUNDARY                                        │     │
│    │                                                                          │     │
│    │   ┌──────────────────────────────────────────────────────────────┐      │     │
│    │   │              Generated Workflow Instance                       │      │     │
│    │   │   • Daily Prep Schedule                                       │      │     │
│    │   │   • Station Configuration Cards                               │      │     │
│    │   │   • Timeline Visualization                                    │      │     │
│    │   │   • Communication Protocols                                   │      │     │
│    │   └──────────────────────────────────────────────────────────────┘      │     │
│    │                                                                          │     │
│    │   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐                │     │
│    │   │   Chef's    │    │   Kitchen   │    │   Printed  │                │     │
│    │   │ Dashboard   │    │   Display   │    │   Station  │                │     │
│    │   │  (Desktop)  │    │  Terminal   │    │   Cards    │                │     │
│    │   └─────────────┘    └─────────────┘    └─────────────┘                │     │
│    └─────────────────────────────────────────────────────────────────────────┘     │
│                                                                                     │
│    ════════════════════════════════════════════════════════════════════════════════    │
│                                                                                     │
│    ┌─────────────────────────────────────────────────────────────────────────┐     │
│    │                    FEEDBACK & LEARNING LOOP                                │     │
│    │                                                                          │     │
│    │   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐                │     │
│    │   │  Execution │    │  Outcome   │    │  Pattern    │                │     │
│    │   │  Observer  │───►│  Tracker   │───►│ Recognizer  │                │     │
│    │   └─────────────┘    └──────┬──────┘  └──────┬──────┘                │     │
│    │                               │                 │                        │     │
│    │                               ▼                 ▼                        │     │
│    │                    ┌────────────────────────────────┐                  │     │
│    │                    │     Knowledge Accumulator      │                  │     │
│    │                    │  • Timing Adjustments         │                  │     │
│    │                    │  • Constraint Refinements     │                  │     │
│    │                    │  • Pattern Libraries          │                  │     │
│    │                    └────────────────────────────────┘                  │     │
│    │                               │                                         │     │
│    │                               │ Feedback Loop                           │     │
│    └───────────────────────────────┼─────────────────────────────────────────┘     │
│                                    │                                              │
│                                    └──────────────────────────────────────────     │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

---

# II. The Physical Network Topology

## II.A. Kitchen Zone Connections

The Copper Beech Kitchen is organized into five interconnected zones, each with specific connections to others:

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           KITCHEN ZONE NETWORK                                      │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│                              ┌─────────────────┐                                    │
│                              │   DRY STORAGE   │                                    │
│                              │    (Back)       │                                    │
│                              └────────┬────────┘                                    │
│                                       │                                              │
│                                       │ Dry goods flow                               │
│                                       ▼                                              │
│    ┌─────────────────────────────────────────────────────────────────────┐         │
│    │                        COLD ZONE                                    │         │
│    │  ┌─────────────────┐              ┌─────────────────┐               │         │
│    │  │   WALK-IN      │◄───────────►│   PREP STATION  │               │         │
│    │  │   REFRIGERATOR │  Protein &   │   (Adjacent)    │               │         │
│    │  │    (8'×10')    │  Produce     └────────┬────────┘               │         │
│    │  └────────┬────────┘  retrieval           │                      │         │
│    │           │                                 │                      │         │
│    │           │ Cold chain                      │ Prep → Line          │         │
│    │           │ preservation                    │ flow                  │         │
│    │           ▼                                 ▼                      │         │
│    │  ┌─────────────────┐              ┌─────────────────┐               │         │
│    │  │   COLD PREP    │◄─────────────│   HOT LINE      │               │         │
│    │  │   STATION      │   Finished   │                 │               │         │
│    │  │   (6'×5')      │   components  │  ┌───────────┐ │               │         │
│    │  └────────┬────────┘   return     │  │   EXPO    │ │               │         │
│    │           │                    │  └───────────┘ │               │         │
│    │           │                    │                 │               │         │
│    │           │                    └────────┬────────┘               │         │
│    │           │                             │                         │         │
│    │           │                             │                         │         │
│    │           │                    ┌────────┴────────┐                │         │
│    │           │                    │   SERVICE ZONE  │                │         │
│    │           │                    │   (The Pass)     │                │         │
│    │           │                    └────────┬────────┘                │         │
│    │           │                             │                          │         │
│    │           │                             │ Plate flow               │         │
│    │           │                             ▼                          │         │
│    │           │                   ┌─────────────────┐                  │         │
│    └───────────┼──────────────────►│   SERVER AREA   │                  │         │
│                │                   │   (Pickup)       │                  │         │
│                │                   └─────────────────┘                  │         │
│                │                                                       │         │
│    ┌──────────┴───────────────────────────────────────────────────────┐│         │
│    │                        SUPPORT ZONE                             ││         │
│    │                                                                      ││         │
│    │   ┌─────────────────┐              ┌─────────────────┐               ││         │
│    │   │   DISH STATION │◄───────────│   POT STATION   │               ││         │
│    │   │    (8'×6')    │   Return    │    (6'×4')    │               ││         │
│    │   └─────────────────┘   flow      └─────────────────┘               ││         │
│    │                                                                      ││         │
│    └──────────────────────────────────────────────────────────────────────┘         │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### Zone Connection Matrix

| From Zone | To Zone | Connection Type | Primary Flow | Distance |
|-----------|---------|-----------------|--------------|----------|
| **Dry Storage** | Prep Station | Physical doorway | Dry ingredients | 15 ft |
| **Walk-in** | Prep Station | Adjacent (shared wall) | Proteins, dairy, produce | 2 ft |
| **Walk-in** | Cold Prep | Adjacent (shared wall) | Ready-to-eat items | 2 ft |
| **Prep Station** | Hot Line | Open flow path | Prepped components | 8 ft |
| **Cold Prep** | Hot Line | Open flow path | Cold items, salads | 12 ft |
| **Hot Line** | Expo/Pass | Direct adjacency | Finished plates | 3 ft |
| **Expo/Pass** | Server Area | Direct adjacency | Plated food | 4 ft |
| **Hot Line** | Dish Station | Through pot station | Dirty equipment | 20 ft |
| **Pot Station** | Dish Station | Adjacent | Soiled pots | 6 ft |
| **Dish Station** | Prep Station | Return path | Clean equipment | 25 ft |

### Critical Path Identification

The most time-sensitive connection in the Copper Beech topology is:

```
WALK-IN ──────► PREP STATION ──────► HOT LINE ──────► EXPO ──────► SERVICE
   │                │                  │                │              │
   │                │                  │                │              │
   0 ft         2 ft              8 ft            3 ft           4 ft
   │                │                  │                │              │
   └────────────────┴──────────────────┴────────────────┴──────────────┘
                                    │
                    Total critical path: 17 feet
                    Maximum acceptable transit time: 45 seconds
```

---

## II.B. Equipment Network Topology

The Copper Beech equipment forms a dependency network where shared utilities create critical connections:

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                         EQUIPMENT DEPENDENCY NETWORK                                │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│                         ┌─────────────────────┐                                   │
│                         │   GAS SUPPLY MAIN   │                                   │
│                         │   (Utility Entry)   │                                   │
│                         └──────────┬──────────┘                                   │
│                                    │                                               │
│               ┌────────────────────┼────────────────────┐                           │
│               │                    │                    │                           │
│               ▼                    ▼                    ▼                           │
│    ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐              │
│    │   6-BURNER      │  │   4-BURNER      │  │  COMMERCIAL     │              │
│    │   RANGE         │  │   RANGE         │  │  GRILL          │              │
│    │   (Sauté)       │  │   (Grill)       │  │                 │              │
│    │   150,000 BTU   │  │   80,000 BTU    │  │  60,000 BTU     │              │
│    └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘              │
│             │                       │                       │                       │
│             │                       │                       │                       │
│             └───────────────────────┼───────────────────────┘                       │
│                                     │                                               │
│                                     ▼                                               │
│                         ┌─────────────────────┐                                   │
│                         │   ELECTRICAL PANEL  │                                   │
│                         │   (Shared Circuit)  │                                   │
│                         └──────────┬──────────┘                                   │
│                                    │                                               │
│               ┌────────────────────┼────────────────────┐                           │
│               │                    │                    │                           │
│               ▼                    ▼                    ▼                           │
│    ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐              │
│    │   COMBI OVEN      │  │  DOUBLE FRYER   │  │   DISHMACHINE    │              │
│    │   (Steam+Conv)    │  │                 │  │                 │              │
│    │   40,000 BTU     │  │   24,000 BTU    │  │   60 Amp         │              │
│    │   480V/3Phase    │  │   240V          │  │   240V           │              │
│    └──────────────────┘  └──────────────────┘  └──────────────────┘              │
│                                                                                     │
│    ┌─────────────────────────────────────────────────────────────────────────┐     │
│    │                      WATER & DRAIN NETWORK                              │     │
│    │                                                                          │     │
│    │   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐        │     │
│    │   │Walk-in   │    │  Prep    │    │  Dish    │    │   Pot    │        │     │
│    │   │Condensate│───►│  Sink    │───►│ Machine  │───►│  Sink    │        │     │
│    │   │Drain     │    │(Handwash)│    │          │    │          │        │     │
│    │   └──────────┘    └──────────┘    └──────────┘    └──────────┘        │     │
│    │                                                                          │     │
│    └─────────────────────────────────────────────────────────────────────────┘     │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### Equipment Dependency Critical Points

| Equipment | Dependencies | Failure Impact | Backup Strategy |
|-----------|--------------|----------------|-----------------|
| **6-Burner Range** | Gas, Exhaust | Complete sauté shutdown | 4-burner backup for simple items |
| **Commercial Grill** | Gas, Exhaust | No grilled proteins | Combi oven for roasting |
| **Combi Oven** | Gas, Electric, Water, Drain | No roasted/reheated items | Prep as finish in pans |
| **Double Fryer** | Electric, Grease trap | No fried appetizers | Combi oven for some items |
| **Dishmachine** | Hot water, Electric | Severe slowdown | 3-compartment sink backup |

---

# III. The Data Flow Topology

## III.A. Daily Workflow Generation Data Flow

The generation of each day's workflow follows a specific data flow path:

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                    DAILY WORKFLOW GENERATION DATA FLOW                             │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  DAY BEFORE SERVICE                                                                │
│  ══════════════════                                                                │
│                                                                                     │
│  ┌─────────────────┐                                                                │
│  │ 1. DEMAND      │                                                                │
│  │    FORECAST    │                                                                │
│  │    INPUT       │                                                                │
│  │                │                                                                │
│  │ • Expected     │                                                                │
│  │   covers       │                                                                │
│  │ • Day of week  │                                                                │
│  │ • Special      │                                                                │
│  │   events       │                                                                │
│  └────────┬────────┘                                                                │
│           │                                                                          │
│           ▼                                                                          │
│  ┌─────────────────┐                                                                │
│  │ 2. MENU        │                                                                │
│  │    SELECTION    │                                                                │
│  │    INPUT       │                                                                │
│  │                │                                                                │
│  │ • Items for    │                                                                │
│  │   tomorrow     │                                                                │
│  │ • 86'd items   │                                                                │
│  │ • Specials     │                                                                │
│  └────────┬────────┘                                                                │
│           │                                                                          │
│           ▼                                                                          │
│  ┌─────────────────┐                                                                │
│  │ 3. STAFF        │                                                                │
│  │    AVAILABILITY │                                                                │
│  │    INPUT        │                                                                │
│  │                │                                                                │
│  │ • Who's working │                                                                │
│  │ • Assignments   │                                                                │
│  │ • Breaks        │                                                                │
│  └────────┬────────┘                                                                │
│           │                                                                          │
│           ▼                                                                          │
│  ┌─────────────────────────────────────────────────────────────────────────┐        │
│  │                    GENERATION ENGINE                                       │        │
│  │  ┌─────────────────────────────────────────────────────────────────┐    │        │
│  │  │ 4. CONSTRAINT EXTRACTION                                         │    │        │
│  │  │                                                                  │    │        │
│  │  │ Input: Context DB ─────► Constraint Network                     │    │        │
│  │  │    │                    │                                        │    │        │
│  │  │    │                    ├──► Physical Constraints                 │    │        │
│  │  │    │                    ├──► Equipment Constraints                │    │        │
│  │  │    │                    ├──► Temporal Constraints                 │    │        │
│  │  │    │                    ├──► Human Constraints                    │    │        │
│  │  │    │                    └──► Safety Constraints                  │    │        │
│  │  └─────────────────────────────────────────────────────────────────┘    │        │
│  │                              │                                              │        │
│  │                              ▼                                              │        │
│  │  ┌─────────────────────────────────────────────────────────────────┐    │        │
│  │  │ 5. DEPENDENCY GRAPH BUILDING                                     │    │        │
│  │  │                                                                  │    │        │
│  │  │ Input: Menu + Constraints ──► Dependency Graph                   │    │        │
│  │  │    │                    │                                        │    │        │
│  │  │    │                    ├──► Recipe Step Dependencies             │    │        │
│  │  │    │                    ├──► Equipment Dependencies               │    │        │
│  │  │    │                    ├──► Timing Dependencies                 │    │        │
│  │  │    │                    └──► Critical Path Analysis              │    │        │
│  │  └─────────────────────────────────────────────────────────────────┘    │        │
│  │                              │                                              │        │
│  │                              ▼                                              │        │
│  │  ┌─────────────────────────────────────────────────────────────────┐    │        │
│  │  │ 6. SCHEDULE GENERATION                                          │    │        │
│  │  │                                                                  │    │        │
│  │  │ Input: Dependencies + Staff ──► Daily Schedule                 │    │        │
│  │  │    │                    │                                        │    │        │
│  │  │    │                    ├──► Prep Schedule (by time)            │    │        │
│  │  │    │                    ├──► Prep Schedule (by person)          │    │        │
│  │  │    │                    ├──► Station Configurations              │    │        │
│  │  │    │                    └──► Role Assignments                    │    │        │
│  │  └─────────────────────────────────────────────────────────────────┘    │        │
│  │                              │                                              │        │
│  │                              ▼                                              │        │
│  │  ┌─────────────────────────────────────────────────────────────────┐    │        │
│  │  │ 7. VALIDATION                                                   │    │        │
│  │  │                                                                  │    │        │
│  │  │ Input: Schedule ──► Validation Result                            │    │        │
│  │  │    │                    │                                        │    │        │
│  │  │    │                    ├──► Hard Constraint Check                │    │        │
│  │  │    │                    ├──► Timing Feasibility                   │    │        │
│  │  │    │                    ├──► Resource Conflicts                   │    │        │
│  │  │    │                    └──► Safety Compliance                   │    │        │
│  │  │                                                                  │    │        │
│  │  │           ┌─────────────────────────────────┐                    │    │        │
│  │  │           │ IF VALIDATION FAILS            │                    │    │        │
│  │  │           │    │                            │                    │    │        │
│  │  │           │    └──► Return to Step 6      │                    │    │        │
│  │  │           │         with adjustments        │                    │    │        │
│  │  │           └─────────────────────────────────┘                    │    │        │
│  │  └─────────────────────────────────────────────────────────────────┘    │        │
│  └─────────────────────────────────┬───────────────────────────────────────┘        │
│                                    │                                              │
│                                    ▼                                              │
│  ┌─────────────────────────────────────────────────────────────────────────┐        │
│  │                    OUTPUT GENERATION                                      │        │
│  │                                                                          │        │
│  │   ┌────────────────────────────────────────────────────────────────┐   │        │
│  │   │ 8. WORKFLOW INSTANCE OUTPUT                                      │   │        │
│  │   │                                                                  │   │        │
│  │   │ • Prep Schedule Document (by time)                               │   │        │
│  │   │ • Prep Schedule Document (by station)                            │   │        │
│  │   │ • Station Configuration Cards                                   │   │        │
│  │   │ • Timeline Visualization                                        │   │        │
│  │   │ • Communication Protocol Summary                                 │   │        │
│  │   │ • All-Day Projections                                            │   │        │
│  │   └────────────────────────────────────────────────────────────────┘   │        │
│  │                                                                          │        │
│  └─────────────────────────────────────────────────────────────────────────┘        │
│                                                                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

## III.B. Real-Time Execution Data Flow

During service, data flows through the kitchen in a specific pattern:

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                         SERVICE DATA FLOW                                           │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                     │
│  EXTERNAL SYSTEMS                                                                  │
│  ═════════════════                                                                  │
│                                                                                     │
│  ┌─────────────┐                    ┌─────────────┐                              │
│  │   POS       │───────────────────►│   PRINTER   │                              │
│  │   SYSTEM    │   Order sent       │   (Ticket)  │                              │
│  │             │                    │             │                              │
│  │ • Table     │                    │ [Table 4]   │                              │
│  │   orders    │                    │ Ribeye MR   │                              │
│  │ • Mods      │                    │ Salmon      │                              │
│  │ • Timing    │                    │ Salad       │                              │
│  └─────────────┘                    └──────┬──────┘                              │
│                                              │                                     │
│                                              │ Ticket printed                      │
│                                              ▼                                     │
│  ┌─────────────────────────────────────────────────────────────────────────┐       │
│  │                    TICKET FLOW                                            │       │
│  │                                                                          │       │
│  │   ┌─────────────────────────────────────────────────────────────────┐   │       │
│  │   │                      THE RAIL                                     │   │       │
│  │   │   ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐          │   │       │
│  │   │   │Table 4 │  │Table 7  │  │Table 2  │  │Table 9  │          │   │       │
│  │   │   │ 7:42   │  │ 7:45    │  │ 7:46    │  │ 7:48    │          │   │       │
│  │   │   │ ↑      │  │ ↑       │  │ ↑       │  │ ↑       │          │   │       │
│  │   │   │Oldest  │  │         │  │         │  │Newest   │          │   │       │
│  │   │   └─────────┘  └─────────┘  └─────────┘  └─────────┘          │   │       │
│  │   │                                                                  │   │       │
│  │   │   Tickets flow: OLDEST ◄────────────────────────────────► NEWEST│       │
│  │   │                                                                  │   │       │
│  │   └─────────────────────────────────────────────────────────────────┘   │       │
│  │                                    │                                       │       │
│  │                                    │ Tickets called                        │       │
│  │                                    ▼                                       │       │
│  │   ┌─────────────────────────────────────────────────────────────────┐   │       │
│  │   │                    EXPO CALL                                     │   │       │
│  │   │                                                                  │   │       │
│  │   │   "TICKET TABLE 4 — 7:42 — RIBEYE MEDIUM RARE, SALMON,         │   │       │
│  │   │    HOUSE SALAD — NO MODS"                                       │   │       │
│  │   │                                                                  │   │       │
│  │   │   ↓                                                              │   │       │
│  │   │   Each station acknowledges: "Heard, Table 4"                  │   │       │
│  │   │                                                                  │   │       │
│  │   └─────────────────────────────────────────────────────────────────┘   │       │
│  │                                    │                                       │       │
│  └────────────────────────────────────┼───────────────────────────────────────┘       │
│                                       │                                              │
│                    ┌──────────────────┼──────────────────┐                           │
│                    │                  │                  │                           │
│                    ▼                  ▼                  ▼                           │
│  ┌─────────────────────────┐ ┌─────────────────────────┐ ┌─────────────────────────┐│
│  │      GRILL STATION       │ │     SAUTÉ STATION      │ │   COLD/FRY STATION      ││
│  │                         │ │                         │ │                         ││
│  │  David acknowledges    │ │  Chen acknowledges     │ │  Rosa acknowledges     ││
│  │  "Ribeye, Table 4"     │ │  "Salmon, Table 4"    │ │  "Salad, Table 4"     ││
│  │         │              │ │         │              │ │         │              ││
│  │         ▼              │ │         ▼              │ │         ▼              ││
│  │  ┌──────────────┐    │ │  ┌──────────────┐    │ │  ┌──────────────┐    ││
│  │  │ FIRE RIBEYE  │    │ │  │ FIRE SALMON  │    │ │  │ PLATE SALAD  │    ││
│  │  │ 7:42 + 12min │    │ │  │  7:42 + 8min │    │ │  │  On ticket   │    ││
│  │  │ = 7:54       │    │ │  │  = 7:50      │    │ │  │             │    ││
│  │  │              │    │ │  │              │    │ │  │             │    ││
│  │  │ "Ribeye      │    │ │  │ "Salmon      │    │ │  │ "Salad up,  │    ││
│  │  │  fired"      │    │ │  │  fired"      │    │ │  │  Table 4"  │    ││
│  │  └──────┬───────┘    │ │  └──────┬───────┘    │ │  └──────┬───────┘    ││
│  │         │              │ │         │              │ │         │              ││
│  │         │              │ │         │              │ │         │              ││
│  │         │  7:54      │ │         │  7:50      │ │         │  7:52      ││
│  │         │  + 3 min    │ │         │  + 2 min   │ │         │  + 1 min   ││
│  │         │  rest       │ │         │  finish     │ │         │  quality    ││
│  │         │              │ │         │              │ │         │  check      ││
│  │         ▼              │ │         ▼              │ │         ▼              ││
│  │  ┌──────────────┐    │ │  ┌──────────────┐    │ │  │  ┌──────────────┐    ││
│  │  │ RIBEYE UP    │    │ │  │ SALMON UP    │    │ │  │  │ COLD TO EXPO │    ││
│  │  │ Table 4      │    │ │  │ Table 4      │    │ │  │  │              │    ││
│  │  │              │    │ │  │              │    │ │  │  │              │    ││
│  │  │ "Ribeye up,  │    │ │  │ "Salmon up,  │    │ │  │  │              │    ││
│  │  │  Table 4"    │    │ │  │  Table 4"    │    │ │  │  │              │    ││
│  │  └──────┬───────┘    │ │  └──────┬───────┘    │ │  └──────┬───────┘    ││
│  └──────────┼──────────────┘ └──────────┼──────────┘ └──────────┼──────────────┘│
│             │                             │                             │          │
│             └─────────────────────────────┼─────────────────────────────┘          │
│                                           │                                        │
│                                           ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────────────┐       │
│  │                         EXPO STATION                                     │       │
│  │                                                                          │       │
│  │   James (Expo) receives all plates:                                     │       │
│  │                                                                          │       │
│  │   1. Visual check: All components present?                              │       │
│  │   2. Quality check: Proper plating? Temperature right?                 │       │
│  │   3. Timing check: Are all items for table at similar completion?      │       │
│  │   4. Modification check: Any mods that need verification?              │       │
│  │                                                                          │       │
│  │   IF ALL CHECKS PASS:                                                   │       │
│  │   "Table 4 UP! All day!" ────► Plates to heat lamp                    │       │
│  │                                                                          │       │
│  │   ┌─────────────────────────────────────────────────────────────┐      │       │
│  │   │                    SERVER PICKUP                              │      │       │
│  │   │                                                                  │      │       │
│  │   │   Server (Pat) responds: "Heard, Table 4"                    │      │       │
│  │   │                                                                  │      │       │
│  │   │   Server goes to pass, picks up Table 4 order                │     