# Domain Specific Language: Daily Workflow Instance Specification

## Pass 3 — Concrete Expression Syntax

### The Copper Beech Kitchen Workflow DSL

---

# I. Introduction to the DSL

## Purpose and Scope

This Domain Specific Language (DSL) provides the concrete syntax and expression patterns for specifying daily workflow instances in small commercial kitchens. Building on the conceptual foundation from Pass 1 and the generation system architecture from Pass 2, this DSL enables practitioners to:

- **Define** specific kitchen configurations with full contextual detail
- **Specify** daily workflow instances with precise timing and assignments
- **Express** constraints, dependencies, and coordination protocols
- **Document** station configurations, prep schedules, and service flows
- **Generate** actionable workflow documentation from specifications

## Design Principles

The DSL embodies three foundational principles:

**1. Fidelity to Domain Language**

The DSL uses vocabulary that practitioners already recognize: stations, tickets, fires, mise en place, expo, and the natural cadence of kitchen work. It does not impose artificial abstractions but rather formalizes the language that cooks, chefs, and kitchen staff use instinctively.

**2. Precision for Generation**

While natural in language, the DSL is precise in structure. Each expression maps to computable semantics that enable workflow generation, validation, and optimization. The DSL bridges human understanding and computational processing.

**3. Extensibility for Context**

The DSL is designed to be extended for specific kitchen contexts. The Copper Beech Kitchen expressions in this document demonstrate instantiation; the patterns extend to any small commercial kitchen configuration.

## Document Structure

This document proceeds as follows:

- Section II establishes the core primitives and vocabulary
- Section III defines constraint expression syntax
- Section IV specifies workflow instance structure
- Section V presents station configuration DSL
- Section VI covers timing and scheduling expressions
- Section VII addresses role and responsibility assignments
- Section VIII provides complete instance examples
- Section IX maps DSL to generation system implementation

---

# II. Core Primitives and Vocabulary

## II.A. Entity Primitives

### Kitchen Primitives

```yaml
# Kitchen Entity
kitchen:
  identifier: <string>           # Unique name, e.g., "copper_beech"
  type: <enum>                  # SMALL_RESTAURANT | CAFETERIA | CATERING | BISTRO
  capacity:
    seats: <integer>            # Total dining seats
    kitchen_sqft: <integer>     # Kitchen square footage
  service_hours:
    <day_of_week>:             # MONDAY through SUNDAY
      open: <time>              # e.g., "17:00"
      close: <time>             # e.g., "22:00"
      last_seating: <time>      # e.g., "21:00"
  timezone: <string>            # e.g., "America/New_York"
```

**Example:**
```yaml
kitchen:
  identifier: copper_beech
  type: SMALL_RESTAURANT
  capacity:
    seats: 45
    kitchen_sqft: 800
  service_hours:
    MONDAY:
      open: "17:00"
      close: "22:00"
      last_seating: "21:00"
    TUESDAY:
      open: "17:00"
      close: "22:00"
      last_seating: "21:00"
    WEDNESDAY:
      open: "17:00"
      close: "22:00"
      last_seating: "21:00"
    THURSDAY:
      open: "17:00"
      close: "22:00"
      last_seating: "21:00"
    FRIDAY:
      open: "17:00"
      close: "23:00"
      last_seating: "22:00"
    SATURDAY:
      open: "17:00"
      close: "23:00"
      last_seating: "22:00"
```

### Zone Primitives

```yaml
# Zone Entity
zone:
  name: <string>               # Unique zone identifier
  type: <enum>                # COLD | HOT | NEUTRAL | SUPPORT | SERVICE
  temperature_range:           # Optional, for temperature-controlled zones
    min_f: <integer>          # Minimum temperature in Fahrenheit
    max_f: <integer>          # Maximum temperature in Fahrenheit
  boundaries:                 # Physical definition
    x: <integer>              # X coordinate in kitchen grid
    y: <integer>              # Y coordinate in kitchen grid
    width: <integer>           # Width in feet
    depth: <integer>           # Depth in feet
  primary_function: <string>   # e.g., "storage", "cooking", "assembly"
```

**Example:**
```yaml
zones:
  - name: walkin_refrigerator
    type: COLD
    temperature_range:
      min_f: 33
      max_f: 41
    boundaries:
      x: 0
      y: 20
      width: 8
      depth: 10
    primary_function: "main_cold_storage"

  - name: hot_line
    type: HOT
    temperature_range:
      min_f: 150
      max_f: 500
    boundaries:
      x: 20
      y: 0
      width: 30
      depth: 12
    primary_function: "active_cooking"

  - name: the_pass
    type: SERVICE
    boundaries:
      x: 35
      y: 12
      width: 6
      depth: 4
    primary_function: "quality_check_handoff"
```

### Station Primitives

```yaml
# Station Entity
station:
  identifier: <string>         # Unique station identifier
  name: <string>              # Display name, e.g., "Grill Station"
  type: <enum>                # GRILL | SAUTE | FRY | COLD | PREP | EXPO | DISH | POT
  zone: <zone_name>           # Parent zone reference
  position:
    x: <integer>             # X coordinate within zone
    y: <integer>             # Y coordinate within zone
  bounds:
    width: <integer>         # Station width in feet
    depth: <integer>         # Station depth in feet
  equipment:                 # List of equipment at this station
    - equipment_id: <string>
      position: <string>     # e.g., "left", "center", "right"
  primary_role: <role_type>    # e.g., "GRILL_COOK"
  backup_role: <role_type>     # e.g., "SAUTE_COOK"
  capacity:
    max_concurrent_tasks: <integer>
    max_item_processing: <integer>
  adjacency:                  # Physically adjacent stations
    - <station_identifier>
  flow_paths:
    upstream:                # Stations that feed this station
      - <station_identifier>
    downstream:              # Stations this station feeds
      - <station_identifier>
```

**Example:**
```yaml
stations:
  - identifier: grill_station
    name: Grill Station
    type: GRILL
    zone: hot_line
    position:
      x: 20
      y: 0
    bounds:
      width: 8
      depth: 10
    equipment:
      - equipment_id: commercial_grill_01
        position: center
      - equipment_id: range_4_burner_01
        position: left
      - equipment_id: salamander_01
        position: overhead
    primary_role: GRILL_COOK
    backup_role: SAUTE_COOK
    capacity:
      max_concurrent_tasks: 3
      max_item_processing: 4
    adjacency:
      - saute_station
      - expo
    flow_paths:
      upstream:
        - prep_station
      downstream:
        - expo

  - identifier: saute_station
    name: Sauté Station
    type: SAUTE
    zone: hot_line
    position:
      x: 28
      y: 0
    bounds:
      width: 8
      depth: 10
    equipment:
      - equipment_id: range_6_burner_01
        position: center
    primary_role: SAUTE_COOK
    backup_role: GRILL_COOK
    capacity:
      max_concurrent_tasks: 4
      max_item_processing: 6
    adjacency:
      - grill_station
      - fry_cold_station
      - expo
    flow_paths:
      upstream:
        - prep_station
        - walkin_refrigerator
      downstream:
        - expo
```

### Equipment Primitives

```yaml
# Equipment Entity
equipment:
  identifier: <string>         # Unique equipment identifier
  type: <enum>                # See equipment taxonomy below
  station: <station_identifier>
  manufacturer: <string>      # e.g., "Vulcan"
  model: <string>             # e.g., "VCC6"
  capacity:
    type: <enum>              # PAN_COUNT | ITEM_COUNT | WEIGHT | VOLUME
    value: <integer>          # Capacity value
    unit: <string>            # e.g., "pans", "lbs", "qt"
  state: <enum>               # OPERATIONAL | NEEDS_MAINTENANCE | OUT_OF_SERVICE
  position:
    x: <integer>
    y: <integer>
  utility_requirements:
    gas_btuh: <integer>       # Gas British Thermal Units per hour
    electric_amps: <integer>  # Electric current in amps
    water_gpm: <integer>      # Water gallons per minute
  operational_parameters:
    preheat_time_minutes: <integer>
    recovery_time_minutes: <decimal>
    optimal_temp_f: <integer>
    temp_tolerance_f: <integer>
```

**Equipment Taxonomy:**
```
COOKING_EQUIPMENT:
  - GRILL (charcoal, gas, electric, flat_top)
  - OVEN (convection, deck, combi, pizza, roast)
  - RANGE (gas, electric, induction)
  - FRYER (deep_fat, shallow, pressure)
  - BROILER (overhead_salamander, drawer)
  - GRIDDLE
  - CHARBROILER
  - SMOKER

PREP_EQUIPMENT:
  - MIXER (planetary, vertical)
  - FOOD_PROCESSOR
  - SLICER (meat, vegetable)
  - SCALE
  - ROBOT_COUPE
  - PASTA_MACHINE
  - VACUUM_SEALER

STORAGE_EQUIPMENT:
  - WALK_IN (refrigerator, freezer)
  - REACH_IN (refrigerator, freezer)
  - PREP_TABLE (refrigerated)
  - HOLDING_CABINET (hot, cold)
  - DRY_STORAGE

CLEANUP_EQUIPMENT:
  - DISHMACHINE
  - COMPARTMENT_SINK (3, 4)
  - POT_SINK
```

**Example:**
```yaml
equipment:
  - identifier: commercial_grill_01
    type: GRILL
    station: grill_station
    manufacturer: "Summit"
    model: "SGA60"
    capacity:
      type: ITEM_COUNT
      value: 4
      unit: zones
    state: OPERATIONAL
    position:
      x: 22
      y: 2
    utility_requirements:
      gas_btuh: 60000
    operational_parameters:
      preheat_time_minutes: 15
      recovery_time_minutes: 2
      optimal_temp_f: 450
      temp_tolerance_f: 25

  - identifier: range_6_burner_01
    type: RANGE
    station: saute_station
    manufacturer: "Vulcan"
    model: "VCC6"
    capacity:
      type: PAN_COUNT
      value: 6
      unit: burners
    state: OPERATIONAL
    position:
      x: 28
      y: 0
    utility_requirements:
      gas_btuh: 150000
    operational_parameters:
      preheat_time_minutes: 10
      recovery_time_minutes: 1.5
```

---

## II.B. Role Primitives

```yaml
# Personnel Entity
personnel:
  identifier: <string>        # Unique personnel identifier
  name: <string>              # Display name
  role: <enum>                # CHEF | SOUS_CHEF | LINE_COOK | PREP_COOK | DISH
  skills:                     # Competency levels
    <skill_type>:
      level: <integer>        # 1-5 proficiency
      certified: <boolean>
  certifications:
    - type: <string>         # e.g., "ServSafe Manager"
      expiry: <date>
  cross_training:             # Stations this person can cover
    - station: <station_identifier>
      proficiency: <integer>  # 1-5
  availability:
    <day_of_week>:
      start: <time>
      end: <time>
      break_required: <boolean>
  fatigue_model:
    max_shift_hours: <integer>
    performance_curve:        # Performance degradation over shift hours
      - hours: <integer>
        multiplier: <decimal>  # e.g., 1.0 at start, 0.9 at hour 6
```

**Example:**
```yaml
personnel:
  - identifier: maria_01
    name: Maria
    role: CHEF
    skills:
      all_stations:
        level: 5
        certified: true
      menu_design:
        level: 5
        certified: false
      staff_development:
        level: 4
        certified: false
    certifications:
      - type: ServSafe Manager
        expiry: "2025-08-15"
    cross_training: []
    availability:
      MONDAY:
        start: "10:00"
        end: "23:00"
        break_required: true
      TUESDAY:
        start: "10:00"
        end: "23:00"
        break_required: true
      WEDNESDAY:
        start: "10:00"
        end: "23:00"
        break_required: true
      THURSDAY:
        start: "10:00"
        end: "23:00"
        break_required: true
      FRIDAY:
        start: "10:00"
        end: "00:00"
        break_required: true
      SATURDAY:
        start: "10:00"
        end: "00:00"
        break_required: true
    fatigue_model:
      max_shift_hours: 10
      performance_curve:
        - hours: 0
          multiplier: 1.0
        - hours: 4
          multiplier: 1.0
        - hours: 6
          multiplier: 0.95
        - hours: 8
          multiplier: 0.85
        - hours: 10
          multiplier: 0.75

  - identifier: james_02
    name: James
    role: SOUS_CHEF
    skills:
      all_stations:
        level: 4
        certified: true
      expediting:
        level: 5
        certified: false
    certifications:
      - type: ServSafe Manager
        expiry: "2025-06-20"
    cross_training:
      - station: grill_station
        proficiency: 4
      - station: saute_station
        proficiency: 4
      - station: prep_station
        proficiency: 3
    availability:
      MONDAY:
        start: "14:00"
        end: "23:00"
        break_required: true
      TUESDAY:
        start: "14:00"
        end: "23:00"
        break_required: true
      WEDNESDAY:
        start: "14:00"
        end: "23:00"
        break_required: true
      THURSDAY:
        start: "14:00"
        end: "23:00"
        break_required: true
      FRIDAY:
        start: "14:00"
        end: "00:00"
        break_required: true
      SATURDAY:
        start: "14:00"
        end: "00:00"
        break_required: true
    fatigue_model:
      max_shift_hours: 10
      performance_curve:
        - hours: 0
          multiplier: 1.0
        - hours: 4
          multiplier: 1.0
        - hours: 6
          multiplier: 0.95
        - hours: 8
          multiplier: 0.85
```

---

## II.C. Menu Primitives

```yaml
# Menu Item Entity
menu_item:
  identifier: <string>        # Unique menu item identifier
  name: <string>              # Display name, e.g., "Grilled Ribeye"
  category: <enum>            # APPETIZER | ENTREE | DESSERT | SIDE | BEVERAGE
  station_assignment: <station_identifier>
  difficulty: <integer>        # 1-5 complexity rating
  expected_demand:
    weekday_avg: <integer>    # Average covers per service
    weekend_avg: <integer>
    peak: <integer>
  recipe: <recipe_reference>

# Recipe Entity
recipe:
  identifier: <string>
  menu_item: <menu_item_identifier>
  ingredient_list:
    - ingredient: <string>
      quantity: <decimal>
      unit: <string>          # oz, lb, each, cup, etc.
      state: <enum>           # RAW | PREPARED | COOKED
  transformation_sequence:
    - step: <integer>
      name: <string>
      technique: <string>
      equipment: <equipment_type>
      duration_minutes: <integer>
      dependencies:            # Steps that must complete before this
        - step: <integer>
      produces: <string>      # Intermediate or final product
  timing_profile:
    prep_lead_hours: <decimal>
    active_cook_minutes: <integer>
    rest_minutes: <integer>
    total_minutes: <integer>
  quality_standards:
    temperature_f: <integer>
    visual_indicators:         # What "done" looks like
      - <string>
    texture_descriptors:        # Expected mouthfeel
      - <string>
  holding_requirements:
    max_hold_minutes: <integer>
    holding_temp_f: <integer>
    degradation_notes: <string>
```

**Example:**
```yaml
menu_items:
  - identifier: grilled_ribeye
    name: Grilled Ribeye
    category: ENTREE
    station_assignment: grill_station
    difficulty: 3
    expected_demand:
      weekday_avg: 8
      weekend_avg: 12
      peak: 15
    recipe: ribeye_recipe_01

  - identifier: pan_seared_salmon
    name: Pan-Seared Salmon
    category: ENTREE
    station_assignment: saute_station
    difficulty: 3
    expected_demand:
      weekday_avg: 10
      weekend_avg: 14
      peak: 18
    recipe: salmon_recipe_01

recipes:
  ribeye_recipe_01:
    identifier: ribeye_recipe_01
    menu_item: grilled_ribeye
    ingredient_list:
      - ingredient: ribeye_steak
        quantity: 14
        unit: oz
        state: RAW
      - ingredient: herb_butter
        quantity: 1
        unit: tbsp
        state: PREPARED
      - ingredient: demi_glace
        quantity: 2
        unit: oz
        state: PREPARED
      - ingredient: seasonal_vegetables
        quantity: 4
        unit: oz
        state: PREPARED
    transformation_sequence:
      - step: 1
        name: Season and fire grill
        technique: direct_heat_grilling
        equipment: GRILL
        duration_minutes: 8
        dependencies: []
        produces: grilled_steak_raw
      - step: 2
        name: Rest steak
        technique: resting
        equipment: NONE
        duration_minutes: 3
        dependencies: [1]
        produces: rested_steak
      - step: 3
        name: Apply herb butter
        technique: mounting
        equipment: NONE
        duration_minutes: 1
        dependencies: [2]
        produces: buttered_steak
      - step: 4
        name: Finish with demi
        technique: finishing
        equipment: NONE
        duration_minutes: 1
        dependencies: [3]
        produces: finished_steak
    timing_profile:
      prep_lead_hours: 0.5
      active_cook_minutes: 10
      rest_minutes: 3
      total_minutes: 13
    quality_standards:
      temperature_f: 145
      visual_indicators:
        - "Grill marks present on 2 sides"
        - "Browned exterior"
        - "Butter melted and pooling"
      texture_descriptors:
        - "Tender when pressed"
        - "Juicy, not dry"
    holding_requirements:
      max_hold_minutes: 5
      holding_temp_f: 140
      degradation_notes: "Best served immediately after butter application"

  salmon_recipe_01:
    identifier: salmon_recipe_01
    menu_item: pan_seared_salmon
    ingredient_list:
      - ingredient: salmon_fillet
        quantity: 6
        unit: oz
        state: RAW
      - ingredient: capers
        quantity: 0.5
        unit: oz
        state: PREPARED
      - ingredient: lemon_juice
        quantity: 0.25
        unit: oz
        state: RAW
      - ingredient: butter
        quantity: 0.5
        unit: oz
        state: PREPARED
      - ingredient: white_wine
        quantity: 1
        unit: oz
        state: PREPARED
    transformation_sequence:
      - step: 1
        name: Score and season salmon
        technique: prep
        equipment: NONE
        duration_minutes: 2
        dependencies: []
        produces: seasoned_salmon
      - step: 2
        name: Sear salmon skin-side down
        technique: pan_searing
        equipment: RANGE
        duration_minutes: 4
        dependencies: [1]
        produces: seared_salmon
      - step: 3
        name: Flip and baste
        technique: basting
        equipment: RANGE
        duration_minutes: 3
        dependencies: [2]
        produces: finished_salmon
    timing_profile:
      prep_lead_hours: 0.25
      active_cook_minutes: 7
      rest_minutes: 0
      total_minutes: 7
    quality_standards:
      temperature_f: 125
      visual_indicators:
        - "Crispy skin"
        - "Golden-brown exterior"
        - "Opaque flesh"
      texture_descriptors:
        - "Moist, not dry"
        - "Skin crispy"
    holding_requirements:
      max_hold_minutes: 3
      holding_temp_f: 140
      degradation_notes: "Skin loses crispiness after 2 minutes"
```

---

# III. Constraint Expression Syntax

## III.A. Constraint Structure

```yaml
# Base Constraint Structure
constraint:
  identifier: <string>         # Unique constraint identifier
  type: <enum>                # HARD | SOFT | OPTIMIZATION
  category: <enum>            # PHYSICAL | EQUIPMENT | TEMPORAL | HUMAN | SAFETY | ECONOMIC
  description: <string>       # Human-readable description
  expression: <expression_type>
  priority: <integer>         # 1-10, higher = more important
  enforcement: <enum>         # STRICT | RECOMMENDED | PREFERRED
```

## III.B. Physical Constraint Expressions

```yaml
# Distance Constraint
expression:
  type: DISTANCE
  source: <entity_reference>    # Station, zone, or equipment
  destination: <entity_reference>
  max_distance_feet: <integer>
  reason: <string>

# Travel Time Constraint
expression:
  type: TRAVEL_TIME
  source: <entity_reference>
  destination: <entity_reference>
  max_time_seconds: <integer>
  reason: <string>

# Adjacency Constraint
expression:
  type: ADJACENCY
  station_a: <station_reference>
  station_b: <station_reference>
  required: <boolean>         # Must be adjacent vs. should not be adjacent
  reason: <string>

# Zone Separation Constraint
expression:
  type: ZONE_SEPARATION
  zone_a: <zone_reference>
  zone_b: <zone_reference>
  separation_required: <boolean>
  crossing_protocol: <enum>   # NOT_ALLOWED | SANITATION_REQUIRED | RESTRICTED_ACCESS
```

**Example:**
```yaml
constraints:
  - identifier: cb-spatial-001
    type: HARD
    category: PHYSICAL
    description: "Walk-in to prep station travel time must not exceed 2 minutes"
    expression:
      type: TRAVEL_TIME
      source: walkin_refrigerator
      destination: prep_station
      max_time_seconds: 120
      reason: "Temperature control for protein transport"
    priority: 10
    enforcement: STRICT

  - identifier: cb-spatial-002
    type: HARD
    category: SAFETY
    description: "Raw protein prep and cold ready-to-eat assembly must not cross"
    expression:
      type: ZONE_SEPARATION
      zone_a: prep_station
      zone_b: cold_prep_station
      separation_required: true
      crossing_protocol: NOT_ALLOWED
    priority: 10
    enforcement: STRICT

  - identifier: cb-spatial-003
    type: SOFT
    category: PHYSICAL
    description: "Grill and sauté stations should be adjacent for sauce coordination"
    expression:
      type: ADJACENCY
      station_a: grill_station
      station_b: saute_station
      required: true
      reason: "Shared sauce work during protein finishing"
    priority: 6
    enforcement: RECOMMENDED
```

## III.C. Equipment Constraint Expressions

```yaml
# Capacity Constraint
expression:
  type: CAPACITY
  equipment: <equipment_reference>
  capacity_type: <enum>       # CONCURRENT_ITEMS | SEQUENTIAL_THROUGHPUT | TEMP_RANGE
  max_value: <integer>
  unit: <string>
  reason: <string>

# Recovery Time Constraint
expression:
  type: RECOVERY_TIME
  equipment: <equipment_reference>
  recovery_minutes: <decimal>
  trigger: <enum>             # AFTER_LOAD | AFTER_TEMP_CHANGE | AFTER_BASKET_CHANGE
  reason: <string>

# Shared Resource Constraint
expression:
  type: SHARED_RESOURCE
  resource: <utility_reference>  # gas_line, electric_circuit, water
  connected_equipment:
    - <equipment_reference>
  max_concurrent_usage_pct: <integer>
  scheduling_constraint: <enum>  # REQUIRED_COORDINATION | PREFERRED_SEQUENTIAL | OPTIONAL
```

**Example:**
```yaml
  - identifier: cb-equip-001
    type: HARD
    category: EQUIPMENT
    description: "Commercial grill limited to 4 simultaneous items"
    expression:
      type: CAPACITY
      equipment: commercial_grill_01
      capacity_type: CONCURRENT_ITEMS
      max_value: 4
      unit: items
      reason: "4 grill zones physically available"
    priority: 10
    enforcement: STRICT

  - identifier: cb-equip-002
    type: HARD
    category: EQUIPMENT
    description: "Combi oven requires 5-minute recovery between loads"
    expression:
      type: RECOVERY_TIME
      equipment: combi_oven_01
      recovery_minutes: 5
      trigger: AFTER_LOAD
      reason: "Steam and temperature equilibration"
    priority: 9
    enforcement: STRICT

  - identifier: cb-equip-003
    type: HARD
    category: EQUIPMENT
    description: "6-burner range limited to 6 active burners"
    expression:
      type: CAPACITY
      equipment: range_6_burner_01
      capacity_type: CONCURRENT_ITEMS
      max_value: 6
      unit: burners
      reason: "6 burners physically available"
    priority: 10
    enforcement: STRICT
```

## III.D. Temporal Constraint Expressions

```yaml
# Time Window Constraint
expression:
  type: TIME_WINDOW
  window_type: <enum>         # SERVICE | PREP | AVAILABILITY | MAINTENANCE
  start_time: <time>
  end_time: <time>
  hard_boundary: <boolean>
  reason: <string>

# Lead Time Constraint
expression:
  type: LEAD_TIME
  item: <menu_item_reference>
  min_lead_minutes: <integer>
  max_lead_minutes: <integer>
  reason: <string>

# Target Timing Constraint
expression:
  type: TARGET_TIMING
  target_type: <enum>         # TICKET | COURSE | PREP_ITEM
  target_value_minutes: <integer>
  max_acceptable_multiplier: <decimal>  # e.g., 1.3 = 30% buffer acceptable
  reason: <string>

# Precedence Constraint
expression:
  type: PRECEDENCE
  predecessor: <task_reference>
  successor: <task_reference>
  offset_minutes: <integer>   # Optional lag time
  hard: <boolean>
```

**Example:**
```yaml
  - identifier: cb-time-001
    type: HARD
    category: TEMPORAL
    description: "Service window: 5:00 PM to 10:00 PM"
    expression:
      type: TIME_WINDOW
      window_type: SERVICE
      start_time: "17:00"
      end_time: "22:00"
      hard_boundary: true
      reason: "Business hours"
    priority: 10
    enforcement: STRICT

  - identifier: cb-time-002
    type: HARD
    category: TEMPORAL
    description: "Prep window: 10:00 AM to 4:30 PM"
    expression:
      type: TIME_WINDOW
      window_type: PREP
      start_time: "10:00"
      end_time: "16:30"
      hard_boundary: true
      reason: "Complete before service, staff availability"
    priority: 10
    enforcement: STRICT

  - identifier: cb-time-003
    type: SOFT
    category: TEMPORAL
    description: "Entrée ticket time target: 18 minutes"
    expression:
      type: TARGET_TIMING
      target_type: COURSE
      target_value_minutes: 18
      max_acceptable_multiplier: 1.3
      reason: "Customer expectation and kitchen reputation"
    priority: 7
    enforcement: RECOMMENDED

  - identifier: cb-time-004
    type: HARD
    category: TEMPORAL
    description: "Risotto cannot start after 9:30 PM"
    expression:
      type: LEAD_TIME
      item: wild_mushroom_risotto
      min_lead_minutes: 18
      max_lead_minutes: 0
      reason: "18-minute cook time; service ends at 10:00 PM"
    priority: 9
    enforcement: STRICT
```

## III.E. Human Constraint Expressions

```yaml
# Minimum Staffing Constraint
expression:
  type: MINIMUM_STAFFING
  min_count: <integer>
  min_roles:
    - role: <role_type>
      count: <integer>
  reason: <string>

# Skill Requirement Constraint
expression:
  type: SKILL_REQUIREMENT
  task: <task_reference>
  required_skills:
    - skill: <skill_type>
      min_level: <integer>
  reason: <string>

# Coverage Constraint
expression:
  type: COVERAGE
  station: <station_reference>
  min_coverage: <integer>
  max_coverage: <integer>
  coverage_map:               # Who can cover whom
    primary: <personnel_reference>
    backup:
      - <personnel_reference>
  reason: <string>

# Fatigue Constraint
expression:
  type: FATIGUE
  max_shift_hours: <integer>
  min_break_minutes: <integer>
  break_frequency_hours: <integer>
  performance_threshold: <decimal>  # e.g., 0.85 = 85% performance minimum
```

**Example:**
```yaml
  - identifier: cb-human-001
    type: HARD
    category: HUMAN
    description: "Minimum 4 staff required to open safely"
    expression:
      type: MINIMUM_STAFFING
      min_count: 4
      min_roles:
        - role: CHEF
          count: 1
        - role: LINE_COOK
          count: 2
        - role: SUPPORT
          count: 1
      reason: "Minimum coverage for safe operation"
    priority: 10
    enforcement: STRICT

  - identifier: cb-human-002
    type: HARD
    category: HUMAN
    description: "ServSafe Manager must be on duty during all service hours"
    expression:
      type: SKILL_REQUIREMENT
      task: ALL_SERVICE_TASKS
      required_skills:
        - skill: food_safety_management
          min_level: 1
      reason: "Health code requirement"
    priority: 10
    enforcement: STRICT

  - identifier: cb-human-003
    type: SOFT
    category: HUMAN
    description: "Cross-training coverage map for evening service"
    expression:
      type: COVERAGE
      station: grill_station
      min_coverage: 1
      max_coverage: 2
      coverage_map:
        primary: david_01
        backup:
          - chen_02
          - james_02
      reason: "Ensure continuity when primary cook unavailable"
    priority: 7
    enforcement: RECOMMENDED
```

## III.F. Food Safety Constraint Expressions

```yaml
# Temperature Zone Constraint
expression:
  type: TEMPERATURE_ZONE
  zone_type: <enum>           # COLD_HOLDING | HOT_HOLDING | DANGER_ZONE
  min_temp_f: <integer>
  max_temp_f: <integer>
  max_time_minutes: <integer>
  measurement_method: <enum>   # INFRARED | PROBE | AMBIENT_ONLY
  monitoring_frequency_minutes: <integer>
  reason: <string>

# Cross-Contamination Prevention
expression:
  type: CROSS_CONTAMINATION
  source_materials:
    - <material_type>
  target_materials:
    - <material_type>
  prevention_method: <enum>   # PHYSICAL