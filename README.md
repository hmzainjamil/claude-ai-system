# claude-ai-system
the behavioral OS that runs before every prompt

![Claude Code](https://img.shields.io/badge/Claude_Code-System_Config-8E44AD?style=flat&labelColor=000) ![CLAUDE.md](https://img.shields.io/badge/CLAUDE.md-behavioral_mandates-blue?style=flat&labelColor=555) ![Hooks](https://img.shields.io/badge/hooks-4_events-orange?style=flat&labelColor=555) ![Skills](https://img.shields.io/badge/skills-200%2B_gated-green?style=flat&labelColor=555) ![Bin](https://img.shields.io/badge/bin-45_production_scripts-red?style=flat&labelColor=555)

HMZ Claude Code system — the behavioral OS layer governing every session. CLAUDE.md mandates, hook scripts, model routing rules, skill gating blockchain, session lifecycle automation, and 45 production scripts. Every prompt passes through this before Claude sees it.

[CLAUDE.md Mandates](#mandates) · [Hook Architecture](#hooks) · [Skill Gating](#skills) · [Bin Scripts](#bin) · [Settings](#settings) · [Gotchas](#gotchas)

## 🧠 CONCEPTS

| Feature | Location | Description |
|---|---|---|
| **Global CLAUDE.md** | `~/.claude/CLAUDE.md` | Universal behavioral rules — all projects, all sessions, cannot be overridden by prompt |
| **Project CLAUDE.md** | `~/CLAUDE.md` | Repo-specific additions, inherits global |
| **Hooks** | `~/.claude/settings.json` → hooks | Shell scripts auto-run on session events — UserPromptSubmit, Stop, compact |
| **Skill Manifest** | `~/.claude/skills/` | Active skill files loaded into context — gated via blockchain manifest |
| **Skills Archive** | `~/.claude/skills-archive/` | 9,565 dormant skills — activated on keyword match only |
| **Bin Scripts** | `~/.claude/bin/` | 45 production utility scripts — model routing, skill management, LaunchAgent ops |
| **Memory Index** | `~/.claude/projects/*/memory/MEMORY.md` | Cross-session persistent memory, loaded at session start |
| **Tier 0 Cache** | `~/.claude/tier0-cache.json` | Dedup cache for repeated prompts across Tier 0 providers |
| **Metrics Log** | `~/.claude/metrics.log` | Per-prompt skill activation log — track what fires most |
| **Session Queue** | `~/.claude/session-queue.jsonl` | Memory write queue — flushed by Stop hook into memory files |

<a id="mandates"></a>
## ⚙️ CLAUDE.MD MANDATES

■ **Tier 0 Model Routing (Immutable — Priority 1)**

```
Tier 0 (always first — 75-95% of all tasks):
  Ollama (local GPU) → Groq (llama3-70b) → Gemini 2.0 Flash
  → DeepSeek-V3 → Kimi K2.5 → GPT-4o-mini → Mistral → OpenRouter → GLM

Tier 1 (last resort — all Tier 0 exhausted):
  Claude Haiku 4.5

Tier 2 (final output layer only):
  Claude Sonnet 4.6 / Opus 4.6 — only when user sees the result
```

■ **L99 Performance Mode (Immutable)**
- Full capability on every response — no hedging, no "it depends", no half-measures
- Every task treated as maximum stakes

■ **OODA Loop (Every task)**
- Observe → Orient → Decide → Act. No flip-flopping after Decide.

■ **Skill Gating (Every session)**
- Default active: 12 core skills only
- Everything else: dormant until keyword fires `~/.claude/bin/skill-auto-activate`
- After task: `~/.claude/bin/skill-off` — non-core skills deactivated immediately

■ **Permanent Behavioral Rules**
- All generated files → `~/Downloads/` (never Desktop)
- No thermal automation (MFC popup issue)
- No Upwork/Freelancer/PPH in any BDM pipelines
- Paperclip API checked every session: `http://127.0.0.1:3100`
- All READMEs use flat badges (`style=flat`), never `for-the-badge`
- Expert README standard: 300+ lines, feature tables, tips tables, competitive context

<a id="hooks"></a>
## 💡 HOOK ARCHITECTURE

| Hook Event | Scripts | Timing | Purpose |
|---|---|---|---|
| `UserPromptSubmit` | `tier0-prompt-inject` | Before every response | Injects L99+OODA, fires Tier 0 blast |
| `UserPromptSubmit` | `skill-auto-activate` | Before every response | Keyword match → activates needed skills |
| `UserPromptSubmit` | `auto-troubleshoot` | Before every response | Checks LaunchAgent health, reports issues |
| `UserPromptSubmit` | `paperclip-ceo-check` | Before every response | Pings Paperclip API at 127.0.0.1:3100 |
| `Stop` | `session-queue-processor` | After every response | Flushes session-queue.jsonl → memory files |
| `Stop` | `skill-cleanup` | After every response | Deactivates all non-core skills |
| `compact` | `context-guard` | At compaction | Warns when approaching context limit |

**Hook config in `~/.claude/settings.json`:**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {"type": "command", "command": "~/.claude/bin/tier0-prompt-inject"},
      {"type": "command", "command": "~/.claude/bin/skill-auto-activate"},
      {"type": "command", "command": "~/.claude/bin/auto-troubleshoot"}
    ],
    "Stop": [
      {"type": "command", "command": "~/.claude/bin/session-learn"},
      {"type": "command", "command": "~/.claude/bin/skill-reset"}
    ]
  }
}
```

<a id="skills"></a>
## 🔧 SKILL GATING SYSTEM

**Default active (always loaded, cost ~10K tokens):**
```
caveman              compact-guard        compress
context-compression  context-window-management
find-skills          launch-optimized     optimize-commands
optimize-dgm-command skill-router         summarize
token-turbo          auto-learn
```

**Auto-activation map (fires on keyword match):**

| Prompt Keywords | Skills Activated | Script |
|---|---|---|
| `ads, ppc, meta, google, campaign, roas` | `ads-strategy, ads-copy, ads-creative, ads-keywords` | `skill-auto-activate` |
| `seo, geo, ranking, schema, crawl` | `geo, geo-technical, geo-content, geo-schema` | `skill-auto-activate` |
| `legal, contract, nda, compliance` | `legal, legal-review` | `skill-auto-activate` |
| `marketing, brand, email, funnel` | `market, market-brand, market-copy` | `skill-auto-activate` |
| `pdf, report, audit, reportlab` | `reportlab-pdf-master` | `skill-auto-activate` |
| `agent, multi-agent, orchestrate` | `all-agents` | `skill-auto-activate` |

<a id="bin"></a>
## 🛠 BIN SCRIPTS (45 production scripts)

■ **Model Routing**
| Script | Purpose |
|---|---|
| `tier0-prompt-inject` | Injects L99+OODA + fires Tier 0 blast before every prompt |
| `tier0-blast` | Fires all Tier 0 models synchronously |
| `tier0-blast-async` | Fires Tier 0 in background (non-blocking) |
| `tier0-burst` | Smart burst: checks RAM, routes to best available |
| `tier0-cache-inject` | Cache-aware inference — dedup repeated prompts |
| `tier0-check` | Pings all Tier 0 providers, logs availability |
| `llm-burst` | CLI wrapper: `llm-burst 'prompt'` → auto-routes |
| `llm-burst-run` | Internal executor called by llm-burst |

■ **Skill Management**
| Script | Purpose |
|---|---|
| `skill-auto-activate` | UserPromptSubmit hook — keyword match → activation |
| `skill-on` | Manual skill activation |
| `skill-off` | Deactivate one skill |
| `skill-reset` | Deactivate all non-core (called by Stop hook) |
| `skill-search` | Find skills by keyword across archive |
| `skill-status` | Show currently active skills |
| `skill-load` | Load skill file into context |
| `skill-guardian` | Audit: detect skill drift, unused activations |
| `skill-scanner` | Scan archive for keyword triggers |
| `skill-watcher` | File watcher: auto-reload skills on change |
| `skill-metrics` | Report skill activation frequency |

■ **Agency / BDM**
| Script | Purpose |
|---|---|
| `agency` | DigiMinds agency runner |
| `agency-run` | Execute agency workflow |
| `agency-runner.sh` | Shell wrapper for agency |
| `agency-email-pickup` | Process incoming client emails |
| `hmz-bdm-catchup` | Catch up on missed BDM sweep tasks |
| `hmz-bdm-state-update` | Update BDM pipeline state |

■ **Infrastructure**
| Script | Purpose |
|---|---|
| `github-sync` | Sync entire system to GitHub portfolio repos |
| `github-portfolio-init` | Initialize new portfolio repo |
| `git-auto-init` | Auto-init + push any local dir to GitHub |
| `openclaw-bridge` | Bridge LaunchAgent status check |
| `openclaw-computer-control` | Queue computer control tasks |
| `openclaw-skill-add` | Add new skill to OpenClaw gateway |
| `memory-sync` | Sync memory files to GitHub |
| `session-learn` | Stop hook: process session queue → memory |
| `auto-troubleshoot` | Health check all LaunchAgents |
| `security-status` | Audit exposed ports, running processes |
| `smart-session-start` | Enhanced session startup with health checks |
| `workflow-dag` | Visualize workflow dependency graph |

<a id="settings"></a>
## 📋 SETTINGS

**`~/.claude/settings.json` key fields:**
```json
{
  "model": "claude-sonnet-4-6",
  "autoApprove": ["Read", "Glob", "Grep", "Bash", "Write", "Edit"],
  "permissions": {
    "allow": ["Bash(~/.claude/bin/*)", "Edit(~/**)", "Write(~/Downloads/*)"]
  },
  "statusLine": "RAM:{ram_free} | Context:{context_pct}% | Model:{model}",
  "theme": "dark",
  "compactThreshold": 0.85
}
```

<a id="gotchas"></a>
## ☠️ GOTCHAS

| Gotcha | Fix |
|---|---|
| `CLAUDE.md` instructions ignored if file > 200 lines — Claude stops reading | Keep global CLAUDE.md < 200 lines, use @imports for overflow |
| Skill activation adds 2-5K tokens per skill — over-activation bloats context | Never activate > 5 skills simultaneously |
| Stop hook `session-learn` fails silently if `jq` not installed | `brew install jq` |
| `tier0-prompt-inject` fires even on trivial prompts ("yes", "ok") — adds latency | Add prompt length check: skip if < 10 chars |
| `skill-auto-activate` can activate conflicting skills (ads + seo simultaneously) | skills have `conflicts: []` field — check before loading |
| GitHub sync uploads settings.json which may contain sensitive API key references | settings.json uses `$ENV_VAR` references, not literal keys |
| `auto-troubleshoot` reports false positives when LaunchAgent just restarted | Add 30s grace period: check if PID exists, not just exit code |

## 📁 REPO STRUCTURE

```
claude-ai-system/
├── config/
│   ├── CLAUDE.md              ← global behavioral mandates
│   ├── settings.json          ← Claude Code settings template
│   ├── AGENCY_MANIFEST.md     ← DigiMinds agency skill/agent manifest
│   └── TIER0-SETUP.md         ← Tier 0 model setup guide
├── bin/                       ← 45 production scripts (all executable)
├── skills-active/             ← 13 active default skill files
├── hooks/                     ← hook scripts by event type
└── README.md
```
