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
