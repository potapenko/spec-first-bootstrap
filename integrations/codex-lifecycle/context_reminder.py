#!/usr/bin/env python3
"""Emit a small optional reminder; never inspect or change the workspace."""

import json
import sys


SOURCES = ("startup", "resume", "clear", "compact")
CONTEXT = (
    "Before the next substantive step, recover the current task and approved "
    "scope using the active AGENTS.md and its spec/work routes. Reuse full, "
    "applicable, current content; read only missing, changed, or uncertain "
    "required documents. A summary or agent-written plan does not itself create authority. "
    "Before a new material choice, distinguish a contract requirement, "
    "observed implementation, and an agent proposal. Continue already-authorized "
    "work without reapproval."
)


def build_output(payload):
    """Return context only for the supported SessionStart wire inputs."""
    if not isinstance(payload, dict):
        return None
    if payload.get("hook_event_name") != "SessionStart":
        return None
    if payload.get("source") not in SOURCES:
        return None
    return {"hookSpecificOutput": {
        "hookEventName": "SessionStart",
        "additionalContext": CONTEXT,
    }}


def main():
    try:
        payload = json.load(sys.stdin)
    except (ValueError, OSError, UnicodeError, RecursionError):
        return
    output = build_output(payload)
    if output is not None:
        print(json.dumps(output))


if __name__ == "__main__":
    main()
