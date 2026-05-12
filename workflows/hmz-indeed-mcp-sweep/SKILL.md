---
name: hmz-indeed-mcp-sweep
description: HMZ dedicated Indeed MCP sweep — structured job search via Indeed connector → top scored jobs → email to hmzainjamil@gmail.com
---

## HMZ INDEED MCP SWEEP — DEDICATED INDEED-ONLY PIPELINE

You are running the dedicated Indeed job sweep for Zulqarnain (HMZ) using the Indeed MCP connector. This is SEPARATE from the general morning/evening sweeps. Use ONLY the Indeed MCP tools — no WebSearch, no WebFetch.

### HARD RULES (never violate):
- Scope: Meta Ads + Google Ads + DTC/Ecom + Lead Gen ONLY
- Rate floor: $15+/hr hourly, $500+ fixed
- GEO BLACKLIST: India, Pakistan, Bangladesh, Philippines, Israel, Indonesia, Malaysia, Nigeria, Egypt, Kenya, Ghana, Sri Lanka, Nepal, Vietnam, Cambodia, Myanmar, Ethiopia, Tanzania, Uganda, Rwanda
- GEO WHITELIST: USA, UK, Canada, Australia, New Zealand, UAE, Germany, Netherlands, Ireland, Norway, Sweden, Denmark, Finland, Switzerland, Austria, Singapore, France, Spain, Italy, Belgium, Portugal
- Freshness: max 48 hours old
- WORK AUTHORIZATION: Zulqarnain is a Pakistani freelancer working 100% remote from Pakistan. HARD REJECT any job that: requires work authorization/visa/permit in any country, says "must be authorized to work in US/UK/EU/AU/CA", requires relocation, requires physical presence, is contractor-only for US residents, or says "local candidates only". ONLY accept: worldwide remote, global remote, contractor/freelance worldwide, or explicitly PK/Asian-timezone eligible.
- HARD REJECT: cold-calling, commission-only, German/Dutch/French language required, creative-producer, retention-only, CRM-only, VA, video editor, Amazon PPC/FBA

### STEP 1: Indeed MCP Search (all via search_jobs tool)
Run these 8 queries via the Indeed MCP `search_jobs` tool:
1. "google ads manager" + location=Remote
2. "meta ads specialist" + location=Remote
3. "paid media buyer" + location=Remote
4. "facebook ads manager" + location=Remote
5. "PPC specialist" + location=Remote
6. "digital marketing manager google ads" + location=Remote
7. "performance marketing manager" + location=Remote
8. "SEM specialist remote" + location=Remote

Sort each by: date (newest first).

### STEP 2: Get Job Details
For each candidate job, call `get_job_details` to retrieve:
- Full job description
- Salary/rate range
- Exact location / remote eligibility
- Company name
- Posted date
- Apply URL

### STEP 3: Filter
Hard reject if:
- Buyer/employer from GEO BLACKLIST
- Not remote or not PK-eligible
- Rate below floor
- Posted >48h ago
- Scope outside Google/Meta/DTC/LeadGen

### STEP 4: Score (0-100)
- Scope match (Google/Meta/DTC/LeadGen) → +25
- Whitelist country employer → +20
- Rate floor met ($15+/hr or $500+) → +15
- Fresh <24h → +15, <48h → +8
- Remote confirmed → +10
- PK/worldwide hiring confirmed → +10
- Salary clearly stated → +5

Deduplicate by job ID. Take top 15 scoring jobs.

### STEP 5: Build HTML Report
Create /Users/mc/Downloads/HMZ-Indeed-MCP-[DATE]-[TIME].html
Structure:
- Header: "HMZ INDEED MCP REPORT — [DATE] [TIME] — [N] JOBS FOUND"
- Each job card: Score badge (≥80=green, 60-79=amber, <60=red), Title, Company, Salary/Rate, Posted, Location, Apply button
- Footer: powered by Indeed MCP connector, next sweep in 12h

### STEP 6: Email Report
Use Gmail MCP `create_draft` tool to send to hmzainjamil@gmail.com:
Subject: "📋 HMZ Indeed MCP — [N] Jobs — [DATE]"
Body: HTML table of top 15 jobs with scores, salary, posted date, and apply links.

### STEP 7: Mark task complete (MANDATORY — run this last)
Run shell command: python3 /Users/mc/.claude/bin/hmz-bdm-state-update hmz-indeed-mcp-sweep

Execute all steps. Use only Indeed MCP tools for job data. Be thorough.
