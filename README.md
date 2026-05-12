# claude-ai-system
Production-grade Claude Code harness — hooks, bin scripts, agents, LaunchAgents, full automation OS.

![hooks](https://img.shields.io/badge/hooks-PostToolUse%20%7C%20UserPromptSubmit-blue?style=flat&labelColor=555)
![scripts](https://img.shields.io/badge/bin_scripts-45%2B-green?style=flat&labelColor=555)
![skills](https://img.shields.io/badge/skills-200%2B-orange?style=flat&labelColor=555)
![launchagents](https://img.shields.io/badge/LaunchAgents-12%2B-purple?style=flat&labelColor=555)
![routing](https://img.shields.io/badge/model_routing-Tier0%20first-brightgreen?style=flat&labelColor=555)
![platform](https://img.shields.io/badge/platform-macOS-lightgrey?style=flat&labelColor=555)
![license](https://img.shields.io/badge/license-MIT-blue?style=flat&labelColor=555)

[Concepts](#-concepts) · [Architecture](#️-architecture) · [Quick Start](#-quick-start) · [Tips](#-tips-and-tricks-48) · [Kills](#️-startups--businesses) · [Stars](#star-history)

## 🧠 CONCEPTS

| Feature | Location | Description |
|---------|----------|-------------|
| [**Skill Router**](automations/bin/skill-router) | `automations/bin/skill-router` | Keyword-match prompt → auto-activate correct skills before every response. Fires on UserPromptSubmit hook. [![always-on](https://img.shields.io/badge/status-always_on-brightgreen?style=flat&labelColor=555)] |
| [**Auto GitHub Push**](automations/bin/auto-github-push) | `automations/bin/auto-github-push` | PostToolUse hook — any Write/Edit to bin/ or skills/ instantly pushes to correct GitHub repo via Contents API. Zero manual git required. |
| [**Skill On**](automations/bin/skill-on) | `automations/bin/skill-on` | Blockchain-gated activation — copies SKILL.md from archive to active skills directory and loads it into context for current task. |
| [**Skill Off**](automations/bin/skill-off) | `automations/bin/skill-off` | Deactivates skill — moves back to archive, releases context tokens, collapses session back to 12 core skills. |
| [**Skill Search**](automations/bin/skill-search) | `automations/bin/skill-search` | fzf-powered fuzzy search across 200+ archive entries — finds matching skills by keyword faster than any manual scan. |
| [**Compact Guard**](automations/bin/compact-guard) | `automations/bin/compact-guard` | Fires at 70% context usage — forces /compact before token overflow silently kills session state. |
| [**LLM Burst**](automations/bin/llm-burst) | `automations/bin/llm-burst` | Cloud-first Tier 0 routing — Groq → OpenRouter → Gemini → Bytez → Claude as absolute last resort only. |
| [**GitHub Portfolio Sync**](automations/bin/github-sync) | `automations/bin/github-sync` | Daily 6:30 AM LaunchAgent — syncs all local ~/.claude/bin scripts to GitHub repos via Contents API. |
| [**Auto Troubleshoot**](automations/bin/auto-troubleshoot) | `automations/bin/auto-troubleshoot` | SessionStart hook — scans LaunchAgents, checks exit codes, flags stale jobs, reports issues before session begins. |
| [**OODA Loop**](automations/bin/ooda) | `automations/bin/ooda` | Observe-Orient-Decide-Act framework injected into every UserPromptSubmit hook for structured decision-making. |
| [**Caveman Compress**](automations/bin/caveman) | `automations/bin/caveman` | Strips filler words and collapses whitespace — 60-80% token reduction applied to all sub-agent outputs. |
| [**Session Queue**](automations/bin/session-queue) | `automations/bin/session-queue` | Writes learnings as JSONL to ~/.claude/session-queue.jsonl during session — Stop hook processes into memory. |
| [**Auto Learn**](automations/bin/auto-learn) | `automations/bin/auto-learn` | Stop hook — converts session-queue.jsonl entries into 4 types of persistent memory files automatically. |
| [**OpenClaw Bridge**](automations/bin/openclaw-bridge) | `automations/bin/openclaw-bridge` | SessionStart hook — verifies Open Design MCP gateway running at 127.0.0.1:51827, starts if needed. |
| [**Tier 0 Prompt Inject**](automations/bin/tier0-prompt-inject) | `automations/bin/tier0-prompt-inject` | Injects G0DM0D3 model routing rules into every Claude session via UserPromptSubmit hook on each prompt. |
| [**GitHub Sweep**](automations/bin/github-sweep) | `automations/bin/github-sweep` | Discovers new local scripts not yet pushed to GitHub and routes them to the correct repo automatically. |
| [**Log Rotate**](automations/bin/log-rotate) | `automations/bin/log-rotate` | Weekly cleanup — prunes ~/.claude/logs/ entries older than 30 days to prevent disk bloat. |
| [**Tier 0 Health**](automations/bin/tier0-health) | `automations/bin/tier0-health` | Pings all 15 providers every 5 minutes — outputs live availability matrix used for routing decisions. |
| [**Skill Auto Activate**](automations/bin/skill-auto-activate) | `automations/bin/skill-auto-activate` | Pre-prompt keyword scanner — activates matching skills from archive before Claude responds to any task. |
| [**BDM Sweep**](automations/bin/bdm-sweep) | `automations/bin/bdm-sweep` | Morning job scan — LinkedIn + Indeed only, geo-blacklist enforced, saves qualified prospects to pipeline. |
| [**Command Optimized**](automations/bin/command-optimized) | `automations/bin/command-optimized` | Pre-processes commands — deduplicates, batches parallel calls, strips redundant operations before execution. |
| [**Launch Optimized**](automations/bin/launch-optimized) | `automations/bin/launch-optimized` | Session startup optimizer — preloads critical models, validates env vars, warms MCP servers on start. |
| [**Agent Codex Trigger**](automations/bin/agent-codex-trigger) | `automations/bin/agent-codex-trigger` | Auto-detects agent/codex/workflow keywords in prompts → activates all-agents skill stack + routes to Groq. |
| [**OpenCLI Integration**](automations/bin/opencli-bridge) | `automations/bin/opencli-bridge` | Wraps 90+ site adapters (Twitter, Reddit, HackerNews, Bilibili) — zero LLM cost per CLI call. |
| [**Bytez Tier 0**](automations/bin/bytez-client) | `automations/bin/bytez-client` | Bytez.com multi-model API — 100+ free LLMs via single key, added to Tier 0 burst routing. |

### 🔥 Hot

| Feature | Location | Description |
|---------|----------|-------------|
| [**Per-Prospect PDF**](automations/bin/per-prospect-pdf) | `automations/bin/per-prospect-pdf` | Each cold email gets a unique audit PDF — business name, city, brand palette extracted from prospect URL. |
| [**Session Continuity**](automations/bin/session-continuity) | `automations/bin/session-continuity` | Bridges sessions — reads session-queue, injects critical context at next session start automatically. |
| [**Cost Tracker**](automations/bin/cost-tracker) | `automations/bin/cost-tracker` | Logs token usage + cost per provider — monthly dashboard, enforces <$10/month total AI spend target. |
| [**RAM Guard**](automations/bin/ram-guard) | `automations/bin/ram-guard` | Checks free RAM before loading local models — skips Ollama below 4GB free, routes to Groq instead. |
| [**Codex Agent Loop**](automations/bin/codex-agent-loop) | `automations/bin/codex-agent-loop` | Self-improving agent loop: understand → plan → execute → test → fix → repeat until done. |

## ⚙️ ARCHITECTURE

```
~/.claude/
├── bin/                        ← 45+ automation scripts (auto-pushed via PostToolUse)
│   ├── skill-on / skill-off    ← blockchain-gated skill activation/deactivation
│   ├── skill-router            ← keyword → skill map (fires on every UserPromptSubmit)
│   ├── skill-auto-activate     ← pre-prompt keyword scanner before every response
│   ├── auto-github-push        ← PostToolUse: Write/Edit → GitHub Contents API
│   ├── auto-learn              ← Stop hook: session-queue.jsonl → typed memory files
│   ├── auto-troubleshoot       ← SessionStart: scan + report all LaunchAgent health
│   ├── llm-burst               ← Tier 0 routing: Groq→OpenRouter→Gemini→Bytez
│   ├── tier0-prompt-inject     ← inject G0DM0D3 routing rules every session
│   ├── compact-guard           ← context overflow prevention at 70% usage
│   ├── caveman                 ← 60-80% token compression on all outputs
│   ├── command-optimized       ← command dedup + parallel batching
│   ├── launch-optimized        ← startup: preload models + warm MCP servers
│   ├── agent-codex-trigger     ← keyword detection → all-agents activation
│   ├── opencli-bridge          ← 90+ site adapters (Twitter, Reddit, HN, Bilibili)
│   └── github-sync             ← daily 6:30 AM portfolio sync daemon
├── skills/                     ← ACTIVE skills (12 core always-on)
├── skills-archive/             ← DORMANT skills (200+, gated by skill-on)
├── agents/                     ← Agent definitions (20+ domain experts)
├── logs/                       ← Hook execution logs (all hooks + daemons)
├── projects/memory/            ← Persistent memory: user/feedback/project/reference
└── settings.json               ← Hook registrations + permission config
```

| Hook Type | Trigger | Scripts | Purpose |
|-----------|---------|---------|---------|
| `UserPromptSubmit` | Every prompt | skill-auto-activate, tier0-prompt-inject, ooda, agent-codex-trigger | Pre-process before Claude responds |
| `PostToolUse` | After Write/Edit | auto-github-push | Sync to GitHub instantly |
| `Stop` | Session end | auto-learn | Persist learnings to memory files |
| `SessionStart` | New session | auto-troubleshoot, openclaw-bridge, launch-optimized | Health check + warm systems |

| Component | Count | Always-On | Cost/Month |
|-----------|-------|-----------|-----------|
| Bin scripts | 45+ | 3 daemons | $0 |
| Active skills | 12 core | All 12 | $0 |
| Archive skills | 200+ | 0 (on-demand) | $0 |
| LaunchAgents | 12 | Ollama, CEO, OClaw | $0 |
| Tier 0 providers | 15 | — (on-demand) | ~$5 |

## 🚀 QUICK START

```bash
# 1. Clone the system
git clone https://github.com/hmzainjamil/claude-ai-system ~/.claude

# 2. Load all LaunchAgents
for plist in ~/Library/LaunchAgents/ai.hmz.*.plist; do
  launchctl load "$plist"
done

# 3. Verify all systems
~/.claude/bin/auto-troubleshoot

# 4. Check Tier 0 model availability
~/.claude/bin/tier0-health

# 5. Test a skill activation
~/.claude/bin/skill-on ads-strategy
~/.claude/bin/skill-search "email outreach"
~/.claude/bin/skill-off ads-strategy

# 6. Run LLM burst (fires 15 models simultaneously)
~/.claude/bin/llm-burst "analyze this ad copy"

# 7. OpenCLI — 90+ sites as CLI commands
opencli hackernews top --limit 5
opencli twitter search "claude code"
opencli reddit top --subreddit MachineLearning
```

## 💡 TIPS AND TRICKS (48)

[routing](#tips-routing) · [hooks](#tips-hooks) · [skills](#tips-skills) · [tokens](#tips-tokens) · [git](#tips-git) · [memory](#tips-memory) · [agents](#tips-agents) · [opencli](#tips-opencli) · [debug](#tips-debug) · [bytez](#tips-bytez) · [codex](#tips-codex) · [launch](#tips-launch)

<a id="tips-routing"></a>■ **Tier 0 Routing (5)**

| Tip | Source |
|-----|--------|
| Check `ollama list` before routing — local models burn zero API tokens forever | [HMZ](https://github.com/hmzainjamil) |
| `llm-burst 'prompt'` auto-routes: Groq → OpenRouter free → Gemini → Bytez → Claude | [HMZ](https://github.com/hmzainjamil) |
| DeepSeek-V3 = $0.14/1M tokens vs Claude Sonnet $3/1M — 21x cheaper for sub-tasks | [OpenRouter](https://openrouter.ai/deepseek/deepseek-chat) |
| Groq Llama 3 70B = ~800 tok/s — fastest cloud inference, use for all analysis tasks | [Groq](https://console.groq.com) |
| Bytez.com key `cb4a7065a586ec6ca26394724ce5ec49` — 100+ models, free tier generous | [Bytez](https://bytez.com) |

<a id="tips-hooks"></a>■ **Hook Engineering (5)**

| Tip | Source |
|-----|--------|
| PostToolUse hooks receive full JSON with `tool_name` + `tool_input` via stdin | [HMZ](https://github.com/hmzainjamil) |
| Always `set -euo pipefail` in hook scripts — silent failures waste tokens silently | [HMZ](https://github.com/hmzainjamil) |
| Use `python3 -c 'import sys,json...'` to parse hook JSON — zero external deps needed | [HMZ](https://github.com/hmzainjamil) |
| Hook logs → `~/.claude/logs/` — `tail -f` for real-time debug output during testing | [HMZ](https://github.com/hmzainjamil) |
| LaunchAgents need both `KeepAlive=true` AND `RunAtLoad=true` — missing either breaks it | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-skills"></a>■ **Skill Management (4)**

| Tip | Source |
|-----|--------|
| `skill-search <keyword>` fuzzy-searches 200+ archive entries — instant, no manual scan | [HMZ](https://github.com/hmzainjamil) |
| Never leave non-core skills active — collapse with `skill-off` after every task | [HMZ](https://github.com/hmzainjamil) |
| Core always-on: caveman, compact-guard, summarize, context-compression, skill-router | [HMZ](https://github.com/hmzainjamil) |
| Every SKILL.md auto-pushes to `claude-ai-skills` repo via PostToolUse hook on Write | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-tokens"></a>■ **Token Savings (4)**

| Tip | Source |
|-----|--------|
| Caveman compression cuts 60-80% output tokens — always apply to all sub-agent outputs | [HMZ](https://github.com/hmzainjamil) |
| Never re-read files already in context — check system-reminder section before any Read | [HMZ](https://github.com/hmzainjamil) |
| Batch parallel tool calls — one message with 5 calls beats 5 sequential messages | [HMZ](https://github.com/hmzainjamil) |
| compact-guard auto-fires at 70% context usage — no manual /compact ever needed | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-git"></a>■ **GitHub API Pattern (4)**

| Tip | Source |
|-----|--------|
| Always GET SHA before PUT — stale SHA causes 422 conflict on any concurrent push | [HMZ](https://github.com/hmzainjamil) |
| Use `gh api repos/owner/repo/contents/path -X PUT` — no git clone needed ever | [GitHub Docs](https://docs.github.com/en/rest/repos/contents) |
| Scrub `ghp_*`, `sk-*`, `AIRTABLE_API_KEY` via sed before base64-encoding any content | [HMZ](https://github.com/hmzainjamil) |
| macOS symlink conflicts: never `git push` from local clone of claude-ai-system repo | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-memory"></a>■ **Memory System (4)**

| Tip | Source |
|-----|--------|
| 4 types: user (profile), feedback (corrections), project (status), reference (pointers) | [HMZ](https://github.com/hmzainjamil) |
| MEMORY.md index — 200 line hard limit, each entry ≤150 chars with pointer to file | [HMZ](https://github.com/hmzainjamil) |
| Verify memory before acting — files move and functions rename — check current state | [HMZ](https://github.com/hmzainjamil) |
| auto-learn Stop hook: reads session-queue.jsonl → writes typed memory files on stop | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-agents"></a>■ **Agent Orchestration (4)**

| Tip | Source |
|-----|--------|
| Sub-agents NEVER use Claude — always Tier 0 (Groq, Gemini, DeepSeek, GPT-4o-mini) | [HMZ](https://github.com/hmzainjamil) |
| Use `run_in_background=true` for research agents — continue other work in parallel | [HMZ](https://github.com/hmzainjamil) |
| `subagent_type=Explore` for codebase scans — read-only, specialized, dramatically faster | [HMZ](https://github.com/hmzainjamil) |
| Batch 3-5 agents in single message — parallel launch = 5x time saving vs sequential | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-opencli"></a>■ **OpenCLI — 90+ Site Adapters (5)**

| Tip | Source |
|-----|--------|
| `opencli hackernews top --limit 10` — top HN posts as clean JSON, zero LLM cost | [OpenCLI](https://github.com/jackwener/opencli) |
| `opencli twitter search "claude"` — searches your logged-in Twitter session directly | [OpenCLI](https://github.com/jackwener/opencli) |
| `opencli bilibili hot --limit 5` — Bilibili trending, perfect for Chinese content intel | [OpenCLI](https://github.com/jackwener/opencli) |
| `opencli reddit top --subreddit MachineLearning` — scrapes your Reddit session, no API | [OpenCLI](https://github.com/jackwener/opencli) |
| `opencli doctor` — verifies browser bridge extension is connected and working correctly | [OpenCLI](https://github.com/jackwener/opencli) |

<a id="tips-debug"></a>■ **Debugging (4)**

| Tip | Source |
|-----|--------|
| `launchctl list \| grep hmz` — check all running agents and their exit codes at once | [HMZ](https://github.com/hmzainjamil) |
| Exit code 256 = script not found or permission denied — always `chmod +x` on scripts | [HMZ](https://github.com/hmzainjamil) |
| `tail -f ~/.claude/logs/<agent>.log` — real-time output during hook/daemon testing | [HMZ](https://github.com/hmzainjamil) |
| auto-troubleshoot SessionStart hook catches most common plist issues automatically | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-bytez"></a>■ **Bytez.com Integration (4)**

| Tip | Source |
|-----|--------|
| API key `cb4a7065a586ec6ca26394724ce5ec49` — 100+ models via single endpoint at bytez.com | [Bytez](https://bytez.com) |
| Endpoint: `POST https://api.bytez.com/models/v2/chat` — OpenAI-compatible format | [Bytez](https://bytez.com) |
| Models: llama-3.1-8b, mistral-7b, qwen2.5-coder, phi-3-mini and 100+ more — free tier | [Bytez](https://bytez.com) |
| Add to llm-burst: `bytez_query 'prompt' 'model-name'` — wired as Tier 0 fallback | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-codex"></a>■ **Codex Agent Loop (5)**

| Tip | Source |
|-----|--------|
| Codex loop: understand task → inspect codebase → plan → build → test → fix → repeat | [OpenAI Codex](https://openai.com/codex) |
| Weak prompt: "Build CRM" — Strong prompt: mission brief with constraints + test criteria | [Beyond Tahir](https://medium.com/@beyondtahir) |
| Codex agents can work in parallel isolated environments — use worktree isolation | [HMZ](https://github.com/hmzainjamil) |
| The new skill is delegation: write clear architecture docs, not just feature requests | [Beyond Tahir](https://medium.com/@beyondtahir) |
| Codex + MCP servers = agent reads repo, edits files, runs commands, proposes PRs | [OpenAI](https://openai.com) |

<a id="tips-launch"></a>■ **Launch Optimized (4)**

| Tip | Source |
|-----|--------|
| `launch-optimized` runs on SessionStart — preloads Ollama model, pings Groq health | [HMZ](https://github.com/hmzainjamil) |
| `command-optimized` pre-processes every command — deduplicates, strips redundant ops | [HMZ](https://github.com/hmzainjamil) |
| Auto-detect: agent/codex/workflow keywords → all-agents skill stack auto-activates | [HMZ](https://github.com/hmzainjamil) |
| launch-optimized also validates env vars (BYTEZ, GROQ, GEMINI keys) at session start | [HMZ](https://github.com/hmzainjamil) |

## ☠️ STARTUPS / BUSINESSES

| Feature | Replaced |
|-|-|
| **Skill Router + Hook System** | [Zapier](https://zapier.com), [Make.com](https://make.com), [n8n Cloud](https://n8n.io) |
| **LLM Burst / Tier 0 Routing** | [OpenAI API direct](https://platform.openai.com), [Anthropic API direct](https://anthropic.com) |
| **Auto GitHub Push Hook** | [GitHub Actions](https://github.com/features/actions), [CircleCI](https://circleci.com), [Travis CI](https://travis-ci.com) |
| **Compact Guard / Memory** | [MemGPT](https://memgpt.ai), [Letta](https://letta.com), [Zep](https://getzep.com) |
| **Session Queue + Auto Learn** | [Notion AI](https://notion.so/ai), [Mem.ai](https://mem.ai), [Rewind AI](https://rewind.ai) |
| **LaunchAgent Automation** | [Zapier](https://zapier.com), [Raycast](https://raycast.com), [Alfred](https://alfredapp.com) |
| **Skill System (200+)** | [OpenAI GPTs](https://openai.com/gpts), [Poe](https://poe.com), [Character.ai](https://character.ai) |
| **OpenCLI Integration** | [Browser Use](https://browser-use.com), [Stagehand](https://stagehand.dev), [Operator](https://openai.com/operator) |
| **Bytez Multi-Model Access** | [OpenRouter](https://openrouter.ai), [LiteLLM](https://litellm.ai), [Martian](https://withmartian.com) |
| **Codex Agent Loop** | [CrewAI](https://crewai.com), [AutoGen](https://github.com/microsoft/autogen), [LangGraph](https://langgraph.com) |
| **Command + Launch Optimized** | [Superhuman](https://superhuman.com), [Magical](https://magical.com), [TextBlaze](https://blaze.today) |
| **Memory System (4 types)** | [Rewind AI](https://rewind.ai), [Mem.ai](https://mem.ai), [Notion AI](https://notion.so/ai) |

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=hmzainjamil/claude-ai-system&type=Date)](https://star-history.com/#hmzainjamil/claude-ai-system&Date)
