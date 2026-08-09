# The Internal Language of WorkflowGen

## A Technical Specification for the Generator's Internal DSL

---

## Part I: Introduction — The System's Native Tongue

### 1.1 From Conceptual Vocabulary to Operational Language

Our prior analysis established the conceptual vocabulary of kitchen workflow generation—the terms, relationships, and grammar through which the domain thinks and communicates. We articulated a comprehensive DSL that captures the essence of small commercial kitchen operations: the substantive vocabulary of ingredients and equipment, the temporal vocabulary of timing and sequencing, the process vocabulary of activities and handoffs, the organizational vocabulary of roles and responsibilities, and the generation vocabulary of patterns and synthesis.

Yet conceptual vocabulary is not operational language. The terms we articulated are meaningful to humans who understand the domain; they must now be made meaningful to the system that will generate workflows. This artifact bridges that gap, specifying the internal language—the data structures, APIs, and operations—through which the workflow generation system thinks, generates, and controls.

The internal language is the translation layer between human understanding and machine computation. It must be precise enough for algorithmic processing yet rich enough to capture the domain's nuance. It must be formal enough for computation yet intuitive enough for practitioners to understand what the system is doing.

### 1.2 What This Artifact Specifies

This artifact provides a complete technical specification for the workflow generation system's internal DSL:

1. **Core Data Structures**: The fundamental types that represent kitchen entities, temporal elements, processes, and constraints
2. **API Interfaces**: The operations through which components interact and through which practitioners engage with the system
3. **Primitive Operations**: The atomic transformations that manipulate data structures
4. **Composite Operations**: The higher-level operations that combine primitives into meaningful synthesis actions
5. **Query Operations**: The mechanisms for extracting information from the system's knowledge
6. **Control Structures**: The mechanisms for directing system behavior

### 1.3 Design Principles

The internal language is designed according to several key principles:

**Expressiveness**: The language must capture all domain-relevant distinctions—every concept that matters for workflow generation must be representable.

**Computability**: The language must be suitable for algorithmic processing—every operation must have a clear, implementable meaning.

**Traceability**: The language must support explanation—the system must be able to explain its reasoning in terms practitioners can understand.

**Extensibility**: The language must accommodate growth—new concepts, constraints, and operations must be addable without redesign.

**Formality**: The language must have precise semantics—no ambiguous terms, no undefined behaviors.

---

## Part II: Core Data Structures

### 2.1 Type System Overview

The internal language defines a comprehensive type system that captures the domain's entities, relationships, and constraints:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CORE TYPE HIERARCHY                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                           ┌─────────────┐                                    │
│                           │   Entity    │                                    │
│                           │  (abstract) │                                    │
│                           └──────┬──────┘                                    │
│                    ┌────────────┼────────────┐                              │
│                    │            │            │                               │
│                    ▼            ▼            ▼                               │
│             ┌──────────┐  ┌──────────┐  ┌──────────┐                        │
│             │Material  │  │  Human   │  │ Process  │                        │
│             │ Entity   │  │  Entity  │  │  Entity  │                        │
│             └────┬─────┘  └────┬─────┘  └────┬─────┘                        │
│                  │            │            │                                │
│                  ▼            ▼            ▼                                │
│           ┌───────────┐ ┌───────────┐ ┌───────────┐                        │
│           │Ingredient│ │   Person  │ │ Activity  │                        │
│           │Equipment │ │   Role    │ │   Task    │                        │
│           │ Station  │ │   Team    │ │   Phase   │                        │
│           │Menu Item│ │           │ │ Workflow  │                        │
│           └───────────┘ └───────────┘ └───────────┘                        │
│                                                                              │
│                           ┌─────────────┐                                    │
│                           │  Temporal   │                                    │
│                           │   (abstract)│                                    │
│                           └──────┬──────┘                                    │
│                    ┌────────────┼────────────┐                              │
│                    │            │            │                               │
│                    ▼            ▼            ▼                               │
│             ┌──────────┐  ┌──────────┐  ┌──────────┐                        │
│             │  Moment  │  │ Interval │  │ Duration │                        │
│             │  Cycle   │  │ Timing   │  │ Sequence │                        │
│             └──────────┘  │ Window   │  └──────────┘                        │
│                           └──────────┘                                       │
│                                                                              │
│                           ┌─────────────┐                                    │
│                           │ Constraint  │                                    │
│                           │  (abstract) │                                    │
│                           └──────┬──────┘                                    │
│                    ┌────────────┼────────────┐                              │
│                    │            │            │                               │
│                    ▼            ▼            ▼                               │
│             ┌──────────┐  ┌──────────┐  ┌──────────┐                        │
│             │ Physical │  │   Food   │  │Operational│                       │
│             │Constraint│  │  Safety  │  │Constraint │                       │
│             └──────────┘  └──────────┘  └──────────┘                        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Material Entity Structures

**Ingredient**

```yaml
data-structure: Ingredient
description: "A material used in food preparation"
type-definition:
  fields:
    - name: ingredient_id
      type: UUID
      required: true
      description: "Unique identifier"
      
    - name: name
      type: String
      required: true
      description: "Human-readable name"
      
    - name: category
      type: Enum[raw, prepared, component]
      required: true
      description: "Position in transformation hierarchy"
      
    - name: unit_type
      type: Enum[purchase, storage, prep, portion]
      required: true
      description: "Measurement context"
      
    - name: storage_requirements
      type: StorageSpec
      required: false
      description: "How ingredient must be stored"
      
    - name: shelf_life
      type: Duration
      required: false
      description: "Expected usable lifespan"
      
    - name: allergen_flags
      type: Set[AllergenType]
      required: false
      description: "Associated allergens"
      
    - name: source
      type: String
      required: false
      description: "Supplier or origin information"

type StorageSpec:
  fields:
    - name: temperature_range
      type: Tuple[Float, Float]
      description: "Minimum and maximum temperature (Fahrenheit)"
      
    - name: humidity_requirements
      type: Enum[dry, ambient, humid]
      required: false
      
    - name: separation_requirements
      type: Set[String]
      required: false
      description: "What this must be kept separate from"

type AllergenType:
  enumeration:
    - dairy
    - eggs
    - fish
    - shellfish
    - tree_nuts
    - peanuts
    - wheat
    - soy
    - sesame
    - sulfites
```

**Equipment**

```yaml
data-structure: Equipment
description: "An apparatus used in food preparation"
type-definition:
  fields:
    - name: equipment_id
      type: UUID
      required: true
      
    - name: name
      type: String
      required: true
      
    - name: equipment_type
      type: Enum[
        range,          # Stovetop burners
        oven,           # Baking/roasting ovens
        grill,          # Grilling surfaces
        fryer,          # Deep frying equipment
        sauté,          # Sauté station equipment
        cooler,         # Refrigeration
        freezer,        # Frozen storage
        prep_table,     # Work surfaces
        sink,           # Washing facilities
        holding_cabinet # Hot holding
      ]
      required: true
      
    - name: subtype
      type: String
      required: false
      description: "Specific subtype (e.g., 'convection', 'deck', 'flat-top')"
      
    - name: capacity
      type: EquipmentCapacity
      required: true
      description: "What the equipment can hold or process"
      
    - name: output_rate
      type: Map[OperationType, Duration]
      required: false
      description: "Time required for common operations"
      
    - name: temperature_range
      type: Tuple[Float, Float]
      required: false
      description: "Operating temperature range"
      
    - name: condition
      type: Enum[excellent, good, fair, poor]
      required: true
      
    - name: location_id
      type: UUID
      required: true
      description: "Reference to station or zone"

type EquipmentCapacity:
  description: "Specifications for what equipment can handle"
  variant-type:
    - quantity_capacity:
        description: "For equipment that holds discrete items"
        fields:
          - name: max_items
            type: Integer
          - name: item_type
            type: Enum[plate, pan, portion, batch]
            
    - area_capacity:
        description: "For equipment with surface area"
        fields:
          - name: width_inches
            type: Float
          - name: depth_inches
            type: Float
          - name: max_items
            type: Integer
            description: "Items that fit on surface"
            
    - volume_capacity:
        description: "For equipment with volume"
        fields:
          - name: volume_liters
            type: Float
          - name: batch_size_liters
            type: Float
```

**Station**

```yaml
data-structure: Station
description: "A defined area of the kitchen dedicated to specific functions"
type-definition:
  fields:
    - name: station_id
      type: UUID
      required: true
      
    - name: name
      type: String
      required: true
      description: "Station name (e.g., 'grill-station', 'cold-prep')"
      
    - name: station_type
      type: Enum[
        hot_line,       # Primary cooking line
        cold_prep,      # Cold preparation and pantry
        grill,          # Grilling station
        sauté,          # Sauté station
        fry,            # Deep frying station
        roast,          # Roasting station
        expediting,     # Plating and timing coordination
        pastry,         # Dessert preparation
        dish,           # Dish washing
        prep_general    # General preparation
      ]
      required: true
      
    - name: location
      type: SpatialLocation
      required: true
      
    - name: equipment
      type: List[UUID]
      required: true
      description: "References to equipment at this station"
      
    - name: capacity
      type: StationCapacity
      required: true
      
    - name: coverage
      type: CoverageSpec
      required: true
      description: "Staff required to operate the station"
      
    - name: adjacent_stations
      type: Set[UUID]
      required: false
      description: "Neighboring stations for flow purposes"
      
    - name: functions
      type: Set[StationFunction]
      required: true
      description: "What types of work occur at this station"

type SpatialLocation:
  description: "Position within the kitchen layout"
  fields:
    - name: zone_id
      type: UUID
      description: "Reference to kitchen zone"
      
    - name: coordinates
      type: Tuple[Float, Float]
      description: "X, Y position within zone"
      
    - name: access_points
      type: Set[Enum[front, back, left, right]]
      description: "Where entry/exit is possible"

type StationCapacity:
  description: "Throughput limits for the station"
  fields:
    - name: simultaneous_workers
      type: Integer
      description: "Maximum people who can work here simultaneously"
      
    - name: max_active_orders
      type: Integer
      description: "Maximum orders the station can handle at once"
      
    - name: equipment_throughput
      type: Map[UUID, Integer]
      description: "Max items per equipment per service"

type CoverageSpec:
  description: "Staffing requirements"
  fields:
    - name: min_staff
      type: Integer
      description: "Minimum staff required"
      
    - name: max_staff
      type: Integer
      description: "Maximum staff useful at this station"
      
    - name: required_skills
      type: Set[SkillRequirement]
      description: "Skills staff must have"
      
    - name: preferred_staff_types
      type: Set[UUID]
      required: false
      description: "Specific staff who prefer this station"
```

**MenuItem**

```yaml
data-structure: MenuItem
description: "A dish offered to customers"
type-definition:
  fields:
    - name: menu_item_id
      type: UUID
      required: true
      
    - name: name
      type: String
      required: true
      
    - name: category
      type: Enum[starter, main, side, dessert, beverage]
      required: true
      
    - name: components
      type: List[ComponentSpec]
      required: true
      description: "Elements that compose this dish"
      
    - name: primary_station
      type: UUID
      required: true
      description: "Station where final assembly occurs"
      
    - name: cooking_time
      type: Duration
      required: true
      description: "Time from order to plate"
      
    - name: plating_time
      type: Duration
      required: true
      description: "Time for plating"
      
    - name: firing_order
      type: Enum[early, early_main, main, late]
      required: true
      description: "When this fires relative to other items"
      
    - name: allergen_risks
      type: Set[AllergenType]
      required: true
      
    - name: quality_standards
      type: QualitySpec
      required: true
      
    - name: presentation_requirements
      type: PresentationSpec
      required: false

type ComponentSpec:
  description: "A prepared element of a menu item"
  fields:
    - name: component_id
      type: UUID
      required: true
      
    - name: name
      type: String
      required: true
      
    - name: component_type
      type: Enum[prepared_ingredient, cooked_component, cold_component, assembled_component]
      required: true
      
    - name: prep_required
      type: Boolean
      required: true
      
    - name: prep_duration
      type: Duration
      required: false
      description: "Time to prepare"
      
    - name: prep_assignment
      type: UUID
      required: false
      description: "Preferred prep staff"
      
    - name: station
      type: UUID
      required: false
      description: "Where this component is prepared"
      
    - name: finish_required
      type: Boolean
      required: false
      description: "Requires final cooking before plating"
      
    - name: finish_station
      type: UUID
      required: false
      description: "Station for final cooking"
      
    - name: finish_time
      type: Duration
      required: false
      description: "Time for final cooking"
```

### 2.3 Human Entity Structures

**Person**

```yaml
data-structure: Person
description: "An individual who works in the kitchen"
type-definition:
  fields:
    - name: person_id
      type: UUID
      required: true
      
    - name: name
      type: String
      required: true
      
    - name: display_name
      type: String
      required: true
      description: "Name used in daily communications"
      
    - name: role
      type: UUID
      required: true
      description: "Reference to role definition"
      
    - name: availability
      type: List[AvailabilityWindow]
      required: true
      description: "When this person can work"
      
    - name: skills
      type: List[SkillEntry]
      required: true
      description: "Competencies in specific techniques or stations"
      
    - name: certifications
      type: List[Certification]
      required: true
      description: "Current licenses and training"
      
    - name: cross_training
      type: List[CrossTrainingEntry]
      required: false
      description: "Additional stations they can cover"
      
    - name: preferences
      type: Map[String, Any]
      required: false
      description: "Work preferences and dislikes"
      
    - name: performance_history
      type: PerformanceSummary
      required: false

type AvailabilityWindow:
  description: "A period when a person is available to work"
  fields:
    - name: day_pattern
      type: Enum[monday, tuesday, wednesday, thursday, friday, saturday, sunday, weekdays, weekends, daily]
      required: true
      
    - name: start_time
      type: Time
      required: true
      description: "When availability begins"
      
    - name: end_time
      type: Time
      required: true
      description: "When availability ends"
      
    - name: effective_date
      type: Date
      required: false
      description: "When this availability pattern begins"
      
    - name: expiration_date
      type: Date
      required: false
      description: "When this availability pattern ends"

type SkillEntry:
  description: "A skill or competency"
  fields:
    - name: skill_domain
      type: Enum[station, technique, cuisine, management]
      required: true
      
    - name: skill_name
      type: String
      required: true
      description: "Specific skill (e.g., 'grill', 'sauté', 'vegetable-prep')"
      
    - name: proficiency_level
      type: Enum[basic, developing, proficient, expert]
      required: true
      
    - name: items
      type: Set[String]
      required: false
      description: "Specific items this skill applies to"

type Certification:
  description: "A license or training certification"
  fields:
    - name: certification_type
      type: Enum[food_handler, food_manager, allergen_awareness, servsafe, first_aid, other]
      required: true
      
    - name: issued_date
      type: Date
      required: true
      
    - name: expiration_date
      type: Date
      required: true
      
    - name: issuing_authority
      type: String
      required: false
      
    - name: certification_number
      type: String
      required: false
```

**Role**

```yaml
data-structure: Role
description: "A function within the kitchen organization"
type-definition:
  fields:
    - name: role_id
      type: UUID
      required: true
      
    - name: name
      type: String
      required: true
      
    - name: description
      type: String
      required: false
      
    - name: responsibilities
      type: List[Responsibility]
      required: true
      
    - name: authorities
      type: Set[Authority]
      required: true
      
    - name: reports_to
      type: UUID
      required: false
      description: "Role this role reports to"
      
    - name: level
      type: Enum[leadership, senior, standard, support]
      required: true
```

**Team**

```yaml
data-structure: Team
description: "A group of people working together during a service period"
type-definition:
  fields:
    - name: team_id
      type: UUID
      required: true
      
    - name: name
      type: String
      required: true
      
    - name: service_period
      type: UUID
      required: true
      description: "Reference to service period this team covers"
      
    - name: members
      type: List[TeamMember]
      required: true
      
    - name: coverage_pattern
      type: CoveragePattern
      required: true
      
    - name: backup_relationships
      type: List[BackupRelationship]
      required: false

type TeamMember:
  description: "A person assigned to a team"
  fields:
    - name: person_id
      type: UUID
      required: true
      
    - name: role_id
      type: UUID
      required: true
      
    - name: station_assignment
      type: UUID
      required: false
      description: "Primary station this member works"
      
    - name: shift_start
      type: Time
      required: true
      
    - name: shift_end
      type: Time
      required: true
      
    - name: break_schedule
      type: BreakSchedule
      required: false

type BackupRelationship:
  description: "Who substitutes for whom"
  fields:
    - name: primary_id
      type: UUID
      description: "Person who may need backup"
      
    - name: backup_id
      type: UUID
      description: "Person who provides backup"
      
    - name: backup_level
      type: Enum[primary, secondary]
      required: true
      
    - name: station_scope
      type: Set[UUID]
      required: false
      description: "Stations this backup covers"
```

### 2.4 Process Entity Structures

**Workflow**

```yaml
data-structure: Workflow
description: "A complete daily workflow specification"
type-definition:
  fields:
    - name: workflow_id
      type: UUID
      required: true
      
    - name: name
      type: String
      required: true
      description: "Descriptive name (e.g., 'Friday Service Workflow')"
      
    - name: date
      type: Date
      required: true
      
    - name: kitchen_id
      type: UUID
      required: true
      
    - name: phases
      type: List[Phase]
      required: true
      description: "Major stages of operation"
      
    - name: station_configurations
      type: Map[UUID, StationConfiguration]
      required: true
      description: "Setup for each active station"
      
    - name: service_flow
      type: ServiceFlow
      required: true
      description: "How orders move through the kitchen"
      
    - name: staffing_plan
      type: StaffingPlan
      required: true
      
    - name: communication_protocols
      type: CommunicationProtocols
      required: true
      
    - name: adaptation_plans
      type: List[AdaptationPlan]
      required: false
      
    - name: generation_metadata
      type: GenerationMetadata
      required: true

type Phase:
  description: "A major stage of kitchen operation"
  fields:
    - name: phase_id
      type: UUID
      required: true
      
    - name: name
      type: String
      required: true
      
    - name: phase_type
      type: Enum[setup, pre_service_prep, service, break, close]
      required: true
      
    - name: start_time
      type: Time
      required: true
      
    - name: end_time
      type: Time
      required: true
      
    - name: activities
      type: List[Activity]
      required: true
      
    - name: dependencies
      type: List[PhaseDependency]
      required: false

type Activity:
  description: "A unit of work within a phase"
  fields:
    - name: activity_id
      type: UUID
      required: true
      
    - name: name
      type: String
      required: true
      
    - name: description
      type: String
      required: false
      
    - name: duration
      type: Duration
      required: true
      
    - name: scheduled_time
      type: Time
      required: true
      
    - name: location
      type: UUID
      required: true
      description: "Station or area where activity occurs"
      
    - name: assigned_staff
      type: Set[UUID]
      required: true
      
    - name: required_equipment
      type: Set[UUID]
      required: false
      
    - name: resources
      type: List[ResourceRequirement]
      required: false
      
    - name: dependencies
      type: Set[UUID]
      required: false
      description: "Activities that must complete before this one"
      
    - name: completion_criteria
      type: String
      required: false
      
    - name: task_breakdown
      type: List[Task]
      required: false

type Task:
  description: "An atomic unit of work assigned to a specific person"
  fields:
    - name: task_id
      type: UUID
      required: true
      
    - name: activity_id
      type: UUID
      required: true
      
    - name: assigned_to
      type: UUID
      required: true
      
    - name: description
      type: String
      required: true
      
    - name: deadline
      type: Time
      required: true
      
    - name: completion_status
      type: Enum[pending, in_progress, completed, blocked]
      required: true
      
    - name: completion_time
      type: Time
      required: false
      
    - name: notes
      type: String
      required: false
```

**ServiceFlow**

```yaml
data-structure: ServiceFlow
description: "How orders move through the kitchen during service"
type-definition:
  fields:
    - name: service_flow_id
      type: UUID
      required: true
      
    - name: phases
      type: List[ServicePhase]
      required: true
      description: "Distinct periods within service"
      
    - name: firing_sequence
      type: FiringSequence
      required: true
      description: "How items are timed for simultaneous completion"
      
    - name: handoff_protocols
      type: List[HandoffProtocol]
      required: true
      
    - name: expo_management
      type: ExpoProtocol
      required: true

type ServicePhase:
  description: "A distinct period within service"
  fields:
    - name: phase_id
      type: UUID
      required: true
      
    - name: name
      type: String
      required: true
      description: "e.g., 'Pre-Rush', 'Peak', 'Wind-Down'"
      
    - name: start_time
      type: Time
      required: true
      
    - name: end_time
      type: Time
      required: true
      
    - name: expected_volume
      type: VolumeEstimate
      required: true
      
    - name: staffing_adjustments
      type: List[StaffingAdjustment]
      required: false

type FiringSequence:
  description: "How items are timed for simultaneous completion"
  fields:
    - name: sequence_id
      type: UUID
      required: true
      
    - name: plate_time
      type: Time
      required: true
      description: "When plate must be complete"
      
    - name: component_firing_times
      type: Map[UUID, ComponentFiringTime]
      required: true
      description: "When each component must start"

type ComponentFiringTime:
  description: "When a component must be started"
  fields:
    - name: component_id
      type: UUID
      required: true
      
    - name: start_time
      type: Time
      required: true
      
    - name: station
      type: UUID
      required: true
      
    - name: assigned_staff
      type: UUID
      required: true
      
    - name: lead_time
      type: Duration
      required: true
      description: "Time from start to component ready"
```

**HandoffProtocol**

```yaml
data-structure: HandoffProtocol
description: "Procedure for transferring work or materials between stations"
type-definition:
  fields:
    - name: protocol_id
      type: UUID
      required: true
      
    - name: handoff_type
      type: Enum[component, order, information, responsibility]
      required: true
      
    - name: from_station
      type: UUID
      required: true
      
    - name: to_station
      type: UUID
      required: true
      
    - name: trigger
      type: HandoffTrigger
      required: true
      
    - name: timing_window
      type: TimingWindow
      required: false
      
    - name: communication_required
      type: List[CommunicationSpec]
      required: false
      
    - name: quality_check
      type: QualityCheckSpec
      required: false
      
    - name: fallback_procedure
      type: String
      required: false
      description: "What to do if handoff fails"

type HandoffTrigger:
  description: "What initiates the handoff"
  variant-type:
    - time_trigger:
        time: Time
        description: "Happens at specific time"
        
    - completion_trigger:
        activity_id: UUID
        description: "Happens when activity completes"
        
    - readiness_trigger:
        signal: String
        description: "Happens when ready signal received"
        
    - order_trigger:
        condition: String
        description: "Happens when order condition met"
```

### 2.5 Temporal Structures

**Time and Duration**

```yaml
data-structure: Time
description: "A point in the service day"
type-definition:
  fields:
    - name: hour
      type: Integer
      constraints: [0, 23]
      
    - name: minute
      type: Integer
      constraints: [0, 59]
      
    - name: second
      type: Integer
      constraints: [0, 59]
      default: 0
      
  methods:
    - add_duration(duration: Duration) → Time
    - subtract_duration(duration: Duration) → Time
    - time_until(other: Time) → Duration
    - is_before(other: Time) → Boolean
    - is_after(other: Time) → Boolean
    - format(format_string: String) → String

data-structure: Duration
description: "A span of time"
type-definition:
  fields:
    - name: minutes
      type: Integer
      description: "Total duration in minutes (can be negative)"
      
  constructors:
    - from_minutes(n: Integer) → Duration
    - from_seconds(n: Integer) → Duration
    - from_hours(h: Float) → Duration
      
  methods:
    - add(other: Duration) → Duration
    - subtract(other: Duration) → Duration
    - multiply(factor: Float) → Duration
    - total_seconds() → Integer
    - total_hours() → Float
    - is_longer_than(other: Duration) → Boolean
    - is_shorter_than(other: Duration) → Boolean
```

**Timing Specifications**

```yaml
data-structure: TimingWindow
description: "A constraint on when something can occur"
type-definition:
  fields:
    - name: earliest
      type: Time
      required: true
      
    - name: latest
      type: Time
      required: true
      
    - name: target
      type: Time
      required: false
      description: "Preferred time within window"
      
    - name: flexibility
      type: Duration
      required: false
      description: "How much deviation from target is acceptable"
      
  methods:
    - contains(time: Time) → Boolean
    - contains_range(start: Time, end: Time) → Boolean
    - overlaps(other: TimingWindow) → Boolean
    - intersection(other: TimingWindow) → TimingWindow

data-structure: Sequence
description: "An ordered list of activities with timing relationships"
type-definition:
  fields:
    - name: sequence_id
      type: UUID
      required: true
      
    - name: items
      type: List[SequenceItem]
      required: true
      
    - name: start_time
      type: Time
      required: false
      
  methods:
    - add_item(item: SequenceItem) → void
    - remove_item(item_id: UUID) → void
    - reorder(item_id: UUID, new_position: Integer) → void
    - calculate_end_time() → Time
    - validate() → ValidationResult

type SequenceItem:
  description: "An item in a sequence"
  fields:
    - name: item_id
      type: UUID
      required: true
      
    - name: scheduled_time
      type: Time
      required: true
      
    - name: duration
      type: Duration
      required: true
      
    - name: predecessor_id
      type: UUID
      required: false
      description: "Previous item in sequence"
```

### 2.6 Constraint Structures

**Base Constraint**

```yaml
data-structure: Constraint
description: "A restriction on what configurations are valid"
abstract: true
type-definition:
  fields:
    - name: constraint_id
      type: UUID
      required: true
      
    - name: name
      type: String
      required: true
      
    - name: description
      type: String
      required: false
      
    - name: constraint_type
      type: Enum[hard, soft]
      required: true
      
    - name: priority
      type: Integer
      constraints: [1, 100]
      default: 50
      
    - name: scope
      type: Set[String]
      required: false
      description: "What elements this constraint applies to"
      
    - name: source
      type: ConstraintSource
      required: true
      description: "Where constraint originates"
```

**Physical Constraints**

```yaml
data-structure: PhysicalConstraint
extends: Constraint
description: "Constraints based on physical reality"
type-definition:
  fields:
    - name: constraint_category
      type: Enum[spatial, capacity, temporal]
      required: true
      
    - name: specification
      type: PhysicalSpec
      required: true

type PhysicalSpec:
  description: "Specification for physical constraints"
  variant-type:
    - spatial_spec:
        dimension: String  # e.g., "width", "height", "distance"
        min_value: Float
        max_value: Float
        unit: String  # e.g., "inches", "feet"
        
    - capacity_spec:
        resource_type: String  # e.g., "equipment", "station", "storage"
        resource_id: UUID
        max_quantity: Integer
        measurement: String  # e.g., "items", "pans", "liters"
        
   