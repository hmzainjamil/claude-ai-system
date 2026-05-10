# Claude AI System — The Most Advanced Claude Code Automation Stack

> **Built by a power user. Runs 24/7. Handles everything from lead gen to $10K website builds — autonomously.**

---

![Skills](https://img.shields.io/badge/Skills-45-blue?style=for-the-badge)
![Agents](https://img.shields.io/badge/Agents-210-purple?style=for-the-badge)
![Pipelines](https://img.shields.io/badge/Scheduled_Pipelines-4-green?style=for-the-badge)
![Models](https://img.shields.io/badge/AI_Models-15-orange?style=for-the-badge)
![Token_Savings](https://img.shields.io/badge/Token_Savings-75--95%25-red?style=for-the-badge)
![n8n](https://img.shields.io/badge/n8n_Workflows-8159-yellow?style=for-the-badge)

---

## What Is This?

This is a fully operational AI automation operating system built on top of Claude Code. It is not a demo, a template, or a proof-of-concept. It runs live, every day, handling lead generation, business development, website building, content creation, legal review, and more — with minimal human intervention.

The system combines 45 skill modules, 210 specialist AI agents, 4 autonomous scheduled pipelines, and a 15-model LLM routing layer that keeps Claude token costs 75-95% lower than a naive implementation. Every component is wired together: skills auto-activate from keywords, agents load on demand, pipelines run on cron, and a GitHub Action keeps this documentation in sync automatically.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                         USER PROMPT                                  │
└─────────────────────────────┬───────────────────────────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │  skill-auto-activate │  ← keyword detection
                    │  (UserPromptSubmit   │    fires on EVERY prompt
                    │   hook)              │
                    └──────────┬──────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
   ┌──────▼──────┐    ┌───────▼───────┐   ┌───────▼───────┐
   │   Skills    │    │    Agents     │   │  MCP Servers  │
   │  (45 loaded)│    │ (210 avail.)  │   │  (15+ tools)  │
   └──────┬──────┘    └───────┬───────┘   └───────┬───────┘
          │                    │                    │
          └────────────────────┼────────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │     llm-burst        │
                    │  (15-model router)   │
                    │                      │
                    │  Tier 0 (free first):│
                    │  • Ollama (local)    │
                    │  • Groq              │
                    │  • DeepSeek V3       │
                    │  • Gemini Flash      │
                    │  • Kimi K2.6         │
                    │  • OpenRouter        │
                    │  • Mistral           │
                    │                      │
                    │  Tier 1 (last resort)│
                    │  • Claude Haiku      │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │      OUTPUT          │
                    │  • Emails drafted    │
                    │  • Files written     │
                    │  • Leads exported    │
                    │  • Sites built       │
                    └─────────────────────┘

SCHEDULED PIPELINES (run autonomously):
┌────────────────────────────────────────────────────────┐
│  7:00 AM PKT  → hmz-daily-leads       (10 elite leads) │
│  9:00 AM PKT  → hmz-bdm-morning-sweep (job intel)      │
│  9:00 PM PKT  → hmz-bdm-evening-sweep (job intel)      │
│  On-demand    → hmz-indeed-mcp-sweep  (Indeed only)    │
└────────────────────────────────────────────────────────┘
```

---

## Key Capabilities

### 1. Multi-LLM Burst — 15 Models Fire in Parallel
**Script:** `bin/llm-burst`

Sends every sub-task to 15 AI models simultaneously. A judge model picks the best response. This gives GPT-4o quality at Groq prices, with zero Claude token burn for internal tasks.

```bash
llm-burst "Write 5 cold email subject lines for a PPC agency"
# → Fires Groq, DeepSeek, Gemini, Kimi, Mistral simultaneously
# → Judge picks winner
# → Returns best output in <3 seconds
```

### 2. Skill Auto-Activation — Zero-Config Keyword Routing
**Script:** `automations/skill-auto-activate`

A `UserPromptSubmit` hook intercepts every prompt before Claude sees it. It keyword-matches against 45 skill triggers and loads only the relevant skills. No manual `/skill-on` needed.

```
"find dental clinic leads in Austin"
  → loads: lead-gen-ai, vibe-prospecting, airtable-sdk
  → activates: Apollo MCP, Vibe Prospecting MCP
  → returns: Excel with phone + email + enrichment
```

### 3. Daily Lead Gen Sweeps — 4 Autonomous Pipelines
**Folder:** `workflows/`

Four scheduled pipelines run on cron via Claude's remote trigger system:

| Pipeline | Time | What It Does |
|---|---|---|
| `hmz-daily-leads` | 7:00 AM PKT | Hunts 10 deeply-qualified client leads — Apollo + Vibe + enrichment → Excel → email |
| `hmz-bdm-morning-sweep` | 9:00 AM PKT | 10-platform job intelligence sweep → scored report → email |
| `hmz-bdm-evening-sweep` | 9:00 PM PKT | Same as morning but catches US business day postings |
| `hmz-indeed-mcp-sweep` | On-demand | Dedicated Indeed MCP pipeline with strict scoring filters |

### 4. Website Builder — $10K Sites From One Prompt
**Skill:** `skills/website-builder/`

A 4-actor pipeline that goes from a one-line prompt to a production-grade website:

```
Actor 1: Google Stitch MCP      → pixel-perfect mockup
Actor 2: ui-ux-promax skill     → 161 palettes, 57 font pairings
Actor 3: Framer Motion builder  → scroll-reveal, page transitions
Actor 4: Premium Web Design     → final production code
```

### 5. Lead Gen AI — Any Niche, Any City
**Skill:** `skills/lead-gen-ai/`

```
"Find 50 roofing contractors in Denver with email and phone"
→ Vibe Prospecting MCP: entity search
→ Apollo MCP: email enrichment
→ Excel export: formatted spreadsheet
→ Outreach sequences: personalized cold email drafts
```

### 6. Token Optimizer — 75-95% Claude Savings
**Skills:** `skills/token-turbo/`, `skills/caveman/`, `skills/compress/`

Three-layer token reduction:
- **Tier 0 routing**: Sub-tasks go to Groq/DeepSeek/Gemini — never Claude
- **caveman compression**: All outputs compressed before returning
- **context-window-management**: Prunes context before it hits limits

### 7. 210 Specialist Agents — Full Agency Coverage
**Folder:** `agents/`

210 agents organized into divisions:

| Division | Count | Examples |
|---|---|---|
| Engineering | 25+ | backend-architect, devops-automator, security-engineer |
| Marketing | 20+ | douyin-strategist, video-optimization, email-intelligence |
| Sales | 10+ | outbound-strategist, deal-strategist, pipeline-analyst |
| Design | 8 | ui-designer, ux-architect, visual-storyteller |
| Finance | 5 | financial-analyst, tax-strategist, bookkeeper-controller |
| GEO/SEO | 5 | ai-visibility, geo-content, geo-schema |
| Specialized | 10+ | salesforce-architect, mcp-builder, workflow-architect |

### 8. Kimi K2.6 as Opus Replacement
**Configured in:** `bin/llm-burst`

Kimi K2.6 (Moonshot AI) delivers Claude Opus-level reasoning at 5% of the cost. 262K context window. Used for all long-document analysis and complex reasoning tasks that would otherwise burn Opus tokens.

---

## All 45 Skills

| Skill | Description | Triggers |
|---|---|---|
| `lead-gen-ai` | Automated lead extraction — Vibe + Apollo + Excel + outreach | find leads, lead gen, extract leads |
| `website-builder` | $10K site from one prompt — 4-actor pipeline | build website, create website |
| `premium-web-design` | AI design workflow — Stitch mockup → production code | premium website, web design workflow |
| `vibe-prospecting` | Vibe Prospecting MCP — fetch-entities, enrich, export | vibe prospecting, business search |
| `all-agents` | Orchestrates all 210 specialist agents simultaneously | comprehensive, 360, full analysis |
| `llm-burst` | 15 models fire in parallel, judge picks winner | burst, multi-model, race models |
| `token-turbo` | Token reduction enforcement — max compression, Tier 0 routing | (always-on) |
| `caveman` | Maximum output compression — removes all filler | (always-on) |
| `compress` | Context compression — prunes redundant content | (always-on) |
| `context-compression` | Context window management — prevents limit errors | (always-on) |
| `context-window-management` | Smart context pruning strategy | (always-on) |
| `skill-router` | Routes prompts to correct skill automatically | (always-on) |
| `find-skills` | Search and discover skills by keyword | find skill, which skill |
| `compact-guard` | Guards against context explosion | (always-on) |
| `summarize` | Compress long outputs into dense summaries | summarize, tldr |
| `optimize-commands` | Optimize Claude Code command execution | optimize command |
| `optimize-dgm-command` | DGM command optimizer | dgm, optimize dgm |
| `launch-optimized` | Launch sequence optimizer for new sessions | (session-start) |
| `prompt-shortcuts` | Shorthand command expansion system | /ps, shortcuts |
| `ui-ux-promax` | 50+ design styles, 161 palettes, 57 font pairings | ui, ux, design system |
| `ui-ux-pro-max` | Extended UI/UX design system | ui/ux, design |
| `framer-motion-builder` | Framer Motion animations — fade, scroll-reveal, transitions | framer motion, animations |
| `geo-brand-mentions` | AI citation tracking — ChatGPT, Perplexity, Gemini, Claude | brand mentions, geo mentions, ai citations |
| `local-seo-30k` | 22-prompt Local SEO workflow — GBP, reviews, citations | seo audit, local seo |
| `apify-actor-development` | Build and deploy Apify scraping actors | apify actor, build actor |
| `apify-actorization` | Convert any scraper to an Apify actor | actorize, apify convert |
| `apify-ultimate-scraper` | Universal web scraper via Apify | scrape, extract, web scraping |
| `apify-generate-output-schema` | Generate Apify actor output schemas | apify schema, output schema |
| `reportlab-pdf-master` | Branded 11-page audit PDFs via ReportLab | pdf report, audit pdf, create pdf |
| `report-creator` | Multi-format report generator — PDF, DOCX, Excel | create report, generate report |
| `legal-review` | Contract and agreement checker | legal review, contract review, nda |
| `market-proposal` | Client proposal generator — 7-section structure | market proposal, client proposal |
| `market-social` | Social media marketing — LinkedIn, Instagram, Twitter | social media, instagram, linkedin post |
| `client-hunting` | Multi-platform lead gen — Arc.dev, Indeed, LinkedIn | find clients, client hunting |
| `outcome-pricing` | Performance-based fee structures — % of spend, revenue share | outcome pricing, performance pricing |
| `service-productizer` | Package services into tiered products | productize, service package, pricing tiers |
| `sub-brand-generator` | Niche brand creation — identity, naming, positioning | sub brand, niche brand, create brand |
| `airtable-sdk` | Full Airtable integration — read/write/sync | airtable, airtable base |
| `g0dm0d3` | 55-model ultra racing via OpenRouter | g0dm0d3, godmode, race all models |
| `luma-image` | Luma AI image and video generation | luma, dream machine, luma video |
| `opusclip` | AI video clipping — long video → 10-30 viral clips | opusclip, clip video, repurpose video |
| `ugc-agency` | Arcads AI actor pipeline for UGC ads | ugc ads, ugc agency, arcads, ai actors |
| `modernization-audit` | Legacy system analysis and modernization roadmap | modernization audit, legacy system |
| `auto-learn` | Automatic memory writing — learnings → memory files | (always-on) |
| `customer-matrix` | Customer segmentation and matrix analysis | customer matrix, segmentation |

---

## Scheduled Workflows

```
┌─────────────────────────────────────────────────────────────────┐
│  DAILY AUTONOMOUS PIPELINE TIMELINE                             │
│                                                                  │
│  7:00 AM ──► hmz-daily-leads                                    │
│              • Apollo MCP: search paying clients                │
│              • Vibe Prospecting: entity enrichment              │
│              • Apify: additional data extraction                │
│              • 80+ score threshold (quality gate)               │
│              • Excel export + email delivery                    │
│                                                                  │
│  9:00 AM ──► hmz-bdm-morning-sweep                              │
│              • 10 platforms searched in parallel                │
│              • Strict PK-remote filter                          │
│              • Scoring algorithm applied                        │
│              • Ranked report → email                            │
│                                                                  │
│  9:00 PM ──► hmz-bdm-evening-sweep                              │
│              • Same as morning                                  │
│              • Catches US business day postings                 │
│              • Reddit draft creation included                   │
│                                                                  │
│  On-demand ► hmz-indeed-mcp-sweep                               │
│              • Indeed MCP connector only                        │
│              • Structured job search                            │
│              • Top scored jobs → email                          │
└─────────────────────────────────────────────────────────────────┘
```

---

## Automations

### LaunchAgents + Hooks
- `UserPromptSubmit` hook → `skill-auto-activate` fires on every prompt
- `Stop` hook → `session-learn` writes session learnings to memory
- `skill-guardian` → watches for zombie skills and deactivates them
- `skill-watcher` → monitors skill file changes

### Key Automation Scripts
| Script | Role |
|---|---|
| `automations/skill-auto-activate` | Keyword → skill mapping on every prompt |
| `automations/website-builder-setup` | Sets up website builder environment |
| `automations/hmz-bdm-state-update` | Updates BDM pipeline state |
| `automations/hmz-bdm-catchup` | Catches up missed sweep cycles |
| `bin/llm-burst` | 15-model parallel LLM router |
| `bin/skill-on` | Activate a skill |
| `bin/skill-off` | Deactivate a skill |
| `bin/skill-search` | Find skills by keyword |

---

## Quick Start

### Example 1: Generate Leads
```bash
# Just type in Claude Code:
"Find 50 dental clinics in Austin TX with owner email and phone"
# → skill-auto-activate loads lead-gen-ai + vibe-prospecting
# → Returns Excel file to ~/Downloads/
```

### Example 2: Build a Website
```bash
"Build a premium website for a SaaS startup — dark theme, animations"
# → loads website-builder, ui-ux-promax, framer-motion-builder
# → 4-actor pipeline fires
# → Production React code with Framer Motion animations
```

### Example 3: Run Multi-Model Burst
```bash
llm-burst "What's the best cold email subject line for a PPC agency targeting ecom brands?"
# → 15 models respond in parallel
# → Judge model picks best
# → Result in <3 seconds, zero Claude tokens burned
```

---

## Tech Stack

![Claude Code](https://img.shields.io/badge/Claude_Code-Anthropic-orange?style=flat-square)
![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-Lightning_Fast-red?style=flat-square)
![DeepSeek](https://img.shields.io/badge/DeepSeek-V3-blue?style=flat-square)
![Gemini](https://img.shields.io/badge/Gemini-2.0_Flash-4285F4?style=flat-square)
![Kimi](https://img.shields.io/badge/Kimi-K2.6_262K-purple?style=flat-square)
![OpenRouter](https://img.shields.io/badge/OpenRouter-100+_Models-green?style=flat-square)
![Apify](https://img.shields.io/badge/Apify-Web_Scraping-yellow?style=flat-square)
![Apollo](https://img.shields.io/badge/Apollo-Lead_Enrichment-blue?style=flat-square)
![Airtable](https://img.shields.io/badge/Airtable-Data_Storage-teal?style=flat-square)
![n8n](https://img.shields.io/badge/n8n-8159_Workflows-orange?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square)
![Bash](https://img.shields.io/badge/Bash-Automation-green?style=flat-square)

---

## Repository Structure

```
claude-ai-system/
├── README.md                    ← This file
├── SYSTEM_MAP.md                ← Visual connection map
├── skills/                      ← 45 SKILL.md modules
├── agents/                      ← 210 specialist agents
├── workflows/                   ← 4 scheduled pipelines
├── automations/                 ← Hook scripts + LaunchAgents
├── bin/                         ← Core automation scripts
├── docs/
│   ├── architecture.md          ← System architecture deep-dive
│   ├── getting-started.md       ← Setup guide
│   ├── skills-reference.md      ← All 45 skills indexed
│   ├── agents-reference.md      ← All 210 agents indexed
│   └── terminology.md           ← Definitions
├── scripts/
│   └── rebuild-index.py         ← Auto-rebuilds docs from source
└── .github/
    └── workflows/
        └── auto-sync.yml        ← Daily doc auto-sync Action
```

---

*Built with Claude Code. Runs on macOS. Zero maintenance required.*
