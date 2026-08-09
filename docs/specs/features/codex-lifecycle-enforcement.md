# Optional Codex Lifecycle Enforcement

- Contract ID: `bootstrap.codex-lifecycle`
- Domain ID: `bootstrap.codex-lifecycle`
- Authority: Active
- Stability: Evolving
- Governs: Optional Codex lifecycle hook adapter
- Contract revision or epoch: `bootstrap.codex-lifecycle@1`
- Release baseline: None

## Goal

Reinforce the active instruction hierarchy after Codex lifecycle events so an
agent re-establishes governing authority before continuing work.

## Scope

- `SessionStart` sources `startup`, `resume`, `clear`, and `compact`;
- `SubagentStart`;
- project-local and global hook templates;
- installation, trust, deduplication, and fixture-test guidance.

## Non-goals

- installing specification, persistent-goal, or browser-QA governance;
- injecting complete specifications or conversations into hook output;
- changing Codex model, reasoning, provider, permission, or concurrency
  settings;
- claiming that hook output mechanically proves every required file was read.

## User-visible behavior

- `SessionStart` injects a root/single-agent pre-action checklist appropriate
  to its lifecycle source.
- `SubagentStart` injects a worker-specific checklist that requires the finite
  packet and only the governing documents named by that packet.
- Worker context does not instruct ordinary workers to read the complete root
  manual or the complete product-governance document unless their role requires
  it.
- A compacted root session receives the restart context before the immediate
  continuation model request.
- Existing hook sources are preserved. Equivalent hooks are reconciled rather
  than duplicated.
- Setup reports the trust-review step required by Codex after adding or
  changing a non-managed hook definition.

## Invariants

- The adapter is optional and Codex-specific.
- The adapter reinforces active `AGENTS.md` authority; it does not replace it.
- Global and project hooks are not both installed for the same requested scope
  without an explicit user decision.
- Hook output is concise, contains no secrets, and stays below its configured
  additional-context limit.
- Event-specific output uses the matching Codex hook event name.

## Edge cases and failure policy

- Malformed or missing input produces a valid conservative `SessionStart`
  response.
- Unsupported event names fall back to `SessionStart` context.
- If the active Codex home or trusted project root cannot be resolved, setup
  stops before writing.
- If a matching hook already exists in another active source, setup reports the
  overlap and avoids duplicate installation.

## Route / state / data implications

- Global adapters use the resolved active Codex home, not a copied username.
- Project adapters resolve scripts from the Git root.
- Hook definitions may live in `hooks.json` or inline config, but setup uses one
  representation per layer.

## Evidence mapping

- OpenAI Codex hooks documentation;
- `integrations/codex-lifecycle/README.md`;
- hook JSON templates;
- `integrations/codex-lifecycle/lifecycle_restart.py`;
- fixture tests.

## Verification mapping

- fixture coverage for all four `SessionStart` sources;
- `SubagentStart` fixture coverage;
- malformed-input fallback;
- JSON parsing of both templates;
- checks for event-specific root and worker context.

## Unknowns requiring confirmation

None.
