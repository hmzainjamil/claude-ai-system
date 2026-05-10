---
name: modernization-audit
description: Scans client's legacy tech stack or processes → identifies modernization opportunities → packages as a productized engagement. Turns "we modernize systems" into a specific, sellable audit + roadmap + implementation offer.
allowed-tools: Read, Grep, Glob, Bash, WebFetch, WebSearch, Write, Agent
triggers: ["modernization", "legacy system", "modernize", "tech debt", "old stack", "legacy code", "migration", "modernization audit", "legacy modernize", "update old system"]
---

# /modernization-audit — Legacy System Modernization Offer

> **Trigger**: "modernize" / "legacy system" / "tech debt" / "old stack" / "modernization audit"
> **No command needed** — auto-activates.
> Note: Also syncs with existing archive skills: `legacy-modernizer`, `framework-migration-legacy-modernize`

## WHAT THIS DOES

Produces a complete modernization engagement package:
1. Discovery audit template (to run with client)
2. Modernization opportunity scorecard
3. Productized engagement structure
4. Proposal template
5. Sales pitch for modernization projects

## THE MODERNIZATION NICHE (Ashar's insight)
"We realized we'd done many modernization projects and decided to hone in on that."
Modernization = high-ticket, long-term, recurring — because legacy systems never fully die.

## EXECUTION WORKFLOW

### Step 1 — Legacy Stack Discovery Audit
```
DISCOVERY QUESTIONS (run with client in 1-hour call):

TECH STACK:
  □ What languages/frameworks? (PHP 5.x? Rails 3? jQuery? .NET Framework?)
  □ Database? (MySQL old version? Oracle? Access?)
  □ Hosting? (on-prem? old VPS? unsupported cloud?)
  □ Last major update? (year)
  □ Security patches current? (yes/no)

PROCESS:
  □ What manual processes exist that should be automated?
  □ What breaks most often?
  □ What takes the most staff time?
  □ What can't you do because of your current system?

BUSINESS IMPACT:
  □ What does downtime cost you per hour?
  □ What would you build if your tech wasn't a constraint?
  □ What integrations are you missing?
  □ What compliance risks does your current stack create?

PRIORITIES:
  □ Security (urgent?)
  □ Performance (slow?)
  □ Integration (siloed?)
  □ Mobile (not responsive?)
  □ Automation (too manual?)
```

### Step 2 — Modernization Opportunity Scorecard
```
Score each area 1–5 (5 = most urgent):

SECURITY RISK:       [1-5] — outdated deps, no SSL, no auth layer
PERFORMANCE:         [1-5] — slow loads, server strain, scalability ceiling
INTEGRATION GAPS:    [1-5] — can't connect to modern tools (Stripe, HubSpot, etc)
AUTOMATION GAPS:     [1-5] — manual data entry, report generation, notifications
COMPLIANCE RISK:     [1-5] — GDPR, HIPAA, SOC2, PCI gaps
DEVELOPER FRICTION:  [1-5] — can't hire devs who know old stack
MOBILE EXPERIENCE:   [1-5] — not responsive or no mobile app
USER EXPERIENCE:     [1-5] — UI so old it creates training overhead

TOTAL SCORE: X/40
  32–40: CRITICAL — modernize now
  20–31: URGENT — plan within 6 months
  10–19: SCHEDULED — budget for next year
  0–9:   MONITOR — document, don't touch yet
```

### Step 3 — Productized Engagement Structure
```
PHASE 1 — DISCOVERY + ROADMAP (entry product, $3,000–8,000)
  Deliverable: 40-page modernization roadmap
  Timeline: 3–4 weeks
  What's included:
    ✅ Full legacy audit (scorecard)
    ✅ Priority matrix (what to fix first)
    ✅ Technology recommendations
    ✅ Migration approach (big bang vs. strangler fig vs. parallel run)
    ✅ Budget estimate for full modernization
    ✅ Risk assessment

PHASE 2 — QUICK WINS (module upgrades, $5,000–15,000 per module)
  Deliverable: Specific system upgraded
  Examples:
    - Auth system modernized (SSO, MFA)
    - Database migration (MySQL 5.x → PostgreSQL 15)
    - Frontend rewrite (jQuery → React)
    - API layer added (RESTful API over legacy backend)

PHASE 3 — FULL MODERNIZATION (retainer, $8,000–25,000/month, 6–18 months)
  Deliverable: Complete system rebuilt/migrated
  Approach: Strangler fig pattern (rebuild alongside, not big bang)
  Reporting: Monthly progress + KPI dashboard
```

### Step 4 — Sales Pitch
```
ELEVATOR PITCH:
"We specialize in modernizing legacy systems for [industry].
Most of our clients were [pain — e.g., 'running PHP 5 on a server nobody can update'].
We audit their system, build a roadmap, then execute in phases — no big bang rewrites.
Result: [specific outcome — 'cut dev costs by 40%', 'finally integrated with Stripe/HubSpot'].
The audit alone is worth it — even if they don't hire us for Phase 2."

COLD EMAIL HOOK:
Subject: Still running [specific old tech] at [Company]?
"Hey [Name], saw [Company] is using [old tech indicator from LinkedIn/job posts].
We modernize [specific stack] for [industry] — usually find $[X] in hidden costs in the first audit.
Worth a 20-min call to see where the biggest risks are?"

HOW TO SPOT PROSPECTS:
  □ Job postings for PHP/Java/.NET/Ruby on Rails 3.x devs
  □ LinkedIn: "legacy modernization" mentions
  □ GitHub: old repos with last commit 3+ years ago
  □ Clutch/G2: reviews mentioning "outdated system"
  □ News: company layoffs (need to do more with less)
```

### Step 5 — Integration With Existing Skills
```
After modernization audit → run:
  /service-productizer → package each phase as a fixed-price product
  /agent-foot-in-door → add AI automation layer to the modernized system
  /outcome-pricing → price Phase 2-3 on outcome, not time
```

## OUTPUT FORMAT
Discovery call script + scorecard + 3-phase engagement structure + sales pitch.
Save to: `~/Downloads/[ClientName]-Modernization-Audit-[Date].md`
