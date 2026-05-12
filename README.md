# claude-ai-system
Production-grade Claude Code harness — hooks, bin scripts, agents, LaunchAgents, and full automation OS.

![hooks](https://img.shields.io/badge/hooks-PostToolUse%20%7C%20UserPromptSubmit-blue?style=flat&labelColor=555)
![scripts](https://img.shields.io/badge/bin_scripts-45%2B-green?style=flat&labelColor=555)
![skills](https://img.shields.io/badge/skills-200%2B-orange?style=flat&labelColor=555)
![launchagents](https://img.shields.io/badge/LaunchAgents-12%2B-purple?style=flat&labelColor=555)
![platform](https://img.shields.io/badge/platform-macOS-lightgrey?style=flat&labelColor=555)
![tier0](https://img.shields.io/badge/model_routing-Tier0%20first-brightgreen?style=flat&labelColor=555)
![license](https://img.shields.io/badge/license-MIT-blue?style=flat&labelColor=555)

[Concepts](#-concepts) · [Architecture](#️-architecture) · [Tips](#-tips-and-tricks-40) · [Kills](#️-startups--businesses) · [Stars](#star-history)

## 🧠 CONCEPTS

| Feature | Location | Description |
|---------|----------|-------------|
| [**Skill Router**](automations/bin/skill-router) | `automations/bin/skill-router` | Keyword-match prompt → auto-activate skills before response [![always-on](https://img.shields.io/badge/status-always_on-brightgreen?style=flat&labelColor=555)] |
| [**Auto GitHub Push**](automations/bin/auto-github-push) | `automations/bin/auto-github-push` | PostToolUse hook — Write/Edit to bin/skills auto-pushes to GitHub via Contents API immediately |
| [**Skill On**](automations/bin/skill-on) | `automations/bin/skill-on` | Blockchain-gated activation — copies SKILL.md from archive to active, loads into context |
| [**Skill Off**](automations/bin/skill-off) | `automations/bin/skill-off` | Deactivates skill — moves back to archive, reduces context load |
| [**Skill Search**](automations/bin/skill-search) | `automations/bin/skill-search` | fzf-powered fuzzy search across 200+ archive entries — faster than manual scan |
| [**Compact Guard**](automations/bin/compact-guard) | `automations/bin/compact-guard` | Fires at 70% context usage — forces /compact before token overflow |
| [**LLM Burst**](automations/bin/llm-burst) | `automations/bin/llm-burst` | Cloud-first Tier 0 routing — Groq → OpenRouter → Gemini → Claude last resort |
| [**GitHub Portfolio Sync**](automations/bin/github-sync) | `automations/bin/github-sync` | Daily 6:30 AM — syncs all local ~/.claude/bin scripts to GitHub via Contents API |
| [**Auto Troubleshoot**](automations/bin/auto-troubleshoot) | `automations/bin/auto-troubleshoot` | SessionStart hook — scans LaunchAgents, checks logs, flags stale jobs, reports issues |
| [**OODA Loop**](automations/bin/ooda) | `automations/bin/ooda` | Observe-Orient-Decide-Act injected into every UserPromptSubmit hook automatically |
| [**Caveman Compress**](automations/bin/caveman) | `automations/bin/caveman` | Strips filler, collapses whitespace — 60-80% token reduction on all sub-agent outputs |
| [**Session Queue**](automations/bin/session-queue) | `automations/bin/session-queue` | Writes learnings to ~/.claude/session-queue.jsonl during session for Stop hook processing |
| [**Auto Learn**](automations/bin/auto-learn) | `automations/bin/auto-learn` | Stop hook — converts session-queue.jsonl entries to persistent typed memory files |
| [**OpenClaw Bridge**](automations/bin/openclaw-bridge) | `automations/bin/openclaw-bridge` | SessionStart hook — verifies Open Design MCP gateway at 127.0.0.1:51827 |
| [**Tier 0 Prompt Inject**](automations/bin/tier0-prompt-inject) | `automations/bin/tier0-prompt-inject` | Injects G0DM0D3 routing rules into every session via UserPromptSubmit |
| [**GitHub Sweep**](automations/bin/github-sweep) | `automations/bin/github-sweep` | Discovers new local scripts not yet in GitHub and pushes to correct repo |
| [**Log Rotate**](automations/bin/log-rotate) | `automations/bin/log-rotate` | Weekly prune — cleans ~/.claude/logs entries older than 30 days |
| [**Tier 0 Health**](automations/bin/tier0-health) | `automations/bin/tier0-health` | Pings all 15 models — outputs live availability matrix for routing decisions |
| [**Skill Auto Activate**](automations/bin/skill-auto-activate) | `automations/bin/skill-auto-activate` | Pre-prompt keyword scanner — activates matching skills from archive before response |
| [**BDM Sweep**](automations/bin/bdm-sweep) | `automations/bin/bdm-sweep` | Morning job scan — LinkedIn + Indeed only, geo-blacklist enforced, saves to pipeline |

### 🔥 Hot

| Feature | Location | Description |
|---------|----------|-------------|
| [**Agent Codex Trigger**](automations/bin/agent-codex-trigger) | `automations/bin/agent-codex-trigger` | Auto-detects agent/codex/workflow keywords → activates all-agents skill stack |
| [**Command Optimized**](automations/bin/command-optimized) | `automations/bin/command-optimized` | Pre-processes commands — deduplicates, batches parallel calls, strips redundant ops |
| [**Launch Optimized**](automations/bin/launch-optimized) | `automations/bin/launch-optimized` | Startup optimizer — preloads critical models, validates env, warms MCP servers |
| [**Reddit Throttle Guard**](automations/bin/reddit-throttle) | `automations/bin/reddit-throttle` | Enforces 1-post/day Reddit limit — rejects if daily count exceeded |
| [**Platform Filter**](automations/bin/platform-filter) | `automations/bin/platform-filter` | Blocks Upwork/Freelancer.com/PPH from BDM pipeline — LinkedIn + Indeed only |

## ⚙️ ARCHITECTURE

```
~/.claude/
├── bin/                        ← 45+ automation scripts
│   ├── skill-on / skill-off    ← blockchain-gated skill activation
│   ├── skill-router            ← keyword → skill map (UserPromptSubmit)
│   ├── skill-auto-activate     ← pre-prompt skill scanner
│   ├── auto-github-push        ← PostToolUse: Write/Edit → GitHub API
│   ├── auto-learn              ← Stop hook: session-queue → memory
│   ├── auto-troubleshoot       ← SessionStart: health check
│   ├── llm-burst               ← Tier 0 cloud routing
│   ├── tier0-prompt-inject     ← routing rules injection
│   ├── compact-guard           ← context overflow prevention
│   ├── caveman                 ← token compression
│   └── github-sync             ← daily portfolio sync
├── skills/                     ← ACTIVE skills (12 core always-on)
├── skills-archive/             ← DORMANT skills (gated by skill-on)
├── agents/                     ← Agent definitions (20+ domain agents)
├── logs/                       ← Hook execution logs (all daemons)
├── projects/memory/            ← Persistent memory files (4 types)
└── settings.json               ← Hook registration + permissions
```

| Hook | Trigger | Script | Purpose |
|------|---------|--------|---------|
| `UserPromptSubmit` | Every prompt | `skill-auto-activate` | Pre-load relevant skills |
| `UserPromptSubmit` | Every prompt | `tier0-prompt-inject` | Inject routing rules |
| `UserPromptSubmit` | Every prompt | `ooda` | OODA decision framework |
| `PostToolUse` | After Write | `auto-github-push` | Sync to GitHub instantly |
| `PostToolUse` | After Edit | `auto-github-push` | Sync to GitHub instantly |
| `Stop` | Session end | `auto-learn` | Persist learnings to memory |
| `SessionStart` | New session | `auto-troubleshoot` | Health check all systems |
| `SessionStart` | New session | `openclaw-bridge` | Verify MCP gateway |
| `SessionStart` | New session | `launch-optimized` | Warm models + MCP servers |

## 💡 TIPS AND TRICKS (40)

[routing](#tips-routing) · [hooks](#tips-hooks) · [skills](#tips-skills) · [tokens](#tips-tokens) · [git](#tips-git) · [memory](#tips-memory) · [agents](#tips-agents) · [debug](#tips-debug)

<a id="tips-routing"></a>■ **Tier 0 Routing (5)**

| Tip | Source |
|-----|--------|
| Always check `ollama list` before routing — local models burn zero API tokens | [HMZ](https://github.com/hmzainjamil) |
| `llm-burst 'prompt'` routes cloud-first: Groq → OpenRouter free → Gemini | [HMZ](https://github.com/hmzainjamil) |
| DeepSeek-V3 via OpenRouter costs $0.14/1M tokens vs Claude Sonnet $3/1M | [OpenRouter](https://openrouter.ai) |
| Groq Llama 3 70B is fastest inference at ~800 tok/s — use for analysis tasks | [Groq](https://console.groq.com) |
| Kimi K2.5 has 262K context at 5% of Claude Opus cost — use for long documents | [Moonshot AI](https://platform.moonshot.cn) |

<a id="tips-hooks"></a>■ **Hook Engineering (5)**

| Tip | Source |
|-----|--------|
| PostToolUse hooks receive full JSON with `tool_name` + `tool_input` via stdin | [HMZ](https://github.com/hmzainjamil) |
| Always `set -euo pipefail` in hook scripts — silent failures waste tokens | [HMZ](https://github.com/hmzainjamil) |
| Use `python3 -c "import sys,json..."` to parse hook JSON — no external deps | [HMZ](https://github.com/hmzainjamil) |
| Hook logs → `~/.claude/logs/` — check with `tail -f` during hook debugging | [HMZ](https://github.com/hmzainjamil) |
| LaunchAgents need both `KeepAlive=true` AND `RunAtLoad=true` for persistence | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-skills"></a>■ **Skill Management (5)**

| Tip | Source |
|-----|--------|
| `skill-search <keyword>` uses fzf — faster than scanning 200+ archive entries | [HMZ](https://github.com/hmzainjamil) |
| Never leave non-core skills active — collapse with `skill-off` after every task | [HMZ](https://github.com/hmzainjamil) |
| Core skills always-on: caveman, compact-guard, summarize, context-compression | [HMZ](https://github.com/hmzainjamil) |
| SKILL.md files auto-push to `claude-ai-skills` via PostToolUse hook on Write | [HMZ](https://github.com/hmzainjamil) |
| Use `skill-router` keyword map to batch-activate related skills in one command | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-tokens"></a>■ **Token Savings (5)**

| Tip | Source |
|-----|--------|
| Caveman compression cuts 60-80% of output tokens — always apply to sub-agents | [HMZ](https://github.com/hmzainjamil) |
| Never re-read files already in context — check system-reminder before Read | [HMZ](https://github.com/hmzainjamil) |
| Batch parallel tool calls — one message with 5 tool calls beats 5 sequential | [HMZ](https://github.com/hmzainjamil) |
| `compact-guard` fires at 70% context usage — forces /compact before overflow | [HMZ](https://github.com/hmzainjamil) |
| Session queue compression — write learnings as JSONL, not full prose in chat | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-git"></a>■ **GitHub API Pattern (5)**

| Tip | Source |
|-----|--------|
| Always GET SHA before PUT — stale SHA causes 422 conflict on concurrent pushes | [HMZ](https://github.com/hmzainjamil) |
| Use `gh api repos/owner/repo/contents/path -X PUT` — no git clone needed | [GitHub Docs](https://docs.github.com/en/rest/repos/contents) |
| Scrub `ghp_*`, `sk-*`, `AIRTABLE_API_KEY` via sed before base64-encoding | [HMZ](https://github.com/hmzainjamil) |
| macOS symlink conflicts: never `git push` from local clone of this repo | [HMZ](https://github.com/hmzainjamil) |
| `auto-github-push` handles routing: bin/ → claude-ai-system, skills/ → claude-ai-skills | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-memory"></a>■ **Memory System (5)**

| Tip | Source |
|-----|--------|
| 4 types: user (profile), feedback (corrections), project (status), reference (pointers) | [HMZ](https://github.com/hmzainjamil) |
| MEMORY.md index — 200 line limit, each entry ≤150 chars with file pointer | [HMZ](https://github.com/hmzainjamil) |
| Verify memory before acting — files move, functions rename — check current state | [HMZ](https://github.com/hmzainjamil) |
| Never save git history, code patterns, debugging solutions — only non-obvious facts | [HMZ](https://github.com/hmzainjamil) |
| Update stale memories immediately — wrong memory is worse than no memory | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-agents"></a>■ **Agent Orchestration (5)**

| Tip | Source |
|-----|--------|
| Sub-agents NEVER use Claude — always Tier 0 (Groq, Gemini, DeepSeek, GPT-4o-mini) | [HMZ](https://github.com/hmzainjamil) |
| Use `run_in_background=true` for research agents — continue other work in parallel | [HMZ](https://github.com/hmzainjamil) |
| `subagent_type=Explore` for codebase scans — read-only, specialized, faster | [HMZ](https://github.com/hmzainjamil) |
| Provide complete task description to agents — they start with no prior context | [HMZ](https://github.com/hmzainjamil) |
| Batch 3-5 agents in single message — parallel launch = massive time saving | [HMZ](https://github.com/hmzainjamil) |

<a id="tips-debug"></a>■ **Debugging (5)**

| Tip | Source |
|-----|--------|
| `launchctl list \| grep hmz` — check all running agents and their exit codes | [HMZ](https://github.com/hmzainjamil) |
| Exit code 256 = script not found or permission denied — `chmod +x` required | [HMZ](https://github.com/hmzainjamil) |
| `tail -f ~/.claude/logs/<agent>.log` — real-time output during testing | [HMZ](https://github.com/hmzainjamil) |
| `auto-troubleshoot` SessionStart hook catches most common plist issues | [HMZ](https://github.com/hmzainjamil) |
| Test hooks with `echo '{"tool_name":"Write","tool_input":{"file_path":"/tmp/test"}}' \| ~/.claude/bin/auto-github-push` | [HMZ](https://github.com/hmzainjamil) |

## ☠️ STARTUPS / BUSINESSES

| Feature | Replaced |
|-|-|
| **Skill Router + Hook System** | [Zapier](https://zapier.com), [Make.com](https://make.com), [n8n Cloud](https://n8n.io) |
| **LLM Burst / Tier 0 Routing** | [OpenAI API direct](https://platform.openai.com), [Anthropic API direct](https://anthropic.com) |
| **Auto GitHub Push Hook** | [GitHub Actions](https://github.com/features/actions), [CircleCI](https://circleci.com), [Travis CI](https://travis-ci.com) |
| **Compact Guard** | [MemGPT](https://memgpt.ai), [Letta](https://letta.com), [Zep](https://getzep.com) |
| **Session Queue + Auto Learn** | [Notion AI](https://notion.so/ai), [Mem.ai](https://mem.ai), [Rewind AI](https://rewind.ai) |
| **LaunchAgent Automation** | [Shortcuts](https://support.apple.com/guide/shortcuts-mac), [Raycast](https://raycast.com), [Alfred](https://alfredapp.com) |
| **Skill System (200+ skills)** | [OpenAI GPTs](https://openai.com/gpts), [Poe](https://poe.com), [Character.ai](https://character.ai) |
| **OODA Decision Framework** | [Lindy AI](https://lindy.ai), [Beam AI](https://beam.ai) |

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=hmzainjamil/claude-ai-system&type=Date)](https://star-history.com/#hmzainjamil/claude-ai-system&Date)
