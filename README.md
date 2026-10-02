# Claude AI System

A public snapshot of Claude Code skills, agent definitions, scripts, configuration notes, scheduled-task files, workflow assets, and selected documentation from one personal macOS setup. This repository is a reference and source archive. It is not a verified one-command installer or a supported general-purpose agent platform.

## Status

| Item | Current evidence |
|---|---|
| Repository | Public GitHub repository |
| Intended environment | Personal Claude Code setup; many scripts and paths are macOS or user specific |
| Install status | No root `install.sh` or `.env.example` is present |
| Verification | This documentation change did not run the scripts, workflows, or tests |
| Release | No release or compatibility promise is made here |

## What is here

- `skills/` and `skills-active/`: skill content and active-set snapshot
- `agents/`: agent definition files
- `bin/` and `automations/`: command-line scripts and automation assets
- `scheduled-tasks/`, `n8n-workflows/`: task and workflow files; external services and schedules are not verified by their presence
- `config/`: setup notes, settings, and architecture records
- `docs/`: getting-started notes, architecture overview, and skill/agent references
- `installed-repos/`: selected README/documentation snapshots from other projects; these are not complete upstream checkouts, so some relative links may point to files or assets not included here. Content may be stale and retains upstream ownership.
- `SYSTEM_MAP.md`: historical system map. Verify every path, trigger, provider, schedule, and delivery step before relying on it

See the [documentation index](docs/README.md) for the guides and their evidence status.

## Safe way to explore

1. Read [getting started](docs/getting-started.md), [security notes](SECURITY.md), and [the system map](SYSTEM_MAP.md).
2. Inspect a skill or script before using it. Check paths, permissions, network calls, data access, and write/send actions.
3. Adapt only the files you understand to your own Claude Code configuration. Back up existing settings first.
4. Configure credentials outside the repository. Never copy personal configuration, tokens, or private data into a public fork.

No blanket copy command is provided: the checked-in scripts include personal paths and automation that may interact with external accounts or send data.

## Evidence and maintenance

Repository contents prove that files are checked in. They do not prove that a hook is installed, a scheduled task is enabled, a service is reachable, a workflow succeeds, or a model/provider is available. Treat counts and operational descriptions in older documents as unverified until regenerated or checked against current source.

When changing this snapshot, update the relevant guide and reference links in the same change. Record tested commands and their results with the environment and date. Do not describe a workflow as working based only on a configuration file.

## Security and privacy

This repository contains executable automation and third-party workflow material. Review each file before running it. Some assets refer to personal directories, account integrations, lead-generation, email, browser automation, and external model APIs. Their presence does not establish that credentials are included or removed. Check the actual diff and file contents before publishing or deploying a copy.

Report a suspected exposure through the repository's private security contact process; do not post secrets in a public issue. See [SECURITY.md](SECURITY.md).

## Limits

- Compatibility with current Claude Code, macOS, external APIs, and MCP servers has not been established by this README.
- Historical architecture and schedule documents can diverge from scripts or live machine state.
- References to other repositories under `installed-repos/` are copied documentation, not maintained upstream releases.

## Repository

- [Source](https://github.com/hmzainjamil/claude-ai-system)
- [Issues](https://github.com/hmzainjamil/claude-ai-system/issues)
- [Documentation](docs/README.md)
