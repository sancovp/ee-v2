#!/usr/bin/env python3
"""§7 THE FAIL-OR-INSANE EXPERIMENT — pre-registered (EE-NEUROSYMBOLIC-DESIGN.md §7).

LIVE seats: a fresh cave-teams MiniMaxRuntime per node/attempt (Isaac's stack,
the same seat dark-factory races). One small knowledge domain. Gated P1+P2
emissions; residue-fed retries bounded at 3; two tower runs → 12 gated
emissions if nothing halts. EVERY gate check appends to gate_log.jsonl.

VERDICT THRESHOLDS — pre-registered BEFORE any live call, so the result
cannot be negotiated after the fact:
  ≥80% of gated emissions reach ONT within ≤3 attempts  → INSANE  (gate everything)
  50–80%                                                → PARTIAL (gate P1 only)
  <50%                                                  → ADVISORY (SOUP ≠ halt)
A persistent-SOUP halt counts as NOT-ONT for that emission and truncates the
run — truncation is reported, never hidden.
"""
import asyncio
import json
import sys
import time
from pathlib import Path

for p in ("/home/ceo/repo/ee-v2", "/home/ceo/repo/map-v2",
          "/home/ceo/repo/cave-teams", "/home/ceo/lcshim2"):
    sys.path.insert(0, p)

from ee_v2.journey import Journey                               # noqa: E402
from ee_v2.topology import ee_chain                             # noqa: E402
from ee_v2.map_gate.gate import MapGate                         # noqa: E402

ROOT = Path(__file__).resolve().parent / "fail_or_insane"
LOG = ROOT / "gate_log.jsonl"
DOMAIN = "designing the daily workflow of a small commercial kitchen"
RUNS = 2


class InstrumentedGate(MapGate):
    """MapGate + a JSONL flight recorder. Semantics untouched."""

    def check(self, journey, layer, pass_num, payload):
        t0 = time.time()
        v = super().check(journey, layer, pass_num, payload)
        rec = {"run": journey.root.name, "node": f"L{layer}P{pass_num}",
               "ont": v["ont"], "n_frontier": len(v["frontier"]),
               "frontier": v["frontier"][:12],
               "secs": round(time.time() - t0, 1),
               "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}
        with LOG.open("a") as f:
            f.write(json.dumps(rec) + "\n")
        print(f"[gate] {rec['run']} {rec['node']} ont={v['ont']} "
              f"frontier={rec['n_frontier']}", flush=True)
        return v


class RetryingSeat:
    """Transport-retry wrapper (the dark-factory lesson): the METHODOLOGY
    never retries — only the wire does. A fresh runtime per transport
    attempt, exponential backoff, bounded."""

    def __init__(self, make, tries=4, base_delay=15):
        self.make, self.tries, self.base_delay = make, tries, base_delay

    async def run(self, prompt):
        last = None
        for i in range(self.tries):
            try:
                return await self.make().run(prompt)
            except Exception as e:                      # transient wire faults
                last = e
                print(f"[transport] attempt {i + 1}/{self.tries} failed: "
                      f"{e}", flush=True)
                await asyncio.sleep(self.base_delay * (2 ** i))
        raise last


def factory():
    from cave_teams.examples import MiniMaxRuntime
    return RetryingSeat(lambda: MiniMaxRuntime(
        name="ee_seat", tools=[], system_prompt="", max_tokens=8000))


async def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    gate = InstrumentedGate()
    model = factory().model
    print(f"§7 START — domain={DOMAIN!r} runs={RUNS} model={model}",
          flush=True)
    attempts_by_node = {}
    journeys = []
    domain = DOMAIN
    for r in range(1, RUNS + 1):
        j = Journey(ROOT / f"run{r}", domain)
        result = await ee_chain(j, factory, gate=gate).execute({})
        for k, v in (result.context or {}).get("_gate_attempts", {}).items():
            attempts_by_node[f"run{r}:{k}"] = v
        journeys.append(j)
        print(f"[run{r}] status={result.status} "
              f"position={j.position()}", flush=True)
        closure = j.final_artifact()
        if closure is None:
            print(f"[run{r}] HALTED — tower truncated here", flush=True)
            break
        domain = closure

    # ── the pre-registered scoreboard ────────────────────────────────────────
    emissions = []
    for i, j in enumerate(journeys, 1):
        for l in (0, 1, 2):
            for p in (1, 2):
                # reached = the chain got to this emission node (its 7 phase
                # files exist); position ordering guarantees that iff a
                # certificate OR a soup OR nothing-was-attempted-yet
                phases_done = len(j.pass_artifacts(l, p)) >= 7
                if not phases_done:
                    continue
                cert = j.certificate(l, p) is not None
                soup = j.soup_path(l, p).exists()
                if not cert and not soup:
                    continue                    # never attempted (post-halt)
                key = f"run{i}:L{l}P{p}W[{l}](E)"
                emissions.append({
                    "emission": f"run{i}:L{l}P{p}", "ont": cert,
                    "attempts": attempts_by_node.get(key),
                    "halted": soup})
    n = len(emissions)
    ok = sum(1 for e in emissions if e["ont"])
    rate = ok / n if n else 0.0
    verdict = ("INSANE — wire the gate into every emission" if rate >= 0.8
               else "PARTIAL — gate P1 only, iterate P2 prompts"
               if rate >= 0.5 else
               "ADVISORY — SOUP must not halt; redesign payload shapes")
    checks = [json.loads(l) for l in LOG.read_text().splitlines()]
    summary = {
        "protocol": "EE-NEUROSYMBOLIC-DESIGN.md §7 (pre-registered)",
        "domain": DOMAIN, "runs_requested": RUNS,
        "runs_completed": sum(1 for j in journeys if j.position() is None),
        "model": model,
        "gated_emissions_attempted": n,
        "ont_within_3": ok, "ont_rate": round(rate, 3),
        "verdict": verdict,
        "per_emission": emissions,
        "total_gate_checks": len(checks),
        "fixpoint_meter": {j.root.name: j.fixpoint_meter() for j in journeys},
    }
    (ROOT / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps({k: summary[k] for k in
                      ("gated_emissions_attempted", "ont_within_3",
                       "ont_rate", "verdict")}, indent=2), flush=True)
    print("§7 DONE", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
