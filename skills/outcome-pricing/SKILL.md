---
name: outcome-pricing
description: Converts hourly/project pricing to outcome-based or usage-based model. Calculates value delivered, sets price anchors, builds pricing page copy, and drafts transition messaging for existing clients.
allowed-tools: Read, Grep, Glob, Bash, WebFetch, WebSearch, Write
triggers: ["outcome pricing", "value based pricing", "stop charging hourly", "usage based pricing", "outcome based", "charge for results", "pricing model", "move away from hourly", "fixed price", "roi pricing"]
---

# /outcome-pricing — Convert to Outcome-Based Pricing

> **Trigger**: "outcome pricing" / "value-based pricing" / "stop charging hourly" / "charge for results"
> **No command needed** — auto-activates.

## WHAT THIS DOES

Takes your current pricing model (hourly/project) → builds outcome-based or usage-based alternative:
- Value calculation (what is the outcome actually worth to the client?)
- Price anchor setting
- Pricing page copy
- Transition script for existing clients
- Risk mitigation (guarantee design)

## INPUT NEEDED
```
Current model: [$X/hr or $Y/project]
What you deliver: [e.g., "lead follow-up automation"]
Client outcome: [e.g., "30% more conversions, 3 hrs/day saved"]
Client industry: [e.g., "insurance brokers, $1M ARR"]
Typical project size: [$X total, X weeks]
```

## EXECUTION WORKFLOW

### Step 1 — Value Calculation
```
OUTCOME VALUE FORMULA:
  Time saved: [X hrs/week × $[hourly rate] × 52 weeks] = $[annual value]
  Revenue gained: [X% lift × $[monthly revenue] × 12] = $[annual value]
  Cost avoided: [X FTE × $[salary]] = $[annual value]

EXAMPLE:
  "3 hrs/day × $50/hr × 250 working days = $37,500/year saved
   30% conversion lift × $50K/month pipeline × 12 = $180,000/year gained
   TOTAL OUTCOME VALUE: ~$217,500/year"

YOUR PRICE SHOULD BE: 10–20% of annual outcome value
  At $217,500 value → charge $21,750–$43,500/year
  vs. your hourly model: [X hrs × $Y = $Z] — show the delta
```

### Step 2 — Pricing Model Design

**Option A — Outcome-Based Fixed**
```
Setup fee: $[X] (one-time, covers build + deploy)
Monthly: $[Y] (covers maintenance + results guarantee)
Outcome guarantee: [If X doesn't happen, we work free until it does]
```

**Option B — Usage-Based**
```
Per [unit of outcome]: $[X]
  Examples:
  - Per lead processed: $[X]
  - Per workflow automation run: $[X]
  - Per hour saved (measured): $[X]
Cap: $[monthly max] so client can budget
Floor: $[monthly min] so you can plan
```

**Option C — Revenue Share (highest trust, highest upside)**
```
% of measurable revenue lift
Only offer if: outcome is clearly measurable, client is trustworthy
Cap at: [X months or $Y total]
```

### Step 3 — Pricing Page Copy
```
HEADLINE: "Pay for results. Not hours."

TIER 1 — Starter: $[X]/month
  ✅ [Outcome 1]
  ✅ [Outcome 2]
  ✅ [Support SLA]
  Best for: [ICP sub-segment]

TIER 2 — Growth: $[Y]/month
  ✅ Everything in Starter
  ✅ [Outcome 3 — higher volume]
  ✅ [Outcome 4 — advanced feature]
  Best for: [ICP segment]

TIER 3 — Enterprise: Custom
  Contact us — [specific use case]

GUARANTEE BOX:
"If you don't [specific outcome] in [X days], we refund [Y]."
```

### Step 4 — Transition Script for Existing Clients
```
EMAIL SUBJECT: A change in how we work together (better for you)

"Hi [Name],

We've been working together for [X months] on an hourly basis. As our work has matured,
we can now guarantee specific outcomes — so we're moving to outcome-based pricing.

Here's what changes for you:
- You pay $[X]/month instead of [hourly]
- You're guaranteed [specific outcome]
- If we don't deliver, [guarantee language]

For you specifically, this means [calculate their personal savings/benefit].

Happy to jump on a quick call to walk through it. Worth 15 minutes?"
```

### Step 5 — Risk Mitigation
```
GUARANTEE DESIGN CHECKLIST:
  ✅ Is the outcome measurable? (yes/no — required for guarantee)
  ✅ What's the measurement method? (GA4, CRM, client's own reporting)
  ✅ What's the guarantee period? (30/60/90 days)
  ✅ What's the remedy? (refund / extra month free / credit)
  ✅ What exclusions? (client must provide X access / data)
```

## OUTPUT FORMAT
Pricing model design + pricing page copy + client transition email.
Save to: `~/Downloads/[AgencyName]-Outcome-Pricing-[Date].md`
