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

## The neurosymbolic gate (MAP v2) — experimental, mechanics proven

`ee_v2/map_gate/` runs a P1 emission through
[map-v2](https://github.com/sancovp/map-v2)'s typed construction boundary
instead of accepting prose: LLM JSON → pydantic (local shape) → deterministic
lowering → `candidate_*` Prolog facts → closed-world proof → **ONT
certificate** (coherence PROVEN: closed + connected ontology) or **SOUP with
a residue that NAMES each violation** (`dangling(r2, mise_en_place)`,
`orphan(adjacency)`) — the retry signal, produced by the prover. The journey
engine holds observation authority (`source_pass_complete`): a seat cannot
witness itself. `python test_map_gate.py` proves all four properties against
real SWI-Prolog. Not yet wired into the chain's node gauge — that's the
fail-or-insane experiment: measure live ONT rates with residue-fed retries.

## `ee_v2.kbc` — the KB-compiler library (the engine of the dark floor)

The MAP gate above, generalized into a full knowledge-compiler. This is the
engine that powers [dark-factory](https://github.com/sancovp/dark-factory)'s
knowledge line — the machine that grows proof-checked knowledge modules,
publishes them, and articulates them.

| module | what it is |
|---|---|
| [`kbc/kb_tool.py`](ee_v2/kbc/kb_tool.py) | the persistent, accumulating **KB** (the dir is the state) + the gauge that mints a worklist from the prover's residue — *SOUP is the product* |
| [`kbc/compiler.py`](ee_v2/kbc/compiler.py) | **THE ONE CURRIED COMPILER** — `compile(kb, X, op)` = `seat.run(CEL.inject(TEMPLATE[op], relative_root(X)))` → ΔKB → re-gate. Every agent (dumper, definer, wirer, expander) is this one call curried; because `X` may be `"compiler"`, it's the D∞ ≅ [D∞→D∞] fixpoint as running code |
| [`kbc/metacompiler.py`](ee_v2/kbc/metacompiler.py) | drop in any recursive prompt-chain notation → a gated, cycling KB compiler; fixpoint meter = zero new atoms |
| [`kbc/brain.py`](ee_v2/kbc/brain.py) | the durable **brain**: grow gyri (proof-gated), `ask` fires neurons numerically over kuzu activation, each answers its territory, the synthesis is PROVEN one level up (the SES tower) |
| [`kbc/automaton.py`](ee_v2/kbc/automaton.py) | **the language automaton** — the RELATES graph read as a Markov kernel; walk → the trichotomy (known/realizable/unformable) → speak certified walks with **zero LLM calls**, mint only named gaps, articulate hyperedges into proven argument DAGs. The meter measures the LLM *retreating to the frontier* |
| [`kbc/owl.py`](ee_v2/kbc/owl.py) | **the OWL projection** — every certified KB → self-contained Turtle (typed individuals, reified certificates, typed argument edges). The gate stays Prolog (residue = closed-world negation OWL can't express); the OWL is a faithful projection |
| [`kbc/projector.py`](ee_v2/kbc/projector.py) · [`specialize.py`](ee_v2/kbc/specialize.py) · [`mount.py`](ee_v2/kbc/mount.py) · [`heaven_tools.py`](ee_v2/kbc/heaven_tools.py) | the `understand-*` skill library, the specialization tower, the mount functor (apply the whole surface to any host), and 14 heaven tools |

`python test_ee_v2.py`, `test_automaton.py`, `test_brain.py`, `test_map_gate.py`
— all deterministic, real SWI-Prolog + kuzu. See dark-factory for the modules
this engine grows, and [the KB Atlas](https://sancovp.github.io/kb-atlas/) for
their graphs.

Built on [cave-teams](https://github.com/sancovp/cave-teams)
(`pipeline`, `context_engineering.compose_context`). MIT.
