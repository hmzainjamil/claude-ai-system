---
name: openclaw-agent37
description: "OpenClaw + Agent37 integration. Control Mac online (Agent37 cloud) and offline (local). Bridge between Claude Code, OpenClaw gateway, and Agent37 subscription."
allowed-tools: Bash, Read, Write, mcp__computer-use__*, mcp__Claude_in_Chrome__*
---

# OpenClaw + Agent37 — Computer Control Integration

Claude Code ↔ OpenClaw Gateway (:18789) ↔ Agent37 Cloud

---

## SETUP STATUS

| Component | Status | Details |
|---|---|---|
| OpenClaw CLI | ✅ v2026.4.21 | `/opt/homebrew/bin/openclaw` |
| Gateway (local) | ✅ RUNNING | `http://localhost:18789` · LaunchAgent permanent |
| Gateway (remote) | ✅ CONFIGURED | `wss://openclaw-ba7f3aivag.h86.openclaw.agent37.com/gateway` |
| Auth token | ✅ SET | `my-local-gateway-token-123` |
| WhatsApp channel | ✅ ACTIVE | `+923314721689` allowlisted |
| Telegram channel | ✅ ENABLED | Bot token configured, user `5927801109` allowlisted |
| OpenRouter model | ✅ ACTIVE | `openrouter/auto` (cheapest/best auto-selected) |
| Gemini image gen | ✅ ACTIVE | `google/gemini-3-pro-image-preview` |
| Notion skill | ✅ KEYED | API key configured |
| OpenAI image/whisper | ✅ KEYED | API key configured |

---

## QUICK COMMANDS

```bash
export PATH="/opt/homebrew/bin:$PATH"

# Health check
openclaw doctor

# Gateway status
openclaw gateway status

# Run a single agent turn
openclaw agent "your prompt here"

# Open control UI in browser
openclaw dashboard

# List agents
openclaw agents list

# Check channels
openclaw channels status

# Restart gateway
openclaw gateway restart
```

---

## INTEGRATION WITH CLAUDE CODE

Claude Code reaches the gateway via HTTP on port 18789.  
Auth header required: `Authorization: Bearer my-local-gateway-token-123`

The gateway bridges to Agent37 cloud via WebSocket — enabling remote control  
of this Mac from anywhere (WhatsApp, Telegram, or the web UI).

**Channels active:**
- WhatsApp → send messages to `+923314721689` → gateway executes
- Telegram → bot `8734176991:AAHw...` → user `5927801109`
- Web UI → `http://localhost:18789`

---

## SKILLS WATCHED (fswatch auto-reload)
- `~/.claude/skills/`
- `~/.agents/skills/`
- `~/.openclaw/workspace/skills/`

Any `.md`, `.sh`, `.py`, `.js`, `.ts`, `.json`, `.yaml` change triggers reload.
