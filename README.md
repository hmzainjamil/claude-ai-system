# claude-ai-system
Production-grade Claude Code harness — hooks, bin scripts, agents, LaunchAgents, and full automation OS.

![hooks](https://img.shields.io/badge/hooks-PostToolUse%20%7C%20UserPromptSubmit-blue?style=flat&labelColor=555)
![scripts](https://img.shields.io/badge/bin_scripts-45%2B-green?style=flat&labelColor=555)
![platform](https://img.shields.io/badge/platform-macOS-lightgrey?style=flat&labelColor=555)
![tier0](https://img.shields.io/badge/model-Tier0%20first-orange?style=flat&labelColor=555)
![license](https://img.shields.io/badge/license-MIT-blue?style=flat&labelColor=555)

[Concepts](#-concepts) · [Architecture](#️-architecture) · [Tips](#-tips-and-tricks-24) · [Kills](#️-startups--businesses) · [Stars](#star-history)

## 🧠 CONCEPTS

| Feature | Location | Description |
|---------|----------|-------------|
| [**Skill Router**](automations/bin/skill-router) | `automations/bin/skill-router` | Keyword-match prompt → auto-activate skills before response [![active](https://img.shields.io/badge/status-always_on-brightgreen?style=flat&labelColor=555)] |
| [**Auto GitHub Push**](automations/bin/auto-github-push) | `automations/bin/auto-github-push` | PostToolUse hook — any Write/Edit to bin/skills auto-pushes to GitHub via Contents API |
| [**Skill On/Off**](automations/bin/skill-on) | `automations/bin/skill-on` | Blockchain-gated skill activation — on-demand, never always-loaded |
| [**Compact Guard**](automations/bin/compact-guard) | `automations/bin/compact-guard` | Enforces context compression before token limit hit |
| [**LLM Burst**](automations/bin/llm-burst) | `automations/bin/llm-burst` | Cloud-first Tier 0 routing — Groq → OpenRouter → Gemini → Claude last |
| [**GitHub Portfolio Sync**](automations/bin/github-sync) | `automations/bin/github-sync` | Daily sync of all local scripts to GitHub repos via Contents API |
| [**Auto Troubleshoot**](automations/bin/auto-troubleshoot) | `automations/bin/auto-troubleshoot` | SessionStart hook — scans LaunchAgents, checks logs, flags stale jobs |
| [**OODA Loop**](automations/bin/ooda) | `automations/bin/ooda` | Observe-Orient-Decide-Act injected into every UserPromptSubmit |
| [**Caveman Compress**](automations/bin/caveman) | `automations/bin/caveman` | Strips filler, collapses whitespace — 60-80% token reduction on all outputs |
| [**Session Queue**](automations/bin/session-queue) | `automations/bin/session-queue` | Writes learnings to ~/.claude/session-queue.jsonl — processed by Stop hook |
| [**Skill Search**](automations/bin/skill-search) | `automations/bin/skill-search` | fzf-powered fuzzy search across 200+ skills in archive |
| [**OpenClaw Bridge**](automations/bin/openclaw-bridge) | `automations/bin/openclaw-bridge` | Gateway to Open Design / OpenClaw local MCP server |

### 🔥 Hot

| Feature | Location | Description |
|---------|----------|-------------|
| [**Tier 0 Prompt Inject**](automations/bin/tier0-prompt-inject) | `automations/bin/tier0-prompt-inject` | Injects G0DM0D3 routing rules into every session — zero Claude tokens for sub-tasks |
| [**Auto Learn**](automations/bin/auto-learn) | `automations/bin/auto-learn` | Stop hook — converts session-queue.jsonl to persistent memory files automatically |
| [**GitHub Sweep**](automations/bin/github-sweep) | `automations/bin/github-sweep` | Discovers new local scripts and pushes to correct GitHub repo with right path |

## ⚙️ ARCHITECTURE

```
~/.claude/
├── bin/                    ← 45+ automation scripts (auto-pushed to this repo)
│   ├── skill-on            ← activate skill from archive
│   ├── skill-off           ← deactivate + collapse
│   ├── skill-router        ← keyword → skill map (fires on UserPromptSubmit)
│   ├── auto-github-push    ← PostToolUse: Write/Edit → GitHub API
│   ├── llm-burst           ← Tier 0 cloud routing
│   └── ...45 more
├── skills/                 ← ACTIVE skills (loaded into context)
├── skills-archive/         ← DORMANT skills (gated behind skill-on)
├── agents/                 ← Agent definitions
├── logs/                   ← Hook execution logs
└── settings.json           ← Hook registration
```

| Hook | Trigger | Script |
|------|---------|--------|
| `UserPromptSubmit` | Every prompt | `skill-auto-activate`, `ooda`, `tier0-prompt-inject` |
| `PostToolUse` | After Write/Edit | `auto-github-push` |
| `Stop` | Session end | `auto-learn` |
| `SessionStart` | New session | `auto-troubleshoot`, `openclaw-bridge` |

## 💡 TIPS AND TRICKS (24)

[routing](#tips-routing) · [hooks](#tips-hooks) · [skills](#tips-skills) · [tokens](#tips-tokens) · [git](#tips-git)

<a id="tips-routing"></a>■ **Tier 0 Routing (6)**

| Tip | Source |
|-----|--------|
| Always check `ollama list` before routing — local models burn zero API tokens | [HMZ](https://github.com/hmzainjamil) |
| `llm-burst 'prompt'` routes cloud-first: Groq → OpenRouter free → Gemini | [HMZ](https://github.com/hmzainjamil) |
| DeepSeek-V3 via OpenRouter costs $0.14/1M tokens vs Claude Sonnet $3/1M | [OpenRouter](https://openrouter.ai/deepseek/deepseek-chat) |
| Groq Llama 3 70B is fastest inference at ~800 tok/s — use for analysis | [Groq](https://console.groq.com) |
| Kimi K2.5 has 262K context at 5% of Claude Opus cost — use for long docs | [Moonshot AI](https://platform.moonshot.cn) |
| GLM-4.6 from Zhipu AI is free tier — use for Chinese market content | [Zhipu](https://open.bigmodel.cn) |

<a id="tips-hooks"></a>■ **Hook Engineering (5)**

| Tip | Source |
|-----|--------|
| PostToolUse hooks receive full JSON with `tool_name` + `tool_input` via stdin | [HMZ](https://github.com/hmzainjamil) |
| Always `set -euo pipefail` in hook scripts — silent failures waste tokens | [HMZ](https://github.com/hmzainjamil) |
| Use `python3 -c "import sys,json..."` to parse hook JSON — no deps needed | [HMZ](https://github.com/hmzainjamil) |
| Hook logs → `~/.claude/logs/` — check with `tail -f` during debugging | [HMZ](https://github.com/hmzainjamil) |
| LaunchAgents need both `KeepAlive=true` AND `RunAtLoad=true` to survive reboots | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-skills"></a>■ **Skill Management (6)**

| Tip | Source |
|-----|--------|
| `skill-search <keyword>` uses fzf — faster than scanning 200+ archive entries | [HMZ](https://github.com/hmzainjamil) |
| Never leave non-core skills active — collapse with `skill-off` after every task | [HMZ](https://github.com/hmzainjamil) |
| Core skills always-on: caveman, compact-guard, summarize, context-compression | [HMZ](https://github.com/hmzainjamil) |
| Skill SKILL.md files auto-push to `claude-ai-skills` repo via `auto-github-push` | [HMZ](https://github.com/hmzainjamil) |
| Use `skill-router` keyword map to batch-activate related skills in one command | [HMZ](https://github.com/hmzainjamil) |
| Archive skills with `skill-off --archive` — moves to skills-archive/ and deactivates | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-tokens"></a>■ **Token Savings (4)**

| Tip | Source |
|-----|--------|
| Caveman compression cuts 60-80% of output tokens — apply to all sub-agent outputs | [HMZ](https://github.com/hmzainjamil) |
| Never re-read files already in context — check system-reminder before Read calls | [HMZ](https://github.com/hmzainjamil) |
| Batch parallel tool calls — one message with 5 tool calls beats 5 sequential messages | [HMZ](https://github.com/hmzainjamil) |
| `compact-guard` fires at 70% context usage — forces /compact before overflow | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-git"></a>■ **GitHub API Pattern (3)**

| Tip | Source |
|-----|--------|
| Always GET SHA before PUT — stale SHA causes 422 conflict on concurrent pushes | [HMZ](https://github.com/hmzainjamil) |
| Use `gh api repos/owner/repo/contents/path -X PUT` — no git clone needed | [GitHub Docs](https://docs.github.com/en/rest/repos/contents) |
| Scrub `ghp_*`, `sk-*`, `AIRTABLE_API_KEY` via sed before base64-encoding content | [HMZ](https://github.com/hmzainjamil) |

## ☠️ STARTUPS / BUSINESSES

| Feature | Replaced |
|-|-|
| **Skill Router + Hook System** | [Zapier](https://zapier.com), [Make.com](https://make.com), [n8n Cloud](https://n8n.io) |
| **LLM Burst / Tier 0 Routing** | [OpenAI API](https://openai.com/api), [Anthropic direct](https://anthropic.com) — routes away from expensive models |
| **Auto GitHub Push Hook** | [GitHub Actions](https://github.com/features/actions), [CircleCI](https://circleci.com) |
| **Compact Guard** | [MemGPT](https://memgpt.ai), [Letta](https://letta.com) |
| **Session Queue + Auto Learn** | [Notion AI](https://notion.so/ai), [Mem.ai](https://mem.ai) |
| **LaunchAgent Automation** | [Shortcuts](https://support.apple.com/guide/shortcuts-mac), [Raycast](https://raycast.com), [Alfred](https://alfredapp.com) |

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=hmzainjamil/claude-ai-system&type=Date)](https://star-history.com/#hmzainjamil/claude-ai-system&Date)
