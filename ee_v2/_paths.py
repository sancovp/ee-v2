"""Dependency path bootstrap — container defaults, overridable via EE_V2_DEPS
(colon-separated). lcshim2 must precede user-site (the crossed-langchain fix)."""
import os
import sys

_DEFAULTS = ("/home/ceo/repo/map-v2", "/home/ceo/repo/cave-teams",
             "/home/ceo/repo/brain-agent", "/home/ceo/lcshim2")


def ensure_deps() -> None:
    extra = os.environ.get("EE_V2_DEPS")
    paths = extra.split(":") if extra else [p for p in _DEFAULTS
                                            if os.path.isdir(p)]
    for p in reversed(paths):
        if p in sys.path:
            sys.path.remove(p)
        sys.path.insert(0, p)
