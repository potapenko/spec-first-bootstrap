#!/usr/bin/env python3
"""Run lightweight structural checks for the documentation-first Bootstrap."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from spec_route import RouteError, count_words, load_graph


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
        "Route Receipt",
        "selected contract",
        "unselected siblings",
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
        "Mandatory pre-decision order",
        "Hierarchical routing",
        "Route Receipt",
        "smallest complete selected contract closure",
    ),
    "docs/agent-governance/product-truth-governance.md": (
        "product-truth/route.json",
        "Completeness means the smallest complete selected contract closure",
        "context compaction",
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
        "Route Receipt",
    ),
    "docs/agent-governance/README.md": (
        "task-owned write set",
        "only overlapping existing changes block editing",
        "outside task commits",
    ),
    "docs/specs/index.md": (
        "bootstrap.governance@6",
        "bootstrap.legacy-spec-migration@1",
        "bootstrap.codex-lifecycle@2",
        "2026-08-18-task-owned-worktree-state.md",
        "2026-08-18-hierarchical-spec-routing.md",
        "2026-08-18-legacy-spec-migration.md",
    ),
    "docs/specs/features/bootstrap-governance.md": (
        "bootstrap.governance@6",
        "Route Receipt",
        "task-owned write set",
        "block implementation only where they overlap",
        "excluded from staging and commits",
    ),
    "docs/specs/features/legacy-spec-migration.md": (
        "bootstrap.legacy-spec-migration@1",
        "BOOTSTRAP.MIGRATION.INVENTORY",
        "BOOTSTRAP.MIGRATION.BATCH",
        "BOOTSTRAP.MIGRATION.RESUME",
        "every inventoried document",
    ),
    "prompts/migrate-legacy-spec-library.md": (
        "Never place the complete inventory or corpus bodies in the conversation",
        "25 documents and 12,000 source words",
        "spec_migration.py inventory",
        "--require-complete",
        "Do not delete, move, merge, split, or rewrite",
    ),
    "prompts/setup-project-spec-first.md": (
        "scripts/spec_migration.py",
        "migrate-legacy-spec-library.md",
        "migration inventory tool can produce compact status",
    ),
    "prompts/repair-spec-first-workflow.md": (
        "Workflow repair and corpus migration are separate scopes",
        "scripts/spec_migration.py",
        "migrate-legacy-spec-library.md",
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
        "Route Receipt",
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
        "Route Receipt",
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


def check_spec_routes(errors: list[str]) -> None:
    route_paths = (
        ROOT / "docs/specs/route.json",
        ROOT / "docs/agent-governance/product-truth/route.json",
    )
    graphs = {}
    for path in route_paths:
        try:
            graphs[path] = load_graph(path)
        except (OSError, RouteError) as error:
            errors.append(f"{path.relative_to(ROOT)}: {error}")

    template = ROOT / "docs/specs/templates/route.json"
    try:
        payload = json.loads(template.read_text(encoding="utf-8"))
        if payload.get("schema_version") != 1:
            errors.append("docs/specs/templates/route.json: schema_version must be 1")
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"docs/specs/templates/route.json: invalid JSON: {error}")

    governance_path = ROOT / "docs/agent-governance/product-truth/route.json"
    governance = graphs.get(governance_path)
    if governance:
        for profile, budget in (("product-question", 1800), ("evolve", 3000)):
            try:
                selected = governance.select([], [profile])
                closure = governance.resolve(selected)
                words = sum(
                    count_words(node.contract.path.read_text(encoding="utf-8"))
                    for node in closure
                    if node.contract
                )
                if words > budget:
                    errors.append(
                        f"{profile} governance closure exceeds {budget}-word "
                        f"regression budget: {words}"
                    )
            except (OSError, RouteError) as error:
                errors.append(f"{profile} profile cannot resolve: {error}")

        registered = {
            node.contract.path.resolve()
            for node in governance.nodes.values()
            if node.contract
        }
        leaf_dir = ROOT / "docs/agent-governance/product-truth"
        for path in leaf_dir.glob("*.md"):
            if path.resolve() not in registered:
                errors.append(
                    f"{path.relative_to(ROOT)}: governance leaf is not registered"
                )

    bootstrap_path = ROOT / "docs/specs/route.json"
    bootstrap = graphs.get(bootstrap_path)
    if bootstrap:
        for profile, budget in (
            ("bootstrap-governance", 2000),
            ("legacy-spec-migration", 3600),
        ):
            try:
                selected = bootstrap.select([], [profile])
                closure = bootstrap.resolve(selected)
                contract_words = sum(
                    count_words(node.contract.path.read_text(encoding="utf-8"))
                    for node in closure
                    if node.contract
                )
                resources = {
                    resource.path: resource
                    for node in closure
                    for resource in node.resources
                }
                resource_words = sum(
                    count_words(path.read_text(encoding="utf-8"))
                    for path in resources
                )
                words = contract_words + resource_words
                if words > budget:
                    errors.append(
                        f"{profile} Bootstrap closure exceeds {budget}-word "
                        f"regression budget: {words}"
                    )
            except (OSError, RouteError) as error:
                errors.append(f"{profile} Bootstrap profile cannot resolve: {error}")

        registered = {
            node.contract.path.resolve()
            for node in bootstrap.nodes.values()
            if node.contract
        }
        for path in (ROOT / "docs/specs/features").glob("*.md"):
            if path.resolve() not in registered:
                errors.append(
                    f"{path.relative_to(ROOT)}: Bootstrap contract is not registered"
                )


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
    check_spec_routes(errors)

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print("bootstrap validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
