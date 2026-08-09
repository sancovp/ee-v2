# The Complete Implementation: Building the Copper Beech Workflow Generation System

## A Constructed System for Daily Kitchen Workflow Generation

---

## Part I: Introduction — From Design to Construction

### 1.1 The Recursive Nature of This Artifact

In our prior analyses, we have established the essential nature of workflow generation systems (L1P1), articulated the meta-generator that constructs such systems (L1P2), and examined the feedback loops that enable continuous improvement. We now arrive at the construction imperative: to build, in concrete detail, the specific system that will generate daily workflow instances for Copper Beech Bistro.

This artifact serves a dual purpose. First, it demonstrates how the abstract principles of system building become an actual, operational system—a working generator capable of producing the workflow instances that guide Copper Beech's daily operations. Second, it provides a template for constructing workflow generation systems for other kitchens: the patterns, structures, and processes articulated here can be adapted to any small commercial kitchen context.

The system we build here is named **CopperBeech-WorkflowGen**—an instance of the workflow generation system archetype, configured specifically for the Copper Beech Bistro context. This is not merely a configuration of a generic system but a complete, coherent construction: the knowledge structures, synthesis engines, feedback mechanisms, and output formatters that together constitute the system's generative capacity.

### 1.2 What This Artifact Accomplishes

This artifact provides the complete construction specification for CopperBeech-WorkflowGen:

1. **The Knowledge Structure**: How the system represents the Copper Beech context—what it knows about the kitchen, the staff, the menu, the equipment, and the constraints
2. **The Pattern Library**: The workflow patterns that encode successful approaches to kitchen operations
3. **The Constraint Specification**: The hard and soft constraints that govern what configurations are possible
4. **The Synthesis Engine**: The algorithms that transform context into workflow instances
5. **The Feedback Mechanisms**: How the system learns from execution outcomes
6. **The Output Specifications**: How generated workflows are formatted for practitioner use
7. **The Integration Architecture**: How all components work together as a unified system
8. **The Instantiation Process**: How the system is configured and deployed

### 1.3 The Architecture in Brief

CopperBeech-WorkflowGen follows the three-level architecture we have established:

**Static Design Level**: The explicit knowledge structures, pattern libraries, constraint specifications, and generation rules that define what the system can produce.

**Dynamic Design Level**: The real-time monitoring and adaptation mechanisms that respond to emerging conditions during execution.

**Learning Design Level**: The feedback collection, interpretation, and incorporation mechanisms that enable the system to improve over time.

These three levels are not separate components but aspects of a unified system—each enabling and informing the others.

---

## Part II: The Knowledge Structure

### 2.1 Overview of the Knowledge Base

The knowledge base is the system's long-term memory—the repository of all information it uses to generate workflows. For CopperBeech-WorkflowGen, the knowledge base contains five primary knowledge domains:

```yaml
knowledge-base-domains:
  spatial-knowledge:
    description: "Physical layout and spatial relationships"
    contents:
      - kitchen-dimensions: "40' × 20' total footprint"
      - station-locations: "Defined positions of all stations"
      - equipment-positions: "Precise locations within stations"
      - flow-paths: "Movement routes between stations"
      - storage-zones: "Walk-in, reach-in, and dry storage locations"
      
  equipment-knowledge:
    description: "Equipment capabilities and constraints"
    contents:
      - equipment-inventory: "Complete list of all equipment"
      - capacity-specifications: "What each piece can handle"
      - timing-characteristics: "How long operations take"
      - condition-tracking: "Current equipment status"
      - maintenance-schedule: "When maintenance is due"
      
  human-knowledge:
    description: "Staff capabilities and availability"
    contents:
      - staff-profiles: "Skills, certifications, preferences for each person"
      - role-definitions: "What each role entails"
      - coverage-patterns: "Who covers whom during breaks"
      - availability-schedules: "When each person can work"
      - performance-history: "How each person has performed"
      
  menu-knowledge:
    description: "Menu structure and requirements"
    contents:
      - menu-items: "All items on the menu"
      - component-requirements: "What each item requires"
      - timing-specifications: "How long each component takes"
      - station-assignments: "Where each component is prepared"
      - allergen-information: "Allergen risks for each item"
      - demand-patterns: "Historical ordering patterns"
      
  operational-knowledge:
    description: "Procedures and practices"
    contents:
      - phase-definitions: "Setup, pre-service, service, close phases"
      - communication-protocols: "How staff communicate"
      - escalation-procedures: "How issues are handled"
      - quality-standards: "What constitutes acceptable output"
      - timing-standards: "Target times for various operations"
```

### 2.2 The Spatial Knowledge Module

The spatial knowledge module represents the physical structure of Copper Beech's kitchen:

```yaml
spatial-knowledge-module:
  module-id: spatial-knowledge
  
  kitchen-layout:
    overall-dimensions:
      length: 40  # feet
      width: 20   # feet
      total-area: 800  # square feet
      
    zones:
      - zone-id: prep-area
        name: "Preparation Area"
        dimensions: [8, 10]  # feet
        position: "northwest"
        area: 80
        adjacent-to: [walk-in, hot-line]
        flow-capacity: 2  # simultaneous workers
        
      - zone-id: hot-line
        name: "Hot Line"
        dimensions: [12, 6]  # linear feet × width
        position: "south"
        area: 72
        adjacent-to: [prep-area, expediting]
        flow-capacity: 4
        
      - zone-id: expediting
        name: "Expediting Station"
        dimensions: [6, 4]
        position: "southeast"
        area: 24
        adjacent-to: [hot-line, dining-access]
        flow-capacity: 2
        
      - zone-id: pastry-corner
        name: "Pastry Corner"
        dimensions: [6, 6]
        position: "northeast"
        area: 36
        adjacent-to: [walk-in]
        flow-capacity: 1
        
      - zone-id: walk-in
        name: "Walk-in Cooler"
        dimensions: [8, 6]
        position: "north"
        area: 48
        adjacent-to: [prep-area, pastry-corner]
        flow-capacity: 1
        
  flow-paths:
    - path-id: ingredient-flow
      name: "Ingredient Retrieval"
      from: [walk-in, dry-storage]
      to: [prep-area, hot-line]
      distance: [8, 6]  # feet
      type: bidirectional
      frequency: high
      
    - path-id: prep-to-line
      name: "Prep to Line"
      from: prep-area
      to: hot-line
      distance: 6  # feet
      type: unidirectional
      frequency: very-high
      
    - path-id: line-to-expo
      name: "Line to Expo"
      from: hot-line
      to: expediting
      distance: 4  # feet
      type: unidirectional
      frequency: very-high
      
    - path-id: dish-return
      name: "Dish Return"
      from: expediting
      to: dish-area
      distance: 10  # feet
      type: unidirectional
      frequency: medium
      
  spatial-constraints:
    minimum-pathway-width: 36  # inches
    maximum-reach-distance: 24  # inches from station edge
    equipment-clearance: 18  # inches around equipment
    emergency-exit-clearance: 44  # inches (ADA minimum)
```

### 2.3 The Equipment Knowledge Module

The equipment knowledge module captures the capabilities and constraints of Copper Beech's equipment:

```yaml
equipment-knowledge-module:
  module-id: equipment-knowledge
  
  equipment-inventory:
    - equipment-id: range-4-burner
      name: "4-Burner Range"
      type: range
      location: hot-line
      position: [2, 2]  # coordinates within zone
      
      capabilities:
        burner-count: 4
        simultaneous-pans: 4
        pan-size-max: 12  # inches
        
      timing:
        heat-to-boil: 4  # minutes (1L water, high heat)
        simmer-recovery: 30  # seconds
        
      condition: good
      maintenance-due: 2025-06-15
      constraint-id: eq-range-001
      
    - equipment-id: grill-main
      name: "Flat-Top Grill"
      type: grill
      subtype: flat-top
      location: hot-line
      position: [8, 2]
      
      capabilities:
        surface-area: [24, 18]  # inches
        surface-area-sq-in: 432
        
      capacity:
        salmon:
          max-simultaneous: 4
          cook-time: 8  # minutes
        chicken:
          max-simultaneous: 3
          cook-time: 12  # minutes
        vegetables:
          max-simultaneous: 6
          cook-time: 6  # minutes
          
      temperature:
        operating-range: [400, 450]  # Fahrenheit
        target: 425
        
      condition: good
      maintenance-due: 2025-09-01
      constraint-id: eq-grill-001
      
    - equipment-id: fryer-main
      name: "Deep Fryer"
      type: fryer
      location: hot-line
      position: [10, 2]
      
      capabilities:
        volume: 12  # liters
        basket-count: 2
        basket-capacity: 2  # pounds each
        
      temperature:
        operating-range: [325, 375]  # Fahrenheit
        target: 350
        
      timing:
        heat-to-temp: 15  # minutes
        recovery-between-batches: 2  # minutes
        
      condition: good
      maintenance-due: 2025-04-20  # oil change due
      constraint-id: eq-fryer-001
      
    - equipment-id: oven-pastry
      name: "Deck Oven"
      type: oven
      subtype: deck
      location: pastry-corner
      position: [1, 3]
      
      capabilities:
        interior-dimensions: [18, 18]  # inches
        max-batch: 4  # items
        
      temperature:
        operating-range: [200, 500]  # Fahrenheit
        
      timing:
        preheat: 20  # minutes
        baking:
          torte: 25  # minutes
          crostata: 20  # minutes
          
      condition: fair
      temperature-variance: 15  # Fahrenheit (older unit)
      maintenance-due: 2025-08-01
      constraint-id: eq-oven-001
      
    - equipment-id: walk-in
      name: "Walk-in Cooler"
      type: cooler
      subtype: walk-in
      location: north
      access: [prep-area, pastry-corner]
      
      capabilities:
        dimensions: [8, 6, 8]  # feet (L × W × H)
        volume: 384  # cubic feet
        
      temperature:
        operating-range: [33, 38]  # Fahrenheit
        target: 36
        
      zones:
        - name: protein
          position: north
          capacity: 20  # full-size pans
        - name: produce
          position: center
          capacity: 15
        - name: dairy
          position: south
          capacity: 10
          
      condition: excellent
      maintenance-due: 2025-10-01
      constraint-id: eq-walkin-001
      
    - equipment-id: reach-in-pastry
      name: "Reach-in Cooler"
      type: cooler
      subtype: reach-in
      location: pastry-corner
      
      capabilities:
        dimensions: [48, 30, 36]  # inches
        shelf-count: 4
        
      temperature:
        operating-range: [33, 38]
        target: 37
        
      condition: good
      maintenance-due: 2025-07-01
      constraint-id: eq-reachin-001
      
  equipment-constraints:
    - constraint-id: grill-capacity-limit
      description: "Grill cannot exceed maximum simultaneous items"
      type: capacity
      equipment: grill-main
      rule: "sum(active-grill-items) ≤ grill-max-capacity"
      
    - constraint-id: fryer-recovery
      description: "Fryer needs recovery time between batches"
      type: temporal
      equipment: fryer-main
      rule: "batch-start[2] ≥ batch-end[1] + 2-minutes"
      
    - constraint-id: oven-temperature-variance
      description: "Pastry oven has known temperature variance"
      type: quality
      equipment: oven-pastry
      rule: "allow ±15°F from target temperature"
      mitigation: "Monitor with independent thermometer"
```

### 2.4 The Human Knowledge Module

The human knowledge module represents the staff of Copper Beech:

```yaml
human-knowledge-module:
  module-id: human-knowledge
  
  staff-profiles:
    - person-id: maria
      name: "Maria Santos"
      role: executive-chef
      display-name: "Maria"
      
      availability:
        - days: [tuesday, wednesday, thursday, friday, saturday]
          hours: [15:00, 22:00]
          note: "Available earlier for special events"
          
      skills:
        - domain: menu
          level: expert
          coverage: all
        - domain: cooking-technique
          level: expert
          coverage: all
        - domain: management
          level: expert
          functions: [staffing, quality-control, menu-planning]
        - domain: station
          level: proficient
          stations: [sauté, grill, expediting]
          
      certifications:
        - type: food-manager
          number: "FM-2024-78432"
          issued: 2024-03-15
          expires: 2026-03-15
        - type: allergen-awareness
          issued: 2024-11-01
          expires: 2025-11-01
          
      performance-history:
        quality-rating: 4.8
        consistency-rating: 4.9
        punctuality-rating: 5.0
        
      preferences:
        work-style: "Prefers clear station assignments"
        communication: "Direct verbal communication preferred"
        
      authority-level: leadership
      
    - person-id: david
      name: "David Chen"
      role: sous-chef
      display-name: "David"
      
      availability:
        - days: [wednesday, thursday, friday, saturday, sunday]
          hours: [14:00, 22:00]
          note: "Leaves at 9 PM Sundays for family"
          
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
          
      performance-history:
        quality-rating: 4.7
        consistency-rating: 4.6
        punctuality-rating: 4.8
        
      preferences:
        work-style: "Works best with moderate pace"
        communication: "Advance notice of busy periods preferred"
        
      authority-level: senior
        
    - person-id: elena
      name: "Elena Rodriguez"
      role: line-cook
      display-name: "Elena"
      
      availability:
        - days: [tuesday, wednesday, thursday, friday, saturday]
          hours: [16:00, 22:00]
          
      skills:
        - domain: grill
          level: expert
          items: [salmon, chicken, vegetables]
        - domain: fry
          level: proficient
          items: [fries, fried-apps]
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
          
      performance-history:
        quality-rating: 4.6
        consistency-rating: 4.8
        punctuality-rating: 4.9
        note: "Struggles when tickets exceed 6 simultaneous"
        
      preferences:
        station-preference: grill
        work-style: "Prefers steady workflow, dislikes ticket piles"
        
      authority-level: standard
      
    - person-id: james
      name: "James Okafor"
      role: prep-cook
      display-name: "James"
      
      availability:
        - days: [tuesday, wednesday, thursday, friday, saturday, sunday]
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
          
      performance-history:
        quality-rating: 4.9
        consistency-rating: 4.8
        punctuality-rating: 4.7
        
      preferences:
        work-style: "Works best with clear prep lists"
        communication: "Prefers written prep lists over verbal"
        
      authority-level: standard
      
    - person-id: sophie
      name: "Sophie Martin"
      role: prep-cook
      display-name: "Sophie"
      
      availability:
        - days: [wednesday, thursday, friday, saturday, sunday]
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
          
      performance-history:
        quality-rating: 4.8
        consistency-rating: 4.7
        punctuality-rating: 4.8
        
      preferences:
        work-style: "Prefers working independently"
        communication: "Face-to-face preferred, text as backup"
        
      authority-level: standard
      
    - person-id: tyler
      name: "Tyler Washington"
      role: support
      display-name: "Tyler"
      
      availability:
        - days: [tuesday, wednesday, thursday, friday, saturday]
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
          
      performance-history:
        quality-rating: 4.5
        consistency-rating: 4.6
        punctuality-rating: 4.8
        note: "Occasional gaps in communication when absorbed in dish tasks"
        
      preferences:
        work-style: "Adaptable, works wherever needed"
        communication: "Direct, immediate communication preferred"
        
      authority-level: support
        
  role-definitions:
    - role-id: executive-chef
      name: "Executive Chef"
      primary-responsibilities:
        - menu-planning-and-development
        - quality-control
        - staff-management
        - expediting
      reports-to: owner
      covers-duties: [sous-chef]
      
    - role-id: sous-chef
      name: "Sous Chef"
      primary-responsibilities:
        - hot-line-lead
        - quality-control
        - staff-training
        - expediting-support
      reports-to: executive-chef
      covers-duties: [line-cook]
      
    - role-id: line-cook
      name: "Line Cook"
      primary-responsibilities:
        - station-operation
        - quality-execution
        - timing-coordination
      reports-to: sous-chef
      
    - role-id: prep-cook
      name: "Prep Cook"
      primary-responsibilities:
        - ingredient-preparation
        - component-preparation
        - station-setup
      reports-to: sous-chef
      
    - role-id: support
      name: "Support Staff"
      primary-responsibilities:
        - dish-and-equipment-cleaning
        - prep-assistance
        - station-support
      reports-to: sous-chef
        
  coverage-patterns:
    - pattern-id: standard-coverage
      description: "Standard break coverage during service"
      entries:
        - time: [18:30, 18:45]
          person-on-break: james
          coverage-provided-by: sophie
          coverage-station: cold-prep
          note: "Sophie's prep duties continue, cold assembly covered"
          
        - time: [18:30, 18:45]
          person-on-break: elena
          coverage-provided-by: tyler
          coverage-station: grill
          note: "Tyler maintains current tickets, no new fires during break"
          
    - pattern-id: backup-chain
      description: "Staff backup order when primary unavailable"
      chain:
        1. elena → tyler  # First backup for Elena is Tyler
        2. james → sophie  # First backup for James is Sophie
        3. sophie → david  # First backup for Sophie is David
        4. tyler → james  # Tyler can cover James in emergency
```

### 2.5 The Menu Knowledge Module

The menu knowledge module captures Copper Beech's menu structure:

```yaml
menu-knowledge-module:
  module-id: menu-knowledge
  
  menu-meta:
    name: "Copper Beech Bistro - Spring Menu"
    season: spring
    effective-date: 2025-03-15
    last-updated: 2025-03-10
    
  service-specification:
    start: 17:30
    end: 21:30
    expected-covers:
      tuesday:
        low: 15
        high: 25
        typical: 20
      wednesday:
        low: 20
        high: 35
        typical: 28
      thursday:
        low: 25
        high: 40
        typical: 32
      friday:
        low: 30
        high: 50
        typical: 40
      saturday:
        low: 30
        high: 55
        typical: 42
        
  menu-items:
    - item-id: house-salad
      name: "House Salad"
      category: starter
      price: 14
      
      components:
        - component-id: mixed-greens
          name: "Mixed Greens"
          type: prepared-ingredient
          prep-required: true
          prep-duration: 15  # minutes
          prep-assigned-to: james
          storage: walk-in-cold
          
        - component-id: vinaigrette
          name: "House Vinaigrette"
          type: component
          prep-required: true
          prep-duration: 10
          prep-assigned-to: james
          storage: walk-in-cold
          
        - component-id: salad-assembly
          name: "Salad Assembly"
          type: assembly
          station: cold-station
          assembly-time: 3  # minutes per plate
          
      cooking-time: 0
      plating-time: 3
      firing-order: early  # Plated before entrees
      
      allergen-risks: [sulfites]
      station: cold-station
      
    - item-id: beet-salad
      name: "Roasted Beet Salad"
      category: starter
      price: 16
      
      components:
        - component-id: roasted-beets
          name: "Roasted Beets"
          type: component
          prep-required: true
          prep-duration: 45  # including roasting
          prep-assigned-to: james
          storage: walk-in-produce
          
        - component-id: goat-cheese
          name: "Goat Cheese"
          type: prepared-ingredient
          prep-required: false
          source: local-dairy
          
        - component-id: candied-walnuts
          name: "Candied Walnuts"
          type: component
          prep-required: true
          prep-duration: 20
          prep-assigned-to: james
          storage: dry-storage
          
        - component-id: beet-salad-assembly
          name: "Beet Salad Assembly"
          type: assembly
          station: cold-station
          assembly-time: 5
          
      cooking-time: 0
      plating-time: 5
      firing-order: early
      
      allergen-risks: [dairy, tree-nuts]
      station: cold-station
      
    - item-id: soup
      name: "Soup of the Day"
      category: starter
      price: 12
      note: "Asparagus soup this week"
      
      components:
        - component-id: soup-base
          name: "Asparagus Soup"
          type: component
          prep-required: true
          prep-duration: 30
          prep-assigned-to: sophie
          storage: hot-hold
          note: "Made from vegetable scraps"
          
        - component-id: soup-garnish
          name: "Soup Garnish"
          type: component
          prep-required: true
          prep-duration: 10
          prep-assigned-to: james
          storage: walk-in-cold
          
      cooking-time: 0  # Reheated only
      plating-time: 2
      firing-order: early
      
      allergen-risks: []  # Varies by soup
      station: sauté-station
      
    - item-id: grilled-salmon
      name: "Grilled Salmon"
      category: main
      price: 34
      
      components:
        - component-id: salmon-fillet
          name: "Salmon Fillet"
          type: prepared-ingredient
          prep-required: true
          prep-duration: 5  # Portioning only
          prep-assigned-to: sophie
          storage: walk-in-protein
          
        - component-id: herb-butter
          name: "Herb Butter"
          type: component
          prep-required: true
          prep-duration: 15
          prep-assigned-to: sophie
          storage: reach-in-pastry
          
        - component-id: lemon-caper-sauce
          name: "Lemon Caper Sauce"
          type: component
          prep-required: true
          prep-duration: 20
          prep-assigned-to: sophie
          storage: hot-hold
          
        - component-id: salmon-vegetables
          name: "Seasonal Vegetables"
          type: component
          prep-required: true
          prep-duration: varies
          prep-assigned-to: james
          storage: walk-in-produce
          
        - component-id: salmon-finish
          name: "Grill Finish"
          type: final-cook
          station: grill
          cook-time: 8  # minutes
          rest-time: 2
          
      cook-time: 8
      plating-time: 4
      firing-order: main
      minimum-internal-temp: 145  # Fahrenheit
      
      allergen-risks: [fish, dairy]
      station: grill-station
      primary-cook: elena
      
    - item-id: chicken-breast
      name: "Pan-Seared Chicken Breast"
      category: main
      price: 28
      
      components:
        - component-id: chicken-breast
          name: "Chicken Breast"
          type: prepared-ingredient
          prep-required: true
          prep-duration: 10  # Trimming, pounding
          prep-assigned-to: sophie
          storage: walk-in-protein
          
        - component-id: pan-sauce
          name: "Pan Sauce"
          type: component
          prep-required: true
          prep-duration: 15
          prep-assigned-to: sophie
          storage: hot-hold
          
        - component-id: roasted-potatoes
          name: "Roasted Potatoes"
          type: component
          prep-required: true
          prep-duration: 45  # Including roasting
          prep-assigned-to: james
          storage: hot-hold
          
        - component-id: chicken-finish
          name: "Pan Sear Finish"
          type: final-cook
          station: sauté
          cook-time: 12  # minutes
          rest-time: 2
          
      cook-time: 12
      plating-time: 4
      firing-order: main
      minimum-internal-temp: 165
      
      allergen-risks: [dairy]
      station: sauté-station
      primary-cook: david
      
    - item-id: short-rib
      name: "Braised Short Rib"
      category: main
      price: 38
      
      components:
        - component-id: short-rib
          name: "Short Rib"
          type: prepared-ingredient
          prep-required: true
          prep-duration: 45  # Braising prep
          prep-assigned-to: sophie
          storage: walk-in-protein
          note: "Pre-braised Monday, reheated for service"
          
        - component-id: braising-reduction
          name: "Braising Reduction"
          type: component
          prep-required: true
          prep-duration: 15  # Reduction
          prep-assigned-to: sophie
          storage: hot-hold
          
        - component-id: root-vegetables
          name: "Root Vegetables"
          type: component
          prep-required: true
          prep-duration: 30
          prep-assigned-to: james
          storage: walk-in-produce
          
        - component-id: short-rib-finish
          name: "Reheat and Finish"
          type: final-cook
          station: sauté
          cook-time: 15  # Reheat + sauce
          rest-time: 2
          
      cook-time: 15
      plating-time: 5
      firing-order: late  # Longest active cook time
      
      allergen-risks: []
      station: sauté-station
      primary-cook: david
      
    - item-id: mushroom-risotto
      name: "Mushroom Risotto"
      category: main
      price: 26
      
      components:
        - component-id: soffritto
          name: "Soffritto"
          type: component
          prep-required: true
          prep-duration: 20
          prep-assigned-to: sophie
          storage: hot-hold
          
        - component-id: mushroom-mix
          name: "Mushroom Mix"
          type: component
          prep-required: true
          prep-duration: 25
          prep-assigned-to: james
          storage: walk-in-produce
          
        - component-id: arborio-rice
          name: "Arborio Rice"
          type: prepared-ingredient
          prep-required: true
          prep-duration: 10  # Washing, soaking
          prep-assigned-to: james
          storage: dry-storage
          
        - component-id: risotto-finish
          name: "Risotto Cooking"
          type: final-cook
          station: sauté
          cook-time: 18  # Active stirring required
          rest-time: 1
          
      cook-time: 18
      plating-time: 4
      firing-order: late  # Fires after short rib due to longer time
      
      allergen-risks: [dairy]
      station: sauté-station
      primary-cook: david
      
    - item-id: roasted-chicken
      name: "Roasted Half Chicken"
      category: main
      price: 32
      
      components:
        - component-id: half-chicken
          name: "Half Chicken"
          type: prepared-ingredient
          prep-required: true
          prep-duration: 20  # Brining, seasoning
          prep-assigned-to: sophie
          storage: walk-in-protein
          
        - component-id: chicken-roast-finish
          name: "Roast Finish"
          type: final-cook
          station: oven-pastry
          cook-time: 30  # Early fire required
          rest-time: 5
          
      cook-time: 30
      plating-time: 4
      firing-order: early-main  # Fires early due to long cook time
      
      allergen-risks: []
      station: sauté-station
      primary-cook: david
      
    - item-id: chocolate-torte
      name: "Chocolate Torte"
      category: dessert
      price: 12
      
      components:
        - component-id: torte-base
          name: "Torte Base"
          type: component
          prep-required: true
          prep-duration: 