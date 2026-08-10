#!/usr/bin/env python3
"""THE CRYSTALLIZATION CURVE — the meter as a CURVE, not a point (§24).

A long automaton session over the mature restaurants brain: N statements
walking the warm interior (kernel-sampled starts rotating through gyri +
high-degree concepts), articulating the top unspeakable every block. The
automaton log accumulates (the dir is the state — fully resumable); at the
end the rolling calls-per-statement series IS the curve. Expected shape:
falling toward 0 over the interior as the ledger grows; spikes = frontier
contact (mints), each spike monotone coverage bought once."""
import asyncio
import json
import random
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, "/home/ceo/repo/ee-v2")

from ee_v2.kbc import KB                                         # noqa: E402
from ee_v2.kbc.automaton import Automaton                        # noqa: E402
from ee_v2.kbc.brain import KbcBrain                             # noqa: E402

KB_ROOT = "/home/ceo/repo/ee-v2/experiments/kb_restaurants"
BRAIN_ROOT = "/home/ceo/repo/ee-v2/experiments/brain_live"
N_STATEMENTS = 40
ARTICULATE_EVERY = 10


def seat_factory(name="seat", persona=""):
    from cave_teams.examples import MiniMaxRuntime
    return MiniMaxRuntime(
        name=name, tools=[],
        system_prompt=persona or
        "You are a precise knowledge-mint for a restaurant-operations "
        "knowledge system. Follow the output schema EXACTLY. ALWAYS end "
        "with the required lines.",
        max_tokens=8000)


async def main():
    kb = KB("restaurants", KB_ROOT).load()
    brain = KbcBrain(kb, BRAIN_ROOT)
    auto = Automaton(kb, brain)
    rng = random.Random(81)

    deg = Counter()
    for s, t in kb.relations:
        deg[s] += 1
        deg[t] += 1
    starts = brain.regions() + [c for c in sorted(kb.concepts,
                                                  key=lambda c: -deg[c])[:20]]
    print(f"KB {len(kb.concepts)}c/{len(kb.relations)}r · "
          f"ledger {len(auto.hyperedges())} hyperedges · "
          f"{len(auto.skeletons())} skeletons · starts pool {len(starts)}")

    for i in range(N_STATEMENTS):
        start = starts[i % len(starts)]
        try:
            r = await auto.statement(start=start, temp=0.7, max_steps=5,
                                     rng=rng, seat_factory=seat_factory,
                                     log=lambda *_: None)
            print(f"[{i+1:02d}] {r['verdict']:<11} {r['llm_calls']}c  "
                  f"{'→'.join(r['path'][:4])}")
        except Exception as e:
            print(f"[{i+1:02d}] TRANSPORT     -  {start}: {str(e)[:60]}")
        if (i + 1) % ARTICULATE_EVERY == 0:
            bucket = auto.explain_bucket(k=3)
            todo = [b for b in bucket if deg[b] >= 3]
            if todo:
                try:
                    a = await auto.articulate(todo[0], seat_factory,
                                              log=lambda *_: None)
                    print(f"     articulate({todo[0]}): ok={a['ok']} "
                          f"{a['llm_calls']}c "
                          f"{len(a.get('edges', []))} edges")
                except Exception as e:
                    print(f"     articulate({todo[0]}): TRANSPORT "
                          f"{str(e)[:60]}")

    rows = auto._read_jsonl(auto.log_path)
    calls = [r["llm_calls"] for r in rows]
    W = 5
    series = [round(sum(calls[max(0, i - W + 1):i + 1])
                    / len(calls[max(0, i - W + 1):i + 1]), 2)
              for i in range(len(calls))]
    curve = {"n": len(calls), "total_calls": sum(calls),
             "overall": round(sum(calls) / len(calls), 3),
             "rolling5": series,
             "ledger": len(auto.hyperedges()),
             "skeletons": len(auto.skeletons()),
             "verdicts": dict(Counter(r["verdict"] for r in rows))}
    Path(KB_ROOT, "curve.json").write_text(json.dumps(curve, indent=2))
    print(f"\nCURVE (rolling-5 calls/stmt over {len(calls)} statements):")
    print("  " + " ".join(f"{x:.1f}" for x in series))
    print(f"ledger now {curve['ledger']} hyperedges, "
          f"{curve['skeletons']} skeletons · verdicts {curve['verdicts']}")
    kb.save()

if __name__ == "__main__":
    asyncio.run(main())
