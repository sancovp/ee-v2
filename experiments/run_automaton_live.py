#!/usr/bin/env python3
"""THE LANGUAGE AUTOMATON, LIVE (§24) — over the durable restaurant brain.
Real kernel (kuzu weights), real gates (swipl), real MiniMax mints.
Speak → gap → mint → speak; articulate one unspeakable; read the meter."""
import asyncio
import random
import sys

sys.path.insert(0, "/home/ceo/repo/ee-v2")

from ee_v2.kbc import KB                                         # noqa: E402
from ee_v2.kbc.automaton import Automaton                        # noqa: E402
from ee_v2.kbc.brain import KbcBrain                             # noqa: E402

KB_ROOT = "/home/ceo/repo/ee-v2/experiments/kb_restaurants"
BRAIN_ROOT = "/home/ceo/repo/ee-v2/experiments/brain_live"


def seat_factory(name="seat", persona=""):
    from cave_teams.examples import MiniMaxRuntime
    return MiniMaxRuntime(
        name=name, tools=[],
        system_prompt=persona or
        "You are a precise knowledge-mint. Follow the output schema "
        "EXACTLY. ALWAYS end with the required lines.",
        max_tokens=8000)


async def main():
    kb = KB("restaurants", KB_ROOT).load()
    brain = KbcBrain(kb, BRAIN_ROOT)
    auto = Automaton(kb, brain)
    print(f"KB: {len(kb.concepts)}c/{len(kb.relations)}r · "
          f"regions: {brain.regions()}")

    rng = random.Random(81)
    # 1) three kernel walks from the warm regions — speak or name the gap
    for start in ("health_department_inspection",
                  "inventory_management_system",
                  "food_safety"):
        if start not in kb.concepts:
            print(f"-- {start!r} not in KB, skipped")
            continue
        r = await auto.statement(start=start, temp=0.6, max_steps=5,
                                 rng=rng, seat_factory=seat_factory)
        print(f"\n[{r['verdict']} · {r['llm_calls']} calls] "
              f"walk={r['path']}")
        if r["text"]:
            print(f"  SPOKEN: {r['text'][:400]}")
        elif r["gaps"]:
            print(f"  GAPS: {r['gaps'][:4]}")

    # 2) speak the same first walk again — the ledger should cover it
    hist = auto._read_jsonl(auto.log_path)
    first = hist[-3]["path"] if len(hist) >= 3 else hist[0]["path"]
    r = await auto.statement(path=first)
    print(f"\n[recheck · {r['verdict']} · {r['llm_calls']} calls] "
          "the ledger covers the first walk" if r["llm_calls"] == 0
          else f"\n[recheck] unexpected calls: {r}")

    # 3) articulate the top unspeakable
    bucket = auto.explain_bucket(k=5)
    print(f"\nexplain bucket (the unspeakable): {bucket}")
    if bucket:
        a = await auto.articulate(bucket[0], seat_factory)
        print(f"articulate({bucket[0]!r}): ok={a['ok']} "
              f"calls={a['llm_calls']} "
              f"{'edges=' + str(a['edges']) if a['ok'] else 'residue=' + str(a.get('residue'))[:200]}")
        if a["ok"]:
            root = a["root"]
            for op, s, t in a["edges"]:
                if s == root or t == root:
                    r2 = await auto.statement(path=[s, t])
                    if r2["text"]:
                        print(f"  now speakable: {r2['text'][:220]}")
                    break

    print(f"\nMETER: {auto.meter()}")

if __name__ == "__main__":
    asyncio.run(main())
