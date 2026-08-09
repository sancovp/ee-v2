import asyncio, sys
sys.path.insert(0, "/home/ceo/repo/ee-v2/experiments")
from metacompiler import metacompile, run_chain

def seat_factory():
    from cave_teams.examples import MiniMaxRuntime
    return MiniMaxRuntime(name="sigil_seat", tools=[], system_prompt="", max_tokens=8000)

async def main():
    k = metacompile(open("kernels/sparefractalcorechain.txt").read())
    r = await run_chain(k, "build a small tool that people actually use every day",
                        seat_factory, "sparefractal_live", max_cycles=3)
    import json
    print(json.dumps(r, indent=2))

asyncio.run(main())
