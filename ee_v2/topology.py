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


class NodeLink(Link):
    """One node of the walk. The engine owns structure and context; the seat
    only thinks."""

    def __init__(self, journey: Journey, runtime_factory: Callable,
                 layer: int, pass_num: int, phase):
        self.journey = journey
        self.runtime_factory = runtime_factory
        self.layer, self.pass_num, self.phase = layer, pass_num, phase
        self.name = notation(layer, pass_num, phase)

    def _context(self) -> str:
        j, l, p = self.journey, self.layer, self.pass_num
        frame = LAYER_FRAMES[l]
        blocks = {
            "POSITION": (f"{self.name} — {frame['name']} · "
                         f"{PASS_NAMES[str(p)]} · "
                         + (PHASE_NAMES[str(self.phase)]
                            if self.phase is not None else "EMISSION")),
            "LAYER FRAME": frame[p],
            "DOMAIN": j.layer_domain(l),
        }
        rules = j.rules_so_far()
        if rules:
            blocks["THE STANDING RULES (from completed passes — obey)"] = \
                "\n".join(f"[{k}] {v}" for k, v in rules.items())
        if self.phase is not None:
            blocks["FROZEN GUIDANCE (ee, verbatim)"] = \
                PAYLOADS[f"pass{p}"][str(self.phase)].replace(
                    "{domain}", j.layer_domain(l)[:200])
            prior = j.pass_artifacts(l, p)
            if prior:
                blocks["THIS PASS SO FAR"] = "\n".join(
                    f"--- {n} ---\n{c[:600]}" for n, c in prior.items())
            blocks["TASK"] = ("Produce the artifact for this phase as a "
                              "complete markdown document. Output ONLY the "
                              "document.")
        else:
            blocks["THIS PASS'S ARTIFACTS"] = "\n".join(
                f"--- {n} ---\n{c[:800]}"
                for n, c in j.pass_artifacts(l, p).items())
            blocks["TASK"] = EMISSION_PROMPTS[EMISSION_KIND[p]]
        return compose_context(blocks)

    async def execute(self, context=None, **_):
        c = dict(context or {})
        j = self.journey
        node = (self.layer, self.pass_num, self.phase)
        if j._done(node):                       # the dir is the memo
            return LinkResult(status=LinkStatus.SUCCESS, context=c)
        seat = self.runtime_factory()           # a FRESH seat, every node
        out = seat.run(self._context())
        if inspect.isawaitable(out):
            out = await out
        out = out if isinstance(out, str) else str(out)
        if self.phase is not None:
            j.write_node(self.layer, self.pass_num, self.phase, out)
        else:
            e = _parse_emission(out)
            j.write_emission(self.layer, self.pass_num, e["name"],
                             e["content"])
        c.setdefault("_walk", []).append(self.name)
        return LinkResult(status=LinkStatus.SUCCESS, context=c)


def ee_chain(journey: Journey, runtime_factory: Callable):
    """The whole methodology as ONE executable object: pipeline over the 72
    nodes, in the frozen walk order."""
    links = [NodeLink(journey, runtime_factory, l, p, w)
             for (l, p, w) in journey.all_nodes()]
    return pipeline(*links, name=f"ee:{journey.root.name}")


__all__ = ["ee_chain", "NodeLink", "EMISSION_PROMPTS"]
