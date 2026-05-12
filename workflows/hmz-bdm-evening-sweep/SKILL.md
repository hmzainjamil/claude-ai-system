---
name: hmz-bdm-evening-sweep
description: HMZ BDM evening sweep — 10-platform job intelligence with strict PK-remote filters + Reddit drafts → scored report → email
---

## HMZ BDM EVENING SWEEP — 9 PM PKT

You are running the daily evening job sweep for Zulqarnain (HMZ), a Pakistani paid ads specialist. Same platform coverage as morning sweep but catches new postings from the US business day. Run all platforms in parallel.

---

### UNIVERSAL HARD FILTERS (apply to EVERY job from EVERY platform — no exceptions)

**SCOPE:** Meta Ads / Google Ads / DTC ecom / Lead Gen / Paid Media / PPC ONLY
**RATE FLOOR:** $15+/hr hourly · $500+ fixed price
**WORK AUTH:** Zulqarnain is Pakistani freelancer, remote-only from Pakistan.
  REJECT: "must be authorized to work in US/UK/EU/AU/CA" · visa/permit required · relocation · physical presence · "local candidates only" · US-only 1099
  ACCEPT: worldwide remote · global · freelance worldwide · timezone-flexible · PK/Asia eligible
**GEO BLACKLIST (buyer/employer country):** India · Pakistan · Bangladesh · Philippines · Israel · Indonesia · Malaysia · Nigeria · Egypt · Kenya · Ghana · Sri Lanka · Nepal · Vietnam · Cambodia · Myanmar · Ethiopia · Tanzania · Uganda · Rwanda
**GEO WHITELIST:** USA · UK · Canada · Australia · New Zealand · UAE · Germany · Netherlands · Ireland · Norway · Sweden · Denmark · Finland · Switzerland · Austria · Singapore · France · Spain · Italy · Belgium · Portugal
**FRESHNESS:** Posted <48h only — hard reject anything older
**HARD REJECT ROLES:** cold-calling · commission-only · German/Dutch/French language required · creative director · video editor · social media manager · Amazon PPC/FBA · retention-only · CRM-only · VA · recruiter · data entry

---

### PLATFORM SWEEP (run all in parallel)

**PLATFORM 1 — LinkedIn**
WebSearch: `site:linkedin.com/jobs "google ads" OR "meta ads" OR "paid media" remote posted:past-24h`
WebSearch: `site:linkedin.com/jobs "media buyer" OR "performance marketing manager" remote 2025`
Extract. Filter. Take top 8.

**PLATFORM 3 — We Work Remotely**
WebFetch: `https://weworkremotely.com/remote-jobs/search?term=paid+media`
WebFetch: `https://weworkremotely.com/remote-jobs/search?term=facebook+ads`
Extract. Filter. Take top 5.

**PLATFORM 4 — Remotive**
WebFetch: `https://remotive.com/remote-jobs/marketing?search=ppc`
WebFetch: `https://remotive.com/remote-jobs/marketing?search=paid+media`
Extract. Filter. Take top 5.

**PLATFORM 5 — Remote.co**
WebSearch: `site:remote.co "PPC" OR "paid media" OR "google ads" remote job`
Extract. Filter. Take top 5.

**PLATFORM 6 — Wellfound (AngelList)**
WebSearch: `site:wellfound.com/jobs "paid media" OR "google ads" OR "meta ads" remote`
Startup roles — often worldwide contractors. Filter. Take top 5.

**PLATFORM 7 — Contra (freelance-first)**
WebSearch: `site:contra.com google ads meta ads paid media freelance remote`
Filter. Take top 5.

**PLATFORM 8 — Workana / Torre**
WebSearch: `site:workana.com "google ads" OR "meta ads" OR "paid media" remote english`
WebSearch: `site:torre.ai "paid media" OR "google ads" remote`
Workana/Torre have global reach. Filter strictly for whitelist clients. Take top 4.

**PLATFORM 9 — Toptal / Braintrust**
WebSearch: `site:toptal.com "paid media" OR "google ads" OR "PPC" freelance`
WebSearch: `site:usebraintrust.com "google ads" OR "paid media" remote`
These platforms pay premium rates globally. Filter. Take top 4.

**PLATFORM 10 — Product Hunt Jobs / HN Who's Hiring**
WebSearch: `site:news.ycombinator.com "who is hiring" "google ads" OR "paid media" OR "meta ads" remote 2025`
WebSearch: `site:producthunt.com/jobs "paid media" OR "google ads" remote`
Direct employer postings. Filter. Take top 4.

---

### SCORING (0-100 per job)
- Scope match (Google/Meta/DTC/LeadGen) → +25
- Whitelist country employer → +20
- Rate floor met ($15+/hr or $500+) → +15
- Fresh <24h → +15 · <48h → +8
- Remote + worldwide/PK eligible confirmed → +15
- Salary clearly stated → +5
- Startup/direct employer (no recruiter middleman) → +5 bonus

**THRESHOLD: Only include jobs scoring ≥65. Hard discard <65.**

---

### REDDIT VALUE COMMENTS (3 max — NEVER new posts, cap is strict)
Search for threads posted <12h in: r/PPC · r/FacebookAds · r/GoogleAds · r/digital_marketing · r/ecommerce
Pick 3 threads where Zulqarnain can add genuine expert value (campaign structure, ROAS issues, bidding strategy, lead gen).
Draft 3 insightful comments (150-250 words each) — expertise-first, solution-specific, never salesy.
Save to: `/Users/mc/Downloads/HMZ-Reddit-Comments-[DATE].txt`

---

### OUTPUT

**STEP 1: Deduplicate** — same job on multiple platforms = keep highest-scoring instance only

**STEP 2: Build HTML Report**
Save: `/Users/mc/Downloads/HMZ-BDM-Evening-[DATE].html`
- Dark theme
- Header: "HMZ BDM EVENING REPORT — [DATE] — [N] JOBS · [N] PLATFORMS"
- Platform sections with job counts
- Job cards: Score badge (≥80=green, 60-79=amber), Title, Company, Platform, Salary, Posted, Location, Apply button
- Reddit Comments section with 3 drafts
- Footer: next sweep 9 AM PKT tomorrow

**STEP 3: Email**
Gmail MCP `create_draft` → hmzainjamil@gmail.com
Subject: "🌙 HMZ Evening — [N] Jobs / [N] Platforms + Reddit Drafts — [DATE]"
Body: top 15 jobs sorted by score + Reddit comment drafts + all apply links

**STEP 4: Save latest**
Copy to `/Users/mc/Downloads/HMZ-BDM-Latest.html`

**STEP 5: Mark complete (MANDATORY)**
Run: `python3 /Users/mc/.claude/bin/hmz-bdm-state-update hmz-bdm-evening-sweep`

Execute all steps. Run platforms in parallel. Apply all filters strictly. This runs autonomously.
