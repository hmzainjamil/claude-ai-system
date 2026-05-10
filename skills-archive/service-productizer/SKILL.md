---
name: service-productizer
description: Transforms vague agency capability into a fixed-price productized service package — scope, deliverables, pricing, landing page brief, and sales one-liner. Based on Ashar Samdani / DotCom Secrets frameworks.
allowed-tools: Read, Grep, Glob, Bash, WebFetch, WebSearch, Write
triggers: ["productize", "productized service", "fixed price package", "sell outcomes", "package my service", "stop selling hours", "service package", "automation package", "workflow package"]
---

# /service-productizer — Turn Any Capability Into a Product

> **Trigger**: "productize my service" / "create a fixed-price package" / "stop selling hours" / "package X as a product"
> **No command needed** — auto-activates on these phrases.

## WHAT THIS DOES

Takes ANY agency capability → produces a complete productized service:
- Fixed name + one-liner
- Defined scope (what's IN, what's OUT)
- Fixed price with rationale
- Delivery timeline
- Landing page brief
- Email pitch (3 sentences)
- Objection handles (top 3)

## EXECUTION WORKFLOW

### Step 1 — Capability Extraction
Ask (or infer from context):
1. What does your agency actually DO well? (raw capability)
2. Who have your last 5 clients been? (industry, role, pain)
3. What outcome did they pay for? (not the work — the result)
4. How long does delivery actually take?

### Step 2 — Package Design

**Output structure:**
```
PRODUCT NAME: [Verb] + [Outcome] + [Timeframe]
Example: "Automate Your Lead Follow-Up in 14 Days"

ONE-LINER: We [action] for [ICP] so they [outcome] without [pain].
Example: "We automate follow-up workflows for insurance brokers so they close 30% more leads without hiring more staff."

WHAT'S INCLUDED:
  ✅ [Deliverable 1 — specific, tangible]
  ✅ [Deliverable 2]
  ✅ [Deliverable 3]
  ✅ [Deliverable 4 — max 5 items]

WHAT'S NOT INCLUDED:
  ❌ [Exclusion 1]
  ❌ [Exclusion 2]

PRICE: $[X] fixed / [payment structure]
TIMELINE: [X] days from kickoff to delivery
GUARANTEE: [optional — e.g., "if not live in 14 days, we refund day 15+"]

LANDING PAGE BRIEF:
  Headline: [pain-focused]
  Subhead: [outcome-focused]
  CTA: [specific action]
  Social proof: [type needed — case study / testimonial / logo]

3-SENTENCE EMAIL PITCH:
  [Problem sentence] [Proof sentence] [CTA sentence]

TOP 3 OBJECTIONS + HANDLES:
  1. "Too expensive" → [handle]
  2. "We do this in-house" → [handle]
  3. "How do I know it'll work?" → [handle]
```

### Step 3 — Value Ladder Position
Map the package into the DotCom Secrets Value Ladder:
```
ENTRY: $500–2,000 — [discovery/audit package]
CORE:  $3,000–8,000 — [THIS productized service]
ASCEND: $10,000+ — [ongoing retainer / custom build]
```

### Step 4 — Test Before Launch
Before going live:
- [ ] Can you explain the package in one sentence?
- [ ] Does the scope fit in the price?
- [ ] Would YOU buy this if you had the problem?
- [ ] Do you have ONE case study or proof point?

## OUTPUT FORMAT
Single document, ready to paste into landing page + email sequence.
Save to: `~/Downloads/[AgencyName]-Productized-Package-[Date].md`
