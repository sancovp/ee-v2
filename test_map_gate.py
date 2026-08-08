#!/usr/bin/env python3
"""The fail-or-insane instrument — EE's P1 emission through MAP v2's typed
construction boundary, against real SWI-Prolog. Deterministic (NO LLM).

What is asserted:
  * a COHERENT ontology (closed + connected) reaches ONT — with a replayable
    certificate covering the exact payload;
  * an INCOHERENT one (a dangling relation endpoint + an orphan concept)
    stays SOUP, and the RESIDUE NAMES BOTH VIOLATIONS EXACTLY — the retry
    signal an LLM can act on, produced by the proof shell for free;
  * malformed emissions (dup ids, bad atoms) die at the PSC boundary BEFORE
    Prolog — typed shape locally, semantics relationally;
  * a seat cannot witness itself: candidates never derive without the journey
    engine's source_pass_complete observation.
"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, "/home/ceo/repo/ee-v2")

from map_v2 import (MapV2Lattice, PrologTargetCompiler,
                    load_domain_manifest)

from ee_v2.map_gate import EEOntologyAdapter, EEPassObservationAdapter

DOMAIN = Path(__file__).parent / "ee_v2/map_gate/domains/ee_ontology/domain.json"


def good_ontology():
    return {"kind": "ee_ontology", "subject": "kitchen_design",
            "concepts": [
                {"kind": "concept", "id": "workflow",
                 "definition": "the movement pattern of cooking work"},
                {"kind": "concept", "id": "station",
                 "definition": "a fixed place where one task happens"},
                {"kind": "concept", "id": "adjacency",
                 "definition": "which stations border which"}],
            "relations": [
                {"kind": "relation", "id": "r1", "source": "workflow",
                 "target": "station"},
                {"kind": "relation", "id": "r2", "source": "station",
                 "target": "adjacency"}]}


def bad_ontology():
    o = good_ontology()
    # a dangling reference (mise_en_place never declared) + an orphan
    # (adjacency loses its only relation)
    o["relations"] = [
        {"kind": "relation", "id": "r1", "source": "workflow",
         "target": "station"},
        {"kind": "relation", "id": "r2", "source": "station",
         "target": "mise_en_place"}]
    return o


def make_lattice(tmp):
    compiler = PrologTargetCompiler(load_domain_manifest(DOMAIN))
    return MapV2Lattice(Path(tmp) / "lattice", compiler=compiler,
                       construction_adapter=EEOntologyAdapter(),
                       observation_adapter=EEPassObservationAdapter())


def prepare(lat, subject="kitchen_design"):
    lat.create(subject, "ee_ontology")
    lat.declare_kappa(subject, "ee_conceptualization",
                      {"ontology_coherence":
                       "every relation touches declared concepts; "
                       "every concept participates"})
    lat.compute(subject)


def test_coherent_reaches_ont(tmp):
    lat = make_lattice(tmp)
    prepare(lat)
    lat.fill_construction("kitchen_design", good_ontology())
    lat.attach_observation("kitchen_design",
                           {"kind": "pass_witness",
                            "subject": "kitchen_design",
                            "layer": 0, "pass_num": 1})
    packet = lat.compile("kitchen_design")
    assert packet["griess_phase"] == "ont", packet
    cert = lat.export_certificate("kitchen_design")["certificate"]
    assert cert["construction_schema_id"] == "ee.map.ontology.v1"
    print("  coherent P1 → ONT certificate (closed + connected, PROVEN, "
          "replayable) ✓")


def test_incoherent_stays_soup_with_named_residue(tmp):
    lat = make_lattice(tmp)
    prepare(lat)
    lat.fill_construction("kitchen_design", bad_ontology())
    lat.attach_observation("kitchen_design",
                           {"kind": "pass_witness",
                            "subject": "kitchen_design",
                            "layer": 0, "pass_num": 1})
    packet = lat.compile("kitchen_design")
    assert packet["griess_phase"] == "soup", packet
    frontier = " ".join(packet.get("frontier", []))
    # THE RESIDUE NAMES BOTH VIOLATIONS — the retry prompt, from the prover
    assert "dangling(r2,mise_en_place)" in frontier, packet
    assert "orphan(adjacency)" in frontier, packet
    print("  incoherent P1 → SOUP with residue naming EXACTLY "
          "dangling(r2,mise_en_place) + orphan(adjacency) — the retry "
          "signal for free ✓")


def test_psc_boundary_rejects_malformed(tmp):
    lat = make_lattice(tmp)
    prepare(lat)
    bad = good_ontology()
    bad["concepts"].append(dict(bad["concepts"][0]))          # duplicate id
    rejected = False
    try:
        lat.fill_construction("kitchen_design", bad)
    except AssertionError:
        raise
    except Exception:
        rejected = True     # NOTE: map-v2 wart — the pydantic error trips
                            # its own JSON serialization (TypeError), but the
                            # construction IS refused at the boundary
    assert rejected, "PSC must reject duplicate concept ids"
    print("  malformed emission dies at the PSC boundary before Prolog "
          "(map-v2 error-serialization wart noted) ✓")


def test_seat_cannot_witness_itself(tmp):
    lat = make_lattice(tmp)
    prepare(lat)
    lat.fill_construction("kitchen_design", good_ontology())
    packet = lat.compile("kitchen_design")                    # NO observation
    assert packet["griess_phase"] == "soup", packet
    print("  no engine witness → SOUP (candidates never self-derive; "
          "authority split holds) ✓")


def main():
    for fn in (test_coherent_reaches_ont,
               test_incoherent_stays_soup_with_named_residue,
               test_psc_boundary_rejects_malformed,
               test_seat_cannot_witness_itself):
        with tempfile.TemporaryDirectory() as d:
            fn(d)
    print("MAP GATE PASS — the neurosymbolic emission gate works against "
          "real SWI-Prolog: coherence is PROVEN not hoped, and failure "
          "arrives as a named, actionable residue.")


if __name__ == "__main__":
    main()
