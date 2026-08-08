"""
journey.py — THE DIR IS THE STATE MACHINE.

ee-v1's state was a counter in /tmp; the structure it guided was unmanaged.
Here the journey directory is laid BY THE ENGINE (the agent can't wreck what
it doesn't lay out), and position/resume/memory are all DERIVED from what
exists on disk — no counter anywhere:

    journey/
    ├── domain.md                     the run's domain
    ├── L{0,1,2}/P{1,2,3}/
    │   ├── 0-abstractgoal.md … 6-feedbackloop.md    (node artifacts)
    │   └── emission.json                            (the pass's distillate)
    ├── rules/<name>.md               P1 emissions — what was LEARNED (RULE-1:
    │                                 knowledge auto-loads into later contexts)
    ├── skills/<name>/SKILL.md        P2 emissions — the CONSTRUCTOR (invokable)
    └── artifacts/<name>.md           P3 emissions — the INSTANCE

position() = the first node whose file is missing ⇒ resume is free (the dir
is the memo). rules_so_far() = the progressive-disclosure feed.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

_HERE = Path(__file__).resolve().parent
PAYLOADS = json.loads((_HERE / "frozen_payloads.json").read_text())
PHASE_NAMES: Dict[str, str] = PAYLOADS["phase_names"]
PASS_NAMES: Dict[str, str] = PAYLOADS["pass_names"]

# The expanded-run layer frames — VERBATIM cells from the frozen table
# (emergence-engine README, "The Traditional Expanded Run 9-Pass Structure").
LAYER_FRAMES = {
    0: {"name": "L0: Conceptualize",
        1: 'What IS "What IS it?"', 2: 'How DETERMINE "What IS it?"',
        3: "Determine what THIS IS"},
    1: {"name": "L1: Generally Reify",
        1: 'What IS "system building?"', 2: "How BUILD systems that BUILD?",
        3: "Build THIS architecture"},
    2: {"name": "L2: Specifically Reify",
        1: 'What IS "this implementation?"', 2: "How BUILD implementations?",
        3: "Build THIS generator"},
}

LAYERS = (0, 1, 2)
PASSES = (1, 2, 3)
PHASES = (0, 1, 2, 3, 4, 5, 6)
EMISSION_KIND = {1: "rule", 2: "skill", 3: "artifact"}


def node_filename(phase: int) -> str:
    return f"{phase}-{PHASE_NAMES[str(phase)].lower()}.md"


def notation(layer: int, pass_num: int, phase: Optional[int]) -> str:
    """The frozen DSL notation; emission nodes get E."""
    w = "E" if phase is None else str(phase)
    return f"L{layer}P{pass_num}W[{layer}]({w})"


class Journey:
    """One run's journey dir. The engine lays structure; agents fill content."""

    def __init__(self, root, domain: str):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        dpath = self.root / "domain.md"
        if not dpath.exists():
            dpath.write_text(domain, encoding="utf-8")
        self.domain = dpath.read_text(encoding="utf-8")
        for sub in ("rules", "skills", "artifacts"):
            (self.root / sub).mkdir(exist_ok=True)
        for l in LAYERS:
            for p in PASSES:
                (self.root / f"L{l}" / f"P{p}").mkdir(parents=True,
                                                      exist_ok=True)

    # ── addressing ───────────────────────────────────────────────────────────
    def node_path(self, layer: int, pass_num: int,
                  phase: Optional[int]) -> Path:
        d = self.root / f"L{layer}" / f"P{pass_num}"
        return d / ("emission.json" if phase is None
                    else node_filename(phase))

    def all_nodes(self) -> List[Tuple[int, int, Optional[int]]]:
        """The full walk: 7 phases + 1 emission per pass, 9 passes = 72."""
        out: List[Tuple[int, int, Optional[int]]] = []
        for l in LAYERS:
            for p in PASSES:
                out.extend((l, p, w) for w in PHASES)
                out.append((l, p, None))
        return out

    def _done(self, node) -> bool:
        p = self.node_path(*node)
        return p.exists() and bool(p.read_text(encoding="utf-8").strip())

    def position(self) -> Optional[Tuple[int, int, Optional[int]]]:
        """The first missing node — None means the run is complete."""
        for node in self.all_nodes():
            if not self._done(node):
                return node
        return None

    # ── progressive disclosure feeds ─────────────────────────────────────────
    def rules_so_far(self) -> Dict[str, str]:
        return {p.stem: p.read_text(encoding="utf-8")
                for p in sorted((self.root / "rules").glob("*.md"))}

    def pass_artifacts(self, layer: int, pass_num: int) -> Dict[str, str]:
        d = self.root / f"L{layer}" / f"P{pass_num}"
        return {p.name: p.read_text(encoding="utf-8")
                for p in sorted(d.glob("*.md"))}

    def layer_domain(self, layer: int) -> str:
        """THE RECURSION, made real: L0 works the run's domain; L{n} works the
        previous layer's P2 emission (the constructor becomes the subject).
        ee-v1's layers reused identical prompts — this is the fix."""
        if layer == 0:
            return self.domain
        prev = self.emission(layer - 1, 2)
        if prev:
            return (f"the generator built at L{layer-1}P2 for "
                    f"[{self.domain.strip()[:80]}]:\n{prev['content']}")
        return self.domain

    # ── writes (the engine's, and the emissions' minting) ────────────────────
    def write_node(self, layer: int, pass_num: int, phase: int,
                   content: str) -> Path:
        p = self.node_path(layer, pass_num, phase)
        p.write_text(content, encoding="utf-8")
        return p

    def write_emission(self, layer: int, pass_num: int,
                       name: str, content: str) -> Path:
        kind = EMISSION_KIND[pass_num]
        self.node_path(layer, pass_num, None).write_text(
            json.dumps({"kind": kind, "name": name, "content": content},
                       indent=2), encoding="utf-8")
        if kind == "rule":
            dest = self.root / "rules" / f"{name}.md"
        elif kind == "skill":
            d = self.root / "skills" / name
            d.mkdir(parents=True, exist_ok=True)
            dest = d / "SKILL.md"
        else:
            dest = self.root / "artifacts" / f"{name}.md"
        dest.write_text(content, encoding="utf-8")
        return dest

    def emission(self, layer: int, pass_num: int) -> Optional[dict]:
        p = self.node_path(layer, pass_num, None)
        if p.exists():
            try:
                return json.loads(p.read_text(encoding="utf-8"))
            except ValueError:
                return None
        return None

    def final_artifact(self) -> Optional[str]:
        """The run's closure — L2P3's emission (THIS generator). Feeds the
        next run's domain in the tower."""
        e = self.emission(2, 3)
        return e["content"] if e else None

    # ── the proof layer (map_gate) — certificates, soup, the fixpoint meter ──
    def certificate_path(self, layer: int, pass_num: int) -> Path:
        return self.root / f"L{layer}" / f"P{pass_num}" / "certificate.json"

    def write_certificate(self, layer: int, pass_num: int,
                          envelope: dict) -> Path:
        p = self.certificate_path(layer, pass_num)
        p.write_text(json.dumps(envelope, indent=2), encoding="utf-8")
        return p

    def certificate(self, layer: int, pass_num: int) -> Optional[dict]:
        p = self.certificate_path(layer, pass_num)
        if p.exists():
            try:
                return json.loads(p.read_text(encoding="utf-8"))
            except ValueError:
                return None
        return None

    def soup_path(self, layer: int, pass_num: int) -> Path:
        return self.root / f"L{layer}" / f"P{pass_num}" / "soup.json"

    def write_soup(self, layer: int, pass_num: int, record: dict) -> Path:
        """Persistent SOUP: the halt breadcrumb. NOT a node file — position()
        is unchanged, so the run halts fail-closed and resumes exactly here."""
        p = self.soup_path(layer, pass_num)
        p.write_text(json.dumps(record, indent=2), encoding="utf-8")
        return p

    def clear_soup(self, layer: int, pass_num: int) -> None:
        p = self.soup_path(layer, pass_num)
        if p.exists():
            p.unlink()

    def fixpoint_meter(self) -> List[dict]:
        """THE FIXPOINT METER (Isaac's measurement, mechanized): per certified
        pass, how much NEWLY-certified structure it added. He measured EE by
        running the master prompt over its own output until the structure
        stopped changing — zero-delta = stabilized. Read for free from the
        stored certificates; a readout, never a gate."""
        seen: set = set()
        rows: List[dict] = []
        for l in LAYERS:
            for p in PASSES:
                cert = self.certificate(l, p)
                if cert is None:
                    continue
                items = certified_structure(cert)
                new = items - seen
                seen |= items
                rows.append({"node": f"L{l}P{p}", "new": len(new),
                             "total_certified": len(seen)})
        return rows


def certified_structure(envelope: dict) -> set:
    """The set of structural atoms a certificate proves — the currency the
    fixpoint meter counts. Read from the certified construction payload
    (map-v2 envelope: proof_context.construction.payload)."""
    payload = (envelope.get("proof_context", {})
               .get("construction", {}).get("payload", {}))
    items: set = set()
    for c in payload.get("concepts", []):
        items.add(f"concept:{c['id']}")
    for r in payload.get("relations", []):
        items.add(f"relation:{r['id']}:{r['source']}:{r['target']}")
    for s in payload.get("steps", []):
        items.add(f"step:{s['id']}")
        items.update(f"use:{s['id']}:{u}" for u in s.get("uses", []))
    return items


__all__ = ["Journey", "PAYLOADS", "LAYER_FRAMES", "PHASE_NAMES", "PASS_NAMES",
           "LAYERS", "PASSES", "PHASES", "EMISSION_KIND", "notation",
           "node_filename", "certified_structure"]
