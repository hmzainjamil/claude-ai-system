# Hermes Agent (NousResearch) — Full System Entry

**Binary:** `~/.hermes/bin/hermes` (auto-detected by hermes-autodetect on SessionStart)
**Model:** `openrouter/nousresearch/hermes-3-llama-3.1-405b:free` (Tier 0, free)
**Config:** `~/.hermes/config.yaml` (auto-configured, keys from ~/.hermes/.env)
**Paperclip type:** `hermes_local` (adapter v0.3.0, wired at localhost:3100)

## Quick Commands
```bash
hermes                          # interactive TUI
hermes chat -q "task" -Q        # one-shot headless (used by Paperclip)
hermes model                    # switch model
hermes skills                   # list/load skills
hermes sessions                 # search past sessions
hermes schedule                 # manage cron tasks
hermes --version                # check version
```

## Self-Evolution
```bash
evolve-skill ads-strategy --iterations 10       # evolve any SKILL.md
evolve-skill optimize-commands --iterations 5   # evolve this skill
evolve-skill [skill] --eval sessiondb           # use real session history
```

## Function Calling (API, no local GPU)
```bash
hermes-fc "What is AAPL stock price?"           # uses nousresearch/hermes-3 free
hermes-fc --json "Describe a SaaS company"      # structured JSON output
hermes-fc --model nousresearch/hermes-4-70b "complex task"
```

## TCC Route
- Keyword: `hermes`, `nous`, `evolve skill`, `self-evolve`
- Routes to: `hermes_local` via Paperclip adapter

## Auto-Detection
- Runs on every SessionStart via hook
- LaunchAgent `ai.hmz.hermes-watch` polls every 2 min
- Auto-adds to PATH, auto-writes config if missing

## Capabilities vs Claude Code
| Feature | Claude Code | Hermes |
|---|---|---|
| Persistent memory | session only | ✅ SQLite FTS5 cross-session |
| Native tools | ~5 | ✅ 30+ |
| Skills | shared | ✅ 80+ + auto-creates from experience |
| Multi-provider | Anthropic only | ✅ OpenRouter, Groq, Kimi, OpenAI, etc |
| Sub-agents | Agent tool | ✅ native parallel |
| Self-improving | ❌ | ✅ creates/improves skills automatically |
| Scheduled tasks | ❌ | ✅ built-in cron |
