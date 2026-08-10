"""automaton.py — THE LANGUAGE AUTOMATON (§24 / §24b / §24c, Isaac 2026-08-10):
"you need it to be trying to make the language statements without llms and
then calling llms when it knows it fails. the specialized llms yield the
alphabets from which the chaining aspect of the continuous markov process
arise... completing DSLs at all granularities, back to plain english."

THE MECHANISM (nothing new is invented — every part re-reads existing state):
  * the KERNEL is the brain's RELATES graph, read as an unnormalized Markov
    kernel: P(next=t | at c) = softmax(weight(c→t)/T). walk() samples it.
  * the SEMANTICS is the certificate ledger (hyperedges.jsonl): each entry
    binds atoms+steps as ONE proven unit (§24b: certificates ARE hyperedges).
    Admitted only through the ee_ontology gate — the automaton never writes
    an unproven hyperedge.
  * cover() is the TRICHOTOMY, one decision procedure, three mechanical exits:
      KNOWN      every step inside the ledger → render, zero LLM calls
      REALIZABLE the walk forms a typed candidate; gaps are NAMED (undefined
                 atom / unasserted step / uncovered step) → route → mint
      UNFORMABLE won't form a typed claim → the negative wire
  * mint() is "calling LLMs when it knows it fails": each named gap gets ONE
    scoped, RULE-2-shaped call (define via the curried compiler; step
    confirmation with an explicit reject line) — then the GATE admits the
    walk and the ledger grows. Monotone.
  * the NEGATIVE WIRE (§24b): the mint-failure record is the HANDLER —
    down-tuning fires only on the record (≥2 recorded failures), never on a
    gauge alone. teach() with a low score decays amplitude + edge weight;
    certified content is never retracted — only the measure is sculpted.
  * articulate() (§24c): a certified atom whose claim the chain cannot walk
    gets its MISSING ALGEBRA minted — an operator DAG (because / since /
    together_fit / explains) proven through the ee_argument domain
    (grounded / rooted / acyclic / warranted; residue names the slot).
    Persisted: articulate once, speak forever. explain_bucket() enumerates
    the unspeakable — certified structure lacking articulation.
  * THE METER: llm_calls-per-statement, logged per generation
    (automaton_log.jsonl). Crystallized = the domain's interior speaks at ~0
    calls; the LLM retreats to the frontier — Isaac's EE measurement
    transposed onto language itself.
"""
from __future__ import annotations

import asyncio
import json
import math
import random
import re
import tempfile
import time
from collections import Counter
from pathlib import Path

from ._paths import ensure_deps
ensure_deps()

from map_v2 import (MapV2Lattice, PrologTargetCompiler,          # noqa: E402
                    load_domain_manifest)

from .kb_tool import sid, relative_root, root_context            # noqa: E402
from .compiler import compile as kbc_compile                     # noqa: E402

ONT_DOM = Path(__file__).resolve().parent.parent \
    / "map_gate/domains/ee_ontology/domain.json"
ARG_DOM = Path(__file__).resolve().parent.parent \
    / "map_gate/domains/ee_argument/domain.json"

FAIL_THRESHOLD = 2          # recorded mint failures before the wire fires
ARG_OPS = ("because", "since", "together_fit", "explains")
_CONNECTIVE = {"because": "because", "since": "since",
               "together_fit": "whose parts together fit",
               "explains": "which explains", None: "relates to"}


async def _run_seat(seat, prompt, tries=4, base=10):
    """Transport-level retry only (mirrors kb_tool._seat_run) — a connection
    error is infra, not a proof verdict; gates are never retried here."""
    import inspect
    last = None
    for i in range(tries):
        try:
            out = seat.run(prompt)
            if inspect.isawaitable(out):
                out = await out
            return out if isinstance(out, str) else str(out)
        except Exception as e:
            last = e
            await asyncio.sleep(base * (2 ** i))
    raise last


def _jsonl_objs(text):
    for line in (text or "").splitlines():
        line = line.strip().rstrip(",")
        if not (line.startswith("{") and line.endswith("}")):
            continue
        try:
            yield json.loads(line)
        except ValueError:
            continue


class Automaton:
    """The language automaton over one KB (+ optionally its brain).
    All state on disk under kb.root — the dir is the state:
      hyperedges.jsonl    the certificate ledger (semantic units)
      skeletons.jsonl     certified argument DAGs (§24c)
      mint_failures.jsonl the handler's record (the negative wire's evidence)
      automaton_log.jsonl one line per statement (the crystallization meter)
    """

    def __init__(self, kb, brain=None):
        self.kb = kb
        self.brain = brain
        self.hyper_path = kb.root / "hyperedges.jsonl"
        self.skel_path = kb.root / "skeletons.jsonl"
        self.fail_path = kb.root / "mint_failures.jsonl"
        self.log_path = kb.root / "automaton_log.jsonl"

    # ── the ledgers (append-only, on disk) ───────────────────────────────────
    def _read_jsonl(self, path):
        if not path.exists():
            return []
        return [json.loads(x) for x in path.read_text().splitlines() if x]

    def _append_jsonl(self, path, obj):
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(obj) + "\n")

    def hyperedges(self):
        return self._read_jsonl(self.hyper_path)

    def skeletons(self):
        return self._read_jsonl(self.skel_path)

    def _step_index(self):
        idx = set()
        for h in self.hyperedges():
            for s, t in h["edges"]:
                idx.add((s, t))
        return idx

    def _certified_atoms(self):
        atoms = set()
        for h in self.hyperedges():
            atoms.update(h["atoms"])
        return atoms

    def _op_index(self):
        ops = {}
        for sk in self.skeletons():
            for op, s, t in sk["edges"]:
                ops[(s, t)] = op
        return ops

    def _fail_count(self, key):
        return sum(1 for f in self._read_jsonl(self.fail_path)
                   if f["key"] == list(key))

    def _record_fail(self, key, why):
        self._append_jsonl(self.fail_path,
                           {"key": list(key), "why": str(why)[:300],
                            "ts": time.time()})

    # ── the kernel (§24: the graph read as a Markov kernel) ──────────────────
    def _known_to_kb(self, a):
        if a in self.kb.concepts:
            return True
        return any(a in st for st in self.kb.relations)

    def _out_edges(self, node):
        if self.brain is not None:
            q = self.brain.graph.conn.execute(
                "MATCH (a:Concept {name: $n})-[e:RELATES]->(b:Concept) "
                "RETURN b.name, e.weight", {"n": node})
            out = []
            while q.has_next():
                b, w = q.get_next()
                if self._known_to_kb(b):
                    out.append((b, float(w)))
            return out
        adj = Counter()
        for s, t in self.kb.relations:
            if s == node:
                adj[t] += 1.0
            if t == node:
                adj[s] += 0.5
        return list(adj.items())

    def walk(self, start, target=None, temp=0.8, max_steps=8, rng=None):
        """Sample the kernel: softmax over outgoing weights, temperature-
        flattened, until target / dead end / max_steps. Memoryless except
        for no-immediate-backtrack."""
        rng = rng or random.Random()
        path = [start]
        while len(path) <= max_steps:
            if target is not None and path[-1] == target:
                break
            cand = [(b, w) for b, w in self._out_edges(path[-1])
                    if b not in path[-2:]]
            if not cand:
                break
            t_ = max(temp, 1e-3)
            mx = max(w for _b, w in cand)
            ps = [math.exp((w - mx) / t_) for _b, w in cand]
            tot = sum(ps)
            r = rng.random() * tot
            acc = 0.0
            nxt = cand[-1][0]
            for (b, _w), p in zip(cand, ps):
                acc += p
                if r <= acc:
                    nxt = b
                    break
            path.append(nxt)
        return path

    # ── the trichotomy (§24b — one procedure, three mechanical exits) ────────
    def cover(self, path):
        steps = [(s, t) for s, t in zip(path, path[1:])]
        malformed = [a for a in path if sid(a) != a]
        if malformed or len(path) < 2:
            return {"verdict": "unformable", "malformed": malformed,
                    "too_short": len(path) < 2}
        undefined = sorted({a for a in path if a not in self.kb.concepts})
        unasserted = [[s, t] for s, t in steps
                      if (s, t) not in self.kb.relations
                      and (t, s) not in self.kb.relations]
        idx = self._step_index()
        uncovered = [[s, t] for s, t in steps
                     if (s, t) not in idx and (t, s) not in idx]
        if not undefined and not unasserted and not uncovered:
            return {"verdict": "known", "steps": len(steps)}
        return {"verdict": "realizable", "undefined": undefined,
                "unasserted": unasserted, "uncovered": uncovered}

    def _gaps_of(self, c):
        keys = [("define", a) for a in c.get("undefined", [])]
        keys += [("assert", s, t) for s, t in c.get("unasserted", [])]
        return keys

    # ── the gate (the ledger admits only proven units) ───────────────────────
    def _gate_walk(self, path):
        from ee_v2.map_gate.adapter import (EEOntologyAdapter,
                                            EEPassObservationAdapter)
        subject = sid(f"walk_{path[0]}_{path[-1]}"[:40]) or "walk"
        steps = [(s, t) for s, t in zip(path, path[1:])]
        payload = {"kind": "ee_ontology", "subject": subject,
                   "concepts": [{"kind": "concept", "id": a,
                                 "definition": self.kb.concepts[a]}
                                for a in dict.fromkeys(path)],
                   "relations": [{"kind": "relation", "id": f"r{i}",
                                  "source": s, "target": t}
                                 for i, (s, t) in enumerate(steps)]}
        with tempfile.TemporaryDirectory(prefix="walkgate-") as td:
            comp = PrologTargetCompiler(load_domain_manifest(ONT_DOM))
            lat = MapV2Lattice(Path(td) / "l", compiler=comp,
                               construction_adapter=EEOntologyAdapter(),
                               observation_adapter=EEPassObservationAdapter())
            lat.create(subject, "ee_ontology")
            lat.declare_kappa(subject, "ee_conceptualization",
                              {"ontology_coherence": "closed + connected"})
            lat.compute(subject)
            lat.fill_construction(subject, payload)
            lat.attach_observation(subject, {"kind": "pass_witness",
                                             "subject": subject,
                                             "layer": 0, "pass_num": 1})
            packet = lat.compile(subject)
        return (packet.get("griess_phase") == "ont",
                packet.get("frontier", []))

    # ── routing (the gap's owner is a lookup, not a decision) ────────────────
    def _owning_region(self, atom):
        if self.brain is None:
            return None
        for r in self.brain.regions():
            cone = {c for c, _d, _l, _dep in
                    relative_root(self.kb, r, direction="both",
                                  max_nodes=80)} | {r}
            if atom in cone:
                return r
        return None

    def _named_seat(self, seat_factory, name):
        """Accept either a named factory (name, persona="") or a bare one."""
        try:
            return seat_factory(name)
        except TypeError:
            return seat_factory()

    # ── mint (§24: the LLM as alphabet-mint — one scoped call per named gap) ─
    async def mint(self, path, seat_factory, log=print):
        c = self.cover(path)
        calls = 0
        if c["verdict"] != "realizable":
            return {"minted": False, "verdict": c["verdict"], "llm_calls": 0}

        for atom in c["undefined"]:
            region = self._owning_region(atom)
            name = f"mint_{region or 'kb'}"
            await kbc_compile(self.kb, atom, "define",
                              lambda: self._named_seat(seat_factory, name),
                              lib="automaton")
            calls += 1
            if atom not in self.kb.concepts:
                self._record_fail(("define", atom), "define did not land")
                log(f"[mint-fail] define {atom!r} — recorded")
                return {"minted": False, "verdict": "mint_failed",
                        "gap": ["define", atom], "llm_calls": calls}
            log(f"[mint] defined {atom!r} (routed via "
                f"{region or 'plain seat'})")

        for s, t in c["unasserted"]:
            ok, calls = await self._confirm_step(s, t, seat_factory,
                                                 calls, log)
            if not ok:
                return {"minted": False, "verdict": "mint_failed",
                        "gap": ["assert", s, t], "llm_calls": calls}

        ont, frontier = self._gate_walk(path)
        if not ont:
            self._record_fail(("gate", *path[:4]), frontier[:4])
            return {"minted": False, "verdict": "mint_failed",
                    "gap": ["gate"] + frontier[:4], "llm_calls": calls}
        steps = [[s, t] for s, t in zip(path, path[1:])]
        self._append_jsonl(self.hyper_path,
                           {"atoms": list(dict.fromkeys(path)),
                            "edges": steps, "src": "walk",
                            "ts": time.time()})
        self.kb.save()
        log(f"[mint] walk certified → hyperedge ({len(path)} atoms)")
        return {"minted": True, "verdict": "known", "llm_calls": calls}

    async def _confirm_step(self, s, t, seat_factory, calls, log):
        """The kernel proposed a step the KB never asserted — a candidate
        claim. The seat CONFIRMS or REJECTS on an exact schema; rejection is
        a recorded mint failure (the domain refused the chain's proposal)."""
        prompt = (f"For a knowledge base about {self.kb.subject!r}, the "
                  f"chain proposed the step: {s} -> {t}\n"
                  f"{s}: {self.kb.concepts.get(s, '«undefined»')}\n"
                  f"{t}: {self.kb.concepts.get(t, '«undefined»')}\n"
                  "Is this relation REAL in this domain? Reply EXACTLY one "
                  "line, nothing else:\n"
                  f'{{"r": ["{s}", "{t}"]}}     to confirm\n'
                  f'{{"reject": ["{s}", "{t}"]}}  to refuse')
        for attempt in range(2):
            out = await _run_seat(
                self._named_seat(seat_factory, f"confirm_{s[:16]}"), prompt)
            calls += 1
            for o in _jsonl_objs(out):
                if o.get("r") == [s, t]:
                    self.kb.add_relation(s, t)
                    log(f"[mint] step {s}->{t} confirmed + asserted")
                    return True, calls
                if o.get("reject") == [s, t]:
                    self._record_fail(("assert", s, t), "seat rejected")
                    log(f"[mint-fail] step {s}->{t} REJECTED — recorded")
                    return False, calls
            prompt += ("\n\nPROOF RESIDUE — reply was not one of the two "
                       "exact lines. Emit exactly one of them.")
        self._record_fail(("assert", s, t), "no parseable confirm/reject")
        return False, calls

    # ── the negative wire (§24b — handler-confirmed, weights only) ───────────
    def down_tune(self, path, log=print):
        if self.brain is None:
            return
        for s, t in zip(path, path[1:]):
            self.brain.graph.teach({s: 1.0}, {t: 1.0})
        log(f"[wire] down-tuned {len(path) - 1} steps (weights, "
            "never content)")

    def _walk_condemned(self, c):
        return [k for k in self._gaps_of(c)
                if self._fail_count(k) >= FAIL_THRESHOLD]

    # ── render (mechanical: definitions + operator templates) ────────────────
    def render(self, path):
        ops = self._op_index()
        d = self.kb.concepts
        out = [f"«{path[0]}» — {d.get(path[0], '?')}"]
        for s, t in zip(path, path[1:]):
            op = ops.get((s, t)) or ops.get((t, s))
            out.append(f"{_CONNECTIVE[op]} «{t}» — {d.get(t, '?')}")
        return "; ".join(out) + "."

    # ── THE STATEMENT (the full loop + the meter) ────────────────────────────
    async def statement(self, start=None, target=None, path=None, query=None,
                        seat_factory=None, temp=0.8, max_steps=8, rng=None,
                        log=print):
        calls = 0
        if path is None:
            if query is not None and start is None and self.brain is not None:
                stim = [k for k in self.brain._stimulus(query)
                        if k in self.kb.concepts]
                if len(stim) >= 1:
                    start = stim[0]
                if target is None and len(stim) >= 2:
                    target = stim[1]
            if start is None:
                raise ValueError("statement needs a path, a start, or a "
                                 "query that hits the KB")
            path = self.walk(start, target, temp=temp, max_steps=max_steps,
                             rng=rng)
        c = self.cover(path)
        verdict, text, gaps = c["verdict"], None, self._gaps_of(c)

        if verdict == "known":
            text = self.render(path)
        elif verdict == "realizable":
            condemned = self._walk_condemned(c)
            if condemned:
                verdict = "bullshit"
                self.down_tune(path, log=log)
                log(f"[bullshit] walk touches condemned gaps {condemned} — "
                    "down-tuned, no call spent")
            elif seat_factory is None and gaps:
                verdict = "gapped"
                log(f"[gapped] no seat provided; gaps stay named: {gaps}")
            else:
                m = await self.mint(path, seat_factory, log=log)
                calls += m["llm_calls"]
                if m["minted"]:
                    verdict, text = "known", self.render(path)
                else:
                    verdict = m["verdict"]
                    key = tuple(m.get("gap", ())[:3])
                    if key and self._fail_count(key) >= FAIL_THRESHOLD:
                        verdict = "bullshit"
                        self.down_tune(path, log=log)
        elif c.get("malformed"):
            for a in c["malformed"]:
                self._record_fail(("form", a), "not a typed atom")
            verdict = "bullshit"
            self.down_tune(path, log=log)
        else:
            # too_short with clean atoms = the kernel had nowhere to go from
            # this start (unwired region) — a coverage fact, NOT nonsense;
            # no record, no down-tune
            verdict = "dead_end"

        rec = {"path": path, "verdict": verdict, "llm_calls": calls,
               "ts": time.time()}
        self._append_jsonl(self.log_path, rec)
        return {**rec, "text": text, "gaps": gaps}

    def meter(self):
        rows = self._read_jsonl(self.log_path)
        if not rows:
            return {"statements": 0, "llm_calls": 0,
                    "calls_per_statement": None, "last5": None}
        calls = [r["llm_calls"] for r in rows]
        return {"statements": len(rows), "llm_calls": sum(calls),
                "calls_per_statement": round(sum(calls) / len(calls), 3),
                "last5": round(sum(calls[-5:]) / len(calls[-5:]), 3),
                "verdicts": dict(Counter(r["verdict"] for r in rows))}

    # ── §24c: articulation (the collapse mints the missing algebra) ──────────
    def explain_bucket(self, k=12):
        """THE UNSPEAKABLE, enumerated: certified atoms (in the ledger) with
        no certified skeleton rooted at them — the adjoint law's demand
        signal (asserting X warrants its because-slot exists)."""
        roots = {sk["root"] for sk in self.skeletons()}
        deg = Counter()
        for s, t in self.kb.relations:
            deg[s] += 1
            deg[t] += 1
        todo = [a for a in self._certified_atoms() if a not in roots]
        return sorted(todo, key=lambda a: -deg[a])[:k]

    def _auto_ground(self, atom, log=print):
        """A skeleton spoke a defined-but-uncertified atom: speak the step
        first — gate the connecting 2-path (zero LLM), then re-articulate.
        Crystallization in miniature."""
        if atom not in self.kb.concepts:
            return False
        certified = self._certified_atoms()
        for s, t in self.kb.relations:
            pair = None
            if s == atom and t in certified:
                pair = [s, t]
            elif t == atom and s in certified:
                pair = [s, t]
            if pair:
                ont, _fr = self._gate_walk(pair)
                if ont:
                    self._append_jsonl(self.hyper_path,
                                       {"atoms": pair, "edges": [pair],
                                        "src": "auto_ground",
                                        "ts": time.time()})
                    log(f"[ground] {atom!r} certified via step "
                        f"{pair[0]}->{pair[1]} (0 calls)")
                    return True
        return False

    def _parse_skeleton(self, text):
        edges = []
        for o in _jsonl_objs(text):
            a = o.get("a")
            if (isinstance(a, list) and len(a) == 3 and a[0] in ARG_OPS
                    and sid(a[1]) and sid(a[2])):
                edges.append([a[0], sid(a[1]), sid(a[2])])
        return edges

    def _gate_skeleton(self, root, edges, ground):
        from ee_v2.map_gate.adapter import (EEArgumentAdapter,
                                            EEArgumentObservationAdapter)
        subject = sid(f"arg_{root}"[:40]) or "arg"
        payload = {"kind": "ee_argument", "subject": subject, "root": root,
                   "edges": [{"kind": "arg", "id": f"e{i}", "op": op,
                              "source": s, "target": t}
                             for i, (op, s, t) in enumerate(edges)]}
        with tempfile.TemporaryDirectory(prefix="arggate-") as td:
            comp = PrologTargetCompiler(load_domain_manifest(ARG_DOM))
            lat = MapV2Lattice(Path(td) / "l", compiler=comp,
                               construction_adapter=EEArgumentAdapter(),
                               observation_adapter=(
                                   EEArgumentObservationAdapter()))
            lat.create(subject, "ee_argument")
            lat.declare_kappa(subject, "ee_articulation",
                              {"argument_walkable":
                               "grounded + rooted + acyclic + warranted"})
            lat.compute(subject)
            lat.fill_construction(subject, payload)
            lat.attach_observation(subject,
                                   {"kind": "argument_ground_witness",
                                    "subject": subject,
                                    "certified_atoms": sorted(ground)})
            packet = lat.compile(subject)
        return (packet.get("griess_phase") == "ont",
                packet.get("frontier", []))

    def _articulate_prompt(self, X, residue=None):
        ctx = root_context(self.kb, X, direction="both", max_nodes=20)
        p = (f"A knowledge system about {self.kb.subject!r} has CERTIFIED "
             f"the claim-structure around «{X}» but cannot yet SPEAK it. "
             "Mint the missing argument skeleton: a DAG that orders the "
             f"structure into an argument rooted at {X}.\n\n"
             f"THE STRUCTURE (X's grounding):\n{ctx}\n\n"
             "Reply ONLY JSONL, one edge per line, nothing else:\n"
             '{"a": ["<op>", "<source_id>", "<target_id>"]}\n'
             f"ops: {', '.join(ARG_OPS)}\n"
             "LAWS (machine-proven): every endpoint must be an id shown "
             f"above; the root {X} needs an outgoing because/explains edge; "
             "no cycles; use `because` ONLY if you also emit a since/"
             "together_fit edge FROM its target (the warrant) — otherwise "
             "use `since`.")
        if residue:
            p += (f"\n\nPROOF RESIDUE — previous skeleton failed: {residue}."
                  " Fix exactly these slots; re-emit the full skeleton.")
        return p

    async def articulate(self, X, seat_factory, attempts=3, log=print):
        """Collapse-mint the argument skeleton for certified atom X, proven
        through the ee_argument gate; residue drives the retry (RULE 2)."""
        if X not in self._certified_atoms():
            raise ValueError(f"{X!r} is not in the certificate ledger — "
                             "speak it first (statement), then articulate")
        calls, residue = 0, None
        for _att in range(attempts):
            out = await _run_seat(
                self._named_seat(seat_factory, f"articulate_{X[:16]}"),
                self._articulate_prompt(X, residue))
            calls += 1
            edges = self._parse_skeleton(out)
            if not edges:
                residue = ("no parseable skeleton lines — emit exactly "
                           '{"a": ["<op>", "<src>", "<tgt>"]} per line')
                continue
            endpoints = {e for _op, s, t in edges for e in (s, t)}
            for a in sorted(endpoints - self._certified_atoms()):
                self._auto_ground(a, log=log)
            ont, frontier = self._gate_skeleton(
                X, edges, self._certified_atoms() | {X})
            if ont:
                self._append_jsonl(self.skel_path,
                                   {"root": X, "edges": edges,
                                    "ts": time.time()})
                log(f"[articulate] {X!r}: skeleton certified "
                    f"({len(edges)} operator edges, {calls} calls)")
                return {"ok": True, "root": X, "edges": edges,
                        "llm_calls": calls}
            residue = "; ".join(str(f) for f in frontier[:5])
            log(f"[residue] articulate {X!r}: {residue}")
        self._record_fail(("articulate", X), residue)
        return {"ok": False, "root": X, "residue": residue,
                "llm_calls": calls}


__all__ = ["Automaton"]
