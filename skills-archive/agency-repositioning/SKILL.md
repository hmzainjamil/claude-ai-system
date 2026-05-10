---
name: agency-repositioning
description: Full orchestrated agency repositioning workflow. Runs customer-matrix → niche selection → service-productizer → sub-brand-generator → outcome-pricing → outreach system → 90-day execution plan. Master orchestrator for agency transformation.
allowed-tools: Read, Grep, Glob, Bash, WebFetch, WebSearch, Write, Agent
triggers: ["reposition agency", "agency repositioning", "transform my agency", "pivot agency", "agency pivot", "reinvent agency", "stop staff augmentation", "move away from staff aug", "agency transformation", "new direction agency"]
---

# /agency-repositioning — Full Agency Transformation Orchestrator

> **Trigger**: "reposition agency" / "agency pivot" / "stop staff augmentation" / "transform my agency"
> **No command needed** — auto-activates.
> **This is the master orchestrator** — it sequences all other skills automatically.

## WHAT THIS DOES

Runs the complete repositioning sequence:
```
customer-matrix → niche decision → service-productizer →
sub-brand-generator (optional) → outcome-pricing →
agent-foot-in-door → agency-rescue plan → outreach launch
```

All in one session. Output: complete repositioning kit, ready to execute.

## PREREQUISITE INPUT
```
1. Agency name + current services (1 sentence)
2. Team size + monthly burn
3. List of last 10–20 clients (name, industry, what you did, deal size)
4. Current revenue + target revenue
5. Runway (months)
6. What's NOT working right now?
```

## ORCHESTRATION SEQUENCE

### PHASE A — DIAGNOSIS (15 min)
```
Run: /customer-matrix on client list
Output: top 3 niches ranked, micro-ICP per niche

Then decide:
  □ Niche #1 to go all-in on (based on score)
  □ Niche #2 to test in parallel
  □ Niches to ignore
```

### PHASE B — OFFER DESIGN (20 min)
```
For winning niche, run: /service-productizer
Output: complete fixed-price package

Then: /outcome-pricing
Output: outcome-based pricing alternative

Combine: offer a choice:
  Option A: Fixed fee ($X, defined scope)
  Option B: Outcome-based ($Y/month, guaranteed result)
```

### PHASE C — POSITIONING (15 min)
```
Decision: Use main brand or sub-brand for this niche?
  If main brand can flex → update headline + ICP language
  If niche is very different → run /sub-brand-generator

Output: positioning doc + website headline + LinkedIn banner text
```

### PHASE D — SALES SYSTEM (20 min)
```
Run: /agent-foot-in-door if automation is core to the offer
Output: agent product kit + pitch + objection handles

Build outreach stack:
  □ 3 cold email hooks (niche-specific)
  □ LinkedIn DM sequence (3-touch)
  □ LinkedIn content hooks (5 post ideas)
  □ Meta ad concept (1 productized offer ad)

Apollo/LinkedIn search:
  □ Exact search string for micro-ICP
  □ Estimated audience size
  □ Recommended daily outreach volume
```

### PHASE E — 90-DAY EXECUTION PLAN
```
MONTH 1 — FOUNDATION:
  Week 1: Niche confirmed, offer finalized, positioning updated
  Week 2: Email infra live (3 warmed inboxes, Smartlead/Instantly)
  Week 3: First 500 emails sent, LinkedIn content started
  Week 4: First calls booked, close #1, document delivery

MONTH 2 — MOMENTUM:
  Week 5: Scale outreach to 1,000/week
  Week 6: LinkedIn DMs + content (1 post/day)
  Week 7: Launch Meta ad experiment ($10–20/day)
  Week 8: 2–3 deals closed, delivery systemized

MONTH 3 — SCALE:
  Week 9: Referral loop built into delivery
  Week 10: Test niche #2 outreach (separate)
  Week 11: Retainer pitch to Month 1 clients
  Week 12: Review, optimize, plan Month 4–6

TARGET METRICS (track weekly):
  Emails sent: [target]
  Open rate: >40%
  Reply rate: >3%
  Calls booked: [X/week]
  Deals closed: [X/month]
  Revenue: $[target]
```

## INTEGRATION MAP
```
This skill orchestrates:
  ├─ /customer-matrix       → niche discovery
  ├─ /service-productizer   → offer design
  ├─ /outcome-pricing       → pricing model
  ├─ /sub-brand-generator   → brand (if needed)
  ├─ /agent-foot-in-door    → agent product (if automation-based)
  ├─ /agency-rescue         → if runway <4 months (urgent mode)
  └─ launch-optimized       → outreach + lead gen + email sequences

Connected to existing launch-optimized routing:
  → /cold-email-outreach
  → /linkedin-automation
  → /meta-ads
  → /client-proposal
  → /pdf-report (final deliverable)
```

## DELIVERABLE PACKAGE
```
Output files (all saved to ~/Downloads/AgencyRepositioning-[Date]/):
  01-Customer-Matrix.md
  02-Niche-Decision.md
  03-Productized-Offer.md
  04-Pricing-Model.md
  05-Brand-Positioning.md
  06-Sales-Kit.md (pitch + emails + objections)
  07-90-Day-Plan.md
  08-Outreach-Sequences.md
```

## OUTPUT FORMAT
Complete repositioning kit. All files. Ready to execute Monday morning.
