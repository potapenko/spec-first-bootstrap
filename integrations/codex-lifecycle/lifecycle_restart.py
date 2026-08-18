#!/usr/bin/env python3
"""Inject event-specific authority recovery guidance into Codex contexts."""

from __future__ import annotations

import json
import sys
from typing import Any


ROOT_CONTEXT = (
    "MANDATORY CODEX LIFECYCLE PRE-ACTION GATE: Take no task action after "
    "startup, resume, clear, or context compaction until the current authority "
    "has been re-established. Re-read every applicable AGENTS.md layer from "
    "global guidance through the current working directory. Restore any current "
    "goal, plan, runbook, registry, checkpoint, Contract Change Envelope, and "
    "latest Route Receipt. For covered product work, rerun route resolution, "
    "check manifest and contract revisions for drift, and re-read the pinned "
    "contract closure, accepted deltas, unresolved discrepancies, and only the "
    "next-action QA instructions. Traverse from the root only if the task "
    "changed or the receipt is missing or ambiguous. Do not load unselected "
    "siblings merely because context was compacted. State the route, contracts, "
    "clauses, and required Spec Basis before source inspection, runtime "
    "interpretation, failure hypotheses, recommendations, non-reading tools, "
    "implementation, or verification. Chat summaries, old receipts, builds, "
    "tests, and screenshots identify recovery state but do not replace current "
    "contracts. If a persistent goal is paused or blocked, re-read it without "
    "reviving or dispatching work."
)


WORKER_CONTEXT = (
    "MANDATORY CODEX WORKER-START PRE-ACTION GATE: Before source inspection, "
    "runtime interpretation, implementation, or verification, re-read every "
    "applicable AGENTS.md layer, then read the finite worker packet, Route "
    "Receipt, and every contract in its pinned closure. Verify routed revisions "
    "and use the packet's Spec Basis, specified expectation, protected behavior, "
    "assigned evidence, permitted delta, and contract epoch. If the packet, "
    "route, or contract is missing or drifted, stop with that exact dependency "
    "instead of reconstructing intent from chat, code, tests, logs, or runtime. "
    "Own exactly the assigned finite scope. Do not read unselected sibling "
    "contracts or the full root manual unless the packet assigns a coordinator, "
    "authority, reconciliation, or contract-review role that requires them. "
    "State the routed contracts read in the first progress update and keep "
    "specified expectation separate from observed evidence in the receipt."
)


def build_output(payload: Any) -> dict[str, Any]:
    """Return a valid Codex hook response for supported or malformed input."""

    if not isinstance(payload, dict):
        payload = {}

    event_name = payload.get("hook_event_name", "SessionStart")
    if event_name == "SubagentStart":
        additional_context = WORKER_CONTEXT
    else:
        event_name = "SessionStart"
        additional_context = ROOT_CONTEXT

    return {
        "continue": True,
        "hookSpecificOutput": {
            "hookEventName": event_name,
            "additionalContext": additional_context,
        },
    }


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError, UnicodeError):
        payload = {}

    print(json.dumps(build_output(payload), ensure_ascii=False))


if __name__ == "__main__":
    main()
