# Operational Hygiene

- Node type: leaf
- Status: Active
- Contract: `bootstrap.governance.operational-hygiene@1`
- Clauses: `BOOTSTRAP.EVIDENCE.TEMPORARY`, `BOOTSTRAP.SSH.IDENTITY`
- Read when: installing work governance or handling run evidence and SSH identities.
- Do not read when: neither operational evidence nor SSH configuration is involved.
- Maximum size: 100 physical lines.

## Temporary run evidence

Generated stdout, stderr, exit statuses, timestamps, hashes, and auxiliary
receipts are temporary by default. Do not store them in the active agent home,
installed skill/package trees, or version-controlled configuration directories.
When capture is necessary, use a uniquely named task-scoped temporary directory
outside the source repository. Remove only this run's files after acceptance.

Durable cross-turn evidence needs a named consumer and explicit user, plan,
goal, runbook, or handoff requirement. Store the minimum in a non-repository
application-state location with a retention owner or cleanup condition; never
stage or commit it. Explicit deliverables and canonical selected tool outputs
follow their own output contracts. Do not delete pre-existing evidence merely
to enforce this policy.

## SSH identities

Use the operator's established SSH key and connection convention. Creating,
copying, replacing, installing, or selecting an additional key, or adding an
SSH-config identity, requires explicit approval for that exact operation.
Isolation or convenience alone does not authorize a new identity.

## Installation and verification

Install these rules through the work-governance tree and compact routing gate.
Installation changes no keys, SSH configuration, retained evidence, or target
product behavior. Verify target links, scope preservation, temporary defaults,
durability exceptions, and exact-operation authorization.
