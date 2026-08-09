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
    "global guidance through the current working directory and execute every "
    "reading gate those files name. Re-read any current goal objective, plan, "
    "runbook, registry, checkpoint, Contract Change Envelope, specification "
    "index, governing clauses, contract epochs, accepted deltas, unresolved "
    "discrepancies, and action-specific QA instructions before continuing. For "
    "covered product work, state the exact documents read completely and the "
    "required Spec Basis before implementation-source inspection, runtime "
    "interpretation, failure hypotheses, recommendations, non-reading task "
    "tools, implementation, or verification. Explicitly record a missing "
    "governing specification and use Discover. Chat summaries, memory, worker "
    "lists, old receipts, builds, tests, screenshots, and raw configuration do "
    "not replace current governing documents. If a persistent goal is paused or "
    "blocked, re-read it without reviving or dispatching work."
)


WORKER_CONTEXT = (
    "MANDATORY CODEX WORKER-START PRE-ACTION GATE: Before source inspection, "
    "runtime interpretation, implementation, or verification, re-read every "
    "applicable AGENTS.md layer, then read the finite worker packet and every "
    "complete governing document that packet names. Use its pinned Spec Basis, "
    "specified expectation, protected behavior, assigned evidence, permitted "
    "delta, and contract epoch. If the packet or a named document is missing, "
    "stop with that exact dependency instead of reconstructing intent from "
    "chat, code, tests, logs, or runtime. Own exactly the assigned finite scope. "
    "Do not read the full root manual or complete product-governance contract "
    "unless the packet assigns a coordinator, authority, reconciliation, or "
    "contract-review role that requires it. State the documents read in the "
    "first progress update and keep specified expectation separate from "
    "observed evidence in the terminal receipt."
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
