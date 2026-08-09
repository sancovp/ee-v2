# The Copper Beech Daily Workflow Constructor

## Engineered System: Complete Instance Specification

### Position: L0P1W[0](5) — Conceptualize · Conceptualize (What IS) · EngineeredSystem

---

## 1. Purpose of This Artifact

While the Conceptual Ontology (L0P1W[0](0)) established *what the Constructor IS in its essential nature*, the Systems Design (L0P1W[0](1)) established *what universal characteristics define the domain*, the Systems Architecture (L0P1W[0](2)) established *what essential functions and structures constitute the Constructor*, and the Domain-Specific Language (L0P1W[0](3)) established *the vocabulary and grammar through which the domain speaks*, this artifact examines *what a fully realized instance of the Constructor looks like when concretely instantiated*.

The question here is: "If we were to run the Copper Beech Daily Workflow Constructor for an actual day at Copper Beech Cafe, what would appear on Maria's workstation? What documents would be generated? What would the complete system look like when operating?"

This artifact provides the concrete answer—a fully realized example that transforms all abstract specifications into tangible operational artifacts.

---

## 2. The Instance Context: Tuesday, March 18th, 2025

To demonstrate a complete instance, we select a specific day with specific circumstances. The instance context establishes the configuration inputs that drive the entire generation process.

### 2.1 Configuration Input Document

```yaml
# ============================================================
# COPPER BEECH CAFE - DAILY CONFIGURATION
# Instance ID: copper_beech_2025-03-18_config
# Generated: 2025-03-17T21:00:00Z
# ============================================================

daily_context:
  date: "2025-03-18"
  day_of_week: "Tuesday"
  expected_volume:
    breakfast_tickets: "25-35"
    lunch_tickets: "10-15"
    volume_tier: "medium-high"
    notes: "Post-St. Patrick's Day; expect residual interest in eggs and griddle items"
  
  weather_indicator: "rainy"
  weather_impact: "moderate"
  expected_effects:
    - "Reduced walk-in traffic expected"
    - "Increased breakfast/brunch crowd (indoor dining preference)"
    - "Slower pace in early service, then normal"
  
  special_events: []
  reservation_notes: "None scheduled"
  operational_notes: "Standard Tuesday operations"

staff_configuration:
  scheduled:
    - name: "Maria"
      role: "chef"
      start_time: "05:30"
      certifications: ["food_safety_manager", "allergen_aware"]
      strengths: ["all_stations", "quality_control", "problem_resolution"]
      availability: "full_shift"
      
    - name: "James"
      role: "line_cook"
      start_time: "06:00"
      certifications: ["food_handler"]
      strengths: ["grill", "eggs_backup"]
      availability: "full_shift"
      
    - name: "Elena"
      role: "prep_cook"
      start_time: "05:45"
      certifications: ["food_handler"]
      strengths: ["mise_en_place", "produce_prep"]
      availability: "full_shift"
      
    - name: "Marcus"
      role: "support"
      start_time: "07:00"
      certifications: ["food_handler"]
      strengths: ["coverage", "cleaning", "supply_retrieval"]
      availability: "full_shift"
  
  expected_changes: []
  coverage_status: "full_team"

inventory_configuration:
  previous_night_delivery: false
  delivery_note: "Regular Tuesday delivery; arrived Monday evening"
  
  notable_items:
    - item: "eggs"
      status: "fully_stocked"
      note: "3 full flats available"
    - item: "canadian_bacon"
      status: "low"
      note: "Last case; prioritize Eggs Benedict orders"
    - item: "hollandaise_base"
      status: "fully_stocked"
      note: "Maria prepped extra on Monday"
    - item: "english_muffins"
      status: "adequate"
      note: "2 cases remaining"
      
  low_stock_alerts:
    - item: "canadian_bacon"
      severity: "low"
      action: "Monitor Benedict orders; may need substitution offer"
    - item: "mayonnaise"
      severity: "moderate"
      action: "Marcus to restock from storage at 10:00"
      
  substitutions_available:
    canadian_bacon: ["smoked_green_beacon_brand", "bacon_substitute"]
    note: "Maria approval required for substitutions"

equipment_configuration:
  available:
    - id: "OVEN_1"
      type: "convection_oven"
      location: "north_wall"
      status: "operational"
      notes: "Primary baking oven"
      
    - id: "GRIDDLE_1"
      type: "griddle"
      location: "center_station"
      status: "operational"
      notes: "Main cooking surface"
      
    - id: "FRYER_1"
      type: "fryer"
      location: "east_station"
      status: "operational"
      notes: "Hash browns and bacon"
      
    - id: "BURNER_1" through "BURNER_6"
      type: "6_burner"
      location: "south_wall"
      status: "operational"
      notes: "All burners operational"
      
  issues: []
  equipment_status: "full_capacity"

constraint_status:
  hard_constraints:
    HC_001: "assessable"
    HC_002: "assessable"
    HC_003: "assessable"
    HC_004: "assessable"
  staffing_minimum_met: true
  staffing_count: 4
  
trigger_context:
  anticipated_triggers:
    - trigger: "AP_001"
      probability: "medium"
      reason: "Volume tier medium-high; possible queue spikes"
    - trigger: "AP_005"
      probability: "low"
      reason: "Standard allergen probability"
  standing_protocols:
    - "AP_005 (Allergen Alert Response)"
    - "AP_002 (Equipment Failure Response)"
```

---

## 3. Generated Instance: The Daily Workflow Document

The following is the complete workflow instance generated from the configuration above. This is what appears on Maria's workstation the evening before the operational day, and what guides Tuesday's operations.

### 3.1 Workflow Instance Document

```yaml
# ============================================================
# COPPER BEECH CAFE - DAILY WORKFLOW INSTANCE
# Instance ID: copper_beech_2025-03-18_daily
# Date: 2025-03-18 (Tuesday)
# Generated: 2025-03-17T21:15:00Z
# Generated By: copper_beech_constructor_v1.0.0
# Status: PENDING_EXECUTION
# ============================================================

configuration_summary:
  expected_volume: "25-35 breakfast tickets, 10-15 lunch tickets (medium-high tier)"
  staff_count: 4
  weather: "rainy"
  special_events: []
  key_notes:
    - "Post-St. Patrick's Day; expect interest in traditional breakfast items"
    - "Canadian bacon LOW - monitor Benedict orders"
    - "Full team present - standard operations"
  configuration_id: "copper_beech_2025-03-18_config"

hard_constraint_verification:
  HC_001:
    status: "satisfied"
    assessment: "No time-temperature combinations exceed 4-hour prep maximum"
  HC_002:
    status: "satisfied"
    assessment: "Color-coded board assignments verified; allergen isolation available"
  HC_003:
    status: "satisfied"
    assessment: "4 staff present (minimum 3 required)"
  HC_004:
    status: "satisfied"
    assessment: "All prep cycles within 4-hour maximum"

# ============================================================
# OPENING SECTION
# Target Completion: 06:45
# Duration: 75 minutes
# ============================================================

opening_section:
  section_id: "opening_2025-03-18"
  target_completion: "06:45"
  target_service_ready: "06:55"
  buffer: "5 minutes"
  
  tasks:
    # ---- 5:30 AM ----
    - task_id: "OT_001"
      time: "5:30"
      name: "Equipment Preheating"
      duration: 15
      assigned_to: "Maria"
      role_required: "chef"
      equipment_used: ["GRIDDLE_1", "FRYER_1", "BURNER_1", "BURNER_2"]
      
      inputs:
        - "Equipment powered on"
        - "Temperature settings applied"
      
      procedure:
        - "Power on griddle; set to 375°F"
        - "Power on fryer; heat to 350°F"
        - "Fill pots with water for poaching; set burners to simmer"
        - "Preheat convection oven to 350°F"
        
      outputs:
        - "GRIDDLE_1 at 375°F"
        - "FRYER_1 at 350°F"
        - "Poaching water at simmer"
        - "OVEN_1 at 350°F"
      
      success_criteria:
        - "All equipment at target temperature by 5:45"
        - "Water maintained at gentle simmer (not boiling)"
        
      notes: "Critical path item - all cooking depends on this completion"
    
    # ---- 5:35 AM ----
    - task_id: "OT_002"
      time: "5:35"
      name: "Egg Retrieval and Temperature Assessment"
      duration: 10
      assigned_to: "Elena"
      role_required: "prep_cook"
      equipment_used: []
      color_board: "green"
      
      inputs:
        - "Walk-in cooler access"
        - "Temperature probe"
      
      procedure:
        - "Retrieve 3 flats of eggs from cooler"
        - "Verify egg temperature (must be below 40°F)"
        - "Stage eggs at station for morning prep"
        - "Record temperature in prep log"
        
      outputs:
        - "Eggs staged at room temperature station"
        - "Temperature logged: [VALUE]°F"
        - "HC_001 compliance verified"
        
      success_criteria:
        - "Eggs at 39°F or below when retrieved"
        - "Temperature recorded in log"
        
      notes: "First point of HC_001 verification - eggs must enter prep cycle cold"
    
    # ---- 5:45 AM ----
    - task_id: "OT_003"
      time: "5:45"
      name: "Inventory Check"
      duration: 20
      assigned_to: ["Elena", "Maria"]
      role_required: "prep_cook, chef"
      equipment_used: []
      
      inputs:
        - "Previous night's inventory sheet"
        - "Storage access"
      
      procedure:
        - "Elena verifies backup stock levels (eggs, butter, cream, produce)"
        - "Maria verifies specialty items (hollandaise base, english muffins, canadian bacon)"
        - "Check for Monday delivery items"
        - "Flag any discrepancies"
        - "Confirm low-stock alert: canadian bacon"
        
      outputs:
        - "Inventory status verified"
        - "Low stock items confirmed and logged"
        - "Substitutions identified if needed"
        
      success_criteria:
        - "All key items accounted for"
        - "Low-stock alerts actionable"
        
      notes: "Maria to decide on canadian bacon allocation for Benedict orders"
      low_stock_protocol: "canadian_bacon_allocation"
    
    # ---- 5:50 AM ----
    - task_id: "OT_004"
      time: "5:50"
      name: "Standard Egg Prep"
      pattern_reference: "TP_001"
      duration: 15
      assigned_to: "Elena"
      role_required: "prep_cook"
      equipment_used: []
      color_board: "green"
      depends_on: ["OT_002"]
      
      inputs:
        - "45 eggs (for expected volume plus buffer)"
        - "Butter, seasoning"
        - "Prep containers"
      
      procedure:
        - "Crack eggs into sanitized bowls (6 per batch)"
        - "Season lightly with salt and white pepper"
        - "Store in covered containers at 39°F"
        - "Label with prep time and expiration (4 hours)"
        - "Stage for service use"
        
      outputs:
        - "8 containers of cracked eggs (6 each)"
        - "Prepped eggs at proper temperature"
        - "HC_004 compliance: prep time logged"
        
      success_criteria:
        - "45 eggs prepped in 15 minutes"
        - "All eggs at 40°F or below"
        - "Prep completed by 6:05"
        - "Prep time logged for HC_004 tracking"
        
      notes: "Elena's standard timing - 15 minutes established from learning record"
      learning_source: "Elena efficiency improvement 2024-10-20"
    
    # ---- 5:55 AM ----
    - task_id: "OT_005"
      time: "5:55"
      name: "Bacon Portioning"
      pattern_reference: "TP_002"
      duration: 20
      assigned_to: "Elena"
      role_required: "prep_cook"
      equipment_used: ["FRYER_1"]
      color_board: "red"
      depends_on: ["OT_001"]
      
      inputs:
        - "2 cases raw bacon"
        - "Fryer at 350°F"
        - "Portioning trays"
      
      procedure:
        - "Portion bacon strips for expected orders (allow 2 strips per egg dish)"
        - "Fry bacon in batches until crispy"
        - "Drain on paper towels"
        - "Store in heated holding area (above 140°F)"
        - "Track time in hot holding for HC_001"
        
      outputs:
        - "Pre-portioned bacon ready for service"
        - "Holding temperatures maintained"
        - "HC_001 tracking initiated"
        
      success_criteria:
        - "Bacon portioned and cooked by 6:15"
        - "Hot holding above 140°F"
        - "Bacon accessible for service start"
        
      allergen_flags: []
      cross_contamination_prevention: "Red board only; no contact with green board items"
      notes: "Canadian bacon note: portion separately; limited supply"
      low_stock_note: "Canadian bacon portions identified separately from regular bacon"
    
    # ---- 6:00 AM ----
    - task_id: "OT_006"
      time: "6:00"
      name: "Produce Prep"
      pattern_reference: "TP_003"
      duration: 30
      assigned_to: "Elena"
      role_required: "prep_cook"
      equipment_used: []
      color_board: "green"
      depends_on: ["OT_003"]
      
      inputs:
        - "Tomatoes (24)"
        - "Lettuce (2 heads)"
        - "Onions (6)"
        - "Fresh herbs as needed"
      
      procedure:
        - "Slice tomatoes for sandwiches and plating"
        - "Chop lettuce for salads and sandwiches"
        - "Dice onions for omelettes and hash browns"
        - "Prepare garnishes (herb bundles, lemon wedges)"
        - "Store in sanitized containers at 40°F"
        
      outputs:
        - "Prepped produce staged for service"
        - "Waste minimized (< 5%)"
        - "All items at or below 40°F"
        
      success_criteria:
        - "All produce prepped by 6:30"
        - "Station ready for service"
        - "Minimal waste"
        
      allergen_flags: []
      notes: "Elena's produce prep efficiency - typically completes in 25 minutes; allow 30 for this instance"
      learning_source: "Elena timing adjustment 2024-10-20"
    
    # ---- 6:00 AM ----
    - task_id: "OT_007"
      time: "6:00"
      name: "Hollandaise Preparation"
      pattern_reference: "TP_005"
      duration: 15
      assigned_to: "Maria"
      role_required: "chef"
      equipment_used: ["BURNER_3", "OVEN_1"]
      depends_on: ["OT_001", "OT_003"]
      
      inputs:
        - "12 egg yolks"
        - "1.5 lbs butter"
        - "Lemon juice"
        - "Cayenne pepper"
      
      procedure:
        - "Clarify butter in small batches"
        - "Whisk egg yolks over gentle heat (bain-marie)"
        - "Slowly incorporate clarified butter"
        - "Season with lemon juice and cayenne"
        - "Hold in thermos at 150°F for service"
        
      outputs:
        - "1 quart hollandaise sauce"
        - "Sauce at proper holding temperature"
        - "Ready for Eggs Benedict production"
        
      success_criteria:
        - "Sauce emulsified properly"
        - "No break in sauce"
        - "Holding temperature 140-150°F"
        
      allergen_flags: ["dairy", "eggs"]
      notes: "Maria's signature hollandaise - quality control critical"
      quality_check: "Maria taste test before service"
    
    # ---- 6:15 AM ----
    - task_id: "OT_008"
      time: "6:15"
      name: "Hash Brown Preparation"
      pattern_reference: "TP_004"
      duration: 25
      assigned_to: "Elena"
      role_required: "prep_cook"
      equipment_used: ["FRYER_1"]
      color_board: "green"
      depends_on: ["OT_001"]
      
      inputs:
        - "20 lbs shredded potatoes"
        - "Fryer at 350°F"
        - "Seasonings"
        - "Pressing equipment"
      
      procedure:
        - "Season shredded potatoes"
        - "Press into hash brown patties"
        - "Fry in batches until golden brown"
        - "Drain and hold in warming area"
        - "Track time in hot holding for HC_001"
        
      outputs:
        - "Pre-portioned hash brown patties (50 count)"
        - "Held at 140°F or above"
        - "Ready for griddle finishing"
        
      success_criteria:
        - "Hash browns cooked through and crispy"
        - "Held at proper temperature"
        - "Completed by 6:40"
        
      allergen_flags: []
      cross_contamination_prevention: "Green board only; no contact with meat items"
      notes: "Elena's timing - historically 30 minutes, adjusted to 25 with improved process"
      learning_source: "Elena timing improvement 2024-11-15"
    
    # ---- 6:20 AM ----
    - task_id: "OT_009"
      time: "6:20"
      name: "English Muffin and Bread Prep"
      duration: 10
      assigned_to: "Maria"
      role_required: "chef"
      equipment_used: ["OVEN_1"]
      
      inputs:
        - "English muffins (2 cases)"
        - "Bread for toast (2 loaves)"
        - "Butter for toasting"
      
      procedure:
        - "Split and butter english muffins"
        - "Stage for toasting as needed"
        - "Slice bread for toast orders"
        - "Store in bread box at room temperature"
        
      outputs:
        - "English muffins portioned and ready"
        - "Toast bread sliced and accessible"
        
      success_criteria:
        - "All items ready for service"
        - "No waste from dried-out product"
        
      allergen_flags: ["gluten", "dairy"]
    
    # ---- 6:30 AM ----
    - task_id: "OT_010"
      time: "6:30"
      name: "Station Setup"
      duration: 15
      assigned_to: ["Maria", "James"]
      role_required: "chef, line_cook"
      equipment_used: ["GRIDDLE_1", "all_stations"]
      
      procedure:
        - "Maria oversees full station setup"
        - "James arranges griddle station (primary role)"
        - "Elena finishes remaining prep items"
        - "Verify all color-coded boards in place"
        - "Confirm allergen isolation equipment available"
        
      station_assignments:
        griddle_station:
          primary: "James"
          backup: "Maria"
          equipment: "GRIDDLE_1"
          items: ["eggs", "pancakes", "french_toast", "sandwiches"]
          
        egg_station:
          primary: "James"
          backup: "Maria"
          equipment: "BURNER_1, BURNER_2"
          items: ["poached_eggs", "fried_eggs", "scrambled_eggs"]
          
        cold_station:
          primary: "Elena"
          equipment: "reach-in_cooler"
          items: ["produce", "plating", "greens"]
          
        expediting_station:
          primary: "Maria"
          items: ["quality_check", "plating", "allergy_orders"]
        
      allergen_protocol_status:
        verified: true
        isolation_equipment: "dedicated utensils, separate plating area"
        notes: "AP_005 ready for activation if needed"
      
      success_criteria:
        - "All stations fully set by 6:40"
        - "Color-coded boards verified"
        - "Allergen equipment accessible"
        
      notes: "Maria to James: 'Remember, rainy day means slower early service - don't rush the setup quality'"
    
    # ---- 6:40 AM ----
    - task_id: "OT_011"
      time: "6:40"
      name: "Pre-Service Quality Check"
      duration: 5
      assigned_to: "Maria"
      role_required: "chef"
      
      procedure:
        - "Tour all stations"
        - "Verify equipment temperatures"
        - "Spot-check prep items"
        - "Confirm hollandaise quality"
        - "Review low-stock item plan (canadian bacon)"
        - "Verify all staff present and ready"
        
      checklist:
        - [ ] Griddle at 375°F
        - [ ] Fryer at 350°F
        - [ ] All prep items at 40°F or below
        - [ ] Hot holding items at 140°F or above
        - [ ] Color boards correct and sanitized
        - [ ] Allergen equipment ready
        - [ ] Canadian bacon allocation confirmed
        
      success_criteria:
        - "All checklist items verified"
        - "Maria approval given for service start"
        
      notes: "Maria verbal approval required before service begins"
      override_authority: "Maria may delay service start if issues found"

# ============================================================
# SERVICE SECTION
# Target Start: 7:00 AM
# Target End: 2:00 PM
# Duration: 7 hours
# ============================================================

service_section:
  section_id: "service_2025-03-18"
  target_start: "07:00"
  target_end: "14:00"
  duration: 7
  
  # ---- PHASE 1: Early Service ----
  phases:
    - phase_id: "early_service"
      name: "Early Service"
      start_time: "07:00"
      end_time: "09:00"
      duration: 120
      expected_volume: "10-15 tickets"
      volume_tier: "low"
      protocols_active:
        - "Standard Service Protocol"
        - "AP_005 (Allergen Alert Response) [standing]"
      
      tasks:
        - task_id: "ES_001"
          time: "07:00"
          name: "Service Start"
          assigned_to: "Maria"
          action: "Announce service open; verify all stations ready"
          
        - task_id: "ES_002"
          time: "07:00"
          name: "Station Monitoring"
          assigned_to: ["Maria", "James"]
          action: "Begin ticket monitoring; James on griddle, Maria expediting"
          
        - task_id: "ES_003"
          time: "07:00"
          name: "Support Staff Position"
          assigned_to: "Marcus"
          position: " dining_room_support"
          action: "Begin dining room support; ready for kitchen call-backs"
      
      service_targets:
        average_ticket_time: "8 minutes"
        sla_target: "10 minutes"
        max_queue_depth: "5 tickets"
        
      notes: "Rainy day - expect gradual buildup; use early service for quality refinement"
    
    # ---- PHASE 2: Peak Service ----
    - phase_id: "peak_service"
      name: "Peak Service"
      start_time: "09:00"
      end_time: "11:30"
      duration: 150
      expected_volume: "20-25 tickets"
      volume_tier: "high"
      
      protocols_active:
        - "Standard Service Protocol"
        - "High Volume Monitoring Protocol"
        - "AP_005 (Allergen Alert Response) [standing]"
        - "AP_001 (High Volume Response) [conditional - trigger: tickets > 8]"
      
      tasks:
        - task_id: "PS_001"
          time: "09:00"
          name: "Peak Service Begin"
          assigned_to: "Maria"
          action: "Announce peak service; verify griddle at full capacity"
          
        - task_id: "PS_002"
          time: "ongoing"
          name: "Ticket Execution"
          assigned_to: ["James", "Maria"]
          procedure:
            - "Ticket received at station"
            - "James fires griddle items first"
            - "Maria coordinates plating"
            - "Expeditor calls order when complete"
            
        - task_id: "PS_003"
          time: "10:00"
          name: "Support Staff Restock Check"
          assigned_to: "Marcus"
          action: "Check supplies at stations; restock from storage as needed"
          specific_check: "mayonnaise restock (moderate alert)"
          
        - task_id: "PS_004"
          time: "ongoing"
          name: "Quality Spot Checks"
          assigned_to: "Maria"
          frequency: "every 10 tickets"
          action: "Spot check plating quality, temperatures, timing"
      
      adaptation_triggers:
        - trigger_id: "AP_001_TRIGGER"
          condition: "tickets_in_queue > 8"
          threshold: 8
          current_value_checked: true
          response_protocol: "AP_001"
          response_actions_if_triggered:
            - "Maria moves to griddle primary"
            - "James moves to egg station backup"
            - "Peak service timing accelerates by 15 minutes"
            - "Maria notifies team of shift"
            
      service_targets:
        average_ticket_time: "10 minutes"
        sla_target: "12 minutes (elevated for high volume)"
        max_queue_depth: "10 tickets"
        ticket_throughput: "18-20 tickets per hour"
        
      notes: "Peak begins at 9:00 per established pattern; Maria on quality control"
      expected_adaptations:
        - "Elena may assist with plating during peak"
        - "Marcus actively retrieving items to minimize station downtime"
    
    # ---- PHASE 3: Lunch Transition ----
    - phase_id: "lunch_transition"
      name: "Lunch Transition"
      start_time: "11:30"
      end_time: "12:00"
      duration: 30
      expected_volume: "5-10 tickets"
      volume_tier: "decreasing"
      
      protocols_active:
        - "Standard Service Protocol"
        - "Lunch Transition Protocol"
        - "AP_005 (Allergen Alert Response) [standing]"
      
      tasks:
        - task_id: "LT_001"
          time: "11:30"
          name: "Menu Transition"
          assigned_to: "Maria"
          action: "Announce lunch menu active; adjust station for sandwiches/salads"
          
        - task_id: "LT_002"
          time: "11:30"
          name: "Station Reconfiguration"
          assigned_to: ["James", "Elena"]
          action: "Reduce griddle usage; add sandwich assembly area"
          
        - task_id: "LT_003"
          time: "11:45"
          name: "Lunch Prep Check"
          assigned_to: "Elena"
          action: "Verify bread sliced, lettuce prepped, proteins ready"
      
      service_targets:
        average_ticket_time: "7 minutes"
        sla_target: "10 minutes"
        
      notes: "Smooth transition from breakfast to lunch; expect 15-20 minute overlap"
    
    # ---- PHASE 4: Lunch Service ----
    - phase_id: "lunch_service"
      name: "Lunch Service"
      start_time: "12:00"
      end_time: "14:00"
      duration: 120
      expected_volume: "10-15 tickets"
      volume_tier: "moderate"
      
      protocols_active:
        - "Standard Service Protocol"
        - "Wind-Down Awareness Protocol"
        - "AP_005 (Allergen Alert Response) [standing]"
      
      tasks:
        - task_id: "LS_001"
          time: "12:00"
          name: "Lunch Service Begin"
          assigned_to: "Maria"
          action: "Announce lunch service; verify sandwich station ready"
          
        - task_id: "LS_002"
          time: "13:00"
          name: "Afternoon Prep Check"
          assigned_to: "Elena"
          action: "Assess remaining inventory; prepare notes for tomorrow"
          
        - task_id: "LS_003"
          time: "13:30"
          name: "Closing Prep Begin"
          assigned_to: ["Maria", "Elena"]
          action: "Begin non-essential item storage; reduce active equipment"
      
      service_targets:
        average_ticket_time: "6 minutes"
        sla_target: "8 minutes"
        
      notes: "Lighter service allows quality focus and closing prep overlap"

# ============================================================
# CLOSING SECTION
# Target Completion: 15:00
# Duration: 60 minutes
# ============================================================

closing_section:
  section_id: "closing_2025-03-18"
  target_completion: "15:00"
  target_service_end: "14:00"
  closing_window: "14:00-15:00"
  
  tasks:
    - task_id: "CT_001"
      time: "14:00"
      name: "Service End"
      assigned_to: "Maria"
      action: "Announce last call if applicable; verify no open tickets"
      
    - task_id: "CT_002"
      time: "14:05"
      name: "Hot Holding Shutdown"
      assigned_to: ["Maria", "James"]
      action: "Discard items exceeding 2-hour hot hold (HC_001 verification)"
      
    - task_id: "CT_003"
      time: "14:10"
      name: "Station Breakdown"
      pattern_reference: "CT_001"
      duration: 30
      assigned_to: ["Maria", "James"]
      action: "Break down and sanitize all cooking stations"
      
    - task_id: "CT_004"
      time: "14:10"
      name: "Kitchen Cleaning"
      pattern_reference: "CT_002"
      duration: 30
      assigned_to: ["Elena", "Marcus"]
      action: "Clean and sanitize prep areas, floors, equipment surfaces"
      
    - task_id: "CT_005"
      time: "14:30"
      name: "Equipment Shutdown"
      assigned_to: "Maria"
      action: "Power down ovens, fryer (cool cycle), griddle; cover equipment"
      
    - task_id: "CT_006"
      time: "14:45"
      name: "Storage and Organization"
      assigned_to: "Elena"
      action: "Store remaining inventory properly; label and date"
      
    - task_id: "CT_007"
      time: "14:45"
      name: "Final Walk-Through"
      assigned_to: "Maria"
      action: "Inspect all stations; verify cleanliness and organization"
      
    - task_id: "CT_008"
      time: "15:00"
      name: "Closing Tasks Complete"
      assigned_to: "Maria"
      action: "Final verification; Maria signs off on kitchen closure"

# ============================================================
# ADAPTATION PROTOCOLS
# Standing and Conditional Protocols for This Instance
# ============================================================

adaptation_protocols:
  standing:
    - protocol_id: "AP_005"
      name: "Allergen Alert Response"
      status: "active"
      trigger_condition: "allergen_order_received"
      response:
        - "Maria immediately notified"
        - "Allergen isolation protocol enacted"
        - "Dedicated utensils and plating area"
        - "Order fired last"
        - "Maria personal quality check"
      
    - protocol_id: "AP_002"
      name: "Equipment Failure Response"
      status: "standing"
      trigger_condition: "equipment_becomes_unavailable"
      response:
        - "Assess impact on menu items"
        - "Notify Maria immediately"
        - "Activate substitution menu if needed"
        - "Document incident"
      
  conditional:
    - protocol_id: "AP_001"
      name: "High Volume Response"
      status: "ready_to_activate"
      trigger_condition: "tickets_in_queue > 8"
      threshold: 8
      response:
        - "Maria moves to griddle primary"
        - "James moves to egg station backup"
        - "Peak service timing accelerates"
        - "Elena assists with plating if needed"
      activation_criteria:
        - "Queue depth exceeds 8 for more than 5 minutes"
        - "Average ticket time exceeds 12 minutes"
      deactivation_criteria:
        - "Queue depth returns below 5"
        - "Average ticket time under 10 minutes"

# ============================================================
# EXECUTION LOG TEMPLATE
# Metrics and Capture Methods for This Instance
# ============================================================

execution_log_template:
  instance_id: "copper_beech_2025-03-18_daily"
  log_id: "execution_log_2025-03-18"
  
  metrics_to_capture:
    - metric: "ticket_times"
      capture_method: "automated_pos_system"
      format: "JSON array with ticket_id, order_time, fire_time, plate_time, complete_time"
      
    - metric: "sla_compliance"
      capture_method: "calculated_from_ticket_times"
      format: "percentage of tickets within target time"
      
    - metric: "volume_actual"
      capture_method: "pos_ticket_count"
      format: "breakfast_count, lunch_count, total"
      
    - metric: "protocol_activations"
      capture_method: "manual_log_by_maria"
      format: "protocol_id, time_activated, reason, outcome"
      
    - metric: "adaptations_made"
      capture_method: "maria_verbal_note"
