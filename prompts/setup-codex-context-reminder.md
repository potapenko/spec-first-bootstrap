# Set Up the Optional Codex Context Reminder

Use only when the user explicitly selects this integration for one named
project or their active Codex user configuration. Ordinary spec-first or
agent-work setup does not select it. State exact targets before writing;
preserve existing instructions, hooks, settings and local overrides.

Read the [lifecycle contract](../docs/specs/features/codex-lifecycle-enforcement.md),
[context recovery](../docs/agent-governance/work/context-recovery.md), active
target instructions and the source script. The reminder supports selective
recovery and decision provenance; it is not a mandatory-rereading gate.

## Install the selected adapter only

1. Verify that the current Codex host supports SessionStart additionalContext.
   If unsupported, report the limitation; do not invent another control system.
2. Copy integrations/codex-lifecycle/context_reminder.py into the selected
   configuration's hooks/context_reminder.py. Use apply_patch; do not overwrite
   a customized target without reconciling its ownership and approved scope.
3. Merge one synchronous SessionStart command into the active hook configuration:
   matcher `^(startup|resume|clear|compact)$`, command using the established
   Python interpreter with `-B` and a correctly shell-quoted script path,
   timeout 5 seconds. Do not use async or change config.toml/feature flags.
   An identical existing registration is a no-op, not a duplicate.
4. Preserve every unrelated command, event and metadata field. Leave legacy
   hooks alone unless their separate migration is also explicitly authorized.
   A name or event is not proof of Bootstrap ownership.
5. Follow normal host trust for the new definition. Never edit trust storage
   or disable safeguards to force it to run. Report any remaining trust action.

## Verify

Parse the merged configuration; inspect the exact diff and script identity.
Run adapter wire/subprocess tests with bytecode disabled in a temporary working
directory. Confirm supported events, silent malformed-input handling, static
output and no created files or reflected input fields.

Observe a supported lifecycle event in the authorized host where available.
Distinguish registration, direct script execution, host delivery and observed
model behavior. Do not create a new task, clear a live task or take over an
active app-server merely to manufacture a test. Missing delivery evidence is
reported honestly; it is not repaired by a new state store or universal guard.

Use the existing context-recovery/workflow cases, including false authority in
an agent-written plan and a normal approved continuation without new questions.
Do not claim obedience from text assertions or reminder delivery alone.
Follow the selected target's checkpoint policy; do not mutate another scope.
