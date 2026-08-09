"""convert.py — capability FORMAT as a gauge choice (§23).

functions ⇄ heaven tools (heaven's make_heaven_tool_from_docstring) ⇄
Claude Code skills (THIS module). heaven_tools_to_skills walks tool classes
— they already carry name/description/args_schema.arguments — and emits
SKILL.md per tool plus one bundle skill with the invocation recipe, so
CC-side agents/humans get the same capability surface as heaven agents."""
from __future__ import annotations

from pathlib import Path


def heaven_tools_to_skills(tools: dict, out_dir, bundle_name: str = "kbc",
                           state_root: str = "~/.onionmorph/kbc") -> dict:
    """Walk heaven tool classes → CC skills. Each class already carries
    name/description/args_schema; the skill body documents the args and the
    invocation recipe. One bundle skill indexes them all."""
    out_dir = Path(out_dir)
    made = {}
    lines_index = []
    for key, cls in sorted(tools.items()):
        args = {}
        try:
            args = cls.args_schema().arguments or {}
        except Exception:
            pass
        rows = "\n".join(
            f"| `{a}` | {d.get('type', '?')} | "
            f"{'yes' if d.get('required') else f'no (default {d.get(chr(39)+chr(100)+chr(101)+chr(102)+chr(97)+chr(117)+chr(108)+chr(116)+chr(39), None)!r})'} | "
            f"{str(d.get('description', '')).strip()[:80]} |"
            for a, d in args.items()) or "| _none_ | | | |"
        kwargs = ", ".join(f"{a}=..." for a, d in args.items()
                           if d.get("required")) or ""
        body = (
            f"---\nname: {key}\ndescription: \"{getattr(cls, 'description', key).strip().splitlines()[0][:140]}\"\n---\n\n"
            f"# {key}\n\n{getattr(cls, 'description', '')}\n\n"
            f"## Arguments\n\n| arg | type | required | description |\n"
            f"|---|---|---|---|\n{rows}\n\n"
            "## Invocation (python)\n\n```python\n"
            "from ee_v2.kbc.heaven_tools import make_kbc_tools\n"
            f"tools = make_kbc_tools({state_root!r})\n"
            f"result = await tools[{key!r}].create()._arun({kwargs})\n"
            "print(result.output or result.error)\n```\n")
        d = out_dir / key
        d.mkdir(parents=True, exist_ok=True)
        (d / "SKILL.md").write_text(body, encoding="utf-8")
        made[key] = str(d / "SKILL.md")
        lines_index.append(f"- **{key}** — "
                           f"{str(getattr(cls, 'description', '')).strip().splitlines()[0][:90]}")
    bundle = out_dir / f"using-{bundle_name}"
    bundle.mkdir(parents=True, exist_ok=True)
    (bundle / "SKILL.md").write_text(
        f"---\nname: using-{bundle_name}\ndescription: \"Index of the "
        f"{bundle_name} capability bundle ({len(made)} tools as skills)\"\n"
        f"---\n\n# using-{bundle_name}\n\nEach tool below is also a "
        "heaven tool (same capability, agent-held). Skills document the "
        "human/CC surface.\n\n" + "\n".join(lines_index) + "\n",
        encoding="utf-8")
    made[f"using-{bundle_name}"] = str(bundle / "SKILL.md")
    return made


__all__ = ["heaven_tools_to_skills"]
