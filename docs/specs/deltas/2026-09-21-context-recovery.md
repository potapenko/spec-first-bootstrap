# Context Recovery and Lifecycle Adapter Retirement

- Change ID: `2026-09-21-context-recovery`
- Mode: Evolve
- Authority: user approved the investigated transfer on 2026-09-21: “Хорошо, делай.”
- Domains: Bootstrap governance and Codex lifecycle.
- Clauses: `BOOTSTRAP.INSTALL`, `BOOTSTRAP.RESTART`,
  `PT.LIFECYCLE.RESTORE`, `PT.ROUTE.TRAVERSE`, `CODEX.LIFECYCLE.INSTALL`,
  `CODEX.LIFECYCLE.MIGRATE`, `BOOTSTRAP.EVIDENCE.TEMPORARY`, `BOOTSTRAP.SSH.IDENTITY`.

## Before and after

Previously, lifecycle recovery required rereading applicable instructions and
selected contracts. Optional installers deployed mandatory reminder hooks.
Recovery now reuses available, applicable, current context and loads complete
documents plus dependencies only when missing, potentially changed, or uncertain.
Summaries preserve continuity without creating authority. Scope, revision drift,
paused goals, product contracts, and acceptance requirements remain protected.

The old adapter is retired. Legacy setup prompts cannot reinstall it or silently
remove a user's hooks. A separate, explicitly scoped migration preserves all
unrelated configuration and removes only proven Bootstrap reminders.

Work governance also carries temporary-evidence hygiene and exact-operation
authorization for additional SSH identities. No actual key operations occur.

## Evidence and compatibility

Donor evidence: global configuration commits dba2899 and 8562ca1 on 2026-09-21;
temporary evidence rule 4dc30b6; SSH rule b0356df. Local settings, model IDs,
product naming rules, display configuration, and plugins are not portable defaults.
QA/Computer Use reorganization is deferred to a separate change.

This deliberately retires the optional installer and changes recovery semantics.
Historical deltas remain historical. Ordinary setup does not migrate live hooks.
Current-branch checkpoints, explicit delegation, product routing, and independent
acceptance standards remain unchanged. This task changes only Bootstrap files.

Revisions: aggregate @19; installation @5; restart-delivery @7;
product-truth coordination @2 and routing @2; lifecycle @4; operational-hygiene @1.

Verification: structural and installed-layout checks, absence of installable hook
artifacts, recovery/migration scenarios, links, node limits, and focused self-review.
No live migration or empirical model-obedience claim follows from text checks.
