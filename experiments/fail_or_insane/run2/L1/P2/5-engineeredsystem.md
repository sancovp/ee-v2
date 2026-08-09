# L1P2W[1](5): System Building — The Engineered System

---

## I. Introduction: From Theory to Implementation

The prior artifacts in this exploration established the essential nature of system building (L1P1W[1]), defined the abstract goal of building a Generator Builder (L1P2W[1](0)), developed the constructor patterns that serve as building blocks (L1P2W[1](1)), detailed the generation process transformation architecture (L1P2W[1](2)), explored the feedback loop that constitutes the Generator Builder as a living architecture (L1P2W[1](3)), and mapped the topological structure of the Generator Builder (L1P2W[1](4)). We now arrive at the culmination: **The Engineered System**—a concrete, implementable specification of the Generator Builder that can be constructed and deployed.

This artifact transforms theoretical understanding into practical implementation. It answers the question: Given what we now understand about system building, how do we actually build a system that can generate workflow constructors? The artifact provides the complete engineered specification, including data structures, algorithms, interfaces, and deployment guidance necessary to construct a working Generator Builder.

The Generator Builder, as an engineered system, must embody all the essential properties established in the L1P1 exploration:
- **Generative Closure**: Produces complete constructor specifications from domain inputs alone
- **Persistent Knowledge**: Maintains patterns, constraints, protocols for workflow construction
- **Transformation Capacity**: Converts domain specifications through selection, assembly, verification
- **Constraint-Bounded**: Operates within GI_001-004 as non-overridable invariants
- **Feedback-Dependent**: Persists as living pattern through continuous feedback participation
- **Human-Subordinate**: Advises but does not decide; serves domain experts

This artifact specifies how each property is realized in implementation.

---

## II. The Engineered Architecture

### A. System Architecture Overview

The Generator Builder implements a three-layer architecture that mirrors the structures it produces:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         GENERATOR BUILDER                                    │
│                      Engineered System Architecture                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                     INTEGRATION LAYER                                  │  │
│  │                                                                       │  │
│  │  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐     │  │
│  │  │   REST API     │    │  Metrics        │    │   Audit        │     │  │
│  │  │   Gateway      │    │  Collector      │    │   Logger       │     │  │
│  │  │                 │    │                  │    │                 │     │  │
│  │  │ POST /generate  │    │ Generation      │    │ Generation     │     │  │
│  │  │ POST /feedback  │    │ Metrics         │    │ History        │     │  │
│  │  │ GET  /status   │    │ Performance      │    │ Decision       │     │  │
│  │  │ GET  /metrics  │    │ Quality         │    │ Trails         │     │  │
│  │  │                 │    │                  │    │                 │     │  │
│  │  └────────┬────────┘    └────────┬────────┘    └────────┬────────┘     │  │
│  │           │                        │                      │              │  │
│  └───────────┼────────────────────────┼──────────────────────┼──────────────┘  │
│              │                        │                      │                 │
│              ▼                        ▼                      │                 │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                       PROCESSING LAYER                                  │  │
│  │                                                                       │  │
│  │     ┌───────────────┐      ┌───────────────┐      ┌───────────────┐   │  │
│  │     │    PARSER     │─────▶│   SELECTOR    │─────▶│   ASSEMBLER   │   │  │
│  │     │               │      │               │      │               │   │  │
│  │     │ • Schema      │      │ • Domain      │      │ • Knowledge   │   │  │
│  │     │   Validation  │      │   Classify   │      │   Layer       │   │  │
│  │     │ • Required   │      │ • Pattern    │      │ • Processing  │   │  │
│  │     │   Elements   │      │   Filter     │      │   Layer       │   │  │
│  │     │ • Constraint │      │ • Score &    │      │ • Integration │   │  │
│  │     │   Check      │      │   Select     │      │   Layer       │   │  │
│  │     │ • Intermediate│     │               │      │ • Feedback   │   │  │
│  │     │   Build      │      │               │      │   Loop       │   │  │
│  │     │               │      │               │      │               │   │  │
│  │     └───────┬───────┘      └───────┬───────┘      └───────┬───────┘   │  │
│  │             │                      │                      │             │  │
│  │             └──────────────────────┼──────────────────────┘             │  │
│  │                                    │                                    │  │
│  │                                    ▼                                    │  │
│  │                         ┌───────────────────┐                          │  │
│  │                         │     VERIFIER      │                          │  │
│  │                         │                   │                          │  │
│  │                         │ • GI_001: Three  │                          │  │
│  │                         │   Layer Check    │                          │  │
│  │                         │ • GI_002: Feed- │                          │  │
│  │                         │   back Check    │                          │  │
│  │                         │ • GI_003: Human │                          │  │
│  │                         │   Auth Check   │                          │  │
│  │                         │ • GI_004: HC   │                          │  │
│  │                         │   Include      │                          │  │
│  │                         │                   │                          │  │
│  │                         └─────────┬─────────┘                          │  │
│  │                                   │                                    │  │
│  │                                   ▼                                    │  │
│  │                         ┌───────────────────┐                          │  │
│  │                         │     DELIVER       │                          │  │
│  │                         │                   │                          │  │
│  │                         │ • Success Result  │                          │  │
│  │                         │ • Error Response │                          │  │
│  │                         │                   │                          │  │
│  │                         └───────────────────┘                          │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                    │                                       │
│                                    ▼                                       │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                        KNOWLEDGE LAYER                                 │  │
│  │                                                                       │  │
│  │  ┌────────────────────────────────────────────────────────────────┐  │  │
│  │  │                    PATTERN LIBRARY                              │  │  │
│  │  │                                                                 │  │  │
│  │  │  Architecture    Constraint    Feedback     Interface          │  │  │
│  │  │  Patterns        Patterns       Patterns     Patterns          │  │  │
│  │  │      │               │              │             │              │  │  │
│  │  │      ▼               ▼              ▼             ▼              │  │  │
│  │  │  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐   │  │  │
│  │  │  │ Three-    │  │ Universal │  │ Standard  │  │ Standard  │   │  │  │
│  │  │  │ Layer     │  │ (HC_001- │  │ Feedback  │  │ Interface │   │  │  │
│  │  │  │ Arch.     │  │ 004)     │  │ Loop      │  │           │   │  │  │
│  │  │  └───────────┘  └───────────┘  └───────────┘  └───────────┘   │  │  │
│  │  │  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐   │  │  │
│  │  │  │ Hub-      │  │ Restaurant│  │ Rapid     │  │ Digital-  │   │  │  │
│  │  │  │ and-Spoke │  │ Domain    │  │ Iteration │  │ First     │   │  │  │
│  │  │  └───────────┘  └───────────┘  └───────────┘  └───────────┘   │  │  │
│  │  │  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐   │  │  │
│  │  │  │ Hier-     │  │ Soft     │  │ Conser-   │  │ Human-   │   │  │  │
│  │  │  │ archical  │  │ Constr.   │  │ vative    │  │ Centric  │   │  │  │
│  │  │  └───────────┘  └───────────┘  └───────────┘  └───────────┘   │  │  │
│  │  │                                                                 │  │  │
│  │  └────────────────────────────────────────────────────────────────┘  │  │
│  │                                                                       │  │
│  │  ┌─────────────────────┐           ┌─────────────────────────────┐   │  │
│  │  │ EFFECTIVENESS       │           │      PROTOCOL LIBRARY         │   │  │
│  │  │ TRACKER             │           │                              │   │  │
│  │  │                     │           │  Assembly Protocols          │   │  │
│  │  │ • Pattern Scores    │           │  Validation Protocols         │   │  │
│  │  │ • Historical Perf   │           │  Integration Protocols        │   │  │
│  │  │ • Usage Stats       │           │                              │   │  │
│  │  │                     │           │                              │   │  │
│  │  └─────────────────────┘           └─────────────────────────────┘   │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                    │                                       │
│                                    │ Feedback Loop Connection              │
│                                    ▼                                       │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                      FEEDBACK LOOP                                     │  │
│  │                                                                       │  │
│  │   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────────────┐   │  │
│  │   │ Observe │───▶│ Capture │───▶│ Extract │───▶│  Validate       │   │  │
│  │   │         │    │         │    │         │    │  (Domain Expert)│   │  │
│  │   └─────────┘    └─────────┘    └─────────┘    └────────┬────────┘   │  │
│  │                                                         │            │  │
│  │                                                         │            │  │
│  │                                                         ▼            │  │
│  │                                                  ┌─────────────┐     │  │
│  │                                                  │   Modify    │     │  │
│  │                                                  │  Knowledge  │     │  │
│  │                                                  └──────┬──────┘     │  │
│  │                                                         │            │  │
│  │                                                         │            │  │
│  │   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │            │  │
│  │   │  Pattern   │    │  Domain    │    │  Protocol   │◀─┘            │  │
│  │   │  Library   │◀───│  Expert    │───▶│  Library    │              │  │
│  │   │  Update    │    │  Validates │    │  Update     │              │  │
│  │   └─────────────┘    └─────────────┘    └─────────────┘              │  │
│  │                                                                       │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### B. Data Flow Summary

The engineered system implements a unidirectional data flow:

```
Domain Specification (Input)
        │
        ▼
┌─────────────────┐
│   API Gateway   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     Parser     │  → Validated intermediate representation
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Selector     │  → Pattern selection from library
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Assembler     │  → Assembled constructor specification
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│    Verifier     │  → Verified against GI_001-004
└────────┬────────┘
         │
         ├── Verified ──▶ ┌─────────────────┐
         │                │    Deliver      │  → Constructor Specification
         │                └────────┬────────┘
         │                         │
         └── Verification Failed ──▶│
                                    │
                                    ▼
                           ┌─────────────────┐
                           │  Error Response │
                           └─────────────────┘
```

---

## III. Core Data Structures

### A. Domain Specification Input

```python
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from enum import Enum

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

@dataclass
class ConfigurationInput:
    """A configuration input for the constructor."""
    name: str
    description: str
    required: bool = True
    data_type: str = "string"

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

@dataclass
class SuccessCriteria:
    """Success criteria for the constructor."""
    generation_success_rate: float = 0.95
    constraint_satisfaction: float = 1.00
    sla_compliance: float = 0.90
    generation_timing: str = "by_9_pm_previous_evening"
    learning_integration: float = 0.80

@dataclass
class FeedbackMechanism:
    """Feedback mechanism specification."""
    execution_capture: str
    pattern_extraction: str
    human_validation: str
    validation_authority: str = "Maria"

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
    
    def validate(self) -> List[str]:
        """
        Validate the domain specification.
        Returns list of validation errors, empty if valid.
        """
        errors = []
        
        # Check required fields
        if not self.domain_name:
            errors.append("domain_name is required")
        
        # Check business type
        if not self.operational_context.business_type:
            errors.append("operational_context.business_type is required")
        
        # Check configuration inputs
        if not self.configuration_inputs:
            errors.append("At least one configuration_input is required")
        
        required_inputs = [i for i in self.configuration_inputs if i.required]
        if not required_inputs:
            errors.append("At least one required configuration_input is required")
        
        # Check hard constraints
        universal_codes = ['HC_001', 'HC_002', 'HC_003', 'HC_004']
        for code in universal_codes:
            if code not in self.hard_constraints:
                errors.append(f"Hard constraint {code} is required")
        
        # Check success criteria
        if not 0 <= self.success_criteria.generation_success_rate <= 1:
            errors.append("generation_success_rate must be between 0 and 1")
        
        if not 0 <= self.success_criteria.constraint_satisfaction <= 1:
            errors.append("constraint_satisfaction must be between 0 and 1")
        
        return errors
```

### B. Constructor Specification Output

```python
@dataclass
class KnowledgeLayerSpec:
    """Specification for the Knowledge Layer of a constructor."""
    patterns: List[Dict[str, Any]]
    constraints: Dict[str, HardConstraint]
    protocols: List[Dict[str, Any]]
    profiles: List[Dict[str, Any]]
    learning_records: Dict[str, Any]

@dataclass
class ProcessingLayerSpec:
    """Specification for the Processing Layer of a constructor."""
    config_parser: Dict[str, Any]
    pattern_selector: Dict[str, Any]
    workflow_assembler: Dict[str, Any]
    constraint_verifier: Dict[str, Any]

@dataclass
class IntegrationLayerSpec:
    """Specification for the Integration Layer of a constructor."""
    configuration_input: Dict[str, Any]
    workflow_output: Dict[str, Any]
    feedback_capture: Dict[str, Any]
    report_generation: Dict[str, Any]

@dataclass
class FeedbackLoopSpec:
    """Specification for the Feedback Loop of a constructor."""
    capture: Dict[str, Any]
    extract: Dict[str, Any]
    validate: Dict[str, Any]
    modify: Dict[str, Any]

@dataclass
class ValidationAuthoritySpec:
    """Specification for the Validation Authority of a constructor."""
    name: str
    role: str
    scope: str
    protocol: str

@dataclass
class ConstructorMetadata:
    """Metadata about the generated constructor specification."""
    generated_from_patterns: List[str]
    generation_timestamp: str
    generator_version: str
    domain_classification: Dict[str, Any]

@dataclass
class ConstructorSpecification:
    """
    Complete constructor specification output from the Generator Builder.
    
    This is the primary output of the Generator Builder. It provides a
    complete description of a workflow constructor that can be implemented
    and deployed for the target operational domain.
    """
    constructor_name: str
    knowledge_layer: KnowledgeLayerSpec
    processing_layer: ProcessingLayerSpec
    integration_layer: IntegrationLayerSpec
    feedback_loop: FeedbackLoopSpec
    validation_authority: ValidationAuthoritySpec
    success_criteria: SuccessCriteria
    metadata: ConstructorMetadata
    
    def to_yaml(self) -> str:
        """Serialize to YAML format."""
        import yaml
        # Implementation would serialize dataclass to YAML
        pass
    
    def to_json(self) -> str:
        """Serialize to JSON format."""
        import json
        # Implementation would serialize dataclass to JSON
        pass
    
    def validate_gi_001(self) -> bool:
        """Verify three-layer architecture present."""
        return (
            self.knowledge_layer is not None and
            self.processing_layer is not None and
            self.integration_layer is not None
        )
    
    def validate_gi_002(self) -> bool:
        """Verify feedback loop present."""
        return (
            self.feedback_loop is not None and
            self.feedback_loop.capture is not None and
            self.feedback_loop.extract is not None and
            self.feedback_loop.validate is not None and
            self.feedback_loop.modify is not None
        )
    
    def validate_gi_003(self) -> bool:
        """Verify human authority defined."""
        return (
            self.validation_authority is not None and
            self.validation_authority.name is not None and
            self.validation_authority.role == "Knowledge Validator"
        )
    
    def validate_gi_004(self) -> bool:
        """Verify hard constraints included."""
        constraint_codes = list(self.knowledge_layer.constraints.keys())
        return all(
            code in constraint_codes 
            for code in ['HC_001', 'HC_002', 'HC_003', 'HC_004']
        )
```

---

## IV. The Processing Layer: Implementation

### A. Domain Specification Parser

```python
class ParserError(Exception):
    """Base exception for parser errors."""
    pass

class MissingFieldError(ParserError):
    """Raised when a required field is missing."""
    def __init__(self, field: str):
        self.field = field
        super().__init__(f"Missing required field: {field}")

class MissingConstraintError(ParserError):
    """Raised when a required constraint is missing."""
    def __init__(self, code: str):
        self.code = code
        super().__init__(f"Missing required constraint: {code}")

class ValidationError(ParserError):
    """Raised when validation fails."""
    def __init__(self, message: str):
        super().__init__(message)

@dataclass
class ParsedDomainSpecification:
    """Validated and parsed domain specification."""
    domain_name: str
    business_type: BusinessType
    complexity: Complexity
    change_rate: ChangeRate
    stakes: Stakes
    configuration_inputs: List[ConfigurationInput]
    hard_constraints: Dict[str, HardConstraint]
    success_criteria: SuccessCriteria
    feedback_mechanisms: FeedbackMechanism
    operational_context: OperationalContext
    raw_spec: DomainSpecification

class DomainSpecificationParser:
    """
    Parses and validates domain specifications.
    
    This module implements the first stage of the generation pipeline,
    transforming raw domain specifications into validated intermediate
    representations.
    """
    
    def __init__(self):
        self.required_fields = [
            'domain_name',
            'operational_context',
            'hard_constraints',
            'success_criteria',
            'feedback_mechanisms'
        ]
        self.universal_constraints = ['HC_001', 'HC_002', 'HC_003', 'HC_004']
    
    def parse(self, raw_spec: DomainSpecification) -> ParsedDomainSpecification:
        """
        Parse and validate a domain specification.
        
        Args:
            raw_spec: The raw domain specification to parse
            
        Returns:
            ParsedDomainSpecification: The validated intermediate representation
            
        Raises:
            ParserError: If validation fails
        """
        # Step 1: Validate required fields
        self._validate_required_fields(raw_spec)
        
        # Step 2: Validate hard constraints
        self._validate_constraints(raw_spec)
        
        # Step 3: Validate success criteria
        self._validate_success_criteria(raw_spec)
        
        # Step 4: Classify domain
        business_type = self._classify_business_type(raw_spec)
        complexity = self._assess_complexity(raw_spec)
        change_rate = self._assess_change_rate(raw_spec)
        stakes = self._assess_stakes(raw_spec)
        
        # Step 5: Build intermediate representation
        return ParsedDomainSpecification(
            domain_name=raw_spec.domain_name,
            business_type=business_type,
            complexity=complexity,
            change_rate=change_rate,
            stakes=stakes,
            configuration_inputs=raw_spec.configuration_inputs,
            hard_constraints=raw_spec.hard_constraints,
            success_criteria=raw_spec.success_criteria,
            feedback_mechanisms=raw_spec.feedback_mechanisms,
            operational_context=raw_spec.operational_context,
            raw_spec=raw_spec
        )
    
    def _validate_required_fields(self, spec: DomainSpecification):
        """Validate all required fields are present."""
        for field in self.required_fields:
            if not hasattr(spec, field) or getattr(spec, field) is None:
                raise MissingFieldError(field)
    
    def _validate_constraints(self, spec: DomainSpecification):
        """Validate hard constraint definitions."""
        constraints = spec.hard_constraints
        
        for code in self.universal_constraints:
            if code not in constraints:
                raise MissingConstraintError(code)
            
            constraint = constraints[code]
            if not hasattr(constraint, 'code') or not hasattr(constraint, 'definition'):
                raise ValidationError(
                    f"Constraint {code} missing required properties"
                )
    
    def _validate_success_criteria(self, spec: DomainSpecification):
        """Validate success criteria values."""
        criteria = spec.success_criteria
        
        if not 0 <= criteria.generation_success_rate <= 1:
            raise ValidationError("generation_success_rate must be 0-1")
        
        if not 0 <= criteria.constraint_satisfaction <= 1:
            raise ValidationError("constraint_satisfaction must be 0-1")
    
    def _classify_business_type(self, spec: DomainSpecification) -> BusinessType:
        """Classify domain into appropriate business type."""
        business = spec.operational_context.business_type.lower()
        
        if 'restaurant' in business or 'food' in business:
            return BusinessType.RESTAURANT
        elif 'manufacturing' in business or 'production' in business:
            return BusinessType.MANUFACTURING
        elif 'healthcare' in business or 'medical' in business:
            return BusinessType.HEALTHCARE
        elif 'service' in business:
            return BusinessType.SERVICE_OPERATIONS
        else:
            return BusinessType.GENERIC_OPERATIONS
    
    def _assess_complexity(self, spec: DomainSpecification) -> Complexity:
        """Assess operational complexity."""
        score = 0
        
        # Multiple service periods
        if '-' in spec.operational_context.operational_hours:
            score += 1
        
        # Multiple configuration inputs indicate more complexity
        if len(spec.configuration_inputs) > 5:
            score += 1
        
        # Multiple constraints indicate more complexity
        if len(spec.hard_constraints) > 4:
            score += 1
        
        if score <= 1:
            return Complexity.SIMPLE
        elif score <= 2:
            return Complexity.MODERATE
        else:
            return Complexity.COMPLEX
    
    def _assess_change_rate(self, spec: DomainSpecification) -> ChangeRate:
        """Assess rate of change in the domain."""
        # Default to medium for most domains
        return ChangeRate.MEDIUM
    
    def _assess_stakes(self, spec: DomainSpecification) -> Stakes:
        """Assess stakes of the domain (cost of errors)."""
        # Healthcare and manufacturing typically have higher stakes
        if spec.operational_context.business_type.lower() in [
            'healthcare', 'medical', 'manufacturing', 'production'
        ]:
            return Stakes.HIGH
        # Restaurants have medium stakes (food safety)
        elif spec.operational_context.business_type.lower() in [
            'restaurant', 'food'
        ]:
            return Stakes.HIGH  # Food safety is high stakes
        else:
            return Stakes.MEDIUM
```

### B. Pattern Selector

```python
@dataclass
class DomainClassification:
    """Classification of a domain by key characteristics."""
    business_type: BusinessType
    complexity: Complexity
    change_rate: ChangeRate
    stakes: Stakes

@dataclass
class PatternSelection:
    """Result of pattern selection."""
    architecture_pattern: Dict[str, Any]
    constraint_patterns: List[Dict[str, Any]]
    feedback_pattern: Dict[str, Any]
    interface_pattern: Dict[str, Any]
    domain_classification: DomainClassification

class IncompatiblePatternsError(Exception):
    """Raised when selected patterns are incompatible."""
    pass

class PatternSelector:
    """
    Selects appropriate constructor patterns based on domain characteristics.
    
    This module implements the second stage of the generation pipeline,
    selecting patterns from the pattern library that are appropriate for
    the target domain.
    """
    
    def __init__(self, pattern_library, effectiveness_tracker):
        self.pattern_library = pattern_library
        self.effectiveness = effectiveness_tracker
    
    def select(self, parsed_spec: ParsedDomainSpecification) -> PatternSelection:
        """
        Select appropriate patterns for the domain specification.
        
        Args:
            parsed_spec: The parsed domain specification
            
        Returns:
            PatternSelection: The selected patterns
        """
        # Step 1: Classify domain
        classification = self._classify_domain(parsed_spec)
        
        # Step 2: Filter applicable patterns
        applicable = self._filter_applicable(classification)
        
        # Step 3: Score patterns
        scored = self._score_patterns(applicable, parsed_spec)
        
        # Step 4: Select optimal set
        selected = self._select_optimal_set(scored)
        
        # Step 5: Validate compatibility
        self._validate_compatibility(selected, classification)
        
        return PatternSelection(
            architecture_pattern=selected['architecture'][0] if selected['architecture'] else None,
            constraint_patterns=selected['constraint'],
            feedback_pattern=selected['feedback'][0] if selected['feedback'] else None,
            interface_pattern=selected['interface'][0] if selected['interface'] else None,
            domain_classification=classification
        )
    
    def _classify_domain(self, spec: ParsedDomainSpecification) -> DomainClassification:
        """Classify domain by characteristics."""
        return DomainClassification(
            business_type=spec.business_type,
            complexity=spec.complexity,
            change_rate=spec.change_rate,
            stakes=spec.stakes
        )
    
    def _filter_applicable(self, classification: DomainClassification) -> Dict[str, List]:
        """Filter patterns by domain applicability."""
        applicable = {
            'architecture': [],
            'constraint': [],
            'feedback': [],
            'interface': []
        }
        
        # Filter architecture patterns
        for pattern in self.pattern_library.architecture_patterns:
            if self._is_applicable(pattern, classification):
                applicable['architecture'].append(pattern)
        
        # Filter constraint patterns
        for pattern in self.pattern_library.constraint_patterns:
            if self._is_applicable(pattern, classification):
                applicable['constraint'].append(pattern)
        
        # Filter feedback patterns
        for pattern in self.pattern_library.feedback_patterns:
            if self._is_applicable(pattern, classification):
                applicable['feedback'].append(pattern)
        
        # Filter interface patterns
        for pattern in self.pattern_library.interface_patterns:
            if self._is_applicable(pattern, classification):
                applicable['interface'].append(pattern)
        
        return applicable
    
    def _is_applicable(self, pattern: Dict, classification: DomainClassification) -> bool:
        """Check if pattern applies to domain classification."""
        applicability = pattern.get('applicability', '')
        
        # Universal applicability
        if applicability == 'universal' or applicability == 'all_constructors':
            return True
        
        # Check business type match
        if classification.business_type.value in str(applicability).lower():
            return True
        
        # Check complexity match
        if hasattr(applicability, 'complexity'):
            if applicability.complexity != classification.complexity.value:
                return False
        
        return True
    
    def _score_patterns(
        self, 
        applicable: Dict[str, List], 
        spec: ParsedDomainSpecification
    ) -> Dict[str, List]:
        """Score patterns by relevance."""
        scored = {k: [] for k in applicable}
        
        for category, patterns in applicable.items():
            for pattern in patterns:
                # Base relevance score
                relevance = self._calculate_relevance(pattern, spec)
                
                # Effectiveness adjustment
                effectiveness = self.effectiveness.get_effectiveness(
                    pattern.get('name', '')
                )
                
                # Combined score
                score = relevance * (1 + effectiveness * 0.5)
                scored[category].append((pattern, score))
        
        return scored
    
    def _calculate_relevance(self, pattern: Dict, spec: ParsedDomainSpecification) -> float:
        """Calculate relevance score for pattern-spec pair."""
        score = 0.0
        
        applicability = pattern.get('applicability', '')
        
        # Direct applicability bonus
        if applicability in ['universal', 'all_constructors']:
            score += 0.3
        elif spec.business_type.value in str(applicability).lower():
            score += 0.7
        else:
            score += 0.1
        
        # Completeness bonus
        completeness = pattern.get('completeness_score', 0.5)
        score += 0.2 * completeness
        
        return min(score, 1.0)
    
    def _select_optimal_set(self, scored: Dict[str, List]) -> Dict[str, List]:
        """Select optimal set of patterns."""
        selected = {}
        
        # Always select universal patterns first
        for category, patterns in scored.items():
            for pattern, score in patterns:
                applicability = pattern.get('applicability', '')
                if applicability in ['universal', 'all_constructors']:
                    selected[category] = [(pattern, score)]
                    break
        
        # Then select domain-specific patterns
        for category, patterns in scored.items():
            domain_specific = [
                (p, s) for p, s in patterns
                if p.get('applicability') not in ['universal', 'all_constructors']
                and p not in [pp for pp, _ in selected.get(category, [])]
            ]
            
            if domain_specific:
                best = max(domain_specific, key=lambda x: x[1])
                if category in selected:
                    selected[category].append(best)
                else:
                    selected[category] = [best]
        
        return selected
    
    def _validate_compatibility(
        self, 
        selected: Dict[str, List], 
        classification: DomainClassification
    ):
        """Validate selected patterns are mutually compatible."""
        # High-stakes domains should use conservative feedback
        if classification.stakes == Stakes.HIGH:
            feedback_pattern = selected.get('feedback', [None])[0]
            if feedback_pattern and feedback_pattern.get('name') == 'Rapid Iteration Feedback':
                # Warning: High-stakes