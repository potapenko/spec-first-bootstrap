#!/usr/bin/env python3
"""Run lightweight structural checks for the documentation-first Bootstrap."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


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
        "exact documents read completely",
        "Outcome and resource proportionality",
        "60/25/15 planning target",
        "Task framing and scope control",
        "first implementation-bearing request",
        "Git-history inspection",
        "Do not propose a plan to perform this planning work",
        "plan is the execution boundary",
        "minimum proposed scope",
        "Current branch only",
        "commit, or push is not permission to create a branch",
        "task-owned write set",
        "Existing changes are blockers only where they overlap",
        "exclude them from staging",
    ),
    "docs/spec-first-workflow.md": (
        "Mandatory Pre-Decision Start Order",
        "Documents read completely",
        "Evidence still needed",
    ),
    "docs/agent-governance/product-truth-governance.md": (
        "Pre-decision specification discovery",
        "Restart and context compaction",
        "concrete user capability reachable from the product",
    ),
    "docs/agent-governance/root-orchestration.md": (
        "Outcome and economic proportionality",
        "60% shipping implementation",
        "support-only implementation checkpoints",
        "receives review proportional to demonstrated",
        "budget variance",
        "primary agent works as a normal single agent",
        "without subagents, workers, or delegation",
    ),
    "docs/agent-governance/agents-sections.md": (
        "Project: Codex lifecycle restart adapter",
        "Global: Codex lifecycle restart adapter",
        "Project: outcome and resource proportionality",
        "Global: outcome and resource proportionality",
        "Project: task framing and scope control",
        "Global: task framing and scope control",
        "Project: current branch only",
        "Global: current branch only",
        "first implementation-bearing request",
        "single-agent exception",
        "immediate-execution waiver",
        "task-owned write set",
        "Existing changes are blockers only where they overlap",
        "exclude them from staging",
    ),
    "docs/agent-governance/README.md": (
        "task-owned write set",
        "only overlapping existing changes block editing",
        "outside task commits",
    ),
    "docs/specs/index.md": (
        "bootstrap.governance@5",
        "bootstrap.codex-lifecycle@1",
        "2026-08-18-task-owned-worktree-state.md",
    ),
    "docs/specs/features/bootstrap-governance.md": (
        "bootstrap.governance@5",
        "task-owned write set",
        "block implementation only where they overlap",
        "excluded from staging and commits",
    ),
    "prompts/setup-project-agents.md": (
        "Project: outcome and resource proportionality",
        "Project: task framing and scope control",
        "Project: current branch only",
        "explicit user approval",
        "approved plan remains the execution boundary",
        "single-agent exception",
        "risk-proportional review",
        "support-only implementation checkpoint",
        "task-owned write set",
        "changes block only where their paths overlap",
        "excluded from staging and commits",
    ),
    "prompts/setup-global-agents.md": (
        "Global: outcome and resource proportionality",
        "Global: task framing and scope control",
        "Global: current branch only",
        "visible approved execution plan",
        "approved plan as the execution boundary",
        "single-agent exception",
        "default 60/25/15 planning",
        "risk-proportional review",
        "task-owned write set",
        "changes block only where their paths overlap",
        "excluded from staging and commits",
    ),
}

FORBIDDEN_TEXT = {
    "AGENTS.md": (
        "A dirty or diverged working tree is a blocker",
    ),
    "docs/agent-governance/root-orchestration.md": (
        "Every product delta must be covered by independent review",
        "Sol with high reasoning",
        "Terra with medium reasoning",
        "Ultra as the default",
        "Computer Use Discovery And Startup",
        "Screenshot Capture Boundary",
        "@oai/sky",
    ),
    "docs/agent-governance/agents-sections.md": (
        "Computer Use Discovery And Startup",
        "Screenshot Capture Boundary",
        "@oai/sky",
        "A dirty or diverged working tree is a blocker",
    ),
    "docs/specs/features/bootstrap-governance.md": (
        "A dirty or diverged worktree is reported as a blocker",
        "If the selected branch is dirty or diverged before implementation",
    ),
    "prompts/setup-project-agents.md": (
        "product changes receive independent review",
        "dirty or diverged worktree state is reported as a blocker",
    ),
}


def check_required_text(errors: list[str]) -> None:
    for relative_path, required_values in REQUIRED_TEXT.items():
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        for value in required_values:
            if value not in text:
                errors.append(f"{relative_path}: missing required text: {value}")


def check_forbidden_text(errors: list[str]) -> None:
    for relative_path, forbidden_values in FORBIDDEN_TEXT.items():
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        for value in forbidden_values:
            if value in text:
                errors.append(f"{relative_path}: forbidden text present: {value}")


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


def check_task_scope_sections(errors: list[str]) -> None:
    sections_path = ROOT / "docs/agent-governance/agents-sections.md"
    sections_text = sections_path.read_text(encoding="utf-8")
    matches = TASK_SCOPE_SECTION.findall(sections_text)
    sections = {scope: payload for scope, payload in matches}

    if len(matches) != 2 or {scope for scope, _ in matches} != {"Project", "Global"}:
        errors.append(
            "docs/agent-governance/agents-sections.md: expected exactly one "
            "Project and one Global task-scope section"
        )
        return

    if sections["Project"] != sections["Global"]:
        errors.append(
            "docs/agent-governance/agents-sections.md: Project and Global "
            "task-scope payloads differ"
        )

    project_agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    installed_count = project_agents.count(sections["Project"])
    if installed_count != 1:
        errors.append(
            "AGENTS.md: canonical Project task-scope payload must be installed "
            f"exactly once, found {installed_count}"
        )


def check_current_branch_sections(errors: list[str]) -> None:
    sections_path = ROOT / "docs/agent-governance/agents-sections.md"
    sections_text = sections_path.read_text(encoding="utf-8")
    matches = CURRENT_BRANCH_SECTION.findall(sections_text)
    sections = {scope: payload for scope, payload in matches}

    if len(matches) != 2 or {scope for scope, _ in matches} != {"Project", "Global"}:
        errors.append(
            "docs/agent-governance/agents-sections.md: expected exactly one "
            "Project and one Global current-branch section"
        )
        return

    if sections["Project"] != sections["Global"]:
        errors.append(
            "docs/agent-governance/agents-sections.md: Project and Global "
            "current-branch payloads differ"
        )

    project_agents = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    installed_count = project_agents.count(sections["Project"])
    if installed_count != 1:
        errors.append(
            "AGENTS.md: canonical Project current-branch payload must be "
            f"installed exactly once, found {installed_count}"
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
    check_forbidden_text(errors)
    check_local_markdown_links(errors)
    check_markdown_fences(errors)
    check_task_scope_sections(errors)
    check_current_branch_sections(errors)
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
