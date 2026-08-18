#!/usr/bin/env python3
"""Run lightweight structural checks for the Markdown-first Bootstrap."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from check_spec_markdown import CheckError, validate


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
TASK_SCOPE_SECTION = re.compile(
    r"## (Project|Global): task framing and scope control\s+"
    r"~~~markdown\n(.*?)\n~~~",
    re.DOTALL,
)
CURRENT_BRANCH_SECTION = re.compile(
    r"## (Project|Global): current branch only\s+"
    r"~~~markdown\n(.*?)\n~~~",
    re.DOTALL,
)

REQUIRED_TEXT = {
    "AGENTS.md": (
        "Mandatory pre-action specification gate",
        "Lifecycle restart gate",
        "traversal receipt",
        "Every node is limited to 100",
        "Outcome and resource proportionality",
        "60/25/15 planning target",
        "Task framing and scope control",
        "first implementation-bearing request",
        "Current branch only",
        "task-owned write set",
    ),
    "docs/spec-first-workflow.md": (
        "Strict Markdown-First Spec Workflow",
        "docs/specs/README.md",
        "Every node is at most 100",
        "Technical checkers are optional",
    ),
    "docs/agent-governance/product-truth-governance.md": (
        "Node type: root",
        "Markdown traversal and Spec Basis",
        "selected Markdown path plus explicit dependency links",
    ),
    "docs/agent-governance/agents-sections.md": (
        "Project: product specifications",
        "Global: product specifications",
        "Markdown traversal receipt",
        "at most 100 physical lines",
        "Project: current branch only",
        "Global: current branch only",
    ),
    "docs/specs/index.md": (
        "bootstrap.governance@7",
        "bootstrap.legacy-spec-migration@2",
        "bootstrap.codex-lifecycle@3",
        "2026-08-18-markdown-first-routing.md",
    ),
    "docs/specs/features/bootstrap-governance.md": (
        "bootstrap.governance@7",
        "bootstrap-governance/markdown-routing.md",
        "100 physical lines",
    ),
    "docs/specs/features/legacy-spec-migration.md": (
        "bootstrap.legacy-spec-migration@2",
        "legacy-spec-migration/batches-and-safety.md",
        "Census and Markdown state",
    ),
    "prompts/migrate-legacy-spec-library.md": (
        "Never place the complete inventory or corpus bodies in the conversation",
        "3 documents or 12,000 source words",
        "spec_migration.py census",
        "Do not create JSON inventory",
        "at most 100 physical lines",
    ),
    "prompts/setup-project-spec-first.md": (
        "scripts/check_spec_markdown.py",
        "scripts/spec_migration.py",
        "migrate-legacy-spec-library.md",
        "100 physical lines",
    ),
    "prompts/repair-spec-first-workflow.md": (
        "Workflow repair and corpus migration are separate scopes",
        "scripts/check_spec_markdown.py",
        "JSON manifests",
    ),
}

FORBIDDEN_PATHS = (
    "docs/specs/route.json",
    "docs/specs/features/route.json",
    "docs/specs/templates/route.json",
    "docs/specs/templates/route-receipt.md",
    "docs/agent-governance/product-truth/route.json",
    "scripts/spec_route.py",
    "scripts/tests/test_spec_route.py",
)

STALE_MARKERS = (
    "route.json",
    "spec_route.py",
    "inventory.json",
    "--mapping-dir",
)

HISTORICAL_JSON_DELTAS = {
    ROOT / "docs/specs/deltas/2026-08-18-hierarchical-spec-routing.md",
    ROOT / "docs/specs/deltas/2026-08-18-legacy-spec-migration.md",
}


def check_required_text(errors: list[str]) -> None:
    for relative_path, required_values in REQUIRED_TEXT.items():
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        for value in required_values:
            if value not in text:
                errors.append(f"{relative_path}: missing required text: {value}")


def check_forbidden_artifacts(errors: list[str]) -> None:
    for relative in FORBIDDEN_PATHS:
        if (ROOT / relative).exists():
            errors.append(f"obsolete JSON-routing artifact remains: {relative}")

    for path in sorted(ROOT.rglob("*.md")):
        if path in HISTORICAL_JSON_DELTAS:
            continue
        text = path.read_text(encoding="utf-8")
        for marker in STALE_MARKERS:
            if marker in text:
                errors.append(
                    f"{path.relative_to(ROOT)}: stale routing marker: {marker}"
                )


def check_local_markdown_links(errors: list[str]) -> None:
    for path in sorted(ROOT.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK.findall(text):
            if "<" in raw_target or ">" in raw_target:
                continue
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
            if sum(line.startswith(marker) for line in lines) % 2:
                errors.append(f"{path.relative_to(ROOT)}: unbalanced {marker} fences")


def check_mirrored_section(
    errors: list[str], pattern: re.Pattern[str], label: str
) -> None:
    text = (ROOT / "docs/agent-governance/agents-sections.md").read_text(
        encoding="utf-8"
    )
    matches = pattern.findall(text)
    sections = {scope: payload for scope, payload in matches}
    if len(matches) != 2 or set(sections) != {"Project", "Global"}:
        errors.append(f"agents-sections.md: expected Project and Global {label}")
        return
    if sections["Project"] != sections["Global"]:
        errors.append(f"agents-sections.md: Project and Global {label} differ")
    installed = (ROOT / "AGENTS.md").read_text(encoding="utf-8").count(
        sections["Project"]
    )
    if installed != 1:
        errors.append(f"AGENTS.md: canonical {label} must appear once, found {installed}")


def check_instruction_size(errors: list[str]) -> None:
    size = (ROOT / "AGENTS.md").stat().st_size
    if size > 32 * 1024:
        errors.append(f"AGENTS.md: {size} bytes exceeds default 32 KiB chain limit")


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


def check_markdown_trees(errors: list[str]) -> None:
    roots = (
        ROOT / "docs/specs/README.md",
        ROOT / "docs/agent-governance/product-truth-governance.md",
        ROOT / "docs/spec-first-workflow.md",
    )
    scans = (
        ROOT / "docs/specs",
        ROOT / "docs/agent-governance/product-truth-governance.md",
        ROOT / "docs/agent-governance/product-truth",
        ROOT / "docs/spec-first-workflow.md",
    )
    try:
        validate(roots, scans, max_lines=100, forbid_json=True)
    except (CheckError, OSError, UnicodeError) as error:
        errors.append(str(error))


def main() -> int:
    errors: list[str] = []
    check_required_text(errors)
    check_forbidden_artifacts(errors)
    check_local_markdown_links(errors)
    check_markdown_fences(errors)
    check_mirrored_section(errors, TASK_SCOPE_SECTION, "task-scope section")
    check_mirrored_section(errors, CURRENT_BRANCH_SECTION, "current-branch section")
    check_instruction_size(errors)
    check_hook_templates(errors)
    check_markdown_trees(errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print("bootstrap validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
