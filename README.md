# ee-v2

**The [emergence engine](https://github.com/sancovp/emergence-engine)'s methodology, compiled into a machine that actually runs it.**

ee-v1 froze the right methodology (the 3-pass / 9-pass systematic-thinking
structure, the master-prompt diagrams) but shipped it as an auto-prompter: a
position counter in `/tmp` serving 21 static strings to one agent that had to
hold the whole journey in its own context — with the structure it was
building left unmanaged. ee-v2 keeps everything ee-v1 froze (extracted
**verbatim**, provenance-stamped — see `ee_v2/frozen_payloads.json` and
`frozen_diagrams/`) and replaces the engine:

| ee-v1 | ee-v2 |
|---|---|
| auto-prompter advises ONE agent | the methodology is **programmed**: a cave-teams `pipeline` of 72 node-Links |
| state = a counter in `/tmp` | **the journey dir IS the state** — position, resume, and memory derived from what exists on disk |
| one context accumulating 63 steps | **a fresh seat per node**, handed a perfectly-scoped context built by `compose_context` (frozen payload + layer frame + domain + rules-so-far — nothing else) |
| the agent builds structure freestyle | **the engine lays every dir and file**; agents only fill content |
| paste the whole topology into your system prompt | **progressive disclosure is mechanical**: each pass mints a RULE that auto-feeds later contexts |
| layers reuse identical prompts (recursion was cosmetic) | **the recursion is real**: L*n*'s domain IS L*n−1*'s P2 emission — the constructor becomes the next subject |
| passes end in nothing | passes end in **emissions**: P1 → a RULE, P2 → a SKILL (`SKILL.md`), P3 → an ARTIFACT |
| one run, then done | **runs compose**: run *n+1*'s domain is run *n*'s L2P3 closure — `ee_run(domain, runs=3)` is the tower |

## The traversability law

Three invariants, all asserted in the proof:

1. **The dir alone determines the next instruction.** `next_instruction(journey)`
   returns the exact context the chain would build — byte-identical (tested) —
   so an agent, a human, or an MCP shim can traverse the journey manually and
   the programmed chain can run it dark: **same state, same instruction,
   two modes.**
2. **State moves only when the file comes to exist.** No counters anywhere.
3. **The reading horizon is PER ORDER**: to write a node you read the current
   layer at FULL fidelity (every prior pass's raw files) but prior layers
   ONLY through their emissions (rules + the closure-as-domain + an index).
   That's what makes the recursion scale-free — the read window is bounded by
   one layer no matter how high the tower goes, because each order's
   interface to its past is constant-size.

## Use

```python
from ee_v2 import ee_run

journeys = ee_run(
    domain="design a customer-onboarding system",
    runtime_factory=lambda: MySeat(),   # anything with .run(str) -> str
    root="./journeys",
    runs=1,                              # 3 for the tower
)
```

Every node writes `journeys/run1/L{n}/P{n}/<phase>.md`; pass emissions land in
`rules/`, `skills/<name>/SKILL.md`, `artifacts/`. Kill it anytime — rerunning
resumes from the first missing node (the dir is the memo).

## Proof

`python test_ee_v2.py` — deterministic, no API: frozen parity against ee-v1's
own source, the 72-node walk, fresh-seat isolation, the disclosure schedule,
real layer recursion, resume-from-wound, and the two-run tower.

Built on [cave-teams](https://github.com/sancovp/cave-teams)
(`pipeline`, `context_engineering.compose_context`). MIT.
