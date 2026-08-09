# The Copper Beech Workflow DSL

## A Concrete Domain-Specific Language for Daily Kitchen Workflow Generation

---

## Part I: Introduction — From Conceptual Vocabulary to Operational Language

### 1.1 The Purpose of This Artifact

This artifact transforms the abstract conceptual vocabulary established in L1P1 into a concrete, operational domain-specific language (DSL) for CopperBeech-WorkflowGen. Where L1P1 articulated the universal concepts of kitchen workflow generation, this artifact specifies how those concepts are *expressed* in the specific context of Copper Beech Bistro—how they are written, configured, and used in generating daily workflow instances.

The DSL presented here is not a programming language but a structured specification language: a set of terms, syntaxes, and conventions that practitioners and systems use to describe, generate, and execute daily kitchen workflows. It is the *native tongue* of CopperBeech-WorkflowGen—the medium through which the system thinks, communicates, and controls.

### 1.2 What the DSL Accomplishes

The Copper Beech Workflow DSL serves three primary purposes:

**Specification**: The DSL provides a standardized way to specify all aspects of a daily workflow—from staffing assignments to timing windows, from station configurations to communication protocols. Any workflow specified in this DSL is complete, unambiguous, and executable.

**Generation**: The DSL is the output language of CopperBeech-WorkflowGen. The synthesis engine produces workflow instances in this DSL, and practitioners read those instances using this DSL's vocabulary and structure.

**Communication**: The DSL provides a shared language for all stakeholders—executive chef, sous chef, line cooks, prep cooks, and support staff—to understand and discuss workflow specifications.

### 1.3 The Relationship to Prior Artifacts

This artifact builds upon the foundational work of L1P1:

- **From L1P1/0-abstractgoal.md**: The essential ontology of workflow generation systems—what they are and what they do
- **From L1P1/1-systemsdesign.md**: The stakeholder context and generative grammar that constitute the system's identity
- **From L1P1/2-systemsarchitecture.md**: The essential architecture—functions, structures, and relationships
- **From L1P1/3-dsl.md**: The general domain-specific language vocabulary and grammar
- **From L1P1/4-topology.md**: The natural structure of the conceptual network
- **From L1P1/5-engineeredsystem.md**: The Copper Beech exemplar demonstrating system coherence
- **From L1P1/6-feedbackloop.md**: The feedback loop architecture for continuous improvement

This artifact takes these conceptual foundations and makes them *operational*—specifying not merely what concepts exist but how they are expressed in the Copper Beech context.

---

## Part II: The Concrete Vocabulary

### 2.1 Kitchen Entity Expressions

The DSL provides specific expressions for all kitchen entities in the Copper Beech context.

#### 2.1.1 Staff Expressions

Staff are referenced using role-based identifiers:

```yaml
# Staff Reference Format
staff-ref: <role>.<day-suffix>

# Examples
maria.executive      # Maria, in executive chef role
david.sous            # David, in sous chef role
elena.line            # Elena, on line
james.prep            # James, on prep
sophie.prep           # Sophie, on prep
tyler.support         # Tyler, in support role

# With temporal qualifier
staff-ref: <role>.<day-suffix>.<time-qualifier>
# Examples
maria.executive.evening    # Maria, evening executive shift
david.sous.early           # David, early arrival
elena.line.service         # Elena, during service period
```

**Staff Skill Expressions**

```yaml
# Skill Level Syntax
skill-expression: <person>.<domain>.<level>
# Levels: expert, proficient, developing, basic

# Examples
elena.grill.expert           # Elena is expert at grill
sophie.sauce.proficient      # Sophie is proficient at sauce-making
james.vegetable.expert       # James is expert at vegetable prep
david.hotline.expert         # David is expert at hot line

# Skill Requirement Syntax
skill-requirement: <domain>.<level> [for <station>]
# Examples
grill.expert for grill-station
sauté.proficient for sauté-station
cold-prep.basic for cold-station
```

**Staff Availability Expressions**

```yaml
# Availability Window Syntax
availability-expression: <person>.<day-pattern>.<time-range>

# Day Patterns
tuesday-saturday    # Specific day
weekdays            # Monday through Friday
weekends            # Saturday and Sunday
daily               # All days

# Time Ranges (24-hour format)
09:00-17:00         # Standard daytime
14:00-22:00         # Afternoon to evening
16:00-22:00         # Evening only

# Examples
maria.tuesday-saturday.15:00-22:00
david.wednesday-sunday.14:00-22:00
elena.tuesday-saturday.16:00-22:00
james.daily.13:00-21:00
```

**Staffing Assignment Expressions**

```yaml
# Station Assignment Syntax
assignment: <person> → <station> @ <time-range>

# Examples
elena → grill @ 17:00-22:00
david → sauté @ 17:00-22:00
james → cold-prep @ 16:00-21:00
sophie → protein-prep @ 16:00-21:00
maria → expo @ 17:30-21:30

# Break Coverage Syntax
break-coverage: <person-on-break> @ <break-time> covered by <coverage-person>

# Examples
james @ 18:30-18:45 covered by sophie
elena @ 18:30-18:45 covered by tyler
```

#### 2.1.2 Equipment Expressions

Equipment is referenced by functional type with location qualifier:

```yaml
# Equipment Reference Format
equipment-ref: <equipment-type>[.<location>]

# Equipment Types (Copper Beech Specific)
range-4burner       # 4-burner range (hot line)
grill-flatop        # Flat-top grill (hot line, end)
fryer-deep          # Deep fryer (hot line, end)
oven-deck           # Deck oven (pastry corner)
cooler-walkin       # Walk-in cooler (north)
cooler-reachin      # Reach-in cooler (pastry corner)

# Examples
grill-flatop.hotline        # Grill on hot line
range-4burner.hotline       # Range on hot line
oven-deck.pastry            # Deck oven in pastry corner

# Equipment Capacity Expression
capacity: <equipment> can handle <quantity> <item> simultaneously

# Examples
capacity: grill-flatop can handle 4 salmon simultaneously
capacity: grill-flatop can handle 3 chicken simultaneously
capacity: range-4burner can handle 4 pans simultaneously

# Equipment Timing Expression
timing: <equipment>.<operation> = <duration>

# Examples
timing: grill-flatop.salmon = 8 minutes
timing: grill-flatop.chicken = 12 minutes
timing: oven-deck.torte = 25 minutes
timing: fryer-deep.reheat = 4 minutes
```

#### 2.1.3 Station Expressions

Stations are defined with their equipment, capacity, and function:

```yaml
# Station Definition Syntax
station <station-name>:
  type: <station-type>
  location: <kitchen-zone>
  equipment: [<equipment-ref>, ...]
  capacity: <max-workers> workers, <max-orders> orders
  primary-function: <description>
  adjacent-to: [<station-name>, ...]

# Station Types
hot-line           # Primary cooking line
cold-prep          # Cold preparation and pantry
grill-station      # Grilling station
sauté-station      # Sauté station
expediting         # Plating and timing coordination
pastry-corner      # Dessert preparation
dish-area          # Dish washing
protein-prep       # Protein preparation

# Examples
station hot-line:
  type: hot-line
  location: south
  equipment: [range-4burner, grill-flatop, fryer-deep]
  capacity: 4 workers, 8 orders
  primary-function: "Primary cooking and hot component preparation"
  adjacent-to: [prep-area, expediting]

station expediting:
  type: expediting
  location: southeast
  equipment: [cooler-reachin]
  capacity: 2 workers, 12 orders
  primary-function: "Final plating, quality control, timing coordination"
  adjacent-to: [hot-line]
```

#### 2.1.4 Menu Item Expressions

Menu items are defined with components, timing, and requirements:

```yaml
# Menu Item Definition Syntax
menu-item <item-name>:
  category: <category>
  components:
    - <component-name>: <prep-spec>
    - ...
  station: <primary-station>
  cook-time: <duration>
  plating-time: <duration>
  firing-order: <order-category>
  temperature-requirement: <temp>°F [if applicable]
  allergen-risks: [<allergen>, ...]

# Categories
starter
main
side
dessert

# Firing Order Categories
early              # Before entrees (salads, soups)
early-main         # Early among mains (long cook items)
main               # Standard main firing
late               # Last among mains (longest cook times)

# Examples
menu-item grilled-salmon:
  category: main
  components:
    - salmon-fillet: prep 5min by sophie
    - herb-butter: prep 15min by sophie
    - lemon-caper-sauce: prep 20min by sophie
    - seasonal-vegetables: prep varies by james
    - grill-finish: 8min at grill-station
  station: grill-station
  cook-time: 8 minutes
  plating-time: 4 minutes
  firing-order: main
  temperature-requirement: 145°F
  allergen-risks: [fish, dairy]

menu-item house-salad:
  category: starter
  components:
    - mixed-greens: prep 15min by james
    - vinaigrette: prep 10min by james
    - assembly: 3min at cold-prep
  station: cold-prep
  cook-time: 0
  plating-time: 3 minutes
  firing-order: early
  allergen-risks: [sulfites]
```

---

## Part III: The Temporal Grammar

### 3.1 Time Expression Syntax

The DSL provides specific temporal expressions for kitchen operations:

#### 3.1.1 Absolute Time References

```yaml
# Absolute Time Format (24-hour)
HH:MM

# Examples
17:30          # 5:30 PM (service start)
21:30          # 9:30 PM (service end)
15:00          # 3:00 PM (Maria arrives)
16:00          # 4:00 PM (Elena arrives)

# Service Phase Markers
service-start    # Alias for 17:30
service-end      # Alias for 21:30
first-fire       # First ticket firing
last-call        # Last order taking
```

#### 3.1.2 Relative Time Expressions

```yaml
# Relative Time Format
[+|-]<duration> [from <anchor>]

# Duration Units
minutes, min
hours, hr
seconds, sec

# Anchors
service-start
first-order
order-receipt
plating-time
service-end

# Examples
+45min from service-start      # 45 minutes after service starts
-30min from service-end       # 30 minutes before service ends
+2min from order-receipt      # 2 minutes after order comes in
+18min from order-receipt     # Standard ticket time target
```

#### 3.1.3 Interval Expressions

```yaml
# Time Interval Format
<start-time> - <end-time>

# Examples
15:00 - 15:45          # Maria's overview period
16:00 - 16:45          # Elena's station setup
17:00 - 17:30          # Final prep before service
18:30 - 18:45          # Standard break window
21:30 - 22:00          # Post-service immediate close

# Interval Duration Calculation
duration(<interval>) = <end-time> - <start-time>

# Example
duration(18:30 - 18:45) = 15 minutes
```

### 3.2 Lead Time and Timing Windows

#### 3.2.1 Lead Time Expressions

```yaml
# Lead Time Definition
lead-time(<activity>) = <duration>

# Examples
lead-time(salmon-fire) = 8 minutes      # From order to fire complete
lead-time(risotto-fire) = 18 minutes    # Longest cook time
lead-time(salad-plate) = 3 minutes     # From order to plate ready

# Firing Calculation
fire-time(<item>) = plating-deadline - lead-time(<item>)

# Example
# Salmon plate deadline: 17:50 (18min from order at 17:32)
# Salmon lead time: 8 minutes
# Therefore fire salmon at: 17:50 - 8min = 17:42
```

#### 3.2.2 Timing Window Expressions

```yaml
# Timing Window Definition
timing-window(<activity>):
  earliest: <time>
  target: <time>
  latest: <time>
  flexibility: <duration>

# Examples
timing-window(prep-complete):
  earliest: 17:00
  target: 17:15
  latest: 17:30
  flexibility: 15min

timing-window(ticket-time):
  earliest: 12 minutes
  target: 14-16 minutes
  latest: 20 minutes
  flexibility: 4 minutes

timing-window(break-coverage):
  earliest: 18:25
  target: 18:30
  latest: 18:35
  flexibility: 5min
```

### 3.3 Sequence and Parallelism

#### 3.3.1 Sequential Dependencies

```yaml
# Dependency Expression
<activity-a> must complete before <activity-b>

# Shorthand
<activity-a> → <activity-b>

# Examples
station-setup → prep-work
prep-work → service-start
order-receipt → fire-sequence
salmon-fire → salmon-up
all-components-ready → plating
plating → expo-check
expo-check → out
```

#### 3.3.2 Parallel Execution

```yaml
# Parallel Block
parallel:
  - <activity-1>
  - <activity-2>
  - ...

# Synchronized Parallel
synchronize at <activity>:
  parallel:
    - <activity-a>
    - <activity-b>
    - ...

# Examples
# These activities happen simultaneously during prep
parallel:
  - james.prep.vegetables
  - sophie.prep.proteins
  - elena.setup.grill

# Plate synchronization
synchronize at plating-deadline:
  parallel:
    - salmon.finish at grill
    - vegetables.finish at sauté
    - sauce.ready at sauce-station
```

### 3.4 Phase Definitions

```yaml
# Phase Definition
phase <phase-name>:
  start: <time>
  end: <time>
  activities: [<activity>, ...]
  transitions-to: <next-phase>

# Examples
phase setup:
  start: 15:00
  end: 16:45
  activities:
    - maria.overview
    - james.station-setup
    - sophie.station-setup
    - david.line-setup
    - elena.grill-setup
    - tyler.support-setup
  transitions-to: pre-service-prep

phase pre-service-prep:
  start: 16:45
  end: 17:15
  activities:
    - james.vegetable-prep
    - sophie.protein-prep
    - james.pastry-prep
    - david.final-verification
  transitions-to: service

phase service:
  start: 17:30
  end: 21:30
  activities:
    - order-receipt
    - fire-sequence
    - component-preparation
    - plating
    - expo-check
    - out
  transitions-to: close

phase close:
  start: 21:30
  end: 22:30
  activities:
    - active-close
    - station-cleandown
    - equipment-shutdown
    - final-walkthrough
  transitions-to: (end)
```

---

## Part IV: The Process Vocabulary

### 4.1 Activity Specifications

#### 4.1.1 Activity Definition Syntax

```yaml
# Activity Definition
activity <activity-name>:
  assigned-to: <staff-ref>
  location: <station-name>
  duration: <duration>
  deadline: <time>
  dependencies: [<activity>, ...]
  completion-criteria: <description>

# Examples
activity grill.salmon.fire:
  assigned-to: elena.line
  location: grill-station
  duration: 8 minutes
  deadline: fire-time(salmon) + 8min
  dependencies: [order.received]
  completion-criteria: "Internal temperature reaches 145°F"

activity prep.vegetables.evening:
  assigned-to: james.prep
  location: cold-prep
  duration: 75 minutes
  deadline: 17:15
  dependencies: [station.setup.complete]
  completion-criteria: "All vegetables prepped, stored at correct temperature"
```

#### 4.1.2 Task Breakdown

```yaml
# Task Definition (Atomic Unit)
task <task-name>:
  for-activity: <activity-name>
  assigned-to: <person>
  description: <text>
  deadline: <time>
  resources: [<resource>, ...]

# Examples
task season.salmon.fillet:
  for-activity: prep.proteins.evening
  assigned-to: sophie
  description: "Season salmon fillets lightly, portion to 6oz"
  deadline: 17:00
  resources: [salmon, salt, pepper, scale]

task make.lemon-caper-sauce:
  for-activity: prep.sauces.evening
  assigned-to: sophie
  description: "Reduce wine, add capers, cream, mount butter"
  deadline: 17:30
  resources: [white wine, capers, cream, butter, range-4burner]
```

### 4.2 Station Operations

#### 4.2.1 Station Setup Specification

```yaml
# Station Setup Definition
station-setup <station-name>:
  performed-by: <person>
  start-time: <time>
  end-time: <time>
  tasks:
    - <task-description>
    - ...
  completion-verification: <criteria>

# Examples
station-setup hot-line:
  performed-by: david.sous
  start-time: 14:00
  end-time: 16:30
  tasks:
    - "Verify all 4 burners operational"
    - "Clean and organize sauté station"
    - "Pull all proteins for evening service"
    - "Set up mise en place containers"
    - "Prepare holding area for finished components"
    - "Test timing system functionality"
  completion-verification: "All stations operational, components accessible, timing system verified"

station-setup grill:
  performed-by: elena.line
  start-time: 16:00
  end-time: 16:45
  tasks:
    - "Fire up grill, bring to 425°F surface temperature"
    - "Verify fryer at 350°F"
    - "Set up grill tools: tongs (2), spatula, grill brush"
    - "Prepare cold holding for proteins"
    - "Portion compound butter for service"
  completion-verification: "Grill at temperature, tools accessible, cold holding ready"
```

#### 4.2.2 Station Operation During Service

```yaml
# Station Operation Cycle
station-operation <station-name>:
  during: service
  loop:
    - receive-order
    - fire-component
    - execute-cooking
    - check-quality
    - call-ready
    - hand-off
  max-concurrent-orders: <number>
  escalation: <trigger> → <action>

# Examples
station-operation grill-station:
  during: service
  loop:
    - receive: "Receive fire call from expo"
    - fire: "Place item on grill, start timing"
    - execute: "Monitor cooking, check temperature"
    - quality-check: "Verify internal temp, visual appearance"
    - call: "Call 'salmon up' when complete"
    - handoff: "Transfer to plating area"
  max-concurrent-orders: 4
  escalation:
    - trigger: "More than 4 active orders"
      action: "Call 'behind' to david.sous"
    - trigger: "Equipment issue"
      action: "Report to david immediately"
```

### 4.3 Handoff Protocols

```yaml
# Handoff Definition
handoff <handoff-name>:
  from: <station>
  to: <station>
  trigger: <condition>
  communication: <call-type>
  quality-check: <criteria>

# Examples
handoff component-to-plating:
  from: grill-station
  to: expediting
  trigger: "Component temperature reached, visual check passed"
  communication: "[Item] up"
  quality-check: "Temperature verified, presentation acceptable"

handoff order-release:
  from: expediting
  to: line
  trigger: "Order received from POS"
  communication: "Order in"
  quality-check: "All special requests noted, modifications confirmed"

handoff break-coverage:
  from: elena.line
  to: tyler.support
  trigger: "6:25 PM announcement, 6:30 PM break start"
  communication: "Coverage in 5... Coverage"
  quality-check: "Coverage person acknowledges, regular person briefs on active tickets"
```

---

## Part V: The Constraint Vocabulary

### 5.1 Hard Constraint Expressions

Hard constraints are non-negotiable requirements expressed in the DSL:

```yaml
# Hard Constraint Syntax
hard-constraint <constraint-id>:
  description: <text>
  specification: <expression>
  verification: <method>
  violation-response: <action>

# Food Safety Constraints
hard-constraint CON-FS-001:
  description: "Cold holding temperature requirement"
  specification: "all cold-foods.temperature ≤ 40°F"
  verification: "thermometer check every 4 hours"
  violation-response: "stop-service, discard food, document incident"

hard-constraint CON-FS-002:
  description: "Hot holding temperature requirement"
  specification: "all hot-holds.temperature ≥ 140°F"
  verification: "thermometer check every 2 hours"
  violation-response: "stop-service, reheat or discard, document incident"

hard-constraint CON-FS-003:
  description: "Salmon minimum cooking temperature"
  specification: "salmon.internal-temp ≥ 145°F"
  verification: "instant-read thermometer before plating"
  violation-response: "return-to-heat, recheck temp, document"

hard-constraint CON-FS-004:
  description: "Chicken minimum cooking temperature"
  specification: "chicken.internal-temp ≥ 165°F"
  verification: "instant-read thermometer before plating"
  violation-response: "return-to-heat, recheck temp, document"

hard-constraint CON-FS-005:
  description: "Danger zone time limit"
  specification: "any-food.danger-zone-duration ≤ 120 minutes"
  verification: "time-in/out logging"
  violation-response: "discard food, document incident"

# Physical Constraints
hard-constraint CON-PH-001:
  description: "Grill capacity limit"
  specification: "grill-flatop.concurrent-items ≤ 4 salmon OR ≤ 3 chicken"
  verification: "generation-time check, execution-time monitoring"
  violation-response: "delay firing, notify expo"

hard-constraint CON-PH-002:
  description: "Elena ticket limit"
  specification: "elena.active-tickets ≤ 6"
  verification: "expo monitoring"
  violation-response: "tyler support, limit new fires"

# Legal Constraints
hard-constraint CON-LG-001:
  description: "Certified manager present"
  specification: "maria OR david.present during all food preparation"
  verification: "shift documentation"
  violation-response: "no service until manager arrives"
```

### 5.2 Soft Constraint Expressions

Soft constraints are preferred conditions expressed with weights:

```yaml
# Soft Constraint Syntax
soft-constraint <constraint-id>:
  description: <text>
  specification: <expression>
  weight: <0.0-1.0>
  target: <value>
  violation-penalty: <description>

# Timing Soft Constraints
soft-constraint CON-ST-001:
  description: "Prep completion buffer"
  specification: "all-prep.complete-by ≥ service-start - 30min"
  weight: 0.8
  target: "30-minute buffer achieved"
  violation-penalty: "Rushed final prep, potential quality impact"

soft-constraint CON-ST-002:
  description: "Average ticket time target"
  specification: "average(ticket-time) between 14min and 16min"
  weight: 0.9
  target: "15-minute average"
  violation-penalty: "Customer satisfaction impact, table turn impact"

soft-constraint CON-ST-003:
  description: "First ticket target"
  specification: "first-ticket-time ≤ 18 minutes"
  weight: 0.7
  target: "16-minute first ticket"
  violation-penalty: "Early customer wait impression"

# Quality Soft Constraints
soft-constraint CON-SQ-001:
  description: "Plate temperature"
  specification: "plates.preheated before plating"
  weight: 0.5
  target: "All plates heated"
  violation-penalty: "Food cools faster on cold plate"

soft-constraint CON-SQ-002:
  description: "Protein rest time"
  specification: "grilled-proteins.rest ≥ 2 minutes before plating"
  weight: 0.6
  target: "2-3 minute rest"
  violation-penalty: "Juices escape during cutting"

# Practitioner Preference Constraints
soft-constraint CON-SP-001:
  description: "Elena ticket preference"
  specification: "elena.active-tickets ≤ 6 (soft limit)"
  weight: 0.8
  target: "4-5 active tickets average"
  violation-penalty: "Elena stress, potential quality degradation"

soft-constraint CON-SP-002:
  description: "James communication preference"
  specification: "james.receives-written-prep-lists = true"
  weight: 0.7
  target: "Written lists for all prep items"
  violation-penalty: "Miscommunication, missed items"
```

### 5.3 Optimization Target Expressions

```yaml
# Optimization Target Syntax
optimization-target <target-id>:
  objective: <description>
  measure: <metric-expression>
  direction: [minimize | maximize]
  weight: <0.0-1.0>
  bounds: [<min>, <max>]

# Examples
optimization-target OPT-001:
  objective: "Maintain consistent food quality"
  measure: "average(quality-ratings)"
  direction: maximize
  weight: 0.4
  bounds: [4.5, 5.0]

optimization-target OPT-002:
  objective: "Keep ticket times within target range"
  measure: "average(ticket-time)"
  direction: minimize
  weight: 0.3
  bounds: [14, 16]

optimization-target OPT-003:
  objective: "Respect practitioner workload preferences"
  measure: "preference-satisfaction-rate"
  direction: maximize
  weight: 0.15
  bounds: [0.9, 1.0]

optimization-target OPT-004:
  objective: "Maintain cost efficiency"
  measure: "labor-cost-per-cover"
  direction: minimize
  weight: 0.15
  bounds: [18, 22]

# Trade-off Resolution
trade-off between <target-a> and <target-b>:
  resolution: <priority-statement>
  threshold: <condition>

# Example
trade-off between OPT-001 (quality) and OPT-002 (speed):
  resolution: "Quality takes precedence over speed"
  threshold: "If ticket time would exceed 20min to maintain quality, accept longer ticket"
```

---

## Part VI: The Communication Protocols

### 6.1 Call Syntax

Communication calls follow standardized patterns:

```yaml
# Call Definition
call <call-name>:
  trigger: <condition>
  speaker: <role>
  response: <expected-response>
  action: <resulting-action>

# Standard Calls
call order-in:
  trigger: "New order received from POS"
  speaker: expo
  response: "Heard"
  action: "Stations acknowledge, begin fire assessment"

call fire <item>:
  trigger: "Order contains <item>, ready to begin cooking"
  speaker: expo
  response: "Firing <item>"
  action: "Station begins cooking item"

call <item> up:
  trigger: "Component cooking complete, ready for next step"
  speaker: <station-cook>
  response: "Heard"
  action: "Expo acknowledges, prepares for next step"

call all-day:
  trigger: "Periodic summary request"
  speaker: expo
  response: "<count> salmon, <count> chicken, ..."
  action: "Line prioritizes based on all-day count"

call gap:
  trigger: "No orders in queue"
  speaker: expo
  response: "Gap"
  action: "Stations prepare for next order, maintain readiness"

call behind:
  trigger: "Station approaching capacity limit"
  speaker: <station-cook>
  response: "Behind"
  action: "Expo prioritizes, support assists if available"

call need <resource>:
  trigger: "Station requires assistance"
  speaker: <station-cook>
  response: "On it" or <acknowledgment>
  action: "Support or colleague provides assistance"

call all-off:
  trigger: "All orders completed, no pending"
  speaker: expo
  response: [celebration]
  action: "Moment of acknowledgment, then reset for next service"
```

### 6.2 Escalation Protocols

```yaml
# Escalation Definition
escalation <escalation-type>:
  trigger: <condition>
  initial-contact: <role>
  escalate-to: <role>
  threshold: <condition>
  action: <response-protocol>

# Quality Escalation
escalation quality-concern:
  trigger: "Observable deviation from quality standard"
  initial-contact: station-cook
  escalate-to: maria.executive
  threshold: "Cook cannot resolve independently"
  action: "Stop plating, assess, correct, document"

# Timing Escalation
escalation timing-delay:
  trigger: "Ticket time exceeds 18 minutes"
  initial-contact: expo
  escalate-to: david.sous
  threshold: "3+ minutes over target"
  action: "Expedite aggressively, assess cause, communicate to tables if needed"

# Equipment Escalation
escalation equipment-issue:
  trigger: "Equipment malfunction or unexpected behavior"
  initial-contact: discovering-staff
  escalate-to: david.sous → maria.executive
  threshold: "Affects current service"
  action: "Assess impact, implement contingency, document, repair"

# Food Safety Escalation
escalation food-safety-concern:
  trigger: "Any potential food safety issue"
  initial-contact: any-staff
  escalate-to: maria.executive
  threshold: "Immediate"
  action: "Stop service if needed, assess, resolve, document, report if required"
```

### 6.3 Communication Schedule

```yaml
# Scheduled Communication
communication <communication-name>:
  time: <time>
  participants: [<role>, ...]
  content: <description>
  format: <structure>

# Examples
communication 15:00-overview:
  time: 15:00
  participants: [maria.executive]
  content: "Kitchen overview, inventory check, special requests"
  format: "Brief walkthrough"

communication 16:45-prep-check:
  time: 16:45
  participants: [david.sous, maria.executive]
  content: "Prep status review, equipment confirmation"
  format: "Checklist verification"

communication 17:15-family-meal:
  time: 17:15
  participants: [all-staff]
  content: "Light meal before service, team moment"
  format: "Informal, 10-15 minutes"

communication 17:25-pre-service-brief:
  time: 17:25
  participants: [all-staff]
  content: "Tonight's menu, special notes, break schedule"
  format: "Quick verbal brief"

communication 18:25-coverage-announcement:
  time: 18:25
  participants: [david.sous, all-staff]
  content: "Break coverage reminder"
  format: "Verbal announcement"
```

---

## Part VII: The Workflow Instance Syntax

### 7.1 Complete Workflow Document Structure

A daily workflow instance follows this structure:

```yaml
# Copper Beech Bistro Daily Workflow Instance
workflow:
  meta:
    document-id: WKF-<YYYYMMDD>-<sequence>
    date: <date>
    generated-by: CopperBeech-WorkflowGen
    generation-time: <timestamp>
    version: <version-number>
    
  context:
    service-date: <date>
    day-of-week: <day>
    expected-covers: <number>
    weather: <conditions>
    special-conditions: <notes>
    
  staffing:
    assignments:
      - role: executive-chef
        person: maria
        station: expediting
        shift: 15:00-22:00
        
      - role: sous-chef
        person: david
        station: sauté
        shift: 14:00-22:00
        
      # ... additional assignments ...
      
    break-schedule:
      - person: james
        break: 18:30-18:45
        coverage-by: sophie
        
      - person: elena
        break: 18:30-18:45
        coverage-by: tyler
        
  equipment:
    status:
      - equipment: range-4burner
        status: operational
        notes: "All burners good"
        
      - equipment: grill-flatop
        status: operational
        notes: "Cleaned, seasoned"
        
      # ... additional equipment status ...
      
  menu:
    tonight:
      starters:
        - house-salad
        - beet-salad
        - soup
        
      mains:
        - grilled-salmon
        - chicken-breast
        - short