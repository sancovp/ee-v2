# The Complete Instance: A Conceptual Model of a Fully Realized Workflow Generation System

## An Exemplar Demonstrating System Coherence

---

## Part I: Introduction — The Purpose of an Exemplar

### 1.1 From Abstract to Concrete

Our prior analyses established the essential nature of workflow generation systems: their ontology as living patterns of transformation (0-abstractgoal.md), their design as a nexus of stakeholder relationships, generative grammars, and epistemological architectures (1-systemsdesign.md), their architecture as a set of essential functions, structures, and relationships (2-systemsarchitecture.md), their vocabulary as a domain-specific language for kitchen operations (3-dsl.md), and their topology as a natural structure of interconnected concepts (4-topology.md).

These analyses are necessary but not sufficient. To truly understand what a workflow generation system *is*, we must see it *in action*—not merely executing a single workflow, but functioning as a complete system across its full lifecycle. We must observe the system as it transforms abstract inputs into concrete workflow instances, as it learns from execution feedback, as it maintains itself through time, and as it participates in the continuous design of kitchen operations.

This artifact provides that concrete understanding. Through a unified exemplar—a fully realized instance of a workflow generation system serving a specific small commercial kitchen—we demonstrate how the abstract principles we have articulated become actual system behavior. The exemplar is necessarily fictional and simplified, but it is *structurally faithful* to the concepts we have developed: every component, relationship, and process in the exemplar corresponds to something in our prior analyses.

### 1.2 The Exemplar's Kitchen: Copper Beech Bistro

We name our exemplar kitchen **Copper Beech Bistro**—a small farm-to-table restaurant with 40 seats, a seasonally rotating menu of 12-15 items, a team of 6 staff members, and a single service period from 5:30 PM to 9:30 PM. This kitchen is complex enough to require genuine workflow design yet simple enough to present comprehensively in an exemplar.

Copper Beech Bistro occupies a narrow storefront with:

- A **preparation area** (8' × 10') for cold prep and pantry
- A **hot line** (12' linear) with a 4-burner range, a grill, and a fryer
- A **sauté station** at the center of the line
- A **expediting station** at the end of the line
- A **walk-in cooler** accessible from the prep area
- A **pastry corner** with a small oven and reach-in refrigeration

The kitchen employs:

- **Maria** (executive chef and owner) — full menu expertise, available 3 PM to 10 PM
- **David** (sous chef) — hot line expertise, available 2 PM to 10 PM
- **Elena** (line cook) — grill and fry expertise, available 4 PM to 10 PM
- **James** (prep cook) — vegetable prep and pantry, available 1 PM to 9 PM
- **Sophie** (prep cook) — protein prep and sauces, available 2 PM to 9 PM
- **Tyler** (dish/prep support) — available 4 PM to 10 PM

The menu for the exemplar service includes:

- **Starters**: House salad, Roasted beet salad, Soup of the day
- **Mains**: Grilled salmon, Pan-seared chicken breast, Braised short rib, Mushroom risotto, Roasted half chicken
- **Sides**: Roasted vegetables, Whipped potatoes, Seasonal greens
- **Desserts**: Chocolate torte, Seasonal fruit crostata

### 1.3 The Exemplar's System: WorkflowGen-1

We name our exemplar system **WorkflowGen-1**—a workflow generation system designed specifically for small commercial kitchens like Copper Beech. WorkflowGen-1 is not a software application per se but a *social-technical formation*: the combination of people, processes, knowledge structures, and technical components that together constitute the system's capacity to generate appropriate workflows.

WorkflowGen-1 operates at three levels:

- **Static design**: Explicit generation rules, constraint specifications, and pattern libraries maintained in documentation
- **Dynamic design**: Real-time adaptations during execution based on emerging conditions
- **Learning design**: Feedback mechanisms that enable the system to improve through accumulated experience

The system is maintained by **the design team** (Maria and David, who have the deepest understanding of generation principles) with input from all practitioners. The system serves **the practitioners** (the entire Copper Beech team) who execute generated workflows and provide feedback.

---

## Part II: The System's Representation of Copper Beech

### 2.1 The Kitchen Model

WorkflowGen-1 maintains a comprehensive representation of Copper Beech's kitchen—the medium through which generation occurs. This representation is not a static database but a dynamic structure, continuously updated through observation, practitioner input, and accumulated experience.

**Physical Layout Representation**

The kitchen layout is represented as a spatial graph with nodes (stations, equipment, access points) and edges (flow paths, adjacency relationships, distance measures):

```yaml
spatial-model:
  kitchen-dimensions:
    length: 40  # feet
    width: 20   # feet
    
  zones:
    - id: prep-area
      type: preparation
      dimensions: [8, 10]  # feet
      position: north-west
      adjacent-to: [walk-in, hot-line]
      flow-capacity: 2  # simultaneous workers
      
    - id: hot-line
      type: cooking
      dimensions: [12, 6]  # linear feet × width
      position: south
      adjacent-to: [prep-area, expediting]
      flow-capacity: 4
      
    - id: expediting
      type: plating
      dimensions: [6, 4]
      position: south-east
      adjacent-to: [hot-line, dining-access]
      flow-capacity: 2
      
    - id: pastry-corner
      type: dessert
      dimensions: [6, 6]
      position: north-east
      adjacent-to: [walk-in]
      flow-capacity: 1
      
    - id: walk-in
      type: storage
      dimensions: [8, 6]
      position: north
      adjacent-to: [prep-area, pastry-corner]
      flow-capacity: 1

  flow-paths:
    - name: prep-to-line
      from: prep-area
      to: hot-line
      distance: 6  # feet
      type: ingredient-flow
      
    - name: line-to-expo
      from: hot-line
      to: expediting
      distance: 4
      type: plated-dish-flow
      
    - name: storage-access
      from: walk-in
      to: [prep-area, pastry-corner]
      distance: 8
      type: retrieval-flow

  equipment-locations:
    - equipment-id: range-4-burner
      zone: hot-line
      position: [2, 2]  # coordinates within zone
      access-points: [front]
      
    - equipment-id: grill-main
      zone: hot-line
      position: [8, 2]
      access-points: [front, right]
      
    - equipment-id: fryer-main
      zone: hot-line
      position: [10, 2]
      access-points: [front]
      
    - equipment-id: oven-pastry
      zone: pastry-corner
      position: [1, 3]
      access-points: [front]
```

**Equipment Inventory Representation**

Equipment is represented with full specifications that enable constraint satisfaction:

```yaml
equipment:
  - id: range-4-burner
    type: range
    subtype: standard-burner
    quantity: 4
    location: hot-line
    capacity:
      - pan-size: 12-inch
        simultaneous: 4
    output-rate:
      - heat-level: high
        time-to-boil: 4-minutes (1L water)
    condition: good
    maintenance-schedule: quarterly inspection
    constraints:
      - type: simultaneous-use
        limit: 4
      - type: pot-size
        max: 12-inch

  - id: grill-main
    type: grill
    subtype: flat-top
    dimensions: [24, 18]  # inches
    location: hot-line-end
    capacity:
      - protein-type: salmon
        simultaneous: 4
      - protein-type: chicken
        simultaneous: 3
    output-rate:
      - item: salmon
        time-per-item: 8-minutes
      - item: chicken-breast
        time-per-item: 10-minutes
    condition: good
    maintenance-schedule: annual cleaning, monthly grates
    constraints:
      - type: surface-area
        limit: 432  # square inches
      - type: cook-times
        specified: true

  - id: fryer-main
    type: fryer
    subtype: deep-fry
    capacity:
      - volume: 12-liters
      - basket-count: 2
    temperature-range: [300, 375]  # Fahrenheit
    output-rate:
      - item: fries
        batch-time: 4-minutes
        batch-size: 2-pounds
    condition: good
    maintenance-schedule: daily filtering, weekly oil-change
    constraints:
      - type: batch-size
        max: 2-pounds
      - type: recovery-time
        between-batches: 2-minutes

  - id: oven-pastry
    type: oven
    subtype: deck
    dimensions: [18, 18]  # inches
    location: pastry-corner
    temperature-range: [200, 500]
    output-rate:
      - item: torte
        time-per-batch: 25-minutes
      - item: crostata
        time-per-batch: 20-minutes
    condition: fair  # older unit, temperature variance ±15°F
    maintenance-schedule: annual inspection
    constraints:
      - type: temperature-variance
        margin: 15  # Fahrenheit
      - type: batch-size
        max: 4-items

  - id: walk-in
    type: cooler
    subtype: walk-in
    dimensions: [8, 6, 8]  # feet (length, width, height)
    temperature-range: [33, 38]  # Fahrenheit
    zones:
      - name: protein
        position: north
        capacity: 20-pans
      - name: produce
        position: center
        capacity: 15-pans
      - name: dairy
        position: south
        capacity: 10-pans
    condition: excellent
    maintenance-schedule: monthly cleaning, semi-annual inspection
    constraints:
      - type: temperature
        hard-range: [33, 40]
      - type: door-open-time
        max: 30-seconds
```

**Staff Profile Representation**

Staff profiles capture the human resources available for workflow execution:

```yaml
staff:
  - id: maria
    name: Maria
    role: executive-chef
    full-name: "Maria Santos"
    availability:
      - type: regular
        days: [tuesday, wednesday, thursday, friday, saturday]
        hours: [15:00, 22:00]
      - type: note
        text: "Available earlier if needed for special events"
    skills:
      - domain: menu
        level: expert
        items: [all]
      - domain: cooking-technique
        level: expert
        techniques: [all]
      - domain: management
        level: expert
        functions: [staffing, quality-control, menu-planning]
    certifications:
      - type: food-manager
        expires: 2026-03-15
      - type: allergen-awareness
        expires: 2025-11-01
    cross-training:
      - station: sauté
        level: proficient
      - station: grill
        level: proficient
      - station: expediting
        level: expert
    preferences:
      - type: work-style
        value: "Prefers clear station assignments, dislikes ambiguity"
      - type: communication
        value: "Favors direct verbal communication over written notes"
    historical-performance:
      - period: last-6-months
        quality-rating: 4.8/5
        consistency-rating: 4.9/5
        punctuality-rating: 5.0/5

  - id: david
    name: David
    role: sous-chef
    full-name: "David Chen"
    availability:
      - type: regular
        days: [wednesday, thursday, friday, saturday, sunday]
        hours: [14:00, 22:00]
      - type: note
        text: "Leaves at 9 PM on Sundays for family commitment"
    skills:
      - domain: hot-line
        level: expert
        stations: [sauté, grill, fry]
      - domain: vegetable-prep
        level: proficient
      - domain: management
        level: proficient
        functions: [quality-control, staff-training]
    certifications:
      - type: food-handler
        expires: 2025-09-20
      - type: allergen-awareness
        expires: 2025-11-01
    cross-training:
      - station: sauté
        level: expert
      - station: expediting
        level: proficient
    preferences:
      - type: work-style
        value: "Works best with moderate pace, dislikes rush without warning"
      - type: communication
        value: "Prefers advance notice of busy periods"
    historical-performance:
      - period: last-6-months
        quality-rating: 4.7/5
        consistency-rating: 4.6/5
        punctuality-rating: 4.8/5

  - id: elena
    name: Elena
    role: line-cook
    full-name: "Elena Rodriguez"
    availability:
      - type: regular
        days: [tuesday, wednesday, thursday, friday, saturday]
        hours: [16:00, 22:00]
      - type: note
        text: "Strong preference for grill station"
    skills:
      - domain: grill
        level: expert
        items: [salmon, chicken, vegetables]
      - domain: fry
        level: proficient
        items: [fries, occasional fried-apps]
      - domain: sauté
        level: developing
        items: [simple-sauces]
    certifications:
      - type: food-handler
        expires: 2026-01-15
    cross-training:
      - station: grill
        level: expert
      - station: fry
        level: proficient
      - station: sauté
        level: developing
    preferences:
      - type: station-preference
        primary: grill
        secondary: fry
      - type: work-style
        value: "Prefers steady workflow, strong dislike of ticket piles"
    historical-performance:
      - period: last-6-months
        quality-rating: 4.6/5
        consistency-rating: 4.8/5
        punctuality-rating: 4.9/5
        note: "Strong performer during steady service, struggles when tickets exceed 6 simultaneous"

  - id: james
    name: James
    role: prep-cook
    full-name: "James Okafor"
    availability:
      - type: regular
        days: [tuesday, wednesday, thursday, friday, saturday, sunday]
        hours: [13:00, 21:00]
    skills:
      - domain: vegetable-prep
        level: expert
        items: [all-vegetables, salads]
      - domain: pantry
        level: proficient
        items: [dressings, cold-apps]
      - domain: hot-line
        level: basic
        items: [simple-sides]
    certifications:
      - type: food-handler
        expires: 2025-08-30
    cross-training:
      - station: prep
        level: expert
      - station: pantry
        level: proficient
      - station: hot-line
        level: basic
    preferences:
      - type: work-style
        value: "Works best with clear prep lists, methodical approach"
      - type: communication
        value: "Prefers written prep lists to verbal instructions"
    historical-performance:
      - period: last-6-months
        quality-rating: 4.9/5
        consistency-rating: 4.8/5
        punctuality-rating: 4.7/5

  - id: sophie
    name: Sophie
    role: prep-cook
    full-name: "Sophie Martin"
    availability:
      - type: regular
        days: [wednesday, thursday, friday, saturday, sunday]
        hours: [14:00, 21:00]
    skills:
      - domain: protein-prep
        level: expert
        items: [butchery, marinades, short-rib-prep]
      - domain: sauce-making
        level: proficient
        items: [mother-sauces, reductions]
      - domain: vegetable-prep
        level: developing
    certifications:
      - type: food-handler
        expires: 2025-12-01
      - type: allergen-awareness
        expires: 2025-11-01
    cross-training:
      - station: protein-prep
        level: expert
      - station: sauce-station
        level: proficient
    preferences:
      - type: work-style
        value: "Prefers working independently, minimal interruption"
      - type: communication
        value: "Prefers face-to-face when possible, otherwise text"
    historical-performance:
      - period: last-6-months
        quality-rating: 4.8/5
        consistency-rating: 4.7/5
        punctuality-rating: 4.8/5

  - id: tyler
    name: Tyler
    role: support
    full-name: "Tyler Washington"
    availability:
      - type: regular
        days: [tuesday, wednesday, thursday, friday, saturday]
        hours: [16:00, 22:00]
    skills:
      - domain: dish
        level: expert
      - domain: prep-support
        level: proficient
        tasks: [ingredient-retrieval, equipment-setup, basic-chopping]
      - domain: line-support
        level: developing
        tasks: [plating-assist, station-cleaning]
    certifications:
      - type: food-handler
        expires: 2025-10-15
    cross-training:
      - station: dish
        level: expert
      - station: prep-support
        level: proficient
    preferences:
      - type: work-style
        value: "Adaptable, works wherever needed"
      - type: communication
        value: "Prefers direct, immediate communication"
    historical-performance:
      - period: last-6-months
        quality-rating: 4.5/5
        consistency-rating: 4.6/5
        punctuality-rating: 4.8/5
        note: "Occasional gaps in communication when absorbed in dish tasks"
```

**Menu Representation**

The menu is represented as a specification of what must be produced, with all the details needed for workflow generation:

```yaml
menu:
  name: "Copper Beech Bistro - Spring Menu"
  season: spring
  effective-date: 2025-03-15
  service:
    start: 17:30
    end: 21:30
    expected-covers:
      - day: tuesday
        low: 15
        high: 25
        typical: 20
      - day: wednesday
        low: 20
        high: 35
        typical: 28
      - day: thursday
        low: 25
        high: 40
        typical: 32
      - day: friday
        low: 30
        high: 50
        typical: 40
      - day: saturday
        low: 30
        high: 55
        typical: 42

  items:
    - id: house-salad
      category: starter
      components:
        - name: mixed-greens
          type: prepared-ingredient
          prep-required: true
          prep-duration: 15-minutes
          prep-assignment: james
        - name: vinaigrette
          type: component
          prep-required: true
          prep-duration: 10-minutes
          prep-assignment: james
        - name: assembly
          type: assembly
          assembly-location: cold-station
          assembly-time: 3-minutes
      station: cold-station
      plating-time: 3-minutes
      cook-time: 0
      firing-order: early
      allergen-risks: [sulfites]

    - id: beet-salad
      category: starter
      components:
        - name: roasted-beets
          type: component
          prep-required: true
          prep-duration: 45-minutes (including roasting)
          prep-assignment: james
        - name: goat-cheese
          type: prepared-ingredient
          prep-required: false
          source: local-dairy
        - name: candied-walnuts
          type: component
          prep-required: true
          prep-duration: 20-minutes
          prep-assignment: james
        - name: microgreens
          type: prepared-ingredient
          prep-required: false
          source: local-farm
        - name: assembly
          type: assembly
          assembly-location: cold-station
          assembly-time: 5-minutes
      station: cold-station
      plating-time: 5-minutes
      cook-time: 0
      firing-order: early
      allergen-risks: [dairy, tree-nuts]

    - id: grilled-salmon
      category: main
      components:
        - name: salmon-fillet
          type: prepared-ingredient
          prep-required: true
          prep-duration: 5-minutes (portioning only)
          prep-assignment: sophie
        - name: herb-butter
          type: component
          prep-required: true
          prep-duration: 15-minutes
          prep-assignment: sophie
        - name: lemon-caper-sauce
          type: component
          prep-required: true
          prep-duration: 20-minutes
          prep-assignment: sophie
        - name: seasonal-vegetables
          type: component
          prep-required: true
          prep-duration: varies
          prep-assignment: james
        - name: finish
          type: final-cook
          station: grill
          time: 8-minutes
      station: grill-station
      plating-time: 4-minutes
      cook-time: 8-minutes
      firing-order: main
      allergen-risks: [fish, dairy]

    - id: chicken-breast
      category: main
      components:
        - name: chicken-breast
          type: prepared-ingredient
          prep-required: true
          prep-duration: 10-minutes (trimming, pounding)
          prep-assignment: sophie
        - name: pan-sauce
          type: component
          prep-required: true
          prep-duration: 15-minutes
          prep-assignment: sophie
        - name: roasted-potatoes
          type: component
          prep-required: true
          prep-duration: 45-minutes (including roasting)
          prep-assignment: james
        - name: finish
          type: final-cook
          station: sauté
          time: 12-minutes (pan-seared)
      station: sauté-station
      plating-time: 4-minutes
      cook-time: 12-minutes
      firing-order: main
      allergen-risks: [dairy]

    - id: short-rib
      category: main
      components:
        - name: short-rib
          type: prepared-ingredient
          prep-required: true
          prep-duration: 45-minutes (braising prep)
          prep-assignment: sophie
          note: "Pre-braised, reheated for service"
        - name: braising-liquid
          type: component
          prep-required: true
          prep-duration: 15-minutes (reduction)
          prep-assignment: sophie
        - name: root-vegetables
          type: component
          prep-required: true
          prep-duration: 30-minutes
          prep-assignment: james
        - name: finish
          type: final-cook
          station: sauté
          time: 15-minutes (reheat + sauce)
      station: sauté-station
      plating-time: 5-minutes
      cook-time: 15-minutes
      firing-order: late
      allergen-risks: []

    - id: mushroom-risotto
      category: main
      components:
        - name: soffritto
          type: component
          prep-required: true
          prep-duration: 20-minutes
          prep-assignment: sophie
        - name: mushroom-mix
          type: component
          prep-required: true
          prep-duration: 25-minutes
          prep-assignment: james
        - name: arborio-rice
          type: prepared-ingredient
          prep-required: true
          prep-duration: 10-minutes (washing, soaking)
          prep-assignment: james
        - name: finish
          type: final-cook
          station: sauté
          time: 18-minutes (risotto cooking)
          note: "Active stirring required"
      station: sauté-station
      plating-time: 4-minutes
      cook-time: 18-minutes
      firing-order: late
      allergen-risks: [dairy]

    - id: roasted-chicken
      category: main
      components:
        - name: half-chicken
          type: prepared-ingredient
          prep-required: true
          prep-duration: 20-minutes (brining, seasoning)
          prep-assignment: sophie
        - name: finish
          type: final-cook
          station: oven-pastry
          time: 30-minutes
          note: "Early fire required, finished before peak"
      station: sauté-station
      plating-time: 4-minutes
      cook-time: 30-minutes
      firing-order: early-main
      allergen-risks: []

    - id: chocolate-torte
      category: dessert
      components:
        - name: torte-base
          type: component
          prep-required: true
          prep-duration: 30-minutes
          prep-assignment: james
        - name: ganache
          type: component
          prep-required: true
          prep-duration: 15-minutes
          prep-assignment: james
        - name: assembly
          type: assembly
          assembly-location: pastry-corner
          assembly-time: 5-minutes
      station: pastry-corner
      plating-time: 5-minutes
      cook-time: 0
      allergen-risks: [dairy, eggs, gluten]
```

### 2.2 The Constraint Specification

WorkflowGen-1 maintains a comprehensive specification of constraints that govern generation for Copper Beech. These constraints define the boundary of possibility—what the system can and cannot generate.

**Hard Constraints (Non-Negotiable)**

```yaml
hard-constraints:
  food-safety:
    - id: temp-cold-holding
      type: temperature
      requirement: "All cold foods below 40°F (4°C)"
      verification: walk-in-temp-check
      frequency: every-4-hours
      priority: critical
      
    - id: temp-hot-holding
      type: temperature
      requirement: "All hot foods above 140°F (60°C)"
      verification: temp-gun-check
      frequency: every-2-hours
      priority: critical
      
    - id: cook-temp-salmon
      type: temperature
      requirement: "Salmon internal temp minimum 145°F (63°C)"
      verification: instant-read-thermometer
      critical: true
      penalty: workflow-invalid
      
    - id: cook-temp-chicken
      type: temperature
      requirement: "Chicken internal temp minimum 165°F (74°C)"
      verification: instant-read-thermometer
      critical: true
      penalty: workflow-invalid
      
    - id: time-danger-zone
      type: time
      requirement: "No food in danger zone (40-140°F) for more than 2 hours cumulative"
      verification: log-time-in-out
      penalty: workflow-invalid
      
    - id: cross-contamination
      type: separation
      requirement: "Raw proteins stored below and separate from ready-to-eat foods"
      verification: visual-inspection
      priority: critical
      
    - id: allergen-separation
      type: separation
      requirement: "Allergen-containing items prepared with dedicated equipment when possible"
      verification: station-designation

  physical:
    - id: equipment-capacity
      type: capacity
      requirement: "No more items on equipment than capacity allows"
      penalty: workflow-invalid
      
    - id: spatial-clearance
      type: space
      requirement: "Minimum 36-inch pathways maintained at all times"
      
    - id: staff-breaks
      type: labor
      requirement: "30-minute break after 5 hours of work"
      
  legal:
    - id: food-handler-certs
      type: certification
      requirement: "All food handlers have current food handler permits"
      
    - id: manager-present
      type: certification
      requirement: "Certified food manager present during all hours of food preparation"

  safety:
    - id: fire-extinguisher-access
      type: equipment
      requirement: "Fire extinguisher accessible within 20 feet of cooking equipment"
      
    - id: clear-exit-paths
      type: egress
      requirement: "Exits and pathways to exits clear at all times"
```

**Soft Constraints (Preferred Conditions)**

```yaml
soft-constraints:
  timing:
    - id: prep-buffer
      type: timing
      preference: "All prep complete 30 minutes before service"
      flexibility: 15-minutes
      weight: 0.8
      
    - id: station-setup-complete
      type: timing
      preference: "Stations fully set up 15 minutes before service"
      flexibility: 10-minutes
      weight: 0.7
      
    - id: first-service-tolerance
      type: timing
      preference: "First order out within 18 minutes of order"
      flexibility: 5-minutes
      weight: 0.6
      
    - id: average-ticket-time
      type: timing
      preference: "Average ticket time 14-16 minutes"
      flexibility: 2-minutes
      weight: 0.9

  quality:
    - id: plate-temperature
      type: quality
      preference: "Plates heated before plating"
      verification: visual
      weight: 0.5
      
    - id: protein-rest
      type: quality
      preference: "Grilled proteins rest 2-3 minutes before plating"
      weight: 0.6
      
    - id: sauce-separation
      type: quality
      preference: "Sauces not touching protein directly unless specified"
      weight: 0.4

  efficiency:
    - id: equipment-utilization
      type: efficiency
      preference: "Equipment utilization between 60-80% during peak"
      weight: 0.5
      
    - id: labor-efficiency
      type: efficiency
      preference: "Labor cost under 32% of food cost"
      weight: 0.6
      
    - id: ticket-pile-limit
      type: workflow
      preference: "No more than 6 active tickets per station"
      note: "Based on Elena's observed threshold"
      weight: 0.8

  practitioner-preferences:
    - id: elena-ticket-limit
      type: staffing
      preference: "Elena not assigned more than 6 simultaneous orders at grill"
      priority: high
      weight: 0.9
      
    - id: sophie-independence
      type: workflow
      preference: "Sophie's prep tasks minimize interruptions"
      priority: medium
      weight: 0.6
      
    - id: james-written-lists
      type: communication
      preference: "James receives written prep lists, not verbal"
      priority: medium
      weight: 0.7
```

**Optimization Targets**

```yaml
optimization-targets:
  primary:
    - id: service-quality
      objective: "Maintain consistent food quality across all orders"
      measure: quality-rating
      direction: maximize
      weight: 0.4
      
    - id: ticket-time
      objective: "Keep average ticket time within target range"
      measure: average-ticket-minutes
      target: [14, 16]
      weight: 0.3

  secondary:
    - id: staff-satisfaction
      objective: "Respect practitioner preferences and workload limits"
      measure: preference-satisfaction-rate
      target: 0.9
      weight: 0.15
      
    - id: cost-efficiency
      objective: "Maintain labor costs within acceptable range"
      measure: labor-cost-per-cover
      target: [18, 22]
      weight: 0.15

  tradeoffs:
    - between: [service-quality, cost-efficiency]
      resolution: "Quality takes precedence over cost savings"
      
    - between: [ticket-time, service-quality]
      resolution: "Quality takes precedence over speed"
```

---

## Part III: The Pattern Library — Accumulated Wisdom

### 3.1 The Structure of Patterns

The pattern library is the repository of WorkflowGen-1's accumulated experience—successful workflow configurations that inform new generation. Each pattern captures a solution to a recurring problem, with specifications for when the pattern applies and how to adapt it.

Patterns are stored with rich structure:

```yaml
pattern-structure:
  - structural-pattern
    description: "The recurring workflow structure"
    
  - context-pattern
    description: "Conditions under which the pattern is effective"
    
  - outcome-pattern
    description: "Results achieved when pattern is applied successfully"
    
  - adaptation-pattern
    description: "Guidance for modifying pattern for different contexts"
```

### 3.2 Exemplar Patterns from Copper Beech

**The Prep-to-Service Flow Pattern**

```yaml
pattern