# Optional Codex Context Reminder

The small context_reminder.py emits static context on SessionStart for startup,
resume, clear and compact. It points to active instructions, selective
[context recovery](../../docs/agent-governance/work/context-recovery.md) and
decision provenance. It does not track reads, write state or block tools.
Use its [separate opt-in prompt](../../prompts/setup-codex-context-reminder.md).
Ordinary setup never installs this adapter or changes application defaults.

The old mandatory-rereading scripts and templates remain retired.

The old [project](../../prompts/setup-project-codex-lifecycle.md) and
[global](../../prompts/setup-global-codex-lifecycle.md) setup links remain as
informational retirement notices. They neither reinstall hooks nor authorize
removal. Ordinary setup preserves existing hook registrations.

For an explicitly authorized existing installation, use
[migration](../../prompts/migrate-codex-lifecycle.md). It removes only proven
Bootstrap reminders in the selected scope and preserves unrelated hooks and
the general hooks feature. Customized or uncertain candidates remain unchanged.
Historical script/template bodies are available at Git revision
`085a84015bad1e5c3ba115c894123ad718eff188` for ownership comparison only.

See the [lifecycle contract](../../docs/specs/features/codex-lifecycle-enforcement.md)
and [verification cases](../../qa/cases/context-recovery.md). Structural checks
run through `scripts/validate_bootstrap.py` and `scripts/tests`; they do not
claim host delivery, runtime migration or empirical model obedience.
