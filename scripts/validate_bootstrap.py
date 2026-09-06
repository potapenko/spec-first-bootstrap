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
MINIMUM_WORK_SECTION = re.compile(
    r"## (Project|Global): minimum-sufficient work\s+"
    r"~~~markdown\n(.*?)\n~~~",
    re.DOTALL,
)

REQUIRED_TEXT = {
    'docs/agent-governance/work/goal-execution.md': (
        'single-agent',
        'coordinated',
        'Honor explicit user mode choice',
        'Required independent',
        'waiting_resource',
        'waiting_evidence',
        'awaiting_authority',
        'every three minutes',
        'host/tool contract requires',
        'no meaningful independent work remains',
        'Never evade',
        'Preserve the mode',
    ),
    'docs/agent-governance/work/scope-and-checkpoints.md': (
        'Every approved implementation plan declares one authority mode',
        '`bounded`',
        '`task-wide`',
        'Every changed diff hunk must map',
        'parent or container',
        'explicit user',
        'global default',
        'project opt-in',
        'both commit and push',
    ),
    'docs/agent-governance/work/task-framing.md': (
        'first implementation-bearing request',
        'Approval persists',
        'A request whose result is itself a plan',
        'without a plan',
        'compaction',
        'User instructions and existing authorization',
        'Silence is not consent',
    ),
    'docs/agent-governance/work-governance.md': (
        'work/task-framing.md',
        'work/scope-and-checkpoints.md',
        'work/minimum-sufficient-work.md',
        'work/goal-execution.md',
        'root-orchestration.md',
        'local overrides',
    ),
    'AGENTS.md': (
        'Mandatory pre-action specification gate',
        'Lifecycle restart gate',
        'traversal receipt',
        'Every node is limited to 100',
        'Task framing and scope control',
        'work-governance.md',
        'Approval persists',
        '`task-wide`',
        'Current branch only',
        'task-owned write set',
        'create a checkpoint commit and push',
        'the checkpoint commit and push succeed.',
        'Persistent-goal continuity',
        'single-agent',
        'coordinated',
        'mandatory host impasse',
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
    'docs/agent-governance/agents-sections.md': (
        'Project: product specifications',
        'Global: product specifications',
        'Markdown traversal receipt',
        'at most 100 physical lines',
        'Project: current branch only',
        'Global: current branch only',
        'work-governance.md',
        'Approval persists',
        '`task-wide`',
        'automatic push is project opt-in',
        'mandatory host impasse',
    ),
    "docs/specs/index.md": (
        "bootstrap.governance@16",
        "bootstrap.legacy-spec-migration@2",
        "bootstrap.codex-lifecycle@3",
        "2026-08-18-markdown-first-routing.md",
        "2026-08-19-current-branch-checkpoint-policy.md",
        "2026-08-19-local-checkpoint-commits.md",
        "2026-08-20-planning-deliverables-and-waiver.md",
        "2026-08-24-checkpoint-commit-and-push.md",
        "2026-08-26-plan-authority-modes.md",
        "2026-08-31-independent-outcome-review.md",
        "2026-09-02-persistent-goal-continuity.md",
        "2026-09-02-minimum-sufficient-work.md",
    ),
    "docs/specs/features/bootstrap-governance.md": (
        "bootstrap.governance@16",
        "BOOTSTRAP.ECONOMY",
        "bootstrap-governance/goal-continuity.md",
        "bootstrap-governance/markdown-routing.md",
        "bootstrap-governance/review-and-acceptance.md",
        "100 physical lines",
    ),
    "docs/specs/features/bootstrap-governance/review-and-acceptance.md": (
        "bootstrap.governance.review@4",
        "BOOTSTRAP.REVIEW.INDEPENDENCE",
        "BOOTSTRAP.REVIEW.VERDICT",
        "BOOTSTRAP.REVIEW.INTEGRATION",
        "`not_verified`",
        "Standalone specification governance remains optional",
        "Do not repeat an\nunchanged check",
    ),
    "docs/specs/features/bootstrap-governance/installation.md": (
        "bootstrap.governance.installation@3",
        "minimum-sufficient work",
        "without adding numerical budgets",
    ),
    "docs/specs/features/bootstrap-governance/restart-and-delivery.md": (
        "bootstrap.governance.restart-delivery@4",
        "expected total token use",
        "Presentation-only edits do not run",
        "A full suite requires",
        "Re-run a\ncheck only when",
    ),
    'docs/specs/features/bootstrap-governance/task-and-scope.md': (
        'bootstrap.governance.task-scope@7',
        'meta-plan or ask for approval',
        'explicitly directs the agent to execute now',
        '`bounded`',
        '`task-wide`',
        'Every changed diff hunk must map to',
        'parent or container',
        'global default',
        'project opt-in',
        'push will not publish unrelated local commits',
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
    "prompts/project-migrations/README.md": (
        "HoldType Swift",
        "SwiftUI Semantic Audit",
        "CodexSwitch",
        "checkpoint 0",
    ),
    "prompts/project-migrations/holdtype-swift.md": (
        "54 Markdown documents",
        "146,123 words",
        "3 documents or 12,000 source words",
        "Do not create JSON",
    ),
    "prompts/project-migrations/swiftui-semantic-audit.md": (
        "contract epoch `tz-v5`",
        "REALISTIC-FIXTURES-001",
        "3 documents or 12,000 source words",
        "Do not create JSON",
    ),
    "prompts/project-migrations/codex-switch.md": (
        "5 Markdown documents",
        "5,446 words",
        "3 documents or 12,000 source words",
        "Do not create JSON",
    ),
    "prompts/project-migrations/phrases-extractor.md": (
        "18 Markdown documents",
        "23,180 words",
        "currently checked-out",
        "Do not create JSON",
    ),
    "prompts/project-migrations/playphraseme-site.md": (
        "90 Markdown documents",
        "138,717 words",
        "currently checked-out",
        "Do not create JSON",
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
    'prompts/setup-project-agents.md': (
        'work-governance.md',
        'work/',
        'local overrides',
        'project opt-in',
        'before committing',
        'both commit and push',
        'Approval persists',
        'meta-plan',
        'bounded',
        'task-wide',
        'single-agent',
        'coordinated',
        'host impasse',
        'Independent observation',
        'not_verified',
        'workflow-compatibility.md',
    ),
    'prompts/setup-global-agents.md': (
        'work-governance.md',
        'work/',
        'local overrides',
        'project opt-in',
        'before committing',
        'both commit and push',
        'Approval persists',
        'meta-plan',
        'bounded',
        'task-wide',
        'single-agent',
        'coordinated',
        'host impasse',
        'Independent observation',
        'not_verified',
        'workflow-compatibility.md',
    ),
    'docs/agent-governance/root-orchestration.md': (
        'authority mode: `bounded` or `task-wide`',
        'an omitted mode means `bounded`',
        'every changed diff hunk',
        'a writable `task-wide` packet is serialized',
        'semantic_scope_check:',
        '### Independent first observation',
        '### Integrated acceptance',
        "criterion coverage before receiving the builder's receipt",
        "Only then does `/root` supply the builder's receipt",
        '`not_verified` to\n`waiting_evidence`',
        'reviewer shopping',
        '`receipt_reconciliation`',
        'Goal continuity and ready-work scheduling',
        'work-governance.md',
        'single-agent',
        'coordinated',
        'host impasse',
        'economy_basis:',
    ),
    'docs/specs/features/bootstrap-governance/goal-continuity.md': (
        'bootstrap.governance.goal-continuity@2',
        'Plan order is not execution order',
        'waiting_resource',
        'recheck every three minutes',
        'single-agent',
        'coordinated',
        'mandatory host',
        'no meaningful',
    ),
    "docs/specs/deltas/2026-09-02-persistent-goal-continuity.md": (
        "bootstrap.governance@14",
        "explicit user request and approval on 2026-09-02",
        "without a fixed attempt ceiling",
    ),
    "qa/cases/goal-continuity.md": (
        "GC-01: independent work",
        "GC-02: repeated contention",
        "GC-07: economic routing",
        "GC-09: completion",
    ),
    "docs/specs/deltas/2026-09-02-minimum-sufficient-work.md": (
        "bootstrap.delta.2026-09-02.minimum-sufficient-work",
        "without token caps, numerical quotas",
        "bootstrap.governance@15",
    ),
    "qa/cases/minimum-sufficient-work.md": (
        "MW-01: presentation only",
        "MW-04: full suite request",
        "MW-07: unnecessary fan-out",
        "MW-11: no budget theater",
        "MW-13: persistent goal",
    ),
}

FORBIDDEN_ECONOMY_TEXT = {
    "AGENTS.md": (
        "60/25/15 planning target",
        "third consecutive support-only",
        "second repair/re-review cycle",
        "budget variance",
    ),
    "docs/agent-governance/agents-sections.md": (
        "60/25/15 planning target",
        "third consecutive support-only",
        "second repair/re-review cycle",
        "budget variance",
    ),
    "docs/agent-governance/root-orchestration.md": (
        "strongest available reasoning model",
        "strongest supported reasoning model",
        "third consecutive support-only",
        "Before dispatching a second repair cycle",
        "budget_variance:",
    ),
    "prompts/setup-project-agents.md": (
        "third consecutive support-only",
        "support depth, budget variance",
    ),
    "prompts/setup-global-agents.md": (
        "default 60/25/15 planning",
        "bounded support-only checkpoints",
        "reset repair or cost limits",
    ),
}

FORBIDDEN_CHECKPOINT_TEXT = {
    "AGENTS.md": (
        "Do not report the task as complete until the checkpoint commit succeeds.",
    ),
    "docs/agent-governance/agents-sections.md": (
        "Do not report the task as complete until the checkpoint commit succeeds.",
    ),
    "docs/specs/features/bootstrap-governance/task-and-scope.md": (
        "Do not report the task as complete until the checkpoint commit succeeds.",
    ),
}

FORBIDDEN_PLANNING_TEXT = {
    "AGENTS.md": (
        "After the new-chat first implementation gate has been satisfied, immediate",
    ),
    "docs/agent-governance/agents-sections.md": (
        "After the new-chat first implementation gate has been satisfied, immediate",
    ),
}

FORBIDDEN_GOAL_CONTINUITY_TEXT = {
    "docs/agent-governance/agents-sections.md": (
        "A paused or blocked goal remains idle",
    ),
    "docs/agent-governance/root-orchestration.md": (
        "status: done | blocked | failed",
        "-> blocked",
    ),
    "prompts/setup-project-agents.md": (
        "a paused or blocked goal stays idle",
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
            if " ".join(value.split()) not in " ".join(text.split()):
                errors.append(f"{relative_path}: missing required text: {value}")


def check_checkpoint_text(errors: list[str]) -> None:
    for relative_path, forbidden_values in FORBIDDEN_CHECKPOINT_TEXT.items():
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        for value in forbidden_values:
            if value in text:
                errors.append(
                    f"{relative_path}: forbidden checkpoint text remains: {value}"
                )


def check_planning_text(errors: list[str]) -> None:
    for relative_path, forbidden_values in FORBIDDEN_PLANNING_TEXT.items():
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        for value in forbidden_values:
            if value in text:
                errors.append(
                    f"{relative_path}: forbidden planning text remains: {value}"
                )


def check_goal_continuity_text(errors: list[str]) -> None:
    for relative_path, forbidden_values in FORBIDDEN_GOAL_CONTINUITY_TEXT.items():
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        for value in forbidden_values:
            if value in text:
                errors.append(
                    f"{relative_path}: forbidden goal-continuity text remains: {value}"
                )


def check_economy_text(errors: list[str]) -> None:
    for relative_path, forbidden_values in FORBIDDEN_ECONOMY_TEXT.items():
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        for value in forbidden_values:
            if value in text:
                errors.append(
                    f"{relative_path}: superseded economy text remains: {value}"
                )


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
    def normalize(value: str) -> str:
        return " ".join(value.replace("docs/agent-governance/", "").replace("docs/agent/", "").split())

    if normalize(sections["Project"]) != normalize(sections["Global"]):
        errors.append(f"agents-sections.md: Project and Global {label} differ")
    if label == "current-branch section":
        # Bootstrap intentionally retains its separately checked commit-and-push override.
        return
    installed = normalize((ROOT / "AGENTS.md").read_text(encoding="utf-8")).count(
        normalize(sections["Project"])
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
        ROOT / "docs/agent-governance/work-governance.md",
    )
    scans = (
        ROOT / "docs/specs",
        ROOT / "docs/agent-governance/product-truth-governance.md",
        ROOT / "docs/agent-governance/product-truth",
        ROOT / "docs/agent-governance/work",
        ROOT / "docs/spec-first-workflow.md",
        ROOT / "docs/agent-governance/work-governance.md",
    )
    try:
        validate(roots, scans, max_lines=100, forbid_json=True)
    except (CheckError, OSError, UnicodeError) as error:
        errors.append(str(error))


def main() -> int:
    errors: list[str] = []
    check_required_text(errors)
    check_checkpoint_text(errors)
    check_planning_text(errors)
    check_goal_continuity_text(errors)
    check_economy_text(errors)
    check_forbidden_artifacts(errors)
    check_local_markdown_links(errors)
    check_markdown_fences(errors)
    check_mirrored_section(errors, TASK_SCOPE_SECTION, "task-scope section")
    check_mirrored_section(errors, CURRENT_BRANCH_SECTION, "current-branch section")
    check_mirrored_section(
        errors, MINIMUM_WORK_SECTION, "minimum-sufficient-work section"
    )
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
