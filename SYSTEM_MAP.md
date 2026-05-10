# System Map — Everything Connected

## Full Data Flow

```
USER TYPES A PROMPT
        │
        ▼
┌───────────────────────────────────────────────────────────────────┐
│  UserPromptSubmit Hook                                             │
│  ~/.claude/bin/skill-auto-activate                                │
│                                                                    │
│  Keyword detection table:                                          │
│  "lead" → lead-gen-ai, vibe-prospecting, airtable-sdk            │
│  "website" → website-builder, ui-ux-promax, framer-motion-builder │
│  "seo" → local-seo-30k, geo-brand-mentions, geo-content           │
│  "pdf" → reportlab-pdf-master, report-creator                     │
│  "legal" → legal-review                                           │
│  "social" → market-social                                         │
│  "proposal" → market-proposal                                     │
│  "scrape" → apify-ultimate-scraper, apify-actor-development       │
│  "ugc" → ugc-agency                                               │
│  "video" → opusclip, luma-image                                   │
│  "g0dm0d3/godmode" → g0dm0d3 (55 models via OpenRouter)          │
└───────────────────────┬───────────────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
  ┌──────────┐   ┌──────────┐   ┌──────────────┐
  │  Skills  │   │  Agents  │   │  MCP Servers │
  │  loaded  │   │ activated│   │  connected   │
  └────┬─────┘   └────┬─────┘   └──────┬───────┘
       │               │                │
       └───────────────┼────────────────┘
                       │
                       ▼
              ┌────────────────┐
              │   llm-burst    │
              │                │
              │  MODEL POOL:   │
              │  ┌───────────┐ │
              │  │ Tier 0    │ │  ← Use FIRST (free/cheap)
              │  │ • Ollama  │ │
              │  │ • Groq    │ │
              │  │ • DeepSeek│ │
              │  │ • Gemini  │ │
              │  │ • Kimi    │ │
              │  │ • OpenRtr │ │
              │  │ • Mistral │ │
              │  │ • GPT-mini│ │
              │  └───────────┘ │
              │  ┌───────────┐ │
              │  │ Tier 1    │ │  ← Last resort
              │  │ • C.Haiku │ │
              │  └───────────┘ │
              │  ┌───────────┐ │
              │  │ Tier 2    │ │  ← Final output only
              │  │ • Sonnet  │ │
              │  │ • Opus    │ │
              │  └───────────┘ │
              └────────────────┘
                       │
                       ▼
              ┌────────────────┐
              │    OUTPUT      │
              └────────────────┘
```

---

## 4 Scheduled Pipelines

```
CRON / REMOTE TRIGGER SCHEDULE
─────────────────────────────────────────────────────────────────────

7:00 AM PKT
    └──► hmz-daily-leads
         │
         ├── Source 1: Apollo MCP search (paying client signals)
         ├── Source 2: Vibe Prospecting MCP (entity enrichment)
         ├── Source 3: Apify actors (supplemental data)
         ├── Source 4: WebSearch (validation)
         │
         ├── GATE: 80+ score threshold (strict quality filter)
         │
         ├── Output: Top 10 leads only (quality > volume)
         ├── Format: Excel (.xlsx) → ~/Downloads/
         └── Delivery: Email to hmzainjamil@gmail.com

9:00 AM PKT
    └──► hmz-bdm-morning-sweep
         │
         ├── Platforms (parallel): LinkedIn, Indeed, Arc.dev,
         │   Upwork (read-only), Reddit, Contra, Toptal,
         │   Guru, Bark.com, PeoplePerHour
         │
         ├── Filter: PK-remote only, strict geo blacklist
         ├── Scoring: Algorithm applied per posting
         │
         ├── Output: Ranked opportunity report
         └── Delivery: Email digest

9:00 PM PKT
    └──► hmz-bdm-evening-sweep
         │
         ├── Same platform coverage as morning sweep
         ├── Focus: Catches US business day new postings
         ├── Extra: Reddit draft creation included
         │
         └── Delivery: Email digest

On-demand
    └──► hmz-indeed-mcp-sweep
         │
         ├── Source: Indeed MCP connector ONLY
         ├── No WebSearch, no WebFetch
         ├── Structured job search via MCP
         │
         └── Delivery: Top scored jobs → email
```

---

## Website Builder Pipeline

```
"Build a website for [client]"
        │
        ▼
Actor 1: Google Stitch MCP
  → Generates pixel-perfect design mockup from prompt
        │
        ▼
Actor 2: ui-ux-promax skill
  → Applies design system: 161 palettes, 57 font pairings, 50+ styles
        │
        ▼
Actor 3: framer-motion-builder skill
  → Adds animations: fade, scale, stagger, scroll-reveal, page transitions
        │
        ▼
Actor 4: premium-web-design skill
  → Final production code: optimized, accessible, deploy-ready
        │
        ▼
OUTPUT: Full React/Next.js site with animations
```

---

## Lead Gen Pipeline

```
"Find 50 [business type] in [city] with contact info"
        │
        ▼
lead-gen-ai skill
  │
  ├── vibe-prospecting MCP → fetch-entities (business search)
  │   └── Returns: name, address, phone, website, category
  │
  ├── Apollo MCP → email enrichment per entity
  │   └── Returns: verified email, LinkedIn, company data
  │
  ├── Apify (optional) → supplemental scraping
  │   └── Returns: Google reviews, social profiles
  │
  └── airtable-sdk → save to base (optional)

        │
        ▼
Excel export → ~/Downloads/leads-[city]-[date].xlsx
        │
        ▼
Outreach sequences → personalized cold email drafts (5-touch)
```

---

## LLM Burst Routing

```
ANY SUB-TASK (internal processing)
        │
        ▼
bin/llm-burst
        │
        ├── Check: Is Ollama running locally?
        │   YES → use Ollama (zero cost, offline)
        │   NO  → continue
        │
        ├── Check: Groq API key present?
        │   YES → route here (fastest, near-free)
        │   NO  → continue
        │
        ├── Check: DeepSeek API key present?
        │   YES → route here (best quality/cost ratio)
        │   NO  → continue
        │
        ├── Check: Gemini API key present?
        │   YES → route here (multimodal, fast)
        │   NO  → continue
        │
        ├── Check: Kimi/Moonshot API key present?
        │   YES → route here (262K context, Opus-quality)
        │   NO  → continue
        │
        ├── Fallback: OpenRouter (100+ models, best available)
        │
        └── Last resort: Claude Haiku (smallest, cheapest Claude)

NOTE: Claude Sonnet/Opus NEVER used for sub-tasks.
```

---

## Memory + Learning Loop

```
SESSION ENDS
     │
     ▼
Stop hook → session-learn
     │
     ├── Reads ~/.claude/session-queue.jsonl
     ├── Processes learnings from the session
     └── Writes to ~/.claude/projects/.../memory/MEMORY.md

MEMORY.md structure:
     ├── user_mc_profile.md           ← preferences, style
     ├── feedback_*.md                ← learned behaviors
     ├── project_*.md                 ← project contexts
     └── reference_*.md               ← domain knowledge

Next session:
     └── MEMORY.md injected via system-reminder
         → Claude remembers everything
```

---

## GitHub Auto-Sync

```
NEW SKILL CREATED or AGENT ADDED
        │
        ▼
skill-auto-activate detects "new skill" / "added agent" keyword
        │
        ▼
bin/github-sync runs in background
  ├── cd /Users/mc/claude-ai-system/
  ├── cp -r ~/.claude/skills/ skills/
  ├── cp ~/.claude/agents/*.md agents/
  ├── Strip credentials (API_KEY, SECRET, TOKEN, sk-*)
  ├── python3 scripts/rebuild-index.py
  ├── git add -A
  ├── git commit -m "sync: YYYY-MM-DD HH:MM"
  └── git push origin main
        │
        ▼
GitHub Action triggers on push
  └── auto-sync.yml: rebuilds skill/agent index
      → updated docs committed automatically
```
