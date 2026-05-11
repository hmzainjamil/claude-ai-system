# claude-ai-system
The complete Claude Code infrastructure — hooks, skills, bin scripts, LaunchAgents, and config that power HMZ's autonomous AI agency stack.

![updated](https://img.shields.io/badge/synced_daily-6%3A30AM-white?style=flat&labelColor=555) [![scripts](https://img.shields.io/badge/bin_scripts-45-blue?style=flat&labelColor=555)](automations/bin/) [![skills](https://img.shields.io/badge/skills-13_core-green?style=flat&labelColor=555)](skills-active/) [![hooks](https://img.shields.io/badge/hooks-4_events-orange?style=flat&labelColor=555)](.claude/settings.json) [![company](https://img.shields.io/badge/DigiMinds-agency-red?style=flat&labelColor=555)](https://digiminds.org)

[Concepts](#-concepts) · [Hot](#-hot) · [Architecture](#️-architecture) · [Tips](#-tips-and-tricks-28) · [Replaced](#️-startups--businesses) · [Stars](#star-history)

---

## 🧠 CONCEPTS

| Feature | Location | Description |
|---------|----------|-------------|
| [**CLAUDE.md Mandates**](CLAUDE.md) | `CLAUDE.md` | G0DM0D3 model routing · L99 performance mode · OODA decision loop · Skill gating protocol — hardcoded for every session |
| [**Bin Scripts (45)**](automations/bin/) | `automations/bin/` | `github-sync` `skill-on/off/search/status/reset` `llm-burst` `tier0-prompt-inject` `skill-auto-activate` `openclaw-bridge` `auto-troubleshoot` `paperclip-*` — full CLI automation layer |
| [**Hook System**](.claude/settings.json) | `.claude/settings.json` | UserPromptSubmit → `skill-auto-activate` + `tier0-prompt-inject` · PostToolUse → `auto-github-push` + `memory-sync` · Stop → `session-queue-processor` |
| [**Skills (Active)**](skills-active/) | `skills-active/` | 13 always-on core skills: `caveman` `compress` `context-compression` `compact-guard` `skill-router` `find-skills` `launch-optimized` `summarize` — zero overhead |
| [**Skills Archive**](skills-archive/) | `skills-archive/` | 100+ domain skills dormant until needed: ads, geo, legal, agents, apify, startup, market — blockchain-gated |
| [**LaunchAgents**](automations/launchagents/) | `automations/launchagents/` | `ai.hmz.github-portfolio-sync` (6:30AM) · `ai.openclaw.gateway` · `ai.hmz.paperclip` · 6 Paperclip scheduled engines |
| [**Memory System**](memory/) | `~/.claude/projects/.../memory/` | Persistent cross-session memory: user · feedback · project · reference types — auto-loaded via system-reminder |
| [**Config**](config/) | `config/` | `settings.json` · `keybindings.json` · `skills-lock.json` manifest |
| [**Installed Repos**](installed-repos/) | `installed-repos/` | Mirror of 50+ third-party tool READMEs for quick local reference |

### 🔥 Hot

| Feature | Location | Description |
|---------|----------|-------------|
| [**auto-github-push**](automations/bin/auto-github-push) | `automations/bin/auto-github-push` | PostToolUse hook — every file written to `~/.claude/bin/` or `skills/` auto-pushes to GitHub via API. No git, no merge conflicts |
| [**skill-auto-activate**](automations/bin/skill-auto-activate) | `automations/bin/skill-auto-activate` | Fires on every UserPromptSubmit — keyword-matches prompt → auto-loads domain skills before Claude responds |
| [**llm-burst**](automations/bin/llm-burst) | `automations/bin/llm-burst` | Blasts prompt to 8 models in parallel (Groq+Gemini+Ollama+DeepSeek+GPT-4o-mini+GLM+Gemma4) — judge picks best. Zero Claude tokens for sub-tasks |
| [**tier0-prompt-inject**](automations/bin/tier0-prompt-inject) | `automations/bin/tier0-prompt-inject` | Injects G0DM0D3 routing rules into every session — enforces Tier 0 model use automatically |

---

## ⚙️ ARCHITECTURE

```
~/.claude/
├── bin/                  ← 45 automation scripts
│   ├── skill-on/off      ← skill activation CLI
│   ├── llm-burst         ← 8-model parallel inference
│   ├── github-sync       ← daily portfolio sync
│   └── auto-github-push  ← instant PostToolUse push
├── skills/               ← 13 always-active core skills
├── skills-archive/       ← 100+ dormant domain skills
├── agents/               ← agent definitions
├── settings.json         ← hook config (4 event types)
└── skills-lock.json      ← blockchain manifest

~/Library/LaunchAgents/
├── ai.hmz.github-portfolio-sync.plist   ← daily 6:30AM
├── ai.openclaw.gateway.plist            ← always-on
└── ai.hmz.paperclip.plist               ← CEO loop
```

| Layer | Component | Trigger |
|-------|-----------|---------|
| Prompt hooks | `skill-auto-activate` + `tier0-prompt-inject` | Every UserPromptSubmit |
| File hooks | `auto-github-push` + `memory-sync` | Every Write/Edit |
| Session hooks | `session-queue-processor` | Session Stop |
| Daemons | 8 LaunchAgents | Scheduled + always-on |
| Models | 8 Tier-0 burst | Every sub-task |

---

## 💡 TIPS AND TRICKS (28)

[Hooks](#tips-hooks) · [Skills](#tips-skills) · [Scripts](#tips-scripts) · [Routing](#tips-routing) · [Git](#tips-git) · [Debugging](#tips-debugging)

<a id="tips-hooks"></a>■ **Hooks (5)**

| Tip | Source |
|-----|--------|
| Hook order matters: `skill-auto-activate` must run before `tier0-prompt-inject` in UserPromptSubmit | [HMZ System SOP](https://github.com/hmzainjamil/claude-ai-system) |
| PostToolUse `Write\|Edit` now auto-pushes to GitHub — never manually push bin scripts again | [auto-github-push](automations/bin/auto-github-push) |
| Stop hook runs `session-queue-processor` — saves learnings to memory between sessions | [memory system](https://github.com/hmzainjamil/hmz-claude-mem-main) |
| Test any hook: simulate trigger by running the script directly from CLI | [settings.json](config/) |
| Hook failures are silent — always check `~/.claude/logs/` after unexpected behavior | [Ops rule](automations/bin/) |

<a id="tips-skills"></a>■ **Skills (7)**

| Tip | Source |
|-----|--------|
| Core skills cost near-zero tokens — domain skills load context space, deactivate after task | [Skill gating](skills-active/) |
| `skill-auto-activate` handles 80% of cases — `skill-on` only for edge cases | [skill-auto-activate](automations/bin/skill-auto-activate) |
| Never leave domain skills active — `skill-off <name>` is mandatory after every task | [Gating protocol](CLAUDE.md) |
| `skill-status` shows exact manifest with timestamps — check before complex multi-skill tasks | [skill-status](automations/bin/) |
| Skills in wrong folder break everything — active → `~/.claude/skills/`, dormant → `skills-archive/` | [Architecture](skills-active/) |
| Symlink skills fail on GitHub checkout — upload as flat `{name}.md` files instead | [GitHub workaround](automations/bin/github-sync) |
| `skill-reset` rebuilds manifest from filesystem — use when lock file drifts from reality | [skill-reset](automations/bin/) |

<a id="tips-scripts"></a>■ **Scripts (6)**

| Tip | Source |
|-----|--------|
| `llm-burst "prompt"` → 8 parallel models → judge picks best — never use Claude for sub-tasks | [llm-burst](automations/bin/llm-burst) |
| `github-sync` runs at 6:30AM — scrubs tokens from LaunchAgent plists before committing | [github-sync](automations/bin/github-sync) |
| `auto-troubleshoot` proactively checks all LaunchAgents every session — never wait to be asked | [auto-troubleshoot](automations/bin/auto-troubleshoot) |
| `openclaw-bridge` bridges Composio + MCP + Paperclip through one persistent gateway | [openclaw-bridge](automations/bin/openclaw-bridge) |
| All new scripts go in `~/.claude/bin/` — auto-pushed to GitHub via PostToolUse hook | [auto-github-push](automations/bin/auto-github-push) |
| `chmod +x` every new script immediately — GitHub push fails on non-executable scripts | [Ops rule](automations/bin/) |

<a id="tips-routing"></a>■ **Routing (5)**

| Tip | Source |
|-----|--------|
| `llm-burst` default: Groq+Gemini+Ollama+DeepSeek+GPT-4o-mini+GLM+Gemma4 — 8 models in parallel | [G0DM0D3](https://github.com/hmzainjamil/hmz-g0dm0d3) |
| Research → Groq (fastest) · Code → DeepSeek/Ollama · Analysis → Gemini · Final → Claude | [Tier 0 routing](CLAUDE.md) |
| Gemini 2.0 Flash = 1,500 free calls/day — use for all analysis and summarization | [API limits](automations/bin/llm-burst) |
| `tier0-prompt-inject` is hardcoded via CLAUDE.md — cannot be overridden per-prompt | [Design](CLAUDE.md) |
| Claude Haiku = Tier 1 (absolute last resort), Claude Sonnet = Tier 2 (final output only) | [Routing hierarchy](CLAUDE.md) |

<a id="tips-git"></a>■ **Git (2)**

| Tip | Source |
|-----|--------|
| Never use `git push` for claude-ai-system — use GitHub Contents API to avoid symlink conflicts | [Lesson learned](automations/bin/github-sync) |
| SHA mismatch on API push = another process updated the file — re-fetch SHA and retry | [API gotcha](automations/bin/auto-github-push) |

<a id="tips-debugging"></a>■ **Debugging (3)**

| Tip | Source |
|-----|--------|
| LaunchAgent exit=256 = script returned exit 1 — check `~/.claude/logs/*-error.log` | [Debug SOP](automations/bin/auto-troubleshoot) |
| `launchctl list \| grep ai.hmz` — verify all daemons running at session start | [Startup check](automations/bin/auto-troubleshoot) |
| `~/.claude/logs/auto-github-push.log` — tracks every auto-push with timestamp | [Log location](automations/bin/auto-github-push) |

---

## ☠️ STARTUPS / BUSINESSES

| Feature | Replaced |
|-|-|
| **Skill gating + auto-activate** | [Continue.dev](https://continue.dev), [Cursor Rules](https://cursor.sh), [Windsurf](https://codeium.com/windsurf) — static rules, no gating |
| **llm-burst (8-model parallel)** | [LiteLLM](https://litellm.ai), [OpenRouter](https://openrouter.ai) — passive routing only, no parallel judge |
| **LaunchAgent daemons** | [n8n](https://n8n.io), [Zapier](https://zapier.com) — cloud-only, not local-first |
| **auto-github-push hook** | Manual git push, [GitHub Desktop](https://desktop.github.com) — zero automation |
| **GitHub Contents API sync** | Raw `git push` — fails on macOS symlinks, diverges on concurrent pushes |
| **Persistent memory system** | [MemGPT](https://memgpt.ai), [Zep](https://getzep.com) — separate service, not native |

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=hmzainjamil/claude-ai-system&type=Date)](https://star-history.com/#hmzainjamil/claude-ai-system&Date)