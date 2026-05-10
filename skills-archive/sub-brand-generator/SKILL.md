---
name: sub-brand-generator
description: Creates a micro-brand for a specific automation niche — name, positioning, one-liner, landing page brief, social handles, domain suggestions, and separation strategy from parent brand. Ashar Samdani "safe test" method.
allowed-tools: Read, Grep, Glob, Bash, WebFetch, WebSearch, Write
triggers: ["sub brand", "sub-brand", "micro brand", "niche brand", "separate brand", "new brand", "spin off", "brand for niche", "test a brand"]
---

# /sub-brand-generator — Create a Niche Micro-Brand

> **Trigger**: "sub-brand" / "micro brand" / "separate brand" / "niche brand" / "spin off"
> **No command needed** — auto-activates.

## WHAT THIS DOES

Creates a complete micro-brand for a specific automation niche —
without risking the parent brand. Test, learn, scale if it works.

**Why sub-brand vs. main brand?**
- Protects main brand reputation during niche experiments
- Allows hyper-specific positioning (can't do "auto liability insurance AI" on a generalist site)
- Easy to spin down if niche doesn't convert
- Can be sold/spun off later as a separate product

## INPUT NEEDED
```
Parent agency name: [X]
Target niche: [e.g., "independent insurance brokers, US-based"]
Core product: [e.g., "lead follow-up automation agent"]
Price point: [e.g., "$3,000 setup + $500/month"]
Tone: [professional/casual/technical]
```

## EXECUTION WORKFLOW

### Step 1 — Brand Name Generation (10 options)
```
NAMING FORMULAS:
  [Outcome].[io/ai/co]  → e.g., FollowedUp.ai
  [Niche][Function]     → e.g., BrokerBot, InsureFlow
  [Verb][It]            → e.g., AutoClose, AutoFollow
  [Animal/Mascot][AI]   → e.g., HoundAI, FalconFlow

OUTPUT: 10 name options + domain availability check
SHORTLIST: Top 3 with rationale
RECOMMENDED: #1 pick + why
```

### Step 2 — Brand Identity
```
NAME: [chosen name]
TAGLINE: "[Specific outcome] for [specific ICP]. Automated."
CATEGORY: [what category do you want to own?]
  Example: "The AI follow-up agent for independent insurance brokers"

BRAND PERSONALITY:
  Tone: [e.g., "confident, specific, no-fluff"]
  Voice: [e.g., "talking to a busy ops manager who's seen too many promises"]
  Avoid: [e.g., "generic AI buzzwords, vague claims"]

COLOR DIRECTION: [based on niche psychology]
  Finance/Insurance: navy, slate, white (trust)
  Real Estate: gold, black, white (premium)
  SaaS/Tech: electric blue, dark, white (modern)
  Healthcare: teal, white, soft grey (clean)
```

### Step 3 — Positioning Document
```
POSITIONING STATEMENT:
"For [specific ICP], [Brand Name] is the [category] that [key benefit]
unlike [alternative], we [key differentiator]."

WEBSITE HEADLINE: [Pain-focused, specific]
  Bad: "AI automation for your business"
  Good: "Insurance brokers close 30% more leads — without hiring more staff"

WEBSITE SUBHEAD: [Mechanism + proof]
  "Our follow-up agent contacts every lead within 5 minutes. Automatically. 24/7."

3 CORE MESSAGES:
  1. [Problem message]
  2. [Solution mechanism]
  3. [Proof/result]
```

### Step 4 — Digital Presence Checklist
```
DOMAIN: [brandname.ai / .io / .co] — check namecheap/godaddy
  Fallback: [brandname-[niche].com]

SOCIAL HANDLES (claim all even if not using):
  LinkedIn Company Page: /company/[brandname]
  Twitter/X: @[brandname]
  Instagram: @[brandname]ai

LANDING PAGE BRIEF (1-page only to start):
  Section 1: Headline + subhead + CTA button
  Section 2: Problem (3 bullets)
  Section 3: Solution (how it works, 3 steps)
  Section 4: Social proof (1 testimonial or "pilot client" result)
  Section 5: Pricing (or "Book a call")
  Section 6: Guarantee

EMAIL DOMAIN: [brand@brandname.ai]
  Set up: Google Workspace ($6/month)
  Warm up: 2 weeks before any outreach
```

### Step 5 — Separation Strategy
```
WHAT TO SEPARATE:
  ✅ Domain + website (always separate)
  ✅ Email infrastructure (separate inboxes)
  ✅ Social presence (separate pages)
  ✅ LinkedIn outreach (use personal profile tied to sub-brand)

WHAT TO KEEP CONNECTED:
  ✅ Your personal LinkedIn (be transparent — "Founder of [ParentAgency] + [SubBrand]")
  ✅ Team (same people, different hats)
  ✅ Delivery ops (same systems, different brand on the front)

WHEN TO MERGE BACK:
  If niche generates >$10K MRR → decision: keep separate or fold into main brand
  If < results in 90 days → sunset quietly, learn, pivot
```

## OUTPUT FORMAT
Brand kit: name options, positioning doc, domain suggestions, landing page brief, social handle list.
Save to: `~/Downloads/[BrandName]-SubBrand-Kit-[Date].md`
