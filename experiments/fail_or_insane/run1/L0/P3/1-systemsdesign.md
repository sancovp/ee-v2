# Build Workflow Generation System

## Implementation Specification: The Copper Beech Kitchen

### Pass 3 — System Build and Instance Generation

---

# I. Implementation Context

## The Copper Beech as Generation Target

The Copper Beech Kitchen represents a specific instantiation of the general small commercial kitchen domain. Building a workflow generation system for this kitchen requires translating the abstract generation architecture from Pass 2 into a concrete implementation tailored to Copper Beech's unique characteristics.

**Key Context Parameters:**

| Parameter | Value | Generation Implication |
|-----------|-------|----------------------|
| Kitchen Size | ~800 sq ft | Limited parallel capacity; flow optimization critical |
| Equipment Count | 12 major pieces | Equipment scheduling constraints moderate |
| Staff Count | 7 evening shift | Role coverage must be explicitly managed |
| Menu Items | 18 dinner items | Recipe dependency complexity high |
| Service Hours | 5:00-10:00 PM | 5-hour service window with defined peaks |
| Average Covers | 45-50 weeknights, 65-70 weekends | Volume variance must be accommodated |

---

# II. System Architecture Implementation

## II.A. Hardware and Infrastructure Requirements

### Computing Infrastructure

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COPPER BEECH GENERATION SYSTEM                          │
│                         INFRASTRUCTURE LAYER                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐ │
│   │                    GENERATION SERVER                                    │ │
│   │   ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                 │ │
│   │   │   CPU: 8    │ │   RAM: 32GB │ │   SSD: 500GB│                 │ │
│   │   │   cores     │ │             │ │             │                 │ │
│   │   └─────────────┘ └─────────────┘ └─────────────┘                 │ │
│   │                                                                      │ │
│   │   Purpose: Workflow generation, constraint solving, scheduling       │ │
│   │   Deployment: On-premise or cloud (Chef's office workstation)        │ │
│   └─────────────────────────────────────────────────────────────────────┘ │
│                                    │                                        │
│                                    │                                        │
│   ┌────────────────────────────────┴────────────────────────────────────┐ │
│   │                       DATA STORAGE LAYER                              │ │
│   │   ┌────────────────┐ ┌────────────────┐ ┌────────────────┐        │ │
│   │   │  Kitchen       │ │  Recipe        │ │  Historical   │        │ │
│   │   │  Context DB   │ │  Library DB    │ │  Performance  │        │ │
│   │   │                │ │                │ │  DB           │        │ │
│   │   │ (PostgreSQL)  │ │ (PostgreSQL)  │ │ (TimescaleDB) │        │ │
│   │   └────────────────┘ └────────────────┘ └────────────────┘        │ │
│   └─────────────────────────────────────────────────────────────────────┘ │
│                                    │                                        │
│                                    │                                        │
│   ┌────────────────────────────────┴────────────────────────────────────┐ │
│   │                       ACCESS INTERFACE LAYER                         │ │
│   │   ┌────────────────┐ ┌────────────────┐ ┌────────────────┐        │ │
│   │   │  Chef's        │ │  Line Cook    │ │  Printed       │        │ │
│   │   │  Dashboard     │ │  Mobile App   │ │  Station Cards │        │ │
│   │   │  (Desktop)     │ │               │ │               │        │ │
│   │   └────────────────┘ └────────────────┘ └────────────────┘        │ │
│   └─────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Display and Output Infrastructure

| Component | Purpose | Location |
|-----------|---------|----------|
| **Chef's Workstation Monitor** | 27" display for workflow review | Chef's office |
| **Kitchen Display Terminal** | 15" touch screen for line reference | Near prep station |
| **Label Printer** | Prep labels, container marking | Prep station |
| **Ticket Printer** | Prep lists, station guides | Prep and each line station |

---

## II.B. Software Architecture

### Core System Components

```python
# copper_beech_generation_system/

class CopperBeechSystem:
    """
    Main system controller for Copper Beech workflow generation.
    Coordinates all subsystems and manages generation lifecycle.
    """
    
    def __init__(self, config: SystemConfig):
        self.context_repository = KitchenContextRepository()
        self.recipe_library = RecipeLibrary()
        self.generation_engine = WorkflowGenerationEngine()
        self.validation_suite = ValidationSuite()
        self.output_generator = OutputGenerator()
        self.learning_engine = LearningEngine()
        
    def generate_daily_workflow(
        self, 
        date: date,
        context_snapshot: ContextSnapshot,
        design_parameters: DesignParameters
    ) -> DailyWorkflowInstance:
        """Generate complete daily workflow for Copper Beech."""
        
        # 1. Load and validate context
        kitchen_context = self.context_repository.load_context(context_snapshot)
        
        # 2. Extract constraints specific to Copper Beech
        constraints = self._extract_copper_beech_constraints(kitchen_context)
        
        # 3. Build dependency graph from menu
        dependency_graph = self._build_dependency_graph(kitchen_context.menu)
        
        # 4. Generate workflow components
        prep_schedule = self._generate_prep_schedule(constraints, dependency_graph)
        station_configs = self._configure_stations(kitchen_context)
        timing_sequences = self._calculate_timing(constraints, prep_schedule)
        role_assignments = self._assign_roles(kitchen_context.staff, station_configs)
        communication_protocols = self._design_communication(station_configs)
        adaptation_plans = self._generate_adaptations(constraints)
        
        # 5. Assemble workflow instance
        workflow = DailyWorkflowInstance(
            date=date,
            kitchen_context=kitchen_context,
            prep_schedule=prep_schedule,
            station_configurations=station_configs,
            timing_sequences=timing_sequences,
            role_assignments=role_assignments,
            communication_protocols=communication_protocols,
            adaptation_plans=adaptation_plans
        )
        
        # 6. Validate workflow
        validation_result = self.validation_suite.validate(workflow, constraints)
        
        # 7. If validation fails, iterate with refinements
        workflow = self._refine_until_valid(workflow, validation_result, constraints)
        
        # 8. Generate outputs
        outputs = self.output_generator.generate(workflow)
        
        return workflow
```

---

## II.C. Context Repository Implementation

### Kitchen Context Database Schema

```sql
-- Copper Beech Kitchen Context Database Schema

-- Physical Layout Table
CREATE TABLE physical_layout (
    layout_id UUID PRIMARY KEY,
    kitchen_name VARCHAR(100) NOT NULL,
    version VARCHAR(20),
    last_updated TIMESTAMP,
    total_square_footage DECIMAL(10,2),
    zone_boundaries JSONB,  -- {zone_name: {bounds: [], temperature_range: []}}
    flow_paths JSONB,       -- [{path_id, from_zone, to_zone, distance_ft, congestion_risk}]
    spatial_graph JSONB     -- Full graph representation
);

-- Station Definition Table
CREATE TABLE stations (
    station_id UUID PRIMARY KEY,
    layout_id UUID REFERENCES physical_layout(layout_id),
    station_name VARCHAR(50) NOT NULL,
    station_type VARCHAR(30) NOT NULL,  -- GRILL, SAUTE, FRY, COLD, PREP, EXPO
    bounds JSONB,  -- {x, y, width, depth, height}
    adjacent_stations UUID[],
    primary_operators_role VARCHAR(50),
    secondary_operators_role VARCHAR(50),
    equipment_assignments JSONB,  -- [{equipment_id, position}]
    capacity_config JSONB  -- {max_concurrent_tasks, max_item_processing}
);

-- Equipment Inventory Table
CREATE TABLE equipment (
    equipment_id UUID PRIMARY KEY,
    station_id UUID REFERENCES stations(station_id),
    equipment_type VARCHAR(50) NOT NULL,
    manufacturer VARCHAR(100),
    model VARCHAR(100),
    capacity_spec JSONB,  -- {type: "pan_count", value: 6}
    current_state VARCHAR(20),  -- OPERATIONAL, NEEDS_MAINTENANCE, OUT_OF_SERVICE
    utility_requirements JSONB,  -- {gas_btuh, electric_amps, water_gpm}
    position_within_station JSONB,
    preheat_time_minutes INTEGER,
    recovery_time_minutes DECIMAL(5,2),
    maintenance_schedule JSONB
);

-- Staff Profile Table
CREATE TABLE staff (
    personnel_id UUID PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(50) NOT NULL,
    skills JSONB,  -- [{skill: "grill", proficiency: 4, certified: true}]
    certifications JSONB,  -- [{type: "ServSafe Manager", expiry: date}]
    cross_training JSONB,  -- [{station: "SAUTE", backup_for: "GRILL"}]
    availability_schedule JSONB,  -- {day: {start_time, end_time, break_required}}
    fatigue_model JSONB  -- {max_shift_hours: 8, performance_curve: []}
);

-- Menu Composition Table
CREATE TABLE menu_items (
    item_id UUID PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    category VARCHAR(30),  -- APPETIZER, ENTREE, DESSERT
    station_assignment VARCHAR(50),
    difficulty_level INTEGER,  -- 1-5
    expected_demand_avg INTEGER,  -- covers per week
    expected_demand_peak INTEGER,
    recipe_id UUID REFERENCES recipes(recipe_id),
    workflow_requirements JSONB  -- {prep_time_min, cook_time_min, holding_window_min}
);

-- Recipe Table
CREATE TABLE recipes (
    recipe_id UUID PRIMARY KEY,
    menu_item_id UUID REFERENCES menu_items(item_id),
    recipe_name VARCHAR(100),
    ingredient_list JSONB,
    transformation_sequence JSONB,  -- [{step: 1, technique: "sear", equipment: "grill", duration_min: 4}]
    timing_profile JSONB,  -- {prep_lead_hours, cook_time_min, rest_time_min, total_time_min}
    quality_standards JSONB,
    equipment_requirements JSONB,
    skill_requirements JSONB,
    holding_requirements JSONB  -- {max_hold_min, temperature_requirements}
);
```

---

## II.D. Generation Engine Implementation

### Constraint Extraction for Copper Beech

```python
class CopperBeechConstraintExtractor:
    """
    Extracts and specializes constraints for the Copper Beech kitchen.
    Incorporates Copper Beech-specific rules and limitations.
    """
    
    def extract_all_constraints(self, context: CopperBeechContext) -> ConstraintNetwork:
        """Extract complete constraint network for Copper Beech."""
        
        constraints = []
        
        # Physical Constraints
        constraints.extend(self._extract_spatial_constraints(context.layout))
        constraints.extend(self._extract_flow_path_constraints(context.layout))
        constraints.extend(self._extract_zone_constraints(context.layout))
        
        # Equipment Constraints
        constraints.extend(self._extract_equipment_capacity_constraints(context.equipment))
        constraints.extend(self._extract_equipment_technique_constraints(context.equipment))
        constraints.extend(self._extract_equipment_failure_constraints(context.equipment))
        
        # Temporal Constraints
        constraints.extend(self._extract_service_window_constraints(context.service_hours))
        constraints.extend(self._extract_prep_window_constraints(context.prep_schedule))
        constraints.extend(self._extract_freshness_constraints(context.menu))
        
        # Human Constraints
        constraints.extend(self._extract_skill_constraints(context.staff, context.menu))
        constraints.extend(self._extract_coverage_constraints(context.staff))
        constraints.extend(self._extract_fatigue_constraints(context.staff))
        
        # Food Safety Constraints
        constraints.extend(self._extract_temperature_constraints(context.menu))
        constraints.extend(self._extract_cross_contamination_constraints(context.stations))
        constraints.extend(self._extract_holding_time_constraints(context.menu))
        
        return ConstraintNetwork(constraints=constraints)
    
    def _extract_spatial_constraints(self, layout: PhysicalLayout) -> List[Constraint]:
        """Extract Copper Beech-specific spatial constraints."""
        
        constraints = []
        
        # Walk-in to Prep Station constraint
        # The walk-in is 15 feet from prep station; this creates a constraint
        # on how far prepped items can travel before requiring temperature protection
        constraints.append(Constraint(
            constraint_id="CB-SPATIAL-001",
            constraint_type=ConstraintType.HARD,
            category=ConstraintCategory.PHYSICAL,
            description="Prep-to-walk-in distance requires efficient organization",
            expression=TravelTimeConstraint(
                source="WALKIN",
                destination="PREP_STATION",
                max_travel_time_minutes=2,
                reason="Temperature control for proteins"
            ),
            priority=10
        ))
        
        # Prep to Line distance constraint
        # 8 feet of travel distance creates timing implications
        constraints.append(Constraint(
            constraint_id="CB-SPATIAL-002",
            constraint_type=ConstraintType.SOFT,
            category=ConstraintCategory.PHYSICAL,
            description="Prep-to-line flow distance affects timing",
            expression=DistanceConstraint(
                source="PREP_STATION",
                destination="HOT_LINE",
                distance_feet=8,
                optimal_travel_time_seconds=15
            ),
            priority=7
        ))
        
        # Cross-contamination zone separation
        # Raw meat prep (adjacent to walk-in) must not cross path to cold assembly
        constraints.append(Constraint(
            constraint_id="CB-SPATIAL-003",
            constraint_type=ConstraintType.HARD,
            category=ConstraintCategory.SAFETY,
            description="Raw and ready food paths must not cross",
            expression=CrossContaminationConstraint(
                raw_zone="PREP_STATION",
                ready_zone="COLD_PREP_STATION",
                prohibited_crossing=True
            ),
            priority=10
        ))
        
        # Station adjacency constraints
        constraints.append(Constraint(
            constraint_id="CB-SPATIAL-004",
            constraint_type=ConstraintType.SOFT,
            category=ConstraintCategory.PHYSICAL,
            description="Grill and Sauté should be adjacent for coordination",
            expression=AdjacencyConstraint(
                station_a="GRILL_STATION",
                station_b="SAUTE_STATION",
                required_adjacency=True,
                reason="Shared sauce work during service"
            ),
            priority=6
        ))
        
        return constraints
    
    def _extract_equipment_capacity_constraints(self, equipment: List[Equipment]) -> List[Constraint]:
        """Extract equipment-specific capacity constraints."""
        
        constraints = []
        
        # Grill capacity constraint
        # Single commercial grill with 4 zones
        grill = self._find_equipment(equipment, "COMMERCIAL_GRILL")
        constraints.append(Constraint(
            constraint_id="CB-EQUIP-001",
            constraint_type=ConstraintType.HARD,
            category=ConstraintCategory.EQUIPMENT,
            description="Grill has maximum 4 simultaneous items",
            expression=CapacityConstraint(
                equipment_id=grill.equipment_id,
                capacity_type="concurrent_items",
                max_value=4,
                reason="4 grill zones available"
            ),
            priority=10
        ))
        
        # Combi oven constraint
        # Shared between multiple uses; recovery time between loads
        combi = self._find_equipment(equipment, "COMBI_OVEN")
        constraints.append(Constraint(
            constraint_id="CB-EQUIP-002",
            constraint_type=ConstraintType.HARD,
            category=ConstraintCategory.EQUIPMENT,
            description="Combi oven requires 5-minute recovery between loads",
            expression=RecoveryTimeConstraint(
                equipment_id=combi.equipment_id,
                recovery_minutes=5,
                reason="Steam/temperature equilibration"
            ),
            priority=9
        ))
        
        # 6-burner range constraint
        # Primary hot work station; no more than 6 active pans
        range_6 = self._find_equipment(equipment, "6_BURNER_RANGE")
        constraints.append(Constraint(
            constraint_id="CB-EQUIP-003",
            constraint_type=ConstraintType.HARD,
            category=ConstraintCategory.EQUIPMENT,
            description="6-burner range limited to 6 active burners",
            expression=CapacityConstraint(
                equipment_id=range_6.equipment_id,
                capacity_type="active_burners",
                max_value=6,
                reason="6 burners physically available"
            ),
            priority=10
        ))
        
        # Fryer constraints
        # 2 baskets; oil temperature recovery time
        fryer = self._find_equipment(equipment, "DOUBLE_DEEP_FRYER")
        constraints.append(Constraint(
            constraint_id="CB-EQUIP-004",
            constraint_type=ConstraintType.HARD,
            category=ConstraintCategory.EQUIPMENT,
            description="Fryer oil temperature requires 3-minute recovery after basket change",
            expression=RecoveryTimeConstraint(
                equipment_id=fryer.equipment_id,
                recovery_minutes=3,
                reason="Oil temperature equilibration"
            ),
            priority=8
        ))
        
        return constraints
    
    def _extract_temporal_constraints(self, context: CopperBeechContext) -> List[Constraint]:
        """Extract time-specific constraints."""
        
        constraints = []
        
        # Service window constraint
        # Service runs 5:00 PM - 10:00 PM
        constraints.append(Constraint(
            constraint_id="CB-TIME-001",
            constraint_type=ConstraintType.HARD,
            category=ConstraintCategory.TEMPORAL,
            description="Service window: 5:00 PM to 10:00 PM",
            expression=TimeWindowConstraint(
                start_time=time(17, 0),
                end_time=time(22, 0),
                hard_boundary=True
            ),
            priority=10
        ))
        
        # Prep window constraint
        # Prep must complete before first seating (5:00 PM)
        # But prep cannot start before 10:00 AM (staff availability)
        constraints.append(Constraint(
            constraint_id="CB-TIME-002",
            constraint_type=ConstraintType.HARD,
            category=ConstraintCategory.TEMPORAL,
            description="Prep window: 10:00 AM to 4:30 PM",
            expression=TimeWindowConstraint(
                start_time=time(10, 0),
                end_time=time(16, 30),
                hard_boundary=True,
                reason="Prep complete before service start, staff availability"
            ),
            priority=10
        ))
        
        # Peak hour timing
        # Friday/Saturday peaks at 7:00 PM and 8:00 PM
        constraints.append(Constraint(
            constraint_id="CB-TIME-003",
            constraint_type=ConstraintType.SOFT,
            category=ConstraintCategory.TEMPORAL,
            description="Friday/Saturday peak service 7:00-8:00 PM",
            expression=PeakWindowConstraint(
                peak_hours=[time(19, 0), time(20, 0)],
                expected_volume_multiplier=1.5,
                recommended_staffing_multiplier=1.25
            ),
            priority=8
        ))
        
        # Ticket time targets
        constraints.append(Constraint(
            constraint_id="CB-TIME-004",
            constraint_type=ConstraintType.SOFT,
            category=ConstraintCategory.TEMPORAL,
            description="Ticket time targets by course",
            expression=TargetTimingConstraint(
                targets={
                    "APPETIZER": 14,  # minutes from order to service
                    "ENTREE": 18,
                    "DESSERT": 12
                },
                hard_max_multiplier=1.3  # 30% buffer acceptable
            ),
            priority=7
        ))
        
        return constraints
    
    def _extract_human_constraints(self, context: CopperBeechContext) -> List[Constraint]:
        """Extract staffing and skill constraints."""
        
        constraints = []
        
        # Minimum staffing constraint
        # Must have at least 4 people to open safely
        constraints.append(Constraint(
            constraint_id="CB-HUMAN-001",
            constraint_type=ConstraintType.HARD,
            category=ConstraintCategory.HUMAN,
            description="Minimum 4 staff required for service",
            expression=MinimumStaffingConstraint(
                min_count=4,
                min_roles=["CHEF", "LINE_COOK", "LINE_COOK", "SUPPORT"],
                reason="Minimum coverage for safe operation"
            ),
            priority=10
        ))
        
        # Standard staffing constraint
        # 7 staff for standard service
        constraints.append(Constraint(
            constraint_id="CB-HUMAN-002",
            constraint_type=ConstraintType.SOFT,
            category=ConstraintCategory.HUMAN,
            description="Standard service with 7 staff",
            expression=StandardStaffingConstraint(
                target_count=7,
                ideal_roles=["CHEF", "SOUS", "GRILL_COOK", "SAUTE_COOK", 
                            "FRY_COLD_COOK", "PREP_COOK", "DISH"]
            ),
            priority=8
        ))
        
        # Skill coverage constraint
        # Must have ServSafe Manager on duty
        constraints.append(Constraint(
            constraint_id="CB-HUMAN-003",
            constraint_type=ConstraintType.HARD,
            category=ConstraintCategory.HUMAN,
            description="ServSafe Manager must be on duty",
            expression=CertificationConstraint(
                required_certification="ServSafe Manager",
                min_count=1,
                reason="Health code requirement"
            ),
            priority=10
        ))
        
        # Cross-training coverage
        # James can cover any station; David can backup sauté; Chen can backup grill
        constraints.append(Constraint(
            constraint_id="CB-HUMAN-004",
            constraint_type=ConstraintType.SOFT,
            category=ConstraintCategory.HUMAN,
            description="Cross-training coverage map",
            expression=CoverageConstraint(
                coverage_map={
                    "GRILL": {"primary": "David", "backup": ["Chen", "James"]},
                    "SAUTE": {"primary": "Chen", "backup": ["David", "James"]},
                    "FRY_COLD": {"primary": "Rosa", "backup": ["Michael", "James"]},
                    "PREP": {"primary": "Michael", "backup": ["Rosa", "James"]},
                    "EXPO": {"primary": "James", "backup": ["Maria"]}
                }
            ),
            priority=7
        ))
        
        # Fatigue constraint
        # Staff should not work more than 8 hours without significant break
        constraints.append(Constraint(
            constraint_id="CB-HUMAN-005",
            constraint_type=ConstraintType.HARD,
            category=ConstraintCategory.HUMAN,
            description="Maximum shift duration and break requirements",
            expression=FatigueConstraint(
                max_shift_hours=8,
                min_break_duration_minutes=30,
                break_frequency_hours=4,
                performance_degradation_threshold=0.85
            ),
            priority=9
        ))
        
        return constraints
    
    def _extract_food_safety_constraints(self, context: CopperBeechContext) -> List[Constraint]:
        """Extract food safety-specific constraints."""
        
        constraints = []
        
        # Temperature danger zone constraint
        constraints.append(Constraint(
            constraint_id="CB-SAFETY-001",
            constraint_type=ConstraintType.HARD,
            category=ConstraintCategory.SAFETY,
            description="Temperature danger zone limits (40°F - 140°F)",
            expression=TemperatureZoneConstraint(
                min_safe_temp_f=40,
                max_safe_temp_f=140,
                max_time_in_danger_zone_minutes=120,
                reason="Bacterial growth prevention"
            ),
            priority=10
        ))
        
        # Cold holding constraint
        constraints.append(Constraint(
            constraint_id="CB-SAFETY-002",
            constraint_type=ConstraintType.HARD,
            category=ConstraintCategory.SAFETY,
            description="Cold foods must be held at 40°F or below",
            expression=ColdHoldingConstraint(
                max_temp_f=40,
                measurement_method="infrared_or_probe",
                frequency_minutes=30
            ),
            priority=10
        ))
        
        # Hot holding constraint
        constraints.append(Constraint(
            constraint_id="CB-SAFETY-003",
            constraint_type=ConstraintType.HARD,
            category=ConstraintCategory.SAFETY,
            description="Hot foods must be held at 140°F or above",
            expression=HotHoldingConstraint(
                min_temp_f=140,
                measurement_method="probe",
                frequency_minutes=30
            ),
            priority=10
        ))
        
        # Cross-contamination prevention
        constraints.append(Constraint(
            constraint_id="CB-SAFETY-004",
            constraint_type=ConstraintType.HARD,
            category=ConstraintCategory.SAFETY,
            description="Raw proteins must not contact ready-to-eat foods",
            expression=CrossContaminationPreventionConstraint(
                raw_materials=["raw_beef", "raw_poultry", "raw_seafood"],
                ready_to_eat=["salads", "dressings", "garnishes"],
                prevention_method="physical_separation",
                required_sanitation_between={
                    "raw_to_ready": ["hand_wash", "glove_change", "surface_sanitize"]
                }
            ),
            priority=10
        ))
        
        # Allergen management
        constraints.append(Constraint(
            constraint_id="CB-SAFETY-005",
            constraint_type=ConstraintType.HARD,
            category=ConstraintCategory.SAFETY,
            description="Allergen protocols must be followed",
            expression=AllergenConstraint(
                major_allergens=["peanuts", "tree_nuts", "dairy", "eggs", 
                               "fish", "shellfish", "soy", "wheat"],
                verification_required=True,
                double_check_required=True,
                documentation_required=True
            ),
            priority=10
        ))
        
        return constraints
```

---

## II.E. Workflow Generation Components

### Prep Schedule Generator

```python
class PrepScheduleGenerator:
    """
    Generates prep schedules for the Copper Beech kitchen.
    Coordinates prep timing, assignments, and dependencies.
    """
    
    def __init__(self, constraint_extractor: CopperBeechConstraintExtractor):
        self.constraint_extractor = constraint_extractor
        self.prep_timing_calculator = PrepTimingCalculator()
        
    def generate_prep_schedule(
        self,
        context: CopperBeechContext,
        service_date: date,
        expected_covers: int
    ) -> PrepSchedule:
        """Generate complete prep schedule for a service day."""
        
        # Calculate required prep quantities
        prep_quantities = self._calculate_prep_quantities(
            context.menu, 
            expected_covers
        )
        
        # Group prep items by timing requirements
        timing_groups = self._group_by_timing(prep_quantities)
        
        # Generate prep items with dependencies
        prep_items = []
        for group_name, items in timing_groups.items():
            for item_name, quantity_needed in items.items():
                prep_item = self._create_prep_item(
                    item_name=item_name,
                    quantity_needed=quantity_needed,
                    timing_group=group_name,
                    context=context
                )
                prep_items.append(prep_item)
        
        # Resolve dependencies
        dependency_graph = self._build_prep_dependency_graph(prep_items)
        
        # Calculate optimal start times
        scheduled_items = self._calculate_start_times(
            prep_items=prep_items,
            dependency_graph=dependency_graph,
            prep_window_end=time(16, 30),  # Must complete by 4:30 PM
            context=context
        )
        
        # Assign to personnel
        assigned_items = self._assign_to_personnel(
            scheduled_items,
            context.staff
        )
        
        # Generate holding specifications
        holding_specs = self._generate_holding_specs(assigned_items)
        
        return PrepSchedule(
            date=service_date,
            prep_items=assigned_items,
            holding_requirements=holding_specs,
            completion_checklist=self._generate_checklist(assigned_items)
        )
    
    def _group_by_timing(self, prep_quantities: Dict[str, int]) -> Dict[str, Dict[str, int]]:
        """
        Group prep items by their timing requirements.
        Long-lead items must start early; quick items can wait.
        """
        
        groups = {
            "LONG_LEAD": {},      # 3+ hours (braises, stocks, fermentations)
            "STANDARD": {},        # 1-3 hours (vegetable prep, sauces)
            "QUICK_TURN": {},      # 15-60 minutes (last-minute prep)
            "SAME_DAY_ONLY": {}    # Must be day of (salads, delicate items)
        }
        
        for item_name, recipe in self.recipe_library.items():
            quantity = prep_quantities.get(item_name, 0)
            if quantity > 0:
                timing_hours = recipe.prep_time_minutes / 60
                
                if timing_hours >= 3:
                    groups["LONG_LEAD"][item_name] = quantity
                elif timing_hours >= 1:
                    groups["STANDARD"][item_name] = quantity
                elif timing_hours >= 0.25:
                    groups["QUICK_TURN"][item_name] = quantity
                else:
                    groups["SAME_DAY_ONLY"][item_name] = quantity
        
        return groups
    
    def _build_prep_dependency_graph(
        self, 
        prep_items: List[PrepItem]
    ) -> DependencyGraph:
        """Build dependency graph for prep items."""
        
        graph = DependencyGraph()
        
        # Add all prep items as nodes
        for item in prep_items:
            graph.add_node(item)
        
        # Add dependencies based on recipe requirements
        for item in prep_items:
            recipe = self.recipe_library.get(item.menu_item_id)
            
            for dependency in recipe.prep_dependencies:
                # Find the dependent prep item
                dependent_item = self._find_prep_item(
                    prep_items, 
                    dependency.ingredient_id
                )
                
                if dependent_item:
                    graph.add_edge(
                        from_node=dependent_item,
                        to_node=item,
                        edge_type=EdgeType.PRECEDENCE,
                        lag_time_minutes=dependency.min_lead_time_minutes
                    )
        
        return graph
    
    def _calculate_start_times(
        self,
        prep_items: List[PrepItem],
        dependency_graph: DependencyGraph,
        prep_window_end: time,
        context: CopperBeechContext
    ) -> List[ScheduledPrepItem]:
        """Calculate optimal start times using critical path analysis."""
        
        # Calculate critical path through prep items
        critical_path = dependency_graph.get_critical_path()
        
        # Work backward from service start to calculate start times
        scheduled_items = []
        current_time = datetime.combine(date.today(), prep_window_end)
        
        # Sort by reverse dependency (items with no dependents first)
        sorted_items = self._topological_sort_reverse(dependency_graph)
        
        for item in sorted_items:
            # Calculate duration
            duration = self._calculate_prep_duration(item, context)
            
            # Calculate latest start time (from dependencies)
            latest_start = self._calculate_latest_start_time(
                item, 
                dependency_graph, 
                current_time
            )
            
            # Calculate earliest start time (from prep window)
            earliest_start = datetime.combine(
                date.today(), 
                time(10, 0)  # Earliest prep start
            )
            
            # Choose optimal start time (allowing for breaks and buffer)
            optimal_start = self._optimize_start_time(
                item=item,
                earliest=earliest_start,
                latest=latest_start,
                duration=duration,
                context=context
            )
            
            scheduled_items.append(ScheduledPrepItem(
                prep_item=item,
                scheduled_start=optimal_start,
                scheduled_end=optimal_start + duration,
                duration_actual=duration
            ))
        
        return scheduled_items
    
    def _optimize_start_time(
        self,
        item: PrepItem,
        earliest: datetime,
        latest: datetime,
        duration: timedelta,
        context: CopperBeechContext
    ) -> datetime:
        """Find optimal start time that balances efficiency and freshness."""
        
        # For most items, prefer earlier start (allows quality check before service)
        # For delicate items, prefer later start (maximizes freshness)
        
        if item.freshness_critical:
            # Start as late as possible within constraints
            return latest - duration
        else:
            # Start early enough to allow quality verification
            target_start = earliest + (latest - earliest - duration) * 0.3
            return target_start
    
    def _assign_to_personnel(
        self,
        scheduled_items: List[ScheduledPrepItem],
        staff: List[Personnel]
    ) -> List[AssignedPrepItem]:
        """Assign prep items to available personnel."""
        
        # Find prep cook(s)
        prep_cooks = [s for s in staff if s.role == "PREP_COOK" or 
                     "PREP" in s.cross_training]
        sous_chef = next((s for s in staff if s.role == "SOUS_CHEF"), None)
        
        assigned_items = []
        available_cooks = list(prep_cooks)
        
        # Sort by scheduled start time
        sorted_items = sorted(scheduled_items, key=lambda x: x.scheduled_start)
        
        for item in sorted_items:
            # Find best available cook
            assigned_cook = self._find_best_available_cook(
                item=item,
                available_cooks=available_cooks,
                current_time=item.scheduled_start,
                sous_chef=sous_chef
            )
            
            if assigned_cook:
                assigned_items.append(AssignedPrepItem(
                    scheduled_item=item,
                    assigned_to=assigned_cook,
                    equipment_required=self._get_required_equipment(item)
                ))
            else:
                # Flag for coverage review
                assigned_items.append(AssignedPrepItem(
                    scheduled_item=item,
                    assigned_to=None,
                    status="UNASSIGNED",
                    coverage_needed=True
                ))
        
        return assigned_items
    
    def _find_best_available_cook(
        self,
        item: PrepItem,
        available_cooks: List[Personnel],
        current_time: datetime,
        sous_chef: Personnel
    ) -> Optional[Personnel]:
        """Find the best available cook for a prep item."""
        
        # Filter by skill match
        qualified_cooks = [
            cook for cook in available_cooks
            if self._has_required_skills(cook, item)
        ]
        
        if not qualified_cooks:
            # Fall back to sous chef
            if sous_chef and self._has_required_skills(sous_chef, item):
                return sous_chef
            return None
        
        # Choose cook with lightest current workload
        return min(
            qualified_cooks, 
            key=lambda c: self._current_workload(c, current_time)
        )
```

### Station Configuration Generator

```python
class StationConfigurationGenerator:
    """
    Generates station configurations for Copper Beech line.
    Configures each station's mise en place, tasks, and protocols.
    """
    
    def __init__(self, context: CopperBeechContext):
        self.context = context
        self.mise_en_place_builder = MiseEnPlaceBuilder()
        
    def generate_all_station_configs(self) -> List[StationConfiguration]:
        """Generate configurations for all Copper Beech stations."""
        
        configs = []
        
        configs.append(self._configure