---
name: customer-matrix
description: Ingests client list or CRM data → pattern-matches → outputs top 3 niches with micro-ICP per niche (industry + buyer role + pain + proof). Foundation for repositioning any services agency. Ashar Samdani method.
allowed-tools: Read, Grep, Glob, Bash, WebFetch, WebSearch, Write, Agent
triggers: ["customer matrix", "analyze my clients", "find my niche", "client patterns", "icp", "ideal customer", "who should i target", "analyze past clients", "what niche", "niche down"]
---

# /customer-matrix — Find Your Winning Niche From Client Data

> **Trigger**: "analyze my clients" / "find my niche" / "customer matrix" / "ICP" / "who should I target"
> **No command needed** — auto-activates on these phrases.

## WHAT THIS DOES

You paste your client list (names, industries, deal sizes, outcomes) →
This skill extracts patterns → outputs your top 3 niches with full micro-ICP per niche.

## INPUT FORMATS ACCEPTED
- Bullet list of clients + industry + what you did
- CRM export (CSV paste)
- Plain text description of past projects
- Invoice history description

## EXECUTION WORKFLOW

### Step 1 — Data Extraction
For each client, extract:
```
Industry | Buyer Title | Pain They Had | Solution Delivered | $ Value | Result Achieved | Repeat client?
```

### Step 2 — Pattern Matrix
Build frequency table:
```
Industry          | Count | Avg Deal $ | Repeat? | Common Pain
[Insurance]       | 3     | $8,400     | Yes     | Manual follow-up
[Real Estate]     | 2     | $5,200     | No      | Lead tracking
[SaaS]            | 4     | $12,000    | Yes     | Onboarding drops
```

### Step 3 — Niche Scoring
Score each industry cluster on:
- Volume (how many clients)
- Deal size (higher = better)
- Repeat rate (sticky = good)
- Pain clarity (can you describe it in 1 sentence?)
- Proof available (case study exists?)
- Market size (enough companies in niche?)

### Step 4 — Micro-ICP Per Top 3 Niches

**Output per niche:**
```
NICHE #[1/2/3]: [Specific Industry]

MICRO-ICP:
  Company type: [e.g., "independent insurance brokers, 5–50 staff, US-based"]
  Buyer title: [e.g., "Operations Manager or Owner-Operator"]
  Company revenue: [$500K–$5M ARR]
  Pain: [specific, 1 sentence — e.g., "manual follow-up on 200+ leads/month causing 40% drop-off"]
  Trigger event: [what makes them ready to buy — e.g., "just hired 2nd agent, overwhelmed"]
  Proof we have: [yes/no + what]
  Outreach angle: [1-line hook for cold email]
  Productized offer match: [which of your packages fits]

WHERE TO FIND THEM:
  LinkedIn search: [exact search string]
  Apollo filter: [industry + headcount + title]
  Facebook groups: [group names]
  Reddit: [subreddits]
  Events: [conferences, associations]
```

### Step 5 — Niche Ranking Decision
Output final recommendation:
```
BET ON: Niche #X — reason (most proof + clearest pain + repeat rate)
TEST NEXT: Niche #Y — reason
WATCH: Niche #Z — reason (promising but needs more data)
```

### Step 6 — Action Plan
For winning niche:
1. Write 1 case study from existing client (format provided)
2. Update website headline to speak to this niche
3. Build Apollo/LinkedIn search query (provided)
4. Draft 3 email hooks (provided)
5. Set up 1 landing page targeting this niche

## OUTPUT FORMAT
Full markdown report + customer matrix table + 3 micro-ICPs + action plan.
Save to: `~/Downloads/[AgencyName]-Customer-Matrix-[Date].md`
