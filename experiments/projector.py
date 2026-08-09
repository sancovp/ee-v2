"""Shim — graduated to ee_v2.kbc; the restaurant-library demo stays here."""
import sys
if "/home/ceo/repo/ee-v2" not in sys.path:
    sys.path.insert(0, "/home/ceo/repo/ee-v2")
from ee_v2.kbc.projector import *  # noqa: F401,F403

if __name__ == "__main__":
    import glob
    from pathlib import Path
    from ee_v2.kbc.kb_tool import KB, parse_jsonl
    from ee_v2.kbc.projector import project_library
    from skilltree import build_index
    base = Path(__file__).resolve().parent
    kb = KB("restaurants", "/tmp/kb_proj")
    for f in sorted(glob.glob(str(base / "scale_dump/dump_*.jsonl"))):
        facet = f.split("dump_")[1].split(".jsonl")[0]
        cs, rs = parse_jsonl(open(f).read())
        for c, d in cs.items():
            kb.add_concept(c, d, lib=facet)
        for s, t in rs:
            kb.add_relation(s, t)
    prev = KB("restaurants", base / "kb_restaurants").load()
    for c, d in prev.concepts.items():
        kb.add_concept(c, d, lib="defined")
    for s, t in prev.relations:
        kb.add_relation(s, t)
    out, n = project_library(kb, base / "library_restaurants")
    print(f"LIBRARY PROJECTED: {out} ({n} understand-* skills)")
    conn = build_index(out)
    q = "stock OR reorder OR inventory OR ingredient"
    rows = conn.execute(
        "SELECT coord, name, snippet(skills, 2, '[', ']', '…', 10) "
        "FROM skills WHERE skills MATCH ? ORDER BY rank LIMIT 5",
        (q,)).fetchall()
    print(f"\nRAG QUERY: {q!r}")
    for r in rows:
        print("  ", r)
