#!/usr/bin/env python3
"""THE GRAND-ARGUMENT DRAIN — the full stack on Isaac's own thesis.

Source: sra-git/scalable-publishing/GRAND-ARGUMENT-KERNEL.md (DRAFT v0,
ruling pending — this run produces a DECISION AID, not canon). The doc's §3
is already argument-shaped: grand_argument ← 6 premises ← receipts. The run:
  1. doc-grounded facet dumps (the doc IS each seat's system prompt)
  2. worklist drain (define → connect)
  3. grow gyri on the root + the premise web
  4. speak walks (the automaton) → articulate grand_argument through the
     ee_argument gate — every `because` forced to discharge its warrant or
     get NAMED as an unfilled slot (exactly what the ruling session needs)
  5. project the understand-* library; read the meter
"""
import asyncio
import random
import sys
from pathlib import Path

sys.path.insert(0, "/home/ceo/repo/ee-v2")

from ee_v2.kbc import KB, work_session, compile as kbc_compile   # noqa: E402
from ee_v2.kbc.automaton import Automaton                        # noqa: E402
from ee_v2.kbc.brain import KbcBrain                             # noqa: E402
from ee_v2.kbc.projector import project_library                  # noqa: E402

DOC_PATH = ("/home/ceo/repo/sra-git/scalable-publishing/"
            "GRAND-ARGUMENT-KERNEL.md")
KB_ROOT = "/home/ceo/repo/ee-v2/experiments/kb_grand_argument"
BRAIN_ROOT = "/home/ceo/repo/ee-v2/experiments/brain_grand_argument"

PREMISES = ["it_is_real", "it_is_one_system", "it_is_proven",
            "talk_was_enough", "it_continues", "it_transfers"]
FACETS = ["grand_argument", "roger_template", "treasure_sentence",
          "premise_receipts", "launch_mapping", "mentorloop_transfer"]


def make_persona(doc):
    return ("You dump knowledge-base content grounded EXCLUSIVELY in the "
            "document below (a draft grand-argument kernel). NEVER invent "
            "content the document does not support; every concept must "
            "trace to the text. Use these EXACT ids where the document "
            "names them: grand_argument, theme, " + ", ".join(PREMISES) +
            ". ALWAYS end with the required output lines.\n\n=== THE "
            "DOCUMENT ===\n" + doc)


def seat_factory_with(persona):
    def factory(name="seat", p=""):
        from cave_teams.examples import MiniMaxRuntime
        return MiniMaxRuntime(name=name, tools=[],
                              system_prompt=p or persona, max_tokens=8000)
    return factory


async def main():
    doc = Path(DOC_PATH).read_text(encoding="utf-8")
    persona = make_persona(doc)
    seat_factory = seat_factory_with(persona)
    kb = KB("the grand argument (draft kernel v0)", KB_ROOT).load()
    print(f"start: {len(kb.concepts)}c/{len(kb.relations)}r")

    # 1 — doc-grounded facet dumps (parallel; RESUMABLE per facet — a
    # transport death costs one facet, never the run; rerun fills it)
    done_libs = set(kb.lib.values())
    todo = [f for f in FACETS if f not in done_libs]
    if todo:
        rs = await asyncio.gather(*[
            kbc_compile(kb, f, "dump",
                        lambda f=f: seat_factory(f"dump_{f}"), lib=f)
            for f in todo], return_exceptions=True)
        for f, r in zip(todo, rs):
            if isinstance(r, Exception):
                print(f"FACET FAILED (transport): {f} — {str(r)[:80]}; "
                      "rerun fills it")
        print(f"dumped: {len(kb.concepts)}c/{len(kb.relations)}r")

    # 2 — drain: define to the contract, then connect orphans
    try:
        r1 = await work_session(kb, seat_factory, budget=120, do=("define",))
        r2 = await work_session(kb, seat_factory, budget=40, do=("connect",))
        print(f"drained: define={r1['did']} connect={r2['did']} "
              f"after={r2['after']}")
    except Exception as e:
        print(f"DRAIN INTERRUPTED (transport): {str(e)[:80]} — partial "
              "accretion kept; rerun continues")

    # 3 — gyri: the root + the strongest premises
    brain = KbcBrain(kb, BRAIN_ROOT)
    targets = [c for c in ["grand_argument"] + PREMISES if c in kb.concepts]
    for t in targets[:4]:
        if t not in brain.regions():
            try:
                rep = await brain.grow(t, seat_factory)
                print(f"grew {t!r} (expanded={rep['expanded']})")
            except Exception as e:
                print(f"GROW FAILED (transport): {t} — {str(e)[:80]}")

    # 4 — the automaton speaks the thesis, then articulates it
    auto = Automaton(kb, brain)
    rng = random.Random(81)
    for start in targets[:3]:
        try:
            r = await auto.statement(start=start, temp=0.6, max_steps=5,
                                     rng=rng, seat_factory=seat_factory)
        except Exception as e:
            print(f"STATEMENT FAILED (transport): {start} — {str(e)[:80]}")
            continue
        print(f"[{r['verdict']} · {r['llm_calls']} calls] {r['path']}")
        if r["text"]:
            print(f"  SPOKEN: {r['text'][:300]}")
    if "grand_argument" in auto._certified_atoms():
        a = await auto.articulate("grand_argument", seat_factory)
        print(f"\nARTICULATE grand_argument: ok={a['ok']} "
              f"calls={a['llm_calls']}")
        if a["ok"]:
            for op, s, t in a["edges"]:
                print(f"  {s} -{op}-> {t}")
        else:
            print(f"  UNFILLED SLOTS (the ruling session's agenda): "
                  f"{a.get('residue')}")
    else:
        print("grand_argument not yet in the certificate ledger — speak a "
              "walk through it first (next session)")

    # 5 — the library + the meter
    out, n = project_library(
        kb, Path("/home/ceo/repo/ee-v2/experiments/library_grand_argument"))
    print(f"\nlibrary: {n} understand-* skills at {out}")
    print(f"METER: {auto.meter()}")
    kb.save()

if __name__ == "__main__":
    asyncio.run(main())
