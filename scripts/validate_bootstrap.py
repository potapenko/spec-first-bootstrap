#!/usr/bin/env python3
"""Run lightweight structural checks for the documentation-first Bootstrap."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")

REQUIRED_TEXT = {
    "AGENTS.md": (
        "Mandatory pre-action specification gate",
        "Lifecycle restart gate",
        "exact documents read completely",
    ),
    "docs/spec-first-workflow.md": (
        "Mandatory Pre-Decision Start Order",
        "Documents read completely",
        "Evidence still needed",
    ),
    "docs/agent-governance/product-truth-governance.md": (
        "Pre-decision specification discovery",
        "Restart and context compaction",
    ),
    "docs/agent-governance/agents-sections.md": (
        "Project: Codex lifecycle restart adapter",
        "Global: Codex lifecycle restart adapter",
    ),
    "docs/specs/index.md": (
        "bootstrap.governance@1",
        "bootstrap.codex-lifecycle@1",
    ),
}


def check_required_text(errors: list[str]) -> None:
    for relative_path, required_values in REQUIRED_TEXT.items():
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        for value in required_values:
            if value not in text:
                errors.append(f"{relative_path}: missing required text: {value}")


def check_local_markdown_links(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            target = raw_target.strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target_path = target.split("#", 1)[0]
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            if not resolved.exists():
                errors.append(
                    f"{path.relative_to(ROOT)}: broken local link: {raw_target}"
                )


def check_markdown_fences(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        for marker in ("```", "~~~"):
            count = sum(line.startswith(marker) for line in lines)
            if count % 2:
                errors.append(
                    f"{path.relative_to(ROOT)}: unbalanced {marker} fences"
                )


def check_instruction_size(errors: list[str]) -> None:
    agent_bytes = (ROOT / "AGENTS.md").stat().st_size
    if agent_bytes > 32 * 1024:
        errors.append(
            f"AGENTS.md: {agent_bytes} bytes exceeds Codex's default 32 KiB chain limit"
        )


def check_hook_templates(errors: list[str]) -> None:
    adapter = ROOT / "integrations/codex-lifecycle"
    for name in ("global-hooks.json.template", "project-hooks.json.template"):
        path = adapter / name
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as error:
            errors.append(f"{path.relative_to(ROOT)}: invalid JSON: {error}")
            continue

        hooks = payload.get("hooks", {})
        if "SessionStart" not in hooks or "SubagentStart" not in hooks:
            errors.append(f"{path.relative_to(ROOT)}: missing lifecycle event")


def main() -> int:
    errors: list[str] = []
    check_required_text(errors)
    check_local_markdown_links(errors)
    check_markdown_fences(errors)
    check_instruction_size(errors)
    check_hook_templates(errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("bootstrap validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
