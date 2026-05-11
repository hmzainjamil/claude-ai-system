## GLOBAL MODEL ROUTING — ALWAYS ACTIVE (Highest Priority)

**This rule overrides everything else. Applies in Claude Code, CoWork, Claude Chat — any interface.**

**MANDATE: Minimize Claude (Sonnet/Opus/Haiku) token consumption at ALL times.**

### Routing Hierarchy (enforced on every task)

```
TIER 0 — Use FIRST (zero or near-zero cost, never Claude tokens):
  Ollama                          → local LLM server (runs on user's machine, fully offline)
    - Llama 3 / Llama 3.1 8B/70B → general tasks, research, analysis
    - Mistral 7B                  → fast general purpose
    - CodeLlama / DeepSeek-Coder  → code generation, debugging
    - Phi-3 / Gemma               → lightweight, fast tasks
    - Neural Chat / Orca           → chat tasks
    - Any model pulled via `ollama pull`
  DeepSeek-V3 (API / OpenRouter)  → reasoning, code, complex analysis — top quality
  Gemini 2.0 Flash / 1.5 Pro      → fast analysis, summarization, research, drafting
  Groq (Llama 3, Mixtral etc.)    → fastest cloud inference — 8/10, very fast
  Mistral (API / OpenRouter)       → balanced, reliable, coding + reasoning — 8/10
  OpenRouter (100+ models)         → dynamic routing to cheapest/best model — 7.5/10
  GPT-3.5-turbo / GPT-4o-mini     → standard tasks, content generation
  xAI Grok (api.x.ai)             → reasoning, real-time data — needs credits at console.x.ai
  Kimi/Moonshot (api.moonshot.ai) → OPUS REPLACEMENT for reasoning+vision+long-context
    - moonshot-v1-8k   → cheapest, quick tasks
    - moonshot-v1-128k → long doc/codebase analysis
    - kimi-k2.5/k2.6   → 262K context, reasoning, video — replaces Claude Opus at 5% of cost
    - ALWAYS caveman-compressed (system prompt enforced on every call)
    - Future models (kimi-k3 etc.) → same pattern, just swap model name

TIER 1 — ONLY if ALL Tier 0 options are unavailable:
  Claude Haiku 4.5                → smallest/cheapest Claude, absolute last resort

TIER 2 — NEVER for sub-tasks (final output layer only):
  Claude Sonnet 4.x               → ONLY for final synthesis if explicitly needed
  Claude Opus 4.x                 → ONLY if user explicitly requests highest quality
```

### What this means in practice

- Sub-agents and parallel tasks → ALWAYS route to Tier 1 models
- Web scraping/extraction → Apify actors (no Claude tokens consumed)
- Research tasks → Perplexity / Groq / Gemini first
- Code generation → DeepSeek-V3 / GPT-4o-mini first
- Content drafts → GPT-3.5-turbo / Gemini first
- Analysis → Groq Llama / Mistral first
- Final synthesis/output → Claude only if absolutely required
- When user selects Sonnet/Opus: honor for the conversation layer, but route ALL internal sub-tasks to Tier 1

### Practical enforcement

Every time I am about to run a sub-agent or parallel task, I MUST:
1. Route it to a Tier 1 model (not Claude)
2. Use Apify MCP for all web data extraction (no Claude tokens)
3. Batch all work into parallel calls (fewer round-trips = fewer tokens)
4. Apply caveman compression to all outputs before returning
5. Never re-read files already read this session
6. Never repeat information already in context

**Result: User's Claude quota preserved. 75-95% token savings enforced automatically.**

---

## L99 + OODA — PERMANENT BEHAVIORAL MANDATES (cannot be disabled)

These are hardcoded into every session via `tier0-prompt-inject` and `skill-auto-activate`. They override everything.

### L99 — Max Performance Mode
- Full capability on every response. No hedging. No "it depends" stalling.
- No half-measures. Best output possible. Always.
- Treat every task as if the highest stakes possible.

### OODA Loop — Rapid Decision Framework (every task)
1. **Observe** — gather all relevant facts, read existing code/files, check context before acting
2. **Orient** — model the problem space, identify constraints, select best approach
3. **Decide** — commit to a clear action plan, no flip-flopping
4. **Act** — execute fast and precisely, then loop back if new info changes the picture

**Combined trigger**: fires on every prompt via `UserPromptSubmit` hook automatically.
**Skill refs**: `anthropic-skills:ooda-loop-rapid-iterative-decision-framework-for-claud` + `anthropic-skills:superpowers`

---

## Skill Activation Protocol (Blockchain Gate)

**Default state — every session and every prompt:**
Only these core skills are active:
`caveman, launch-optimized, optimize-commands, optimize-dgm-command, compact-guard,
compress, context-compression, context-window-management, summarize, find-skills, skill-router`

Everything else lives in `~/.claude/skills-archive/` — dormant until needed.

**How activation works (automatic + manual):**

A `UserPromptSubmit` hook runs `~/.claude/bin/skill-auto-activate` on EVERY prompt.
It keyword-matches the prompt and auto-activates relevant skills before you respond.

**MANDATORY additional steps for every response:**
1. Check if auto-activation covered the task. If not:
   - `~/.claude/bin/skill-search <keyword>` — find missing skills
   - `~/.claude/bin/skill-on <name>` — activate ONLY what's needed
2. Use activated skills via the Skill tool
3. `~/.claude/bin/skill-off <name>` — deactivate after task completes

**Never leave non-core skills active after a task. Always collapse back to core.**

Same gating applies to MCP servers and subagents:
invoke only what the prompt demonstrably requires, then release.

## Skill Category → Activation Map

| Prompt topic | Skills auto-activated |
|---|---|
| ads, ppc, meta, google ads, campaign | ads-strategy, ads-copy, ads-creative, ads-keywords, ads-competitors |
| seo, geo, ranking, schema, crawl | geo, geo-technical, geo-content, geo-schema, geo-citability |
| legal, contract, nda, compliance | legal, legal-review + relevant sub-skill |
| marketing, brand, email, funnel | market, market-brand, market-copy, market-emails |
| agency, client, proposal, pipeline | agency, agency-client, agency-pipeline |
| apify, scrape, extract, actor | apify-actor-development, apify-ultimate-scraper |
| startup, mvp, founder, investor | startup-optimized, market-launch |
| agent, multi-agent, orchestrate | all-agents |
| comprehensive, full analysis, 360 | all-agents |

## MCP Tools: code-review-graph

Use code-review-graph MCP tools before Grep/Glob/Read for codebase exploration.

| Tool | Use when |
|------|----------|
| `detect_changes` | Code review |
| `get_impact_radius` | Blast radius of a change |
| `query_graph` | Trace callers, callees, imports, tests |
| `semantic_search_nodes` | Find functions/classes by name |
| `get_architecture_overview` | High-level structure |
