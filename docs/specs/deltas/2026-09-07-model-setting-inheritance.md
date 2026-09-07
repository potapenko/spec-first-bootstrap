# Model Setting Inheritance

- Change ID: `bootstrap.delta.2026-09-07.model-setting-inheritance`
- Mode: Evolve
- Authority: user approved inheritance, optional recommendations, and justified
  overrides on 2026-09-07 after the read-only model-policy audit.
- Domain and clause: `bootstrap.governance`, `BOOTSTRAP.ECONOMY`.
- Revisions: `bootstrap.governance@16` → `bootstrap.governance@17`;
  `bootstrap.governance.restart-delivery@4` → `bootstrap.governance.restart-delivery@5`.

## Before and after

Worker packets required assigned models and reasoning effort. The policy
required task-based selection and prohibited maximum capability by default.
Now ordinary work and workers inherit the user's current settings, including a
chosen high-capability model. Overrides are optional, permitted by the host and
user constraints, and justified by a concrete task property. Recommendations
remain advisory without generation names, fixed tiers, or role mappings.

`inherit` describes policy; it is not sent as a model ID. Overrides use current
host capabilities. Unsupported overrides preserve usable inherited settings or
produce an exact limitation instead of invented aliases or silent substitution.

## Evidence, compatibility, and acceptance

The audit inspected portable and installed orchestration, compact global rules,
local configuration, and policy history. Names were already portable, but
mandatory assignments and maximum-capability restrictions remained.
This is an authorized default-policy change; explicit user choices, host/tool
constraints, installation boundaries, application configuration, goal execution,
review gates, permissions, and unrelated local differences remain protected.

Changed specification owners: [governance](../features/bootstrap-governance.md)
and [restart and delivery](../features/bootstrap-governance/restart-and-delivery.md).
There is no UI change. Acceptance uses focused policy review, installation
fixtures, Markdown validation, and [model-policy scenarios](../../../qa/cases/minimum-sufficient-work.md).
Structural checks establish instruction consistency, not future model obedience.
