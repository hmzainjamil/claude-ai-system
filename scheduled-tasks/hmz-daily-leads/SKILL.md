---
name: hmz-daily-leads
description: HMZ Elite Lead Pipeline — deep-qualified potential clients only, 80+ score threshold, Apollo + Vibe + Apify + WebSearch + enrichment → top 10 leads → Excel → email
---

## HMZ ELITE DAILY LEAD PIPELINE — 7 AM PKT

You are hunting high-quality potential clients for Zulqarnain (HMZ), a Pakistani paid ads specialist. The goal is NOT volume — it's 10 deeply qualified, high-potential leads where Zulqarnain has a genuine chance of winning the work. Quality over quantity. Every lead must pass all gates before scoring.

---

### WHO IS ZULQARNAIN (know this to qualify leads correctly)

- Pakistani freelancer, remote-only from Pakistan
- Specializes: Google Ads · Meta/Facebook Ads · DTC ecom · Lead Gen campaigns
- Proven results: 3-10x ROAS, CPL reduction, scaling ad accounts
- Target clients: businesses actively spending on ads but getting bad results OR businesses about to launch paid ads
- Ideal budget: $5k–$100k/mo ad spend under management
- Cannot do: physical meetings · visa-restricted contracts · US-only 1099

---

### LEAD QUALIFICATION GATES (ALL must pass — fail any = discard)

**GATE 1 — Business is real and active**
- Has website, social presence, is trading
- Not a job board posting, not an agency looking for whitelabel

**GATE 2 — They spend money on ads (or clearly need to)**
- Running Google/Meta ads (visible via ad library, WebSearch signals)
- OR e-commerce brand with products clearly needing paid traffic
- OR SaaS/service business with budget but no PPC expertise visible

**GATE 3 — They have a problem Zulqarnain solves**
- Running ads but with obvious inefficiencies (bad landing pages, generic copy, no ROAS data shown)
- OR growing fast and need to scale paid channels
- OR launched recently with no PPC person on team

**GATE 4 — They can pay**
- Company has revenue signals: funded startup · Shopify store with reviews · established brand · hires freelancers
- Budget signal: $5k+ ad spend/mo (estimated from company size/category)

**GATE 5 — They can hire globally / remote**
- Not government · not regulated industry (healthcare ads, crypto, gambling) · not local-only brick-and-mortar

---

### LEAD SOURCES — use ALL in parallel

**SOURCE 1 — Apollo MCP (primary B2B source)**
Use `apollo_mixed_companies_search` or `apollo_mixed_people_api_search`:
- Search: e-commerce companies, DTC brands, SaaS startups, lead-gen businesses
- Filters: USA/UK/CA/AU/UAE · 10–500 employees · revenue $1M–$50M
- Industries: e-commerce · SaaS · health/wellness · education · real estate · insurance · legal services · home services
- Look for: "Marketing Manager" or "CMO" or "Founder" as decision maker contact
- Use `apollo_organizations_enrich` to get full company data for top candidates
- Use `apollo_people_match` to find decision maker email/LinkedIn

**SOURCE 2 — Vibe Prospecting MCP**
Use `fetch-entities` and `enrich-business` tools:
- Search for DTC ecom brands, SaaS companies, growing startups in whitelist countries
- Use `fetch-businesses-events` to find companies with recent funding, product launches, hiring signals — these are buying signals
- Use `enrich-prospects` to get contact details for decision makers
- Use `match-business` to verify company data

**SOURCE 3 — Apify MCP (scraping signals)**
Use `call-actor` to invoke relevant Apify actors:
- Search actors for: LinkedIn company scraper, Facebook Ad Library scraper, Shopify store scraper
- LinkedIn: find companies posting "hiring marketing manager" (they have budget)
- Facebook Ad Library: find brands actively running ads (confirmed spend)
- Shopify: find DTC stores with traffic but potentially poor ad performance
Use `get-actor-output` to retrieve and parse results

**SOURCE 4 — Meta Ad Library (active ad spenders)**
WebSearch: `"facebook ad library" ecommerce brand active ads USA 2025 site:facebook.com`
WebSearch: `site:facebook.com/ads/library active_status=active ecommerce`
Companies running active Meta ads = confirmed ad budget. Extract brand names → enrich via Apollo/Vibe.

**SOURCE 5 — WebSearch buying signals (HOT leads)**
These companies are actively expressing pain right now:
- `"looking for google ads" OR "need PPC help" OR "hiring paid media" site:reddit.com`
- `"google ads aren't working" OR "ROAS dropped" OR "wasting money on ads" site:reddit.com`
- `"google ads consultant" needed site:twitter.com 2025`
- `"our facebook ads" OR "meta ads performance" dropped site:reddit.com r/ecommerce`
- `"need freelancer" "google ads" OR "meta ads" site:reddit.com OR site:twitter.com`

**SOURCE 6 — Job postings as lead signal (pitch instead of apply)**
Find companies posting PPC/paid media jobs they haven't filled in 30+ days — they have budget and need:
- WebSearch: `site:linkedin.com/jobs "google ads specialist" OR "paid media manager" remote past-month`
- WebSearch: `site:indeed.com "meta ads" OR "google ads" remote past-30-days`
Extract company name → research as a direct client pitch target (NOT applying to the job)

---

### ENRICHMENT (mandatory for every lead passing all 5 gates)

For each candidate lead, gather:
1. **Company name + website**
2. **Decision maker**: name, title, LinkedIn URL, email (via Apollo `apollo_people_match` or Vibe `enrich-prospects`)
3. **Ad spend signal**: are they running ads? (Meta Ad Library / Google Transparency Center check via WebSearch)
4. **Revenue/size signal**: funding round, employee count, Shopify reviews, app store presence
5. **Pain point**: what's broken or missing in their current marketing? (1-2 sentences, evidence-based)
6. **Entry angle**: how would Zulqarnain pitch this lead? (1 sentence hook)

---

### SCORING (0-100 — MINIMUM 80 TO INCLUDE)

| Signal | Points |
|---|---|
| Decision maker contact found (email or LinkedIn) | +20 |
| Confirmed active ad spend (Meta/Google library) | +20 |
| Clear pain point identified (evidence-based) | +15 |
| Company in whitelist country | +10 |
| Revenue signal ($1M+) or recently funded | +10 |
| Fresh buying signal (<7 days old) | +10 |
| Warm entry angle exists | +10 |
| Can hire PK/remote confirmed possible | +5 |

**HARD THRESHOLD: Only leads scoring ≥80 make the final list.**
**TARGET: 10 leads max — quality over quantity. If fewer than 10 reach 80+, report however many qualified. NEVER pad with low-quality leads to hit a number.**

---

### OUTPUT

**STEP 1: Build lead cards (one per qualified lead)**
For each lead include:
- Score (0-100)
- Company name + website
- Industry + country
- Decision maker: name, title, LinkedIn URL, email
- Ad spend evidence (what signals confirm they spend)
- Pain point (1-2 sentences, specific)
- Entry angle / pitch hook (1 sentence)
- Source platform

**STEP 2: Append to Excel**
File: `/Users/mc/Downloads/Leads/HMZ-Leads-Daily.xlsx`
Columns: Date · Score · Company · Website · Country · Industry · Decision Maker · Title · Email · LinkedIn · Ad Spend Signal · Pain Point · Entry Angle · Source
Create directories/file if they don't exist. Append today's rows. Never wipe existing data.

**STEP 3: Build HTML Report**
Save: `/Users/mc/Downloads/HMZ-Elite-Leads-[DATE].html`
- Header: "HMZ ELITE LEADS — [DATE] — [N] QUALIFIED (80+ score)"
- Lead cards sorted by score (highest first)
- Color coding: ≥90=gold · 80-89=green
- Each card: score badge, company, country, decision maker name/title/links, pain point, entry angle, ad spend evidence, all contact links
- Footer: sources used, total leads in Excel to date

**STEP 4: Email**
Gmail MCP `create_draft` → hmzainjamil@gmail.com
Subject: "💎 HMZ Elite Leads — [N] Qualified — [DATE]"
Body:
- Summary: N leads found, sources used, avg score
- Top 5 lead cards with full details
- Path to full report: ~/Downloads/HMZ-Elite-Leads-[DATE].html

**STEP 5: Mark complete (MANDATORY)**
Run: `python3 /Users/mc/.claude/bin/hmz-bdm-state-update hmz-daily-leads`

Execute all steps. Use Apollo MCP, Vibe MCP, Apify MCP, Gmail MCP, WebSearch — all in parallel where possible. Prioritize quality — 10 gold leads beats 100 garbage leads. This runs autonomously.
