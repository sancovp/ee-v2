# The Copper Beech Daily Workflow Constructor

## Domain-Specific Language: Internal Vocabulary, Data Structures, and Operations

### Position: L0P2W[0](3) — Conceptualize · Generally Reify (How MAKE) · DSL

---

## 1. Purpose of This Artifact

While the Abstract Goal (L0P2W[0](0)) established *why we build the Constructor*, the Systems Design (L0P2W[0](1)) established *what the system must achieve*, and the Systems Architecture (L0P2W[0](2)) established *how components work together*, this artifact examines *the internal language through which the system operates*. We define the vocabulary, data structures, and operations that constitute the Constructor's domain-specific language—the medium through which knowledge is expressed, workflows are generated, and feedback is captured.

The question here is: "What words does the Constructor speak? What do those words mean? How are they combined to express domain knowledge?"

This artifact serves as the definitive reference for the Constructor's internal language, providing the formal specifications that guide implementation and ensure consistency across all system components.

---

## 2. Foundational Vocabulary

The Constructor operates with a defined vocabulary of terms, each with a specific meaning and usage. This vocabulary constitutes the fundamental lexicon of the domain-specific language.

### 2.1 Entity Terms

These terms refer to things that exist independently within the domain.

#### 2.1.1 CONSTRUCTOR

**Term**: `CONSTRUCTOR`

**Definition**: The complete system apparatus that generates daily workflow instances from configurations, incorporates feedback, and improves through learning.

**Usage**: Refers to the entire system in its current state, including all knowledge structures, processing components, and interface components.

**Synonyms**: System, apparatus, engine

**Example**:
```
The CONSTRUCTOR generated copper_beech_2025-03-18_daily at 21:15.
```

#### 2.1.2 WORKFLOW_INSTANCE

**Term**: `WORKFLOW_INSTANCE`

**Definition**: A specific, unrepeatable, time-bound execution plan generated for a particular day at Copper Beech Cafe.

**Identifier Format**: `copper_beech_YYYY-MM-DD_daily`

**Properties**:
- Unique to its generation date
- Contains complete task definitions, assignments, and timing
- Archived after execution
- Never modified after generation

**Example**:
```
WORKFLOW_INSTANCE::copper_beech_2025-03-18_daily {
  date: 2025-03-18
  generated_at: 2025-03-17T21:15:00Z
  phases: [opening, early_service, peak_service, lunch_transition, lunch_service, closing]
  task_count: 47
  constraint_satisfaction: 100%
}
```

#### 2.1.3 TASK_PATTERN

**Term**: `TASK_PATTERN`

**Definition**: A reusable template encoding an atomic unit of work with defined inputs, outputs, duration, and assignment criteria.

**Identifier Format**: `TP_###` (e.g., `TP_001`, `TP_047`)

**Properties**:
- Versioned for change tracking
- Referenced by workflow patterns
- Instantiated into specific task instances within workflows
- Contains role requirements, not specific staff assignments

**Example**:
```
TASK_PATTERN::TP_001 {
  name: "Standard Egg Prep"
  duration: 15
  assigned_roles: [prep_cook]
  inputs: [eggs, butter, seasoning]
  outputs: [prepped_eggs]
  dependencies: []
  color_board: green
  category: prep
  version: 1
}
```

#### 2.1.4 WORKFLOW_PATTERN

**Term**: `WORKFLOW_PATTERN`

**Definition**: A reusable template encoding a complete operational sequence (opening, service phase, or closing) that can be instantiated for specific days.

**Identifier Format**: `WP_###` (e.g., `WP_001`, `WP_012`)

**Properties**:
- References task patterns by ID
- Defines temporal structure
- Specifies applicable volume tiers and day types
- Organized by type: opening, service, closing

**Example**:
```
WORKFLOW_PATTERN::WP_001 {
  name: "Standard Opening Sequence"
  type: opening
  task_sequence: [
    {task_id: TP_XXX, start: "5:30"},
    {task_id: TP_YYY, start: "5:45"}
  ]
  phases: [preheat, inventory, production, setup, final]
  applicable_volume_tiers: [low, medium, high]
  version: 1
}
```

#### 2.1.5 PROTOCOL

**Term**: `PROTOCOL`

**Definition**: A triggered response procedure activated by specific conditions that modifies workflow generation or execution.

**Identifier Format**: `AP_###` (e.g., `AP_001`, `AP_008`)

**Properties**:
- Has trigger conditions (threshold, time, state_change)
- Has defined response actions
- Can be standing (always active) or conditional
- Logged when activated for feedback purposes

**Example**:
```
PROTOCOL::AP_001 {
  name: "High Volume Response"
  trigger: {
    type: threshold
    condition: "tickets_in_queue > 8"
  }
  response_actions: [
    {type: reassign, from: James, to: Maria, task_category: griddle},
    {type: accelerate, phase: peak_service, factor: 1.2}
  ]
  standing: false
  version: 1
}
```

#### 2.1.6 CONSTRAINT

**Term**: `CONSTRAINT`

**Definition**: A condition that valid workflow outputs must satisfy, defining the boundary of acceptable generation.

**Identifier Format**: `HC_###` (hard) or `SC_###` (soft)

**Properties**:
- Hard constraints are invariant (HC_001-HC_004)
- Soft constraints are optimizable targets (SC_001+)
- Hard constraints cannot be overridden
- Soft constraints have target values

**Example**:
```
CONSTRAINT::HC_001 {
  name: "Food Safety Temperature Control"
  definition: "Food must not remain in danger zone (40°F-140°F) for more than 2 hours cumulative"
  enforcement: invariant
  verification_method: time_temperature_tracking
}
```

#### 2.1.7 STAFF_PROFILE

**Term**: `STAFF_PROFILE`

**Definition**: A structured representation of a person's role, capabilities, typical assignments, and learning record at Copper Beech Cafe.

**Identifier Format**: Name string (e.g., `Maria`, `James`, `Elena`, `Marcus`)

**Properties**:
- Contains role, certifications, strengths
- References typical task pattern assignments
- Includes learning record with observations and adjustments
- Updated through knowledge integration

**Example**:
```
STAFF_PROFILE::Maria {
  role: chef
  certifications: [food_safety_manager, allergen_aware]
  strengths: [all_stations, quality_control, problem_resolution]
  typical_assignments: [TP_005, hollandaise, final_quality_check]
  learning_record: [
    {
      date: 2024-11-15
      observation: "Saturday peak timing consistently earlier than expected"
      adjustment: "Shifted peak_service start to 8:45 from 9:00"
    }
  ]
}
```

#### 2.1.8 MENU_ITEM

**Term**: `MENU_ITEM`

**Definition**: A producible food item on the Copper Beech Cafe menu with defined components, cooking methods, timing, and allergen flags.

**Identifier Format**: `BI_###` (breakfast) or `LI_###` (lunch)

**Properties**:
- Belongs to a menu category
- Specifies components, equipment, and timing
- Includes allergen flags
- Referenced by task patterns

**Example**:
```
MENU_ITEM::BI_001 {
  name: "Eggs Any Style"
  category: eggs
  components: [eggs, butter, seasoning]
  cooking_method: pan
  typical_duration: 8
  allergen_flags: [dairy]
  equipment_requirements: [burner, pan]
}
```

### 2.2 Event Terms

These terms refer to occurrences that happen within the domain.

#### 2.2.1 GENERATION

**Term**: `GENERATION`

**Definition**: The event of creating a workflow instance from a configuration.

**Properties**:
- Has timestamp (generated_at)
- Has configuration inputs
- Has constraint verification status
- Produces a workflow instance

**Example**:
```
GENERATION::copper_beech_2025-03-18_daily {
  timestamp: 2025-03-17T21:15:00Z
  configuration_id: copper_beech_2025-03-18_config
  status: successful
  constraint_satisfaction: 100%
}
```

#### 2.2.2 EXECUTION

**Term**: `EXECUTION`

**Definition**: The event of carrying out a workflow instance during operational hours.

**Properties**:
- Has start and end timestamps
- Produces execution metrics
- May include adaptations
- Generates feedback

**Example**:
```
EXECUTION::copper_beech_2025-03-18_daily {
  workflow_instance: copper_beech_2025-03-18_daily
  start: 2025-03-18T05:30:00Z
  end: 2025-03-18T15:00:00Z
  service_start: 2025-03-18T07:00:00Z
  service_end: 2025-03-18T14:00:00Z
  adaptations: [AP_001]
}
```

#### 2.2.3 ADAPTATION

**Term**: `ADAPTATION`

**Definition**: A modification to workflow generation or execution made in response to triggered conditions.

**Properties**:
- Linked to a specific protocol activation
- Records what was modified
- Includes rationale
- Captured for feedback

**Example**:
```
ADAPTATION::A_2025-03-18_001 {
  protocol_id: AP_001
  activated_at: 2025-03-18T09:15:00Z
  modifications: [
    {type: reassign, task: ST_001, from: James, to: Maria},
    {type: timing_change, phase: peak_service, new_start: "8:45"}
  ]
  reason: "tickets_in_queue exceeded threshold (10 > 8)"
}
```

#### 2.2.4 FEEDBACK

**Term**: `FEEDBACK`

**Definition**: Information about workflow execution that is captured and stored for learning purposes.

**Properties**:
- Has source (automated, Maria, staff)
- Has timestamp
- Has content and significance
- Stored in feedback archive

**Example**:
```
FEEDBACK::F_2025-03-18_001 {
  date: 2025-03-18
  source: maria_review
  rating: 4
  what_went_well: "Peak service handled well despite volume"
  what_could_improve: "Lunch transition could be smoother"
  captured_at: 2025-03-18T15:30:00Z
}
```

### 2.3 Relationship Terms

These terms express connections between entities and events.

#### 2.3.1 GENERATES

**Term**: `GENERATES`

**Definition**: The relationship between a configuration and the workflow instance it produces.

**Syntax**: `CONFIGURATION --GENERATES--> WORKFLOW_INSTANCE`

**Example**:
```
copper_beech_2025-03-18_config --GENERATES--> copper_beech_2025-03-18_daily
```

#### 2.3.2 INSTANTIATES

**Term**: `INSTANTIATES`

**Definition**: The relationship between a pattern and the tasks or workflows it produces when used in generation.

**Syntax**: `PATTERN --INSTANTIATES--> INSTANCE`

**Example**:
```
WP_001::Standard Opening Sequence --INSTANTIATES--> opening_section
TP_001::Standard Egg Prep --INSTANTIATES--> OT_004
```

#### 2.3.3 CONSTRAINS

**Term**: `CONSTRAINS`

**Definition**: The relationship between a constraint and the elements it limits.

**Syntax**: `CONSTRAINT --CONSTRAINS--> ELEMENT`

**Example**:
```
HC_001::Food Safety Temperature Control --CONSTRAINS--> workflow
HC_001 --CONSTRAINS--> task[prep_items]
```

#### 2.3.4 ACTIVATES

**Term**: `ACTIVATES`

**Definition**: The relationship between a trigger condition and the protocol it activates.

**Syntax**: `CONDITION --ACTIVATES--> PROTOCOL`

**Example**:
```
tickets_in_queue: 10 (> 8 threshold) --ACTIVATES--> AP_001::High Volume Response
```

#### 2.3.5 MODIFIES

**Term**: `MODIFIES`

**Definition**: The relationship between a protocol/adaptation and the workflow it changes.

**Syntax**: `PROTOCOL --MODIFIES--> WORKFLOW`

**Example**:
```
AP_001::High Volume Response --MODIFIES--> peak_service_phase
```

#### 2.3.6 ENABLES

**Term**: `ENABLES`

**Definition**: The relationship between equipment and the tasks it makes possible.

**Syntax**: `EQUIPMENT --ENABLES--> TASK`

**Example**:
```
GRIDDLE_1::Main Griddle --ENABLES--> ST_001::Execute Egg Order
```

---

## 3. Type System

The Constructor's domain-specific language employs a strict type system that ensures consistency and enables validation.

### 3.1 Primitive Types

#### 3.1.1 IDENTIFIER

**Type**: `IDENTIFIER`

**Definition**: A unique string that names an entity within the system.

**Format Rules**:
- Alphanumeric characters and underscores only
- Maximum 64 characters
- Case-sensitive
- Must be unique within its namespace

**Examples**:
```
Maria
TP_001
copper_beech_2025-03-18_daily
```

#### 3.1.2 TIMESTAMP

**Type**: `TIMESTAMP`

**Definition**: An ISO 8601 formatted date-time indicating when something occurred or should occur.

**Format**: `YYYY-MM-DDTHH:MM:SSZ` (UTC) or `YYYY-MM-DDTHH:MM:00` (local)

**Examples**:
```
2025-03-18T05:30:00Z
2025-03-18T21:15:00Z
```

#### 3.1.3 TIME_VALUE

**Type**: `TIME_VALUE`

**Definition**: A time of day expressed in 24-hour format.

**Format**: `HH:MM`

**Range**: `00:00` to `23:59`

**Examples**:
```
05:30
14:00
```

#### 3.1.4 DURATION

**Type**: `DURATION`

**Definition**: A length of time expressed in minutes.

**Format**: Integer (minutes)

**Range**: 1 to 480 (8 hours)

**Examples**:
```
15
120
30
```

#### 3.1.5 ENUMERATED VALUES

**Type**: Various enumerated types

**Definition**: Fixed sets of allowed values for specific attributes.

| Type Name | Allowed Values |
|-----------|---------------|
| `DAY_OF_WEEK` | Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday |
| `VOLUME_TIER` | low, medium, high, extreme |
| `WEATHER_INDICATOR` | clear, rainy, cold, hot |
| `WEATHER_IMPACT` | none, moderate, significant |
| `ROLE` | chef, line_cook, prep_cook, support |
| `ALLERGEN_FLAG` | dairy, eggs, gluten, soy, nuts, shellfish |
| `COLOR_BOARD` | green, red, yellow, blue |
| `TASK_CATEGORY` | prep, service, closing, support |
| `PHASE_TYPE` | opening, early_service, peak_service, lunch_transition, lunch_service, closing |
| `RATING` | 1, 2, 3, 4, 5 |
| `SIGNIFICANCE` | low, medium, high |
| `CONSTRAINT_STATUS` | satisfied, violated, at_risk |
| `WORKFLOW_STATUS` | pending_execution, executing, completed, archived |
| `HYPOTHESIS_STATUS` | pending, validated, rejected |
| `REVIEW_STATUS` | pending, approved, denied |

### 3.2 Composite Types

#### 3.2.1 VOLUME_RANGE

**Type**: `VOLUME_RANGE`

**Definition**: An expected range of ticket volume.

**Structure**:
```typescript
type VOLUME_RANGE = {
  min: number;      // Minimum expected tickets
  max: number;      // Maximum expected tickets
}
```

**Constraints**: `min >= 0` and `max >= min`

**Example**:
```yaml
breakfast_tickets:
  min: 25
  max: 35
```

#### 3.2.2 TIME_WINDOW

**Type**: `TIME_WINDOW`

**Definition**: A bounded period of time with start and end.

**Structure**:
```typescript
type TIME_WINDOW = {
  start: TIME_VALUE;
  end: TIME_VALUE;
}
```

**Constraints**: `start < end`

**Example**:
```yaml
window:
  start: "07:00"
  end: "09:00"
```

#### 3.2.3 ASSIGNMENT

**Type**: `ASSIGNMENT`

**Definition**: The association of a task with a staff member.

**Structure**:
```typescript
type ASSIGNMENT = {
  task_id: IDENTIFIER;
  assigned_to: IDENTIFIER;     // Staff member name
  role_required: ROLE;
  assigned_at: TIMESTAMP;
  assignment_rationale: string;
}
```

**Example**:
```yaml
assignment:
  task_id: "OT_007"
  assigned_to: "Maria"
  role_required: "chef"
  assigned_at: "2025-03-17T21:15:00Z"
  assignment_rationale: "Maria strengths: quality_control, all_stations"
```

#### 3.2.4 TASK_INSTANCE

**Type**: `TASK_INSTANCE`

**Definition**: A specific occurrence of a task within a workflow instance.

**Structure**:
```typescript
type TASK_INSTANCE = {
  task_id: IDENTIFIER;         // e.g., "OT_001", "ST_001"
  pattern_reference?: IDENTIFIER;  // e.g., "TP_001" if instantiated from pattern
  time: TIME_VALUE;
  name: string;
  duration: DURATION;
  assigned_to: IDENTIFIER;
  role_required: ROLE;
  equipment_used: IDENTIFIER[];
  inputs: string[];
  outputs: string[];
  procedure: string[];
  success_criteria: string[];
  dependencies: IDENTIFIER[];
  color_board?: COLOR_BOARD;
  allergen_flags?: ALLERGEN_FLAG[];
  notes?: string;
}
```

#### 3.2.5 PHASE

**Type**: `PHASE`

**Definition**: A grouping of tasks representing a distinct operational stage.

**Structure**:
```typescript
type PHASE = {
  phase_id: IDENTIFIER;
  name: string;
  phase_type: PHASE_TYPE;
  start_time: TIME_VALUE;
  end_time: TIME_VALUE;
  duration: DURATION;
  expected_volume: {
    tickets_min: number;
    tickets_max: number;
    tier: VOLUME_TIER;
  };
  protocols_active: IDENTIFIER[];
  tasks: TASK_INSTANCE[];
  adaptation_triggers?: ADAPTATION_TRIGGER[];
  service_targets?: {
    average_ticket_time: DURATION;
    sla_target: DURATION;
    max_queue_depth?: number;
  };
  notes?: string;
}
```

#### 3.2.6 CONSTRAINT_VIOLATION

**Type**: `CONSTRAINT_VIOLATION`

**Definition**: A record of a constraint not being satisfied.

**Structure**:
```typescript
type CONSTRAINT_VIOLATION = {
  constraint_id: IDENTIFIER;
  element: string;
  description: string;
  severity: 'critical' | 'major' | 'minor';
  remediation?: string;
}
```

---

## 4. Data Structure Schemas

These schemas define the structure of all persistent and transient data within the Constructor system.

### 4.1 Knowledge Structure Schemas

#### 4.1.1 Pattern Library Schema

```yaml
pattern_library:
  version: string
  last_modified: TIMESTAMP
  
  task_patterns:
    type: array
    items:
      type: object
      required: [id, version, name, duration, assigned_roles, category, created]
      properties:
        id:
          type: IDENTIFIER
          pattern: "^TP_\\d{3}$"
        version:
          type: integer
          minimum: 1
        name:
          type: string
          maxLength: 100
        duration:
          type: DURATION
        assigned_roles:
          type: array
          items:
            type: ROLE
        inputs:
          type: array
          items:
            type: string
        outputs:
          type: array
          items:
            type: string
        dependencies:
          type: array
          items:
            type: IDENTIFIER
        color_board:
          type: COLOR_BOARD
        allergen_flags:
          type: array
          items:
            type: ALLERGEN_FLAG
        category:
          type: TASK_CATEGORY
        created:
          type: TIMESTAMP
        modified:
          type: TIMESTAMP
  
  workflow_patterns:
    type: array
    items:
      type: object
      required: [id, version, name, type, task_sequence, created]
      properties:
        id:
          type: IDENTIFIER
          pattern: "^WP_\\d{3}$"
        version:
          type: integer
        name:
          type: string
        type:
          type: enum
          values: [opening, service, closing]
        task_sequence:
          type: array
          items:
            type: object
            properties:
              task_id:
                type: IDENTIFIER
              sequence_order:
                type: integer
              start_time:
                type: TIME_VALUE
        phases:
          type: array
          items:
            type: string
        applicable_volume_tiers:
          type: array
          items:
            type: VOLUME_TIER
        applicable_day_types:
          type: array
          items:
            type: string
        created:
          type: TIMESTAMP
        modified:
          type: TIMESTAMP
```

#### 4.1.2 Constraints Schema

```yaml
constraints:
  hard:
    type: array
    items:
      type: object
      required: [id, name, definition, enforcement, verification_method]
      properties:
        id:
          type: IDENTIFIER
          pattern: "^HC_\\d{3}$"
        name:
          type: string
        definition:
          type: string
        enforcement:
          type: string
          const: "invariant"
        verification_method:
          type: string
        parameters:
          type: object
  
  soft:
    type: array
    items:
      type: object
      required: [id, name, definition, target, unit, enforcement]
      properties:
        id:
          type: IDENTIFIER
          pattern: "^SC_\\d{3}$"
        name:
          type: string
        definition:
          type: string
        target:
          type: number
        unit:
          type: string
        enforcement:
          type: string
          const: "optimize"
```

#### 4.1.3 Protocols Schema

```yaml
protocols:
  type: array
  items:
    type: object
    required: [id, version, name, trigger, response_actions, standing]
    properties:
      id:
        type: IDENTIFIER
        pattern: "^AP_\\d{3}$"
      version:
        type: integer
      name:
        type: string
      trigger:
        type: object
        required: [type, condition]
        properties:
          type:
            type: enum
            values: [threshold, time, state_change]
          condition:
            type: string
          metric:
            type: string
          operator:
            type: enum
            values: [">", "<", ">=", "<=", "==", "!="]
          value:
            oneOf:
              - type: number
              - type: string
      response_actions:
        type: array
        items:
          type: object
          properties:
            type:
              type: enum
              values: [reassign, accelerate, insert_task, remove_task, notify]
            from:
              type: IDENTIFIER
            to:
              type: IDENTIFIER
            task_category:
              type: string
            phase:
              type: string
            factor:
              type: number
      standing:
        type: boolean
      created:
        type: TIMESTAMP
      modified:
        type: TIMESTAMP
```

#### 4.1.4 Staff Profiles Schema

```yaml
staff_profiles:
  type: array
  items:
    type: object
    required: [name, role, created]
    properties:
      name:
        type: string
      role:
        type: ROLE
      certifications:
        type: array
        items:
          type: string
      strengths:
        type: array
        items:
          type: string
      typical_assignments:
        type: array
        items:
          type: string
      learning_record:
        type: array
        items:
          type: object
          properties:
            date:
              type: DATE
            observation:
              type: string
            adjustment:
              type: string
            approved_by:
              type: string
      created:
        type: TIMESTAMP
      modified:
        type: TIMESTAMP
```

#### 4.1.5 Menu Knowledge Schema

```yaml
menu_knowledge:
  version: string
  last_modified: TIMESTAMP
  
  breakfast_items:
    type: array
    items:
      type: object
      required: [id, name, category, components, cooking_method, typical_duration]
      properties:
        id:
          type: IDENTIFIER
          pattern: "^BI_\\d{3}$"
        name:
          type: string
        category:
          type: string
        components:
          type: array
          items:
            type: string
        cooking_method:
          type: string
        typical_duration:
          type: DURATION
        allergen_flags:
          type: array
          items:
            type: ALLERGEN_FLAG
        equipment_requirements:
          type: array
          items:
            type: string
  
  lunch_items:
    type: array
    items:
      type: object
      required: [id, name, category, components, cooking_method, typical_duration]
      # Same structure as breakfast_items with id pattern "^LI_\\d{3}$"
  
  category_specs:
    type: object
    additionalProperties:
      type: object
      properties:
        temperature_range:
          type: string
        timing_notes:
          type: string
        common_allergens:
          type: array
          items:
            type: ALLERGEN_FLAG
```

### 4.2 Instance Structure Schemas

#### 4.2.1 Configuration Schema

```yaml
daily_configuration:
  type: object
  required: [configuration_id, date, day_of_week, daily_context, staff_configuration]
  properties:
    configuration_id:
      type: IDENTIFIER
      pattern: "^copper_beech_\\d{4}-\\d{2}-\\d{2}_config$"
    date:
      type: string
      format: date
    day_of_week:
      type: DAY_OF_WEEK
    daily_context:
      type: object
      required: [expected_volume]
      properties:
        expected_volume:
          type: object
          required: [breakfast_tickets, lunch_tickets, volume_tier]
          properties:
            breakfast_tickets:
              type: VOLUME_RANGE
            lunch_tickets:
              type: VOLUME_RANGE
            volume_tier:
              type: VOLUME_TIER
            notes:
              type: string
        weather_indicator:
          type: WEATHER_INDICATOR
        weather_impact:
          type: WEATHER_IMPACT
        special_events:
          type: array
          items:
            type: object
        reservation_notes:
          type: string
        operational_notes:
          type: string
    staff_configuration:
      type: object
      required: [scheduled]
      properties:
        scheduled:
          type: array
          items:
            type: object
            required: [name, role, start_time]
            properties:
              name:
                type: string
              role:
                type: ROLE
              start_time:
                type: TIME_VALUE
              certifications:
                type: array
              strengths:
                type: array
              availability:
                type: string
        expected_changes:
          type: array
    inventory_configuration:
      type: object
      properties:
        previous_night_delivery:
          type: boolean
        notable_items:
          type: array
        low_stock_alerts:
          type: array
        substitutions_available:
          type: object
    equipment_configuration:
      type: object
      properties:
        available:
          type: array
        issues:
          type: array
```

#### 4.2.2 Workflow Instance Schema

```yaml
daily_workflow_instance:
  type: object
  required: [instance_id, date, generated_at, configuration_summary]
  properties:
    instance_id:
      type: IDENTIFIER
      pattern: "^copper_beech_\\d{4}-\\d{2}-\\d{2}_daily$"
    date:
      type: string
      format: date
    generated_at:
      type: TIMESTAMP
    generated_by:
      type: string
    configuration_summary:
      type: object
      properties:
        expected_volume:
          type: string
        staff_count:
          type: integer
        weather:
          type: string
        special_events:
          type: array
        key_notes:
          type: array
    hard_constraint_verification:
      type: object
      properties:
        HC_001:
          type: CONSTRAINT_STATUS
          details:
            type: string
        HC_002:
          type: CONSTRAINT_STATUS
          details:
            type: string
        HC_003:
          type: CONSTRAINT_STATUS
          details:
            type: string
        HC_004:
          type: CONSTRAINT_STATUS
          details:
            type: string
    opening_section:
      type: object
      properties:
        section_id:
          type: IDENTIFIER
        target_completion:
          type: TIME_VALUE
        tasks:
          type: array
          items:
            type: TASK_INSTANCE
    service_section:
      type: object
      properties:
        section_id:
          type: IDENTIFIER
        target_start:
          type: TIME_VALUE
        target_end:
          type: TIME_VALUE
        phases:
          type: array
          items:
            type: PHASE
    closing_section:
      type: object
      properties:
        section_id:
          type: IDENTIFIER
        target_completion:
          type: TIME_VALUE
        tasks:
          type: array
          items:
            type: TASK_INSTANCE
    adaptation_protocols:
      type: object
      properties:
        standing:
          type: array
          items:
            type: PROTOCOL
        conditional:
          type: array
          items:
            type: PROTOCOL
    execution_log_template:
      type: object
      properties:
        instance_id:
          type: IDENTIFIER
        log_id:
          type: IDENTIFIER
        metrics_to_capture:
          type: array
```

### 4.3 Feedback Structure Schemas

#### 4.3.1 Daily Review Schema

```sql
CREATE TABLE daily_reviews (
  id INTEGER PRIMARY KEY,
  date DATE NOT NULL UNIQUE,
  reviewer TEXT NOT NULL,
  rating INTEGER CHECK(rating >= 1 AND rating <= 5),
  what_went_well TEXT,
  what_could_improve TEXT,
  specific_observations TEXT,
  adjustment_recommendations TEXT,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

#### 4.3.2 Staff Observation Schema

```sql
CREATE TABLE staff_observations (
  id INTEGER PRIMARY KEY,
  date DATE NOT NULL,
  staff_member TEXT NOT NULL,
  observation_type TEXT CHECK(observation_type IN ('positive', 'negative', 'suggestion')),
  content TEXT NOT NULL,
  significance TEXT CHECK(significance IN ('low', 'medium', 'high')),
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (date) REFERENCES daily_reviews(date)
);
```

#### 4.3.3 Automated Metrics Schema

```sql
CREATE TABLE automated_metrics (
  id INTEGER PRIMARY KEY,
  date DATE NOT NULL UNIQUE,
  ticket_times JSON,
  sla_compliance REAL,
  protocol_activations JSON,
  volume_actual JSON,
  adaptation_made JSON,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

#### 4.3.4 Hypothesis Schema

```sql
CREATE TABLE hypotheses (
  id TEXT PRIMARY KEY,
  generated_date DATE NOT NULL,
  source TEXT,
  description TEXT,
  proposed_change JSON,
  evidence JSON,
  validation_status TEXT CHECK(validation_status IN ('pending', 'validated', 'rejected')),
  review_status TEXT CHECK(review_status IN ('pending', 'approved', 'denied')),
  reviewed_by TEXT,
  review_date DATE,
  review_notes TEXT,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

#### 4.3.5 Knowledge Change Schema

```sql
CREATE TABLE knowledge_changes (
  id TEXT PRIMARY KEY,
  hypothesis_id TEXT,
  integration_date DATE NOT NULL,
  structure_changed TEXT,
  element_id TEXT,
  field_changed TEXT,
  previous_value TEXT,
  new_value TEXT,
  approved_by TEXT,
  effective_date DATE,
  rollback_available BOOLEAN DEFAULT TRUE,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (hypothesis_id) REFERENCES hypotheses(id)
);
```

---

## 5. Operation Definitions

The Constructor's domain-specific language defines operations—actions that transform inputs into outputs. Each operation has a defined signature, preconditions, and postconditions.

### 5.1 Configuration Operations

#### 5.1.1 PARSE_CONFIGURATION

**Operation**: `PARSE_CONFIGURATION(raw_yaml: string) → ParseResult`

**Definition**: Transform raw YAML configuration content into a validated, normalized configuration object.

**Parameters**:
- `raw_yaml`: Raw YAML string from configuration file

**Returns**:
```typescript
type ParseResult = {
  success: boolean;
  configuration?: ValidatedConfiguration;
  errors: ParseError[];
  warnings: ParseWarning[];
}
```

**Preconditions**:
- `raw_yaml` must be non-empty string

**Postconditions**:
- If `success` is true, `configuration` contains validated configuration
- All `errors` must be resolved before proceeding
- `warnings` are advisory but do not block processing

**Example**:
```typescript
const result = PARSE_CONFIGURATION(yamlContent);
if (result.success) {
  proceedWithGeneration(result.configuration);
} else {
  reportErrors(result.errors);
}
```

#### 5.1.2 VALIDATE_CONFIGURATION

**Operation**: `VALIDATE_CONFIGURATION(configuration: RawConfiguration) → ValidationResult`

**Definition**: Check that a configuration contains all required fields and valid values.

**Parameters**:
- `configuration`: Configuration object to validate

**Returns**:
```typescript
type ValidationResult = {
  isValid: boolean;
  errors: ValidationError[];
  warnings: ValidationWarning[];
}
```

**Validation Rules**:
- Required fields present: date, day_of_week, daily_context, staff