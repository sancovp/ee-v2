"""Shim — graduated to ee_v2.kbc (the importable lib); kept so experiments
scripts and tests keep working unchanged."""
import sys
if "/home/ceo/repo/ee-v2" not in sys.path:
    sys.path.insert(0, "/home/ceo/repo/ee-v2")
from ee_v2.kbc.metacompiler import *  # noqa: F401,F403
