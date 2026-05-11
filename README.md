# claude-ai-system
HMZ Claude Code system configuration — CLAUDE.md, hooks, settings, and behavioral mandates

![Claude Code](https://img.shields.io/badge/Claude_Code-system_config-orange?style=flat&labelColor=000) ![Hooks](https://img.shields.io/badge/hooks-UserPromptSubmit%7CStop-blue?style=flat&labelColor=555) ![L99](https://img.shields.io/badge/L99-Max_Performance-red?style=flat&labelColor=555)

The system configuration layer powering HMZ's Claude Code environment.

---

## 🧠 CONFIGURATION HIERARCHY

| File | Scope | Purpose |
|------|-------|---------|
| `~/.claude/CLAUDE.md` | Global | Model routing, L99, OODA, skill gating |
| `~/CLAUDE.md` | Project | Project-specific overrides |
| `~/.claude/settings.json` | System | Hooks, permissions, model config |
| `~/.mcp.json` | Global | All MCP server definitions |

## ⚙️ HOOK SYSTEM

| Event | Hook Script | What it does |
|-------|------------|--------------|
| `UserPromptSubmit` | `skill-auto-activate` | Paperclip health check + keyword skill activation |
| `Stop` | `auto-learn` | Writes session learnings to `session-queue.jsonl` |
| `SessionStart` | `compact-guard` | Checks LaunchAgent health, BDM missed tasks |

## 💡 BEHAVIORAL MANDATES (hardcoded)

■ **L99 — Max Performance Mode**
- Full capability on every response. No hedging.
- Treat every task as highest stakes possible.

■ **OODA Loop — every prompt**
1. Observe — read existing state before acting
2. Orient — model the problem, identify constraints
3. Decide — commit to clear action plan
4. Act — execute precisely

■ **Model Routing — enforced on every sub-task**
- Tier 0 first: Ollama / Groq / Gemini / DeepSeek
- Claude only for final output layer
- 75-95% token savings enforced automatically

---
Built by [HMZ](https://github.com/hmzainjamil) · [DigiMinds](https://digiminds.org)
