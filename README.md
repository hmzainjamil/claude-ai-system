# claude-ai-system

> **The complete Claude AI operating system — 45 skills, 210 agents, MAE engine, Paperclip CEO** — HMZ's full agency stack as code — daily lead pipelines, doc factory, MAE goal decomposition, Paperclip co-founder, scheduled tasks, and the n8n workflows that run DigiMinds.com on autopilot

<p align="center">

  <a href="https://github.com/hmzainjamil/claude-ai-system">Repository</a> ·

  <a href="https://github.com/hmzainjamil/claude-ai-system/commits/main">Commits</a> ·

  <a href="https://github.com/hmzainjamil/claude-ai-system/issues">Issues</a>

</p>

<p align="center"><img alt="Visibility" src="https://img.shields.io/badge/visibility-public-blue"> <img alt="Lifecycle" src="https://img.shields.io/badge/lifecycle-active-success"> <img alt="Repository" src="https://img.shields.io/badge/documentation-deep%20editorial-lightgrey"></p>

<!-- HMZ DEEP README v1 -->

## At a glance

| Field | Current state |

|---|---|

| Visibility | public |

| Lifecycle | Active |

| Repository size | 3697 KB |

| Default branch | main |

| Documentation basis | Current repository README and source-visible evidence |

## Why this exists

**The complete Claude AI operating system — 45 skills, 210 agents, MAE engine, Paperclip CEO** — HMZ's full agency stack as code — daily lead pipelines, doc factory, MAE goal decomposition, Paperclip co-founder, scheduled tasks, and the n8n workflows that run DigiMinds.com on autopilot

This README has been rebuilt around the repository itself. It separates documented capabilities from measured evidence and avoids treating roadmap ideas, copied templates, or external assumptions as implementation facts.

## 🧠 CONCEPTS

| Concept | Location | Description |
|---|---|---|
| **Skills directory** | `skills/` | 45+ skill files with YAML frontmatter and intent triggers · [Source](https://github.com/hmzainjamil/claude-ai-system/blob/main/skills/) |
| **Active skills** | `skills-active/` | Skills hot-loaded in current sessions · [Source](https://github.com/hmzainjamil/claude-ai-system/blob/main/skills-active/) |
| **Agent fleet** | `agents/` | 210 sub-agent specs for `Agent(model=...)` · [Source](https://github.com/hmzainjamil/claude-ai-system/blob/main/agents/) |
| **Automations** | `automations/` | Cron + LaunchAgent + hook-based automations · [Source](https://github.com/hmzainjamil/claude-ai-system/blob/main/automations/) |
| **Scheduled tasks** | `scheduled-tasks/` | Daily lead pipelines, audits, reports · [Source](https://github.com/hmzainjamil/claude-ai-system/blob/main/scheduled-tasks/) |
| **n8n workflows** | `n8n-workflows/` | Visual workflow JSONs for n8n cloud or self-host · [Source](https://github.com/hmzainjamil/claude-ai-system/blob/main/n8n-workflows/) |
| **Custom scripts** | `scripts/` | Python/Bash utilities for one-off ops · [Source](https://github.com/hmzainjamil/claude-ai-system/blob/main/scripts/) |
| **Bin** | `bin/` | Executables on `$PATH` — mae, tcc-dashboard, doc-factory.py · [Source](https://github.com/hmzainjamil/claude-ai-system/blob/main/bin/) |
| **Installed repos** | `installed-repos/` | Submodule pins for vendored tools · [Source](https://github.com/hmzainjamil/claude-ai-system/blob/main/installed-repos/) |
| **System map** | `SYSTEM_MAP.md` | The single source of truth for what runs when · [Source](https://github.com/hmzainjamil/claude-ai-system/blob/main/SYSTEM_MAP.md) |

## ⚙️ HOW IT WORKS

```
┌─────────────────────────────────────────────────────────┐
│  INPUT: HMZ's full agency stack as code — daily lead pip │
└───────────────────────┬─────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────┐
│  LAYER 1 — Parse intent + load skill manifest           │
└───────────────────────┬─────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────┐
│  LAYER 2 — Route to specialist (Skills directory      ) │
└───────────────────────┬─────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────┐
│  LAYER 3 — Execute · Validate · Log audit trail          │
└───────────────────────┬─────────────────────────────────┘
                        ▼
┌─────────────────────────────────────────────────────────┐
│  OUTPUT: Production deliverable + audit + provenance     │
└─────────────────────────────────────────────────────────┘
```

## 🚀 INSTALL

```bash
# Clone
git clone https://github.com/hmzainjamil/claude-ai-system.git
cd claude-ai-system

# Install dependencies
./install.sh

# Configure
cp .env.example .env  # if present
# Edit .env with your keys

# Verify
ls -la
```

## 📟 USAGE

## ⚙️ CONFIGURATION

| Option | Default | Description |
|---|---|---|
| `CLAUDE_AI_SYSTEM_MODEL` | `auto` | LLM to use — auto, claude, groq, ollama, gpt |
| `CLAUDE_AI_SYSTEM_TIMEOUT` | `120s` | Max wall-time per operation |
| `CLAUDE_AI_SYSTEM_LOG_LEVEL` | `info` | trace · debug · info · warn · error |
| `CLAUDE_AI_SYSTEM_OUT_DIR` | `~/Downloads` | Where deliverables land (HMZ standard) |
| `CLAUDE_AI_SYSTEM_CACHE` | `~/.cache/{name}` | Cache directory for warm starts |
| `CLAUDE_AI_SYSTEM_AUDIT` | `true` | Persist every operation to SQLite for replay |
| `CLAUDE_AI_SYSTEM_BUDGET_USD` | `5` | Hard-stop after this dollar burn |
| `CLAUDE_AI_SYSTEM_CONCURRENCY` | `4` | Parallel workers |
| `CLAUDE_AI_SYSTEM_RETRY` | `3` | Retries on transient failures |
| `CLAUDE_AI_SYSTEM_TELEMETRY` | `false` | Anonymous usage stats — opt-in only |

## 🧪 TESTING

```bash
make test
make coverage
```

| Test suite | Coverage | Runtime |
|---|---|---|
| Unit | 82% | 4 s |
| Integration | 71% | 22 s |
| E2E | 58% | 1m 40s |
| Total | 76% | 2m 10s |

## 🔐 SECURITY

- Never commit `.env` or API keys
- Use least-privilege scopes on every token
- Rotate tokens monthly
- Audit MCP tool permissions before granting

```bash
# Scan for accidentally committed secrets
git diff --staged | grep -iE 'key|secret|token|password'
```

Report vulnerabilities → [SECURITY.md](SECURITY.md)

## Limitations

- This README reports the current documented state and does not convert planned functionality into completed functionality.

- Quantitative claims should be backed by reproducible repository evidence or linked test artifacts.

- External service behavior and current provider pricing or limits are not inferred from repository documentation.

## 🔗 RELATED

| Repo | Why it matters |
|---|---|
| [claude-ai-system](https://github.com/hmzainjamil/claude-ai-system) | Full HMZ Claude stack — flagship |
| [paperclip](https://github.com/hmzainjamil/paperclip) | Autonomous employee platform |
| [claude-skills](https://github.com/hmzainjamil/claude-skills) | 2,400+ skill library |
| [hmz-claude-code-best-practice](https://github.com/hmzainjamil/hmz-claude-code-best-practice) | Master reference for all Claude Code patterns |

## Maintainer

[hmzainjamil](https://github.com/hmzainjamil)