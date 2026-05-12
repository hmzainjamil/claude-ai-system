# claude-ai-system

![v](https://img.shields.io/badge/version-2.0-blue?style=flat&labelColor=555) ![s](https://img.shields.io/badge/status-active-brightgreen?style=flat&labelColor=555) ![l](https://img.shields.io/badge/license-MIT-orange?style=flat&labelColor=555)

> Core infrastructure for the entire HMZ AI stack — MAE orchestrator, TCC task queue, hooks, model routing (Tier 0), llm-burst, G0DM0D3, CLAUDE.md rules, and all automation bins.

---

## 🧠 CONCEPTS

| Feature | Location | Description |
|---|---|---|
| [MAE Orchestrator](bin/mae) | `bin/mae` | Master Automation Engine — 12-agent swarm + cross-LLM blast + Groq synthesis |
| [TCC Queue](bin/tcc) | `bin/tcc` | Task queue — add/fire/list/retry/purge/blast tasks across all Tier 0 models |
| [TCC Dashboard](bin/tcc-dashboard) | `bin/tcc-dashboard` | Full system status: queue depth, RAM, model health, last run time |
| [llm-burst](bin/llm-burst) | `bin/llm-burst` | 15 models fire simultaneously — judge picks winner, Claude synthesizes result |
| [llm-burst Bytez](bin/llm-burst) | `bin/llm-burst` | bytez_query() added — 100+ free Bytez models participate in burst |
| [skill-auto-activate](bin/skill-auto-activate) | `bin/skill-auto-activate` | Hook script — keyword-scans every prompt and activates matching skills |
| [skill-search](bin/skill-search) | `bin/skill-search` | Full-text semantic search across all 200+ skill metadata and descriptions |
| [skill-on/off](bin/skill-on) | `bin/skill-on` | Toggle skills between active and archive — blockchain manifest updated |
| [auto-github-push](bin/auto-github-push) | `bin/auto-github-push` | PostToolUse hook — bin/ and skills/ files auto-synced to correct repos |
| [git-auto-init](bin/git-auto-init) | `bin/git-auto-init` | PostBash hook — initializes git on any new project directory |
| [memory-sync](bin/memory-sync) | `bin/memory-sync` | PostWrite hook — syncs memory files to Paperclip AI |
| [CLAUDE.md Rules](CLAUDE.md) | `CLAUDE.md` | Global AI rules: Tier 0 routing, L99 mode, OODA loop, skill gate |
| [MAE Daily](workflows/digiminds-daily.json) | `workflows/digiminds-daily.json` | Full DigiMinds daily ops workflow — all divisions run in sequence |
| [TCC Routes](tcc-routes/routes.json) | `tcc-routes/routes.json` | Task → agent routing map — 18 specialist agents registered |
| [Agent Registry](tcc-routes/agent-registry.json) | `tcc-routes/agent-registry.json` | 18 automation agents with model, division, and trigger keyword mapping |
| [LaunchAgents](launchd/) | `launchd/` | macOS LaunchAgent plists for Ollama, openclaw-bridge, MAE watchdog |
| [Hooks Config](hooks/) | `hooks/` | UserPromptSubmit, PostToolUse, Stop hook configurations |
| [Model Rules](config/model-rules.md) | `config/model-rules.md` | Tier 0 routing rules — which model for which task type |
| [RAM Guard](bin/ram-guard.sh) | `bin/ram-guard.sh` | Checks free RAM before Ollama burst — skips local if < 2GB |
| [Session Queue](session-queue.jsonl) | `session-queue.jsonl` | Auto-learn hook writes learnings — processed by Stop hook into memory |
| [TCC Logs](tcc-logs/) | `tcc-logs/` | All MAE run outputs saved as timestamped Markdown — full audit trail |
| [free-coding-models](bin/free-coding-models) | `bin/free-coding-models` | Pings 170 models across 16 providers — live latency + stability score |
| [OpenCLI Config](config/opencli.json) | `config/opencli.json` | OpenCLI adapter settings — Chrome profile, 90+ site configs |
| [Composio Config](config/composio.json) | `config/composio.json` | Composio 3000+ actions config — auth and tool routing |
| [health-check](bin/health.sh) | `bin/health.sh` | Pings all model endpoints — identifies dead APIs before burst mode |

### 🔥 Hot

| Feature | Location | Description |
|---|---|---|
| [MAE 12-Agent Swarm](bin/mae) | `bin/mae` | Default for every task — 12 agents + synthesis in ~8s, zero manual routing |
| [llm-burst 15 Models](bin/llm-burst) | `bin/llm-burst` | All 15 models fire in parallel — no single point of failure, judge picks best |
| [Tier 0 Zero-Cost](CLAUDE.md) | `CLAUDE.md` | 75-95% Claude token savings — Groq/Gemini/DeepSeek for all sub-tasks |
| [skill-auto-activate](bin/skill-auto-activate) | `bin/skill-auto-activate` | Every prompt auto-analyzed — correct skill loaded before response |
| [auto-github-push](bin/auto-github-push) | `bin/auto-github-push` | Write to ~/.claude/bin/ → instantly synced to GitHub, zero manual push |

---

## ⚙️ ARCHITECTURE

```
┌──────────────────────────────────────────────────────────────────┐
│               CLAUDE-AI-SYSTEM v2.0                             │
│                                                                  │
│  Every Prompt → UserPromptSubmit hook → skill-auto-activate     │
│                        │                                        │
│              ┌─────────▼──────────────┐                        │
│              │   MAE ORCHESTRATOR     │                        │
│              │  Phase 1: Groq decomposes goal → sub-tasks      │
│              │  Phase 2: 12 specialist agents fire parallel     │
│              │  Phase 3: Groq+Gemini+DeepSeek cross-LLM blast  │
│              │  Phase 4: Groq-70B synthesizes → final output   │
│              └─────────────────────────────────────────────────┘│
│                        │                                        │
│  TCC queue → wave batching → Tier 0 cloud + Ollama local       │
│  Output auto-saved → ~/.claude/tcc-logs/ + Paperclip sync      │
└──────────────────────────────────────────────────────────────────┘
```

| Layer | Technology | Purpose |
|---|---|---|
| Orchestration | MAE + TCC | Decompose → specialist swarm → synthesize |
| Model Layer | Groq / Gemini / DeepSeek / Bytez | Tier 0 zero-cost routing |
| Memory | Paperclip + ~/.claude/tcc-logs/ | Cross-session persistent context |
| Routing | skill-router + keyword map | Auto-activate correct skill per prompt |
| Hooks | PostToolUse / Stop / SessionStart | Auto-sync, memory, health checks |

---

## 🚀 Quick Start

```bash
# Run 12-agent swarm on any goal
mae run "write a cold email sequence for B2B SaaS"

# Fire 3 tasks in parallel
tcc blast "audit Google Ads" "spy Meta ads" "write LinkedIn post"

# Full agency daily ops
mae daily

# 15 models in parallel on one prompt
~/.claude/bin/llm-burst "what is our best GTM strategy for Q3"

# Check live model latency across 170 models
~/.claude/bin/free-coding-models

# System status
tcc-dashboard
```

---

## 💡 TIPS AND TRICKS (72)

<a id="tips-mae_orchestration_6"></a>
### ■ **MAE Orchestration (6)**
| Tip | Source |
|---|---|
| mae run 'goal' = 12-agent swarm + synthesis in ~8 seconds — default | [MAE](https://github.com/hmzainjamil/claude-ai-system) |
| tcc blast 't1' 't2' = parallel fire multiple tasks — 8x faster than sequential | [TCC](https://github.com/hmzainjamil/claude-ai-system) |
| mae daily = full DigiMinds agency operations automated in one command | [MAE](https://github.com/hmzainjamil/claude-ai-system) |
| tcc fire all = execute entire pending queue in parallel wave batches | [TCC](https://github.com/hmzainjamil/claude-ai-system) |
| tcc-dashboard = full system status: queue, RAM, model health, last run | [tcc-dashboard](https://github.com/hmzainjamil/claude-ai-system) |
| All MAE outputs auto-saved to ~/.claude/tcc-logs/ as timestamped Markdown | [tcc-logs](https://github.com/hmzainjamil/claude-ai-system) |

<a id="tips-model_routing_6"></a>
### ■ **Model Routing (6)**
| Tip | Source |
|---|---|
| Always Tier 0 first — Ollama→Groq→Gemini→Bytez→OpenRouter→DeepSeek→Claude | [CLAUDE.md](https://github.com/hmzainjamil/claude-ai-system) |
| Groq llama3-70b: sub-500ms, best for synthesis and analysis tasks | [Groq](https://console.groq.com) |
| Gemini 2.0 Flash: free, 1M context — use for long document analysis | [Google AI](https://ai.google.dev) |
| DeepSeek-V3 via OpenRouter: best free code model, beats GPT-4o on code | [OpenRouter](https://openrouter.ai) |
| Bytez API: 100+ free models — cb4a7065a586ec6ca26394724ce5ec49 | [Bytez](https://bytez.com) |
| caveman compression: 60-80% token savings on every response automatically | [caveman](https://github.com/hmzainjamil/claude-ai-skills) |

<a id="tips-hooks_6"></a>
### ■ **Hooks (6)**
| Tip | Source |
|---|---|
| UserPromptSubmit → skill-auto-activate → keyword scan → correct skill loaded | [hooks](https://github.com/hmzainjamil/claude-ai-system) |
| PostToolUse Write/Edit → auto-github-push → bin/ and skills/ auto-synced | [hooks](https://github.com/hmzainjamil/claude-ai-system) |
| Stop hook → session-queue.jsonl → memory files updated for next session | [hooks](https://github.com/hmzainjamil/claude-ai-system) |
| compact-guard hook fires before context overflow — prevents wasteful re-runs | [compact-guard](https://github.com/hmzainjamil/claude-ai-skills) |
| All hooks run async < 200ms — never block the main conversation thread | [settings.json](https://github.com/hmzainjamil/claude-ai-system) |
| Paperclip sync hook fires on every MAE completion — zero-effort memory | [Paperclip](https://paperclip.ai) |

<a id="tips-memory_6"></a>
### ■ **Memory (6)**
| Tip | Source |
|---|---|
| ~/.claude/projects/ MEMORY.md index loads every session — full context | [MEMORY.md](https://github.com/hmzainjamil/claude-ai-system) |
| Paperclip AI ingests all outputs — searchable company OS across sessions | [Paperclip](https://paperclip.ai) |
| Auto-learn hook writes learnings to session-queue.jsonl on every prompt | [auto-learn](https://github.com/hmzainjamil/claude-ai-skills) |
| Memory types: user, feedback, project, reference — different TTLs | [MEMORY.md](https://github.com/hmzainjamil/claude-ai-system) |
| Never save code patterns to memory — read code directly every session | [CLAUDE.md](https://github.com/hmzainjamil/claude-ai-system) |
| Stale memories: verify before acting — git log / grep for current state | [CLAUDE.md](https://github.com/hmzainjamil/claude-ai-system) |

<a id="tips-token_savings_6"></a>
### ■ **Token Savings (6)**
| Tip | Source |
|---|---|
| 75-95% Claude token savings via Tier 0 routing — enforced on every task | [CLAUDE.md](https://github.com/hmzainjamil/claude-ai-system) |
| Never re-read files already in context — agent state persists per session | [CLAUDE.md](https://github.com/hmzainjamil/claude-ai-system) |
| Batch all parallel tasks in one tcc blast — fewer round-trips = fewer tokens | [TCC](https://github.com/hmzainjamil/claude-ai-system) |
| Use --jq on GH API calls — returns only the field needed, not full JSON | [gh CLI](https://cli.github.com) |
| Wave batching: cloud APIs first, Ollama last (if RAM > 2GB free) | [CLAUDE.md](https://github.com/hmzainjamil/claude-ai-system) |
| Skip verification steps on internal code — trust framework guarantees | [CLAUDE.md](https://github.com/hmzainjamil/claude-ai-system) |

<a id="tips-skills_6"></a>
### ■ **Skills (6)**
| Tip | Source |
|---|---|
| Core 10 skills always active — never deactivate caveman/compact-guard/etc | [CLAUDE.md](https://github.com/hmzainjamil/claude-ai-system) |
| skill-auto-activate runs on every prompt — correct skill auto-loaded | [skill-router](https://github.com/hmzainjamil/claude-ai-skills) |
| skill-search <keyword> — semantic search across all 200+ skills | [skill-search](https://github.com/hmzainjamil/claude-ai-skills) |
| skill-on/skill-off toggle — moves between active and skills-archive/ | [skill-on](https://github.com/hmzainjamil/claude-ai-skills) |
| Always deactivate non-core skills after task — collapse back to baseline | [CLAUDE.md](https://github.com/hmzainjamil/claude-ai-system) |
| skills-lock.json: blockchain manifest — dep tracking, version hashes | [skills-lock](https://github.com/hmzainjamil/claude-ai-skills) |

<a id="tips-git_/_github_6"></a>
### ■ **Git / GitHub (6)**
| Tip | Source |
|---|---|
| Always use GitHub Contents API for README pushes — avoids symlink conflicts | [gh CLI](https://cli.github.com) |
| Re-fetch SHA before every PUT — never cache SHA across multiple pushes | [GitHub API](https://docs.github.com) |
| auto-github-push hook: Write/Edit to ~/.claude/bin/ → auto-synced | [hooks](https://github.com/hmzainjamil/claude-ai-system) |
| Conventional commits: feat/fix/docs/chore — searchable history | [git](https://conventionalcommits.org) |
| Never push secrets — auto-github-push hook scrubs API keys before commit | [hooks](https://github.com/hmzainjamil/claude-ai-system) |
| Use git worktrees for parallel feature work — isolated branches per agent | [git](https://git-scm.com) |

<a id="tips-opencli_6"></a>
### ■ **OpenCLI (6)**
| Tip | Source |
|---|---|
| v1.7.18 installed: /Users/mc/.nvm/versions/node/v24.14.1/bin/opencli | [npm](https://npmjs.com) |
| 90+ site adapters — GitHub, LinkedIn, Notion, Jira, Figma, Confluence, Slack | [OpenCLI](https://github.com/jackwener/opencli) |
| Zero LLM cost — Chrome session + adapter, no AI API calls consumed | [OpenCLI](https://github.com/jackwener/opencli) |
| Persistent Chrome session — never triggers re-login flows between calls | [OpenCLI](https://github.com/jackwener/opencli) |
| opencli linkedin search — lead scraping without LinkedIn API rate limits | [OpenCLI](https://github.com/jackwener/opencli) |
| Wire OpenCLI actions into MAE: mae run triggers opencli adapters for data | [MAE](https://github.com/hmzainjamil/claude-ai-system) |

<a id="tips-launchagents_6"></a>
### ■ **LaunchAgents (6)**
| Tip | Source |
|---|---|
| KeepAlive=true + RunAtLoad=true = always-on service that survives reboots | [launchd](https://developer.apple.com) |
| Set HOME + PATH in EnvironmentVariables — scripts find all tools | [launchd](https://developer.apple.com) |
| Log stdout/stderr to /tmp/ — check if LaunchAgent crashes silently | [launchd](https://developer.apple.com) |
| Reload: launchctl unload then load — applies plist config changes | [launchd](https://developer.apple.com) |
| ThrottleInterval=10 — prevents restart loop on persistent crash | [launchd](https://developer.apple.com) |
| launchctl list | grep ai.hmz — verify all services are running | [launchd](https://developer.apple.com) |

<a id="tips-n8n_workflows_6"></a>
### ■ **n8n Workflows (6)**
| Tip | Source |
|---|---|
| 8,159 workflows in index — grep before building any automation from scratch | [n8n](https://github.com/hmzainjamil/hmz-n8n-workflows) |
| Error workflow: connect all nodes → Slack alert + retry on any failure | [n8n](https://n8n.io) |
| Queue mode + Redis: handles 1000+ concurrent workflow executions | [n8n](https://n8n.io) |
| Deploy any workflow: bash bin/deploy.sh workflows/my-flow.json | [n8n](https://github.com/hmzainjamil/hmz-n8n-workflows) |
| Split In Batches node: process 10K+ records without OOM errors | [n8n](https://n8n.io) |
| MAE bridge: mae run triggers n8n workflows for execution-heavy steps | [MAE](https://github.com/hmzainjamil/claude-ai-system) |

<a id="tips-debugging_6"></a>
### ■ **Debugging (6)**
| Tip | Source |
|---|---|
| tcc-dashboard — system status: queue depth, RAM, model health, last run | [tcc-dashboard](https://github.com/hmzainjamil/claude-ai-system) |
| ~/.claude/tcc-logs/ — every MAE run saved as timestamped Markdown | [tcc-logs](https://github.com/hmzainjamil/claude-ai-system) |
| mae plan 'goal' — preview decomposition before committing to full run | [MAE](https://github.com/hmzainjamil/claude-ai-system) |
| OODA on failures: Observe error → Orient cause → Decide fix → Act | [CLAUDE.md](https://github.com/hmzainjamil/claude-ai-system) |
| health.sh pings all model endpoints — identifies dead APIs before blast | [health.sh](https://github.com/hmzainjamil/claude-ai-agents) |
| llm-burst --json 'prompt' — see all model scores before synthesis | [llm-burst](https://github.com/hmzainjamil/claude-ai-system) |

<a id="tips-paperclip_os_6"></a>
### ■ **Paperclip OS (6)**
| Tip | Source |
|---|---|
| Paperclip AI = always-on zero-human company OS — autopilot co-founder layer | [Paperclip](https://paperclip.ai) |
| All MAE run outputs auto-synced to Paperclip — full searchable audit trail | [Paperclip](https://paperclip.ai) |
| Set Paperclip to auto-approve low-risk decisions — true zero-human ops | [Paperclip](https://paperclip.ai) |
| Paperclip ingests n8n automation outputs via webhook → structured memory | [Paperclip](https://paperclip.ai) |
| Cross-session context: Paperclip + MEMORY.md = never lose context again | [Paperclip](https://paperclip.ai) |
| Paperclip dashboard shows all autonomous decisions — review weekly | [Paperclip](https://paperclip.ai) |

---

## ☠️ STARTUPS / BUSINESSES

| Feature | Replaced |
|---|---|
| MAE 12-agent orchestration | [CrewAI](https://crewai.com) |
| Tier 0 model routing | [LiteLLM](https://litellm.ai) |
| 15-model parallel burst | [Together AI](https://together.ai) |
| Skill blockchain gate | [npm package-lock](https://npmjs.com) |
| Auto GitHub push hook | [GitHub Actions](https://github.com/features/actions) |
| 170-model latency benchmarker | [OpenLLM](https://github.com/bentoml/openllm) |
| Session persistent memory | [Mem.ai](https://mem.ai) |
| Task queue + routing | [Linear](https://linear.app) |
| Cross-LLM synthesis judge | [Helicone](https://helicone.ai) |
| Daily ops automation | [n8n](https://n8n.io) |
| Paperclip company OS | [Notion AI](https://notion.ai) |
| RAM-aware wave batching | [Docker Compose](https://docker.com) |
| Webhook triggers | [Zapier](https://zapier.com) |
| Health monitoring | [Datadog](https://datadoghq.com) |
| Skill auto-routing | [LangChain](https://langchain.com) |

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=hmzainjamil/claude-ai-system&type=Date)](https://star-history.com/#hmzainjamil/claude-ai-system&Date)
