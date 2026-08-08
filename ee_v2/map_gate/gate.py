"""
gate.py — the neurosymbolic emission gauge, wired.

    MapGate.check(journey, layer, pass_num, payload)
        → {"ont": bool, "frontier": [...], "certificate": ...}

RUN THE SEAT UNTIL THE DSL GOES ONT: the topology's emission node calls this
gauge; SOUP's frontier feeds the retry prompt (the prover writes the
correction); only ONT lets the emission file come to exist — so the
traversability law ("state moves when the file exists") and the proof law
("state moves when proven") become the same law.

Authority chain: the engine witnesses a pass only after ALL its phase files
exist (checked here, not assumed); P2's ground truth is P1's STORED ONT
CERTIFICATE (the trust root) — certified concepts are lowered as source_*
facts by the engine, never by the seat.
"""
from __future__ import annotations

import json
import tempfile
from pathlib import Path
from typing import Optional

from map_v2 import MapV2Lattice, PrologTargetCompiler, load_domain_manifest

from .adapter import (EEOntologyAdapter, EEPassObservationAdapter,
                      EESkillAdapter, EESkillObservationAdapter)

_DOMAINS = Path(__file__).resolve().parent / "domains"

# which pass emissions are gated, and with what
_TARGETS = {
    1: dict(domain=_DOMAINS / "ee_ontology" / "domain.json",
            construction=EEOntologyAdapter, observation=EEPassObservationAdapter,
            kappa=("ee_conceptualization",
                   {"ontology_coherence":
                    "every relation touches declared concepts; "
                    "every concept participates"})),
    2: dict(domain=_DOMAINS / "ee_skill" / "domain.json",
            construction=EESkillAdapter, observation=EESkillObservationAdapter,
            kappa=("ee_generalization",
                   {"skill_grounding":
                    "every step's uses reference P1-certified concepts"})),
}

N_PHASES = 7


class MapGate:
    """Stateless per check: each emission gets a fresh lattice; the durable
    truth is the certificate the JOURNEY stores. (§R Option A — ruled.)"""

    gated_passes = frozenset(_TARGETS)
    max_attempts = 3            # bounded retries; then fail-closed halt

    def subject_for(self, journey, layer: int, pass_num: int) -> str:
        return f"j_l{layer}_p{pass_num}"

    def payload_from_emission(self, pass_num: int, emission: dict) -> dict:
        """Seat JSON → typed construction payload. The ENGINE stamps the
        pydantic discriminator kinds so the seat has less shape to get wrong;
        everything semantic stays the seat's claim."""
        if pass_num == 1:
            return {"kind": "ee_ontology",
                    "concepts": [{**c, "kind": "concept"}
                                 for c in emission.get("concepts", [])],
                    "relations": [{**r, "kind": "relation"}
                                  for r in emission.get("relations", [])]}
        name = emission.get("name", "skill")
        if not name[:1].isalpha():
            name = f"s_{name}"
        return {"kind": "ee_skill", "name": name,
                "steps": [{**s, "kind": "step"}
                          for s in emission.get("steps", [])]}

    def _witness_payload(self, journey, layer: int, pass_num: int,
                         subject: str) -> Optional[dict]:
        # THE ENGINE'S WITNESS: all 7 phase files must actually exist
        if len(journey.pass_artifacts(layer, pass_num)) < N_PHASES:
            return None
        if pass_num == 1:
            return {"kind": "pass_witness", "subject": subject,
                    "layer": layer, "pass_num": pass_num}
        # P2: ground truth = P1's STORED certificate (the trust root)
        cert_path = journey.node_path(layer, 1, None).parent / "certificate.json"
        if not cert_path.exists():
            return None
        envelope = json.loads(cert_path.read_text())
        payload = envelope.get("proof_context", {}) \
                          .get("construction", {}).get("payload", {})
        concepts = [c["id"] for c in payload.get("concepts", [])]
        if not concepts:
            return None
        return {"kind": "skill_ground_witness", "subject": subject,
                "certified_concepts": concepts}

    def check(self, journey, layer: int, pass_num: int,
              construction_payload: dict) -> dict:
        spec = _TARGETS[pass_num]
        subject = self.subject_for(journey, layer, pass_num)
        construction_payload = dict(construction_payload)
        construction_payload["subject"] = subject       # engine-owned subject
        witness = self._witness_payload(journey, layer, pass_num, subject)
        if witness is None:
            return {"ont": False, "certificate": None,
                    "frontier": ["engine_witness_refused(pass_incomplete_or_"
                                 "missing_p1_certificate)"]}
        with tempfile.TemporaryDirectory(prefix="ee-map-") as td:
            compiler = PrologTargetCompiler(
                load_domain_manifest(spec["domain"]))
            lat = MapV2Lattice(Path(td) / "lattice", compiler=compiler,
                              construction_adapter=spec["construction"](),
                              observation_adapter=spec["observation"]())
            target = compiler.domain.targets[0]
            lat.create(subject, target)
            kd, inv = spec["kappa"]
            lat.declare_kappa(subject, kd, inv)
            lat.compute(subject)
            try:
                lat.fill_construction(subject, construction_payload)
            except Exception as exc:
                # PSC boundary rejection = SOUP with the pydantic residue as
                # the frontier (map-v2 ceo branch carries the serialization
                # fix, so the message is the real violation, not a TypeError)
                return {"ont": False, "certificate": None,
                        "frontier": [f"psc_rejected: {exc}"]}
            lat.attach_observation(subject, witness)
            packet = lat.compile(subject)
            ont = packet.get("griess_phase") == "ont"
            cert = (lat.export_certificate(subject) if ont else None)
            return {"ont": ont, "certificate": cert,
                    "frontier": list(packet.get("frontier", []))}


__all__ = ["MapGate"]
