"""ee_v2.kbc — the KB-compiler library (graduated from experiments/).

Pure machinery: KB + worklist (SOUP is the product), the curried compiler,
the metacompiler (any chain notation -> a gated cycling KB compiler), the
relative-root contextualizer, the skilltree library projection, and mount()
— the FUNCTOR that applies the whole command surface to ANY host runtime
(OM, cave-teams, anything with a seat factory + a state root)."""
from .kb_tool import (KB, derive_worklist, reconcile_scan, work_session,
                      parse_jsonl, relative_root, root_context)
from .compiler import compile, build_context, cycle, OPS
from .metacompiler import metacompile, run_chain, run_cycle, Kernel, KernelNode
from .projector import project_library, skill_body, call_number
from .mount import mount, HOST_PROTOCOL
from .automaton import Automaton

__all__ = ["KB", "derive_worklist", "reconcile_scan", "work_session",
           "parse_jsonl", "relative_root", "root_context", "compile",
           "build_context", "cycle", "OPS", "metacompile", "run_chain",
           "run_cycle", "Kernel", "KernelNode", "project_library",
           "skill_body", "call_number", "mount", "HOST_PROTOCOL",
           "Automaton"]
