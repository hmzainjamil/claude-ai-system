# claude-ai-system

> **Complete Claude AI automation OS — MAE orchestrator, TCC queue, Tier 0 routing, 45 skills, 210 agents, daily lead pipelines**

<p align="center">
  <a href="https://github.com/hmzainjamil/claude-ai-system/stargazers"><img src="https://img.shields.io/github/stars/hmzainjamil/claude-ai-system?style=for-the-badge&labelColor=555&color=yellow" alt="Stars"/></a>
  <a href="https://github.com/hmzainjamil/claude-ai-system/network/members"><img src="https://img.shields.io/github/forks/hmzainjamil/claude-ai-system?style=for-the-badge&labelColor=555&color=blue" alt="Forks"/></a>
  <a href="https://github.com/hmzainjamil/claude-ai-system/issues"><img src="https://img.shields.io/github/issues/hmzainjamil/claude-ai-system?style=for-the-badge&labelColor=555&color=red" alt="Issues"/></a>
  <a href="https://github.com/hmzainjamil/claude-ai-system/pulls"><img src="https://img.shields.io/github/issues-pr/hmzainjamil/claude-ai-system?style=for-the-badge&labelColor=555&color=purple" alt="PRs"/></a>
  <a href="https://github.com/hmzainjamil/claude-ai-system/commits/main"><img src="https://img.shields.io/github/last-commit/hmzainjamil/claude-ai-system?style=for-the-badge&labelColor=555&color=green" alt="Last Commit"/></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Skills-45-blue?style=flat&labelColor=555"/>
  <img src="https://img.shields.io/badge/Agents-210-orange?style=flat&labelColor=555"/>
  <img src="https://img.shields.io/badge/Tier_0-zero_Claude_tokens-green?style=flat&labelColor=555"/>
  <img src="https://img.shields.io/badge/License-MIT-lightgrey?style=flat&labelColor=555"/>
</p>

---

## Why This Exists

Claude Code alone is one AI assistant. `claude-ai-system` is an autonomous operating system built on top of Claude Code — MAE orchestrates 12-agent swarms on every task, TCC queues and routes 18 specialist agents, hooks automate everything from session start to daily lead generation, and Tier 0 routing ensures Claude tokens are only spent on final synthesis, never on sub-tasks.

---

## At a Glance

| Component | Location | Role |
|---|---|---|
| MAE orchestrator | `bin/mae-bridge.sh` | 12-agent swarm, decompose→execute→synthesize |
| TCC queue | `tcc-routes/routes.json` | 18 specialist agents, wave-batched |
| Tier 0 routing | `config/model-rules.json` | Groq→Gemini→DeepSeek, zero Claude tokens for sub-tasks |
| Skill router | `skills/skill-router/` | Keyword→skill auto-activation on every prompt |
| LaunchAgent | `launchd/` | Always-on macOS service |
| Hooks | `hooks/` | UserPromptSubmit, PostToolUse, Stop hooks |
| Paperclip sync | `bin/paperclip-sync.sh` | All outputs synced to Paperclip AI OS |
| Health monitor | `bin/health.sh` | Pings endpoints, Slack alert + auto-restart |
| n8n workflows | `workflows/` | 8,159 workflow JSONs |
| CLAUDE.md rules | `.claude/CLAUDE.md` | Caveman mode, routing, skill protocol |

---

## 🧠 CONCEPTS

| Concept | Description |
|---|---|
| **MAE** | Master Automation Engine — Groq decomposes task → specialist swarm executes → Opus synthesizes |
| **TCC** | Task Command Center — queue system routing tasks to 18 specialist agents |
| **Tier 0** | Free model tier: Groq, Ollama, DeepSeek, Gemini — never spend Claude tokens on sub-tasks |
| **Wave batching** | Spawn agents in waves of 6 — prevents OOM on 16GB RAM |
| **Skill router** | Reads prompt keywords → auto-loads matching skills → no manual activation |
| **LaunchAgent** | macOS always-on service — KeepAlive=true, RunAtLoad=true |
| **Paperclip CEO** | All outputs synced to Paperclip AI — zero-human company OS |
| **llm-burst** | Parallel blast across Groq+Gemini+DeepSeek simultaneously |
| **Session queue** | `~/.claude/session-queue.jsonl` — learnings written at Stop hook → processed into memory |
| **Health monitor** | Pings all endpoints every 5min — Slack alert + restart on failure |

### 🔥 Hot

- **Zero-Claude sub-tasks** — 95% of work happens in Tier 0 (Groq/Ollama/DeepSeek). Claude only touches final synthesis
- **8,159 n8n workflow JSONs** — grep before building any automation from scratch
- **LaunchAgent always-on** — system restarts even if mac reboots, crashes, or goes to sleep
- Source → [HMZ](https://github.com/hmzainjamil)

---

## ⚙️ HOW IT WORKS

```
User prompt submitted
    ↓ UserPromptSubmit hook → skill-router loads matching skills
    ↓ MAE: mae run "goal"
    ↓ Groq decomposes task into N sub-tasks
    ↓ TCC routes sub-tasks to specialist agents (wave-batched, 6/wave)
    ↓ Tier 0 agents execute (Groq/Ollama/DeepSeek)
    ↓ Results saved to ~/.claude/tcc-logs/
    ↓ Opus sub-agent synthesizes final output
    ↓ Stop hook: learnings → session-queue.jsonl → Paperclip sync
```

---

## 🚀 INSTALL

```bash
git clone https://github.com/hmzainjamil/claude-ai-system ~/.claude-ai-system
cd ~/.claude-ai-system
bash install.sh

# Load LaunchAgent
cp launchd/com.claude.mae.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.claude.mae.plist

# Verify
bash bin/health.sh
```

---

## 📟 USAGE

```bash
# Run task with MAE
mae run "Build REST API for user auth"

# Parallel blast
tcc blast "research auth patterns" "design DB schema" "draft API spec"

# Fire all queued
tcc fire all

# Daily ops
mae daily

# Dashboard
tcc-dashboard

# Health check
bash bin/health.sh
```

---

## ⚙️ CONFIGURATION

| Variable | Default | Description |
|---|---|---|
| `MAE_PROVIDER` | `groq` | Primary inference provider |
| `MAE_MODEL` | `llama-3.3-70b` | Primary model |
| `TCC_WAVE_SIZE` | `6` | Agents per wave |
| `TCC_MAX_QUEUE` | `50` | Max queued tasks |
| `SYNTHESIS_MODEL` | `opus` | Final synthesis model |
| `PAPERCLIP_URL` | `http://127.0.0.1:3100` | Paperclip endpoint |
| `PAPERCLIP_CID` | required | Company ID |
| `HEALTH_INTERVAL` | `300` | Health check interval (sec) |
| `LOG_DIR` | `~/.claude/tcc-logs/` | Run log directory |
| `SKILL_DIR` | `~/.claude/skills/` | Skills directory |

---

## 💡 TIPS AND TRICKS

### Performance
1. **Wave size tuning** — 16GB RAM → wave_size=6. 32GB → wave_size=12. Monitor with `htop` during first run. Source → [HMZ](https://github.com/hmzainjamil)
2. **Groq free tier** — Groq's free API handles 100% of sub-task work. Save Anthropic credits for synthesis only. Source → [HMZ](https://github.com/hmzainjamil)
3. **Ollama local** — `ollama pull qwen2.5:7b` — fastest Tier 0 option for code tasks, zero API cost. Source → [HMZ](https://github.com/hmzainjamil)

### Integration
4. **Paperclip sync** — every MAE run output lands in Paperclip as an issue comment — full audit trail. Source → [HMZ](https://github.com/hmzainjamil)
5. **n8n grep before build** — `grep -r "webhook" workflows/` before writing new automation. Source → [HMZ](https://github.com/hmzainjamil)
6. **Skill router keywords** — add keywords to SKILL.md `triggers:` block to auto-load on matching prompts. Source → [HMZ](https://github.com/hmzainjamil)

### Advanced
7. **LaunchAgent logs** — `tail -f /tmp/mae.log` to watch LaunchAgent execution in real time. Source → [HMZ](https://github.com/hmzainjamil)
8. **Session queue drain** — Stop hook writes to `session-queue.jsonl` — processed nightly into memory files. Source → [HMZ](https://github.com/hmzainjamil)
9. **Health alerts** — configure `SLACK_WEBHOOK_URL` in `.env` for instant alerts when any endpoint fails. Source → [HMZ](https://github.com/hmzainjamil)

### Debugging
10. **TCC dashboard** — `tcc-dashboard` shows live queue depth, agent status, and cost metrics. Source → [HMZ](https://github.com/hmzainjamil)
11. **Model fallback** — if Groq rate-limited, system auto-falls to Gemini → DeepSeek → Bytez. Source → [HMZ](https://github.com/hmzainjamil)
12. **Log search** — `grep -r "ERROR" ~/.claude/tcc-logs/` finds all failures across all runs. Source → [HMZ](https://github.com/hmzainjamil)

---

## 🔧 TROUBLESHOOTING

| Issue | Cause | Fix |
|---|---|---|
| LaunchAgent not starting | plist path wrong | `launchctl list \| grep mae` |
| MAE hangs | Wave too large for RAM | Reduce `TCC_WAVE_SIZE` to 4 |
| Groq rate limit | Free tier exceeded | Switch to `MAE_PROVIDER=gemini` |
| Paperclip sync failing | Server not running | `paperclip start` |
| Health check red | Endpoint down | Check `.env` API keys |
| Skills not loading | Wrong directory | Ensure `~/.claude/skills/` path |

---

## 📊 ARCHITECTURE

```
claude-ai-system/
├── bin/                    # Core automation scripts
│   ├── mae-bridge.sh       # MAE entry point
│   ├── tcc.sh              # Task queue runner
│   ├── health.sh           # Endpoint monitor
│   └── paperclip-sync.sh   # Paperclip integration
├── config/
│   └── model-rules.json    # Tier 0 routing rules
├── tcc-routes/
│   └── routes.json         # 18 specialist agent routes
├── skills/                 # 45 Claude Code skills
├── hooks/                  # SessionStart, PostToolUse, Stop
├── launchd/                # macOS LaunchAgent plists
├── workflows/              # 8,159 n8n workflow JSONs
└── .claude/
    └── CLAUDE.md           # Master instruction file
```

---

## 🗺️ ROADMAP

- [ ] Windows support (WSL2 + Task Scheduler equivalent)
- [ ] Web dashboard — real-time MAE run visualization
- [ ] Cost analytics — per-task token cost breakdown
- [ ] Model benchmark tracker — auto-update routing rules based on performance
- [ ] Docker deployment for team use

---

## ☠️ STARTUPS / BUSINESSES

This system is the backbone of DigiMinds agency operations: daily lead generation, client audit PDFs, social content, cold email sequences — all automated. Zero human time on standard deliverables. Engineers only touch creative decisions.

**Cost:** $0-50/mo API costs for full automation stack that replaces a junior employee.

---

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=hmzainjamil/claude-ai-system&type=Date)](https://star-history.com/#hmzainjamil/claude-ai-system&Date)

---

<p align="center">
  Built by <a href="https://github.com/hmzainjamil">HMZ</a> · <a href="https://github.com/hmzainjamil/claude-ai-system/issues">Issues</a> · <a href="https://github.com/hmzainjamil/claude-ai-system/pulls">PRs</a>
</p>
