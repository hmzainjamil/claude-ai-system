---
name: hmz-bdm-morning-sweep
description: HMZ BDM morning sweep — 10-platform job intelligence with strict PK-remote filters → scored report → email
---

## HMZ BDM MORNING SWEEP — 9 AM PKT

You are running the daily morning job sweep for Zulqarnain (HMZ), a Pakistani paid ads specialist. Execute all platforms in parallel where possible. Apply ALL filters before scoring.

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
WebSearch: `site:linkedin.com/jobs "PPC specialist" OR "performance marketing" remote 2025`
Extract title, company, salary, posted, URL. Take top 8 after filtering.

**PLATFORM 3 — We Work Remotely**
WebFetch: `https://weworkremotely.com/remote-jobs/search?term=google+ads`
WebFetch: `https://weworkremotely.com/remote-jobs/search?term=paid+media`
Extract all open roles. Filter. Take top 5.

**PLATFORM 4 — Remotive**
WebFetch: `https://remotive.com/remote-jobs/marketing?search=google+ads`
WebFetch: `https://remotive.com/remote-jobs/marketing?search=meta+ads`
Extract. Filter. Take top 5.

**PLATFORM 5 — Remote.co**
WebSearch: `site:remote.co "google ads" OR "meta ads" OR "paid media" remote job`
Extract. Filter. Take top 5.

**PLATFORM 6 — Wellfound (AngelList)**
WebSearch: `site:wellfound.com/jobs "google ads" OR "meta ads" OR "paid media" remote`
Extract startup roles — these often allow worldwide contractors. Filter. Take top 5.

**PLATFORM 7 — Contra**
WebFetch: `https://contra.com/opportunities?q=google+ads&remote=true`
WebSearch: `site:contra.com google ads meta ads paid media freelance remote`
Contra is freelance-first, worldwide eligible. Filter. Take top 5.

**PLATFORM 8 — Pangian / Jobspresso**
WebSearch: `site:pangian.com "google ads" OR "paid media" remote`
WebSearch: `site:jobspresso.co "google ads" OR "meta ads" remote`
Extract. Filter. Take top 4.

**PLATFORM 9 — Himalayas / EuroRemote**
WebSearch: `site:himalayas.app "google ads" OR "paid media" OR "meta ads" remote`
WebSearch: `site:euroremote.io "paid media" OR "google ads" remote`
Extract. Filter. Take top 4.

**PLATFORM 10 — X/Twitter Jobs + Slack Communities**
WebSearch: `"hiring" "google ads" OR "meta ads" remote freelance twitter.com 2025`
WebSearch: `"looking for" "PPC" OR "paid media" remote freelancer site:twitter.com`
These are often direct-hire with no middleman. Filter. Take top 4.

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

### OUTPUT

**STEP 1: Deduplicate** — same job posted on multiple platforms = keep highest-scoring instance only

**STEP 2: Build HTML Report**
Save: `/Users/mc/Downloads/HMZ-BDM-Morning-[DATE].html`
- Header: "HMZ BDM MORNING REPORT — [DATE] — [N] JOBS · [N] PLATFORMS"
- Platform sections with counts
- Job cards: Score badge (≥80=green, 60-79=amber), Title, Company, Platform, Salary, Posted, Location, Apply button
- Footer: next sweep 9 PM PKT

**STEP 3: Email**
Gmail MCP `create_draft` → hmzainjamil@gmail.com
Subject: "🎯 HMZ Morning — [N] Jobs / [N] Platforms — [DATE]"
Body: top 15 jobs sorted by score, with apply links

**STEP 4: Save latest**
Copy to `/Users/mc/Downloads/HMZ-BDM-Latest.html`

**STEP 5: Mark complete (MANDATORY)**
Run: `python3 /Users/mc/.claude/bin/hmz-bdm-state-update hmz-bdm-morning-sweep`

Execute all steps. Run platforms in parallel. Apply all filters strictly. This runs autonomously.
