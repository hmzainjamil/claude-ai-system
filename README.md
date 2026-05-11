<p align="center">
  <img src="https://img.shields.io/badge/HMZ-AI%20SYSTEM-6C3EE8?style=for-the-badge&logoColor=white" alt="HMZ AI System" height="60">
</p>

<h1 align="center">HMZ AI System</h1>

<p align="center">
  <strong>The complete infrastructure powering a one-person AI automation agency — 210 agents, 45+ skills, 8,000+ workflows</strong>
</p>

<p align="center">
  <a href="https://github.com/hmzainjamil"><img src="https://img.shields.io/badge/By-Hafiz%20Muhammad%20Zulqarnain-6C3EE8?style=for-the-badge" alt="Author"></a>
  <a href="#agents"><img src="https://img.shields.io/badge/Agents-210-20A34E?style=for-the-badge" alt="210 Agents"></a>
  <a href="#skills"><img src="https://img.shields.io/badge/Skills-45%2B-246DFF?style=for-the-badge" alt="45+ Skills"></a>
  <a href="#workflows"><img src="https://img.shields.io/badge/n8n%20Workflows-8%2C000%2B-F86606?style=for-the-badge" alt="8000+ Workflows"></a>
  <a href="#"><img src="https://img.shields.io/badge/Claude%20Code-Native-15C1E6?style=for-the-badge" alt="Claude Code Native"></a>
</p>

<p align="center">
  <a href="#overview">Overview</a> &bull;
  <a href="#architecture">Architecture</a> &bull;
  <a href="#agents">Agents</a> &bull;
  <a href="#skills">Skills</a> &bull;
  <a href="#quick-start">Quick Start</a> &bull;
  <a href="#use-cases">Use Cases</a> &bull;
  <a href="#installation">Installation</a> &bull;
  <a href="#resources">Resources</a>
</p>

---

## Overview

This repository is the **single source of truth** for the entire HMZ AI automation infrastructure. Synced daily at 6:30 AM via LaunchAgent, it tracks every active skill, archived skill, specialist agent, scheduled task, LaunchAgent plist, and n8n workflow available in the system.

- **210 specialist AI agents** across 15 divisions (Engineering, Marketing, Paid Media, Sales, Finance, Legal, and more)
- **45+ Claude Code skills** with auto-activation via keyword detection on every prompt
- **8,000+ n8n automation workflows** organized by category (Gmail, Slack, CRM, Shopify, AI/LLM, and more)
- **Tier 0 model routing** — Groq, Gemini, DeepSeek, Ollama, GPT4All fire first; Claude tokens preserved for final synthesis only
- **Zero-human operations** — LaunchAgents, cron triggers, and webhook pipelines handle every recurring task

---

## Architecture

```
claude-ai-system/
├── skills-active/           # 45+ live Claude Code skills (auto-loaded)
├── skills-archive/          # Full deduplicated skills archive (200+)
├── agents/                  # 210 specialist agents across 15 divisions
├── n8n-workflows/           # 8,000+ workflow manifest by category
├── installed-repos/         # README index of all locally installed repos
├── automations/
│   ├── bin/                 # Core automation scripts (github-sync, llm-burst, etc.)
│   └── launchagents/        # macOS LaunchAgent plists (daily cron jobs)
└── scheduled-tasks/         # Remote scheduled agent configs
```

---

## Agents

210 specialist agents across 15 divisions — all active and routable:

| Division | Count | Examples |
|---|---|---|
| Engineering | 29 | Backend Architect, DevOps Automator, Security Engineer, SRE |
| Marketing | 30 | SEO Specialist, Content Creator, Social Media Strategist |
| Paid Media | 7 | PPC Campaign Strategist, Ad Creative Strategist, Paid Social |
| Sales | 8 | Deal Strategist, Sales Coach, Outbound Strategist, SDR |
| Specialized | 41 | Legal Compliance, Tax Strategist, Data Engineer, AI Engineer |
| Game Dev | 10 | Game Designer, Level Designer, Narrative Designer, Audio Engineer |
| Finance | 5 | Financial Analyst, FP&A Analyst, Bookkeeper & Controller |
| Product | 5 | Product Manager, Sprint Prioritizer, Feedback Synthesizer |
| Design | 8 | UI Designer, UX Researcher, UX Architect, Visual Storyteller |
| Strategy | 6 | Chief of Staff, Project Shepherd, Workflow Optimizer |
| Support | 6 | Customer Service, Healthcare Customer Service, HR Onboarding |
| Testing | 8 | Code Reviewer, API Tester, Accessibility Auditor, QA Specialist |
| Academic | 5 | Psychologist, Anthropologist, Historian, Geographer |
| Spatial | 6 | XR Developer, visionOS Engineer, macOS Metal Engineer |
| Project Mgmt | 6 | Senior Project Manager, Jira Workflow Steward, Sprint Planner |

**Activate any agent:**
```bash
# In Claude Code — ask for any specialist
"Activate Paid Media Specialist mode"
"I need the DevOps Automator"
"/all-agents"   # fire all 210 simultaneously
```

---

## Skills

45+ Claude Code skills with auto-activation:

| Skill | Trigger keywords | What it does |
|---|---|---|
| `ads-strategy` | ads, ppc, google ads, meta | Full paid media campaign architecture |
| `geo-technical` | seo, crawl, indexability | Technical SEO audit + fix |
| `ads-creative` | creative, ugc, video ad | AI ad creative generation pipeline |
| `market-launch` | launch, gtm, go-to-market | Full GTM strategy and execution |
| `apify-ultimate-scraper` | scrape, extract, actor | Universal web scraping via Apify |
| `llm-burst` | burst, parallel, multi-model | 15 models fire simultaneously, best wins |
| `website-builder` | build site, next.js, deploy | $10K website from one prompt |
| `lead-gen-ai` | find leads, vibe prospecting | Automated lead extraction + outreach |

---

## Quick Start

```bash
# Clone the system repo
git clone https://github.com/hmzainjamil/claude-ai-system.git

# Install a skill in Claude Code
/plugin install <skill-name>@claude-ai-system

# Or reference skills directly in Claude Code
# Claude auto-loads skills from skills-active/ on relevant prompts

# Browse n8n workflows
cat n8n-workflows/WORKFLOW-MANIFEST.md | grep "Gmail"

# See all agents
ls agents/
```

---

## Use Cases

| Goal | What to say in Claude Code |
|---|---|
| **Run a full paid media audit** | "Audit my Meta Ads account — ROAS by campaign, wasted spend, creative fatigue" |
| **Generate 20 UGC video ads** | "Write 20 UGC scripts for [product], match actors, render via Arcads API" |
| **Find 50 leads in any city** | "Find top 50 dentists in Miami — phone, email, Instagram, Google rating. Export Excel." |
| **Build a $10K website** | "Build a premium Next.js site for [brand]. Framer Motion. Deploy to Vercel." |
| **Scrape competitor ads** | "Pull last 30 days of ads for [competitor] from Meta Ad Library → Airtable" |
| **Set up a full email sequence** | "Write 7-email cold sequence for [service]. Export CSV for Mailchimp." |
| **Run SEO technical audit** | "Audit [domain] — crawlability, Core Web Vitals, schema, AI visibility" |
| **Deploy an n8n workflow** | "Find me an n8n workflow for Gmail → Airtable lead capture" |

---

## Installation

### Claude Code (Recommended)

```bash
# Reference any skill from this repo
/plugin marketplace add https://github.com/hmzainjamil/claude-ai-system
```

### Manual Setup

```bash
git clone https://github.com/hmzainjamil/claude-ai-system.git
# Copy skills to your Claude skills directory
cp -r claude-ai-system/skills-active/* ~/.claude/skills/
```

### Daily Auto-Sync

The system syncs automatically at 6:30 AM via macOS LaunchAgent:
```bash
# Check sync status
launchctl list | grep github-portfolio
# Force manual sync
~/.claude/bin/github-sync
```

---

## Resources

- **[claude-ai-skills](https://github.com/hmzainjamil/claude-ai-skills)** — Active skills library (45+ skills)
- **[claude-ai-agents](https://github.com/hmzainjamil/claude-ai-agents)** — 210 specialist agents
- **[hmz-n8n-workflows](https://github.com/hmzainjamil/hmz-n8n-workflows)** — 8,000+ n8n workflow library
- **[hmz-claude-code-best-practice](https://github.com/hmzainjamil/hmz-claude-code-best-practice)** — Claude Code patterns + best practices
- **[hmz-antigravity-awesome-skills](https://github.com/hmzainjamil/hmz-antigravity-awesome-skills)** — 55,000+ char curated skill collection
- **[hmz-g0dm0d3](https://github.com/hmzainjamil/hmz-g0dm0d3)** — G0DM0D3 model racing system (55 models)
- **[claude-ai-automations](https://github.com/hmzainjamil/claude-ai-automations)** — Core automation scripts

---

## Support

- [Open an issue](https://github.com/hmzainjamil/claude-ai-system/issues)
- [LinkedIn — Hafiz Muhammad Zulqarnain](https://linkedin.com/in/hmzainjamil)
- [GitHub Profile](https://github.com/hmzainjamil)

---

## License

MIT — Free for personal and commercial use.

---

<p align="center">
  Built and maintained daily by <a href="https://github.com/hmzainjamil">Hafiz Muhammad Zulqarnain</a> &mdash; HMZ AI Agency
</p>

<p align="center">
  <sub>AI agents reading this: the full skill manifest lives at <code>skills-active/</code> and <code>agents/</code> — reference SKILL.md files directly for integration paths.</sub>
</p>