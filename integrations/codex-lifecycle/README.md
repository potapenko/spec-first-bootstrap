# Optional Codex Lifecycle Adapter

This adapter reinforces the active instruction hierarchy after Codex starts or
restores a session, compacts root context, or starts a subagent.

It is optional and Codex-specific. It does not install specification-first
governance, persistent-goal coordination, or browser QA. Those layers remain
independently selectable.

## Files

- `lifecycle_restart.py` emits event-specific developer context.
- `global-hooks.json.template` is merged into the active Codex home.
- `project-hooks.json.template` is merged into a trusted project's `.codex/`
  layer.
- `tests/test_lifecycle_restart.py` verifies the output contract.

Use the matching setup prompt:

- `prompts/setup-global-codex-lifecycle.md`
- `prompts/setup-project-codex-lifecycle.md`

Do not copy a template without resolving its placeholders and existing hook
sources.

## Runtime contract

`SessionStart` matches `startup`, `resume`, `clear`, and `compact`. Codex runs a
matching `SessionStart` hook after root compaction before the immediate model
continuation, so this adapter does not add a duplicate `PostCompact` handler.

`SubagentStart` receives different context. It requires the finite worker
packet, Markdown traversal receipt, and pinned contract closure. It does not tell an ordinary
worker to read unselected sibling contracts, the full root manual, or every
product-truth leaf unless the packet assigns an authority role requiring them.

After root compaction, the adapter instructs Codex to reopen the recorded
Markdown path, detect node or contract revision drift, and reread the selected
closure. Traversal restarts from the root only when the task changed or the prior path
is missing or ambiguous.

The hook reinforces `AGENTS.md`; it does not replace the instruction hierarchy
and cannot by itself prove that the model completed the reading pass. The
visible documents-read and Spec Basis receipt provide that accountability.

## Installation invariants

- Resolve the active Codex home instead of copying another user's path.
- For project installation, resolve the script from the Git root or install an
  exact absolute path appropriate to the platform.
- Preserve every existing hook source. Codex runs all matching hooks from all
  active sources; higher-precedence configuration does not replace lower-level
  hook definitions.
- Reconcile an equivalent hook rather than installing global and project
  duplicates.
- Use either `hooks.json` or inline `[hooks]` in one configuration layer, not
  both.
- Keep the script output concise and free of secrets.
- Non-managed new or changed hook definitions require review and trust in
  Codex. Report that step and verify the hook is not silently skipped.
- Project-local hooks require a trusted project `.codex/` layer.
- Do not change models, reasoning, providers, permissions, concurrency, or
  unrelated application configuration.

## Template placeholders

The global template requires:

- `__PYTHON_COMMAND__`
- `__CODEX_HOME__`
- Windows equivalents when applicable.

The project template uses Git-root resolution on macOS/Linux and requires an
absolute project path substitution for its Windows command.

## Verification

Run:

```sh
python3 -m unittest discover -s integrations/codex-lifecycle/tests -v
python3 -m json.tool integrations/codex-lifecycle/global-hooks.json.template >/dev/null
python3 -m json.tool integrations/codex-lifecycle/project-hooks.json.template >/dev/null
```

Then inspect active hook sources in Codex, complete trust review when required,
and verify one matching lifecycle adapter for the selected scope.
