# Documentation index

Repository documentation map, ownership, and confidence. The repository is a personal configuration snapshot; guides describe files, not proof of live operation.

| Document | Role | Evidence and limits |
|---|---|---|
| [Getting started](getting-started.md) | Safe inspection and selective adaptation | Commands are examples; review each file before use |
| [Architecture](architecture.md) | Conceptual overview | Historical claims; verify against current scripts and Claude Code behavior |
| [Skills reference](skills-reference.md) | Skill inventory | Generated snapshot dated 2026-05-10; may be stale |
| [Agents reference](agents-reference.md) | Agent inventory | Generated snapshot dated 2026-05-10; may be stale |
| [Terminology](terminology.md) | Project vocabulary | Definitions do not establish implementation |
| [System map](../SYSTEM_MAP.md) | Historical triggers, flows, and schedules | Verify every path and external integration before relying on it |
| [Security notice](../SECURITY.md) | Credential handling notes | Its claims are not a scan or security certification |
| [Root README](../README.md) | Repository purpose, scope, and navigation | Describes checked-in content and explicit limits |

## Update rules

- Update the relevant page when a supported source path or user-facing workflow changes.
- Mark generated inventories with their generation date and source command. Do not hand-edit generated output as if it were current.
- State command results only after running them; include environment and date.
- Distinguish checked-in configuration from enabled or functioning runtime behavior.
- Preserve upstream attribution for material under `installed-repos/`; verify redistribution terms before publishing changes to copied material.
