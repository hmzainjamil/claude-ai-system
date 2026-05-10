# Architecture — How Everything Connects

## Core Architecture Principles

1. **Skills are loaded on demand** — never all at once. Each skill loads only its required context, tools, and agents. After task completion, it deactivates.

2. **Agents are personas, not processes** — agents define how Claude should think and respond in a domain, not a separate running process.

3. **LLM routing is hardcoded at Tier 0** — every sub-task is routed to the cheapest capable model. Claude tokens are only spent on the final synthesis layer.

4. **Automations run outside Claude** — hooks, LaunchAgents, and cron jobs wire the system together at the OS level. Claude sees only the result.

5. **Memory persists across sessions** — MEMORY.md is injected into every session, giving Claude full continuity of user preferences, project contexts, and learned behaviors.

---

## Directory Structure Deep Dive

```
~/.claude/
├── CLAUDE.md                    ← Global instructions (model routing, L99, OODA)
├── skills/                      ← 45 skill modules
│   └── <skill-name>/
│       └── SKILL.md             ← Trigger keywords + step-by-step instructions
├── skills-archive/              ← Dormant skills (not in active rotation)
├── agents/                      ← 210 specialist agent personas
├── scheduled-tasks/             ← 4 autonomous pipeline definitions
├── bin/                         ← Automation scripts
│   ├── skill-auto-activate      ← Keyword → skill mapping (every prompt)
│   ├── llm-burst                ← 15-model parallel router
│   ├── skill-on / skill-off     ← Manual skill management
│   ├── skill-search             ← Keyword skill search
│   ├── github-sync              ← Syncs to GitHub portfolio repo
│   ├── session-learn            ← Writes session learnings to memory
│   └── tier0-prompt-inject      ← Injects model routing rules
└── projects/.../memory/
    └── MEMORY.md                ← Persistent cross-session memory
```

---

## Hook Architecture

Claude Code supports hooks — shell scripts that run at defined lifecycle events:

| Hook | Event | Script | Purpose |
|---|---|---|---|
| `UserPromptSubmit` | Every prompt | `skill-auto-activate` | Load correct skills |
| `UserPromptSubmit` | Every prompt | `tier0-prompt-inject` | Enforce model routing |
| `Stop` | Session end | `session-learn` | Write learnings to memory |

This means two scripts fire on **every single prompt** before Claude processes it. The user never needs to manually load skills or think about model routing — it is handled automatically.

---

## Skill Lifecycle

```
1. DORMANT — skill is in skills-archive/ or skills/ but not loaded
   └── No context consumed, no effect on responses

2. ACTIVATED — skill SKILL.md is in active skills/ directory
   └── Claude reads it as part of system context
   └── Instructions, tools, and agents in the skill become available

3. DEACTIVATED — skill-off <name> runs after task
   └── Skill removed from active context
   └── Core skills remain: caveman, compress, launch-optimized, etc.
```

**Core skills** (always active, never deactivated):
- `caveman` — compression
- `compress` — context pruning
- `token-turbo` — Tier 0 routing enforcement
- `context-window-management` — prevents limit errors
- `compact-guard` — guards against bloat
- `skill-router` — routes new prompts
- `find-skills` — skill discovery
- `auto-learn` — memory writing
- `summarize` — output compression
- `launch-optimized` — session optimization

---

## LLM Routing Architecture

`bin/llm-burst` implements a tiered routing system:

```python
# Simplified routing logic from llm-burst

MODELS = [
    # Tier 0 — try first
    {"name": "ollama/llama3", "cost": 0, "check": lambda: ollama_running()},
    {"name": "groq/llama3", "cost": 0.0001, "key": "GROQ_API_KEY"},
    {"name": "deepseek/deepseek-v3", "cost": 0.0002, "key": "DEEPSEEK_API_KEY"},
    {"name": "gemini/flash", "cost": 0.0003, "key": "GEMINI_API_KEY"},
    {"name": "kimi/k2.6", "cost": 0.005, "key": "KIMI_API_KEY"},
    {"name": "openrouter/auto", "cost": "dynamic", "key": "OPENROUTER_API_KEY"},
    {"name": "mistral/medium", "cost": 0.003, "key": "MISTRAL_API_KEY"},
    {"name": "gpt-4o-mini", "cost": 0.0015, "key": "OPENAI_API_KEY"},
    # Tier 1 — last resort
    {"name": "claude-haiku", "cost": 0.025, "key": "ANTHROPIC_KEY"},
]

def route(prompt, mode="burst"):
    if mode == "burst":
        # Fire all available models in parallel
        results = parallel_call(MODELS, prompt)
        return judge_best(results)
    elif mode == "fast":
        # Return first successful Tier 0 result
        for model in MODELS:
            if model_available(model):
                return call(model, prompt)
```

---

## Scheduled Pipeline Architecture

Pipelines are defined as `SKILL.md` files in `scheduled-tasks/` and executed by Claude's remote trigger system via cron.

Each pipeline SKILL.md contains:
1. **Identity** — who is running this, what's the goal
2. **Data sources** — which MCP tools to call, in what order
3. **Filters** — quality gates, scoring algorithms, blacklists
4. **Output format** — Excel, email, Airtable, etc.
5. **Delivery** — where to send the result

The pipelines use MCP tools directly — no web browsing, no ambiguity. Apollo MCP, Vibe Prospecting MCP, and Indeed MCP return structured data that is scored and filtered before any output is generated.

---

## Memory Architecture

Cross-session memory is implemented via MEMORY.md:

```
~/.claude/projects/-Users-mc/memory/MEMORY.md
    └── Index pointing to individual memory files

~/.claude/projects/-Users-mc/memory/
    ├── user_mc_profile.md           ← preferences, tools, style
    ├── feedback_model_routing.md    ← learned routing preferences
    ├── feedback_reportlab_pdf_laws.md ← ReportLab hard rules
    ├── project_elementec_agency.md  ← Elementec project context
    ├── project_hmz_freelancer_params.md ← HMZ job search params
    └── reference_*.md               ← domain reference docs
```

The `session-learn` script (Stop hook) reads `~/.claude/session-queue.jsonl` — a file Claude writes to during sessions using the `auto-learn` skill — and processes it into persistent memory files after each session ends.

---

## GitHub Portfolio Sync Architecture

```
NEW SKILL/AGENT CREATED
        │
        ▼
skill-auto-activate detects trigger:
  "new skill" | "added agent" | "new workflow" | "created skill"
        │
        ▼
github-sync runs in background:
  1. cp -r ~/.claude/skills/ /Users/mc/claude-ai-system/skills/
  2. cp ~/.claude/agents/*.md /Users/mc/claude-ai-system/agents/
  3. strip_credentials() — removes API keys, tokens, secrets
  4. python3 scripts/rebuild-index.py — regenerates reference docs
  5. git add -A
  6. git commit -m "sync: YYYY-MM-DD HH:MM"
  7. git push origin main
        │
        ▼
GitHub Action (auto-sync.yml) fires on push:
  - Rebuilds skill/agent index from actual files
  - Auto-commits updated docs
  - Runs daily at 6AM UTC as well
```

This creates a fully automatic documentation pipeline: create a skill → it appears in the GitHub repo within seconds.
