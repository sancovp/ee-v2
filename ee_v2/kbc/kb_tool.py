#!/usr/bin/env python3
"""kb_tool — the mass-KB tool where SOUP IS THE PRODUCT (Isaac, 2026-08-09).

The gate does NOT auto-converge. Using the tool DUMPS a huge graph and MINTS A
WORK LIST: the prover names every referenced-but-undefined concept + every
orphan, a cheap LLM names every near-duplicate. That worklist PERSISTS and
ACCUMULATES; homie (a human, or an agent on a cron/heartbeat) grinds it down;
the KB coheres over SESSIONS. This is JobWorld: frontier = task queue, prover =
the gauge that mints work, cron = the heartbeat, homie = the handler.

    kb = KB(root); kb.load()
    wl = derive_worklist(kb)                 # the gauge mints work
    await work_session(kb, seat, budget=…)   # one cron tick: homie drains some
    kb.save()                                # monotone accretion, persisted

Every state lives on disk (concepts.jsonl, relations.jsonl, worklist.json) so
the tool is resumable and the accumulation survives crashes — the dir is the
state, the same law as the journey.
"""
from __future__ import annotations

import asyncio
import json
import re
import sys
import tempfile
from pathlib import Path

for _p in ("/home/ceo/repo/ee-v2", "/home/ceo/repo/map-v2",
           "/home/ceo/repo/cave-teams", "/home/ceo/lcshim2"):
    sys.path.insert(0, _p)

from map_v2 import (MapV2Lattice, PrologTargetCompiler,        # noqa: E402
                    load_domain_manifest)
from ee_v2.map_gate.adapter import (EEOntologyAdapter,          # noqa: E402
                                    EEPassObservationAdapter)

DOM = Path(__file__).resolve().parent.parent \
    / "map_gate/domains/ee_ontology/domain.json"
ATOM = re.compile(r"^[a-z][a-zA-Z0-9_]*$")
_DANGLING = re.compile(r"dangling\([a-z][a-zA-Z0-9_]*,\s*([a-z][a-zA-Z0-9_]*)")
_ORPHAN = re.compile(r"orphan\(([a-z][a-zA-Z0-9_]*)")


def sid(x):
    x = re.sub(r"[^a-z0-9_]+", "_", str(x).strip().lower()).strip("_")
    return x if x and ATOM.match(x) else None


def parse_jsonl(text):
    concepts, relations = {}, []
    for line in (text or "").splitlines():
        line = line.strip().rstrip(",")
        if not (line.startswith("{") and line.endswith("}")):
            continue
        try:
            o = json.loads(line)
        except ValueError:
            continue
        if "c" in o and "d" in o:
            c = sid(o["c"])
            if c and len(str(o["d"]).strip()) >= 8:
                concepts.setdefault(c, str(o["d"]).strip()[:400])
        elif "r" in o and isinstance(o.get("r"), list) and len(o["r"]) == 2:
            s, t = sid(o["r"][0]), sid(o["r"][1])
            if s and t:
                relations.append((s, t))
    return concepts, relations


class KB:
    """A persistent, accumulating knowledge base. Monotone by discipline:
    concepts/relations only ever added or canonicalized, never silently lost."""

    def __init__(self, subject, root):
        self.subject = subject
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)
        self.concepts = {}
        self.relations = set()
        self.lib = {}                 # concept -> origin lib (facet/expansion)

    # ── persistence (the dir is the state) ───────────────────────────────────
    def load(self):
        cp = self.root / "concepts.jsonl"
        rp = self.root / "relations.jsonl"
        if cp.exists():
            for line in cp.read_text().splitlines():
                o = json.loads(line)
                self.concepts[o["c"]] = o["d"]
                if o.get("lib"):
                    self.lib[o["c"]] = o["lib"]
        if rp.exists():
            for line in rp.read_text().splitlines():
                s, t = json.loads(line)
                self.relations.add((s, t))
        return self

    def save(self):
        (self.root / "concepts.jsonl").write_text(
            "\n".join(json.dumps({"c": c, "d": d, "lib": self.lib.get(c)})
                      for c, d in sorted(self.concepts.items())))
        (self.root / "relations.jsonl").write_text(
            "\n".join(json.dumps([s, t]) for s, t in sorted(self.relations)))

    def add_concept(self, cid, d, lib=None):
        cid = sid(cid)
        if cid and len(str(d).strip()) >= 8:
            self.concepts.setdefault(cid, str(d).strip()[:400])
            if lib and cid not in self.lib:
                self.lib[cid] = lib
            return True
        return False

    def add_relation(self, s, t):
        s, t = sid(s), sid(t)
        if s and t:
            self.relations.add((s, t))

    def merge_ids(self, canonical, dup):
        """Reconcile: fold dup into canonical (rewrite relation endpoints)."""
        if dup == canonical or dup not in self.concepts:
            return
        self.concepts.pop(dup, None)
        self.relations = {(canonical if s == dup else s,
                           canonical if t == dup else t)
                          for (s, t) in self.relations}

    # ── the gauge (the prover) ───────────────────────────────────────────────
    def check(self):
        payload = {"kind": "ee_ontology", "subject": self.subject,
                   "concepts": [{"kind": "concept", "id": c, "definition": d}
                                for c, d in self.concepts.items()] or
                   [{"kind": "concept", "id": "seed", "definition": "seed"}],
                   "relations": [{"kind": "relation", "id": f"r{i}",
                                  "source": s, "target": t}
                                 for i, (s, t) in enumerate(sorted(
                                     self.relations))] or
                   [{"kind": "relation", "id": "r0",
                     "source": "seed", "target": "seed"}]}
        with tempfile.TemporaryDirectory(prefix="kb-") as td:
            comp = PrologTargetCompiler(load_domain_manifest(DOM))
            lat = MapV2Lattice(Path(td) / "l", compiler=comp,
                               construction_adapter=EEOntologyAdapter(),
                               observation_adapter=EEPassObservationAdapter())
            lat.create(self.subject, "ee_ontology")
            lat.declare_kappa(self.subject, "ee_conceptualization",
                              {"ontology_coherence": "closed + connected"})
            lat.compute(self.subject)
            lat.fill_construction(self.subject, payload)
            lat.attach_observation(self.subject,
                                   {"kind": "pass_witness",
                                    "subject": self.subject, "layer": 0,
                                    "pass_num": 1})
            packet = lat.compile(self.subject)
            fr = packet.get("frontier", [])
        undefined = sorted({m.group(1) for f in fr
                            for m in [_DANGLING.match(f)] if m})
        orphan = sorted({m.group(1) for f in fr
                         for m in [_ORPHAN.match(f)] if m})
        return {"phase": packet.get("griess_phase"),
                "undefined": undefined, "orphan": orphan,
                "n_concepts": len(self.concepts),
                "n_relations": len(self.relations)}


def relative_root(kb, target, direction="both", max_nodes=200):
    """THE RELATIVE ROOT (Isaac, 2026-08-09): the LEAST-FIXED-POINT closure of
    everything `target` bundles from — walk the dependency graph transitively
    until it bottoms out at primitives (or max_nodes). This is the grounding
    context for coherently working on `target`: the API + all the prims it
    imports from other libs.

      direction='deps'      → follow OUTGOING (what target is built FROM,
                              down to prims) — grounds a DEFINED concept.
      direction='consumers' → follow INCOMING (what NEEDS target) — grounds
                              an UNDEFINED stub by the contract its callers
                              impose.
      direction='both'      → the full local cone.

    Returns an ordered list of (concept_id, definition_or_None, lib, depth) —
    BFS order = nearest ground first. Leaves (no further unseen deps) are the
    primitives; a defined-everywhere cone terminating at seeds = is_ont by
    structural recursion."""
    adj_out, adj_in = {}, {}
    for s, t in kb.relations:
        adj_out.setdefault(s, set()).add(t)
        adj_in.setdefault(t, set()).add(s)
    seen = {target}
    frontier = [(target, 0)]
    order = []
    while frontier:
        nxt = []
        for n, depth in frontier:
            neigh = set()
            if direction in ("deps", "both"):
                neigh |= adj_out.get(n, set())
            if direction in ("consumers", "both"):
                neigh |= adj_in.get(n, set())
            for m in sorted(neigh):
                if m not in seen:
                    seen.add(m)
                    order.append((m, kb.concepts.get(m),
                                  kb.lib.get(m), depth + 1))
                    nxt.append((m, depth + 1))
                    if len(seen) >= max_nodes:
                        return order
        frontier = nxt
    return order


def root_context(kb, target, direction="both", max_nodes=120):
    """Render a relative root as grounding context for a seat prompt: the prims
    it must define `target` in terms of, tagged by lib (undefined ones flagged
    so the seat knows the frontier)."""
    root = relative_root(kb, target, direction=direction, max_nodes=max_nodes)
    lines = []
    for cid, d, libname, depth in root:
        tag = f"[{libname}]" if libname else "[?]"
        body = d if d else "«still undefined — frontier»"
        lines.append(f"{'  '*min(depth,4)}{cid} {tag}: {body}")
    return "\n".join(lines) if lines else "(no relative root yet — isolated)"


def derive_worklist(kb, reconcile=None):
    """THE GAUGE MINTS WORK. define = referenced-but-undefined (the prover);
    connect = orphans (the prover); reconcile = near-dup groups (cheap LLM,
    supplied by the caller). This list is what homie/cron drains."""
    chk = kb.check()
    wl = {"phase": chk["phase"], "define": chk["undefined"],
          "connect": chk["orphan"], "reconcile": reconcile or [],
          "n_concepts": chk["n_concepts"], "n_relations": chk["n_relations"]}
    (kb.root / "worklist.json").write_text(json.dumps(wl, indent=2))
    return wl


# ── the handlers (what draining a worklist item DOES) ────────────────────────
def _define_prompt(subject, ids, kb=None):
    """Contextualized define: each undefined concept is presented WITH ITS
    RELATIVE ROOT (the consumers that reference it = the contract it must
    satisfy). The seat defines it grounded in what already needs it, not in a
    vacuum — coherence by construction (Isaac 2026-08-09)."""
    if kb is not None:
        blocks = []
        for cid in ids:
            ctx = root_context(kb, cid, direction="consumers", max_nodes=8)
            blocks.append(f"### {cid}\nreferenced by (the contract to "
                          f"satisfy):\n{ctx}")
        body = "\n\n".join(blocks)
        return (f"For a knowledge base about {subject}, DEFINE each concept "
                "below. It was referenced but never defined; its REFERENCERS "
                "are shown as the contract it must satisfy — define it "
                "COHERENTLY with what already needs it. Output JSONL, one per "
                'line, nothing else: {"c": "<id>", "d": "<definition, 8+ '
                f'chars>"}}\n\n{body}')
    return (f"For a knowledge base about {subject}, DEFINE each of these "
            f"concepts that were referenced but never defined. Output JSONL, "
            'one per line, nothing else: {"c": "<id>", "d": "<definition, 8+ '
            "chars>\"}\nConcepts:\n" + "\n".join(ids))


def _connect_prompt(subject, orphans, sample):
    return (f"For a KB about {subject}, each concept below is UNCONNECTED. "
            "Wire each to ONE closely-related EXISTING concept (pick from the "
            "sample). Output JSONL, one per line, nothing else: "
            '{"r": ["<orphan>", "<existing>"]}\n'
            f"UNCONNECTED:\n{', '.join(orphans)}\n\n"
            f"EXISTING (sample):\n{', '.join(sample)}")


def _reconcile_prompt(subject, batch):
    return (f"For a KB about {subject}, find concepts in this list that denote "
            "THE SAME thing (true synonyms/duplicates only — not merely "
            "related). Output JSONL, one group per line, nothing else: "
            '{"same": ["<canonical_id>", "<dup_id>", ...]}\n'
            f"CONCEPTS:\n{', '.join(batch)}")


async def _seat_run(seat_factory, prompt, tries=4, base=10):
    last = None
    for i in range(tries):
        try:
            import inspect
            out = seat_factory().run(prompt)
            if inspect.isawaitable(out):
                out = await out
            return out if isinstance(out, str) else str(out)
        except Exception as e:
            last = e
            await asyncio.sleep(base * (2 ** i))
    raise last


async def reconcile_scan(kb, seat_factory, batch=100, max_batches=None):
    """The cheap-LLM dedup pass (Isaac: ~100 at a time). Returns merge groups
    [[canonical, dup, ...], ...] — does NOT apply them (that's a work item)."""
    ids = sorted(kb.concepts)
    groups = []
    batches = [ids[i:i + batch] for i in range(0, len(ids), batch)]
    if max_batches:
        batches = batches[:max_batches]
    outs = await asyncio.gather(*[
        _seat_run(seat_factory, _reconcile_prompt(kb.subject, b))
        for b in batches])
    for out in outs:
        for line in out.splitlines():
            line = line.strip().rstrip(",")
            if not (line.startswith("{") and line.endswith("}")):
                continue
            try:
                o = json.loads(line)
            except ValueError:
                continue
            g = [sid(x) for x in o.get("same", []) if sid(x) in kb.concepts]
            if len(g) >= 2:
                groups.append(g)
    return groups


async def work_session(kb, seat_factory, budget=250, do=("define",),
                       reconcile_groups=None):
    """ONE CRON TICK — homie drains up to `budget` items of the chosen kinds.
    Monotone: define ADDS concepts (saving relations); reconcile FOLDS dups;
    connect ADDS relations. Every action grows coherence, never shrinks the KB
    silently. Returns a per-tick report."""
    wl = derive_worklist(kb)
    report = {"before": {"phase": wl["phase"], "concepts": wl["n_concepts"],
                         "relations": wl["n_relations"],
                         "define": len(wl["define"]),
                         "connect": len(wl["connect"])},
              "did": {}}

    if "reconcile" in do and reconcile_groups:
        folded = 0
        for g in reconcile_groups:
            canon = g[0]
            for dup in g[1:]:
                kb.merge_ids(canon, dup)
                folded += 1
        report["did"]["reconciled"] = folded

    if "define" in do and wl["define"]:
        ids = wl["define"][:budget]
        chunks = [ids[i:i + 40] for i in range(0, len(ids), 40)]
        outs = await asyncio.gather(*[
            _seat_run(seat_factory, _define_prompt(kb.subject, c, kb=kb))
            for c in chunks])
        added = 0
        for out in outs:
            cs, _ = parse_jsonl(out)
            for c, d in cs.items():
                if kb.add_concept(c, d):
                    added += 1
        report["did"]["defined"] = added

    if "connect" in do and wl["connect"]:
        orphans = wl["connect"][:budget]
        sample = sorted(kb.concepts)[:300]
        out = await _seat_run(seat_factory,
                              _connect_prompt(kb.subject, orphans, sample))
        _, rels = parse_jsonl(out)
        wired = 0
        for s, t in rels:
            if s in kb.concepts and t in kb.concepts:
                kb.add_relation(s, t)
                wired += 1
        report["did"]["wired"] = wired

    kb.save()
    after = derive_worklist(kb)
    report["after"] = {"phase": after["phase"], "concepts": after["n_concepts"],
                       "relations": after["n_relations"],
                       "define": len(after["define"]),
                       "connect": len(after["connect"])}
    return report


__all__ = ["KB", "derive_worklist", "reconcile_scan", "work_session",
           "parse_jsonl", "relative_root", "root_context"]
