#!/usr/bin/env python3
"""The PATTERN GEOMETRY LIBRARY is gate-ready — generic proof over all 6.

For each canonical geometry: auto-build the minimal CONFORMANT mapping (one
element per role + every required edge, no forbidden edge) → assert IN PATTERN.
Then inject the first forbidden invariant's edge → assert OUT with that drift
named. Proves the whole library plugs into the ee_pattern gate."""
import sys

sys.path.insert(0, "/home/ceo/repo/ee-v2")

from ee_v2.kbc.geometries import list_patterns, geometry, describe  # noqa: E402
from ee_v2.kbc.pattern import conformance                           # noqa: E402


def conformant_mapping(g):
    """Bind e_<role> per role; add every required edge; add NO forbidden edge."""
    bindings = [(f"E_{r}", r) for r in g["roles"]]
    edges = []
    for inv in g["invariants"]:
        if inv["inv"] == "required":
            edges.append((inv["relation"], f"E_{inv['source_role']}",
                          f"E_{inv['target_role']}"))
    return {"bindings": bindings, "edges": edges}


def main():
    pats = list_patterns()
    assert len(pats) == 6, pats
    for name in pats:
        g = geometry(name)   # authored (direct) invariants; the transitive
                             # mechanism is proven in test_pattern.py
        m = conformant_mapping(g)
        v = conformance(g, m, subject=f"lib_{name}")
        assert v["in_pattern"], (name, v["drift"])
        # break it: add the first forbidden invariant's edge
        forb = [i for i in g["invariants"]
                if i["inv"] in ("forbidden", "forbidden_transitive")]
        if forb:
            f = forb[0]
            m2 = {"bindings": m["bindings"],
                  "edges": m["edges"] + [(f["relation"],
                                          f"E_{f['source_role']}",
                                          f"E_{f['target_role']}")]}
            v2 = conformance(g, m2, subject=f"lib_{name}_drift")
            assert not v2["in_pattern"], (name, "should have drifted")
            hit = (v2["drift"]["forbidden"] + v2["drift"]["forbidden_path"])
            assert any(i == f["id"] for i, *_ in hit), (name, v2["drift"])
            fb = f"; drift on {f['id']} named"
        else:
            fb = "; (no forbidden invariant)"
        d = describe(name)
        print(f"  {name} ({d['archi_kind'][:32]}): {len(g['roles'])} roles, "
              f"{len(g['invariants'])} invariants → conformant IN PATTERN{fb} ✓")


if __name__ == "__main__":
    main()
    print("PATTERN LIBRARY PASS — all 6 canonical geometries are gate-ready: "
          "each certifies its conformant fill and names the drift when a "
          "forbidden edge is injected.")
