# The Copper Beech Daily Workflow Constructor

## Complete Operational Instance Specification

### Version: 1.0.0  
### Position: L0P3W[2] — Specifically Reify · Specifically Reify (Make THIS) · EMISSION  
### Instance: Copper Beech Cafe, 42-seat capacity, 4 staff  
### Built: 2024-01-15  

---

## Document Identity

**Artifact Name**: Copper Beech Daily Workflow Constructor — Operational Instance  
**Version**: 1.0.0  
**Domain**: Small Commercial Kitchen, American Breakfast/Lunch Service  
**Target Kitchen**: Copper Beech Cafe  
**Seating Capacity**: 42 seats  
**Service Hours**: 7:00 AM — 2:00 PM  
**Staff Complement**: Maria (Chef), James (Line Cook), Elena (Prep Cook), Marcus (Support)  
**Configuration Status**: DEPLOYED  

---

## Part I: Constructor Identity and Purpose

### 1.1 What This Constructor Is

The Copper Beech Daily Workflow Constructor is a generative apparatus that transforms the accumulated operational knowledge of Copper Beech Cafe into concrete daily workflow instances. It stands between each morning's arrival and that day's service—producing the guidance that enables Maria and the team to execute consistently, safely, and effectively.

This is not a template. A template produces identical outputs for identical inputs. The Constructor produces *different* workflows for *different* days—high volume Saturday workflows differ from low volume Tuesday workflows; full-staff workflows differ from reduced-staff workflows; post-holiday workflows differ from ordinary workflows. The Constructor's value lies in this responsiveness.

The Constructor is also not static. It incorporates every day's execution into its knowledge base, extracting patterns from feedback, generating hypotheses for improvement, and—after Maria's validation—integrating validated learning into its generative capacity. The Constructor improves through use.

### 1.2 The Problems This Constructor Solves

**The Cognitive Burden Problem**: Every morning, someone must answer: What do we do today? This question encompasses dozens of subsidiary questions—tasks to complete, order of completion, who does what, when tasks begin, how to handle volume, which protocols activate, what might go wrong. For four years, Maria has answered these questions from memory. The Constructor bears this cognitive burden so Maria can focus on execution and quality rather than planning.

**The Consistency Problem**: Manual planning is inherently variable. Some days produce excellent workflows; other days, fatigue or distraction or unusual circumstances produce gaps. The 47 tasks of a daily workflow are too numerous for perfect mental management every day. The Constructor provides consistent planning quality—every day receives the same thoughtful attention, informed by accumulated experience.

**The Learning Problem**: Manual planning cannot capture what it does not know it is learning. When Elena reduces her produce prep time, this improvement exists in her hands but not in any shared record. When James's efficiency improves, this learning exists in his experience but not in systematic form. The Constructor creates a vessel for operational learning—a structure that captures insights and applies them to future generations.

### 1.3 The Constructor's Mode of Being

The Constructor exists in a distinctive mode: it is **both tool and organism, both artifact and living pattern**.

As **tool**, it is designed, built, and maintained. It has specifications, version numbers, and deployment configurations. It can be inspected, modified, and replaced. Maria's workstation runs the Electron application; the pattern library resides in JSON files; the feedback archive sits in SQLite.

As **organism**, it grows, adapts, and learns. It participates in cycles of generation and feedback. It has a kind of persistence through change—maintaining identity while continuously modifying its knowledge structures. When TP_004's duration changes from 25 to 30 minutes, the Constructor is still the Constructor; it has simply learned something.

This dual nature is not a contradiction but a synthesis. The Constructor achieves its purpose precisely by embodying this tension.

---

## Part II: Hard Constraints — The Invariants

These constraints define the boundary of acceptable generation. The Constructor MUST enforce these constraints without exception. No stakeholder, including Maria, may override a hard constraint. These are not preferences but requirements.

### HC_001: Food Safety Temperature Control

**Constraint ID**: HC_001  
**Name**: Food Safety Temperature Control  
**Definition**: Food must not remain in the temperature danger zone (40°F-140°F) for more than 2 hours cumulative time.  
**Danger Zone**: 40°F through 140°F  
**Maximum Cumulative Time**: 120 minutes  
**Verification Method**: Time-temperature tracking for all prep and holding operations

**Enforcement Requirements**:
- All prep items must enter prep cycle at or below 40°F
- Hot holding must maintain items at or above 140°F
- Cumulative time in danger zone tracked for all items
- Prep cycles must complete with sufficient time before service expiration
- Any item exceeding 2-hour cumulative danger zone time must be discarded

**Implications for Workflow Generation**:
- Task timing must account for temperature transitions
- Hot holding tasks must include discard timers
- Prep tasks must be sequenced to prevent temperature abuse
- The Constructor cannot assign tasks that would cause HC_001 violation

**Verification Checkpoints**:
- Egg retrieval: Temperature verified below 40°F
- Prep completion: All prepped items properly refrigerated or held hot
- Hot holding: Temperatures checked and logged every 30 minutes
- Service: Items held hot or plated within time limits

---

### HC_002: Cross-Contamination Prevention

**Constraint ID**: HC_002  
**Name**: Cross-Contamination Prevention  
**Definition**: Raw animal proteins and ready-to-eat foods must be completely separated to prevent cross-contamination. Allergen-containing items must not contact allergen-free items without proper disclosure.

**Enforcement Requirements**:
- Color-coded cutting boards enforced: GREEN (produce/dairy), RED (raw meat/poultry), YELLOW (cooked items), BLUE (seafood)
- Allergen isolation equipment available: dedicated utensils, separate plating area, communication protocols
- Handwashing required between handling raw and ready-to-eat items
- Equipment sanitization required between different food types

**Implications for Workflow Generation**:
- Task assignments must specify correct color board
- Station setup must include proper board placement
- Allergen orders must receive isolated handling protocol
- The Constructor cannot assign tasks that would cause HC_002 violation

**Verification Checkpoints**:
- Opening: All color boards in correct positions
- Prep: Each task assigned correct board color
- Service: Allergen orders receive isolated handling
- Closing: All boards properly sanitized

---

### HC_003: Minimum Staffing Levels

**Constraint ID**: HC_003  
**Name**: Minimum Staffing Levels  
**Definition**: A minimum of 3 staff members must be present during all service operations. Service cannot begin or continue with fewer than 3 staff.

**Staff Roles Required for Service**:
- 1 Chef (Maria) or qualified backup
- 1 Line Cook (James) or qualified backup
- 1 Prep Cook (Elena) or qualified backup
- 1 Support Staff (Marcus) recommended but optional during service

**Enforcement Requirements**:
- Staff count verified at service start
- Staff count monitored throughout service
- Service reduction protocol if staff drops below minimum
- No service initiation without HC_003 compliance

**Implications for Workflow Generation**:
- Workflows cannot be generated for configurations with fewer than 3 staff
- Service phases must have minimum 3 assigned staff
- Coverage plans must account for potential absences
- The Constructor cannot generate workflows that violate HC_003

**Verification Checkpoints**:
- 6:45 AM: All scheduled staff confirmed present
- 7:00 AM: Service start verification (3+ staff)
- Throughout service: Staff count monitoring
- Emergency: Service reduction if staff drops below minimum

---

### HC_004: Time-Temperature Combinations for Prep Items

**Constraint ID**: HC_004  
**Name**: Time-Temperature Combinations  
**Definition**: No prep item may remain in the production pipeline for more than 4 hours from initial prep start to final use in service. Prep items prepared too early create both safety and quality risks.

**Maximum Prep Pipeline Duration**: 240 minutes (4 hours)

**Enforcement Requirements**:
- Prep start times must allow completion within 4-hour window
- Batch refresh protocols for items approaching time limit
- Discard protocols for items exceeding 4-hour limit
- Time tracking from prep initiation to service use

**Implications for Workflow Generation**:
- Prep timing must align with expected service start
- Prep quantities must match anticipated demand
- Prep refresh schedules must be embedded in workflows
- The Constructor cannot assign prep tasks that would cause HC_004 violation

**Verification Checkpoints**:
- 5:45 AM: First prep tasks begin
- Throughout prep: Time tracking for all items
- Service start: Items prepared within 4-hour window
- Throughout service: Refresh batches as needed

---

## Part III: Pattern Library — The Constructor's Memory

The pattern library encodes the accumulated operational knowledge of Copper Beech Cafe. It contains task patterns (atomic units of work), workflow patterns (complete operational sequences), constraint definitions, and adaptation protocols.

### 3.1 Task Patterns

Task patterns are reusable templates encoding atomic units of work. Each pattern specifies what must be done, how long it takes, who typically does it, what equipment it requires, and what constraints apply.

#### Prep Task Patterns

---

**TASK PATTERN TP_001: Standard Egg Prep**

| Field | Value |
|-------|-------|
| Pattern ID | TP_001 |
| Name | Standard Egg Prep |
| Duration | 15 minutes |
| Assigned Roles | prep_cook |
| Typical Assignee | Elena |
| Color Board | GREEN |
| Category | prep |
| Inputs | eggs, butter, seasoning |
| Outputs | prepped_eggs |
| Allergen Flags | dairy |
| Dependencies | OT_002 (Egg Retrieval) |
| Version | 1 |
| Learning Source | Elena efficiency improvement 2024-10-20 |

**Procedure**:
1. Retrieve eggs from refrigerated storage
2. Crack eggs into sanitized bowls (6 per batch)
3. Season lightly with salt and white pepper
4. Store in covered containers at 40°F
5. Label with prep time and expiration (4 hours)
6. Stage for service use

**Success Criteria**:
- 45 eggs prepped in 15 minutes
- All eggs at 40°F or below
- Prep completed by 6:05 AM
- Prep time logged for HC_004 tracking

---

**TASK PATTERN TP_002: Bacon Portioning**

| Field | Value |
|-------|-------|
| Pattern ID | TP_002 |
| Name | Bacon Portioning |
| Duration | 20 minutes |
| Assigned Roles | prep_cook |
| Typical Assignee | Elena |
| Color Board | RED |
| Category | prep |
| Inputs | raw_bacon |
| Outputs | portioned_bacon |
| Allergen Flags | none |
| Dependencies | OT_001 (Equipment Preheating — fryer) |
| Version | 1 |

**Procedure**:
1. Portion bacon strips for expected orders (2 strips per egg dish)
2. Fry bacon in batches until crispy (350°F fryer)
3. Drain on paper towels
4. Store in heated holding area (above 140°F)
5. Track time in hot holding for HC_001

**Success Criteria**:
- Bacon portioned and cooked by 6:15 AM
- Hot holding above 140°F
- Bacon accessible for service start
- Canadian bacon portions identified separately (limited supply)

---

**TASK PATTERN TP_003: Produce Prep**

| Field | Value |
|-------|-------|
| Pattern ID | TP_003 |
| Name | Produce Prep |
| Duration | 30 minutes |
| Assigned Roles | prep_cook |
| Typical Assignee | Elena |
| Color Board | GREEN |
| Category | prep |
| Inputs | tomatoes, lettuce, onions, fresh_herbs |
| Outputs | prepped_produce |
| Allergen Flags | none |
| Dependencies | OT_003 (Inventory Check) |
| Version | 1 |
| Learning Source | Elena timing adjustment 2024-10-20 |

**Procedure**:
1. Slice tomatoes for sandwiches and plating (24 tomatoes)
2. Chop lettuce for salads and sandwiches (2 heads)
3. Dice onions for omelettes and hash browns (6 onions)
4. Prepare garnishes (herb bundles, lemon wedges)
5. Store in sanitized containers at 40°F
6. Minimize waste (target < 5%)

**Success Criteria**:
- All produce prepped by 6:30 AM
- Station ready for service
- Minimal waste achieved

**Note**: Elena's historical timing is 25 minutes; 30 minutes allocated to allow for quality checks Maria values.

---

**TASK PATTERN TP_004: Hash Brown Preparation**

| Field | Value |
|-------|-------|
| Pattern ID | TP_004 |
| Name | Hash Brown Preparation |
| Duration | 30 minutes |
| Assigned Roles | prep_cook |
| Typical Assignee | Elena |
| Color Board | GREEN |
| Category | prep |
| Inputs | shredded_potatoes, seasonings |
| Outputs | hash_brown_patties |
| Allergen Flags | none |
| Dependencies | OT_001 (Equipment Preheating — fryer) |
| Version | 2 |
| Learning Source | Statistical pattern — updated from 25 to 30 minutes 2025-03-24 |

**Procedure**:
1. Season shredded potatoes
2. Press into hash brown patties
3. Fry in batches until golden brown (350°F fryer)
4. Drain and hold in warming area
5. Track time in hot holding for HC_001
6. Produce 50 patties

**Success Criteria**:
- Hash browns cooked through and crispy
- Held at proper temperature (above 140°F)
- Completed by 6:45 AM

**Note**: Duration updated from 25 to 30 minutes based on 12 instances of observed timing (mean +4.9 minutes deviation). Maria approved integration 2025-03-21.

---

**TASK PATTERN TP_005: Hollandaise Preparation**

| Field | Value |
|-------|-------|
| Pattern ID | TP_005 |
| Name | Hollandaise Preparation |
| Duration | 15 minutes |
| Assigned Roles | chef |
| Typical Assignee | Maria |
| Color Board | Not applicable |
| Category | prep |
| Inputs | egg_yolks, butter, lemon_juice, cayenne |
| Outputs | hollandaise_sauce |
| Allergen Flags | dairy, eggs |
| Dependencies | OT_001 (Equipment Preheating), OT_003 (Inventory Check) |
| Version | 1 |

**Procedure**:
1. Clarify butter in small batches
2. Whisk egg yolks over gentle heat (bain-marie)
3. Slowly incorporate clarified butter
4. Season with lemon juice and cayenne
5. Hold in thermos at 150°F for service
6. Maria taste test before service

**Success Criteria**:
- Sauce emulsified properly (no break)
- Holding temperature 140-150°F
- Quality confirmed by Maria taste test

**Note**: This is Maria's signature preparation. Quality control is critical.

---

#### Service Task Patterns

---

**TASK PATTERN ST_001: Execute Egg Order**

| Field | Value |
|-------|-------|
| Pattern ID | ST_001 |
| Name | Execute Egg Order |
| Duration | 8 minutes |
| Assigned Roles | line_cook, chef |
| Typical Assignees | James (primary), Maria (backup) |
| Color Board | GREEN |
| Category | service |
| Inputs | prepped_eggs, plating_supplies |
| Outputs | plated_eggs |
| Allergen Flags | dairy, eggs (varies) |
| SLA Target | 10 minutes (customer wait time) |
| Dependencies | Opening prep complete |
| Version | 1 |

**Procedure**:
1. Receive ticket at station
2. Fire eggs on griddle (medium-high heat, 375°F)
3. Cook to order specification (fried, scrambled, poached)
4. Plate with appropriate presentation
5. Quality check by expeditor
6. Hand off to server

**Success Criteria**:
- Eggs cooked to order specification
- Plated within 8 minutes
- Quality check complete before handoff

---

**TASK PATTERN ST_002: Execute Benedict Order**

| Field | Value |
|-------|-------|
| Pattern ID | ST_002 |
| Name | Execute Benedict Order |
| Duration | 12 minutes |
| Assigned Roles | line_cook, chef |
| Typical Assignees | James (griddle), Maria (hollandaise/expediting) |
| Color Board | GREEN |
| Category | service |
| Inputs | english_muffin, canadian_bacon, poached_eggs, hollandaise |
| Outputs | plated_benedict |
| Allergen Flags | dairy, eggs, gluten |
| SLA Target | 15 minutes |
| Dependencies | Opening prep complete, hollandaise prepared |
| Version | 1 |

**Procedure**:
1. Receive ticket at station
2. Toast english muffin halves
3. Warm canadian bacon on griddle
4. Poach eggs (simmering water, 3 minutes)
5. Assemble: muffin, bacon, poached egg
6. Ladle hollandaise over eggs
7. Garnish and plate
8. Quality check by Maria
9. Hand off to server

**Success Criteria**:
- Eggs poached correctly (yolk runny)
- Hollandaise properly emulsified
- Plated within 12 minutes
- Maria quality check complete before handoff

**Note**: Canadian bacon is LOW this day. Monitor orders and may need substitution offer if supply exhausted.

---

**TASK PATTERN ST_003: Execute Griddle Item Order**

| Field | Value |
|-------|-------|
| Pattern ID | ST_003 |
| Name | Execute Griddle Item Order |
| Duration | 10 minutes |
| Assigned Roles | line_cook |
| Typical Assignee | James |
| Color Board | GREEN |
| Category | service |
| Inputs | pancake_batter, french_toast_batter, bread |
| Outputs | plated_griddle_items |
| Allergen Flags | dairy, eggs, gluten (varies) |
| SLA Target | 12 minutes |
| Dependencies | Opening prep complete |
| Version | 1 |

**Procedure**:
1. Receive ticket at station
2. Fire griddle items first (longest cook time)
3. Cook pancakes (2-3 minutes per side)
4. Cook french toast (2-3 minutes per side)
5. Toast bread for breakfast sandwich
6. Plate with appropriate accompaniments
7. Quality check
8. Hand off to server

**Success Criteria**:
- Items cooked to golden brown
- Plated within 10 minutes
- Accompaniments complete

---

**TASK PATTERN ST_004: Execute Omelette Order**

| Field | Value |
|-------|-------|
| Pattern ID | ST_004 |
| Name | Execute Omelette Order |
| Duration | 10 minutes |
| Assigned Roles | line_cook, chef |
| Typical Assignees | James (primary), Maria (backup) |
| Color Board | GREEN |
| Category | service |
| Inputs | prepped_eggs, fillings, cheese |
| Outputs | plated_omelette |
| Allergen Flags | dairy, eggs (varies by fillings) |
| SLA Target | 12 minutes |
| Dependencies | Opening prep complete |
| Version | 1 |

**Procedure**:
1. Receive ticket at station (note omelette variety)
2. Fire omelette on griddle (medium heat)
3. Add fillings as specified
4. Fold and plate
5. Quality check
6. Hand off to server

**Omelette Varieties**:
- Western: Ham, peppers, onions, cheese
- Veggie: Peppers, onions, mushrooms, tomatoes, cheese
- Cheese: Cheddar, swiss, or american
- Meat Lovers: Bacon, ham, sausage, cheese
- Fiesta: Chorizo, peppers, onions, jalapeños, cheese
- Mediterranean: Spinach, feta, tomatoes, olives
- Denver: Ham, peppers, onions, cheese
- Custom: As specified

---

**TASK PATTERN ST_005: Execute Lunch Sandwich Order**

| Field | Value |
|-------|-------|
| Pattern ID | ST_005 |
| Name | Execute Lunch Sandwich Order |
| Duration | 6 minutes |
| Assigned Roles | line_cook, support |
| Typical Assignees | James (primary), Marcus (assembly) |
| Color Board | varies |
| Category | service |
| Inputs | bread, protein, toppings, condiments |
| Outputs | plated_sandwich |
| Allergen Flags | gluten, dairy, eggs (varies) |
| SLA Target | 8 minutes |
| Dependencies | Lunch menu active |
| Version | 1 |

**Procedure**:
1. Receive ticket at station
2. Prepare bread (toast if needed)
3. Apply condiments
4. Layer protein and toppings
5. Slice and plate
6. Quality check
7. Hand off to server

**Success Criteria**:
- Sandwich properly assembled
- Plated within 6 minutes
- Presentation clean

---

**TASK PATTERN ST_006: Execute Salad Order**

| Field | Value |
|-------|-------|
| Pattern ID | ST_006 |
| Name | Execute Salad Order |
| Duration | 5 minutes |
| Assigned Roles | prep_cook, support |
| Typical Assignees | Elena (assembly), Marcus (plating) |
| Color Board | GREEN |
| Category | service |
| Inputs | greens, toppings, protein, dressing |
| Outputs | plated_salad |
| Allergen Flags | varies |
| SLA Target | 7 minutes |
| Dependencies | Lunch menu active |
| Version | 1 |

**Procedure**:
1. Receive ticket at station
2. Select appropriate greens
3. Add toppings and protein as ordered
4. Toss or present as specified
5. Add dressing (side or tossed)
6. Quality check
7. Hand off to server

**Success Criteria**:
- Greens fresh and properly portioned
- Plated within 5 minutes
- Presentation appealing

---

#### Closing Task Patterns

---

**TASK PATTERN CT_001: Station Breakdown**

| Field | Value |
|-------|-------|
| Pattern ID | CT_001 |
| Name | Station Breakdown |
| Duration | 30 minutes |
| Assigned Roles | chef, line_cook |
| Typical Assignees | Maria, James |
| Color Board | varies |
| Category | closing |
| Dependencies | Service ended |
| Version | 1 |

**Procedure**:
1. Allow equipment to cool slightly (5 minutes)
2. Remove food debris from cooking surfaces
3. Disassemble station components
4. Clean griddle (steel wool, then oil)
5. Clean fryer (filter, clean)
6. Sanitize all surfaces
7. Reassemble for next day

**Success Criteria**:
- All cooking stations clean and sanitized
- Equipment properly maintained
- Ready for next day setup

---

**TASK PATTERN CT_002: Kitchen Cleaning**

| Field | Value |
|-------|-------|
| Pattern ID | CT_002 |
| Name | Kitchen Cleaning |
| Duration | 30 minutes |
| Assigned Roles | prep_cook, support |
| Typical Assignees | Elena, Marcus |
| Color Board | varies |
| Category | closing |
| Dependencies | Station breakdown complete |
| Version | 1 |

**Procedure**:
1. Clean prep areas (counters, cutting boards)
2. Mop kitchen floors
3. Clean and organize walk-in cooler
4. Take out trash and recyclables
5. Restock supplies for next day
6. Final walkthrough inspection

**Success Criteria**:
- All prep areas clean and sanitized
- Floors clean
- Walk-in organized
- Next day supplies restocked

---

### 3.2 Workflow Patterns

Workflow patterns are complete operational sequences that can be instantiated for specific days. Each workflow pattern specifies which task patterns to include, their temporal relationships, and how they group into phases.

---

**WORKFLOW PATTERN WP_001: Standard Opening Sequence**

| Field | Value |
|-------|-------|
| Pattern ID | WP_001 |
| Name | Standard Opening Sequence |
| Type | opening |
| Target Completion | 6:45 AM |
| Service Ready | 6:55 AM |
| Version | 1 |

**Task Sequence**:

| Sequence | Task | Start Time | Duration | Assignee |
|----------|------|------------|----------|----------|
| 1 | OT_001 — Equipment Preheating | 5:30 AM | 15 min | Maria |
| 2 | OT_002 — Egg Retrieval | 5:35 AM | 10 min | Elena |
| 3 | OT_003 — Inventory Check | 5:45 AM | 20 min | Maria, Elena |
| 4 | TP_001 — Standard Egg Prep | 5:50 AM | 15 min | Elena |
| 5 | TP_002 — Bacon Portioning | 5:55 AM | 20 min | Elena |
| 6 | TP_003 — Produce Prep | 6:00 AM | 30 min | Elena |
| 7 | TP_005 — Hollandaise | 6:00 AM | 15 min | Maria |
| 8 | TP_004 — Hash Browns | 6:15 AM | 30 min | Elena |
| 9 | OT_009 — English Muffin/Bread | 6:20 AM | 10 min | Maria |
| 10 | OT_010 — Station Setup | 6:30 AM | 15 min | Maria, James |
| 11 | OT_011 — Pre-Service Check | 6:40 AM | 5 min | Maria |

**Phases**:
- Preheat (5:30-5:45): Equipment heating
- Inventory (5:45-6:00): Stock verification
- Production (6:00-6:30): Food preparation
- Setup (6:30-6:40): Station arrangement
- Final (6:40-6:45): Quality verification

**Applicable Volume Tiers**: low, medium, high  
**Applicable Day Types**: weekday, weekend  

---

**WORKFLOW PATTERN WP_002: Standard Service Sequence**

| Field | Value |
|-------|-------|
| Pattern ID | WP_002 |
| Name | Standard Service Sequence |
| Type | service |
| Target Start | 7:00 AM |
| Target End | 2:00 PM |
| Version | 1 |

**Service Phases**:

| Phase | Start | End | Duration | Expected Volume | Protocols |
|-------|-------|-----|----------|-----------------|-----------|
| Early Service | 7:00 AM | 9:00 AM | 120 min | 10-15 tickets | Standard, AP_005 (standing) |
| Peak Service | 9:00 AM | 11:30 AM | 150 min | 20-25 tickets | High Volume, AP_001 (conditional) |
| Lunch Transition | 11:30 AM | 12:00 PM | 30 min | 5-10 tickets | Lunch Protocol |
| Lunch Service | 12:00 PM | 2:00 PM | 120 min | 10-15 tickets | Wind-Down |

**Applicable Volume Tiers**: low, medium, high  
**Applicable Day Types**: weekday  

---

**WORKFLOW PATTERN WP_003: High Volume Service Sequence**

| Field | Value |
|-------|-------|
| Pattern ID | WP_003 |
| Name | High Volume Service Sequence |
| Type | service |
| Target Start | 7:00 AM |
| Target End | 2:00 PM |
| Version | 1 |

**Service Phases**:

| Phase | Start | End | Duration | Expected Volume | Protocols |
|-------|-------|-----|----------|-----------------|-----------|
| Early Service | 7:00 AM | 8:45 AM | 105 min | 15-20 tickets | Standard, AP_005 (standing) |
| Peak Service | 8:45 AM | 11:30 AM | 165 min | 35-45 tickets | High Volume, AP_001 (active) |
| Lunch Transition | 11:30 AM | 12:00 PM | 30 min | 10-15 tickets | Lunch Protocol |
| Lunch Service | 12:00 PM | 2:00 PM | 120 min | 15-20 tickets | Wind-Down |

**Differences from WP_002**:
- Peak service begins 15 minutes earlier (8:45 vs 9:00)
- Peak service duration extended to handle volume
- AP_001 (High Volume Response) active from start
- Elena assists with plating during peak

**Applicable Volume Tiers**: high, extreme  
**Applicable Day Types**: weekend  

---

**WORKFLOW PATTERN WP_004: Standard Closing Sequence**

| Field | Value |
|-------|-------|
| Pattern ID | WP_004 |
| Name | Standard Closing Sequence |
| Type | closing |
| Target Completion | 3:00 PM |
| Version | 1 |

**Task Sequence**:

| Sequence | Task | Start Time | Duration | Assignee |
|----------|------|------------|----------|----------|
| 1 | CT_001 — Hot Holding Shutdown | 2:00 PM | 5 min | Maria, James |
| 2 | CT_002 — Station Breakdown | 2:05 PM | 30 min | Maria, James |
| 3 | CT_003 — Kitchen Cleaning | 2:05 PM | 30 min | Elena, Marcus |
| 4 | CT_004 — Equipment Shutdown | 2:35 PM | 10 min | Maria |
| 5 | CT_005 — Storage/Organization | 2:35 PM | 15 min | Elena |
| 6 | CT_006 — Final Walkthrough | 2:50 PM | 10 min | Maria |

**Phase Overlap**: Station breakdown (2:05-2:35) and kitchen cleaning (2:05-2:35) run concurrently.

---

### 3.3 Adaptation Protocols

Adaptation protocols are triggered response procedures that modify workflow generation or execution based on specific conditions.

---

**PROTOCOL AP_001: High Volume Response**

| Field | Value |
|-------|-------|
| Protocol ID | AP_001 |
| Name | High Volume Response |
| Type | Conditional |
| Version | 1 |

**Trigger Condition**:
```
tickets_in_queue > 8
```

**Threshold**: 8 tickets in queue  
**Monitored Metric**: queue_depth  
**Check Frequency**: Every 5 minutes during service

**Response Actions**:

| Action Type | From | To | Target | Description |
|-------------|------|-----|--------|-------------|
| reassign | James | Maria | griddle_primary | Maria moves to griddle primary |
| reassign | Maria | James | quality_control | James moves to quality backup |
| accelerate | phase | peak_service | timing | Peak service timing accelerates 15 minutes |
| assist | Elena | plating | as_needed | Elena assists with plating if needed |

**Activation Procedure**:
1. Monitor queue depth during peak service
2. When queue exceeds 8 tickets for more than 5 minutes, activate protocol
3. Maria receives notification
4. Maria announces reassignment to team
5. James transitions to quality backup
6. Maria assumes griddle primary
7. Elena prepares to assist with plating
8. Peak service timing accelerates

**Deactivation Criteria**:
- Queue depth returns below 5 tickets
- Average ticket time under 10 minutes

**Deactivation Procedure**:
1. Maria announces return to standard configuration
2. James returns to griddle primary
3. Maria returns to expediting/quality control

**Recording**: All activations logged for pattern extraction.

---

**PROTOCOL AP_002: Equipment Failure Response**

| Field | Value |
|-------|-------|
| Protocol ID | AP_002 |
| Name | Equipment Failure Response |
| Type | Standing |
| Version | 1 |

**Trigger Condition**:
```
equipment.status == "unavailable"
```

**Standing Protocol**: Activates immediately when equipment becomes unavailable

**Response Actions**:

| Action Type | Description |
|-------------|-------------|
| assess | Assess impact on menu items |
| notify | Notify Maria immediately |
| substitute | Activate substitution menu if needed |
| document | Document incident for review |

**Equipment-Specific Responses**:

| Equipment | Menu Impact | Substitution |
|-----------|-------------|--------------|
| GRIDDLE_1 | All griddle items | Reduced menu; eggs poached only |
| FRYER_1 | Hash browns, bacon | Hash browns pan-fried; bacon limited |
| OVEN_1 | Benedict muffins, baked items | Toaster for muffins; reduced Benedict |
| BURNER_1-6 | Poaching, sautéing | Limited poached items |

**Recording**: All equipment failures logged with time, duration, and impact.

---

**PROTOCOL AP_003: Staff Shortage Response**

| Field | Value |
|-------|-------|
| Protocol ID | AP_003 |
| Name | Staff Shortage Response |
| Type | Conditional |
| Version | 1 |

**Trigger Condition**:
```
staff_count < 3
```

**Threshold**: Fewer than 3 staff present  
**Check Time**: 6:30 AM (final staff confirmation)

**Response Actions**:

| Action Type | Description |
|-------------|-------------|
| reduce | Reduce service scope |
| backup | Activate backup staff |
| merge | Merge stations |

**Reduced Service Protocol**:
1. Assess available staff count
2. If 2 staff: Service reduction mode (limited menu)
3. If 1 staff: Emergency closure consideration
4. Maria makes final determination

**Recording**: All shortages logged with cause, duration, and service impact.

---

**PROTOCOL AP_004: Large Party Response**

| Field | Value |
|-------|-------|
| Protocol ID | AP_004 |
| Name | Large Party Response |
| Type | Conditional |
| Version | 1 |

**Trigger Condition**:
```
party_size > 8
```

**Threshold**: Party of more than 8 guests  
**Detection**: Reservation notes or advance notification

**Response Actions**:

| Action Type | Description |
|-------------|-------------|
| prep | Notify prep for increased volume |
| stagger | Coordinate ticket timing with front of house |
| dedicate | Dedicate support to party if needed |
| communicate | Maria communicates timeline to party |

**Recording**: All large parties logged with size and coordination notes.

---

**PROTOCOL AP_005: Allergen Alert Response**

| Field | Value |
|-------|-------|
| Protocol ID | AP_005 |
| Name | Allergen Alert Response |
| Type | Standing |
| Version | 1 |

**Trigger Condition**:
```
allergen_order_received == true
```

**Standing Protocol**: Activates for any order containing allergen information

**Response Actions**:

| Action Type | Description |
|-------------|-------------|
| isolate | Dedicated utensils and plating area |
| communicate | Order fired last |
| verify | Maria personal quality check |
| document | Allergen order documented |

**Allergen Information Protocol**:
1. POS system flags allergen order
2. Maria immediately notified
3. Allergen isolation station prepared
4. Dedicated utensils retrieved (colored handles)
5. Separate prep area sanitized
6. Order fired after all other orders
7. Maria inspects before plating
8. Server notified of allergen