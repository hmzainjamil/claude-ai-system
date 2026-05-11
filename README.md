# claude-ai-system

![Claude Code](https://img.shields.io/badge/Claude_Code-system_config-8E44AD?style=flat&labelColor=000) ![CLAUDE.md](https://img.shields.io/badge/CLAUDE.md-behavioral_mandates-blue?style=flat&labelColor=555) ![Hooks](https://img.shields.io/badge/hooks-UserPromptSubmit_%7C_Stop_%7C_compact-orange?style=flat&labelColor=555) ![Status](https://img.shields.io/badge/status-always--active-green?style=flat&labelColor=555)

HMZ Claude Code system configuration — the behavioral OS layer that governs every Claude session. CLAUDE.md mandates, hook scripts, model routing rules, skill gating logic, and session lifecycle automation. Touches every prompt before Claude sees it.

## 🧠 WHAT THIS IS

Claude Code reads `CLAUDE.md` before every response. This repo holds the full configuration stack that makes Claude Code behave as a production AI OS rather than a chat assistant.

| Component | Location | Purpose |
|---|---|---|
| Global CLAUDE.md | `~/.claude/CLAUDE.md` | Universal rules — all projects, all sessions |
| Project CLAUDE.md | `~/CLAUDE.md` | Repo-specific overrides |
| Hook scripts | `~/.claude/hooks/` | Auto-run on session events |
| Skill manifest | `~/.claude/skills/` | Active skill files loaded into context |
| Memory index | `~/.claude/projects/*/memory/MEMORY.md` | Cross-session persistent memory |

## ⚙️ CLAUDE.MD MANDATES

**Tier 0 Model Routing (highest priority — overrides everything):**
```
Tier 0 (always first): Ollama → Groq → Gemini → DeepSeek → Mistral → GPT-4o-mini
Tier 1 (last resort):  Claude Haiku
Tier 2 (final layer):  Claude Sonnet / Opus — ONLY for user-facing final output
```
Result: 75-95% Claude token savings on every session.

**L99 Performance Mode:**
- Full capability on every response — no hedging, no "it depends" stalling
- Treat every task as maximum stakes

**OODA Loop:**
- Every task: Observe → Orient → Decide → Act
- No half-measures, no flip-flopping

**Skill Gating:**
- Default active: `caveman, launch-optimized, compress, context-window-management, find-skills`
- Everything else: dormant in `~/.claude/skills-archive/` until keyword match fires

## 💡 HOOK ARCHITECTURE

```bash
~/.claude/hooks/
├── UserPromptSubmit/
│   ├── tier0-prompt-inject.sh     ← injects L99+OODA into every prompt
│   ├── skill-auto-activate.sh     ← keyword matches → activates skills
│   └── paperclip-ceo-check.sh    ← verifies Paperclip API is running
├── Stop/
│   ├── session-queue-processor.sh ← processes ~/.claude/session-queue.jsonl → memory files
│   └── skill-cleanup.sh           ← deactivates all non-core skills
└── compact/
    └── context-guard.sh           ← warns when approaching context limit
```

**Hook trigger map:**
| Hook | When | Action |
|---|---|---|
| `UserPromptSubmit` | Before every response | Model routing inject, skill activation, Paperclip check |
| `Stop` | Session end | Memory queue flush, skill cleanup |
| `compact` | Context approaching limit | Compression trigger, summary request |

## 🔧 BEHAVIORAL SETTINGS

**`.claude/settings.json`:**
```json
{
  "model": "claude-sonnet-4-6",
  "autoApprove": ["Read", "Glob", "Grep", "Bash"],
  "contextWindowBuffer": 0.15,
  "compactThreshold": 0.85
}
```

**Key enforced behaviors:**
- Never use `for-the-badge` badges in READMEs — always `style=flat`
- All generated files → `~/Downloads/` (never Desktop)
- Paperclip API checked on every session start: `http://127.0.0.1:3100`
- No thermal management automation (MFC popup issue)
- No Upwork/Freelancer/PPH in BDM pipelines — LinkedIn + Indeed only

## ☠️ WHY A SYSTEM CONFIG REPO

Claude Code settings drift. Machines get rebuilt. Configs get overwritten by updates.
This repo is the source of truth: version-controlled, auditable, reproducible.
Any machine running `git clone` + setup script → identical Claude Code behavior in minutes.

## 📁 REPO STRUCTURE

```
claude-ai-system/
├── CLAUDE.md                      ← global behavioral mandates (copy of ~/.claude/CLAUDE.md)
├── hooks/
│   ├── UserPromptSubmit/          ← pre-prompt hooks
│   ├── Stop/                      ← post-session hooks
│   └── compact/                   ← context management hooks
├── settings/
│   └── settings.json              ← Claude Code settings template
├── memory/
│   └── MEMORY.md                  ← memory index snapshot
└── setup.sh                       ← bootstrap script: links configs to ~/.claude/
```
