# The Copper Beech Daily Workflow Constructor

## Engineered System: Complete Instance Specification

### Position: L0P2W[0](5) — Conceptualize · Generally Reify (How MAKE) · EngineeredSystem

---

## 1. Purpose of This Artifact

While the Abstract Goal (L0P2W[0](0)) established *why we build the Constructor*, the Systems Design (L0P2W[0](1)) established *what the system must achieve*, the Systems Architecture (L0P2W[0](2)) established *how components work together*, the DSL (L0P2W[0](3)) established *the internal language of the system*, and the Topology (L0P2W[0](4)) established *how components are connected*, this artifact examines *what a fully realized instance of the Constructor looks like when concretely instantiated and operational*.

The question here is: "If we were to build and deploy the Copper Beech Daily Workflow Constructor, what would the complete system look like? What code modules would exist? What data structures would be implemented? What interfaces would be created? How would the system be deployed and operated?"

This artifact provides the concrete answer—a fully realized engineering specification that transforms all abstract designs into implementable components.

---

## 2. Instance Context: Building for Copper Beech Cafe

Before examining the engineered system itself, we establish the concrete context that shapes its construction. The Constructor is not built for an abstract kitchen but for a specific establishment with specific characteristics.

### 2.1 The Target Kitchen

**Establishment**: Copper Beech Cafe
**Location**: [Specific address]
**Seating Capacity**: 42 seats
**Operating Hours**: 7:00 AM - 2:00 PM (breakfast and lunch service)
**Service Days**: Monday through Sunday
**Staff Count**: 4 regular staff members (Maria, James, Elena, Marcus)

**Physical Configuration**:
- Kitchen layout: Single-room production kitchen
- Equipment: 1 griddle, 1 fryer, 1 convection oven, 6-burner range
- Stations: Griddle station, egg station, prep station, cold station, expediting station
- Storage: Walk-in cooler, dry storage, refrigerated reach-in

**Operational Profile**:
- Average daily volume: 25-35 breakfast tickets, 10-15 lunch tickets
- Peak service: Saturday, 9:00 AM - 11:30 AM (35-45 tickets)
- Low volume days: Monday-Tuesday (18-25 tickets)
- Seasonal variations: Summer increase, post-holiday decrease

### 2.2 The Staff

**Maria** (Kitchen Manager/Head Chef):
- Role: Chef, quality arbiter, ultimate authority
- Certifications: Food Safety Manager, Allergen Aware
- Strengths: All stations, quality control, problem resolution
- Learning: 4 years of operational patterns accumulated
- Typical assignments: Hollandaise preparation, final quality check, expediting

**James** (Line Cook):
- Role: Line cook, grill specialist
- Certifications: Food Handler
- Strengths: Grill, eggs backup
- Learning: Efficiency improving over time
- Typical assignments: Griddle primary, egg station backup

**Elena** (Prep Cook):
- Role: Prep cook, production enabler
- Certifications: Food Handler
- Strengths: Mise en place, produce prep
- Learning: Reduced produce prep time from 30 to 25 minutes
- Typical assignments: All prep tasks, produce station

**Marcus** (Support Staff):
- Role: Support, coverage provider
- Certifications: Food Handler
- Strengths: Coverage, cleaning, supply retrieval
- Learning: Coverage patterns
- Typical assignments: Support rotations, closing tasks

### 2.3 The Menu

**Breakfast Menu** (23 items):
- **Eggs Category** (10 items): Eggs Any Style, Eggs Benedict, Omelette (8 variations)
- **Griddle Items** (8 items): Pancakes, French Toast, Breakfast Sandwich, etc.
- **Sides** (5 items): Hash Browns, Fresh Fruit, Toast, etc.

**Lunch Menu** (8 items):
- **Sandwiches** (5 items): BLT, Turkey Club, Grilled Cheese, etc.
- **Salads** (3 items): Caesar Salad, House Salad, etc.

### 2.4 The Constraints

**Hard Constraints** (invariant):
- HC_001: Food Safety Temperature Control (40°F-140°F danger zone, 2-hour cumulative maximum)
- HC_002: Cross-Contamination Prevention (color-coded cutting boards, allergen isolation)
- HC_003: Minimum Staffing Levels (3 staff minimum for service)
- HC_004: Time-Temperature Combinations (4-hour prep item maximum)

**Soft Constraints** (optimizable):
- SC_001: SLA Compliance (90% target)
- SC_002: Opening Target (6:45 AM completion)
- SC_003: Service Start (7:00 AM)
- SC_004: Closing Target (3:00 PM completion)

---

## 3. System Architecture: Complete Component Map

### 3.1 Architectural Overview

The Copper Beech Daily Workflow Constructor employs a three-layer architecture:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         INTEGRATION LAYER                                   │
│  Configuration Receiver  │  Workflow Publisher  │  Feedback Collector       │
│  Report Generator                                                        │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PROCESSING LAYER                                   │
│  Configuration Parser  │  Pattern Selection  │  Workflow Assembler          │
│  Constraint Verifier   │  Adaptation Controller                                    │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
┌─────────────────────────────────────────────────────────────────────────────┐
│                          KNOWLEDGE LAYER                                   │
│  Pattern Library  │  Menu Knowledge  │  Staff Profiles  │  Equipment      │
│  Feedback Archive  │  Pattern Extraction  │  Knowledge Integration          │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Component Directory Structure

```
copper_beech_constructor/
│
├── src/
│   ├── main/
│   │   ├── index.ts                    # Electron main process entry
│   │   ├── ipc-handlers.ts             # IPC communication handlers
│   │   └── engine/
│   │   │   ├── index.ts                # Engine entry point
│   │   │   ├── config-parser.ts        # Configuration parsing module
│   │   │   ├── pattern-selection.ts     # Pattern selection module
│   │   │   ├── workflow-assembler.ts    # Workflow assembly module
│   │   │   ├── constraint-verifier.ts   # Constraint verification module
│   │   │   ├── adaptation-controller.ts  # Adaptation management module
│   │   │   ├── feedback-integration.ts  # Feedback processing module
│   │   │   └── knowledge-integration.ts # Knowledge update module
│   │   │
│   │   ├── knowledge/
│   │   │   ├── index.ts                # Knowledge layer entry
│   │   │   ├── pattern-library.ts      # Pattern library management
│   │   │   ├── staff-profiles.ts       # Staff profile management
│   │   │   ├── menu-knowledge.ts        # Menu knowledge management
│   │   │   ├── equipment-inventory.ts   # Equipment management
│   │   │   └── feedback-archive.ts      # Feedback storage management
│   │   │
│   │   ├── learning/
│   │   │   ├── index.ts                # Learning layer entry
│   │   │   ├── pattern-extraction.ts    # Pattern extraction engine
│   │   │   ├── hypothesis-generator.ts   # Hypothesis generation
│   │   │   └── validation-engine.ts     # Hypothesis validation
│   │   │
│   │   └── types/
│   │       ├── index.ts                # Type definitions entry
│   │       ├── configuration.ts         # Configuration types
│   │       ├── workflow.ts              # Workflow types
│   │       ├── pattern.ts               # Pattern types
│   │       ├── constraint.ts            # Constraint types
│   │       ├── protocol.ts              # Protocol types
│   │       ├── staff.ts                # Staff types
│   │       ├── feedback.ts              # Feedback types
│   │       └── learning.ts              # Learning types
│   │
│   └── renderer/
│       ├── index.tsx                   # React entry point
│       ├── App.tsx                     # Main application component
│       ├── components/
│       │   ├── Layout/
│       │   │   ├── MainLayout.tsx
│       │   │   ├── Header.tsx
│       │   │   └── Navigation.tsx
│       │   ├── Dashboard/
│       │   │   ├── Dashboard.tsx
│       │   │   ├── StatusCard.tsx
│       │   │   └── RecentActivity.tsx
│       │   ├── Workflow/
│       │   │   ├── WorkflowViewer.tsx
│       │   │   ├── WorkflowTimeline.tsx
│       │   │   ├── TaskList.tsx
│       │   │   └── TaskCard.tsx
│       │   ├── Configuration/
│       │   │   ├── ConfigForm.tsx
│       │   │   ├── ContextSection.tsx
│       │   │   ├── StaffSection.tsx
│       │   │   ├── InventorySection.tsx
│       │   │   └── EquipmentSection.tsx
│       │   ├── Feedback/
│       │   │   ├── ReviewForm.tsx
│       │   │   ├── ObservationList.tsx
│       │   │   └── MetricsDisplay.tsx
│       │   ├── Reports/
│       │   │   ├── ReportDashboard.tsx
│       │   │   ├── DailySummary.tsx
│       │   │   ├── WeeklyPatterns.tsx
│       │   │   └── HypothesisList.tsx
│       │   └── Common/
│       │       ├── Button.tsx
│       │       ├── Card.tsx
│       │       ├── FormField.tsx
│       │       ├── Modal.tsx
│       │       ├── Table.tsx
│       │       └── Toast.tsx
│       │
│       ├── views/
│       │   ├── DashboardView.tsx
│       │   ├── WorkflowView.tsx
│       │   ├── ConfigurationView.tsx
│       │   ├── FeedbackView.tsx
│       │   ├── ReportsView.tsx
│       │   └── SettingsView.tsx
│       │
│       ├── hooks/
│       │   ├── useWorkflow.ts
│       │   ├── useConfiguration.ts
│       │   ├── useFeedback.ts
│       │   └── useLearning.ts
│       │
│       ├── services/
│       │   ├── api.ts                   # IPC communication wrapper
│       │   ├── storage.ts               # Local storage utilities
│       │   └── pdf-generator.ts         # PDF generation for printing
│       │
│       └── styles/
│           ├── index.css
│           ├── variables.css
│           └── components/
│
├── data/
│   ├── pattern_library/
│   │   ├── task_patterns.json
│   │   ├── workflow_patterns.json
│   │   ├── constraints.json
│   │   └── protocols.json
│   │
│   ├── menu_knowledge.json
│   ├── staff_profiles.json
│   ├── equipment_inventory.json
│   │
│   ├── daily_configurations/
│   │   └── .gitkeep
│   │
│   ├── daily_workflows/
│   │   └── .gitkeep
│   │
│   └── historical_workflows/
│       └── .gitkeep
│
├── databases/
│   ├── feedback_archive.db
│   └── metrics_warehouse.db
│
├── tests/
│   ├── unit/
│   │   ├── engine/
│   │   │   ├── config-parser.test.ts
│   │   │   ├── pattern-selection.test.ts
│   │   │   ├── workflow-assembler.test.ts
│   │   │   └── constraint-verifier.test.ts
│   │   ├── knowledge/
│   │   │   ├── pattern-library.test.ts
│   │   │   └── staff-profiles.test.ts
│   │   └── learning/
│   │       └── pattern-extraction.test.ts
│   │
│   └── integration/
│       ├── generation.test.ts
│       └── feedback-loop.test.ts
│
├── package.json
├── tsconfig.json
├── electron-builder.yml
├── webpack.config.js
└── README.md
```

---

## 4. Module Specifications

### 4.1 Engine Module Specifications

#### 4.1.1 Configuration Parser Module

**File**: `src/main/engine/config-parser.ts`

**Purpose**: Transform raw YAML configuration data into validated, normalized internal representation.

**Public Interface**:
```typescript
export class ConfigurationParser {
  /**
   * Parse raw YAML configuration content
   * @param rawYaml Raw YAML string from configuration file
   * @returns ParseResult with validated configuration or errors
   */
  public parse(rawYaml: string): Promise<ParseResult>;
  
  /**
   * Validate a specific field value
   * @param field Field name
   * @param value Value to validate
   * @returns FieldValidationResult
   */
  public validateField(field: string, value: unknown): FieldValidationResult;
  
  /**
   * Normalize a field value to internal format
   * @param field Field name
   * @param value Value to normalize
   * @returns Normalized value
   */
  public normalizeField(field: string, value: unknown): unknown;
}
```

**Internal Processing**:
```typescript
// Step 1: Parse YAML
private parseYaml(yaml: string): YamlParseResult;

// Step 2: Validate required fields
private validateRequiredFields(parsed: object): ValidationError[];

// Step 3: Validate field values
private validateFieldValues(parsed: object): ValidationError[];

// Step 4: Normalize values
private normalizeConfiguration(parsed: object): ValidatedConfiguration;

// Step 5: Build validation report
private buildValidationReport(config: ValidatedConfiguration, errors: ValidationError[]): ParseResult;
```

**Key Validations**:
- `date`: Must be valid YYYY-MM-DD format
- `day_of_week`: Must be Monday-Sunday
- `expected_volume.breakfast_tickets.min`: Must be >= 0
- `expected_volume.breakfast_tickets.max`: Must be >= min
- `staff_configuration.scheduled`: Must have at least 3 staff
- `staff_configuration.scheduled[].role`: Must be valid role

**Key Normalizations**:
- `volume_tier`: Derive from ticket ranges (low: <20, medium: 20-35, high: 35-50, extreme: >50)
- `weather_impact`: Map weather indicator to impact (clear: none, rainy: moderate, cold/hot: significant)

---

#### 4.1.2 Pattern Selection Engine Module

**File**: `src/main/engine/pattern-selection.ts`

**Purpose**: Identify patterns from the knowledge layer relevant to the current configuration.

**Public Interface**:
```typescript
export class PatternSelectionEngine {
  constructor(
    private patternLibrary: PatternLibraryManager,
    private menuKnowledge: MenuKnowledgeManager,
    private staffProfiles: StaffProfileManager
  );
  
  /**
   * Select patterns appropriate for the given configuration
   * @param configuration Validated configuration
   * @returns SelectionResult with selected patterns and rationale
   */
  public selectPatterns(configuration: ValidatedConfiguration): Promise<SelectionResult>;
  
  /**
   * Get task patterns for specific menu items
   * @param menuItems Menu items to cover
   * @returns Array of task patterns
   */
  public getTaskPatternsForMenu(menuItems: MenuItem[]): Promise<TaskPattern[]>;
  
  /**
   * Get workflow pattern for day type and volume tier
   * @param dayType Day type
   * @param volumeTier Volume tier
   * @returns Selected workflow pattern
   */
  public getWorkflowPattern(dayType: DayType, volumeTier: VolumeTier): Promise<WorkflowPattern>;
  
  /**
   * Determine which protocols should activate
   * @param configuration Validated configuration
   * @returns Array of protocols to activate
   */
  public getActiveProtocols(configuration: ValidatedConfiguration): Promise<Protocol[]>;
}
```

**Selection Logic**:
```typescript
// Menu Coverage Determination
private determineMenuCoverage(config: ValidatedConfiguration): MenuItem[] {
  // Based on volume tier, determine likely menu item distribution
  const volumeTier = config.dailyContext.expectedVolume.volumeTier;
  // Return menu items with expected ordering probability based on historical data
}

// Task Pattern Selection
private selectTaskPatterns(menuItems: MenuItem[]): TaskPattern[] {
  // For each menu item, find task patterns that produce required outputs
  // Filter by staff availability
  // Return selected task patterns
}

// Workflow Pattern Selection
private selectWorkflowPattern(dayType: DayType, volumeTier: VolumeTier): WorkflowPattern {
  // Find workflow patterns matching day type and volume tier
  // Select most appropriate based on specific context
}

// Protocol Activation
private determineActiveProtocols(config: ValidatedConfiguration): Protocol[] {
  const protocols: Protocol[] = [];
  
  // Standing protocols always activate
  protocols.push(...this.patternLibrary.getStandingProtocols());
  
  // Conditional protocols check trigger conditions
  const conditionalProtocols = this.patternLibrary.getConditionalProtocols();
  for (const protocol of conditionalProtocols) {
    if (this.checkTriggerCondition(protocol.trigger, config)) {
      protocols.push(protocol);
    }
  }
  
  return protocols;
}
```

---

#### 4.1.3 Workflow Assembler Module

**File**: `src/main/engine/workflow-assembler.ts`

**Purpose**: Construct complete workflow instances from selected patterns.

**Public Interface**:
```typescript
export class WorkflowAssembler {
  constructor(
    private staffProfiles: StaffProfileManager
  );
  
  /**
   * Assemble a complete workflow instance
   * @param configuration Validated configuration
   * @param selection Pattern selection result
   * @returns AssemblyResult with complete workflow or errors
   */
  public assemble(
    configuration: ValidatedConfiguration,
    selection: SelectionResult
  ): Promise<AssemblyResult>;
  
  /**
   * Sequence tasks based on dependencies and timing
   * @param tasks Tasks to sequence
   * @returns Array of tasks in temporal order
   */
  public sequenceTasks(tasks: Task[]): Promise<SequencedTask[]>;
  
  /**
   * Assign tasks to appropriate staff
   * @param tasks Tasks to assign
   * @param staffProfiles Available staff profiles
   * @returns Array of task assignments
   */
  public assignTasks(
    tasks: Task[],
    staffProfiles: StaffProfile[]
  ): Promise<TaskAssignment[]>;
  
  /**
   * Organize tasks into operational phases
   * @param tasks Assigned tasks
   * @returns Array of phases
   */
  public organizeIntoPhases(tasks: AssignedTask[]): Promise<Phase[]>;
  
  /**
   * Apply protocol modifications to workflow
   * @param workflow Workflow to modify
   * @param protocols Protocols to apply
   * @returns Modified workflow
   */
  public applyProtocols(
    workflow: PartialWorkflow,
    protocols: Protocol[]
  ): Promise<ModifiedWorkflow>;
}
```

**Assembly Algorithm**:
```typescript
// Phase 1: Initialize workflow instance
private initializeWorkflow(config: ValidatedConfiguration): WorkflowInstance {
  return {
    instanceId: `copper_beech_${config.date}_daily`,
    date: config.date,
    generatedAt: new Date().toISOString(),
    generatedBy: 'copper_beech_constructor_v1.0.0',
    configurationSummary: this.buildConfigurationSummary(config),
    openingSection: { tasks: [] },
    serviceSection: { phases: [] },
    closingSection: { tasks: [] },
    adaptationProtocols: { standing: [], conditional: [] }
  };
}

// Phase 2: Assemble opening sequence
private assembleOpeningSequence(
  workflow: WorkflowInstance,
  workflowPattern: WorkflowPattern,
  staffProfiles: StaffProfile[]
): WorkflowInstance {
  const openingTasks = this.selectOpeningTasks(workflowPattern);
  const sequencedTasks = this.sequenceTasks(openingTasks);
  const assignedTasks = this.assignTasks(sequencedTasks, staffProfiles);
  
  workflow.openingSection.tasks = assignedTasks;
  workflow.openingSection.targetCompletion = '06:45';
  
  return workflow;
}

// Phase 3: Assemble service phases
private assembleServicePhases(
  workflow: WorkflowInstance,
  servicePattern: WorkflowPattern,
  staffProfiles: StaffProfile[],
  protocols: Protocol[]
): WorkflowInstance {
  const servicePhases = this.selectServicePhases(servicePattern);
  
  for (const phase of servicePhases) {
    const phaseTasks = this.selectPhaseTasks(phase);
    const assignedPhaseTasks = this.assignTasks(phaseTasks, staffProfiles);
    const phaseWithProtocols = this.applyProtocolsToPhase(assignedPhaseTasks, protocols);
    
    phase.tasks = phaseWithProtocols;
    workflow.serviceSection.phases.push(phase);
  }
  
  workflow.serviceSection.targetStart = '07:00';
  workflow.serviceSection.targetEnd = '14:00';
  
  return workflow;
}

// Phase 4: Assemble closing sequence
private assembleClosingSequence(
  workflow: WorkflowInstance,
  closingPattern: WorkflowPattern,
  staffProfiles: StaffProfile[]
): WorkflowInstance {
  const closingTasks = this.selectClosingTasks(closingPattern);
  const assignedTasks = this.assignTasks(closingTasks, staffProfiles);
  
  workflow.closingSection.tasks = assignedTasks;
  workflow.closingSection.targetCompletion = '15:00';
  
  return workflow;
}

// Phase 5: Generate documentation
private generateDocumentation(workflow: WorkflowInstance): WorkflowDocumentation {
  return {
    configurationSummary: workflow.configurationSummary,
    generationNotes: this.generateGenerationNotes(),
    constraintSatisfaction: this.getConstraintSatisfactionSummary()
  };
}
```

**Task Assignment Algorithm**:
```typescript
private assignTasksToStaff(tasks: Task[], staffProfiles: StaffProfile[]): TaskAssignment[] {
  const assignments: TaskAssignment[] = [];
  const staffWorkload: Map<string, number> = new Map();
  
  // Initialize workload tracking
  for (const profile of staffProfiles) {
    staffWorkload.set(profile.name, 0);
  }
  
  // Sort tasks by priority (dependencies first, then duration)
  const sortedTasks = this.sortTasksByPriority(tasks);
  
  for (const task of sortedTasks) {
    const bestMatch = this.findBestStaffMatch(task, staffProfiles, staffWorkload);
    
    if (bestMatch) {
      assignments.push({
        taskId: task.id,
        taskName: task.name,
        assignedTo: bestMatch.profile.name,
        roleRequired: task.assignedRoles[0],
        assignedAt: new Date().toISOString(),
        assignmentRationale: this.generateAssignmentRationale(task, bestMatch)
      });
      
      // Update workload
      staffWorkload.set(
        bestMatch.profile.name,
        staffWorkload.get(bestMatch.profile.name)! + task.duration
      );
    }
  }
  
  return assignments;
}

private findBestStaffMatch(
  task: Task,
  staffProfiles: StaffProfile[],
  workload: Map<string, number>
): StaffMatch | null {
  const matches: StaffMatch[] = [];
  
  for (const profile of staffProfiles) {
    // Check if profile has required role
    if (!task.assignedRoles.includes(profile.role)) {
      continue;
    }
    
    // Check if profile has required certifications
    if (!this.hasRequiredCertifications(task, profile)) {
      continue;
    }
    
    // Calculate match score
    const score = this.calculateMatchScore(task, profile, workload);
    
    matches.push({
      profile,
      score,
      reasons: this.generateMatchReasons(task, profile),
      issues: this.identifyPotentialIssues(task, profile)
    });
  }
  
  // Sort by score and return best match
  matches.sort((a, b) => b.score - a.score);
  return matches.length > 0 ? matches[0] : null;
}
```

---

#### 4.1.4 Constraint Verifier Module

**File**: `src/main/engine/constraint-verifier.ts`

**Purpose**: Ensure that assembled workflows satisfy all hard constraints and optimize toward soft constraint targets.

**Public Interface**:
```typescript
export class ConstraintVerifier {
  constructor(
    private constraintDefinitions: ConstraintDefinition[]
  );
  
  /**
   * Verify all constraints against a workflow
   * @param workflow Workflow instance to verify
   * @returns VerificationResult with constraint status
   */
  public verify(workflow: WorkflowInstance): Promise<VerificationResult>;
  
  /**
   * Check a specific hard constraint
   * @param workflow Workflow to check
   * @param constraintId Constraint ID (HC_001-HC_004)
   * @returns Constraint check result
   */
  public checkHardConstraint(
    workflow: WorkflowInstance,
    constraintId: HardConstraintId
  ): Promise<HardConstraintResult>;
  
  /**
   * Evaluate soft constraint satisfaction
   * @param workflow Workflow to evaluate
   * @returns Array of soft constraint evaluations
   */
  public evaluateSoftConstraints(
    workflow: WorkflowInstance
  ): Promise<SoftConstraintEvaluation[]>;
  
  /**
   * Determine if workflow is approved or rejected
   * @param verification Verification result
   * @returns Approval decision
   */
  public determineApproval(verification: VerificationResult): ApprovalDecision;
}
```

**Constraint Verification Implementation**:

```typescript
// HC_001: Food Safety Temperature Control
private verifyHC_001(workflow: WorkflowInstance): HardConstraintResult {
  const violations: ConstraintViolation[] = [];
  const checkedElements: CheckedElement[] = [];
  
  // Check all tasks that handle temperature-sensitive items
  const temperatureTasks = workflow.openingSection.tasks
    .concat(...workflow.serviceSection.phases.map(p => p.tasks))
    .filter(task => task.inputs.some(input => this.isTemperatureSensitive(input)));
  
  for (const task of temperatureTasks) {
    const tempCheck = this.checkTemperatureCompliance(task);
    checkedElements.push({
      elementId: task.taskId,
      elementType: 'task',
      checkedAt: new Date(),
      result: tempCheck.compliant ? 'pass' : 'fail'
    });
    
    if (!tempCheck.compliant) {
      violations.push({
        element: task.taskId,
        description: tempCheck.reason,
        severity: 'critical',
        remediation: tempCheck.remediation
      });
    }
  }
  
  return {
    constraintId: 'HC_001',
    status: violations.length === 0 ? 'satisfied' : 'violated',
    details: violations.length === 0 
      ? 'All temperature-sensitive items comply with danger zone limits'
      : `${violations.length} temperature compliance violations found`,
    checkedElements,
    violations
  };
}

// HC_002: Cross-Contamination Prevention
private verifyHC_002(workflow: WorkflowInstance): HardConstraintResult {
  const violations: ConstraintViolation[] = [];
  const checkedElements: CheckedElement[] = [];
  
  // Verify color-coded board assignments
  const boardAssignments = this.getBoardAssignments(workflow);
  for (const assignment of boardAssignments) {
    if (!this.isValidBoardAssignment(assignment)) {
      violations.push({
        element: assignment.taskId,
        description: `Cross-contamination risk: ${assignment.taskName} uses ${assignment.board} board for ${assignment.allergenFlags.join(', ')} items`,
        severity: 'critical',
        remediation: 'Reassign to appropriate color board'
      });
    }
  }
  
  // Verify allergen isolation capability
  const allergenCapability = this.checkAllergenIsolationCapability(workflow);
  if (!allergenCapability.available) {
    violations.push({
      element: 'allergen_station',
      description: 'Allergen isolation equipment not available',
      severity: 'critical',
      remediation: 'Ensure dedicated utensils and separate plating area are available'
    });
  }
  
  return {
    constraintId: 'HC_002',
    status: violations.length === 0 ? 'satisfied' : 'violated',
    details: violations.length === 0 
      ? 'All cross-contamination prevention measures verified'
      : `${violations.length} cross-contamination risks identified`,
    checkedElements,
    violations
  };
}

// HC_003: Minimum Staffing Levels
private verifyHC_003(workflow: WorkflowInstance): HardConstraintResult {
  const violations: ConstraintViolation[] = [];
  
  // Check all service phases for minimum staffing
  for (const phase of workflow.serviceSection.phases) {
    const assignedStaff = new Set(phase.tasks.map(t => t.assignedTo));
    if (assignedStaff.size < 3) {
      violations.push({
        element: phase.phaseId,
        description: `Phase ${phase.name} has only ${assignedStaff.size} staff (minimum 3 required)`,
        severity: 'critical',
        remediation: 'Add additional staff coverage or reduce service scope'
      });
    }
  }
  
  return {
    constraintId: 'HC_003',
    status: violations.length === 0 ? 'satisfied' : 'violated',
    details: violations.length === 0 
      ? 'All phases meet minimum staffing requirements'
      : `${violations.length} phases below minimum staffing`,
    checkedElements: [],
    violations
  };
}

// HC_004: Time-Temperature Combinations
private verifyHC_004(workflow: WorkflowInstance): HardConstraintResult {
  const violations: ConstraintViolation[] = [];
  
  // Check all prep tasks for 4-hour maximum
  const prepTasks = workflow.openingSection.tasks.filter(
    task => task.patternReference?.startsWith('TP_')
  );
  
  for (const task of prepTasks) {
    // Calculate total time from prep start to service use
    const totalTime = this.calculatePrepToServiceTime(task, workflow);
    if (totalTime > 240) { // 4 hours in minutes
      violations.push({
        element: task.taskId,
        description: `${task.name} exceeds 4-hour prep maximum (${totalTime} minutes)`,
        severity: 'critical',
        remediation: 'Adjust prep timing or implement batch refresh'
      });
    }
  }
  
  return {
    constraintId: 'HC_004',
    status: violations.length === 0 ? 'satisfied' : 'violated',
    details: violations.length === 0 
      ? 'All prep items within 4-hour time-temperature maximum'
      : `${violations.length} prep items exceed 4-hour limit`,
    checkedElements: [],
    violations
  };
}
```

---

### 4.2 Knowledge Layer Module Specifications

#### 4.2.1 Pattern Library Manager

**File**: `src/main/knowledge/pattern-library.ts`

**Purpose**: Manage the persistent storage and retrieval of patterns.

**Public Interface**:
```typescript
export class PatternLibraryManager {
  constructor(private dataPath: string);
  
  /**
   * Load all patterns from disk
   */
  public loadLibrary(): Promise<PatternLibrary>;
  
  /**
   * Get task patterns matching criteria
   */
  public getTaskPatterns(criteria?: TaskPatternCriteria): TaskPattern[];
  
  /**
   * Get workflow patterns matching criteria
   */
  public getWorkflowPatterns(criteria?: WorkflowPatternCriteria): WorkflowPattern[];
  
  /**
   * Get specific pattern by ID
   */
  public getPattern(type: PatternType, id: string): Pattern | null;
  
  /**
   * Get standing protocols
   */
  public getStandingProtocols(): Protocol[];
  
  /**
   * Get conditional protocols
   */
  public getConditionalProtocols(): Protocol[];
  
  /**
   * Update a pattern
   */
  public updatePattern(pattern: Pattern, changeId: string): Promise<UpdateResult>;
  
  /**
   * Get pattern version history
   */
  public getPatternHistory(type: PatternType, id: string): Promise<PatternVersion[]>;
}
```

**Data Files**:

```typescript
// data/pattern_library/task_patterns.json structure
interface TaskPatternsFile {
  version: string;
  last_modified: string;
  patterns: TaskPattern[];
}

// Example entry
{
  "id": "TP_001",
  "version": 1,
  "name": "Standard Egg Prep",
  "duration": 15,
  "assigned_roles": ["prep_cook"],
  "inputs": ["eggs", "butter", "seasoning"],
  "outputs": ["prepped_eggs"],
  "dependencies": [],
  "color_board": "green",
  "allergen_flags": [],
  "category": "prep",
  "created": "2024-01-15",
  "modified": "2024-01-15"
}
```

```typescript
// data/pattern_library/workflow_patterns.json structure
interface WorkflowPatternsFile {
  version: string;
  last_modified: string;
  patterns: WorkflowPattern[];
}

// Example entry
{
  "id": "WP_001",
  "version": 1,
  "name": "Standard Opening Sequence",
  "type": "opening",
  "task_sequence": [
    {"task_id": "TP_XXX", "sequence_order": 1, "start_time": "5:30"},
    {"task_id": "TP_YYY", "sequence_order": 2, "start_time": "5:45"}
  ],
  "phases": ["preheat", "inventory", "production", "setup", "final"],
  "applicable_volume_tiers": ["low", "medium", "high"],
  "applicable_day_types": ["weekday", "weekend"],
  "created": "2024-01-15",
  "modified": "2024-01-15"
}
```

```typescript
// data/pattern_library/constraints.json structure
interface ConstraintsFile {
  version: string;
  hard: HardConstraint[];
  soft: SoftConstraint[];
}

// Example hard constraint
{
  "id": "HC_001",
  "name": "Food Safety Temperature Control",
  "definition": "Food must not remain in danger zone (40°F-140°F) for more than 2 hours cumulative",
  "enforcement": "invariant",
  "verification_method": "time_temperature_tracking",
  "parameters": {
    "danger_zone_max": 120,
    "danger_zone_temp_low": 40,
    "danger_zone_temp_high": 140
  }
}
```

```typescript
// data/pattern_library/protocols.json structure
interface ProtocolsFile {
  version: string;
  protocols: Protocol[];
}

// Example protocol
{
  "id": "AP_001",
  "version": 1,
  "name": "High Volume Response",
  "trigger": {
    "type": "threshold",
    "condition": "tickets_in_queue > 8",
    "metric": "queue_depth",
    "operator": ">",
    "value": 8
  },
  "response_actions": [
    {
      "type": "reassign",
      "from": "James",
      "to": "Maria",
      "task_category": "griddle"
    },
    {
      "type": "accelerate",
      "phase": "peak_service",
      "factor": 1.2
    }
  ],
  "standing": false,
  "created": "2024-01-15",
  "modified": "2024-01-15"
}
```

---

#### 4.2.2 Staff Profile Manager

**File**: `src/main/knowledge/staff-profiles.ts`

**Purpose**: