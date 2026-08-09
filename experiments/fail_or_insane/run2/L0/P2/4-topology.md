# The Copper Beech Daily Workflow Constructor

## Topology: Network of Services, APIs, and Data Flows

### Position: L0P2W[0](4) — Conceptualize · Generally Reify (How MAKE) · Topology

---

## 1. Purpose of This Artifact

While the Abstract Goal (L0P2W[0](0)) established *why we build the Constructor*, the Systems Design (L0P2W[0](1)) established *what the system must achieve*, the Systems Architecture (L0P2W[0](2)) established *how components work together*, and the DSL (L0P2W[0](3)) established *the internal language of the system*, this artifact examines *how the system components are connected*—the topology of services, the APIs that enable communication, and the data flows that transform configuration into workflow.

The question here is: "What is the network of connections that binds the Constructor's components together? How does data move through the system? What are the integration points, the boundaries, and the communication patterns?"

This artifact provides the topological map—the diagram of connections—that reveals how the Constructor hangs together as a unified system.

---

## 2. Architectural Topology Overview

### 2.1 Three-Layer Topology

The Constructor's architecture organizes into three interconnected layers, each with distinct responsibilities and communication patterns:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         INTEGRATION LAYER                                    │
│                                                                             │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐                 │
│  │ Configuration│     │   Workflow  │     │  Feedback   │                 │
│  │   Receiver  │     │  Publisher  │     │  Collector  │                 │
│  └──────┬──────┘     └──────┬──────┘     └──────┬──────┘                 │
│         │                   │                   │                          │
│         └───────────────────┴───────────────────┘                          │
│                             │                                               │
└─────────────────────────────┼───────────────────────────────────────────────┘
                              │
┌─────────────────────────────┼───────────────────────────────────────────────┐
│                         PROCESSING LAYER                                    │
│                             │                                               │
│  ┌─────────────────────────┴─────────────────────────┐                     │
│  │              Configuration Parser                   │                     │
│  └─────────────────────────┬─────────────────────────┘                     │
│                            │                                               │
│  ┌─────────────────────────┴─────────────────────────┐                     │
│  │           Pattern Selection Engine                 │                     │
│  └─────────────────────────┬─────────────────────────┘                     │
│                            │                                               │
│  ┌─────────────────────────┴─────────────────────────┐                     │
│  │              Workflow Assembler                    │                     │
│  └─────────────────────────┬─────────────────────────┘                     │
│                            │                                               │
│  ┌─────────────────────────┴─────────────────────────┐                     │
│  │            Constraint Verifier                    │                     │
│  └─────────────────────────┬─────────────────────────┘                     │
│                            │                                               │
│  ┌─────────────────────────┴─────────────────────────┐                     │
│  │           Adaptation Controller                   │                     │
│  └─────────────────────────┬─────────────────────────┘                     │
│                            │                                               │
└─────────────────────────────┼───────────────────────────────────────────────┘
                              │
┌─────────────────────────────┼───────────────────────────────────────────────┐
│                          KNOWLEDGE LAYER                                    │
│                             │                                               │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌───────────┐     │
│  │  Pattern  │ │   Menu    │ │   Staff   │ │Equipment  │ │ Feedback  │     │
│  │  Library  │ │ Knowledge │ │  Profile  │ │Inventory  │ │  Archive  │     │
│  └───────────┘ └───────────┘ └───────────┘ └───────────┘ └───────────┘     │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │                    Pattern Extraction Engine                           │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │                  Knowledge Integration Manager                         │  │
│  └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Component Connection Topology

The following diagram shows the detailed connections between all components, including data flows and control signals:

```
                                    ┌─────────────────┐
                                    │  File System    │
                                    │ (YAML Config)  │
                                    └────────┬────────┘
                                             │
                                             ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         INTEGRATION LAYER                                   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        Configuration Receiver                          │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────────┐ │   │
│  │  │ File Watch │  │  Schema     │  │ Duplicate Detection         │ │   │
│  │  │  Service   │──│ Validator   │──│   Service                  │ │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┬───────────────┘ │   │
│  └─────────────────────────────────────────────────┼─────────────────┘   │
│                                                      │                    │
│                                    ┌─────────────────┴─────────────────┐   │
│                                    │      Configuration Publisher       │   │
│                                    │  ┌─────────────┐  ┌────────────┐ │   │
│                                    │  │  Display    │  │   Print    │ │   │
│                                    │  │  Formatter  │──│   Formatter│ │   │
│                                    │  └─────────────┘  └────────────┘ │   │
│                                    └─────────────────────────────────────┘   │
│                                                      │                    │
└──────────────────────────────────────────────────────┼────────────────────┘
                                                       │
                        ┌───────────────────────────────┼───────────────────────┐
                        │                               │                       │
                        ▼                               ▼                       ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              PROCESSING LAYER                                   │
│                                                                                 │
│  ┌─────────────────────────────────────────────────────────────────────────┐   │
│  │                         Configuration Parser                              │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌────────────┐ │   │
│  │  │ YAML Parser  │──│ Field        │──│ Normalizer   │──│ Validator  │ │   │
│  │  │              │  │ Validator    │  │              │  │            │ │   │
│  │  └──────────────┘  └──────────────┘  └──────────────┘  └─────┬──────┘ │   │
│  └──────────────────────────────────────────────────────────────┼────────┘   │
│                                                                     │         │
│                                              ┌──────────────────────┴──────┐  │
│                                              │     Pattern Selection Engine   │  │
│                                              │  ┌──────────────────────────┐│  │
│                                              │  │    Menu Coverage          ││  │
│                                              │  │      Calculator          ││  │
│                                              │  └───────────┬──────────────┘│  │
│                                              │              │              │  │
│                                              │  ┌───────────┴──────────────┐│  │
│                                              │  │    Workflow Pattern      ││  │
│                                              │  │       Selector           ││  │
│                                              │  └───────────┬──────────────┘│  │
│                                              │              │              │  │
│                                              │  ┌───────────┴──────────────┐│  │
│                                              │  │    Protocol             ││  │
│                                              │  │   Activator             ││  │
│                                              │  └──────────────────────────┘│  │
│                                              └──────────────┬───────────────┘  │
│                                                             │                │
│                                    ┌────────────────────────┴───────────────┐ │
│                                    │         Workflow Assembler             │ │
│                                    │  ┌──────────────────────────────────┐│ │
│                                    │  │      Temporal Sequencer           ││ │
│                                    │  └──────────────┬───────────────────┘│ │
│                                    │                 │                   │ │
│                                    │  ┌──────────────┴───────────────────┐│ │
│                                    │  │      Staff Assignment            ││ │
│                                    │  │         Engine                   ││ │
│                                    │  └──────────────┬───────────────────┘│ │
│                                    │                 │                   │ │
│                                    │  ┌──────────────┴───────────────────┐│ │
│                                    │  │        Phase                    ││ │
│                                    │  │     Organizer                  ││ │
│                                    │  └──────────────┬───────────────────┘│ │
│                                    │                 │                   │ │
│                                    │  ┌──────────────┴───────────────────┐│ │
│                                    │  │      Documentation              ││ │
│                                    │  │       Generator                 ││ │
│                                    │  └──────────────────────────────────┘│ │
│                                    └──────────────┬───────────────────────┘  │
│                                                       │                      │
│                                    ┌─────────────────┴───────────────────────┐ │
│                                    │         Constraint Verifier            │ │
│                                    │  ┌────────────┐  ┌────────────────┐ │ │
│                                    │  │   HC_001   │  │    HC_002      │ │ │
│                                    │  │  Checker   │  │    Checker     │ │ │
│                                    │  └────────────┘  └───────┬────────┘ │ │
│                                    │                          │          │ │
│                                    │  ┌────────────┐  ┌───────┴────────┐ │ │
│                                    │  │   HC_003   │  │    HC_004      │ │ │
│                                    │  │  Checker   │──│    Checker     │ │ │
│                                    │  └────────────┘  └────────────────┘ │ │
│                                    │                          │          │ │
│                                    │  ┌──────────────────────┴────────┐ │ │
│                                    │  │       Soft Constraint          │ │ │
│                                    │  │         Evaluator             │ │ │
│                                    │  └──────────────────────┬───────┘ │ │
│                                    │                         │         │ │
│                                    │  ┌──────────────────────┴───────┐ │ │
│                                    │  │      Decision                 │ │ │
│                                    │  │      Engine                   │ │ │
│                                    │  └───────────────────────────────┘ │ │
│                                    └────────────────────────────────────┘   │
│                                                       │                      │
│                                    ┌─────────────────┴───────────────────────┐ │
│                                    │         Adaptation Controller          │ │
│                                    │  ┌─────────────┐  ┌───────────────┐ │ │
│                                    │  │  Monitor    │──│   Protocol    │ │ │
│                                    │  │  Service    │  │   Activator   │ │ │
│                                    │  └─────────────┘  └───────────────┘ │ │
│                                    └────────────────────────────────────────┘   │
│                                                       │                      │
└───────────────────────────────────────────────────────┼──────────────────────┘
                                                    │                          │
                                                    ▼                          ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                               KNOWLEDGE LAYER                                   │
│                                                                                 │
│   ┌────────────────────────────────────────────────────────────────────────┐   │
│   │                          Pattern Library Manager                          │   │
│   │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                │   │
│   │  │ Task Pattern │  │Workflow      │  │   Protocol   │                │   │
│   │  │   Loader     │──│ Pattern      │──│   Loader     │                │   │
│   │  │              │  │ Loader       │  │              │                │   │
│   │  └──────────────┘  └──────────────┘  └──────────────┘                │   │
│   └────────────────────────────────────────────────────────────────────────┘   │
│                                                                                 │
│   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│   │    Menu     │  │   Staff     │  │ Equipment   │  │   Report    │        │
│   │ Knowledge   │  │  Profile    │  │ Inventory   │  │  Generator  │        │
│   │  Manager    │  │  Manager    │  │  Manager    │  │             │        │
│   └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └─────────────┘        │
│          │                 │                 │                               │
│          └─────────────────┴────────┬────────┘                               │
│                                     │                                        │
│   ┌─────────────────────────────────┴───────────────────────────────────┐    │
│   │                        Feedback Archive Manager                      │    │
│   │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │    │
│   │  │    Review    │  │   Metrics    │  │  Observation │            │    │
│   │  │   Storage    │  │   Storage    │  │   Storage    │            │    │
│   │  └──────────────┘  └──────────────┘  └──────────────┘            │    │
│   └───────────────────────────────────────────────────────────────────┘    │
│                                     │                                        │
│   ┌─────────────────────────────────┴───────────────────────────────────┐    │
│   │                      Pattern Extraction Engine                        │    │
│   │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │    │
│   │  │ Statistical  │  │  Symbolic    │  │  Temporal    │            │    │
│   │  │  Analyzer    │──│   Analyzer   │──│   Analyzer   │            │    │
│   │  └──────────────┘  └──────────────┘  └──────────────┘            │    │
│   └───────────────────────────────────────────────────────────────────┘    │
│                                     │                                        │
│   ┌─────────────────────────────────┴───────────────────────────────────┐    │
│   │                     Knowledge Integration Manager                      │    │
│   │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐            │    │
│   │  │  Hypothesis  │  │  Validation  │  │   Change     │            │    │
│   │  │  Generator   │──│   Engine     │──│   Applier    │            │    │
│   │  └──────────────┘  └──────────────┘  └──────────────┘            │    │
│   └───────────────────────────────────────────────────────────────────┘    │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
                                                    │
                                                    ▼
                              ┌───────────────────────────────────────┐
                              │           Maria's Review Interface     │
                              │  ┌─────────────┐  ┌───────────────┐ │
                              │  │ Hypothesis  │  │    Daily      │ │
                              │  │  Approver   │──│    Review     │ │
                              │  └─────────────┘  │    Form       │ │
                              │                  └───────────────┘ │
                              └───────────────────────────────────────┘
```

---

## 3. API Interfaces

### 3.1 Configuration Receiver API

**Service**: `ConfigurationReceiverService`

**Purpose**: Receive and validate configuration inputs before processing.

```typescript
interface ConfigurationReceiverAPI {
  // Check for new configurations and validate format
  checkForNewConfigurations(): Promise<ConfigurationFile[]>;
  
  // Validate a configuration file
  validateConfiguration(file: ConfigurationFile): Promise<ValidationResult>;
  
  // Get validation errors for display
  getValidationErrors(validationId: string): ValidationError[];
  
  // Route validated configuration to parser
  routeToParser(validated: ValidatedConfiguration): Promise<void>;
}

// Data types
interface ConfigurationFile {
  path: string;
  filename: string;
  content: string;
  receivedAt: Date;
}

interface ValidationResult {
  isValid: boolean;
  validationId: string;
  errors: ValidationError[];
  warnings: ValidationWarning[];
}

interface ValidationError {
  field: string;
  message: string;
  severity: 'error';
  line?: number;
  column?: number;
}
```

**Connection Points**:
- **Input**: File system monitoring of `daily_configurations/` directory
- **Output**: IPC to Configuration Parser service

### 3.2 Configuration Parser API

**Service**: `ConfigurationParserService`

**Purpose**: Transform raw configuration data into validated, normalized internal representation.

```typescript
interface ConfigurationParserAPI {
  // Main parsing operation
  parse(rawYaml: string): Promise<ParseResult>;
  
  // Validate specific field
  validateField(field: string, value: any): FieldValidationResult;
  
  // Normalize specific value
  normalizeField(field: string, value: any): NormalizedValue;
  
  // Get parse result for inspection
  getParseResult(parseId: string): ParseResult;
}

// Core data types
interface ParseResult {
  success: boolean;
  parseId: string;
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
    volumeTier: VolumeTier;
  };
  weatherIndicator: WeatherIndicator;
  weatherImpact: WeatherImpact;
  specialEvents: SpecialEvent[];
  reservationNotes: string;
  operationalNotes: string;
}
```

**Connection Points**:
- **Input**: IPC from Configuration Receiver
- **Output**: IPC to Pattern Selection Engine

### 3.3 Pattern Selection Engine API

**Service**: `PatternSelectionEngineService`

**Purpose**: Identify patterns from the knowledge layer relevant to the current configuration.

```typescript
interface PatternSelectionEngineAPI {
  // Main selection operation
  selectPatterns(configuration: ValidatedConfiguration): Promise<SelectionResult>;
  
  // Get patterns for specific category
  getTaskPatterns(criteria: TaskPatternCriteria): Promise<TaskPattern[]>;
  
  // Get workflow pattern for context
  getWorkflowPattern(dayType: DayType, volumeTier: VolumeTier): Promise<WorkflowPattern>;
  
  // Check which protocols should activate
  getActiveProtocols(configuration: ValidatedConfiguration): Promise<Protocol[]>;
  
  // Get selection result for inspection
  getSelectionResult(selectionId: string): SelectionResult;
}

// Core data types
interface SelectionResult {
  success: boolean;
  selectionId: string;
  taskPatterns: TaskPattern[];
  workflowPattern: WorkflowPattern;
  activeProtocols: Protocol[];
  selectionRationale: SelectionRationale;
  warnings: SelectionWarning[];
}

interface TaskPatternCriteria {
  category?: TaskCategory;
  assignedRole?: Role;
  outputProduct?: string;
  minDuration?: number;
  maxDuration?: number;
}

interface SelectionRationale {
  menuCoverage: MenuCoverageRationale;
  dayType: DayTypeSelection;
  volumeTier: VolumeTierSelection;
  protocolActivations: ProtocolActivationRationale[];
}
```

**Connection Points**:
- **Input**: IPC from Configuration Parser, direct file access to Pattern Library
- **Output**: IPC to Workflow Assembler

### 3.4 Workflow Assembler API

**Service**: `WorkflowAssemblerService`

**Purpose**: Construct complete workflow instances from selected patterns.

```typescript
interface WorkflowAssemblerAPI {
  // Main assembly operation
  assemble(
    configurationId: string,
    selectionId: string
  ): Promise<AssemblyResult>;
  
  // Sequence tasks by dependencies
  sequenceTasks(tasks: Task[]): Promise<SequencedTask[]>;
  
  // Assign tasks to staff
  assignTasks(
    tasks: Task[],
    staffProfiles: StaffProfile[]
  ): Promise<AssignedTask[]>;
  
  // Organize into phases
  organizeIntoPhases(tasks: AssignedTask[]): Promise<Phase[]>;
  
  // Apply protocol modifications
  applyProtocols(
    workflow: PartialWorkflow,
    protocols: Protocol[]
  ): Promise<ModifiedWorkflow>;
  
  // Get assembly result for inspection
  getAssemblyResult(assemblyId: string): AssemblyResult;
}

// Core data types
interface AssemblyResult {
  success: boolean;
  assemblyId: string;
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
```

**Connection Points**:
- **Input**: IPC from Pattern Selection Engine, direct file access to Staff Profiles
- **Output**: IPC to Constraint Verifier

### 3.5 Constraint Verifier API

**Service**: `ConstraintVerifierService`

**Purpose**: Ensure that assembled workflows satisfy all hard constraints and optimize toward soft constraint targets.

```typescript
interface ConstraintVerifierAPI {
  // Main verification operation
  verify(workflowId: string): Promise<VerificationResult>;
  
  // Check specific constraint
  checkConstraint(
    workflow: WorkflowInstance,
    constraintId: string
  ): Promise<ConstraintCheckResult>;
  
  // Evaluate soft constraint satisfaction
  evaluateSoftConstraints(
    workflow: WorkflowInstance
  ): Promise<SoftConstraintEvaluation[]>;
  
  // Generate constraint report
  generateConstraintReport(
    verificationId: string
  ): Promise<ConstraintReport>;
  
  // Approve or reject workflow
  approveWorkflow(verificationId: string): Promise<ApprovalResult>;
}

// Core data types
interface VerificationResult {
  workflowId: string;
  verificationId: string;
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

interface SoftConstraintEvaluation {
  constraintId: string;
  status: 'satisfied' | 'at_risk' | 'violated';
  target: number;
  projected: number;
  gap: number;
}

interface ApprovalResult {
  approved: boolean;
  verificationId: string;
  nextAction: 'publish' | 'remediate' | 'reject';
  message?: string;
}
```

**Connection Points**:
- **Input**: IPC from Workflow Assembler, direct file access to Constraints definitions
- **Output**: IPC to Workflow Publisher (if approved) or back to Workflow Assembler (if rejected)

### 3.6 Adaptation Controller API

**Service**: `AdaptationControllerService`

**Purpose**: Manage real-time adaptations during workflow execution.

```typescript
interface AdaptationControllerAPI {
  // Configure monitoring for protocols
  configureMonitoring(
    workflowId: string,
    protocols: Protocol[]
  ): Promise<MonitoringConfiguration>;
  
  // Check if trigger condition is met
  checkTrigger(
    trigger: TriggerCondition,
    currentState: ExecutionState
  ): Promise<TriggerStatus>;
  
  // Activate protocol and apply modifications
  activateProtocol(
    protocolId: string,
    workflowId: string,
    executionState: ExecutionState
  ): Promise<AdaptationResult>;
  
  // Record adaptation for feedback
  recordAdaptation(adaptation: AppliedAdaptation): Promise<void>;
  
  // Get monitoring status
  getMonitoringStatus(workflowId: string): Promise<MonitoringStatus>;
}

// Core data types
interface MonitoringConfiguration {
  workflowId: string;
  monitoredTriggers: MonitoredTrigger[];
  checkIntervalMs: number;
  activeSince: Date;
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
  window?: TimeWindow;
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

**Connection Points**:
- **Input**: IPC from Pattern Selection Engine (protocol definitions)
- **Output**: Direct storage to Feedback Archive

### 3.7 Workflow Publisher API

**Service**: `WorkflowPublisherService`

**Purpose**: Deliver generated workflows to stakeholders and archive for reference.

```typescript
interface WorkflowPublisherAPI {
  // Format workflow for display
  formatForDisplay(workflow: WorkflowInstance): Promise<DisplayWorkflow>;
  
  // Generate printable document
  generatePrintable(workflow: WorkflowInstance): Promise<PrintableDocument>;
  
  // Archive workflow instance
  archive(workflow: WorkflowInstance): Promise<ArchiveResult>;
  
  // Send notification of availability
  notifyAvailability(workflow: WorkflowInstance): Promise<void>;
  
  // Get archived workflow
  getArchivedWorkflow(instanceId: string): Promise<WorkflowInstance | null>;
}

// Core data types
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
  content: Buffer;
  printerReady: boolean;
  pageCount: number;
}

interface ArchiveResult {
  success: boolean;
  archivePath: string;
  archivedAt: Date;
}
```

**Connection Points**:
- **Input**: IPC from Constraint Verifier
- **Output**: File system to `daily_workflows/`, display to React UI

### 3.8 Feedback Collector API

**Service**: `FeedbackCollectorService`

**Purpose**: Capture feedback from multiple sources in normalized format.

```typescript
interface FeedbackCollectorAPI {
  // Accept automated metrics
  acceptAutomatedMetrics(metrics: RawMetrics): Promise<NormalizedMetrics>;
  
  // Accept Maria's review
  acceptMariaReview(review: MariaReviewInput): Promise<NormalizedReview>;
  
  // Accept staff observation
  acceptStaffObservation(observation: StaffObservationInput): Promise<NormalizedObservation>;
  
  // Validate feedback completeness
  validateFeedback(feedback: NormalizedFeedback): Promise<ValidationResult>;
  
  // Store validated feedback
  store(feedback: NormalizedFeedback): Promise<StorageResult>;
}

// Core data types
interface MariaReviewInput {
  date: string;
  overallRating: number;
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

interface StorageResult {
  success: boolean;
  storageId: string;
  storedAt: Date;
}
```

**Connection Points**:
- **Input**: React UI forms, POS system integration
- **Output**: SQLite database (Feedback Archive)

### 3.9 Pattern Extraction Engine API

**Service**: `PatternExtractionEngineService`

**Purpose**: Analyze accumulated feedback to identify patterns and generate hypotheses.

```typescript
interface PatternExtractionEngineAPI {
  // Run full extraction cycle
  runExtraction(timeRange: TimeRange): Promise<ExtractionResult>;
  
  // Run statistical analysis
  analyzeStatistical(timeRange: TimeRange): Promise<StatisticalPatterns>;
  
  // Run symbolic analysis
  analyzeSymbolic(timeRange: TimeRange): Promise<SymbolicPatterns>;
  
  // Run temporal analysis
  analyzeTemporal(timeRange: TimeRange): Promise<TemporalPatterns>;
  
  // Generate hypotheses from patterns
  generateHypotheses(patterns: ExtractedPattern[]): Promise<Hypothesis[]>;
}

// Core data types
interface ExtractionResult {
  extractionId: string;
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

interface Hypothesis {
  hypothesisId: string;
  generatedDate: Date;
  source: string;
  description: string;
  proposedChange: ProposedChange;
  evidence: any;
  validationStatus: 'pending' | 'validated' | 'rejected';
  reviewStatus: 'pending' | 'approved' | 'denied';
}
```

**Connection Points**:
- **Input**: Direct SQLite queries to Feedback Archive
- **Output**: SQLite storage of hypotheses, IPC to Knowledge Integration Manager

### 3.10 Knowledge Integration Manager API

**Service**: `KnowledgeIntegrationManagerAPI`

**Purpose**: Apply validated knowledge modifications to the knowledge base.

```typescript
interface KnowledgeIntegrationManagerAPI {
  // Validate hypothesis
  validateHypothesis(hypothesis: Hypothesis): Promise<ValidationResult>;
  
  // Present hypothesis to Maria
  presentForApproval(hypothesis: Hypothesis): Promise<void>;
  
  // Apply approved hypothesis
  applyApproved(hypothesisId: string, approvedBy: string): Promise<IntegrationResult>;
  
  // Rollback change
  rollback(changeId: string, reason: string): Promise<RollbackResult>;
  
  // Get pending hypotheses
  getPendingHypotheses(): Promise<Hypothesis[]>;
  
  // Get change history
  getChangeHistory(elementId?: string): Promise<KnowledgeChange[]>;
}

// Core data types
interface ValidationResult {
  passed: boolean;
  checks: {
    safetyCheck: { passed: boolean; details: string };
    consistencyCheck: { passed: boolean; details: string };
    benefitCheck: { passed: boolean; details: string };
  };
  overallResult: 'validated' | 'rejected' | 'needs_review';
}

interface IntegrationResult {
  success: boolean;
  changeId: string;
  hypothesisId: string;
  modifiedStructures: string[];
  effectiveDate: Date;
}

interface RollbackResult {
  success: boolean;
  changeId: string;
  rolledBackAt: Date;
  message?: string;
}

interface KnowledgeChange {
  changeId: string;
  hypothesisId: string;
  integrationDate: Date;
  structureChanged: string;
  elementId: string;
  fieldChanged: string;
  previousValue: any;
  newValue: any;
  approvedBy: string;
  effectiveDate: Date;
  rollbackAvailable: boolean;
}
```

**Connection Points**:
- **Input**: IPC from Pattern Extraction Engine, direct SQLite queries
- **Output**: File system to Pattern Library, Staff Profiles; SQLite to Knowledge Changes

---

## 4. Data Flow Architecture

### 4.1 Primary Generation Data Flow

The primary data flow transforms configuration inputs into workflow outputs:

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                            PRIMARY GENERATION DATA FLOW                          │
│                                                                                 │
│  ┌─────────────────┐                                                            │
│  │   YAML Config   │                                                            │
│  │     File        │                                                            │
│  │ (copper_beech_  │                                                            │
│  │   YYYY-MM-DD_   │                                                            │
│  │    config.yaml) │                                                            │
│  └────────┬────────┘                                                            │
│           │                                                                      │
│           ▼                                                                      │
│  ┌─────────────────┐     ┌─────────────────┐     ┌─────────────────────────┐   │
│  │  Configuration  │────▶│  Configuration  │────▶│   Pattern Selection     │   │
│  │   Receiver      │     │    Parser       │     │      Engine            │   │
│  └─────────────────┘     └─────────────────┘     └───────────┬─────────────┘   │
│                                                             │                   │
│                                                             ▼                   │
│                                               ┌─────────────────────────────┐   │
│                                               │       Knowledge Layer       │   │
│                                               │  ┌─────────┐ ┌─────────┐   │   │
│                                               │  │ Pattern │ │  Menu   │   │   │
│                                               │  │ Library │ │Knowledge│   │   │
│                                               │  └─────────┘ └─────────┘   │   │
│                                               │  ┌─────────┐ ┌─────────┐   │   │
│                                               │  │  Staff  │ │Equipment│   │   │
│                                               │  │Profiles │ │Inventory│   │   │
│                                               │  └─────────┘ └─────────┘   │   │
│                                               └───────────────┬─────────────┘   │
│                                                               │                 │
│                                                               ▼                 │
│                                               ┌─────────────────────────────┐   │
│                                               │    Selected Patterns        │   │
│                                               │  • Task Patterns (TP_###)  │   │
│                                               │  • Workflow Patterns        │   │
│                                               │  • Active Protocols         │   │
│                                               │  • Selection Rationale      │   │
│                                               └───────────────┬─────────────┘   │
│                                                               │                 │
│                                                               ▼                 │
│                                               ┌─────────────────────────────┐   │
│                                               │    Workflow Assembler       │   │
│                                               │  ┌─────────────────────┐   │   │
│                                               │  │ Temporal Sequencer  │   │   │
│                                               │  └──────────┬──────────┘   │   │
│                                               │             │              │   │
│                                               │  ┌──────────┴──────────┐   │   │
│                                               │  │  Staff Assignment   │   │   │
│                                               │  │      Engine        │   │   │
│                                               │  └──────────┬──────────┘   │   │
│                                               │             │              │   │
│                                               │  ┌──────────┴──────────┐   │   │
│                                               │  │    Phase            │   │   │
│                                               │  │   Organizer         │   │   │
│                                               │  └─────────────────────┘   │   │
│                                               └────────────