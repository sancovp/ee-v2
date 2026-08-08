"""
topology.py — THE DIAGRAM COMPILED INTO A CHAIN (the ee-v1 fix, structural).

ee-v1 was an auto-prompter trying to keep ONE agent's context sane across the
whole 9-pass walk — context pollution with ceremony. Here the methodology is
PROGRAMMED as a cave-teams pipeline: 72 nodes (9 passes × 7 phases + 9
emission nodes), each node a Link that

  1. SKIPS itself if its artifact already exists (the dir is the memo —
     resume free, crash-proof);
  2. builds a perfectly-scoped context with cave-teams' context-assembly
     plane (`compose_context`): the FROZEN payload for (pass, phase) + the
     layer frame + the layer's domain + the rules minted so far + this pass's
     prior artifacts — and NOTHING else;
  3. runs a FRESH seat from `runtime_factory()` (no agent carries memory —
     the journey dirs do);
  4. writes the artifact through the Journey engine (the agent never touches
     the structure).

Pass-end EMISSION nodes distill each pass into its RULE-1-shaped output:
P1 → a RULE, P2 → a SKILL, P3 → an ARTIFACT. (Emission prompts are v2
additions — marked, not frozen content.)
"""
from __future__ import annotations

import inspect
import json
import re
from typing import Any, Callable

from cave_teams.chain_ontology import Link, LinkResult, LinkStatus
from cave_teams.topologies import pipeline
from cave_teams.context_engineering import compose_context

from .journey import (Journey, PAYLOADS, LAYER_FRAMES, PHASE_NAMES,
                      PASS_NAMES, EMISSION_KIND, notation)

# v2 ADDITION (not frozen): the pass-end distillation contract.
EMISSION_PROMPTS = {
    "rule": ("Distill this completed pass into ONE operational RULE — the "
             "knowledge every later pass must always know. Reply ONLY JSON: "
             '{"name": "<snake_case>", "content": "<the rule, <=120 words>"}'),
    "skill": ("Distill this completed pass into ONE SKILL — the reusable "
              "constructor (how to MAKE these), as a complete SKILL.md body "
              "a fresh agent could follow. Reply ONLY JSON: "
              '{"name": "<snake_case>", "content": "<the SKILL.md body>"}'),
    "artifact": ("Distill this completed pass into THE ARTIFACT — the "
                 "specific instance this pass built. Reply ONLY JSON: "
                 '{"name": "<snake_case>", "content": "<the artifact body>"}'),
}

# v2 ADDITION (not frozen): the GATED distillation contract — same emission,
# PLUS the typed construction the MapGate proves (§R: run the seat until the
# DSL goes ONT; the laws are PROVEN by SWI-Prolog, never reviewed by a model).
GATED_EMISSION_PROMPTS = {
    1: ("Distill this completed pass into ONE operational RULE — the "
        "knowledge every later pass must always know — PLUS this pass's "
        "ONTOLOGY as a typed construction. Reply ONLY JSON: "
        '{"name": "<snake_case>", "content": "<the rule, <=120 words>", '
        '"concepts": [{"id": "<snake_case atom>", "definition": '
        '"<what it is, >=8 chars>"}], '
        '"relations": [{"id": "r1", "source": "<concept id>", '
        '"target": "<concept id>"}]}. '
        "LAWS (machine-proven, not reviewed): every relation's source and "
        "target MUST be declared concept ids; every concept MUST appear in "
        "at least one relation."),
    2: ("Distill this completed pass into ONE SKILL — the reusable "
        "constructor — as a complete SKILL.md body PLUS the skill's STEPS "
        "as a typed construction. Reply ONLY JSON: "
        '{"name": "<snake_case>", "content": "<the SKILL.md body>", '
        '"steps": [{"id": "<snake_case atom>", "action": '
        '"<what this step does, >=8 chars>", "uses": ["<concept id>"]}]}. '
        "LAWS (machine-proven, not reviewed): every uses entry MUST be a "
        "P1-CERTIFIED concept id of this layer (the list is in your "
        "context)."),
}

_JSON_RE = re.compile(r"\{.*\}", re.S)


def _parse_emission(text: str) -> dict:
    m = _JSON_RE.search(text or "")
    if not m:
        raise ValueError(f"emission is not JSON: {text[:120]!r}")
    o = json.loads(m.group(0))
    if not o.get("name") or not o.get("content"):
        raise ValueError("emission needs name + content")
    o["name"] = re.sub(r"[^a-z0-9_]+", "_", str(o["name"]).lower()).strip("_")
    return o


def _parse_gated_emission(text: str, pass_num: int) -> dict:
    o = _parse_emission(text)
    if pass_num == 1 and not (o.get("concepts") and o.get("relations")):
        raise ValueError("gated P1 emission needs concepts + relations")
    if pass_num == 2 and not o.get("steps"):
        raise ValueError("gated P2 emission needs steps")
    return o


def _residue_block(frontier) -> str:
    return ("\n\nPROOF RESIDUE — your previous emission FAILED the "
            "closed-world check.\nViolations (fix EXACTLY these; keep "
            "everything else):\n"
            + "\n".join(f"- {f}" for f in frontier)
            + "\nRe-emit the FULL JSON.")


def node_context(journey: Journey, layer: int, pass_num: int, phase,
                 gate=None) -> str:
    """THE READING HORIZON (the traversability law, Isaac 2026-08-08):
    to write a node you read everything that came before — SCOPED PER ORDER:

      * the CURRENT LAYER: full fidelity — every phase file + emission from
        this layer's prior passes, plus this pass's files so far;
      * PRIOR LAYERS: emissions only — the standing rules (always), the
        previous layer's P2 closure as the DOMAIN, and an index of minted
        skills/artifacts. Never their raw phase files.

    This is what makes the recursion scale-free: the read window is bounded
    by ONE layer no matter how high the tower goes, because each order's
    interface to its past is constant-size (the distillates)."""
    j, l, p = journey, layer, pass_num
    frame = LAYER_FRAMES[l]
    blocks = {
        "POSITION": (f"{notation(l, p, phase)} — {frame['name']} · "
                     f"{PASS_NAMES[str(p)]} · "
                     + (PHASE_NAMES[str(phase)] if phase is not None
                        else "EMISSION")),
        "LAYER FRAME": frame[p],
        "DOMAIN": j.layer_domain(l),
    }
    rules = j.rules_so_far()
    if rules:
        blocks["THE STANDING RULES (from completed passes — obey)"] =             "\n".join(f"[{k}] {v}" for k, v in rules.items())
    # prior layers: compressed — an index of their minted emissions only
    prior_layer_emissions = []
    for pl in range(l):
        for pp in (1, 2, 3):
            e = j.emission(pl, pp)
            if e:
                prior_layer_emissions.append(
                    f"L{pl}P{pp} {e['kind']}: {e['name']}")
    if prior_layer_emissions:
        blocks["PRIOR LAYERS (emissions index — the compressed past)"] =             "\n".join(prior_layer_emissions)
    # the CURRENT layer: full fidelity from prior passes
    layer_so_far = []
    for pp in range(1, p):
        for fname, content in j.pass_artifacts(l, pp).items():
            layer_so_far.append(f"--- L{l}P{pp}/{fname} ---\n{content}")
        e = j.emission(l, pp)
        if e:
            layer_so_far.append(
                f"--- L{l}P{pp}/emission ({e['kind']}: {e['name']}) ---\n"
                f"{e['content']}")
    if layer_so_far:
        blocks["THIS LAYER SO FAR (full fidelity)"] = "\n".join(layer_so_far)
    if phase is not None:
        blocks["FROZEN GUIDANCE (ee, verbatim)"] =             PAYLOADS[f"pass{p}"][str(phase)].replace(
                "{domain}", j.layer_domain(l)[:200])
        prior = j.pass_artifacts(l, p)
        if prior:
            blocks["THIS PASS SO FAR"] = "\n".join(
                f"--- {n} ---\n{c}" for n, c in prior.items())
        blocks["TASK"] = ("Produce the artifact for this phase as a complete "
                          "markdown document. Output ONLY the document.")
    else:
        blocks["THIS PASS'S ARTIFACTS"] = "\n".join(
            f"--- {n} ---\n{c}" for n, c in j.pass_artifacts(l, p).items())
        gated = gate is not None and p in gate.gated_passes
        if gated and p == 2:
            # ENGINE-SUPPLIED GROUND: the legal vocabulary is P1's CERTIFIED
            # concepts (from the stored certificate — the trust root), handed
            # to the seat so grounding is an instruction before it's a proof
            cert = j.certificate(l, 1) or {}
            ids = [c["id"] for c in cert.get("proof_context", {})
                   .get("construction", {}).get("payload", {})
                   .get("concepts", [])]
            if ids:
                blocks["P1-CERTIFIED CONCEPTS (steps' uses MUST come from "
                       "these)"] = ", ".join(ids)
        blocks["TASK"] = (GATED_EMISSION_PROMPTS[p] if gated
                          else EMISSION_PROMPTS[EMISSION_KIND[p]])
    return compose_context(blocks)


def next_instruction(journey: Journey, gate=None):
    """TRAVERSAL MODE — the dir alone determines the next instruction. Any
    agent (or human, or MCP shim) can ask a journey what's next and receive
    the exact context the chain would build; writing the file IS the state
    transition. Returns (notation, context) or None when the run is closed."""
    pos = journey.position()
    if pos is None:
        return None
    l, p, w = pos
    return notation(l, p, w), node_context(journey, l, p, w, gate=gate)


class NodeLink(Link):
    """One node of the walk. The engine owns structure and context; the seat
    only thinks. With a gate, emission nodes of gated passes run the RETRY
    LOOP: seat → typed payload → MapGate; ONT lets the file exist (the proof
    law and the traversability law become the same law); persistent SOUP
    halts the chain FAIL-CLOSED (no file → position unchanged → resumable)."""

    def __init__(self, journey: Journey, runtime_factory: Callable,
                 layer: int, pass_num: int, phase, gate=None):
        self.journey = journey
        self.runtime_factory = runtime_factory
        self.layer, self.pass_num, self.phase = layer, pass_num, phase
        self.gate = gate
        self.name = notation(layer, pass_num, phase)

    def _context(self) -> str:
        return node_context(self.journey, self.layer, self.pass_num,
                            self.phase, gate=self.gate)

    async def _seat_output(self, prompt: str) -> str:
        seat = self.runtime_factory()           # a FRESH seat, every attempt
        out = seat.run(prompt)
        if inspect.isawaitable(out):
            out = await out
        return out if isinstance(out, str) else str(out)

    async def execute(self, context=None, **_):
        c = dict(context or {})
        j = self.journey
        node = (self.layer, self.pass_num, self.phase)
        if j._done(node):                       # the dir is the memo
            return LinkResult(status=LinkStatus.SUCCESS, context=c)
        if (self.phase is None and self.gate is not None
                and self.pass_num in self.gate.gated_passes):
            return await self._execute_gated(c)
        out = await self._seat_output(self._context())
        if self.phase is not None:
            j.write_node(self.layer, self.pass_num, self.phase, out)
        else:
            e = _parse_emission(out)
            j.write_emission(self.layer, self.pass_num, e["name"],
                             e["content"])
        c.setdefault("_walk", []).append(self.name)
        return LinkResult(status=LinkStatus.SUCCESS, context=c)

    async def _execute_gated(self, c):
        """RUN THE SEAT UNTIL THE DSL GOES ONT (bounded)."""
        j, l, p = self.journey, self.layer, self.pass_num
        base = self._context()
        frontier = None
        for attempt in range(1, self.gate.max_attempts + 1):
            prompt = base + (_residue_block(frontier) if frontier else "")
            out = await self._seat_output(prompt)
            try:
                e = _parse_gated_emission(out, p)
            except ValueError as exc:
                frontier = [f"malformed_emission: {exc}"]
                continue
            verdict = self.gate.check(
                j, l, p, self.gate.payload_from_emission(p, e))
            if verdict["ont"]:
                j.write_certificate(l, p, verdict["certificate"])
                j.write_emission(l, p, e["name"], e["content"])
                j.clear_soup(l, p)
                c.setdefault("_walk", []).append(self.name)
                c.setdefault("_gate_attempts", {})[self.name] = attempt
                return LinkResult(status=LinkStatus.SUCCESS, context=c)
            frontier = verdict["frontier"]
        j.write_soup(l, p, {"notation": self.name,
                            "attempts": self.gate.max_attempts,
                            "frontier": frontier})
        c.setdefault("_gate_attempts", {})[self.name] = self.gate.max_attempts
        # BLOCKED (not ERROR): blocked ON PROOF — the chain stops here, the
        # dir is unchanged, and a rerun resumes at exactly this node
        return LinkResult(status=LinkStatus.BLOCKED, context=c,
                          error=f"persistent SOUP at {self.name}: {frontier}")


def ee_chain(journey: Journey, runtime_factory: Callable, gate=None):
    """The whole methodology as ONE executable object: pipeline over the 72
    nodes, in the frozen walk order. Chain semantics stop on first FAILURE —
    a persistent-SOUP emission halts the run exactly at its node."""
    links = [NodeLink(journey, runtime_factory, l, p, w, gate=gate)
             for (l, p, w) in journey.all_nodes()]
    return pipeline(*links, name=f"ee:{journey.root.name}")


__all__ = ["ee_chain", "NodeLink", "node_context", "next_instruction",
           "EMISSION_PROMPTS", "GATED_EMISSION_PROMPTS"]
