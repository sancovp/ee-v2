# The Copper Beech Daily Workflow Constructor

## Systems Architecture: Module Design, Interfaces, Data Flow, and Control Flow

### Position: L0P2W[0](2) — Conceptualize · Generally Reify (How MAKE) · SystemsArchitecture

---

## 1. Purpose of This Artifact

While the Abstract Goal (L0P2W[0](0)) established *why we build the Constructor* and the Systems Design (L0P2W[0](1)) established *what the system must achieve*, this artifact examines *how the components work together* to fulfill that purpose. We address the architectural decisions that enable the system to generate daily workflows: the module structure, the interfaces between modules, the data that flows through the system, and the control mechanisms that govern generation.

The question here is: "What is the internal architecture of the generation system, and how do its parts cooperate to transform configuration inputs into workflow outputs?"

---

## 2. Architectural Overview

### 2.1 The Generation Problem

The core architectural challenge is transformation: the Constructor must transform a configuration—a set of parameters describing a specific day's circumstances—into a workflow—a complete, executable plan for that day's operations. This transformation is not simple mapping but involves reasoning, adaptation, and verification.

The architecture must support:
- **Configuration ingestion** with validation and normalization
- **Knowledge retrieval** from persistent pattern libraries
- **Pattern selection** appropriate to the specific context
- **Workflow assembly** from selected patterns
- **Constraint verification** ensuring safety and quality
- **Adaptation** responding to anticipated conditions
- **Documentation** maintaining traceability

### 2.2 Architectural Philosophy

The architecture embodies three guiding principles:

**Separation of Concerns**: Each module handles a distinct aspect of the generation problem. Configuration parsing is separate from pattern selection, which is separate from workflow assembly, which is separate from constraint verification. This separation enables independent development and testing of each concern.

**Knowledge Isolation**: The Constructor's persistent knowledge—patterns, constraints, protocols, staff profiles—exists in dedicated structures, separate from processing logic. This isolation enables learning: knowledge can be modified without changing code, and code can evolve without losing accumulated learning.

**Transparency by Design**: Every decision the system makes is logged with sufficient context to understand its rationale. The architecture includes explicit documentation mechanisms rather than treating documentation as an afterthought.

### 2.3 Three-Layer Architecture

The Constructor's architecture organizes into three interconnected layers:

```
┌─────────────────────────────────────────────────────────────────────┐
│                         INTEGRATION LAYER                           │
│                                                                     │
│  Handles communication between the system and its environment:      │
│  - Configuration input reception                                    │
│  - Workflow output delivery                                          │
│  - Feedback capture                                                  │
│  - Report generation                                                 │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         PROCESSING LAYER                            │
│                                                                     │
│  Transforms inputs into outputs through staged processing:          │
│  - Configuration Parser: Validates and normalizes inputs            │
│  - Pattern Selection Engine: Selects relevant patterns              │
│  - Workflow Assembler: Constructs complete workflow instances       │
│  - Constraint Verifier: Ensures safety and quality requirements     │
│  - Adaptation Controller: Applies context-specific modifications    │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────────────┐
│                          KNOWLEDGE LAYER                           │
│                                                                     │
│  Stores persistent operational knowledge used by the processing     │
│  layer to generate workflows:                                       │
│  - Pattern Library: Task patterns, workflow patterns, protocols    │
│  - Menu Knowledge: Menu items, components, allergen flags          │
│  - Staff Profiles: Roles, capabilities, learning records            │
│  - Equipment Inventory: Capabilities, constraints, status          │
│  - Feedback Archive: Historical execution records                   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. Module Design

### 3.1 Integration Layer Modules

#### 3.1.1 Configuration Receiver Module

**Purpose**: Receive and validate configuration inputs before processing.

**Responsibilities**:
- Monitor the configuration input directory for new files
- Validate configuration file format (YAML)
- Detect duplicate configurations for the same date
- Route validated configurations to the Configuration Parser

**Public Interface**:
```typescript
interface ConfigurationReceiver {
  // Check for new configurations and validate format
  checkForNewConfigurations(): ConfigurationFile[];
  
  // Validate a configuration file
  validateConfiguration(file: ConfigurationFile): ValidationResult;
  
  // Route validated configuration to parser
  routeToParser(validated: ValidatedConfiguration): void;
}
```

**Data Structures**:
```typescript
interface ConfigurationFile {
  path: string;
  filename: string;
  content: string;
  receivedAt: Date;
}

interface ValidationResult {
  isValid: boolean;
  errors: ValidationError[];
  warnings: ValidationWarning[];
}

interface ValidationError {
  field: string;
  message: string;
  severity: 'error';
}

interface ValidationWarning {
  field: string;
  message: string;
  severity: 'warning';
}
```

**Dependencies**:
- Reads from: `daily_configurations/` directory
- Outputs to: Configuration Parser module

---

#### 3.1.2 Workflow Publisher Module

**Purpose**: Deliver generated workflows to stakeholders and archive for reference.

**Responsibilities**:
- Format workflow instances for human readability
- Deliver workflows to Maria's workstation display
- Generate printable workflow documents
- Archive completed workflow instances
- Notify stakeholders of workflow availability

**Public Interface**:
```typescript
interface WorkflowPublisher {
  // Format workflow for display
  formatForDisplay(workflow: WorkflowInstance): DisplayWorkflow;
  
  // Generate printable document
  generatePrintable(workflow: WorkflowInstance): PrintableDocument;
  
  // Archive workflow instance
  archive(workflow: WorkflowInstance): ArchiveResult;
  
  // Send notification of availability
  notifyAvailability(workflow: WorkflowInstance): void;
}
```

**Data Structures**:
```typescript
interface DisplayWorkflow {
  header: WorkflowHeader;
  sections: DisplaySection[];
  footer: WorkflowFooter;
}

interface WorkflowHeader {
  instanceId: string;
  date: string;
  dayOfWeek: string;
  generatedAt: string;
  configurationSummary: ConfigurationSummary;
  constraintVerificationStatus: ConstraintStatusSummary;
}

interface PrintableDocument {
  format: 'pdf' | 'html';
  content: string;
  printerReady: boolean;
}

interface ArchiveResult {
  success: boolean;
  archivePath: string;
  archivedAt: Date;
}
```

**Dependencies**:
- Reads from: Workflow Assembler module
- Outputs to: `daily_workflows/` directory, Maria's workstation, printer

---

#### 3.1.3 Feedback Collector Module

**Purpose**: Capture feedback from multiple sources in normalized format.

**Responsibilities**:
- Accept automated metrics from POS system integration
- Present interface for Maria's post-service review
- Receive staff observations via Maria's capture
- Validate and normalize feedback data
- Store feedback in the feedback archive

**Public Interface**:
```typescript
interface FeedbackCollector {
  // Accept automated metrics
  acceptAutomatedMetrics(metrics: RawMetrics): NormalizedMetrics;
  
  // Accept Maria's review
  acceptMariaReview(review: MariaReviewInput): NormalizedReview;
  
  // Accept staff observations
  acceptStaffObservation(observation: StaffObservationInput): NormalizedObservation;
  
  // Validate feedback completeness
  validateFeedback(feedback: NormalizedFeedback): ValidationResult;
  
  // Store validated feedback
  store(feedback: NormalizedFeedback): StorageResult;
}
```

**Data Structures**:
```typescript
interface MariaReviewInput {
  date: string;
  overallRating: number; // 1-5
  whatWentWell: string;
  whatCouldImprove: string;
  specificObservations: string;
  adjustmentRecommendations: string;
}

interface StaffObservationInput {
  date: string;
  staffMember: string;
  observationType: 'positive' | 'negative' | 'suggestion';
  content: string;
  significance: 'low' | 'medium' | 'high';
}

interface NormalizedFeedback {
  date: string;
  automatedMetrics?: NormalizedMetrics;
  mariaReview?: NormalizedReview;
  staffObservations: NormalizedObservation[];
  capturedAt: Date;
}
```

**Dependencies**:
- Reads from: POS system, Maria's review interface, staff observation capture
- Outputs to: Feedback Archive (SQLite)

---

#### 3.1.4 Report Generator Module

**Purpose**: Produce reports summarizing system activity and learning.

**Responsibilities**:
- Generate daily summary reports
- Generate weekly pattern reports
- Generate hypothesis status reports
- Provide query interface for historical data

**Public Interface**:
```typescript
interface ReportGenerator {
  // Generate daily summary
  generateDailySummary(date: string): DailySummaryReport;
  
  // Generate weekly pattern report
  generateWeeklyPatternReport(startDate: string, endDate: string): WeeklyPatternReport;
  
  // Generate hypothesis status report
  generateHypothesisStatus(): HypothesisStatusReport;
  
  // Query historical workflows
  queryWorkflows(query: WorkflowQuery): WorkflowInstance[];
}
```

**Dependencies**:
- Reads from: Feedback Archive, Workflow Archive, Hypothesis Store
- Outputs to: Report interface, Maria's review meetings

---

### 3.2 Processing Layer Modules

#### 3.2.1 Configuration Parser Module

**Purpose**: Transform raw configuration data into validated, normalized internal representation.

**Responsibilities**:
- Parse YAML configuration format
- Validate required fields are present
- Validate field values are within acceptable ranges
- Normalize time formats to standard representation
- Normalize volume expressions to tier indicators
- Normalize weather conditions to impact categories
- Produce detailed validation report

**Processing Steps**:
```
1. PARSE_YAML(configuration_content)
   └─► YAML parse result or syntax error

2. VALIDATE_REQUIRED_FIELDS(parsed_yaml)
   └─► Missing field errors or continue

3. VALIDATE_FIELD_VALUES(parsed_yaml)
   └─► Value range errors or continue

4. NORMALIZE_TIME_FIELDS(parsed_yaml)
   └─► Parsed configuration with normalized times

5. NORMALIZE_VOLUME_TIER(parsed_yaml.expected_volume)
   └─► Parsed configuration with volume tier

6. NORMALIZE_WEATHER_IMPACT(parsed_yaml.weather_indicator)
   └─► Parsed configuration with weather impact

7. BUILD_VALIDATION_REPORT(parsed_config)
   └─► ValidationResult with errors, warnings, parsed data
```

**Public Interface**:
```typescript
interface ConfigurationParser {
  // Main parsing operation
  parse(rawConfiguration: string): ParseResult;
  
  // Validate specific field
  validateField(field: string, value: any): FieldValidationResult;
  
  // Normalize specific value
  normalizeField(field: string, value: any): NormalizedValue;
}
```

**Data Structures**:
```typescript
interface ParseResult {
  success: boolean;
  validatedConfiguration?: ValidatedConfiguration;
  errors: ParseError[];
  warnings: ParseWarning[];
}

interface ValidatedConfiguration {
  configurationId: string;
  date: string;
  dayOfWeek: DayOfWeek;
  dailyContext: NormalizedDailyContext;
  staffConfiguration: NormalizedStaffConfiguration;
  inventoryConfiguration: NormalizedInventoryConfiguration;
  equipmentConfiguration: NormalizedEquipmentConfiguration;
  validationTimestamp: Date;
}

interface NormalizedDailyContext {
  expectedVolume: {
    breakfastTickets: VolumeRange;
    lunchTickets: VolumeRange;
    volumeTier: VolumeTier; // 'low' | 'medium' | 'high' | 'extreme'
  };
  weatherIndicator: WeatherIndicator;
  weatherImpact: WeatherImpact; // 'none' | 'moderate' | 'significant'
  specialEvents: SpecialEvent[];
  reservationNotes: string;
  operationalNotes: string;
}

type VolumeTier = 'low' | 'medium' | 'high' | 'extreme';
type WeatherIndicator = 'clear' | 'rainy' | 'cold' | 'hot';
type WeatherImpact = 'none' | 'moderate' | 'significant';
```

**Dependencies**:
- Reads from: Configuration Receiver module
- Outputs to: Pattern Selection Engine module

---

#### 3.2.2 Pattern Selection Engine Module

**Purpose**: Identify patterns from the knowledge layer relevant to the current configuration.

**Responsibilities**:
- Select task patterns based on menu coverage requirements
- Select workflow patterns based on day type and volume tier
- Identify adaptation protocols to activate based on trigger conditions
- Filter patterns by staff availability and capabilities
- Rank pattern alternatives by relevance

**Selection Logic**:
```
1. DETERMINE_MENU_COVERAGE(configuration)
   └─► List of menu items likely to be ordered

2. SELECT_TASK_PATTERNS(menu_coverage, staff_configuration)
   └─► Task patterns covering required menu items
   
3. DETERMINE_DAY_TYPE(daily_context)
   └─► Day type: 'weekday' | 'weekend' | 'special'

4. DETERMINE_VOLUME_TIER(configuration)
   └─► Volume tier: 'low' | 'medium' | 'high' | 'extreme'

5. SELECT_WORKFLOW_PATTERNS(day_type, volume_tier)
   └─► Opening, service, and closing workflow patterns

6. CHECK_PROTOCOL_TRIGGERS(configuration)
   └─► Protocols to activate (standing + conditional)

7. VALIDATE_STAFF_ASSIGNMENTS(selected_patterns, staff_configuration)
   └─► Confirmation that all assignments are possible
```

**Public Interface**:
```typescript
interface PatternSelectionEngine {
  // Main selection operation
  selectPatterns(configuration: ValidatedConfiguration): SelectionResult;
  
  // Get patterns for specific category
  getTaskPatterns(menuItems: MenuItem[]): TaskPattern[];
  
  // Get workflow pattern for context
  getWorkflowPattern(dayType: DayType, volumeTier: VolumeTier): WorkflowPattern;
  
  // Check which protocols should activate
  getActiveProtocols(configuration: ValidatedConfiguration): Protocol[];
}
```

**Data Structures**:
```typescript
interface SelectionResult {
  success: boolean;
  taskPatterns: TaskPattern[];
  workflowPattern: WorkflowPattern;
  activeProtocols: Protocol[];
  selectionRationale: SelectionRationale;
  warnings: SelectionWarning[];
}

interface SelectionRationale {
  menuCoverage: MenuCoverageRationale;
  dayType: DayTypeSelection;
  volumeTier: VolumeTierSelection;
  protocolActivations: ProtocolActivationRationale[];
}

interface MenuCoverageRationale {
  anticipatedItems: string[];
  coveredByPatterns: string[];
  coveragePercentage: number;
}

interface ProtocolActivationRationale {
  protocolId: string;
  activationType: 'standing' | 'conditional';
  triggerCondition?: string;
  reason: string;
}
```

**Dependencies**:
- Reads from: Configuration Parser module, Knowledge Layer (Pattern Library, Menu Knowledge, Staff Profiles)
- Outputs to: Workflow Assembler module

---

#### 3.2.3 Workflow Assembler Module

**Purpose**: Construct complete workflow instances from selected patterns.

**Responsibilities**:
- Arrange tasks in proper temporal sequence based on dependencies
- Assign tasks to staff based on roles, capabilities, and availability
- Organize tasks into operational phases
- Apply adaptation modifications from active protocols
- Insert tasks required by protocols
- Verify task completeness and consistency
- Generate documentation (configuration summary, generation notes)

**Assembly Algorithm**:
```
1. INITIALIZE_WORKFLOW_INSTANCE(configuration, date)
   └─► Empty workflow structure with metadata

2. ASSEMBLE_OPENING_SEQUENCE(workflow_pattern.opening, staff_profiles)
   └─► Opening tasks arranged temporally, assigned to staff

3. ASSEMBLE_SERVICE_PHASES(workflow_pattern.service, staff_profiles, protocols)
   └─► Service phases with tasks, timing, assignments

4. ASSEMBLE_CLOSING_SEQUENCE(workflow_pattern.closing, staff_profiles)
   └─► Closing tasks arranged temporally, assigned to staff

5. APPLY_PROTOCOL_MODIFICATIONS(assembled_workflow, active_protocols)
   └─► Workflow with protocol insertions and adjustments

6. ORGANIZE_INTO_PHASES(assembled_workflow)
   └─► Phases with defined boundaries and transitions

7. GENERATE_DOCUMENTATION(assembled_workflow, configuration)
   └─► Configuration summary, generation notes, rationale

8. BUILD_EXECUTION_LOG_TEMPLATE(assembled_workflow)
   └─► Metrics to capture, capture methods
```

**Public Interface**:
```typescript
interface WorkflowAssembler {
  // Main assembly operation
  assemble(
    configuration: ValidatedConfiguration,
    selection: SelectionResult
  ): AssemblyResult;
  
  // Sequence tasks by dependencies
  sequenceTasks(tasks: Task[]): SequencedTask[];
  
  // Assign tasks to staff
  assignTasks(tasks: Task[], staffProfiles: StaffProfile[]): AssignedTask[];
  
  // Organize into phases
  organizeIntoPhases(tasks: AssignedTask[]): Phase[];
  
  // Apply protocol modifications
  applyProtocols(workflow: PartialWorkflow, protocols: Protocol[]): ModifiedWorkflow;
}
```

**Data Structures**:
```typescript
interface AssemblyResult {
  success: boolean;
  workflow?: WorkflowInstance;
  phaseStructure?: PhaseStructure;
  taskAssignments?: TaskAssignment[];
  documentation?: WorkflowDocumentation;
  errors: AssemblyError[];
  warnings: AssemblyWarning[];
}

interface WorkflowInstance {
  instanceId: string;
  date: string;
  generatedAt: Date;
  generatedBy: string;
  configurationSummary: ConfigurationSummary;
  openingSection: OpeningSection;
  serviceSection: ServiceSection;
  closingSection: ClosingSection;
  executionLogTemplate: ExecutionLogTemplate;
  adaptationProtocols: AppliedProtocol[];
}

interface PhaseStructure {
  opening: Phase;
  service: Phase[];
  closing: Phase;
}

interface TaskAssignment {
  taskId: string;
  taskName: string;
  assignedTo: string;
  roleRequired: string;
  assignmentRationale: string;
}
```

**Dependencies**:
- Reads from: Pattern Selection Engine module, Knowledge Layer (Staff Profiles)
- Outputs to: Constraint Verifier module

---

#### 3.2.4 Constraint Verifier Module

**Purpose**: Ensure that assembled workflows satisfy all hard constraints and optimize toward soft constraint targets.

**Responsibilities**:
- Check HC_001: Food Safety Temperature Control
- Check HC_002: Cross-Contamination Prevention
- Check HC_003: Minimum Staffing Levels
- Check HC_004: Time-Temperature Combinations
- Evaluate soft constraint satisfaction (SLA targets, timing preferences)
- Report constraint satisfaction status
- Approve or reject workflow based on constraint status

**Verification Logic**:
```
1. VERIFY_HC_001(workflow)
   ├─► Check prep item temperatures
   ├─► Track time-temperature exposure
   ├─► Verify cumulative time in danger zone < 2 hours
   └─► PASS | FAIL with details

2. VERIFY_HC_002(workflow)
   ├─► Verify color-coded board assignments
   ├─► Check allergen isolation capabilities
   └─► PASS | FAIL with details

3. VERIFY_HC_003(workflow)
   ├─► Verify minimum 3 staff for service phases
   ├─► Check coverage during overlapping tasks
   └─► PASS | FAIL with details

4. VERIFY_HC_004(workflow)
   ├─► Check all prep cycles
   ├─► Verify maximum 4-hour prep time per item
   └─► PASS | FAIL with details

5. EVALUATE_SOFT_CONSTRAINTS(workflow)
   ├─► Check SLA target compliance projection
   ├─► Check timing preference alignment
   └─► SATISFIED | AT_RISK | VIOLATED

6. DETERMINE_WORKFLOW_STATUS(constraint_results)
   ├─► All HC satisfied: APPROVED
   └─► Any HC violated: REJECTED
```

**Public Interface**:
```typescript
interface ConstraintVerifier {
  // Main verification operation
  verify(workflow: WorkflowInstance): VerificationResult;
  
  // Check specific constraint
  checkConstraint(
    workflow: WorkflowInstance,
    constraintId: string
  ): ConstraintCheckResult;
  
  // Evaluate soft constraint satisfaction
  evaluateSoftConstraints(
    workflow: WorkflowInstance
  ): SoftConstraintEvaluation[];
  
  // Generate constraint report
  generateConstraintReport(
    verification: VerificationResult
  ): ConstraintReport;
}
```

**Data Structures**:
```typescript
interface VerificationResult {
  workflowId: string;
  overallStatus: 'approved' | 'rejected';
  hardConstraints: HardConstraintResult[];
  softConstraints: SoftConstraintResult[];
  verificationTimestamp: Date;
}

interface HardConstraintResult {
  constraintId: 'HC_001' | 'HC_002' | 'HC_003' | 'HC_004';
  status: 'satisfied' | 'violated';
  details: string;
  checkedElements: CheckedElement[];
  violations?: ConstraintViolation[];
}

interface ConstraintViolation {
  element: string;
  description: string;
  severity: 'critical' | 'major' | 'minor';
  remediation?: string;
}

interface SoftConstraintResult {
  constraintId: string;
  status: 'satisfied' | 'at_risk' | 'violated';
  target: number;
  projected: number;
  gap: number;
}

interface CheckedElement {
  elementId: string;
  elementType: 'task' | 'phase' | 'workflow';
  checkedAt: Date;
  result: 'pass' | 'fail';
}
```

**Dependencies**:
- Reads from: Workflow Assembler module, Knowledge Layer (Constraint Definitions)
- Outputs to: Workflow Publisher module (if approved) or back to Workflow Assembler (if rejected with remediation)

---

#### 3.2.5 Adaptation Controller Module

**Purpose**: Manage real-time adaptations during workflow execution.

**Responsibilities**:
- Monitor trigger conditions during execution
- Activate protocols when triggers are met
- Apply protocol response actions to executing workflows
- Track adaptations for feedback capture
- Coordinate with execution monitoring systems

**Note**: The Adaptation Controller operates during execution, not generation. Its role in the generation architecture is to pre-configure monitoring for conditional protocols.

**Pre-Generation Responsibilities**:
```
1. CONFIGURE_PROTOCOL_MONITORING(active_protocols)
   └─► Set up trigger condition monitoring for execution

2. GENERATE_ADAPTATION_TRIGGERS(workflow_instance, protocols)
   └─► Document trigger conditions to monitor during execution

3. PREPARE_ADAPTATION_LOG(workflow_instance)
   └─► Create structure for recording adaptations
```

**Public Interface**:
```typescript
interface AdaptationController {
  // Configure monitoring for protocols
  configureMonitoring(
    workflow: WorkflowInstance,
    protocols: Protocol[]
  ): MonitoringConfiguration;
  
  // Check if trigger condition is met
  checkTrigger(
    trigger: TriggerCondition,
    currentState: ExecutionState
  ): TriggerStatus;
  
  // Activate protocol and apply modifications
  activateProtocol(
    protocol: Protocol,
    workflow: WorkflowInstance,
    executionState: ExecutionState
  ): AdaptationResult;
  
  // Record adaptation for feedback
  recordAdaptation(adaptation: AppliedAdaptation): void;
}
```

**Data Structures**:
```typescript
interface MonitoringConfiguration {
  workflowId: string;
  monitoredTriggers: MonitoredTrigger[];
  checkIntervalMs: number;
}

interface MonitoredTrigger {
  protocolId: string;
  condition: TriggerCondition;
  lastChecked: Date;
  currentStatus: 'active' | 'inactive' | 'approaching';
}

interface TriggerCondition {
  type: 'threshold' | 'time' | 'state_change';
  metric: string;
  operator: '>' | '<' | '>=' | '<=' | '==' | '!=';
  value: number | string;
  window?: TimeWindow; // For time-based triggers
}

interface AdaptationResult {
  protocolId: string;
  activatedAt: Date;
  modifications: WorkflowModification[];
  adaptationsRecorded: AppliedAdaptation[];
}

interface WorkflowModification {
  type: 'task_insertion' | 'task_removal' | 'reassignment' | 'timing_change';
  target: string;
  previousState: any;
  newState: any;
  reason: string;
}
```

**Dependencies**:
- Reads from: Pattern Selection Engine module (protocol definitions)
- Coordinates with: Execution monitoring systems during runtime

---

### 3.3 Knowledge Layer Modules

#### 3.3.1 Pattern Library Manager Module

**Purpose**: Manage the persistent storage and retrieval of patterns.

**Responsibilities**:
- Load pattern library from JSON files
- Provide version management for patterns
- Support pattern queries by type, category, and criteria
- Enable pattern updates through the knowledge integration process
- Maintain pattern change history

**Note**: The Pattern Library Manager is a facade over the JSON files in `pattern_library/`. It provides structured access and caching, but the actual data resides in human-readable files.

**Public Interface**:
```typescript
interface PatternLibraryManager {
  // Load all patterns
  loadLibrary(): PatternLibrary;
  
  // Get task patterns
  getTaskPatterns(criteria?: TaskPatternCriteria): TaskPattern[];
  
  // Get workflow patterns
  getWorkflowPatterns(criteria?: WorkflowPatternCriteria): WorkflowPattern[];
  
  // Get specific pattern by ID
  getPattern(patternType: PatternType, patternId: string): Pattern | null;
  
  // Update pattern (via knowledge integration)
  updatePattern(pattern: Pattern, changeId: string): UpdateResult;
  
  // Get pattern version history
  getPatternHistory(patternType: PatternType, patternId: string): PatternVersion[];
}
```

**Data Structures**:
```typescript
interface PatternLibrary {
  taskPatterns: TaskPattern[];
  workflowPatterns: WorkflowPattern[];
  constraints: ConstraintDefinition[];
  protocols: ProtocolDefinition[];
  loadedAt: Date;
  version: string;
}

interface TaskPattern {
  id: string;
  version: number;
  name: string;
  duration: number; // minutes
  assignedRoles: Role[];
  inputs: string[];
  outputs: string[];
  dependencies: string[]; // IDs of prerequisite tasks
  colorBoard?: ColorBoard;
  allergenFlags?: AllergenFlag[];
  category: TaskCategory;
  created: Date;
  modified: Date;
}

interface WorkflowPattern {
  id: string;
  version: number;
  name: string;
  type: 'opening' | 'service' | 'closing';
  taskSequence: WorkflowTaskReference[];
  phases: Phase[];
  applicableVolumeTiers: VolumeTier[];
  applicableDayTypes: DayType[];
  created: Date;
  modified: Date;
}

interface TaskPatternCriteria {
  category?: TaskCategory;
  assignedRole?: Role;
  outputProduct?: string;
  minDuration?: number;
  maxDuration?: number;
}

interface WorkflowPatternCriteria {
  type?: 'opening' | 'service' | 'closing';
  volumeTier?: VolumeTier;
  dayType?: DayType;
}
```

**Dependencies**:
- Reads from: `data/pattern_library/` JSON files
- Writes to: Pattern library files (via Knowledge Integration)

---

#### 3.3.2 Staff Profile Manager Module

**Purpose**: Manage staff profile data and provide capability matching for task assignment.

**Responsibilities**:
- Load and cache staff profiles
- Provide staff lookup by name
- Support capability queries for task assignment
- Track staff availability for specific dates
- Update learning records

**Public Interface**:
```typescript
interface StaffProfileManager {
  // Load all staff profiles
  loadProfiles(): StaffProfile[];
  
  // Get specific staff profile
  getProfile(name: string): StaffProfile | null;
  
  // Get staff by role
  getStaffByRole(role: Role): StaffProfile[];
  
  // Find best match for task
  findBestMatch(task: TaskPattern, availableStaff: StaffProfile[]): StaffMatch[];
  
  // Check availability for date
  checkAvailability(names: string[], date: string): AvailabilityResult[];
  
  // Update learning record
  updateLearningRecord(name: string, record: LearningEntry): void;
}
```

**Data Structures**:
```typescript
interface StaffProfile {
  name: string;
  role: Role;
  certifications: Certification[];
  strengths: Strength[];
  typicalAssignments: string[]; // Task pattern IDs
  learningRecord: LearningEntry[];
  created: Date;
  modified: Date;
}

interface LearningEntry {
  date: Date;
  observation: string;
  adjustment: string;
  approvedBy: string;
}

interface StaffMatch {
  staffMember: StaffProfile;
  matchScore: number; // 0-100
  matchReasons: string[];
  potentialIssues: string[];
}

type Role = 'chef' | 'line_cook' | 'prep_cook' | 'support';
type Certification = 'food_safety_manager' | 'food_handler' | 'allergen_aware';
type Strength = 'all_stations' | 'quality_control' | 'mise_en_place' | 'produce_prep' | 'grill' | 'eggs_backup' | 'coverage' | 'cleaning';
```

**Dependencies**:
- Reads from: `data/staff_profiles.json`
- Writes to: Staff profiles file (via Knowledge Integration)

---

#### 3.3.3 Menu Knowledge Manager Module

**Purpose**: Manage menu item definitions and support menu-related queries.

**Responsibilities**:
- Load menu knowledge from JSON file
- Provide menu item lookup by ID
- Support component queries for task coverage
- Manage allergen information
- Handle category specifications

**Public Interface**:
```typescript
interface MenuKnowledgeManager {
  // Load menu knowledge
  loadMenuKnowledge(): MenuKnowledge;
  
  // Get breakfast items
  getBreakfastItems(): MenuItem[];
  
  // Get lunch items
  getLunchItems(): MenuItem[];
  
  // Get item by ID
  getMenuItem(itemId: string): MenuItem | null;
  
  // Get items by category
  getItemsByCategory(category: MenuCategory): MenuItem[];
  
  // Check allergen content
  checkAllergens(itemId: string): AllergenFlag[];
  
  // Get category specifications
  getCategorySpec(category: MenuCategory): CategorySpec | null;
}
```

**Data Structures**:
```typescript
interface MenuKnowledge {
  breakfastItems: MenuItem[];
  lunchItems: MenuItem[];
  categorySpecs: CategorySpec[];
  loadedAt: Date;
}

interface MenuItem {
  id: string;
  name: string;
  category: MenuCategory;
  components: string[];
  cookingMethod: string;
  typicalDuration: number; // minutes
  allergenFlags: AllergenFlag[];
  equipmentRequirements: string[];
}

type MenuCategory = 'eggs' | 'griddle' | 'sandwiches' | 'salads' | 'sides';
type AllergenFlag = 'dairy' | 'eggs' | 'gluten' | 'soy' | 'nuts' | 'shellfish';

interface CategorySpec {
  category: MenuCategory;
  temperatureRange?: string;
  timingNotes: string;
  commonAllergens: AllergenFlag[];
}
```

**Dependencies**:
- Reads from: `data/menu_knowledge.json`

---

#### 3.3.4 Equipment Inventory Manager Module

**Purpose**: Manage equipment inventory and capabilities.

**Responsibilities**:
- Load equipment inventory
- Provide equipment lookup by ID and type
- Track equipment status
- Support capability queries for task requirements

**Public Interface**:
```typescript
interface EquipmentInventoryManager {
  // Load equipment inventory
  loadInventory(): EquipmentInventory;
  
  // Get all operational equipment
  getOperationalEquipment(): Equipment[];
  
  // Get equipment by ID
  getEquipment(equipmentId: string): Equipment | null;
  
  // Get equipment by type
  getEquipmentByType(type: EquipmentType): Equipment[];
  
  // Check equipment availability
  checkAvailability(equipmentIds: string[], date: string): AvailabilityResult;
}
```

**Dependencies**:
- Reads from: `data/equipment_inventory.json`

---

#### 3.3.5 Feedback Archive Manager Module

**Purpose**: Manage the SQLite feedback archive database.

**Responsibilities**:
- Store normalized feedback records
- Support pattern extraction queries
- Maintain hypothesis status tracking
- Enable historical workflow queries

**Public Interface**:
```typescript
interface FeedbackArchiveManager {
  // Store daily review
  storeDailyReview(review: NormalizedReview): StorageResult;
  
  // Store staff observation
  storeStaffObservation(observation: NormalizedObservation): StorageResult;
  
  // Store automated metrics
  storeAutomatedMetrics(metrics: NormalizedMetrics): StorageResult;
  
  // Query reviews by date range
  queryReviews(startDate: string, endDate: string): NormalizedReview[];
  
  // Query observations by staff member
  queryObservationsByStaff(staffMember: string, limit?: number): NormalizedObservation[];
  
  // Query metrics by date
  queryMetrics(date: string): NormalizedMetrics | null;
  
  // Store hypothesis
  storeHypothesis(hypothesis: Hypothesis): StorageResult;
  
  // Update hypothesis status
  updateHypothesisStatus(hypothesisId: string, status: HypothesisStatus): void;
  
  // Get pending hypotheses
  getPendingHypotheses(): Hypothesis[];
  
  // Store knowledge change
  storeKnowledgeChange(change: KnowledgeChange): StorageResult;
}
```

**Dependencies**:
- Reads/Writes: `databases/feedback_archive.db` (SQLite)

---

### 3.4 Learning Layer Modules

#### 3.4.1 Pattern Extraction Engine Module

**Purpose**: Analyze accumulated feedback to identify patterns and generate hypotheses.

**Responsibilities**:
- Execute statistical pattern detection
- Execute symbolic pattern recognition
- Execute temporal pattern analysis
- Generate hypotheses for knowledge improvements
- Support extraction for specific time periods

**Public Interface**:
```typescript
interface PatternExtractionEngine {
  // Run full extraction cycle
  runExtraction(timeRange: TimeRange): ExtractionResult;
  
  // Run statistical analysis
  analyzeStatistical(timeRange: TimeRange): StatisticalPatterns;
  
  // Run symbolic analysis
  analyzeSymbolic(timeRange: TimeRange): SymbolicPatterns;
  
  // Run temporal analysis
  analyzeTemporal(timeRange: TimeRange): TemporalPatterns;
  
  // Generate hypotheses from patterns
  generateHypotheses(patterns: ExtractedPattern[]): Hypothesis[];
}
```

**Data Structures**:
```typescript
interface ExtractionResult {
  extractionDate: Date;
  timeRange: TimeRange;
  statisticalPatterns: StatisticalPattern[];
  symbolicPatterns: SymbolicPattern[];
  temporalPatterns: TemporalPattern[];
  generatedHypotheses: Hypothesis[];
}

interface StatisticalPattern {
  patternType: 'timing_deviation' | 'volume_correlation' | 'sla_trend';
  affectedElement: string;
  description: string;
  evidence: StatisticalEvidence;
  confidence: 'low' | 'medium' | 'high';
}

interface StatisticalEvidence {
  sampleSize: number;
  meanValue: number;
  expectedValue: number;
  deviation: number;
  standardDeviation: number;
  correlationCoefficient?: number;
}

interface SymbolicPattern {
  patternType: 'successful_adaptation' | 'staff_insight' | 'protocol_effectiveness';
  affectedElement: string;
  description: string;
  evidence: SymbolicEvidence;
  confidence: 'low' | 'medium' | 'high';
}

interface SymbolicEvidence {
  occurrences: number;
  positiveOutcomes: number;
  mariaValidation?: boolean;
}

interface TemporalPattern {
  patternType: 'recurring_issue' | 'cyclical_variation' | 'learning_progress';
  affectedElement: string;
  description: string;
  evidence: TemporalEvidence;
  confidence: 'low' | 'medium' | 'high';
}

interface TemporalEvidence {
  frequency: number;
  periodicity?: string; // 'weekly', 'monthly', 'seasonal'
  consistency: number; // 0-100
}
```

**Dependencies**:
- Reads from: Feedback Archive Manager module
- Outputs to: Hypothesis store (via Feedback Archive Manager)

