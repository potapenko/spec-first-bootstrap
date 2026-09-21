# Codex Lifecycle Adapter Retirement

- Node type: leaf
- Status: Active
- Contract ID: `bootstrap.codex-lifecycle`
- Domain ID: `bootstrap.codex-lifecycle`
- Authority: Active
- Stability: Evolving
- Contract revision: `bootstrap.codex-lifecycle@4`
- Clauses: `CODEX.LIFECYCLE.INSTALL`, `CODEX.LIFECYCLE.MIGRATE`
- Read when: handling legacy adapter entrypoints or migrating an existing installation.
- Do not read when: only portable context recovery is involved.
- Maximum size: 100 physical lines.

## Retirement

Bootstrap no longer ships or installs lifecycle reminder scripts or hook
templates. Legacy setup entrypoints explain retirement and link to migration;
invoking an old install prompt does not authorize removal of existing hooks.
Portable recovery follows
[restart and delivery](bootstrap-governance/restart-and-delivery.md).

## Explicit migration

Migration is independently authorized for one named project or active user
configuration. Ordinary setup and repair preserve existing hook registrations.
Do not disable the general hooks feature or replace a whole hooks collection.

Inspect the selected configuration, registrations, and referenced script before
editing. Match Bootstrap provenance, exact command target, and script content
against a known historical revision. A basename or event name alone is not proof.
Remove only proven Bootstrap reminder commands, preserving sibling commands,
events, metadata, and unrelated sources. Customized or uncertain entries remain
unchanged with an exact residual. Stop that slice if the format cannot be edited
while preserving unrelated content.

Delete a proven legacy script only after all its references in the inspected
sources are gone and no remaining ownership is uncertain. Never execute a
candidate hook to identify it. Reconcile only obsolete Bootstrap rereading text
in the authorized instruction chain; preserve safety and product contracts.

## Verification

Use the [migration prompt](../../../prompts/migrate-codex-lifecycle.md).
Inspect a bounded proposed diff, parse the edited representation, compare
unrelated hook configuration, and verify no dangling removed-script references.
Mixed-hook, customized-script, already-retired, and wrong-scope cases must be
covered. Report uninspected sources and do not claim global hook absence from
one empty user configuration. No live migration is implied by updating Bootstrap.
