"""
run.py — THE TOWER: runs compose.

One run = the 9-pass walk closing on itself (L2P3 emits THE GENERATOR).
run n+1's domain IS run n's closure — each run is one application of the
function-space step. `ee_run(domain, runs=3)` is the ascent.
"""
from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Callable, List

from .journey import Journey
from .topology import ee_chain


async def ee_run_async(domain: str, runtime_factory: Callable, root,
                       runs: int = 1, gate=None) -> List[Journey]:
    root = Path(root)
    journeys: List[Journey] = []
    current_domain = domain
    for r in range(1, runs + 1):
        j = Journey(root / f"run{r}", current_domain)
        await ee_chain(j, runtime_factory, gate=gate).execute({})
        journeys.append(j)
        closure = j.final_artifact()
        if closure is None:
            break                      # incomplete run — the tower halts here
        current_domain = closure       # the generator becomes the next domain
    return journeys


def ee_run(domain: str, runtime_factory: Callable, root,
           runs: int = 1, gate=None) -> List[Journey]:
    return asyncio.run(ee_run_async(domain, runtime_factory, root, runs,
                                    gate=gate))


__all__ = ["ee_run", "ee_run_async"]
