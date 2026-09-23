# Retired Codex Lifecycle Setup (Project)

The legacy mandatory-rereading adapter is retired. Do not install or recreate
scripts, hook registrations, or mandatory rereading gates from historical versions.
Context recovery now uses available, applicable, current context and loads missing,
potentially changed, or uncertain required documents completely.

This legacy installation entrypoint is informational and changes no files.
It does not authorize removing existing hooks or changing the general hooks feature.

For an explicit request to remove the old adapter from one named project, use
[the migration prompt](migrate-codex-lifecycle.md). Preserve other hook sources,
settings, and product/safety instructions. Ordinary setup never performs migration.

The new [optional context reminder](setup-codex-context-reminder.md) has its own
explicit opt-in prompt; this legacy entrypoint does not select or install it.
