"""convert.py — capability FORMAT as a gauge choice (§23).

functions ⇄ heaven tools (heaven's make_heaven_tool_from_docstring) ⇄
Claude Code skills (THIS module). heaven_tools_to_skills walks tool classes
— they already carry name/description/args_schema.arguments — and emits
SKILL.md per tool plus one bundle skill with the invocation recipe, so
CC-side agents/humans get the same capability surface as heaven agents."""
from __future__ import annotations

from pathlib import Path


def heaven_tools_to_skills(tools: dict, out_dir, bundle_name: str = "kbc") -> dict:
    """TODO(fill — kbworld rule step 9): for each tool class: read .name,
    .description, .args_schema().arguments {name: {type, required, default,
    description}} → render skills/<tool>/SKILL.md (frontmatter + arg table +
    python invocation recipe via .create()._arun(**kwargs)) + one
    skills/using-<bundle>/SKILL.md indexing them. Return {tool: path}."""
    raise NotImplementedError("fill: kbworld rule step 9")


__all__ = ["heaven_tools_to_skills"]
