# WFH / REMOTE JOB FINDER — 2026 Edition (always-on)

**Auto-activates on:** "remote job" / "wfh job" / "work from home" / "find remote work" / "job search" / "remote hiring" / "job board" / "find job india" / "remote apply" / "ats search" / "job tracker"

---

## WHAT THIS SYSTEM DOES

Full automated remote job-finding pipeline:
- Multi-board scraping (LinkedIn, RemoteOK, Remotive, Wellfound, WWR, Himalayas)
- Google ATS operator search (Lever, Greenhouse, Ashby, Workday)
- Daily fresh-role alerts → deduplicated tracker sheet
- Resume tailoring per role (keyword swap, headline match)
- Scam detection filter (auto-scores every listing)
- Outreach sequencer (follow-up cadence per application)
- Weekly rhythm enforcer (day-by-day action plan)

---

## QUICK COMMANDS

```bash
# Full daily sweep — new roles across all boards
python3 ~/.claude/bin/remote-job-hunter --daily

# Target search
python3 ~/.claude/bin/remote-job-hunter --role "customer support" --location "india" --boards all

# ATS operator blast (finds hidden roles)
python3 ~/.claude/bin/remote-job-hunter --ats --role "data analyst"

# Scam check a listing
python3 ~/.claude/bin/remote-job-hunter --check "https://job-url.com"

# Export tracker to Excel
python3 ~/.claude/bin/remote-job-hunter --export

# Weekly schedule printout
python3 ~/.claude/bin/remote-job-hunter --weekly-plan
```

---

## PLATFORM STACK

| Platform | Type | Best for | India-friendly |
|---|---|---|---|
| LinkedIn Jobs | General + remote filter | Fast alerts, broad coverage | ✅ |
| We Work Remotely | Remote-first board | All functions | ✅ |
| Remote OK | Global remote | Tech + ops | ✅ |
| Remotive | Remote-first | India-friendly searches | ✅ |
| Wellfound | Startup hiring | Early-stage, equity roles | ✅ |
| Himalayas | Remote-first | High-quality listings | ✅ |
| FlexJobs | Curated | Scam-reduced, trust-high | ✅ |
| Naukri | India-specific | WFH roles in India | ✅ |
| Indeed | General | WFH filter + India | ✅ |
| Official ATS | Direct company | Lever / Greenhouse / Ashby | ✅ |

---

## ATS GOOGLE OPERATOR PATTERNS

```
site:lever.co "Customer Support" "Remote"
site:lever.co "Data Analyst" "Remote" "India"
site:greenhouse.io "Marketing" "Remote"
site:greenhouse.io "Operations" "Remote" "India"
site:myworkdayjobs.com "Remote" "India"
site:jobs.ashbyhq.com "operations" "remote"
site:jobs.ashbyhq.com "customer success" "remote" "india"
```

**Add to Google:** `after:2026-04-01` → forces fresh results only

---

## 29 REMOTE SEARCH KEYWORD VARIATIONS

Use these across all job boards:
```
Remote · Work from home · WFH · Virtual · Distributed
Anywhere · India remote · Hybrid · Fully remote · Remote-first
Work from anywhere · Location independent · Async · Async-first
Remote friendly · Remote eligible · APAC remote · IST timezone
```

---

## LINKEDIN FEED DISCOVERY STRINGS

Search the LinkedIn main feed (not just Jobs tab):

```
"hiring" "remote" "customer support"
"hiring" "remote" "data analyst"
"remote" "apply" "india" "marketing"
"work from anywhere" "operations"
"we're hiring" "remote" "customer success"
"open role" "remote" "india"
"join our team" "wfh" "india"
```

---

## SCAM DETECTION FILTER — AUTO-SCORE

Score any listing automatically. Flags if ≥ 3 match:

| Red flag | Weight |
|---|---|
| Pay unrealistically high for simple work | +3 |
| Weak/missing company website | +3 |
| Recruiter avoids official email domain | +3 |
| Asks for money / equipment deposit / training fee | +5 |
| Vague description copied across many titles | +2 |
| Process unusually rushed or "too easy" | +2 |
| Contact via Telegram/WhatsApp only | +2 |
| No LinkedIn company page | +2 |

**Score 0–2**: Apply  |  **Score 3–5**: Verify first  |  **Score 6+**: Skip

---

## RESUME TAILORING PROTOCOL (per application)

Edit these 4 zones per role — nothing else:

1. **Headline** → match job title family exactly
2. **Top summary** (3 lines) → mirror top 3 role keywords
3. **Tools section** → add any missing tools mentioned in JD
4. **Top 2 bullet points** → reframe to match primary responsibility

**Remote-readiness signals to always include:**
- Tools: Slack, Zoom, Google Workspace, Jira, Notion, Trello, Asana, MS Teams
- Proof: "Coordinated weekly reporting across distributed stakeholders using Slack, Sheets, and async updates"
- Show: ownership, independent execution, async communication

---

## APPLICATION VELOCITY TARGETS

| Approach | Daily target | Expected response rate |
|---|---|---|
| Spray & pray (never do) | 100+ | < 0.5% |
| Quality-focused | 5–12 | 3–8% |
| Hyper-targeted (best) | 3–5 | 8–15% |

**Apply within 24–48h of posting.** After 72h, response rate drops 40%.

---

## WEEKLY RHYTHM (Day-by-Day)

| Day | Focus | Actions |
|---|---|---|
| Monday | Fresh roles | Check alerts → apply to newest → update tracker |
| Tuesday | Company watchlist | Visit 10–15 target career pages → save openings |
| Wednesday | LinkedIn discovery | Search feed posts → founder/recruiter posts |
| Thursday | Resume optimization | Improve 1 resume version + 1 cover template |
| Friday | Follow-up | Reconnect with recruiters → check status → polite follow-ups |
| Saturday | Skill proof | Improve portfolio / case studies / certs |
| Sunday | Review | Measure apps/interviews → set next-week priorities |

---

## APPLICATION TRACKER COLUMNS

Track in `~/Downloads/job-tracker.xlsx`:
```
Date Applied | Company | Job Title | Source | Role URL
Country/TZ restriction | Resume version | Status
Follow-up date | Notes | Scam score
```

---

## TARGET COMPANY WATCHLIST STRATEGY

1. Build list of 30–50 remote-first companies
2. Check career pages 2x/week
3. Set Google Alert: `"[company name]" "we're hiring" OR "join us"`
4. Note any country/timezone restrictions per company

**Top remote-first company types to target:**
- SaaS companies (most remote-friendly)
- US/EU startups that hire globally
- Digital agencies (content, marketing, ops roles)
- Customer success / support (most India-friendly)

---

## FUNDING + GROWTH SIGNAL TRACKING

Watch for:
- Series A/B announcements → spike in hiring
- Product launches → content/support roles follow
- "We're expanding to APAC" → India hires imminent
- Founder posts on LinkedIn about hiring

**Where to watch:** TechCrunch, Product Hunt, LinkedIn, Twitter/X

---

## MAE INTEGRATION

```bash
# Full daily job sweep via MAE
mae run "Remote job search: find customer support roles for India-based candidate. Search LinkedIn, RemoteOK, Remotive, Wellfound. Filter: remote, India-friendly, posted last 48h. Score each for scam signals. Export top 10 to tracker."

# Resume tailoring via MAE
mae run "Tailor resume for [ROLE]. Match headline, top 3 keywords, remote tools, 2 bullets. Input: [JD text]. Output: updated sections only."

# Company watchlist check via MAE
mae run "Check career pages for [company1, company2, company3]. Find any new remote openings. Report: role title, URL, country restrictions, apply deadline."
```

---

## DigiMinds Service Offering

| Package | Deliverable | Price |
|---|---|---|
| Job Search Audit | Current strategy review + 10 fixes | $150 |
| Resume Makeover | Remote-ready rewrite + ATS optimize | $200 |
| Full Search System | Tracker + tailored resume + weekly plan | $400 |
| Monthly Managed Search | Daily applications + follow-up handled | $800/mo |
