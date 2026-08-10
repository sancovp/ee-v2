"""The EE ontology gate — a P1 emission as a TYPED CONSTRUCTION (MAP v2 PSC
boundary) instead of a prose blob.

The neurosymbolic experiment: P1 (Conceptualize) claims an ontology. PSC
proves the LOCAL shape (unique ids, well-formed atoms); Prolog proves what
pydantic can't — CLOSURE (no relation touches an undeclared concept) and
CONNECTEDNESS (no orphan concepts). ONT certificate ⇒ the pass is PROVEN
coherent; SOUP ⇒ the residue NAMES exactly what's dangling/orphaned — the
retry signal, for free.

Authority split (the MAP law): the SEAT may only author candidate_* facts;
the JOURNEY ENGINE (the trusted observer — it watched the pass complete)
authors source_* facts. A seat cannot witness itself.
"""
from __future__ import annotations

from typing import Annotated, Literal

from pydantic import Field, field_validator
from pydantic_stack_core import RenderablePiece

Atom = Annotated[str, Field(pattern=r"^[a-z][a-zA-Z0-9_]*$")]


class Concept(RenderablePiece):
    kind: Literal["concept"]
    id: Atom
    definition: str = Field(min_length=8)

    def render(self) -> str:
        return f"{self.id}: {self.definition}"


class Relation(RenderablePiece):
    kind: Literal["relation"]
    id: Atom
    source: Atom
    target: Atom

    def render(self) -> str:
        return f"{self.id}: {self.source} -> {self.target}"


class OntologyConstruction(RenderablePiece):
    kind: Literal["ee_ontology"]
    subject: Atom
    concepts: list[Concept] = Field(min_length=1)
    relations: list[Relation] = Field(min_length=1)

    @field_validator("concepts")
    @classmethod
    def unique_concepts(cls, v):
        ids = [c.id for c in v]
        if len(ids) != len(set(ids)):
            raise ValueError("concept ids must be unique")
        return v

    @field_validator("relations")
    @classmethod
    def unique_relations(cls, v):
        ids = [r.id for r in v]
        if len(ids) != len(set(ids)):
            raise ValueError("relation ids must be unique")
        return v

    def render(self) -> str:
        return (f"ontology:{self.subject}\n"
                + "\n".join(c.render() for c in self.concepts)
                + "\n" + "\n".join(r.render() for r in self.relations))


class EEOntologyAdapter:
    target = "ee_ontology"
    schema_id = "ee.map.ontology.v1"
    lowering_id = "ee.map.ontology.lowering.v1"
    model_type = OntologyConstruction
    candidate_predicates = frozenset({"candidate_concept",
                                      "candidate_relation"})

    def lower(self, construction: RenderablePiece) -> list[str]:
        if not isinstance(construction, OntologyConstruction):
            raise TypeError("EEOntologyAdapter requires OntologyConstruction")
        facts = [f"candidate_concept({construction.subject},{c.id})."
                 for c in construction.concepts]
        facts += [f"candidate_relation({construction.subject},{r.id},"
                  f"{r.source},{r.target})."
                  for r in construction.relations]
        return facts


class PassWitness(RenderablePiece):
    kind: Literal["pass_witness"]
    subject: Atom
    layer: int = Field(ge=0)
    pass_num: int = Field(ge=1, le=3)

    def render(self) -> str:
        return f"witness:{self.subject}:L{self.layer}P{self.pass_num}"


class EEPassObservationAdapter:
    """The JOURNEY ENGINE's authority: it observed the pass's phase files all
    exist (the traversability law) — only then do candidates derive."""
    target = "ee_ontology"
    schema_id = "ee.map.pass_witness.v1"
    lowering_id = "ee.map.pass_witness.lowering.v1"
    model_type = PassWitness
    observation_predicates = frozenset({"source_pass_complete"})

    def lower(self, observation: RenderablePiece) -> list[str]:
        if not isinstance(observation, PassWitness):
            raise TypeError("EEPassObservationAdapter requires PassWitness")
        return [f"source_pass_complete({observation.subject})."]


# ── P2: the SKILL construction — cross-pass fortification ────────────────────
# A skill's steps must GROUND in P1's CERTIFIED concepts. The engine (holding
# P1's certificate) is the observation authority for what "certified" means.

class SkillStep(RenderablePiece):
    kind: Literal["step"]
    id: Atom
    action: str = Field(min_length=8)
    uses: list[Atom] = Field(min_length=1)

    def render(self) -> str:
        return f"{self.id}: {self.action} [uses: {', '.join(self.uses)}]"


class SkillConstruction(RenderablePiece):
    kind: Literal["ee_skill"]
    subject: Atom
    name: Atom
    steps: list[SkillStep] = Field(min_length=1)

    @field_validator("steps")
    @classmethod
    def unique_steps(cls, v):
        ids = [s.id for s in v]
        if len(ids) != len(set(ids)):
            raise ValueError("step ids must be unique")
        return v

    def render(self) -> str:
        return (f"skill:{self.name}\n"
                + "\n".join(s.render() for s in self.steps))


class EESkillAdapter:
    target = "ee_skill"
    schema_id = "ee.map.skill.v1"
    lowering_id = "ee.map.skill.lowering.v1"
    model_type = SkillConstruction
    candidate_predicates = frozenset({"candidate_step", "candidate_use"})

    def lower(self, construction: RenderablePiece) -> list[str]:
        if not isinstance(construction, SkillConstruction):
            raise TypeError("EESkillAdapter requires SkillConstruction")
        facts = []
        for s in construction.steps:
            facts.append(f"candidate_step({construction.subject},{s.id}).")
            facts += [f"candidate_use({construction.subject},{s.id},{c})."
                      for c in s.uses]
        return facts


class SkillGroundWitness(RenderablePiece):
    """The ENGINE's authority: the concepts P1 CERTIFIED (read from the
    stored ONT certificate — the trust root), plus the pass witness."""
    kind: Literal["skill_ground_witness"]
    subject: Atom
    certified_concepts: list[Atom] = Field(min_length=1)

    def render(self) -> str:
        return f"ground:{self.subject}:{','.join(self.certified_concepts)}"


class EESkillObservationAdapter:
    target = "ee_skill"
    schema_id = "ee.map.skill_ground.v1"
    lowering_id = "ee.map.skill_ground.lowering.v1"
    model_type = SkillGroundWitness
    observation_predicates = frozenset({"source_concept",
                                        "source_pass_complete"})

    def lower(self, observation: RenderablePiece) -> list[str]:
        if not isinstance(observation, SkillGroundWitness):
            raise TypeError("EESkillObservationAdapter requires "
                            "SkillGroundWitness")
        facts = [f"source_concept({observation.subject},{c})."
                 for c in observation.certified_concepts]
        facts.append(f"source_pass_complete({observation.subject}).")
        return facts


# ── §24c: the ARGUMENT SKELETON — the algebra of articulation ────────────────
# A hyperedge holds a claim as an unordered proven set; the skeleton is the
# DAG that orders it into walkability. Operator edges are higher-order (they
# relate claims/atoms); each `because` implies its templated warrant subgraph
# — dischargeable obligations in domains/ee_argument. THE OBSERVATION
# AUTHORITY is the certificate ledger: only atoms already certified may be
# spoken (articulation demands certification first).

ArgOp = Literal["because", "since", "together_fit", "explains"]


class ArgEdge(RenderablePiece):
    kind: Literal["arg"]
    id: Atom
    op: ArgOp
    source: Atom
    target: Atom

    def render(self) -> str:
        return f"{self.id}: {self.source} -{self.op}-> {self.target}"


class ArgumentSkeleton(RenderablePiece):
    kind: Literal["ee_argument"]
    subject: Atom
    root: Atom
    edges: list[ArgEdge] = Field(min_length=1)

    @field_validator("edges")
    @classmethod
    def unique_edges(cls, v):
        ids = [e.id for e in v]
        if len(ids) != len(set(ids)):
            raise ValueError("arg edge ids must be unique")
        return v

    def render(self) -> str:
        return (f"argument:{self.root}\n"
                + "\n".join(e.render() for e in self.edges))


class EEArgumentAdapter:
    target = "ee_argument"
    schema_id = "ee.map.argument.v1"
    lowering_id = "ee.map.argument.lowering.v1"
    model_type = ArgumentSkeleton
    candidate_predicates = frozenset({"candidate_root", "candidate_arg"})

    def lower(self, construction: RenderablePiece) -> list[str]:
        if not isinstance(construction, ArgumentSkeleton):
            raise TypeError("EEArgumentAdapter requires ArgumentSkeleton")
        facts = [f"candidate_root({construction.subject},"
                 f"{construction.root})."]
        facts += [f"candidate_arg({construction.subject},{e.id},{e.op},"
                  f"{e.source},{e.target})."
                  for e in construction.edges]
        return facts


class ArgumentGroundWitness(RenderablePiece):
    """The CERTIFICATE LEDGER's authority: the atoms the hyperedge store has
    certified — the only vocabulary a skeleton may speak."""
    kind: Literal["argument_ground_witness"]
    subject: Atom
    certified_atoms: list[Atom] = Field(min_length=1)

    def render(self) -> str:
        return f"ground:{self.subject}:{','.join(self.certified_atoms)}"


class EEArgumentObservationAdapter:
    target = "ee_argument"
    schema_id = "ee.map.argument_ground.v1"
    lowering_id = "ee.map.argument_ground.lowering.v1"
    model_type = ArgumentGroundWitness
    observation_predicates = frozenset({"source_concept",
                                        "source_pass_complete"})

    def lower(self, observation: RenderablePiece) -> list[str]:
        if not isinstance(observation, ArgumentGroundWitness):
            raise TypeError("EEArgumentObservationAdapter requires "
                            "ArgumentGroundWitness")
        facts = [f"source_concept({observation.subject},{c})."
                 for c in observation.certified_atoms]
        facts.append(f"source_pass_complete({observation.subject}).")
        return facts
