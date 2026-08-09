# L1P3W[1](5): The Copper Beech Daily Workflow Constructor — Engineered System Specification

---

## I. Introduction: Making THIS Concrete

This artifact is the definitive engineered specification for **The Copper Beech Daily Workflow Constructor**—the specific instance of a system builder constructed at L0P2 for The Copper Beech restaurant. Where L1P1 established what system building *is* in general, and L1P2 explored how to build generators that produce system builders, this artifact makes that understanding concrete for *this specific system*.

The Copper Beech Daily Workflow Constructor is a living architecture that:
- Generates complete daily workflows from configuration alone (achieving generative closure)
- Persists as a living pattern through continuous feedback participation
- Maintains identity through invariance in purpose, architecture, constraints, and human authority
- Evolves through validated learning from execution feedback

This document provides the complete engineered specification necessary to understand, operate, and maintain this specific system. It translates the abstract principles of system building into concrete components, data structures, and processes appropriate for The Copper Beech restaurant's operational context.

---

## II. System Identity

### A. What This System IS

```yaml
System_Identity:
  name: "The Copper Beech Daily Workflow Constructor"
  alternative_names:
    - "Copper Beech Constructor"
    - "Daily Workflow Generator"
    - "The Constructor"
  version: "1.0.0"
  built_at: "L0P2"
  generator: "Generator Builder (L1P3)"
  domain: "The Copper Beech Restaurant"

Purpose:
  statement: |
    Transform accumulated operational knowledge for The Copper Beech restaurant
    into daily execution plans that satisfy all hard constraints, improve 
    through continuous feedback, and remain aligned with Maria's validation 
    authority.
  
  scope:
    - Consumes daily configuration (covers, staff, inventory, events)
    - Produces daily workflows (prep schedules, station assignments, service timing)
    - Maintains knowledge of restaurant-specific patterns
    - Participates in feedback loop for continuous improvement
  
  boundaries:
    - Operates within The Copper Beech restaurant only
    - Does not extend to other locations (single-unit operations)
    - Feedback loop aligned with Copper Beech context

Success_Definition: |
  The Copper Beech Daily Workflow Constructor succeeds when:
  - 95% of workflows generated without errors
  - 100% of workflows satisfy all hard constraints (HC_001-004)
  - 90% of workflows delivered by 9 PM SLA
  - 80% of identified patterns addressed within 30 days
```

### B. The Operational Context

```yaml
Operational_Context:
  restaurant_name: "The Copper Beech"
  business_type: "Full-service restaurant"
  cuisine_type: "American with seasonal specials"
  service_model: "Table service with full bar"
  operational_hours:
    lunch: "11:30 AM - 2:30 PM"
    dinner: "5:00 PM - 10:00 PM"
    bar: "11:30 AM - 11:00 PM"
  
  physical_layout:
    kitchen:
      stations: ["grill", "saute", "fry", "prep", "expo"]
      zones:
        - name: "Cold Prep"
          purpose: "Salads, cold appetizers"
          temperature: "Below 40°F"
        - name: "Hot Prep"
          purpose: "Sauces, side items"
          temperature: "Above 140°F"
        - name: "Line"
          purpose: "Final assembly"
          temperature: "Ambient"
        - name: "Raw Storage"
          purpose: "Meats and seafood"
          separated_from: "Ready-to-eat areas"
        - name: "Dry Storage"
          purpose: "Dry goods and supplies"
    dining:
      capacity: 65 seats
      private_room: 20 seats
      bar seating: 12 seats
  
  typical_volumes:
    lunch: 25-35 covers
    dinner: 40-55 covers
    weekend_brunch: 45-65 covers
    special_events: up to 30 additional covers

Staffing:
  management:
    - Maria (Head Chef / General Manager)
  
  kitchen:
    - Senior Line Cooks: 2
    - Line Cooks: 3
    - Prep Cooks: 2
  
  service:
    - Servers: 5
    - Hosts: 2
    - Bartenders: 2
    - Busser: 1
  
  total_typical: 14-16 staff

Equipment:
  cooking:
    - 6-burner ranges: 2
    - Char broiler: 1
    - Fryer (double): 1
    - Convection oven: 1
    - Combi oven: 1
    - Salamander: 1
  refrigeration:
    - Walk-in cooler: 1
    - Reach-in coolers: 3
    - Freezer: 1
  prep:
    - Prep tables: 4
    - Stand mixers: 2
    - Food processors: 2
```

---

## III. Hard Constraints (The Invariants)

### A. The Four Hard Constraints

These constraints are non-negotiable invariants. Violation produces INVALID_OUTPUT, not an error.

```yaml
Hard_Constraints:
  HC_001:
    code: "HC_001"
    name: "Food Safety Temperature Control"
    type: "temperature_boundary"
    
    definition: |
      Food items must be maintained outside the danger zone 
      (40°F-140°F) with cumulative time in danger zone not 
      exceeding 2 hours total.
    
    specifics_for_copper_beech:
      cold_hold_line: 40°F or below
      hot_hold_line: 140°F or above
      danger_zone: "40°F to 140°F"
      cumulative_maximum: "2 hours"
      check_frequency: "Every 30 minutes during service"
      critical_points:
        - "During prep (items out of refrigeration)"
        - "During plating (items waiting for pickup)"
        - "During transport (expo to table)"
      
    verification_method: |
      1. Temperature logs maintained continuously
      2. Spot checks at critical points
      3. Any item exceeding limits triggers immediate action
      4. Cumulative time tracked per item
    
    violation_result: "INVALID_OUTPUT"
    applies_to: "ALL food items"
    
    copper_beech_specifics:
      high_risk_items:
        - "Grilled chicken (held for more than 10 minutes)"
        - "Beef medallions (held for more than 15 minutes)"
        - "Seafood (any holding time)"
      protocol: "If temp approaches danger zone, immediate service or discard"

  HC_002:
    code: "HC_002"
    name: "Cross-Contamination Prevention"
    type: "spatial_separation"
    
    definition: |
      Raw foods (meats, seafood) and ready-to-eat foods (salads, 
      desserts, cooked items) must maintain complete spatial 
      separation in all prep and storage areas.
    
    specifics_for_copper_beech:
      raw_zones:
        - "Walk-in cooler: designated raw section"
        - "Walk-in freezer: designated raw section"
        - "Prep table: raw proteins only section"
      ready_to_eat_zones:
        - "Walk-in cooler: designated RTE section"
        - "Cold prep table: RTE only"
        - "Dessert station: RTE only"
      equipment_separation:
        - "Cutting boards: color-coded (red=raw, green=RTE)"
        - "Knives: designated for raw or RTE only"
        - "Storage containers: labeled raw or RTE"
      
    verification_method: |
      1. Visual inspection of zone separation
      2. Equipment color-coding verified
      3. Staff handling procedures observed
      4. Storage audits at shift start and end
    
    violation_result: "INVALID_OUTPUT"
    applies_to: "ALL prep areas and storage"
    
    copper_beech_specifics:
      check_points:
        - "Morning walk-in audit"
        - "Pre-service prep area check"
        - "Mid-service spot checks"
        - "Closing storage verification"

  HC_003:
    code: "HC_003"
    name: "Minimum Staffing Levels"
    type: "resource_minimum"
    
    definition: |
      Service periods must maintain minimum staffing of 3 staff 
      members who can handle food preparation and service tasks.
    
    specifics_for_copper_beech:
      minimums:
        lunch_service: 3
        dinner_service: 3
        bar_service: 1
        host_service: 1
      
      qualified_staff_definitions:
        kitchen: "Maria, Senior Line Cook, Line Cook (any)"
        service: "Server, Host, Bartender"
        busser: "Can assist but not primary kitchen"
      
      coverage_requirements:
        - "Grill station requires Senior Line Cook or Line Cook"
        - "Sauté station requires Senior Line Cook or Line Cook"
        - "Expo requires Maria or Senior Line Cook"
        - "At least one server on floor at all times"
      
    verification_method: |
      1. Staff availability confirmed in daily configuration
      2. Minimums verified before workflow generation
      3. If minimums cannot be met, workflow rejected
      4. Alternative coverage plans documented if available
    
    violation_result: "INVALID_OUTPUT"
    applies_to: "ALL service periods"
    
    copper_beech_specifics:
      service_periods:
        lunch: "11:30 AM - 2:30 PM"
        dinner: "5:00 PM - 10:00 PM"
      check_timing: "Before generation, at workflow delivery"

  HC_004:
    code: "HC_004"
    name: "Time-Temperature Combinations"
    type: "time_accumulation"
    
    definition: |
      Prep items must not exceed 4 hours from prep start to plate 
      service. Items approaching 3 hours should be monitored closely.
    
    specifics_for_copper_beech:
      prep_stages:
        - "Initial prep (cutting, seasoning): not time-limited"
        - "Cooking (grilling, sautéing): immediate service preferred"
        - "Holding (finished items waiting): max 30 minutes"
        - "Plated (sitting on plate): max 10 minutes before delivery"
      
      cumulative_tracking:
        - "From cook completion to plate delivery"
        - "From plate completion to table delivery"
        - "Total from cook completion to customer receipt"
      
      items_with_shorter_windows:
        - "Fish (max 20 minutes from cook to table)"
        - "Steak medium-rare (max 15 minutes from cook to table)"
        - "Grilled chicken (max 25 minutes from cook to table)"
      
    verification_method: |
      1. Time stamps on all cooked items
      2. Expo logs entry and exit times
      3. Server logs delivery times
      4. Any item exceeding 4 hours triggers immediate discard
    
    violation_result: "INVALID_OUTPUT"
    applies_to: "ALL prep items"
    
    copper_beech_specifics:
      special_events:
        - "Multi-course meals require coordination of timing"
        - "Private events may need extended prep holding"
        - "When extended holding needed, verify temp compliance"
```

### B. Constraint Properties

| Property | HC_001 | HC_002 | HC_003 | HC_004 |
|----------|--------|--------|--------|--------|
| **Type** | Temperature boundary | Spatial separation | Resource minimum | Time accumulation |
| **Violation Result** | INVALID_OUTPUT | INVALID_OUTPUT | INVALID_OUTPUT | INVALID_OUTPUT |
| **Applies To** | All food items | All prep areas | All service periods | All prep items |
| **Check Frequency** | Continuous/30 min | Shift start/end | Pre-generation | Per item |
| **Can Be Overridden** | Never | Never | Never | Never |
| **Can Be Relaxed** | Never | Never | Never | Never |

---

## IV. Three-Layer Architecture

### A. The Complete Architecture for The Copper Beech

```yaml
Three_Layer_Architecture:
  knowledge_layer:
    description: |
      Persistent structures providing patterns, constraints, and protocols
      specific to The Copper Beech restaurant. This layer provides resources
      to the processing layer without initiating transformations itself.
    
    components:
      pattern_library:
        description: "Accumulated solution templates from 1,247 days of operation"
        
        service_patterns:
          - name: "Standard Lunch Service"
            applicability: ["lunch_hours", "casual_volume", "25-35_covers"]
            structure:
              - prep_sequence: "Light morning prep, 30-min lead"
              - station_assignment: "Grill + sauté, 2 stations"
              - service_timing: "Continuous flow"
            constraints_satisfied: ["HC_001", "HC_002", "HC_003", "HC_004"]
            typical_duration: "11:30 AM - 2:30 PM"
            
          - name: "Standard Dinner Service"
            applicability: ["dinner_hours", "moderate_volume", "40-50_covers"]
            structure:
              - prep_sequence: "Full afternoon prep, 90-min lead"
              - station_assignment: "Grill + sauté + fry, 3 stations"
              - service_timing: "Staggered waves"
            constraints_satisfied: ["HC_001", "HC_002", "HC_003", "HC_004"]
            typical_duration: "5:00 PM - 10:00 PM"
            
          - name: "High-Volume Dinner Service"
            applicability: ["dinner_hours", "high_volume", "50+_covers"]
            structure:
              - prep_sequence: "Extended afternoon prep, 2-hour lead"
              - station_assignment: "All 5 stations staffed"
              - service_timing: "Coordinated waves with backup"
            constraints_satisfied: ["HC_001", "HC_002", "HC_003", "HC_004"]
            typical_duration: "5:00 PM - 10:00 PM"
            
          - name: "Weekend Brunch Service"
            applicability: ["brunch_hours", "mixed_demand", "45-65_covers"]
            structure:
              - prep_sequence: "Combined prep for lunch + dinner items"
              - station_assignment: "Combined grill/sauté, 2-3 stations"
              - service_timing: "Extended continuous"
            constraints_satisfied: ["HC_001", "HC_002", "HC_003", "HC_004"]
            typical_duration: "11:00 AM - 3:00 PM"
            
          - name: "Special Event Service"
            applicability: ["private_event", "reservation_heavy", "varies"]
            structure:
              - prep_sequence: "Custom based on event type"
              - station_assignment: "Dedicated private room service"
              - service_timing: "Synchronized for event"
            constraints_satisfied: ["HC_001", "HC_002", "HC_003", "HC_004"]
            variations:
              - birthday: "Cake timing, gift coordination"
              - anniversary: "Special dessert timing"
              - corporate: "Set menu, efficient service"
              - rehearsal_dinner: "Multi-course, relaxed timing"
        
        prep_patterns:
          - name: "Morning Prep (Standard)"
            lead_time: "90 minutes"
            tasks: ["Ingredient prep", "Sauce bases", "Proteins portioning"]
            
          - name: "Afternoon Prep (Dinner)"
            lead_time: "120 minutes"
            tasks: ["Full protein prep", "Special prep", "Dessert components"]
            
          - name: "Refresh Prep (Service)"
            frequency: "Every 2 hours during service"
            tasks: ["Garnish refresh", "Sauce refresh", "Protein restocking"]
        
        failure_patterns:
          - name: "Grill Bottleneck Pattern"
            frequency: "4 times per month average"
            symptoms: ["Plate wait times exceed 8 minutes", "Expo queue builds"]
            mitigation: "Pre-heat extra proteins, backup timing"
            
          - name: "Dessert Station Delay Pattern"
            frequency: "3 times per month average"
            symptoms: ["Desserts 10+ minutes behind main course"]
            mitigation: "Earlier dessert start, dedicated server"
        
      constraint_definitions:
        description: "Complete constraint definitions with Copper Beech specifics"
        constraints: "{{HARD_CONSTRAINTS}}"  # From Section III
        
      protocol_library:
        description: "Standard procedures for Copper Beech operations"
        
        opening_protocol:
          name: "Opening Protocol"
          description: "Standard opening procedures"
          steps:
            - step: "Maria arrives (10:00 AM)"
              tasks: ["Walk-in audit", "Equipment check", "Staff briefing prep"]
              duration: "30 minutes"
            - step: "Kitchen team arrives (10:30 AM)"
              tasks: ["Station setup", "Prep begins", "Walk-in organization"]
              duration: "60 minutes"
            - step: "Service prep complete (11:00 AM)"
              tasks: ["Line check", "Temp verification", "Maria sign-off"]
              duration: "30 minutes"
            - step: "Service ready (11:30 AM)"
              tasks: ["Doors open", "First covers seated"]
          constraint_checks:
            - HC_002: "Walk-in separation verified"
            - HC_001: "All cold storage at or below 40°F"
            
        lunch_service_protocol:
          name: "Lunch Service Protocol"
          description: "Standard lunch service procedures"
          steps:
            - step: "First covers (11:30 AM)"
              tasks: ["Welcome", "Orders in", "Kitchen called"]
            - step: "Continuous service (until 2:00 PM)"
              tasks: ["Steady flow", "Temp checks every 30 min", "Expo coordination"]
            - step: "Winding down (2:00 PM)"
              tasks: ["Last orders", "Kitchen fire-down"]
            - step: "Service end (2:30 PM)"
              tasks: ["All plates delivered", "Kitchen break begins"]
          constraint_checks:
            - HC_001: "Temp logs maintained"
            - HC_004: "Timing tracked per item"
            
        dinner_service_protocol:
          name: "Dinner Service Protocol"
          description: "Standard dinner service procedures"
          steps:
            - step: "Pre-service prep (3:30 PM)"
              tasks: ["Station setup", "Full prep", "Line check"]
              duration: "90 minutes"
            - step: "First covers (5:00 PM)"
              tasks: ["Welcome", "Orders in", "Kitchen called"]
            - step: "Peak service (6:00-8:00 PM)"
              tasks: ["Coordinated waves", "Active monitoring", "Backup ready"]
            - step: "Winding down (9:00 PM)"
              tasks: ["Last orders", "Kitchen fire-down begins"]
            - step: "Service end (10:00 PM)"
              tasks: ["All plates delivered", "Closing begins"]
          constraint_checks:
            - HC_001: "Temp checks increased during peak"
            - HC_003: "Minimum staffing verified"
            
        closing_protocol:
          name: "Closing Protocol"
          description: "Standard closing procedures"
          steps:
            - step: "Service complete"
              tasks: ["All checks delivered", "Guests departed"]
              time: "10:00 PM"
            - step: "Initial breakdown"
              tasks: ["Hot line cleanup", "Equipment shutdown"]
              time: "10:00-10:30 PM"
            - step: "Storage procedures"
              tasks: ["Date labeling", "Proper storage", "Cross-contamination prevention"]
              time: "10:30-11:00 PM"
            - step: "Final walk-through"
              tasks: ["Maria inspection", "Next-day prep noted"]
              time: "11:00 PM"
          constraint_checks:
            - HC_002: "Raw/RTE separation verified for next day"
            
        special_event_protocol:
          name: "Special Event Protocol"
          description: "Procedures for private events"
          steps:
            - step: "Event confirmation (day before)"
              tasks: ["Menu confirmed", "Staffing verified", "HC_003 confirmed"]
            - step: "Event prep (event day)"
              tasks: ["Private room setup", "Special prep", "Coordination meeting"]
            - step: "Event service"
              tasks: ["Synchronized timing", "Dedicated attention", "Quality monitoring"]
            - step: "Event closeout"
              tasks: ["Guest departure", "Room reset", "Feedback noted"]
          variations:
            birthday:
              additional_steps:
                - "Cake timing coordinated with kitchen"
                - "Gift presentation timing"
                - "Photo opportunity coordination"
            corporate:
              additional_steps:
                - "Set menu items prepared"
                - "Efficient course timing"
                - "Billing coordination"
      
      staff_profiles:
        description: "Capabilities and limitations of Copper Beech staff"
        
        profiles:
          - name: "Maria"
            role: "Head Chef / General Manager"
            capabilities:
              - "Full kitchen operations"
              - "Menu execution"
              - "Quality control"
              - "Staff management"
              - "Customer relations"
              - "Final plate inspection"
            limitations: []
            schedule: "Full-time, opens and closes"
            
          - name: "Senior Line Cook 1"
            role: "Lead Line Cook"
            capabilities:
              - "Grill station lead"
              - "Sauté station"
              - "Quality checks"
              - "Backup expo"
            limitations:
              - "Cannot manage alone"
              - "Requires senior oversight for new items"
            schedule: "Full-time, dinner service"
            
          - name: "Senior Line Cook 2"
            role: "Lead Line Cook"
            capabilities:
              - "Sauté station lead"
              - "Grill station"
              - "Prep supervision"
            limitations:
              - "Limited management responsibility"
            schedule: "Full-time, lunch/dinner rotation"
            
          - name: "Line Cook 1"
            role: "Line Cook"
            capabilities:
              - "Fry station"
              - "Backup grill"
              - "Basic prep"
            limitations:
              - "Cannot lead station"
            schedule: "Part-time, dinner service"
            
          - name: "Line Cook 2"
            role: "Line Cook"
            capabilities:
              - "Prep station"
              - "Fry station"
              - "Basic sauté"
            limitations:
              - "Cannot lead grill"
            schedule: "Full-time, dinner service"
            
          - name: "Line Cook 3"
            role: "Line Cook"
            capabilities:
              - "Prep station"
              - "Line support"
            limitations:
              - "Limited fry/grill capability"
            schedule: "Part-time, weekends"
            
          - name: "Server 1"
            role: "Server"
            capabilities:
              - "Full table service"
              - "Private room service"
              - "Wine service"
            limitations: []
            schedule: "Full-time"
            
          - name: "Server 2"
            role: "Server"
            capabilities:
              - "Full table service"
              - "Bar backup"
            limitations:
              - "Limited private room"
            schedule: "Full-time"
            
          - name: "Server 3"
            role: "Server"
            capabilities:
              - "Full table service"
              - "Special events"
            limitations: []
            schedule: "Full-time"
            
          - name: "Server 4"
            role: "Server"
            capabilities:
              - "Table service"
            limitations:
              - "Newer, less experience"
            schedule: "Part-time"
            
          - name: "Server 5"
            role: "Server"
            capabilities:
              - "Table service"
            limitations:
              - "Newer, less experience"
            schedule: "Part-time"
            
          - name: "Host 1"
            role: "Host"
            capabilities:
              - "Seating management"
              - "Reservation coordination"
            limitations: []
            schedule: "Full-time"
            
          - name: "Host 2"
            role: "Host"
            capabilities:
              - "Seating management"
              - "Takeout coordination"
            limitations: []
            schedule: "Part-time"
            
          - name: "Bartender 1"
            role: "Bartender"
            capabilities:
              - "Full bar service"
              - "Bar food coordination"
            limitations: []
            schedule: "Full-time"
            
          - name: "Bartender 2"
            role: "Bartender"
            capabilities:
              - "Full bar service"
              - "Server backup"
            limitations: []
            schedule: "Part-time"
            
          - name: "Busser"
            role: "Busser"
            capabilities:
              - "Table reset"
              - "Water service"
              - "Support runner"
            limitations:
              - "Cannot serve"
            schedule: "Part-time, dinner"

  processing_layer:
    description: |
      Transformation modules that convert daily configuration
      into daily workflow for The Copper Beech. This layer performs
      the generative work of the constructor.
    
    modules:
      config_parser:
        description: "Validates and normalizes daily configuration"
        
        inputs:
          - date
          - expected_covers
          - staff_availability
          - inventory_status
          - special_events
          - equipment_status
        
        validation_rules:
          covers:
            type: "integer"
            min: 0
            max: 100
            required: true
            
          staff:
            type: "list of staff names"
            required: true
            min_count: 3
            must_include_roles:
              - "kitchen_coverage: [Maria OR Senior Line Cook, Line Cook]"
              - "floor_coverage: [At least 1 server]"
            
          inventory:
            type: "percentage or item list"
            required: true
            format: "Either 'freshness_percentage' or 'item_availability_list'"
            
          events:
            type: "list of event objects"
            required: false
            each_requires:
              - event_type
              - cover_count
              - timing
              - special_requirements
        
        outputs:
          - validated_configuration
          - configuration_summary
          - missing_fields (if any)
        
        error_handling:
          - MissingRequiredField: "Request from shift supervisor"
          - InvalidStaffing: "Reject if HC_003 cannot be met"
          - LowInventory: "Flag for Maria review"
          - FormatError: "Request corrected input"
        
        copper_beech_defaults:
          default_covers: 35
          default_staffing: "Full available staff"
          default_inventory: "Assumed adequate unless noted"
          sla_deadline: "9:00 PM previous evening"

      pattern_selector:
        description: "Selects appropriate service patterns based on configuration"
        
        inputs:
          - validated_configuration
          - pattern_library
        
        selection_criteria:
          primary_match:
            - service_period: "lunch or dinner"
            - volume_category: "based on expected covers"
            - special_events: "any event types present"
          
          secondary_factors:
            - day_of_week: "Weekends may trigger brunch"
            - seasonality: "Summer may affect menu mix"
            - historical_patterns: "Maria's notes from similar days"
        
        matching_rules:
          lunch_low_volume:
            condition: "covers < 30 AND lunch_hours"
            patterns: ["Standard Lunch Service"]
            
          lunch_standard:
            condition: "covers 30-45 AND lunch_hours"
            patterns: ["Standard Lunch Service"]
            
          dinner_standard:
            condition: "covers 40-50 AND dinner_hours"
            patterns: ["Standard Dinner Service"]
            
          dinner_high_volume:
            condition: "covers > 50 AND dinner_hours"
            patterns: ["High-Volume Dinner Service"]
            
          weekend_brunch:
            condition: "day IN [Saturday, Sunday] AND time IN [11-15]"
            patterns: ["Weekend Brunch Service"]
            
          special_event:
            condition: "events NOT empty"
            patterns: ["Special Event Service"] + [appropriate base pattern]
        
        outputs:
          - selected_primary_pattern
          - selected_supporting_patterns
          - pattern_configuration_overrides
        
        conflict_resolution:
          - "High volume + special event: Prioritize high volume pattern, add event components"
          - "Ambiguous volume: Default to higher service level"
          - "No matching pattern: Default to standard dinner, flag for Maria review"

      workflow_assembler:
        description: "Assembles complete daily workflow from selected patterns"
        
        inputs:
          - validated_configuration
          - selected_patterns
          - staff_profiles
          - protocol_library
        
        assembly_process:
          step_1_prep_schedule:
            description: "Build prep timeline"
            inputs:
              - selected_patterns.prep_sequence
              - inventory_status
              - special_menu_items
            outputs:
              - prep_tasks: list of task objects
              - prep_start_time: timestamp
              - prep_completion_target: timestamp
            task_structure:
              - task_name: string
              - assigned_staff: list of staff names
              - start_time: timestamp
              - duration_minutes: integer
              - dependencies: list of task names
              - constraint_notes: string
            
          step_2_station_assignments:
            description: "Assign staff to stations"
            inputs:
              - available_staff
              - cover_count
              - special_events
              - staff_profiles
            outputs:
              - station_assignments: map of station to staff
              - coverage_verification: boolean
            assignment_rules:
              grill:
                required_capability: "grill OR senior_line_cook"
                preferred_staff: ["Senior Line Cook 1", "Senior Line Cook 2"]
              saute:
                required_capability: "saute OR senior_line_cook"
                preferred_staff: ["Senior Line Cook 2", "Senior Line Cook 1"]
              fry:
                required_capability: "fry"
                preferred_staff: ["Line Cook 1", "Line Cook 2"]
              prep:
                required_capability: "prep"
                preferred_staff: ["Line Cook 2", "Line Cook 3"]
              expo:
                required_capability: "expo"
                preferred_staff: ["Maria"]
            
          step_3_service_timing:
            description: "Build service timing sequence"
            inputs:
              - cover_count
              - expected_arrival_distribution
              - course_structure
              - special_events
            outputs:
              - wave_schedule: list of waves
              - expected_first_course_time: timestamp
              - expected_last_seating: timestamp
            timing_rules:
              - "First seating: 15-30 min after doors"
              - "Wave spacing: 10-15 min for standard, 5-10 min for high volume"
              - "Course timing: Appetizer 20 min, Entree 25 min, Dessert 15 min"
              - "Special events: Synchronized timing per event requirements"
            
          step_4_resource_allocation:
            description: "Allocate equipment and resources"
            inputs:
              - menu_items_for_day
              - equipment_status
              - station_assignments
            outputs:
              - equipment_schedule
              - backup_plan
            allocation_rules:
              - "Primary equipment assigned by station"
              - "Backup equipment identified for critical items"
              - "Equipment stagger to prevent overload"
            
          step_5_break_schedule:
            description: "Plan staff breaks"
            inputs:
              - staff_availability_hours
              - service_duration
              - minimum_coverage
            outputs:
              - break_assignments
              - coverage_during_breaks
            break_rules:
              - "No breaks during first 90 min of service"
              - "Maximum 15 min per break"
              - "Coverage maintained at HC_003 minimum"
              - "Maria and at least one senior cook always present"
        
        outputs:
          - complete_daily_workflow
          - workflow_components:
              - prep_schedule
              - station_assignments
              - service_timing
              - resource_allocation
              - break_schedule
              - special_instructions
              - constraint_highlights

      constraint_verifier:
        description: "Verifies assembled workflow satisfies all hard constraints"
        
        inputs:
          - assembled_workflow
          - hard_constraints
        
        verification_sequence:
          step_1_hc_001_temperature_control:
            check: "Temperature control provisions in workflow"
            verification_points:
              - "Temp check schedule included?"
              - "Critical checkpoints identified?"
              - "Cumulative tracking method specified?"
              - "Danger zone response protocol included?"
            failure_action: "Reject workflow, regenerate with temp controls"
            
          step_2_hc_002_cross_contamination:
            check: "Cross-contamination prevention in workflow"
            verification_points:
              - "Zone separation specified in prep schedule?"
              - "Equipment assignment respects separation?"
              - "Storage procedures include separation checks?"
              - "Opening audit includes separation verification?"
            failure_action: "Reject workflow, regenerate with separation controls"
            
          step_3_hc_003_staffing:
            check: "Minimum staffing maintained throughout"
            verification_points:
              - "All service periods have minimum coverage?"
              - "Break schedule maintains minimums?"
              - "Special events have adequate staffing?"
              - "Backup coverage identified for absences?"
            failure_action: "Reject workflow, request additional staffing or reduce scope"
            
          step_4_hc_004_time_temperature:
            check: "Time-temperature combinations within limits"
            verification_points:
              - "Prep timing allows service within 4 hours?"
              - "Holding protocols specified?"
              - "Item timing tracked in workflow?"
              - "Expediting procedures included?"
            failure_action: "Reject workflow, regenerate with adjusted timing"
        
        outputs:
          - verification_result: "PASS" or "FAIL"
          - violations: list of violated constraints (if any)
          - modified_workflow: workflow with constraint highlights (if passed)
        
        failure_handling:
          - "If any check fails: Workflow is INVALID_OUTPUT"
          - "Violations returned to assembler with specifics"
          - "Assembler attempts regeneration with fixes"
          - "After 3 failures: Flag for Maria review"

  integration_layer:
    description: |
      Interfaces connecting The Copper Beech Constructor to
      external systems and stakeholders.
    
    interfaces:
      configuration_input:
        description: "Receives daily configuration from shift supervisor"
        method: "Web form submission"
        timing: "By 9:00 PM previous evening"
        fields:
          - field: "date"
            type: "date"
            required: true
            example: "2024-01-15"
          - field: "expected_covers"
            type: "integer"
            required: true
            example: 45
          - field: "staff_available"
            type: "multi-select"
            required: true
            options: "List of all staff names"
            example: ["Maria", "Senior Line Cook 1", "Line Cook 1", "Server 1", "Server 2", "Host 1", "Bartender 1"]
          - field: "inventory_status"
            type: "text or percentage"
            required: true
            example: "75% fresh, missing salmon"
          - field: "special_events"
            type: "structured list"
            required: false
            structure:
              - event_type: string
              - cover_count: integer
              - timing: time
              - notes: text
            example: "Birthday party, 