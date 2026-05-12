# claude-ai-system
Production-grade Claude Code harness — hooks, bin scripts, agents, LaunchAgents, full automation OS.

![hooks](https://img.shields.io/badge/hooks-PostToolUse%20%7C%20UserPromptSubmit-blue?style=flat&labelColor=555)
![scripts](https://img.shields.io/badge/bin_scripts-45%2B-green?style=flat&labelColor=555)
![skills](https://img.shields.io/badge/skills-200%2B-orange?style=flat&labelColor=555)
![launchagents](https://img.shields.io/badge/LaunchAgents-12%2B-purple?style=flat&labelColor=555)
![platform](https://img.shields.io/badge/platform-macOS-lightgrey?style=flat&labelColor=555)
![routing](https://img.shields.io/badge/model_routing-Tier0%20first-brightgreen?style=flat&labelColor=555)
![license](https://img.shields.io/badge/license-MIT-blue?style=flat&labelColor=555)

[Concepts](#-concepts) · [Architecture](#️-architecture) · [Tips](#-tips-and-tricks) · [Kills](#️-startups--businesses) · [Stars](#star-history)

## 🧠 CONCEPTS

| Feature | Location | Description |
|---------|----------|-------------|
| [**Skill Router**](automations/bin/skill-router) | `automations/bin/skill-router` | Keyword-match prompt → auto-activate correct skills before response, every UserPromptSubmit |
| [**Auto GitHub Push**](automations/bin/auto-github-push) | `automations/bin/auto-github-push` | PostToolUse hook: Write/Edit to bin/skills auto-pushes to GitHub via Contents API immediately |
| [**Skill On**](automations/bin/skill-on) | `automations/bin/skill-on` | Blockchain-gated activation — copies SKILL.md from archive to active skills directory |
| [**Skill Off**](automations/bin/skill-off) | `automations/bin/skill-off` | Deactivates skill — moves back to archive, releases context tokens, collapses to core |
| [**Skill Search**](automations/bin/skill-search) | `automations/bin/skill-search` | fzf-powered fuzzy search across 200+ archive entries — instant, no manual scan |
| [**Compact Guard**](automations/bin/compact-guard) | `automations/bin/compact-guard` | Fires at 70% context usage — forces /compact before token overflow silently kills session |
| [**LLM Burst**](automations/bin/llm-burst) | `automations/bin/llm-burst` | Cloud-first Tier 0 routing — Groq → OpenRouter → Gemini → Claude as last resort only |
| [**GitHub Portfolio Sync**](automations/bin/github-sync) | `automations/bin/github-sync` | Daily 6:30 AM — syncs all ~/.claude/bin scripts to GitHub repos via Contents API |
| [**Auto Troubleshoot**](automations/bin/auto-troubleshoot) | `automations/bin/auto-troubleshoot` | SessionStart hook — scans LaunchAgents, checks exit codes, flags stale jobs proactively |
| [**OODA Loop**](automations/bin/ooda) | `automations/bin/ooda` | Observe-Orient-Decide-Act framework injected into every UserPromptSubmit hook |
| [**Caveman Compress**](automations/bin/caveman) | `automations/bin/caveman` | Strips filler, collapses whitespace — 60-80% token reduction on all sub-agent outputs |
| [**Session Queue**](automations/bin/session-queue) | `automations/bin/session-queue` | Writes learnings to ~/.claude/session-queue.jsonl during session, Stop hook processes it |
| [**Auto Learn**](automations/bin/auto-learn) | `automations/bin/auto-learn` | Stop hook — converts session-queue.jsonl entries to typed memory files automatically |
| [**OpenClaw Bridge**](automations/bin/openclaw-bridge) | `automations/bin/openclaw-bridge` | SessionStart — verifies Open Design MCP gateway running at 127.0.0.1:51827 |
| [**Tier 0 Prompt Inject**](automations/bin/tier0-prompt-inject) | `automations/bin/tier0-prompt-inject` | Injects G0DM0D3 model routing rules into every Claude session via UserPromptSubmit |
| [**GitHub Sweep**](automations/bin/github-sweep) | `automations/bin/github-sweep` | Discovers new local scripts not yet pushed to GitHub, routes to correct repo |
| [**Log Rotate**](automations/bin/log-rotate) | `automations/bin/log-rotate` | Weekly — cleans ~/.claude/logs entries older than 30 days automatically |
| [**Tier 0 Health**](automations/bin/tier0-health) | `automations/bin/tier0-health` | Pings all 15 providers — outputs live availability matrix for routing decisions |
| [**Skill Auto Activate**](automations/bin/skill-auto-activate) | `automations/bin/skill-auto-activate` | Pre-prompt keyword scanner — activates matching skills from archive before responding |
| [**BDM Sweep**](automations/bin/bdm-sweep) | `automations/bin/bdm-sweep` | Morning job scan — LinkedIn + Indeed only, geo-blacklist enforced, saves to pipeline |
| [**Command Optimized**](automations/bin/command-optimized) | `automations/bin/command-optimized` | Pre-processes commands — deduplicates, batches parallel calls, strips redundant ops |
| [**Launch Optimized**](automations/bin/launch-optimized) | `automations/bin/launch-optimized` | Startup optimizer — preloads models, validates env vars, warms MCP servers on start |
| [**Agent Codex Trigger**](automations/bin/agent-codex-trigger) | `automations/bin/agent-codex-trigger` | Auto-detects agent/codex/workflow keywords → activates all-agents + routes to Groq |
| [**Reddit Throttle Guard**](automations/bin/reddit-throttle) | `automations/bin/reddit-throttle` | Enforces 1-post/day Reddit max — account on bot-watch, rejects if daily count exceeded |
| [**Platform Filter**](automations/bin/platform-filter) | `automations/bin/platform-filter` | Blocks Upwork/Freelancer.com/PPH — LinkedIn + Indeed only for all BDM operations |

### 🔥 Hot

| Feature | Location | Description |
|---------|----------|-------------|
| [**Per-Prospect PDF**](automations/bin/per-prospect-pdf) | `automations/bin/per-prospect-pdf` | Unique audit PDF per prospect — business name, city, brand palette from their URL |
| [**Session Continuity**](automations/bin/session-continuity) | `automations/bin/session-continuity` | Bridges sessions — reads session-queue, injects critical context at next start |
| [**Cost Tracker**](automations/bin/cost-tracker) | `automations/bin/cost-tracker` | Logs token usage + cost per provider — monthly dashboard for budget management |
| [**RAM Guard**](automations/bin/ram-guard) | `automations/bin/ram-guard` | Checks free RAM before loading local models — skips Ollama if below 4GB free |
| [**Skill Creator**](automations/bin/skill-creator) | `automations/bin/skill-creator` | Generates new SKILL.md from template with correct structure + auto-archives it |

## ⚙️ ARCHITECTURE

```
~/.claude/
├── bin/                        ← 45+ automation scripts (auto-pushed via PostToolUse)
│   ├── skill-on / skill-off    ← blockchain-gated skill activation/deactivation
│   ├── skill-router            ← keyword → skill map (fires UserPromptSubmit)
│   ├── skill-auto-activate     ← pre-prompt keyword scanner
│   ├── auto-github-push        ← PostToolUse: Write/Edit → GitHub Contents API
│   ├── auto-learn              ← Stop hook: session-queue → typed memory files
│   ├── auto-troubleshoot       ← SessionStart: LaunchAgent health check
│   ├── llm-burst               ← Tier 0 cloud routing (Groq→OpenRouter→Gemini)
│   ├── tier0-prompt-inject     ← G0DM0D3 routing rules injection
│   ├── compact-guard           ← context overflow prevention at 70%
│   ├── caveman                 ← 60-80% token compression strip
│   ├── command-optimized       ← command dedup + parallel batching
│   ├── launch-optimized        ← session startup: models + MCP warm
│   ├── agent-codex-trigger     ← keyword → all-agents activation
│   └── github-sync             ← daily 6:30 AM portfolio sync daemon
├── skills/                     ← ACTIVE skills (12 core always-on)
├── skills-archive/             ← DORMANT skills (200+, gated by skill-on)
├── agents/                     ← Agent definitions (20+ domain experts)
├── logs/                       ← Hook execution logs (all daemons)
├── projects/memory/            ← 4-type persistent memory (user/feedback/project/ref)
└── settings.json               ← Hook registrations + permissions config
```

| Component | Detail |
|-----------|--------|
| **UserPromptSubmit hooks** | skill-auto-activate, tier0-prompt-inject, ooda, agent-codex-trigger |
| **PostToolUse hooks** | auto-github-push (Write + Edit triggers, immediate sync) |
| **Stop hooks** | auto-learn (session-queue.jsonl → typed memory files) |
| **SessionStart hooks** | auto-troubleshoot, openclaw-bridge, launch-optimized |
| **Always-on skills (12)** | caveman, compact-guard, summarize, context-compression, skill-router + 7 more |
| **On-demand skills (200+)** | ads-strategy, legal-review, geo, market-emails, agency-pipeline, ... |
| **GitHub repos synced** | claude-ai-system, claude-ai-skills, claude-ai-agents, claude-ai-automations |
| **LaunchAgents active** | Ollama, CEO-loop, OpenClaw, portfolio-sync, bdm-sweep, log-rotate |
| **Memory types** | user (profile), feedback (corrections), project (status), reference (pointers) |
| **Token savings** | 75-95% via Tier 0 routing + caveman compression + context batching |

## 💡 TIPS AND TRICKS (48)

[tier-0-routing](#tips-tier-0-routing) · [hook-engineering](#tips-hook-engineering) · [skill-management](#tips-skill-management) · [token-savings](#tips-token-savings) · [github-api-pattern](#tips-github-api-pattern) · [memory-system](#tips-memory-system)

<a id="tips-tier-0-routing"></a>■ **Tier 0 Routing (8)**

| Tip | Source |
|-----|--------|
| Check `ollama list` before routing — local models burn zero API tokens | [HMZ](https://github.com/hmzainjamil) |
| `llm-burst 'prompt'` auto-routes: Groq → OpenRouter free → Gemini → Claude | [HMZ](https://github.com/hmzainjamil) |
| DeepSeek-V3 = $0.14/1M tokens vs Claude Sonnet $3/1M — 21x cheaper for sub-tasks | [OpenRouter](https://openrouter.ai/deepseek/deepseek-chat) |
| Groq Llama 3 70B = ~800 tok/s — fastest inference, use for all analysis tasks | [Groq](https://console.groq.com) |
| Kimi K2.5 262K context at 5% of Opus cost — use for long document analysis | [Moonshot AI](https://platform.moonshot.cn) |
| GLM-4.6 free tier — Chinese market content at $0, no rate limits | [Zhipu](https://open.bigmodel.cn) |
| Gemma 4 31B free tier — strong reasoning, good fallback when Groq rate-limited | [Google](https://ai.google.dev) |
| Sub-agents: NEVER Claude — always Tier 0 for all internal processing | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-hook-engineering"></a>■ **Hook Engineering (8)**

| Tip | Source |
|-----|--------|
| PostToolUse hooks receive full JSON with `tool_name` + `tool_input` via stdin | [HMZ](https://github.com/hmzainjamil) |
| Always `set -euo pipefail` in hook scripts — silent failures waste tokens | [HMZ](https://github.com/hmzainjamil) |
| Use `python3 -c 'import sys,json...'` to parse hook JSON — zero external deps | [HMZ](https://github.com/hmzainjamil) |
| Hook logs → `~/.claude/logs/` — `tail -f` for real-time debug output | [HMZ](https://github.com/hmzainjamil) |
| LaunchAgents need `KeepAlive=true` AND `RunAtLoad=true` — missing either breaks it | [HMZ](https://github.com/hmzainjamil) |
| PostToolUse fires after EVERY Write/Edit — dedupe pushes by checking file mtime | [HMZ](https://github.com/hmzainjamil) |
| Hook timeout is 30s — offload heavy work to background scripts, not inline | [HMZ](https://github.com/hmzainjamil) |
| Test hooks: pipe mock JSON to script before wiring into settings.json | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-skill-management"></a>■ **Skill Management (8)**

| Tip | Source |
|-----|--------|
| `skill-search <keyword>` uses fzf — faster than scanning 200+ archive entries | [HMZ](https://github.com/hmzainjamil) |
| Never leave non-core skills active — collapse with `skill-off` after every task | [HMZ](https://github.com/hmzainjamil) |
| Core always-on: caveman, compact-guard, summarize, context-compression, skill-router | [HMZ](https://github.com/hmzainjamil) |
| SKILL.md files auto-push to `claude-ai-skills` via PostToolUse hook on Write | [HMZ](https://github.com/hmzainjamil) |
| skill-router keyword map — edit `automations/bin/skill-router` to add triggers | [HMZ](https://github.com/hmzainjamil) |
| Every SKILL.md needs: trigger keywords, model routing, output format, examples | [HMZ](https://github.com/hmzainjamil) |
| Skill desc ≤80 chars — shown in skill-search results, must be instantly scannable | [HMZ](https://github.com/hmzainjamil) |
| Test: `skill-on <name> && claude 'trigger phrase'` — validate before archiving | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-token-savings"></a>■ **Token Savings (8)**

| Tip | Source |
|-----|--------|
| Caveman: 60-80% output token reduction — always apply to sub-agent outputs | [HMZ](https://github.com/hmzainjamil) |
| Never re-read files already in context — check system-reminder before Read calls | [HMZ](https://github.com/hmzainjamil) |
| Batch parallel tool calls — one message with 5 calls beats 5 sequential ones | [HMZ](https://github.com/hmzainjamil) |
| `compact-guard` auto-fires at 70% context — no manual /compact needed | [HMZ](https://github.com/hmzainjamil) |
| Write learnings as JSONL not prose — 90% smaller than full text notes | [HMZ](https://github.com/hmzainjamil) |
| Use file:line_number refs instead of quoting full code blocks in responses | [HMZ](https://github.com/hmzainjamil) |
| Compress agent output via caveman before returning — strip markdown too | [HMZ](https://github.com/hmzainjamil) |
| Cache model availability for 5 min — avoid pinging health on every call | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-github-api-pattern"></a>■ **GitHub API Pattern (8)**

| Tip | Source |
|-----|--------|
| Always GET SHA before PUT — stale SHA causes 422 conflict on concurrent pushes | [HMZ](https://github.com/hmzainjamil) |
| Use `gh api repos/owner/repo/contents/path -X PUT` — no git clone needed | [GitHub Docs](https://docs.github.com/en/rest/repos/contents) |
| Scrub `ghp_*`, `sk-*`, `AIRTABLE_API_KEY` via sed before base64-encoding content | [HMZ](https://github.com/hmzainjamil) |
| macOS symlink conflicts: never `git push` from local clone of claude-ai-system | [HMZ](https://github.com/hmzainjamil) |
| auto-github-push routes: bin/ → claude-ai-system, skills/ → claude-ai-skills | [HMZ](https://github.com/hmzainjamil) |
| Re-fetch SHA immediately before PUT — never cache SHA across multiple pushes | [HMZ](https://github.com/hmzainjamil) |
| base64 encode: `base64.b64encode(content.encode()).decode()` — full file always | [HMZ](https://github.com/hmzainjamil) |
| Check `'sha' in response` to detect success — HTTP status alone insufficient | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-memory-system"></a>■ **Memory System (8)**

| Tip | Source |
|-----|--------|
| 4 types: user (profile), feedback (corrections), project (status), reference (pointers) | [HMZ](https://github.com/hmzainjamil) |
| MEMORY.md index — 200 line hard limit, each entry ≤150 chars + file pointer | [HMZ](https://github.com/hmzainjamil) |
| Verify memory before acting — files move, functions rename — check current state | [HMZ](https://github.com/hmzainjamil) |
| Never save git history, code patterns, debugging solutions — non-obvious only | [HMZ](https://github.com/hmzainjamil) |
| Update stale memories immediately — wrong memory is worse than no memory | [HMZ](https://github.com/hmzainjamil) |
| Feedback memories: rule → **Why:** → **How to apply:** — 3-part structure always | [HMZ](https://github.com/hmzainjamil) |
| auto-learn Stop hook: reads session-queue.jsonl → writes typed memory files | [HMZ](https://github.com/hmzainjamil) |
| Convert relative dates to absolute in memory: 'Thursday' → '2026-05-15' | [HMZ](https://github.com/hmzainjamil) |

## ☠️ STARTUPS / BUSINESSES

| Feature | Replaced |
|-|-|
| **Skill Router + Hook System** | [Zapier](https://zapier.com), [Make.com](https://make.com), [n8n Cloud](https://n8n.io) |
| **LLM Burst / Tier 0 Routing** | [OpenAI API direct](https://platform.openai.com), [Anthropic API direct](https://anthropic.com) |
| **Auto GitHub Push Hook** | [GitHub Actions](https://github.com/features/actions), [CircleCI](https://circleci.com) |
| **Compact Guard / Memory** | [MemGPT](https://memgpt.ai), [Letta](https://letta.com), [Zep](https://getzep.com) |
| **Session Queue + Auto Learn** | [Notion AI](https://notion.so/ai), [Mem.ai](https://mem.ai) |
| **LaunchAgent Automation** | [Zapier](https://zapier.com), [Raycast](https://raycast.com), [Alfred](https://alfredapp.com) |
| **Skill System (200+)** | [OpenAI GPTs](https://openai.com/gpts), [Poe](https://poe.com), [Character.ai](https://character.ai) |
| **OODA Decision Framework** | [Lindy AI](https://lindy.ai), [Beam AI](https://beam.ai) |
| **Command + Launch Optimized** | [Superhuman](https://superhuman.com), [Magical](https://magical.com) |
| **Memory System (4 types)** | [Rewind AI](https://rewind.ai), [Mem.ai](https://mem.ai), [Notion AI](https://notion.so/ai) |

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=hmzainjamil/claude-ai-system&type=Date)](https://star-history.com/#hmzainjamil/claude-ai-system&Date)
