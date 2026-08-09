"""ee-v2 — the emergence engine as an executable cave-teams topology."""
from ._paths import ensure_deps
ensure_deps()                      # deps (cave-teams/map-v2/lcshim2) before any import
from .journey import Journey
from .topology import ee_chain
from .run import ee_run, ee_run_async
