# claude-ai-system
> 55-script automation OS for Claude Code — bin scripts, LaunchAgents, hooks, MAE orchestration wired end-to-end.

[![scripts](https://img.shields.io/badge/scripts-55-blue?style=flat&labelColor=555)](automations/bin/)
[![launchagents](https://img.shields.io/badge/launchagents-12-green?style=flat&labelColor=555)](launchagents/)
[![tier0](https://img.shields.io/badge/tier0-LLMs-orange?style=flat&labelColor=555)](tier0.env)
[![mae](https://img.shields.io/badge/MAE-active-purple?style=flat&labelColor=555)](automations/bin/mae)
[![license](https://img.shields.io/badge/license-MIT-lightgrey?style=flat&labelColor=555)](LICENSE)

[concepts](#concepts) · [architecture](#architecture) · [tips](#tips) · [startups](#startups) · [star](#star)

---

## 🧠 CONCEPTS <a id="concepts"></a>

| Feature | Location | Description |
|---|---|---|
| [**MAE Orchestrator**](automations/bin/mae) | `automations/bin/mae` | 4-phase multi-agent engine: decompose → swarm → cross-LLM blast → synthesis |
| [**TCC Task Queue**](automations/bin/tcc) | `automations/bin/tcc` | Python CLI task queue with parallel thread execution and retry/purge |
| [**llm-burst**](automations/bin/llm-burst) | `automations/bin/llm-burst` | Fires 11 models simultaneously, judge picks winner, Claude only for synthesis |
| [**tier0.env**](tier0.env) | `tier0.env` | All API keys: Groq, Gemini, DeepSeek, Kimi, GLM, Dashscope, Bytez, OpenRouter |
| [**auto-github-push**](automations/bin/auto-github-push) | `automations/bin/auto-github-push` | PostToolUse hook — any written file auto-uploaded to GitHub via Contents API |
| [**tcc-dashboard**](automations/bin/tcc-dashboard) | `automations/bin/tcc-dashboard` | Full system status: LLMs, queue, workflows, agents, disk/RAM |
| [**sys-optimize**](automations/bin/sys-optimize) | `automations/bin/sys-optimize` | Python cache cleaner — npm, pip, brew, Claude CLI, browser caches |
| [**session-learn**](automations/bin/session-learn) | `automations/bin/session-learn` | Stop hook — distills session learnings to persistent memory files |
| [**gap-detector**](automations/bin/gap-detector) | `automations/bin/gap-detector` | Stop hook — finds missing skills/tools after every session |
| [**skill-auto-activate**](automations/bin/skill-auto-activate) | `automations/bin/skill-auto-activate` | UserPromptSubmit hook — keyword-matches prompt and activates skills |
| [**openclaw-bridge**](automations/bin/openclaw-bridge) | `automations/bin/openclaw-bridge` | SessionStart hook — starts OpenClaw gateway on every session |
| [**smart-session-start**](automations/bin/smart-session-start) | `automations/bin/smart-session-start` | SessionStart hook — injects session context, RAM status, pending tasks |

### 🔥 Hot

| Feature | Location | Description |
|---|---|---|
| [**mae-task-intercept**](automations/bin/mae-task-intercept) | `automations/bin/mae-task-intercept` | UserPromptSubmit hook — auto-registers task prompts to TCC in background |
| [**llm-burst Bytez**](automations/bin/llm-burst) | `automations/bin/llm-burst` | Bytez.com integration — 100+ free models via OpenAI-compatible API |
| [**tier0-cache-inject**](automations/bin/tier0-cache-inject) | `automations/bin/tier0-cache-inject` | Injects prompt cache context before every Claude response |

---

## ⚙️ ARCHITECTURE <a id="architecture"></a>

```
SessionStart hooks        UserPromptSubmit hooks      Stop hooks
       │                          │                        │
  tier0-check              skill-auto-activate       session-learn
  gap-remediate            tier0-prompt-inject       gap-detector
  smart-session-start      tier0-cache-inject        mae-stop-sync
  openclaw-bridge          mae-task-intercept
  mae-session-init
       │                          │                        │
       └──────────────────────────┴────────────────────────┘
                                  │
                         TCC Task Queue (tcc)
                                  │
                    ┌─────────────┴─────────────┐
                    │     MAE Orchestrator       │
                    │  decompose → swarm → synth │
                    └─────────────┬─────────────┘
                                  │
              ┌───────────────────┼───────────────────┐
           Groq-fast           Gemini             DeepSeek
           Kimi-K2.6           GPT4o-mini         Ollama
           GLM-4.5             Bytez              OpenRouter
```

| Component | Role | Models |
|---|---|---|
| Decomposer | Breaks goal into sub-tasks | Groq llama-3.1-8b-instant |
| Swarm | 7 specialist agents in parallel | All Tier 0 models |
| Cross-LLM blast | Race 11 models | Kimi + Groq + Gemini + DeepSeek + Bytez + ... |
| Synthesizer | Merges best outputs | Groq llama-3.3-70b-versatile |

---

## 💡 TIPS AND TRICKS (18) <a id="tips"></a>

[session-hooks](#tips-hooks) · [llm-routing](#tips-llm) · [task-queue](#tips-tcc) · [cache-clean](#tips-cache) · [github-sync](#tips-gh)

<a id="tips-hooks"></a>
■ **Session Hooks (4)**

| Tip | Source |
|---|---|
| Run `chmod +x ~/.claude/bin/*` after any new script to prevent silent hook failures | [Claude Code docs](https://docs.anthropic.com/claude-code) |
| Set `"timeout": 5` on UserPromptSubmit hooks — longer ones delay Claude's first response token | [Anthropic](https://anthropic.com) |
| Hook stderr goes to Claude's output — print `[hook-name] ✓` to confirm hook ran | [hmzainjamil](https://github.com/hmzainjamil) |
| Use `run_in_background=true` equivalent: spawn detached subprocess from hook to avoid blocking | [hmzainjamil](https://github.com/hmzainjamil) |

<a id="tips-llm"></a>
■ **LLM Routing (4)**

| Tip | Source |
|---|---|
| `llm-burst --models kimi-k2.6,groq,gemini "prompt"` — 3-model race in ~2s, winner returned | [Moonshot AI](https://moonshot.cn) |
| Bytez.com free tier: `curl -H "Authorization: Bearer KEY" https://api.bytez.com/models/v2/chat` | [Bytez](https://bytez.com) |
| Groq `llama-3.1-8b-instant` for decomposition (< 0.5s), `llama-3.3-70b-versatile` for synthesis | [Groq](https://groq.com) |
| Kimi K2.6 replaces Claude Opus at 5% cost — 262K context, vision, video reasoning | [Moonshot AI](https://moonshot.cn) |

<a id="tips-tcc"></a>
■ **Task Queue (4)**

| Tip | Source |
|---|---|
| `tcc blast "t1" "t2" "t3"` fires all tasks in parallel threads — no waiting | [hmzainjamil](https://github.com/hmzainjamil) |
| `tcc retry --fire` resets failed tasks to pending and re-runs all in one command | [hmzainjamil](https://github.com/hmzainjamil) |
| `tcc purge --status failed` cleans failed queue without touching pending/active | [hmzainjamil](https://github.com/hmzainjamil) |
| `mae run "goal"` auto-decomposes, runs 7 specialist agents, synthesizes — ~8s total | [hmzainjamil](https://github.com/hmzainjamil) |

<a id="tips-cache"></a>
■ **Cache Clean (3)**

| Tip | Source |
|---|---|
| `sys-optimize --status` shows disk/RAM without touching anything | [hmzainjamil](https://github.com/hmzainjamil) |
| `sys-optimize --deep --run` adds Playwright (520MB), Electron (111MB), uv cache | [hmzainjamil](https://github.com/hmzainjamil) |
| LaunchAgent `ai.hmz.sys-optimize-daily` runs at 3am daily — no manual cleanup needed | [hmzainjamil](https://github.com/hmzainjamil) |

<a id="tips-gh"></a>
■ **GitHub Sync (3)**

| Tip | Source |
|---|---|
| Never `git push` to claude-ai-system — use Contents API only to avoid symlink conflicts | [hmzainjamil](https://github.com/hmzainjamil) |
| `auto-github-push` scrubs `ghp_*`, `sk-*`, `AIRTABLE_API_KEY` before any push | [hmzainjamil](https://github.com/hmzainjamil) |
| Re-fetch SHA before every PUT — prevents "expected SHA mismatch" on concurrent writes | [GitHub API docs](https://docs.github.com/en/rest) |

---

## ☠️ STARTUPS / BUSINESSES <a id="startups"></a>

| Feature | Replaced |
|---|---|
| **MAE multi-agent orchestration** | [Zapier AI](https://zapier.com), [Make.com](https://make.com), [n8n Cloud](https://n8n.io) |
| **llm-burst parallel blast** | [OpenRouter](https://openrouter.ai), [RouteLLM](https://github.com/lm-sys/RouteLLM) |
| **TCC task queue** | [Linear](https://linear.app), [Asana AI](https://asana.com), [ClickUp AI](https://clickup.com) |
| **sys-optimize daily cleanup** | [CleanMyMac X](https://cleanmymac.com), [DaisyDisk](https://daisydiskapp.com) |
| **auto-github-push hook** | [GitHub Actions](https://github.com/features/actions), [Netlify](https://netlify.com) |
| **Tier 0 LLM routing** | [AWS Bedrock](https://aws.amazon.com/bedrock/), [Azure AI](https://azure.microsoft.com/en-us/products/ai-services/) |

---

## Star History <a id="star"></a>

[![Star History Chart](https://api.star-history.com/svg?repos=hmzainjamil/claude-ai-system&type=Date)](https://star-history.com/#hmzainjamil/claude-ai-system&Date)
