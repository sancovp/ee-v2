# L1P3W[1]: The Generator Builder — Definitive Specification

---

## I. Introduction: Making THIS Concrete

This artifact is the definitive specification for the Generator Builder—the concrete instantiation of what L1P1 established as the essential nature of system building, and what L1P2 explored in abstraction. Here, the Generator Builder becomes *this specific system*—complete, implementable, and ready for construction.

The Generator Builder is the meta-generative apparatus that transforms domain specifications into workflow constructor specifications. It is itself a system builder, embodying the same essential properties it produces in the constructors it generates:
- **Generative closure**: Produces complete constructor specifications from domain inputs alone
- **Persistent knowledge**: Maintains patterns, constraints, and protocols across generations
- **Transformation capacity**: Converts domain specifications through selection, assembly, and verification
- **Constraint-bounded**: Operates within GI_001-004 as non-overridable invariants
- **Feedback-dependent**: Persists as a living pattern through continuous participation
- **Human-subordinate**: Advises but does not decide; serves domain experts

This document provides the complete specification necessary to construct the Generator Builder. It consolidates the patterns, processes, architectures, and mechanisms explored in L1P2 into a definitive reference that enables implementation.

---

## II. System Definition

### A. Name and Purpose

```yaml
System_Name: "Workflow Constructor Generator Builder"
Version: "1.0.0"
Classification: "Meta-Generative System"

Purpose:
  statement: |
    Transform domain specifications into operational workflow constructor 
    specifications, achieving generative closure over the space of workflow 
    constructors while maintaining the essential properties of system builders.
  
  scope:
    - Consumes domain specifications (operational context, constraints, success criteria)
    - Produces constructor specifications (complete three-layer architectures)
    - Maintains knowledge of constructor patterns across generations
    - Participates in feedback loop for continuous improvement
  
  boundaries:
    - Generates specifications, not implementations
    - Implementation is performed separately on generated specifications
    - Generator Builder knowledge does not include domain-specific implementation details

Success_Definition: |
  The Generator Builder succeeds when it can consume any valid domain 
  specification and produce a constructor specification that:
  - Satisfies all generator invariants (GI_001-004)
  - Is complete enough to be implemented and deployed
  - Produces working workflow constructors when implemented
```

### B. Relationship to L0P2

The generator built at L0P2 for The Copper Beech Daily Workflow Constructor is a specific instantiation of what the Generator Builder produces:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           GENERATIVE RELATIONSHIP                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Generator Builder                                                         │
│   (L1P3W[1] - THIS SPECIFICATION)                                          │
│           │                                                                  │
│           │ Consumes: Domain Specification for Restaurant Operations          │
│           │                                                                  │
│           │ Produces: Constructor Specification                             │
│           │                                                                  │
│           ▼                                                                  │
│   ┌─────────────────────────────────────────────────────────────────────┐ │
│   │  Constructor Specification for Copper Beech                            │ │
│   │  (Could be produced by Generator Builder from restaurant domain spec)   │ │
│   └─────────────────────────────────────────────────────────────────────┘ │
│           │                                                                  │
│           │ Implemented at L0P2                                            │
│           ▼                                                                  │
│   ┌─────────────────────────────────────────────────────────────────────┐ │
│   │  Copper Beech Daily Workflow Constructor                               │ │
│   │  (The generator that produces daily workflows)                        │ │
│   └─────────────────────────────────────────────────────────────────────┘ │
│           │                                                                  │
│           │ Operates: Receives daily configuration, produces workflows      │
│           ▼                                                                  │
│   ┌─────────────────────────────────────────────────────────────────────┐ │
│   │  Daily Workflows                                                      │ │
│   │  (Executed by operational staff)                                      │ │
│   └─────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

The Generator Builder is the apparatus that could generate the Copper Beech constructor from a domain specification—closing the loop between understanding system building and constructing systems that do system building.

---

## III. Generator Invariants

### A. The Four Invariants

These are the non-overridable structural requirements that all generated constructor specifications must satisfy:

```yaml
Generator_Invariants:
  GI_001:
    code: "GI_001"
    name: "Three-Layer Architecture"
    type: "structural_requirement"
    
    requirement: |
      All generated constructors must have three distinct layers with 
      defined components:
      
      - Knowledge Layer:
        * patterns: solution templates accumulated from execution
        * constraints: hard invariants defining possibility space
        * protocols: standard procedures from validated practice
        * profiles: contextual understanding of operational elements
        * learning_records: feedback integration history
      
      - Processing Layer:
        * config_parser: validates and normalizes configuration input
        * pattern_selector: matches patterns to configuration
        * workflow_assembler: constructs workflow from selected patterns
        * constraint_verifier: enforces hard invariants before output
      
      - Integration Layer:
        * configuration_input: receives daily parameters
        * workflow_output: delivers generated workflows
        * feedback_capture: collects execution observations
        * report_generation: communicates system status
    
    verification:
      method: "structural_check"
      checks:
        - "Knowledge layer has all required components"
        - "Processing layer has all required modules"
        - "Integration layer has all required interfaces"
        - "Layer relationships are correctly specified"
    
    violation_result: "INVALID_OUTPUT"
    applies_to: "all_generated_specifications"
  
  GI_002:
    code: "GI_002"
    name: "Feedback Loop Presence"
    type: "structural_requirement"
    
    requirement: |
      All generated constructors must have a complete feedback loop specification
      with five phases that connect execution back to generation:
      
      - Execute: Workflow runs in operational environment
      - Capture: Observations collected without interpretation
      - Extract: Raw observations transformed into candidates
      - Validate: Human authority reviews and decides
      - Modify: Validated patterns integrated into knowledge
    
    verification:
      method: "completeness_check"
      checks:
        - "All five phases are specified"
        - "Each phase has required components"
        - "Phase transitions are defined"
        - "Human validation authority is specified"
    
    violation_result: "INVALID_OUTPUT"
    applies_to: "all_generated_specifications"
  
  GI_003:
    code: "GI_003"
    name: "Human Authority Definition"
    type: "structural_requirement"
    
    requirement: |
      All generated constructors must define a validation authority:
      
      - name: identifier for the human validator
      - role: must be "Knowledge Validator"
      - scope: all knowledge modifications
      - protocol: how validation occurs (accept/reject/modify/defer)
      - criteria: what makes a pattern valid
    
    verification:
      method: "authority_check"
      checks:
        - "Validator name is specified"
        - "Role is 'Knowledge Validator'"
        - "Scope covers all knowledge modifications"
        - "Validation protocol is defined"
        - "Validation criteria are specified"
    
    violation_result: "INVALID_OUTPUT"
    applies_to: "all_generated_specifications"
  
  GI_004:
    code: "GI_004"
    name: "Hard Constraints Included"
    type: "structural_requirement"
    
    requirement: |
      All generated constructors must include the four universal hard constraints
      with complete definitions and verification methods:
      
      - HC_001: Food Safety Temperature Control
        * danger_zone: (40°F, 140°F)
        * cumulative_maximum: 2.hours
        * applies_to: ALL food_items
      
      - HC_002: Cross-Contamination Prevention
        * required_separation: (raw_foods, ready_to_eat)
        * spatial_invariant: TRUE
        * applies_to: ALL prep_areas
      
      - HC_003: Minimum Staffing Levels
        * minimum_staff: 3
        * applies_to: ALL service_periods
      
      - HC_004: Time-Temperature Combinations
        * prep_item_maximum: 4.hours
        * applies_to: ALL prep_items
    
    verification:
      method: "constraint_check"
      checks:
        - "HC_001 is defined with verification method"
        - "HC_002 is defined with verification method"
        - "HC_003 is defined with verification method"
        - "HC_004 is defined with verification method"
        - "All constraints have violation_result: INVALID_OUTPUT"
    
    violation_result: "INVALID_OUTPUT"
    applies_to: "all_generated_specifications"
```

### B. Invariant Properties

| Property | Expression |
|----------|------------|
| **Non-overridable** | Cannot be traded, relaxed, or overridden |
| **Total** | Apply to every generated specification |
| **Foundational** | Define what specifications are valid at all |
| **Static** | Do not change within Generator Builder lifetime |
| **Absolute** | Violation produces INVALID_OUTPUT, not warning |

### C. Invariant Hierarchy

```
META-INVARIANTS (How invariants can change)
        ▲
        │ Generator Builder redesign required
        │
GENERATOR INVARIANTS (GI_001-004)
        ▲
        │ Structural requirement for all specifications
        │
DOMAIN CONSTRAINTS (Added by domain specification)
        ▲
        │ Domain-specific requirements
        │
SOFT REQUIREMENTS (Can be optimized)
        ▲
        │ Quality improvements within invariants
```

---

## IV. Three-Layer Architecture

### A. The Complete Architecture

The Generator Builder embodies the same three-layer architecture it generates:

```yaml
Generator_Builder_Architecture:
  knowledge_layer:
    description: |
      Persistent structures providing patterns, constraints, and protocols
      for constructor construction. This layer provides resources to the
      processing layer without initiating transformations itself.
    
    components:
      pattern_library:
        description: "Structured collection of all constructor patterns"
        categories:
          architecture_patterns:
            description: "Structural templates for constructors"
            entries:
              - three_layer_architecture
              - hub_and_spoke_architecture
              - hierarchical_architecture
          
          constraint_patterns:
            description: "Constraint definitions and verification methods"
            entries:
              - universal_constraints
              - restaurant_domain_constraints
              - soft_constraints
          
          feedback_patterns:
            description: "Feedback loop mechanisms"
            entries:
              - standard_feedback_loop
              - rapid_iteration_feedback
              - conservative_learning_feedback
          
          interface_patterns:
            description: "External interface specifications"
            entries:
              - standard_interfaces
              - digital_first_interfaces
              - human_centric_interfaces
        
        management:
          versioning: true
          validation_required: "domain_expert"
          deprecation_tracked: true
          backup_maintained: true
      
      effectiveness_tracker:
        description: "Scores and tracks pattern performance over time"
        
        metrics_tracked:
          - generation_success_rate_by_pattern
          - constructor_quality_by_pattern
          - pattern_usage_frequency
          - pattern_effectiveness_over_time
          - cross_domain_transfer_success
        
        update_frequency: "after_each_generation"
        
        decay:
          enabled: true
          rate: "gradual_for_unused_patterns"
          threshold: "12_months_without_use"
      
      protocol_library:
        description: "Procedures for constructor construction"
        
        protocols:
          - name: "Standard Assembly Protocol"
            description: "Default procedure for constructor construction"
            steps: ["parse", "select", "assemble", "verify", "deliver"]
            applicable: "all_domains"
          
          - name: "Expedited Assembly Protocol"
            description: "Fast procedure for simple domains"
            steps: ["parse", "select", "assemble", "deliver"]
            applicable: "simple_complexity_only"
          
          - name: "Validation Protocol"
            description: "Procedure for pattern candidate validation"
            steps: ["prepare_presentation", "expert_review", "render_decision", "implement"]
            applicable: "all_validations"
      
      domain_profiles:
        description: "Characteristics of known operational domains"
        
        profiles:
          restaurant:
            business_type: "food_service"
            typical_constraints: ["HC_001", "HC_002", "HC_003", "HC_004", "RC_001-004"]
            typical_patterns: ["three_layer", "standard_feedback", "standard_interfaces"]
            recommended_feedback: "standard_feedback_loop"
          
          manufacturing:
            business_type: "production"
            typical_constraints: ["safety", "quality", "throughput"]
            typical_patterns: ["hub_and_spoke", "conservative_feedback"]
            recommended_feedback: "conservative_learning_feedback"
          
          healthcare:
            business_type: "medical_service"
            typical_constraints: ["patient_safety", "compliance", "privacy"]
            typical_patterns: ["hierarchical", "conservative_feedback", "human_centric"]
            recommended_feedback: "conservative_learning_feedback"
          
          service_operations:
            business_type: "service"
            typical_constraints: ["response_time", "quality", "customer_satisfaction"]
            typical_patterns: ["three_layer", "rapid_iteration_feedback"]
            recommended_feedback: "rapid_iteration_feedback"
    
    responsibilities:
      - "Provide patterns for constructor construction"
      - "Track pattern effectiveness for informed selection"
      - "Supply protocols for assembly processes"
      - "Maintain domain profiles for classification"
    
    boundaries:
      - "Does not execute generation independently"
      - "Does not interface with external systems directly"
      - "Only provides resources to processing layer"
  
  processing_layer:
    description: |
      Transformation modules that convert domain specifications
      into constructor specifications. This layer performs the
      generative work of the Generator Builder.
    
    modules:
      domain_specification_parser:
        description: "Validates and normalizes domain specifications"
        
        inputs:
          - raw_domain_specification
        
        outputs:
          - parsed_domain_specification
        
        validation_checks:
          - "Schema conformance"
          - "Required fields present"
          - "Universal constraints defined"
          - "Success criteria valid"
        
        classification_outputs:
          - business_type
          - complexity_level
          - change_rate
          - stakes_level
        
        error_types:
          - MissingFieldError
          - MissingConstraintError
          - ValidationError
          - SchemaError
      
      pattern_selector:
        description: "Selects appropriate patterns for the domain"
        
        inputs:
          - parsed_domain_specification
          - pattern_library
          - effectiveness_tracker
        
        outputs:
          - pattern_selection
        
        selection_strategy:
          architecture:
            required: "three_layer_architecture"
            optional: ["hub_and_spoke", "hierarchical"]
            selection_basis: "complexity_level"
          
          constraints:
            required: "universal_constraints"
            optional: ["domain_specific", "soft_constraints"]
            selection_basis: "business_type"
          
          feedback:
            required: "one_feedback_pattern"
            selection_basis: "stakes_level"
          
          interface:
            required: "one_interface_pattern"
            selection_basis: "technical_maturity"
        
        scoring:
          formula: "score = relevance × (1 + effectiveness × 0.5)"
          components:
            relevance:
              base_score: 0.0
              universal_applicable: 0.3
              domain_match: 0.7
              partial_match: 0.1
            
            effectiveness:
              source: "effectiveness_tracker"
              range: [0.0, 1.0]
        
        compatibility_rules:
          - "High-stakes domains use conservative feedback"
          - "Complex domains use hub-and-spoke"
          - "Technology-mature domains use digital-first interfaces"
      
      workflow_assembler:
        description: "Assembles constructor specification from patterns"
        
        inputs:
          - pattern_selection
          - parsed_domain_specification
          - pattern_library
        
        outputs:
          - assembled_constructor_specification
        
        assembly_order:
          - "Knowledge Layer components"
          - "Processing Layer components"
          - "Integration Layer components"
          - "Feedback Loop specification"
          - "Validation Authority definition"
          - "Success Criteria"
        
        derivation_rules:
          knowledge_layer:
            patterns:
              source: "architecture_pattern + constraint_pattern"
              derivation: "template instantiation for domain"
            
            constraints:
              source: "constraint_pattern"
              universal: "always include HC_001-004"
              domain_specific: "include if applicable"
            
            protocols:
              source: "pattern_library + business_type"
              standard: "opening, service, closing"
              domain_specific: "include if applicable"
            
            profiles:
              source: "domain_profile"
              base: "senior, standard, junior"
              domain: "include if applicable"
          
          processing_layer:
            config_parser:
              source: "parsed_spec.configuration_inputs"
            
            pattern_selector:
              source: "pattern_selection"
            
            workflow_assembler:
              source: "pattern_selection"
            
            constraint_verifier:
              source: "constraint_pattern"
              checks: ["HC_001", "HC_002", "HC_003", "HC_004"]
          
          feedback_loop:
            source: "feedback_pattern"
            phases: ["execute", "capture", "extract", "validate", "modify"]
          
          validation_authority:
            source: "default or domain_specification"
            default_name: "Maria"
            default_role: "Knowledge Validator"
      
      constraint_verifier:
        description: "Verifies constructor satisfies all generator invariants"
        
        inputs:
          - assembled_constructor_specification
        
        outputs:
          - verified_constructor_specification
          - OR verification_failure
        
        verification_sequence:
          - check: "GI_001: Three-Layer Architecture"
            method: "structural_completeness"
            required_layers:
              knowledge: ["patterns", "constraints", "protocols", "profiles"]
              processing: ["config_parser", "pattern_selector", "workflow_assembler", "constraint_verifier"]
              integration: ["configuration_input", "workflow_output", "feedback_capture"]
            
          - check: "GI_002: Feedback Loop Presence"
            method: "phase_completeness"
            required_phases: ["execute", "capture", "extract", "validate", "modify"]
            
          - check: "GI_003: Human Authority Definition"
            method: "authority_specification"
            required_fields: ["name", "role", "scope", "protocol"]
            required_role: "Knowledge Validator"
            
          - check: "GI_004: Hard Constraints Included"
            method: "constraint_presence"
            required_constraints: ["HC_001", "HC_002", "HC_003", "HC_004"]
            
          - check: "Internal Consistency"
            method: "reference_integrity"
            checks:
              - "All referenced patterns exist"
              - "All referenced constraints exist"
              - "All phases connect correctly"
        
        failure_handling:
          - "Log violation details"
          - "Return verification_failure with specifics"
          - "Trigger regeneration_attempt"
          - "Do not deliver invalid specification"
    
    boundaries:
      - "Receives from Knowledge Layer"
      - "Delivers to Integration Layer"
      - "Processes without external intervention during generation"
  
  integration_layer:
    description: |
      Interfaces connecting the Generator Builder to external systems
      and to its own feedback loop.
    
    components:
      api_gateway:
        description: "REST API for external interaction"
        
        base_path: "/api/v1"
        
        endpoints:
          POST /generate:
            description: "Generate constructor from domain specification"
            content_type: "application/json or application/yaml"
            input_schema: "DomainSpecification"
            output_schema: "ConstructorSpecification"
            responses:
              200:
                description: "Generation successful"
                body: "ConstructorSpecification"
              400:
                description: "Invalid domain specification"
                body: "ErrorResponse"
              422:
                description: "Validation failed"
                body: "ValidationErrorResponse"
              500:
                description: "Generation failed"
                body: "ErrorResponse"
            
            authentication: "required"
            rate_limit: "10 requests per minute"
          
          POST /feedback:
            description: "Submit constructor performance feedback"
            content_type: "application/json"
            input_schema: "PerformanceFeedback"
            responses:
              200:
                description: "Feedback recorded"
              400:
                description: "Invalid feedback format"
              404:
                description: "Constructor not found"
            
            authentication: "required"
          
          GET /constructors/{id}:
            description: "Get constructor specification by ID"
            responses:
              200:
                body: "ConstructorSpecification"
              404:
                body: "NotFoundResponse"
            
            authentication: "required"
          
          GET /patterns:
            description: "List available constructor patterns"
            query_params:
              - category (optional)
              - applicability (optional)
            responses:
              200:
                body: "PatternListResponse"
            
            authentication: "required"
          
          GET /patterns/{name}:
            description: "Get specific pattern details"
            responses:
              200:
                body: "PatternDetailResponse"
              404:
                body: "NotFoundResponse"
            
            authentication: "required"
          
          GET /metrics:
            description: "Get Generator Builder metrics"
            responses:
              200:
                body: "MetricsResponse"
            
            authentication: "required"
          
          GET /health:
            description: "Health check endpoint"
            responses:
              200:
                body: "HealthResponse"
            
            authentication: "not_required"
        
        authentication:
          method: "API Key"
          header: "X-API-Key"
          format: "Bearer token"
        
        error_handling:
          standard_errors:
            - ValidationError (422)
            - NotFoundError (404)
            - AuthenticationError (401)
            - RateLimitError (429)
            - InternalError (500)
          
          error_response_format:
            code: "string"
            message: "string"
            details: "object (optional)"
            request_id: "string"
      
      metrics_collector:
        description: "Collects generation and performance metrics"
        
        metrics:
          generation:
            - name: "generation_attempts_total"
              type: "counter"
              description: "Total generation attempts"
            
            - name: "generation_successes_total"
              type: "counter"
              description: "Successful generations"
            
            - name: "generation_failures_total"
              type: "counter"
              description: "Failed generations"
              labels: ["failure_reason"]
            
            - name: "generation_duration_seconds"
              type: "histogram"
              description: "Generation duration in seconds"
              buckets: [0.1, 0.5, 1, 2, 5, 10, 30, 60]
            
            - name: "regeneration_count"
              type: "counter"
              description: "Regenerations due to verification failure"
          
          pattern_usage:
            - name: "pattern_selections_total"
              type: "counter"
              description: "Pattern selection count"
              labels: ["pattern_name", "pattern_category"]
            
            - name: "pattern_effectiveness_score"
              type: "gauge"
              description: "Current effectiveness score"
              labels: ["pattern_name"]
          
          verification:
            - name: "verification_attempts_total"
              type: "counter"
              description: "Verification attempts"
            
            - name: "verification_failures_total"
              type: "counter"
              description: "Verification failures"
              labels: ["invariant_violated"]
            
            - name: "specifications_delivered_total"
              type: "counter"
              description: "Successfully delivered specifications"
          
          feedback_loop:
            - name: "feedback_submissions_total"
              type: "counter"
              description: "Feedback submissions received"
            
            - name: "patterns_extracted_total"
              type: "counter"
              description: "Pattern candidates extracted"
            
            - name: "patterns_validated_total"
              type: "counter"
              description: "Patterns validated"
              labels: ["decision"]
            
            - name: "patterns_integrated_total"
              type: "counter"
              description: "Patterns integrated into knowledge"
        
        storage:
          type: "time_series_database"
          retention: "90_days"
          aggregation: "1_minute_intervals"
        
        exposure:
          format: "Prometheus"
          endpoint: "/metrics"
      
      audit_logger:
        description: "Logs generation history and decisions"
        
        logged_events:
          generation:
            timestamp: "ISO8601"
            domain_specification_hash: "SHA256"
            patterns_selected: ["pattern_names"]
            generation_duration_ms: "integer"
            success: "boolean"
            error_details: "object (if failed)"
            request_id: "string"
          
          verification:
            timestamp: "ISO8601"
            constructor_id: "string"
            checks_performed: ["check_names"]
            checks_passed: ["check_names"]
            checks_failed: ["check_names"]
            violations: ["violation_details"]
          
          feedback:
            timestamp: "ISO8601"
            constructor_id: "string"
            feedback_type: "string"
            patterns_extracted: ["pattern_candidates"]
            validation_decisions: ["decisions"]
        
        storage:
          type: "append_only_database"
          retention: "1_year"
          encryption: "at_rest"
        
        access:
          authentication: "required"
          roles: ["admin", "auditor"]
        
        compliance:
          - "All generations logged before delivery"
          - "All modifications logged before application"
          - "Audit trail tamper-evident"
      
      feedback_loop_interface:
        description: "Connects to Generator Builder's own feedback loop"
        
        connections:
          to_performance_monitor:
            data_received:
              - constructor_id
              - deployment_timestamp
              - generation_quality_metrics
              - workflow_generation_success_rate
              - constraint_satisfaction_rate
              - user_satisfaction_scores
            
            frequency: "continuous"
          
          to_pattern_extractor:
            data_sent:
              - performance_observations
              - pattern_effectiveness_correlations
              - assembly_quality_assessments
            
            frequency: "batch_daily"
          
          to_knowledge_modifier:
            data_received:
              - validated_pattern_improvements
              - effectiveness_score_updates
              - new_pattern_variants
            
            frequency: "per_validation"
```

---

## V. Complete Data Structures

### A. Domain Specification Input

```python
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any, Union
from enum import Enum
import json

class BusinessType(Enum):
    RESTAURANT = "restaurant"
    MANUFACTURING = "manufacturing"
    HEALTHCARE = "healthcare"
    SERVICE_OPERATIONS = "service_operations"
    GENERIC_OPERATIONS = "generic_operations"

class Complexity(Enum):
    SIMPLE = "simple"
    MODERATE = "moderate"
    COMPLEX = "complex"

class Stakes(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class ChangeRate(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

@dataclass
class OperationalContext:
    """Context describing the operational environment."""
    business_type: str
    operational_hours: str
    service_model: Optional[str] = None
    cuisine_type: Optional[str] = None
    additional_context: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'business_type': self.business_type,
            'operational_hours': self.operational_hours,
            'service_model': self.service_model,
            'cuisine_type': self.cuisine_type,
            'additional_context': self.additional_context
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'OperationalContext':
        return cls(
            business_type=data.get('business_type', ''),
            operational_hours=data.get('operational_hours', ''),
            service_model=data.get('service_model'),
            cuisine_type=data.get('cuisine_type'),
            additional_context=data.get('additional_context', {})
        )

@dataclass
class ConfigurationInput:
    """A configuration input for the constructor."""
    name: str
    description: str
    required: bool = True
    data_type: str = "string"
    validation_rules: Optional[Dict[str, Any]] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'name': self.name,
            'description': self.description,
            'required': self.required,
            'data_type': self.data_type,
            'validation_rules': self.validation_rules
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ConfigurationInput':
        return cls(
            name=data['name'],
            description=data['description'],
            required=data.get('required', True),
            data_type=data.get('data_type', 'string'),
            validation_rules=data.get('validation_rules')
        )

@dataclass
class HardConstraint:
    """A hard constraint definition."""
    code: str
    name: str
    type: str
    definition: str
    verification_method: str
    violation_result: str = "INVALID_OUTPUT"
    applies_to: str = "all"
    additional_properties: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        result = {
            'code': self.code,
            'name': self.name,
            'type': self.type,
            'definition': self.definition,
            'verification_method': self.verification_method,
            'violation_result': self.violation_result,
            'applies_to': self.applies_to
        }
        result.update(self.additional_properties)
        return result
    
    @classmethod
    def from_dict(cls, code: str, data: Dict[str, Any]) -> 'HardConstraint':
        known_fields = {'code', 'name', 'type', 'definition', 'verification_method', 
                       'violation_result', 'applies_to'}
        additional = {k: v for k, v in data.items() if k not in known_fields}
        return cls(
            code=code,
            name=data.get('name', code),
            type=data['type'],
            definition=data['definition'],
            verification_method=data['verification_method'],
            violation_result=data.get('violation_result', 'INVALID_OUTPUT'),
            applies_to=data.get('applies_to', 'all'),
            additional_properties=additional
        )

@dataclass
class SuccessCriteria:
    """Success criteria for the constructor."""
    generation_success_rate: float = 0.95
    constraint_satisfaction: float = 1.00
    sla_compliance: float = 0.90
    generation_timing: str = "by_9_pm_previous_evening"
    learning_integration: float = 0.80
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'generation_success_rate': self.generation_success_rate,
            'constraint_satisfaction': self.constraint_satisfaction,
            'sla_compliance': self.sla_compliance,
            'generation_timing': self.generation_timing,
            'learning_integration': self.learning_integration
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SuccessCriteria':
        return cls(
            generation_success_rate=data.get('generation_success_rate', 0.95),
            constraint_satisfaction=data.get('constraint_satisfaction', 1.00),
            sla_compliance=data.get('sla_compliance', 0.90),
            generation_timing=data.get('generation_timing', 'by_9_pm_previous_evening'),
            learning_integration=data.get('learning_integration', 0.80)
        )

@dataclass
class FeedbackMechanism:
    """Feedback mechanism specification."""
    execution_capture: str
    pattern_extraction: str
    human_validation: str
    validation_authority: str = "Maria"
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'execution_capture': self.execution_capture,
            'pattern_extraction': self.pattern_extraction,
            'human_validation': self.human_validation,
            'validation_authority': self.validation_authority
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'FeedbackMechanism':
        return cls(
            execution_capture=data['execution_capture'],
            pattern_extraction=data['pattern_extraction'],
            human_validation=data['human_validation'],
            validation_authority=data.get('validation_authority', 'Maria')
        )

@dataclass
class DomainSpecification:
    """
    Complete domain specification for constructor generation.
    
    This is the primary input to the Generator Builder. It characterizes
    the target operational context for which a workflow constructor will
    be generated.
    """
    domain_name: str
    operational_context: OperationalContext
    configuration_inputs: List[ConfigurationInput]
    hard_constraints: Dict[str, HardConstraint]
    success_criteria: SuccessCriteria
    feedback_mechanisms: FeedbackMechanism
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            'domain_name': self.domain_name,
            'operational_context': self.operational_context.to_dict(),
            'configuration_inputs': [c.to_dict() for c in self.configuration_inputs],
            'hard_constraints': {code: c.to_dict() for code, c in self.hard_constraints.items()},
            'success_criteria': self.success_criteria.to_dict(),
            'feedback_mechanisms': self.feedback_mechanisms.to_dict(),
            'metadata': self.metadata
        }
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)
    
    def to_yaml(self) -> str:
        import yaml
        return yaml.dump(self.to_dict(), default_flow_style=False)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DomainSpecification':
        constraints = {
            code: HardConstraint.from_dict(code, constraint_data)
            for code, constraint_data in data.get('hard_constraints', {}).items()
        }
        return cls(
            domain_name=data['domain_name'],
            operational_context=OperationalContext.from_dict(data['operational_context']),
            configuration_inputs=[
                ConfigurationInput.from_dict(c) 
                for c in data.get('configuration_inputs', [])
            ],
            hard_constraints=constraints,
            success_criteria=SuccessCriteria.from_dict(data.get('success_criteria', {})),
            feedback_mechanisms=FeedbackMechanism.from_dict(data.get('feedback_mechanisms', {})),
            metadata=data.get('metadata', {})
        )
    
    @classmethod