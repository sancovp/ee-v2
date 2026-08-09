import asyncio, glob, sys
sys.path.insert(0, "/home/ceo/repo/ee-v2/experiments")
from kb_tool import KB, derive_worklist, work_session, parse_jsonl

def seat_factory():
    from cave_teams.examples import MiniMaxRuntime
    return MiniMaxRuntime(name="homie", tools=[], system_prompt="", max_tokens=16000)

async def main():
    kb = KB("restaurants", "/home/ceo/repo/ee-v2/experiments/kb_restaurants")
    # seed from cached dumps (keep EVERYTHING — no auto-drop)
    for f in glob.glob("/home/ceo/repo/ee-v2/experiments/scale_dump/dump_*.jsonl"):
        cs, rs = parse_jsonl(open(f).read())
        for c,d in cs.items(): kb.add_concept(c,d)
        for s,t in rs: kb.add_relation(s,t)
    kb.save()
    wl = derive_worklist(kb)
    print(f"SEEDED: {wl['n_concepts']} concepts, {wl['n_relations']} relations")
    print(f"WORKLIST minted by the prover: define={len(wl['define'])} connect={len(wl['connect'])}")
    print("\n[cron tick 1] homie drains the DEFINE bucket...")
    r = await work_session(kb, seat_factory, budget=250, do=("define",))
    print(f"  before: {r['before']['concepts']}c/{r['before']['relations']}r  define-backlog={r['before']['define']}")
    print(f"  did:    defined {r['did'].get('defined')} missing concepts")
    print(f"  after:  {r['after']['concepts']}c/{r['after']['relations']}r  define-backlog={r['after']['define']}  connect-backlog={r['after']['connect']}")
    # how many relations are now valid (endpoints defined) vs before?
    valid = sum(1 for s,t in kb.relations if s in kb.concepts and t in kb.concepts)
    print(f"  relations with BOTH endpoints now defined: {valid}/{len(kb.relations)} "
          f"({100*valid//len(kb.relations)}%)")

asyncio.run(main())
