# Conceptualization: Daily Workflow Design for Small Commercial Kitchens

## Topology — Pass 1

---

# The Central Question

**What entities and relationships form the natural structure of designing the daily workflow of a small commercial kitchen? How do concepts connect, cluster, and relate in this domain?**

This document maps the conceptual topology—the network of entities and their relationships—that underlies daily workflow design. It identifies the nodes (concepts), edges (relationships), clusters (natural groupings), and structural patterns that emerge when this domain is examined as a connected system rather than a collection of isolated elements.

---

# I. Primary Entities

## The Fundamental Nodes

Entities are the distinct concepts that exist as nodes in the workflow network. Each has identity, attributes, and connections to other entities.

### 1. Material Entities

**Ingredient**
- Raw materials entering the system
- Attributes: type, quantity, quality state, temperature, freshness window, storage requirements
- Transforms into: Prepared Component, Waste, Scrap
- Connections: Storage, Prep Station, Recipe, Supplier, Inventory

**Prepared Component**
- An ingredient that has undergone transformation but is not yet a finished plate
- Attributes: degree of preparation, holding requirements, shelf life, quantity
- Transforms into: Cooked Component, Plate Assembly, Waste
- Connections: Prep Station, Walk-In, Line Station, Recipe

**Cooked Component**
- A component that has completed thermal transformation
- Attributes: temperature, doneness level, holding window, plating readiness
- Transforms into: Plate Assembly, Waste (if over-held)
- Connections: Cooking Equipment, Line Station, Expo, Holding Area

**Finished Plate**
- A complete dish ready for service
- Attributes: temperature, presentation state, modification flags, destination
- Connections: Expo, Pass, Server, Customer

**Waste and Scrap**
- Material exiting the transformation chain
- Attributes: type (organic, packaging, hazardous), volume, disposal method
- Connections: Cleanup Station, Disposal, Inventory (for tracking)

### 2. Spatial Entities

**Station**
- A bounded workspace defined by equipment and function
- Attributes: type (grill, sauté, prep, etc.), equipment inventory, capacity, operator assignment
- Contains: Equipment, Tools, Containers
- Connections: Other Stations, Flow Paths, Operators, Prep Items

**Equipment**
- Fixed or semi-fixed tools that enable transformation
- Attributes: type, capacity, current state, maintenance status, location
- Types: Cooking Equipment, Storage Equipment, Prep Equipment, Cleanup Equipment
- Connections: Station, Operator, Recipe Step, Maintenance

**Flow Path**
- A route by which materials and people move between locations
- Attributes: type (raw-to-prep, prep-to-line, line-to-pass), distance, congestion risk, cross-contamination risk
- Connections: Station to Station, Zone to Zone

**Zone**
- An area of the kitchen defined by temperature or function
- Attributes: type (cold, hot, neutral, support, service), temperature range, regulatory classification
- Contains: Stations, Flow Paths
- Connections: Adjacent Zones, Handoff Points

**The Pass**
- The boundary and handoff zone between kitchen and service
- Attributes: capacity, expo assignment, heat lamp availability
- Connections: Line, Expo, Server, Finished Plate

### 3. Temporal Entities

**Prep Window**
- A bounded time period for preparation work
- Attributes: start time, end time, duration, available capacity
- Connections: Service Start, Prep Tasks, Staffing

**Service Window**
- A bounded time period for active customer service
- Attributes: start time, end time, expected volume, peak identification
- Connections: Prep Window, Tickets, Staffing, Revenue

**Ticket**
- A work order representing one or more customer items
- Attributes: table/seat ID, items, modifications, timestamps (received, fired, due), priority
- Lifecycle: Called → Fired → Cooking → Plating → Expo → Served
- Connections: Customer, POS, Line Cook, Expo, Server, Recipe

**Task**
- A unit of work with defined start, duration, and end
- Attributes: type, duration estimate, actual duration, dependencies, assigned person, status
- Connections: Recipe, Person, Equipment, Station, Preceding Task, Following Task

**Time Block**
- A defined segment of the operational day
- Types: Opening, Pre-Service Prep, Service, Wind-Down, Closing
- Connections: Tasks, Transitions, Phase Changes

### 4. Human Entities

**Person**
- A human actor in the workflow
- Attributes: role, skills, current location, current task, fatigue level, attention state
- Roles: Chef de Cuisine, Sous Chef, Line Cook, Prep Cook, Dishwasher, Expo, Server
- Connections: Tasks, Stations, Other People, Communication

**Role**
- A defined set of responsibilities and authorities
- Attributes: primary duties, backup duties, escalation authority, skill requirements
- Connections: People, Tasks, Stations, Other Roles

**Team**
- A group of people working together during a shift
- Attributes: composition, shift type, experience level, cohesion
- Connections: People, Roles, Tasks, Communication Patterns

**Customer**
- A person receiving food service
- Attributes: party size, order, modifications, special requirements, patience level
- Connections: Ticket, Server, Finished Plate, Satisfaction

### 5. Information Entities

**Recipe**
- A specification for transforming ingredients into a dish
- Attributes: ingredient list, quantities, sequence, techniques, timing, quality standards, variations
- Connections: Ingredients, Equipment, Tasks, Station, Temperature, Quality Standards

**Modification**
- A deviation from standard recipe preparation
- Attributes: type (allergen, preference, restriction), scope (full dish, component), priority
- Connections: Recipe, Ticket, Line Cook, Special Handling

**Standard Operating Procedure (SOP)**
- A codified workflow for a specific task or situation
- Attributes: scope, steps, quality checkpoints, failure modes
- Connections: Task, Station, Training, Compliance

**Communication**
- Information transferred between entities
- Types: Call (announcement), Mark (acknowledgment), Request (need), Status (state update)
- Attributes: sender, receiver, content, urgency, channel
- Connections: People, Stations, Tasks, Tickets

### 6. Resource Entities

**Capacity**
- The maximum throughput or storage of a resource
- Attributes: type (equipment, space, time, human), limit, current utilization, slack
- Connections: Equipment, Station, Space, Person, Time

**Inventory**
- Stock of ingredients and supplies
- Attributes: item type, quantity on hand, par level, reorder point, location
- Connections: Ingredient, Supplier, Storage, Par Level, Usage

**Par Level**
- The target quantity of an item to maintain
- Attributes: item type, target quantity, reorder trigger
- Connections: Inventory, Supplier, Prep Task

---

# II. Relationship Types

## The Fundamental Edges

Relationships are the connections between entities. Each relationship type has direction, attributes, and meaning.

### 1. Transformation Relationships

**Transforms-Into**
- A material entity changes state through work
- Direction: Material → New Material
- Attributes: transformation type, equipment required, duration, quality risk
- Example: Ingredient → Prepared Component

**Is-Part-Of**
- A component combines to form a larger whole
- Direction: Component → Plate
- Attributes: quantity, timing contribution, presentation role
- Example: Cooked Component → Finished Plate

**Requires**
- A transformation requires specific conditions or inputs
- Direction: Task → Equipment/Condition/Ingredient
- Attributes: specificity, flexibility, criticality
- Example: Recipe Step → Equipment

### 2. Flow Relationships

**Feeds**
- Output from one location becomes input to another
- Direction: Source → Destination
- Attributes: timing sensitivity, quantity, holding requirements
- Example: Prep Station → Line Station

**Precedes**
- One task or entity must occur before another
- Direction: Earlier → Later
- Attributes: hard/soft, lag time, criticality
- Example: Prep → Cooking

**Holds-For**
- A buffer or staging area holds items until needed
- Direction: Item → Storage → Retrieval
- Attributes: holding duration, degradation risk, retrieval priority
- Example: Walk-In → Line Station

### 3. Assignment Relationships

**Assigned-To**
- A human or resource is allocated to a task or location
- Direction: Person → Task/Station
- Attributes: primary/secondary, authority level, coverage scope
- Example: Line Cook → Grill Station

**Responsible-For**
- An entity has accountability for an outcome
- Direction: Person/Role → Task/Area/Standard
- Attributes: scope, decision authority, escalation path
- Example: Expo → Plating Quality

**Covers**
- A person or resource temporarily assumes another's duties
- Direction: Coverer → Covered
- Attributes: scope of coverage, duration, communication requirement
- Example: Prep Cook → Sauté Station

### 4. Constraint Relationships

**Limits**
- One entity constrains the capacity or behavior of another
- Direction: Constraint → Constrained
- Attributes: constraint type (time, space, resource), flexibility, threshold
- Example: Equipment Capacity → Throughput

**Requires-Availability-Of**
- A task requires a resource to be free or accessible
- Direction: Task → Resource
- Attributes: exclusivity, timing window, reservation status
- Example: Recipe Step → Burner

**Depends-On**
- A task or entity's viability depends on another
- Direction: Dependent → Dependency
- Attributes: dependency type (hard/soft), criticality, fallback options
- Example: Plating → Cooking Completion

### 5. Communication Relationships

**Informs**
- Information flows from one entity to another
- Direction: Sender → Receiver
- Attributes: urgency, confirmation required, channel
- Example: Line Cook → Expo

**Announces**
- A status or need is broadcast to relevant parties
- Direction: Source → Relevant Parties
- Attributes: audience scope, frequency, acknowledgment requirement
- Example: Ticket Called → Line

**Escalates-To**
- A problem or decision is transferred to higher authority
- Direction: Lower Authority → Higher Authority
- Attributes: trigger criteria, urgency, response time expectation
- Example: Line Cook → Sous Chef

### 6. Quality Relationships

**Meets-Standard**
- An output satisfies quality requirements
- Direction: Output → Standard
- Attributes: standard type, tolerance, measurement method
- Example: Finished Plate → Quality Specification

**Verified-By**
- Quality is confirmed through a check process
- Direction: Output → Check Process → Person
- Attributes: check type, frequency, threshold
- Example: Temperature → Thermometer Reading → Cook

**Triggers-Exception**
- A deviation from standard initiates a response
- Direction: Deviation → Response Process
- Attributes: severity, response type, documentation required
- Example: Undercooked Protein → Recook Protocol

---

# III. Network Topology Maps

## The Conceptual Network Structure

### 1. The Material Flow Network

```
                    ┌─────────────────────────────────────────┐
                    │          INGREDIENT RECEIVING            │
                    └─────────────────────┬───────────────────┘
                                          │
                                          ▼
                    ┌─────────────────────────────────────────┐
                    │         STORAGE (Walk-in/Dry)          │
                    └─────────────────────┬───────────────────┘
                                          │
                    ┌─────────────────────┼─────────────────────┐
                    │                     │                     │
                    ▼                     ▼                     ▼
            ┌───────────────┐     ┌───────────────┐     ┌───────────────┐
            │  PREP STATION │     │  PREP STATION │     │  PREP STATION │
            │   (Proteins)  │     │   (Produce)   │     │   (Starches)  │
            └───────┬───────┘     └───────┬───────┘     └───────┬───────┘
                    │                     │                     │
                    ▼                     ▼                     ▼
            ┌───────────────┐     ┌───────────────┐     ┌───────────────┐
            │ PREPARED      │     │ PREPARED      │     │ PREPARED      │
            │ COMPONENT     │     │ COMPONENT     │     │ COMPONENT     │
            └───────┬───────┘     └───────┬───────┘     └───────┬───────┘
                    │                     │                     │
                    └─────────────────────┼─────────────────────┘
                                          │
                                          ▼
                    ┌─────────────────────────────────────────┐
                    │        WALK-IN HOLDING (Staging)         │
                    └─────────────────────┬───────────────────┘
                                          │
                                          ▼
                    ┌─────────────────────────────────────────┐
                    │              THE LINE                    │
                    │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐       │
                    │  │GRILL│ │SAUTÉ│ │ FRY │ │COLD │       │
                    │  └──┬──┘ └──┬──┘ └──┬──┘ └──┬──┘       │
                    └─────┼───────┼───────┼───────┼──────────┘
                          │       │       │       │
                          ▼       ▼       ▼       ▼
                    ┌─────────────────────────────────────────┐
                    │              THE PASS                    │
                    └─────────────────────┬───────────────────┘
                                          │
                                          ▼
                    ┌─────────────────────────────────────────┐
                    │            FINISHED PLATES              │
                    │              TO SERVICE                 │
                    └─────────────────────────────────────────┘
```

**Network Properties of Material Flow:**
- **Path length**: Variable from 3 steps (simple cold dish) to 10+ steps (complex multi-component hot dish)
- **Branching factor**: High at prep stage (many ingredients into one dish), converges at assembly
- **Critical path**: The longest sequence determines minimum lead time
- **Parallelism**: Multiple dishes flow simultaneously through the network

### 2. The Information Flow Network

```
                    ┌─────────────────────────────────────────┐
                    │            CUSTOMER ORDER                │
                    └─────────────────────┬───────────────────┘
                                          │
                                          ▼
                    ┌─────────────────────────────────────────┐
                    │              POS SYSTEM                 │
                    └─────────────────────┬───────────────────┘
                                          │
                                          ▼
                    ┌─────────────────────────────────────────┐
                    │           TICKET CALLED                 │
                    │    (Physical/Digital Rail)             │
                    └───────┬─────────────────────┬──────────┘
                            │                     │
                            ▼                     ▼
                    ┌───────────────┐     ┌───────────────┐
                    │  LINE COOK    │     │     EXPO      │
                    │  (Receives)   │     │  (Monitors)   │
                    └───────┬───────┘     └───────┬───────┘
                            │                     │
                            ▼                     │
                    ┌───────────────┐             │
                    │  COOKING      │             │
                    │  (Execution)   │             │
                    └───────┬───────┘             │
                            │                     │
                            ▼                     │
                    ┌───────────────┐             │
                    │   PLATING    │◄────────────┘
                    │  (Complete)  │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │  EXPO CHECK   │
                    │  (Quality)    │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   MARKED/UP   │
                    │ (Acknowledged)│
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │   SERVER      │
                    │  (PICKUP)     │
                    └───────────────┘
```

**Information Flow Characteristics:**
- **Broadcast nature**: "All day" calls inform everyone
- **Acknowledge pattern**: Marked tickets confirm receipt
- **Status propagation**: Each station updates state for downstream visibility
- **Escalation channels**: Problems escalate through defined paths

### 3. The People-Task Network

```
                    ┌─────────────────────────────────────────┐
                    │           CHEF DE CUISINE               │
                    │  (Menu, Standards, Oversight)           │
                    └─────────────────────┬───────────────────┘
                                          │
                    ┌─────────────────────┼─────────────────────┐
                    │                     │                     │
                    ▼                     ▼                     ▼
            ┌───────────────┐     ┌───────────────┐     ┌───────────────┐
            │   SOUS CHEF   │     │   SOUS CHEF   │     │   EXPO        │
            │  (If present) │     │   (If present)│     │(Coordination) │
            └───────┬───────┘     └───────┬───────┘     └───────┬───────┘
                    │                     │                     │
                    └──────────┬──────────┴──────────┬──────────┘
                               │                     │
              ┌────────────────┼─────────────────────┼────────────────┐
              │                │                     │                │
              ▼                ▼                     ▼                ▼
      ┌───────────────┐ ┌───────────────┐   ┌───────────────┐ ┌───────────────┐
      │   LINE COOK   │ │   LINE COOK   │   │   LINE COOK   │ │   LINE COOK   │
      │    (GRILL)    │ │   (SAUTÉ)     │   │    (FRY)      │ │    (COLD)     │
      └───────┬───────┘ └───────┬───────┘   └───────┬───────┘ └───────┬───────┘
              │                 │                   │                 │
              ▼                 ▼                   ▼                 ▼
      ┌───────────────┐ ┌───────────────┐   ┌───────────────┐ ┌───────────────┐
      │  STATION      │ │  STATION      │   │  STATION      │ │  STATION      │
      │  TASKS        │ │  TASKS        │   │  TASKS        │ │  TASKS        │
      │  (Grill)      │ │  (Sauté)      │   │  (Fry)        │ │  (Cold)       │
      └───────┬───────┘ └───────┬───────┘   └───────┬───────┘ └───────┬───────┘
              │                 │                   │                 │
              └─────────────────┴───────────────────┴─────────────────┘
                                         │
                                         ▼
                              ┌─────────────────────┐
                              │   SUPPORT STAFF     │
                              │ (Prep, Dish, Utility)│
                              └─────────────────────┘
```

**People-Task Network Characteristics:**
- **Star topology at chef level**: Chef connects to all roles
- **Mesh at line level**: Cooks coordinate laterally
- **Hub-spoke at stations**: Station is hub, individual tasks are spokes
- **Cross-training creates backup edges**: Potential connections for coverage

### 4. The Dependency Network

```
INGREDIENT ──────► PREPARED ──────► COOKED ──────► PLATE ──────► SERVICE
                 │                │                │
                 ▼                ▼                ▼
           (Requires          (Requires         (Requires
            Prep Skill,        Temp,              Plating,
            Time,              Time,              Expo Check,
            Equipment)         Equipment)         Timing)
           
           ┌─────────────────────────────────────────────────────────┐
           │                    TIME WINDOW                          │
           │  ┌─────────────────────────────────────────────────┐   │
           │  │           PREP WINDOW                           │   │
           │  │  ┌─────────────────────────────────────────┐    │   │
           │  │  │         SERVICE WINDOW                   │    │   │
           │  │  │                                          │    │   │
           │  │  │   ████████████████████████████████     │    │   │
           │  │  │                                          │    │   │
           │  │  └─────────────────────────────────────────┘    │   │
           │  └─────────────────────────────────────────────────┘   │
           └─────────────────────────────────────────────────────────┘

CRITICAL PATH: Ingredient → Prep → Hold → Pull → Cook → Plate → Expo → Serve
                    │
                    ├─► (Minimum 15 min for simple prep)
                    │   (Up to 8+ hours for braised items)
                    │
                    └─► Service cannot begin until all prep complete
```

### 5. The Equipment Dependency Network

```
                    ┌─────────────────────────────────────────┐
                    │           SHARED EQUIPMENT               │
                    │  (Refrigeration, Water, Gas, Electric)  │
                    └─────────────────────┬───────────────────┘
                                          │
          ┌───────────────┬───────────────┼───────────────┬───────────────┐
          │               │               │               │               │
          ▼               ▼               ▼               ▼               ▼
  ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
  │    OVEN       │ │    RANGE      │ │    FRYER      │ │    WALK-IN    │ │    PREP       │
  │   STATION     │ │   STATION     │ │   STATION     │ │   STATION     │ │   STATION     │
  └───────┬───────┘ └───────┬───────┘ └───────┬───────┘ └───────┬───────┘ └───────┬───────┘
          │                 │                 │                 │                 │
          ▼                 ▼                 ▼                 ▼                 ▼
  ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
  │  Roast Ops    │ │ Sauté Ops     │ │  Fry Ops      │ │  All Cold     │ │  All Prep     │
  │  Bake Ops     │ │ Grill Support │ │  Reheat       │ │  Storage      │ │  Surface      │
  └───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘ └───────────────┘

BOTTLENECK IDENTIFICATION:
• Single oven = limited roasting/baking capacity
• Single fryer = potential slowdown during high-fry demand
• Walk-in access = potential congestion point
• Prep surface = limited parallel prep capacity
```

---

# IV. Natural Clusters

## Conceptual Groupings

### 1. The Transformation Cluster

**Entities in cluster**: Ingredient, Prepared Component, Cooked Component, Finished Plate, Recipe, Equipment, Technique

**Internal relationships**:
- Ingredient → (transforms) → Prepared Component
- Prepared Component → (transforms) → Cooked Component
- Cooked Component → (assembles) → Finished Plate
- Recipe → (specifies) → Transformation Sequence
- Equipment → (enables) → Transformation

**External connections**:
- Recipe ← (provides) ← Chef
- Ingredient ← (receives) ← Supplier
- Finished Plate → (serves) ← Customer
- Equipment → (maintained by) ← Maintenance

**Cluster characteristic**: This is the productive core—the cluster where value is created. All other clusters exist to support this one.

### 2. The Coordination Cluster

**Entities in cluster**: Ticket, Rail, Expo, Communication, Timing, Handoff, Status

**Internal relationships**:
- Ticket → (located on) → Rail
- Expo → (monitors) → Rail
- Communication → (coordinates) → Handoff
- Status → (reflects) → Current State
- Timing → (governs) → Sequence

**External connections**:
- Ticket ← (generates) ← POS
- Expo → (checks) → Finished Plate
- Communication ← (initiates) ← Line Cook
- Handoff → (transfers to) ← Server

**Cluster characteristic**: This is the control center. It monitors, directs, and synchronizes all other clusters.

### 3. The Space-Equipment Cluster

**Entities in cluster**: Station, Zone, Equipment, Flow Path, Real Estate, Capacity

**Internal relationships**:
- Station → (contains) → Equipment
- Station → (located in) → Zone
- Equipment → (connected via) → Flow Path
- Real Estate → (constrains) → Station Layout
- Capacity → (limited by) → Equipment/Zone

**External connections**:
- Station ← (assigned to) ← Person
- Flow Path → (moves) ← Material
- Capacity → (affects) ← Throughput
- Zone → (requires) ← Temperature Control

**Cluster characteristic**: This is the physical substrate. It defines what is possible given the kitchen's geometry and equipment.

### 4. The People-Role Cluster

**Entities in cluster**: Person, Role, Team, Skill, Training, Coverage, Fatigue

**Internal relationships**:
- Person → (holds) → Role
- Role → (defines) → Responsibility
- Team → (contains) ← Persons
- Skill → (enables) ← Task
- Training → (develops) ← Skill
- Coverage → (provides backup) ← Person

**External connections**:
- Person → (executes) ← Task
- Person → (assigned to) ← Station
- Skill → (required by) ← Equipment
- Fatigue → (limits) ← Capacity

**Cluster characteristic**: This is the human engine. It executes all work and provides adaptability that equipment cannot.

### 5. The Constraint Cluster

**Entities in cluster**: Time Window, Food Safety, Temperature Control, Capacity Limit, Par Level, Economic Margin

**Internal relationships**:
- Time Window → (bounds) ← Service
- Food Safety → (requires) ← Temperature Control
- Capacity Limit → (constrains) ← Throughput
- Par Level → (determines) ← Inventory Target
- Economic Margin → (requires) ← Cost Control

**External connections**:
- Time Window → (affects) ← Task Scheduling
- Food Safety → (enforced by) ← Compliance
- Capacity Limit → (imposed by) ← Equipment/Space
- Economic Margin → (monitored by) ← Management

**Cluster characteristic**: This cluster defines the boundaries within which the system must operate. It is non-negotiable.

### 6. The Adaptation Cluster

**Entities in cluster**: Problem, Escalation, Recovery, Reallocation, Exception, Backup

**Internal relationships**:
- Problem → (triggers) ← Escalation
- Escalation → (authorizes) ← Recovery
- Recovery → (involves) ← Reallocation
- Exception → (requires) ← Modified Procedure
- Backup → (provides) ← Coverage

**External connections**:
- Problem ← (identifies) ← Monitoring
- Escalation → (to) ← Higher Authority
- Recovery → (restores) ← Normal Operation
- Reallocation → (shifts) ← Person/Equipment

**Cluster characteristic**: This cluster handles variation and disruption. It is activated when the designed system encounters the unexpected.

---

# V. Centrality Analysis

## Which Entities Are Most Connected

### High-Centrality Entities (Network Hubs)

These entities have the most connections and are critical to workflow function:

**1. Station**
- Connections: 15+ (to equipment, people, materials, flow paths, zones)
- Role: Junction point where materials, equipment, and people converge
- Impact: Station failure cascades to multiple dependent processes

**2. Ticket**
- Connections: 10+ (to customer, POS, rail, cook, expo, server, recipe, timing)
- Role: The work unit that drives all kitchen activity
- Impact: Ticket errors or delays propagate throughout the system

**3. Line Cook**
- Connections: 12+ (to station, equipment, ticket, communication, expo, recipe, support)
- Role: Primary executor of transformation work
- Impact: Cook performance directly determines throughput and quality

**4. Prep**
- Connections: 10+ (to ingredients, stations, recipes, storage, timing)
- Role: Foundation that enables all service activity
- Impact: Prep shortfalls cascade into service failures

**5. Equipment**
- Connections: 8+ (to station, transformation, maintenance, capacity, recipe)
- Role: Enables specific transformations
- Impact: Equipment failure stops related work entirely

### Medium-Centrality Entities (Important Connectors)

**6. Expo**
- Connections: 8 (to tickets, line, pass, servers, quality, timing)
- Role: Coordination hub during service
- Impact: Coordinates but does not directly execute transformation

**7. Communication**
- Connections: 7 (to people, tickets, status, problems)
- Role: Information transfer
- Impact: Communication failure causes coordination failures

**8. Storage (Walk-in)**
- Connections: 7 (to ingredients, prep, line, holding, temperature)
- Role: Buffer between prep and service
- Impact: Storage issues cause timing or quality problems

**9. Recipe**
- Connections: 6 (to ingredients, equipment, technique, quality, modifications)
- Role: Knowledge specification
- Impact: Recipe errors cause execution errors

**10. Time Window**
- Connections: 6 (to prep, service, tasks, staffing, ingredients)
- Role: Temporal boundary
- Impact: Window violations cause service failures

### Low-Centrality Entities (Specialized)

**11. Customer**
- Connections: 4 (to ticket, finished plate, server, satisfaction)
- Role: External endpoint and revenue source
- Impact: Indirect—customer behavior affects demand but not internal workflow

**12. Supplier**
- Connections: 3 (to ingredients, inventory, par level)
- Role: External input source
- Impact: Supply chain disruptions affect availability

---

# VI. Structural Patterns

## Recurring Network Architectures

### 1. The Linear Chain Pattern

**Structure**: A → B → C → D (each step depends on the previous)

**Example**: Ingredient → Prep → Cook → Plate → Serve

**Properties**:
- Simple dependency tracking
- Critical path is linear
- Delay at any step delays entire chain
- Easy to identify bottleneck

**Design implication**: Protect critical path with buffers or redundancy

### 2. The Convergence Pattern

**Structure**: A, B, C, D → E (multiple inputs combine into one)

**Example**: Proteins, starches, vegetables, sauce → Finished Plate

**Properties**:
- High coordination requirement
- Timing must synchronize multiple streams
- One late input delays entire output
- Quality of each input affects final quality

**Design implication**: Explicit timing synchronization and hold buffers for each stream

### 3. The Divergence Pattern

**Structure**: A → B, C, D, E (one input feeds multiple outputs)

**Example**: Roasted chicken → Chicken breast, thigh, wings, stock bones

**Properties**:
- Yield optimization opportunity
- Scheduling must balance multiple outputs
- Quality at split point determines all downstream quality

**Design implication**: Plan splits to match downstream demand

### 4. The Parallel Streams Pattern

**Structure**: A1 → B1; A2 → B2; A3 → B3 (simultaneous independent operations)

**Example**: Grill station, sauté station, and fry station operating simultaneously

**Properties**:
- Enables throughput
- Each stream has its own critical path
- Cross-stream resource sharing creates dependencies
- Coordination required for synchronized completion

**Design implication**: Balance stream capacities and provide cross-stream coordination

### 5. The Mesh Pattern

**Structure**: Multiple connections between multiple nodes (complex interdependency)

**Example**: Multiple stations sharing equipment, sharing prep, sharing expo

**Properties**:
- High flexibility
- Multiple paths to achieve outcomes
- Coordination complexity increases
- Failure modes multiply

**Design implication**: Map all connections and identify single points of failure

### 6. The Star Pattern

**Structure**: Hub connected to multiple spokes; spokes do not directly connect

**Example**: Chef at center; line cooks at periphery; cooks do not directly coordinate with each other

**Properties**:
- Clear authority structure
- Information bottleneck at hub
- Slower lateral communication
- Simpler but less flexible

**Design implication**: Ensure hub has capacity for all coordination demands

### 7. The Hub-and-Spoke with Cross-Talk Pattern

**Structure**: Star with additional lateral connections for flexibility

**Example**: Chef at center; line cooks communicate through chef AND directly with each other

**Properties**:
- Combines clarity with flexibility
- Additional coordination overhead
- Faster lateral communication
- More resilient to hub unavailability

**Design implication**: Define which communications flow through hub vs. direct

---

# VII. Dependency Mapping

## What Depends on What

### Hard Dependencies (Must Be Satisfied)

| Dependency | From | To | Consequence if Broken |
|------------|------|----|----------------------|
| Ingredient availability | Recipe | Plate | Cannot produce dish |
| Prep completion | Prep | Cooking | Cannot start cooking |
| Cooking completion | Cooking | Plating | Cannot plate |
| Temperature compliance | Food safety | Any holding | Regulatory violation |
| Equipment function | Equipment | Use | Cannot perform operation |

### Soft Dependencies (Should Be Satisfied)

| Dependency | From | To | Consequence if Broken |
|------------|------|----|----------------------|
| Timing synchronization | Multiple stations | Expo | Plates ready at different times |
| Par levels | Inventory | Service | Run out during service |
| Station readiness | Mise en place | Service start | Slow start to service |
| Communication | Team members | Coordination | Errors and delays |

### Preference Dependencies (Better if Satisfied)

| Dependency | From | To | Consequence if Broken |
|------------|------|----|----------------------|
| Ideal equipment timing | Recipe | Equipment schedule | Suboptimal but possible |
| Preferred person for task | Skill | Task assignment | Less efficient but doable |
| Perfect freshness | Ingredient age | Quality | Acceptable if within window |

---

# VIII. Network Resilience

## What Happens When Nodes Fail

### Single Point of Failure Identification

**Critical Single Points**:
1. **Head Chef** — Without decision authority, coordination degrades
2. **Key Equipment** (single oven, single fryer) — Related production stops
3. **Walk-in Refrigeration** — All cold storage and prep affected
4. **Expo during service** — Coordination and quality checking breaks down
5. **Main cooking equipment** — Core transformation impossible

**Redundant Elements** (multiple options):
- Prep stations (can share work)
- Line cooks (cross-training allows coverage)
- Communication methods (verbal, visual, ticket)
- Ingredient substitutes (when available)

### Failure Cascade Patterns

**Equipment Failure Cascade**:
```
Single Fryer Fails
       │
       ▼
Fry Station Cannot Operate
       │
       ├──► Fried items unavailable (menu impact)
       │
       ├──► Other stations overwhelmed (load shift)
       │
       └──► Tickets delayed (timing impact)
```

**Personnel Failure Cascade**:
```
Line Cook Calls Out
       │
       ▼
Station Uncovered
       │
       ├──► Backup cook shifts (coverage)
       │
       ├──► Original cook's tasks redistributed (load)
       │
       ├──► If no backup: tasks delayed or eliminated (service impact)
       │
       └──► If service impact: customer satisfaction affected
```

**Coordination Failure Cascade**:
```
Communication Breakdown
       │
       ▼
Handoff Fails
       │
       ├──► Items not ready when needed (timing)
       │
       ├──► Quality not checked (quality)
       │
       ├──► Duplicated work (waste)
       │
       └──► Wrong items sent (errors)
```

### Resilience Mechanisms

**Built-in Redundancy**:
- Cross-trained staff
- Multiple cooking methods for same items
- Backup equipment (when available)
- Shared station space

**Buffer Capacity**:
- Prep ahead (time buffer)
- Hold space in walk-in (storage buffer)
- Extra equipment (capacity buffer)
- Backup staff on call (human buffer)

**Fast Recovery Paths**:
- Escalation procedures
- Equipment repair contacts
- Menu simplification options
-