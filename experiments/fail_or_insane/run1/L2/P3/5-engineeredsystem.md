# The Copper Beech Daily Workflow Constructor: Engineered System

## L2P3W[2](5) — Engineered System Pass 1: Build, Implement, and Deploy the Copper Beech Constructor

---

## 1. Introduction: From Specification to Concrete Instance

The prior passes have established what the Copper Beech Daily Workflow Constructor IS (abstract goal), how it is designed (systems design), what internal structures it exhibits (systems architecture), what vocabulary describes it (DSL), and how its components connect (topology). This document completes the investigation by presenting the **complete concrete implementation**—what a fully realized, deployable instance of the Copper Beech Constructor looks like when built according to the specifications.

The question we address is: **what does it look like when we open the box and examine the actual implementation?** What code structures implement the abstract concepts? What data formats encode the patterns? What deployment configurations enable operation? What does it mean when the Copper Beech Constructor actually runs and produces a daily workflow for January 16, 2024?

This document provides the concrete manifestation of the abstract principles, grounding the Copper Beech-specific generation system in tangible implementation artifacts ready for deployment in Copper Beech Cafe's operations.

---

## 2. Implementation Architecture: Core Component Realization

### 2.1 System Architecture Overview

The Copper Beech Daily Workflow Constructor is implemented as a desktop application with cloud synchronization, designed for the specific context of a small commercial kitchen where Chef Maria needs reliable, simple operation without complex infrastructure.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COPPER BEECH CONSTRUCTOR: IMPLEMENTATION ARCHITECTURE       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    USER INTERFACE LAYER                                │   │
│  │  Implementation: Desktop Application (Electron + React)               │   │
│  │  Purpose: Chef Maria's daily interaction interface                    │   │
│  │  ┌─────────────────────────────────────────────────────────────┐   │   │
│  │  │ Components:                                                    │   │   │
│  │  │ ├── Configuration Input Form                                  │   │   │
│  │  │ ├── Daily Workflow Display                                   │   │   │
│  │  │ ├── Post-Service Review Form                                 │   │   │
│  │  │ ├── Feedback Submission Interface                            │   │   │
│  │  │ └── Learning Dashboard (monthly view)                        │   │   │
│  │  └─────────────────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    │ IPC                                    │
│                                    ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    GENERATION ENGINE LAYER                             │   │
│  │  Implementation: Node.js Application                                 │   │
│  │  Purpose: Core workflow generation logic                             │   │
│  │  ┌─────────────────────────────────────────────────────────────┐   │   │
│  │  │ Core Services:                                                │   │   │
│  │  │ ├── ConfigurationParser (validates daily inputs)             │   │   │
│  │  │ ├── PatternSelector (selects tasks from library)             │   │   │
│  │  │ ├── WorkflowAssembler (composes task sequences)               │   │   │
│  │  │ ├── ConstraintValidator (verifies food safety)                │   │   │
│  │  │ └── DocumentationGenerator (creates readable output)          │   │   │
│  │  └─────────────────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    │ File System                           │
│                                    ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    DATA STORAGE LAYER                                 │   │
│  │  Implementation: Local JSON files + SQLite for metrics               │   │
│  │  Purpose: Pattern library, historical workflows, feedback             │   │
│  │  ┌─────────────────────────────────────────────────────────────┐   │   │
│  │  │ Data Stores:                                                  │   │   │
│  │  │ ├── pattern_library.json (47 task patterns, 12 workflows)    │   │   │
│  │  │ ├── constraint_definitions.json (hard + soft constraints)   │   │   │
│  │  │ ├── adaptation_protocols.json (8 protocols)                 │   │   │
│  │  │ ├── menu_knowledge.json (23 breakfast, 8 lunch items)      │   │   │
│  │  │ ├── staff_profiles.json (roles, capabilities, learning)    │   │   │
│  │  │ ├── historical_workflows/ (past workflow instances)        │   │   │
│  │  │ ├── feedback_archive.db (SQLite - feedback records)        │   │   │
│  │  │ └── metrics_warehouse.db (SQLite - execution metrics)       │   │   │
│  │  └─────────────────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    │ Optional Sync                         │
│                                    ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    CLOUD SYNC LAYER (Optional)                        │   │
│  │  Implementation: Cloudflare D1 (SQLite) + R2                       │   │
│  │  Purpose: Backup, multi-device access, aggregate learning            │   │
│  │  ┌─────────────────────────────────────────────────────────────┐   │   │
│  │  │ Sync Components:                                              │   │   │
│  │  │ ├── Pattern Library Sync                                     │   │   │
│  │  │ ├── Feedback Aggregation (for learning)                      │   │   │
│  │  │ └── Workflow Archive                                         │   │   │
│  │  └─────────────────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Technology Stack

The Copper Beech Constructor uses a pragmatic technology stack optimized for small kitchen deployment:

```yaml
# Copper Beech Constructor Technology Stack

desktop_application:
  framework: Electron 28+
  frontend: React 18 + TypeScript 5.2
  state_management: Zustand 4.4
  styling: Tailwind CSS 3.4
  deployment: Electron Builder (Windows, macOS)

generation_engine:
  runtime: Node.js 20 LTS
  language: TypeScript 5.2
  data_processing: Native JSON processing
  validation: Zod 3.22 (schema validation)

data_storage:
  local_files: Native fs module (JSON files)
  metrics: better-sqlite3 9.0
  pattern_storage: Structured JSON with versioning

cloud_services:
  database: Cloudflare D1 (SQLite at edge)
  storage: Cloudflare R2 (workflow archives)
  sync: Custom sync protocol with conflict resolution

printing:
  pdf_generation: Electron print API
  document_format: Print-ready PDF with formatting

testing:
  unit: Vitest 1.0
  integration: Playwright 1.40
  smoke_testing: Chef Maria's test suite (manual)
```

### 2.3 Core Data Structures

The implementation operates on well-defined data structures:

**2.3.1 Daily Configuration Schema**

```typescript
// configuration.ts

interface DailyConfiguration {
  // Required fields
  date: string;                    // ISO date: "2024-01-16"
  dayOfWeek: DayOfWeek;            // "Monday" | "Tuesday" | ...
  expectedVolume: VolumeExpectation;
  staffConfiguration: StaffConfiguration;
  
  // Optional fields
  weather?: WeatherCondition;      // "cold" | "hot" | "rainy" | "clear"
  specialEvents?: SpecialEvent[];
  inventoryNotes?: InventoryNote[];
  equipmentStatus?: EquipmentStatus[];
  notes?: string;
}

interface VolumeExpectation {
  breakfastTickets: { min: number; max: number };
  lunchTickets: { min: number; max: number };
  volumeTier: "low" | "medium" | "high" | "extreme";
}

interface StaffConfiguration {
  scheduled: ScheduledStaff[];
  expectedChanges: StaffChange[];
}

interface ScheduledStaff {
  name: StaffName;
  role: StaffRole;
  startTime: string;              // "05:30", "06:00", etc.
  certifications?: string[];
  strengths?: string[];
}

// Validation schema using Zod
const DailyConfigurationSchema = z.object({
  date: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
  dayOfWeek: z.enum(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]),
  expectedVolume: z.object({
    breakfastTickets: z.object({
      min: z.number().min(0).max(100),
      max: z.number().min(0).max(100)
    }).refine(data => data.min <= data.max, {
      message: "Min must be <= max"
    }),
    lunchTickets: z.object({
      min: z.number().min(0).max(100),
      max: z.number().min(0).max(100)
    }).refine(data => data.min <= data.max, {
      message: "Min must be <= max"
    }),
    volumeTier: z.enum(["low", "medium", "high", "extreme"])
  }),
  staffConfiguration: z.object({
    scheduled: z.array(z.object({
      name: z.enum(["Maria", "James", "Elena", "Marcus"]),
      role: z.enum(["chef", "line_cook", "prep_cook", "support"]),
      startTime: z.string().regex(/^\d{2}:\d{2}$/),
      certifications: z.array(z.string()).optional(),
      strengths: z.array(z.string()).optional()
    })).min(3, "Minimum 3 staff required for service"),
    expectedChanges: z.array(z.object({
      name: z.string(),
      type: z.enum(["late", "absent", "early_departure"]),
      time: z.string().optional()
    })).optional()
  }),
  weather: z.enum(["cold", "hot", "rainy", "clear"]).optional(),
  specialEvents: z.array(z.object({
    type: z.enum(["reservation", "event", "party"]),
    time: z.string(),
    description: z.string(),
    headcount: z.number().optional()
  })).optional(),
  inventoryNotes: z.array(z.object({
    item: z.string(),
    status: z.enum(["low", "out", "substitute_available", "delivery_delayed"]),
    notes: z.string().optional()
  })).optional(),
  equipmentStatus: z.array(z.object({
    equipment: z.string(),
    status: z.enum(["operational", "maintenance", "unavailable"]),
    notes: z.string().optional()
  })).optional(),
  notes: z.string().optional()
});
```

**2.3.2 Task Pattern Schema**

```typescript
// patterns.ts

interface TaskPattern {
  patternId: PatternId;           // "TP_001", "TP_002", etc.
  name: string;
  category: TaskCategory;
  durationMinutes: number;
  forMenuItems?: string[];         // Which menu items this prep supports
  sequence: TaskStep[];
  staffAssignment: StaffRole;       // Primary role assignment
  dependencies?: PatternId[];       // Tasks that must complete first
  variations?: string[];           // Named variations
}

interface TaskStep {
  step: string;                    // "pull_eggs", "crack_eggs", etc.
  description: string;
  verification?: string;            // "temp_check < 45°F"
  quantity?: string;               // "3 dozen for typical day"
  storage?: string;                // "refrigerated until service"
}

interface WorkflowPattern {
  patternId: WorkflowPatternId;     // "WP_001", "WP_002", etc.
  name: string;
  targetCompletion: string;        // "06:45" for opening
  phases: WorkflowPhase[];
}

interface WorkflowPhase {
  phaseId: string;
  name: string;
  startTime: string;
  durationMinutes: number;
  tasks: PhaseTask[];
}

interface PhaseTask {
  sequence: number;
  task: PatternId | string;       // Pattern ID or inline task
  assigned: StaffRole | StaffName;
  durationMinutes?: number;
  dependencies?: string[];
  details?: string;
}
```

**2.3.3 Daily Workflow Instance Schema**

```typescript
// workflow-instance.ts

interface DailyWorkflowInstance {
  instanceId: InstanceId;
  date: string;
  generatedAt: string;             // ISO timestamp
  generatedBy: string;             // Constructor version
  
  configurationSummary: ConfigurationSummary;
  
  openingSection: OpeningSection;
  serviceSection: ServiceSection;
  closingSection: ClosingSection;
  
  executionLogTemplate: ExecutionLogTemplate;
}

interface ConfigurationSummary {
  expectedVolume: string;
  staffCount: number;
  weather?: string;
  specialEvents?: string[];
  keyNotes?: string[];
}

interface OpeningSection {
  targetCompletion: string;
  tasks: OpeningTask[];
}

interface OpeningTask {
  sequenceNumber: number;
  taskId: string;
  name: string;
  assigned: string;
  startTime: string;
  durationMinutes: number;
  status: "pending" | "in_progress" | "completed" | "skipped";
  dependencies?: string[];
  details?: string;
}

interface ServiceSection {
  targetStart: string;
  targetEnd: string;
  phases: ServicePhase[];
  adaptationTriggers: AdaptationTrigger[];
}

interface ServicePhase {
  phaseId: string;
  name: string;
  timeWindow: string;
  expectedVolume: string;
  staffing: string;
  protocols: string[];
  specialNotes?: string;
}

interface AdaptationTrigger {
  name: string;
  condition: string;
  responseProtocol: string;
}

interface ClosingSection {
  targetCompletion: string;
  tasks: ClosingTask[];
}

interface ClosingTask {
  sequenceNumber: number;
  taskId: string;
  name: string;
  assigned: string;
  startTime: string;
  durationMinutes: number;
  status: "pending" | "in_progress" | "completed" | "skipped";
}

interface ExecutionLogTemplate {
  metricsToCapture: string[];
  captureMethod: string;
  submitTo: string;
}
```

**2.3.4 Constraint Definition Schema**

```typescript
// constraints.ts

interface HardConstraint {
  constraintId: ConstraintId;      // "HC_001", etc.
  name: string;
  definition: string;
  enforcement: "generation_blocks_violation";
  copperBeechApplication: string[];
  validator: ConstraintValidator;
}

interface SoftConstraint {
  constraintId: ConstraintId;
  name: string;
  definition: string;
  optimizationTarget: string;
  weight: number;                  // 0-1
  validator: ConstraintValidator;
}

type ConstraintValidator = (
  workflow: DailyWorkflowInstance,
  configuration: DailyConfiguration
) => ConstraintViolation[];

interface ConstraintViolation {
  constraintId: string;
  severity: "error" | "warning";
  message: string;
  affectedTasks?: string[];
}
```

---

## 3. Core Implementation Components

### 3.1 Configuration Parser Implementation

```typescript
// services/configuration-parser.ts

import { z } from "zod";
import { DailyConfiguration, DailyConfigurationSchema } from "../types/configuration";
import { DEFAULT_CONFIGURATION } from "../defaults";

export class ConfigurationParser {
  
  /**
   * Parse and validate daily configuration input
   */
  parse(rawInput: unknown): ParseResult {
    // Step 1: Schema validation
    const schemaResult = DailyConfigurationSchema.safeParse(rawInput);
    
    if (!schemaResult.success) {
      return {
        success: false,
        errors: this.formatZodErrors(schemaResult.error),
        configuration: null
      };
    }
    
    // Step 2: Business logic validation
    const config = schemaResult.data;
    const businessErrors = this.validateBusinessLogic(config);
    
    if (businessErrors.length > 0) {
      return {
        success: false,
        errors: businessErrors,
        configuration: null
      };
    }
    
    // Step 3: Apply defaults for optional fields
    const completeConfig = this.applyDefaults(config);
    
    // Step 4: Calculate derived values
    const enrichedConfig = this.enrichConfiguration(completeConfig);
    
    return {
      success: true,
      errors: [],
      configuration: enrichedConfig
    };
  }
  
  private validateBusinessLogic(config: DailyConfiguration): ValidationError[] {
    const errors: ValidationError[] = [];
    
    // Validate staffing minimums
    const chefCount = config.staffConfiguration.scheduled
      .filter(s => s.role === "chef").length;
    if (chefCount < 1) {
      errors.push({
        field: "staffConfiguration.scheduled",
        message: "At least one chef is required for service"
      });
    }
    
    // Validate service start time staffing
    const staffBy6AM = config.staffConfiguration.scheduled
      .filter(s => s.startTime <= "06:00").length;
    if (staffBy6AM < 2) {
      errors.push({
        field: "staffConfiguration.scheduled",
        message: "At least 2 staff needed by 6 AM for opening prep"
      });
    }
    
    // Validate service start staffing
    const staffBy7AM = config.staffConfiguration.scheduled
      .filter(s => s.startTime <= "07:00").length;
    if (staffBy7AM < 3) {
      errors.push({
        field: "staffConfiguration.scheduled",
        message: "Service requires minimum 3 staff by 7 AM"
      });
    }
    
    return errors;
  }
  
  private applyDefaults(config: DailyConfiguration): DailyConfiguration {
    return {
      ...config,
      weather: config.weather ?? "clear",
      specialEvents: config.specialEvents ?? [],
      inventoryNotes: config.inventoryNotes ?? [],
      equipmentStatus: config.equipmentStatus ?? [],
      notes: config.notes ?? ""
    };
  }
  
  private enrichConfiguration(config: DailyConfiguration): DailyConfiguration {
    // Calculate volume tier if not provided
    const totalExpected = config.expectedVolume.breakfastTickets.max + 
                         config.expectedVolume.lunchTickets.max;
    
    let volumeTier = config.expectedVolume.volumeTier;
    if (!volumeTier) {
      if (totalExpected < 40) volumeTier = "low";
      else if (totalExpected < 60) volumeTier = "medium";
      else if (totalExpected < 80) volumeTier = "high";
      else volumeTier = "extreme";
    }
    
    // Determine which adaptation protocols to arm
    const protocolsArmed: string[] = [];
    
    if (volumeTier === "high" || volumeTier === "extreme") {
      protocolsArmed.push("AP_001"); // High volume response
    }
    
    if (config.staffConfiguration.expectedChanges?.length ?? 0 > 0) {
      protocolsArmed.push("AP_003"); // Staff shortage response
    }
    
    if (config.specialEvents?.some(e => e.type === "party" && e.headcount ?? 0 > 8)) {
      protocolsArmed.push("AP_004"); // Large party response
    }
    
    return {
      ...config,
      expectedVolume: {
        ...config.expectedVolume,
        volumeTier
      },
      _meta: {
        protocolsArmed,
        generatedAt: new Date().toISOString(),
        version: "1.0.0"
      }
    };
  }
  
  private formatZodErrors(error: z.ZodError): ValidationError[] {
    return error.errors.map(err => ({
      field: err.path.join("."),
      message: err.message
    }));
  }
}

interface ParseResult {
  success: boolean;
  errors: ValidationError[];
  configuration: DailyConfiguration | null;
}

interface ValidationError {
  field: string;
  message: string;
}
```

### 3.2 Pattern Selector Implementation

```typescript
// services/pattern-selector.ts

import { 
  TaskPattern, 
  WorkflowPattern, 
  AdaptationProtocol 
} from "../types/patterns";
import { DailyConfiguration } from "../types/configuration";

export class PatternSelector {
  private taskPatterns: Map<string, TaskPattern>;
  private workflowPatterns: Map<string, WorkflowPattern>;
  private adaptationProtocols: Map<string, AdaptationProtocol>;
  
  constructor(
    taskPatterns: TaskPattern[],
    workflowPatterns: WorkflowPattern[],
    adaptationProtocols: AdaptationProtocol[]
  ) {
    this.taskPatterns = new Map(taskPatterns.map(p => [p.patternId, p]));
    this.workflowPatterns = new Map(workflowPatterns.map(p => [p.patternId, p]));
    this.adaptationProtocols = new Map(adaptationProtocols.map(p => [p.protocolId, p]));
  }
  
  /**
   * Select appropriate patterns based on configuration
   */
  selectPatterns(config: DailyConfiguration): SelectedPatterns {
    // Select opening workflow pattern
    const openingPattern = this.selectOpeningPattern(config);
    
    // Select task patterns for opening
    const openingTasks = this.selectOpeningTasks(config, openingPattern);
    
    // Select service phases based on volume
    const servicePhases = this.selectServicePhases(config);
    
    // Select closing workflow pattern
    const closingPattern = this.selectClosingPattern(config);
    
    // Select closing tasks
    const closingTasks = this.selectClosingTasks(config, closingPattern);
    
    // Select adaptation protocols based on context
    const protocols = this.selectAdaptationProtocols(config);
    
    return {
      openingPattern,
      openingTasks,
      servicePhases,
      closingPattern,
      closingTasks,
      protocols
    };
  }
  
  private selectOpeningPattern(config: DailyConfiguration): WorkflowPattern {
    // Base pattern for all days
    const basePattern = this.workflowPatterns.get("WP_001");
    if (!basePattern) {
      throw new Error("Opening workflow pattern WP_001 not found");
    }
    
    // Could extend with day-specific patterns in future
    return basePattern;
  }
  
  private selectOpeningTasks(
    config: DailyConfiguration,
    _pattern: WorkflowPattern
  ): TaskPattern[] {
    const tasks: TaskPattern[] = [];
    
    // Equipment preheat - always needed
    const equipPreheat = this.taskPatterns.get("TP_000");
    if (equipPreheat) tasks.push(equipPreheat);
    
    // Inventory check - always needed
    const inventoryCheck = this.taskPatterns.get("TP_000b");
    if (inventoryCheck) tasks.push(inventoryCheck);
    
    // Production prep based on menu and inventory
    const eggPrep = this.taskPatterns.get("TP_001");
    if (eggPrep) tasks.push(eggPrep);
    
    const baconPrep = this.taskPatterns.get("TP_002");
    if (baconPrep) tasks.push(baconPrep);
    
    // Check for produce delivery delay
    const hasProduceDelay = config.inventoryNotes?.some(
      n => n.item.toLowerCase().includes("produce") && 
           n.status === "delivery_delayed"
    );
    
    if (!hasProduceDelay) {
      const producePrep = this.taskPatterns.get("TP_003");
      if (producePrep) tasks.push(producePrep);
    } else {
      // Use canned tomatoes alternative
      const producePrepAlt = this.taskPatterns.get("TP_003_alt");
      if (producePrepAlt) tasks.push(producePrepAlt);
    }
    
    const hashBrownPrep = this.taskPatterns.get("TP_004");
    if (hashBrownPrep) tasks.push(hashBrownPrep);
    
    // Hollandaise base - needed for Benedict
    const hollandaiseBase = this.taskPatterns.get("TP_005");
    if (hollandaiseBase) tasks.push(hollandaiseBase);
    
    // Station setup - always needed
    const stationSetup = this.taskPatterns.get("TP_006");
    if (stationSetup) tasks.push(stationSetup);
    
    return tasks;
  }
  
  private selectServicePhases(config: DailyConfiguration): ServicePhaseConfig[] {
    const phases: ServicePhaseConfig[] = [];
    
    // Early service phase
    phases.push({
      phaseId: "early_service",
      name: "Early Service",
      timeWindow: { start: "07:00", end: "09:00" },
      expectedTickets: Math.round(
        config.expectedVolume.breakfastTickets.max * 0.25
      ),
      protocols: ["STANDARD_SERVICE", "ALLERGEN_VERIFICATION"]
    });
    
    // Peak service phase
    const peakVolume = config.expectedVolume.volumeTier === "high" || 
                       config.expectedVolume.volumeTier === "extreme";
    
    phases.push({
      phaseId: "peak_service",
      name: "Peak Service",
      timeWindow: { start: "09:00", end: "11:30" },
      expectedTickets: Math.round(
        config.expectedVolume.breakfastTickets.max * 0.55
      ),
      protocols: peakVolume 
        ? ["STANDARD_SERVICE", "HIGH_VOLUME_MONITORING", "QUEUE_THRESHOLD_8"]
        : ["STANDARD_SERVICE", "HIGH_VOLUME_MONITORING"]
    });
    
    // Lunch transition
    const hasLargeParty = config.specialEvents?.some(
      e => e.type === "party" && (e.headcount ?? 0) >= 10
    );
    
    phases.push({
      phaseId: "lunch_transition",
      name: "Lunch Transition",
      timeWindow: { start: "11:30", end: "12:00" },
      expectedTickets: Math.round(
        config.expectedVolume.lunchTickets.max * 0.3
      ),
      protocols: ["LUNCH_SERVICE_PROTOCOL"],
      specialNotes: hasLargeParty 
        ? `Large party (${config.specialEvents?.find(e => e.type === "party")?.headcount ?? "?"}) expected at 11:30`
        : undefined
    });
    
    // Lunch service
    phases.push({
      phaseId: "lunch_service",
      name: "Lunch Service",
      timeWindow: { start: "12:00", end: "14:00" },
      expectedTickets: Math.round(
        config.expectedVolume.lunchTickets.max * 0.7
      ),
      protocols: ["LUNCH_SERVICE_PROTOCOL", "WIND_DOWN_AWARENESS"]
    });
    
    return phases;
  }
  
  private selectClosingPattern(config: DailyConfiguration): WorkflowPattern {
    return this.workflowPatterns.get("WP_003") ?? 
           this.workflowPatterns.get("WP_003_base")!;
  }
  
  private selectClosingTasks(
    config: DailyConfiguration,
    _pattern: WorkflowPattern
  ): TaskPattern[] {
    const tasks: TaskPattern[] = [];
    
    // Station breakdown
    const stationBreakdown = this.taskPatterns.get("CT_001");
    if (stationBreakdown) tasks.push(stationBreakdown);
    
    // Kitchen cleaning
    const kitchenCleaning = this.taskPatterns.get("CT_002");
    if (kitchenCleaning) tasks.push(kitchenCleaning);
    
    // Documentation
    const documentation = this.taskPatterns.get("CT_003");
    if (documentation) tasks.push(documentation);
    
    return tasks;
  }
  
  private selectAdaptationProtocols(config: DailyConfiguration): AdaptationProtocol[] {
    const protocols: AdaptationProtocol[] = [];
    
    // High volume response if armed
    if (config._meta?.protocolsArmed?.includes("AP_001")) {
      const ap001 = this.adaptationProtocols.get("AP_001");
      if (ap001) protocols.push(ap001);
    }
    
    // Equipment failure - always standing
    const ap002 = this.adaptationProtocols.get("AP_002");
    if (ap002) protocols.push(ap002);
    
    // Staff shortage if expected changes
    if (config._meta?.protocolsArmed?.includes("AP_003")) {
      const ap003 = this.adaptationProtocols.get("AP_003");
      if (ap003) protocols.push(ap003);
    }
    
    // Large party response
    if (config._meta?.protocolsArmed?.includes("AP_004")) {
      const ap004 = this.adaptationProtocols.get("AP_004");
      if (ap004) protocols.push(ap004);
    }
    
    // Allergen alert - always standing
    const ap005 = this.adaptationProtocols.get("AP_005");
    if (ap005) protocols.push(ap005);
    
    return protocols;
  }
}

interface SelectedPatterns {
  openingPattern: WorkflowPattern;
  openingTasks: TaskPattern[];
  servicePhases: ServicePhaseConfig[];
  closingPattern: WorkflowPattern;
  closingTasks: TaskPattern[];
  protocols: AdaptationProtocol[];
}

interface ServicePhaseConfig {
  phaseId: string;
  name: string;
  timeWindow: { start: string; end: string };
  expectedTickets: number;
  protocols: string[];
  specialNotes?: string;
}
```

### 3.3 Workflow Assembler Implementation

```typescript
// services/workflow-assembler.ts

import { DailyWorkflowInstance, OpeningSection, ServiceSection, ClosingSection } from "../types/workflow-instance";
import { DailyConfiguration } from "../types/configuration";
import { TaskPattern, WorkflowPattern, AdaptationProtocol } from "../types/patterns";
import { SelectedPatterns } from "./pattern-selector";

export class WorkflowAssembler {
  
  /**
   * Assemble complete workflow instance from selected patterns
   */
  assemble(
    config: DailyConfiguration,
    patterns: SelectedPatterns
  ): DailyWorkflowInstance {
    
    const instanceId = `copper_beech_${config.date.replace(/-/g, "")}_daily`;
    
    // Assemble opening section
    const openingSection = this.assembleOpeningSection(
      patterns.openingPattern,
      patterns.openingTasks,
      config
    );
    
    // Assemble service section
    const serviceSection = this.assembleServiceSection(
      patterns.servicePhases,
      patterns.protocols,
      config
    );
    
    // Assemble closing section
    const closingSection = this.assembleClosingSection(
      patterns.closingPattern,
      patterns.closingTasks,
      config
    );
    
    // Build configuration summary
    const configurationSummary = this.buildConfigurationSummary(config);
    
    return {
      instanceId,
      date: config.date,
      generatedAt: new Date().toISOString(),
      generatedBy: "copper_beech_constructor_v1.0.0",
      
      configurationSummary,
      
      openingSection,
      serviceSection,
      closingSection,
      
      executionLogTemplate: {
        metricsToCapture: [
          "ticket_times",
          "sla_compliance",
          "adaptation_activations",
          "deviations",
          "waste_records"
        ],
        captureMethod: "post_service_form",
        submitTo: "feedback_interface"
      }
    };
  }
  
  private assembleOpeningSection(
    pattern: WorkflowPattern,
    tasks: TaskPattern[],
    config: DailyConfiguration
  ): OpeningSection {
    const openingTasks = [];
    let currentTime = this.parseTime("05:30");
    let sequenceNumber = 1;
    
    // Get staff names from configuration
    const staffMap = new Map(
      config.staffConfiguration.scheduled.map(s => [s.role, s.name])
    );
    
    // Phase 1: Equipment startup (5:30 - 6:00)
    const equipmentTasks = tasks.filter(t => 
      t.patternId === "TP_000" || t.patternId === "TP_000b"
    );
    
    for (const task of equipmentTasks) {
      openingTasks.push({
        sequenceNumber: sequenceNumber++,
        taskId: task.patternId,
        name: task.name,
        assigned: staffMap.get("chef") ?? "Maria",
        startTime: this.formatTime(currentTime),
        durationMinutes: task.durationMinutes,
        status: "pending",
        details: task.sequence[0]?.description
      });
      currentTime = this.addMinutes(currentTime, task.durationMinutes);
    }
    
    // Phase 2: Production prep (6:00 - 6:30)
    const prepTasks = tasks.filter(t => 
      t.category === "prep_task" && 
      t.patternId !== "TP_000" && 
      t.patternId !== "TP_000b" &&
      t.patternId !== "TP_006"
    );
    
    // Elena does most prep
    const prepStaff = staffMap.get("prep_cook") ?? "Elena";
    
    for (const task of prepTasks) {
      // Check for inventory adjustments
      let details = task.sequence[0]?.description;
      
      if (task.patternId === "TP_003") {
        const produceDelay = config.inventoryNotes?.find(
          n => n.item.toLowerCase().includes("produce") && 
               n.status === "delivery_delayed"
        );
        if (produceDelay) {
          details = `NOTE: ${produceDelay.notes ?? "Fresh produce unavailable, using alternatives"}`;
        }
      }
      
      openingTasks.push({
        sequenceNumber: sequenceNumber++,
        taskId: task.patternId,
        name: task.name,
        assigned: task.patternId === "TP_005" 
          ? (staffMap.get("chef") ?? "Maria")  // Maria does hollandaise
          : prepStaff,
        startTime: this.formatTime(currentTime),
        durationMinutes: task.durationMinutes,
        status: "pending",
        details
      });
      currentTime = this.addMinutes(currentTime, task.durationMinutes);
    }
    
    // Phase 3: Station setup (6:30 - 6:40)
    const setupTask = tasks.find(t => t.patternId === "TP_006");
    if (setupTask) {
      openingTasks.push({
        sequenceNumber: sequenceNumber++,
        taskId: setupTask.patternId,
        name: setupTask.name,
        assigned: `${staffMap.get("chef") ?? "Maria"}, ${staffMap.get("line_cook") ?? "James"}`,
        startTime: this.formatTime(currentTime),
        durationMinutes: setupTask.durationMinutes,
        status: "pending"
      });
      currentTime = this.addMinutes(currentTime, setupTask.durationMinutes);
    }
    
    // Phase 4: Final check (6:40 - 6:45)
    openingTasks.push({
      sequenceNumber: sequenceNumber++,
      taskId: "FINAL_CHECK",
      name: "Chef Final Check",
      assigned: staffMap.get("chef") ?? "Maria",
      startTime: this.formatTime(currentTime),
      durationMinutes: 5,
      status: "pending",
      details: "Walk through all stations, confirm readiness, announce team ready for service"
    });
    
    return {
      targetCompletion: "06:45",
      tasks: openingTasks
    };
  }
  
  private assembleServiceSection(
    phases: ServicePhaseConfig[],
    protocols: AdaptationProtocol[],
    config: DailyConfiguration
  ): ServiceSection {
    const servicePhases = phases.map(phase => ({
      phaseId: phase.phaseId,
      name: phase.name,
      timeWindow: `${phase.timeWindow.start}-${phase.timeWindow.end}`,
      expectedVolume: `~${phase.expectedTickets} tickets`,
      staffing: `${config.staffConfiguration.scheduled.length} staff`,
      protocols: phase.protocols,
      specialNotes: phase.specialNotes
    }));
    
    const adaptationTriggers = protocols.map(protocol => ({
      name: protocol.name,
      condition: protocol.trigger.condition,
