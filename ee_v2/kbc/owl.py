"""owl.py — THE OWL PROJECTION (Isaac 2026-08-10: "PSC with OWL inside").

The gate stays Prolog — residue-naming is closed-world negation (\\+), which
OWL's open-world semantics cannot express (absence of an axiom is unknown,
never false; this is why the RDF world needed SHACL for validation). So the
resolution is PSC-with-OWL-PROJECTED: every certified KB exports a
self-contained Turtle document. From the outside the system IS OWL-bearing —
triple stores, SPARQL, Protégé all read it; the proofs stay Prolog inside.

Mapping (deliberately modest — no fake semantics):
  concept        → owl:NamedIndividual, typed kbo:Concept,
                   rdfs:label (words) + rdfs:comment (the definition)
  relation (s,t) → kb:s kbo:relatesTo kb:t         (relations are untyped
                   in the KB; projecting them as subclass axioms would
                   CLAIM taxonomy we never proved — so we don't)
  hyperedge      → a kbo:Certificate individual, kbo:binds each member
                   (the certificate ledger, reified)
  skeleton edge  → kbo:because / kbo:since / kbo:togetherFit /
                   kbo:explains object-property assertions (the certified
                   argument DAGs — the one place edges HAVE types)

Cross-KB linking happens at the ATLAS layer: every module shares the kbo:
core namespace, and same-name atoms across modules are surfaced as
CANDIDATE bridges (never owl:sameAs — same word is not same concept until
someone proves it)."""
from __future__ import annotations

import json
import re
from pathlib import Path

DEFAULT_BASE = "https://sancovp.github.io/kb-atlas/ns"
ARG_PROPS = {"because": "because", "since": "since",
             "together_fit": "togetherFit", "explains": "explains"}


def _slug(x: str) -> str:
    return re.sub(r"[^a-z0-9_]+", "_", x.strip().lower()).strip("_")[:48]


def _lit(x: str) -> str:
    return json.dumps(str(x))          # valid Turtle double-quoted literal


def project_owl(kb, out_path, base: str = DEFAULT_BASE) -> dict:
    """Emit the KB as one self-contained Turtle file. Reads the certificate
    ledgers from kb.root when present. Returns emission counts."""
    slug = _slug(kb.subject)
    lines = [
        f"@prefix kb: <{base}/{slug}#> .",
        f"@prefix kbo: <{base}/core#> .",
        "@prefix owl: <http://www.w3.org/2002/07/owl#> .",
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
        "",
        f"<{base}/{slug}> a owl:Ontology ;",
        f"    rdfs:label {_lit(kb.subject)} ;",
        f"    rdfs:comment {_lit('Machine-grown, Prolog-gate-admitted knowledge module. The gate proves coherence, not truth.')} .",
        "",
        "# the tiny core vocabulary (self-contained on purpose)",
        "kbo:Concept a owl:Class .",
        "kbo:Certificate a owl:Class .",
        "kbo:relatesTo a owl:ObjectProperty .",
        "kbo:binds a owl:ObjectProperty .",
    ]
    for p in ARG_PROPS.values():
        lines.append(f"kbo:{p} a owl:ObjectProperty .")
    lines.append("")

    for c, d in sorted(kb.concepts.items()):
        lines += [f"kb:{c} a owl:NamedIndividual, kbo:Concept ;",
                  f"    rdfs:label {_lit(c.replace('_', ' '))} ;",
                  f"    rdfs:comment {_lit(d)} ."]
    lines.append("")

    n_rel = 0
    for s, t in sorted(kb.relations):
        if s in kb.concepts or t in kb.concepts:
            lines.append(f"kb:{s} kbo:relatesTo kb:{t} .")
            n_rel += 1
    lines.append("")

    n_cert = 0
    hyper = Path(kb.root) / "hyperedges.jsonl"
    if hyper.exists():
        for i, line in enumerate(hyper.read_text().splitlines()):
            h = json.loads(line)
            members = ", ".join(f"kb:{a}" for a in h["atoms"])
            lines.append(f"kb:certificate_{i} a kbo:Certificate ; "
                         f"kbo:binds {members} .")
            n_cert += 1
        lines.append("")

    n_arg = 0
    skel = Path(kb.root) / "skeletons.jsonl"
    if skel.exists():
        for line in skel.read_text().splitlines():
            sk = json.loads(line)
            for op, s, t in sk["edges"]:
                if op in ARG_PROPS:
                    lines.append(f"kb:{s} kbo:{ARG_PROPS[op]} kb:{t} .")
                    n_arg += 1
        lines.append("")

    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return {"path": str(out_path), "concepts": len(kb.concepts),
            "relations": n_rel, "certificates": n_cert,
            "argument_edges": n_arg}


__all__ = ["project_owl", "DEFAULT_BASE"]
