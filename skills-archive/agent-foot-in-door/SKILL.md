---
name: agent-foot-in-door
description: Packages ANY workflow automation as an "AI Agent" product for sales purposes. Creates pitch, demo script, pricing, objection handles, and email sequence. Uses "agent" terminology as a strategic foot-in-door even for standard automations.
allowed-tools: Read, Grep, Glob, Bash, WebFetch, WebSearch, Write
triggers: ["agent product", "sell automation as agent", "ai agent pitch", "foot in door", "agent offer", "sell ai agent", "automation as product", "position as ai", "ai agent sales"]
---

# /agent-foot-in-door — Package Any Automation as an AI Agent Product

> **Trigger**: "sell automation as agent" / "agent product" / "AI agent pitch" / "foot in door"
> **No command needed** — auto-activates.

## WHAT THIS DOES

Takes ANY workflow automation (Zapier, n8n, Make, custom script, chatbot) →
Packages it as a sellable "AI Agent" product →
Produces: pitch deck outline, demo script, pricing, email hooks, objection handles.

**Key insight (Ashar Samdani):** "Agent" is a foot-in-the-door term. Even if the actual solution is a standard workflow, positioning it as an agent gets meetings. Once inside, you expand.

## INPUT — DESCRIBE YOUR AUTOMATION
```
What it does: [e.g., "sends follow-up emails based on CRM stage changes"]
Tech stack: [e.g., n8n + Gmail + HubSpot]
Who benefits: [e.g., sales teams at SaaS companies, 10–50 reps]
Time saved: [e.g., 3 hours/day per rep]
Current pain: [e.g., reps forget to follow up, leads go cold]
```

## EXECUTION WORKFLOW

### Step 1 — Agent Identity Design
```
AGENT NAME: [Memorable, outcome-focused]
  Example: "FollowUp.AI" / "LeadKeeper Agent" / "Pipeline Guardian"

AGENT TAGLINE: "[Does X] so your team [gets Y] automatically."
  Example: "Follows up with every lead automatically so your team closes more without chasing."

AGENT PERSONA (for sales materials):
  - "Always on" (24/7)
  - "Never forgets" a follow-up
  - "Learns" which leads are hot (even if it's just a filter)
  - "Reports" weekly (even if it's a Slack digest)
```

### Step 2 — Pitch Package
```
ELEVATOR PITCH (30 seconds):
"We built an AI agent that [does X] for [ICP]. Most of our clients were [pain].
After deploying the agent, they [result]. We can set it up for your team in [X] days."

DEMO SCRIPT (5 minutes):
  Minute 1: Show the problem (screenshot of messy inbox / missed follow-ups)
  Minute 2: Show the agent dashboard / trigger (Zapier/n8n flow)
  Minute 3: Show the output (email sent, CRM updated, Slack notified)
  Minute 4: Show the result (client testimonial or metric)
  Minute 5: Pricing + next step

SLIDE DECK OUTLINE (5 slides):
  1. Problem: [Pain, quantified]
  2. Solution: [Agent name + what it does]
  3. How it works: [Simple 3-step diagram]
  4. Results: [Case study or projection]
  5. Pricing + CTA
```

### Step 3 — Pricing
```
ENTRY PACKAGE: $[1,500–3,000] — Setup + 30-day support
  Includes: build, test, deploy, train 1 person, 30-day bug fix

GROWTH PACKAGE: $[500–1,000/month] — Ongoing management + upgrades
  Includes: monitoring, updates, new triggers, monthly report

ENTERPRISE: Custom — multi-team deployment, custom integrations

PRICING PSYCHOLOGY:
  - Lead with outcome value (3 hrs/day × $50/hr × 250 days = $37,500/year)
  - Position your price against that: "For $3,000 setup, you get $37,500 back"
  - Always offer a discovery call as zero-risk entry point
```

### Step 4 — Cold Email Hooks (3 variants)
```
HOOK 1 — Pain:
Subject: [Company] still doing [manual task] manually?
"Hey [Name], noticed [Company] uses [tool] — most [ICP] teams waste [X hrs/week] on [task].
We built an agent that handles it automatically. Booked 2 clients last month in [their industry].
Worth a 15-min call to see if it fits?"

HOOK 2 — Result:
Subject: How [Similar Company] automated [outcome]
"[Name], we helped [anonymized similar company] automate [outcome] in 14 days.
They were losing [X leads/deals/hours] before. The agent fixed it.
Can I show you how it works in 15 mins?"

HOOK 3 — Curiosity:
Subject: AI agent for [their job title]?
"[Name], we built an AI agent specifically for [ICP] that [does X].
[Company] might already be doing this manually — curious what your setup looks like.
15 mins?"
```

### Step 5 — Objection Handles
```
"We already have automation tools."
→ "Great — this agent works WITH your existing stack, not instead of it. We layer on top of [Hubspot/Salesforce/etc]."

"How is this different from Zapier?"
→ "Zapier moves data. Our agent makes decisions — it knows WHEN to trigger, not just IF. That's the AI layer."

"Is it really AI?"
→ "It uses AI for [specific part — prioritization/personalization/routing]. The rest is rock-solid automation. The result: it actually works."

"Too expensive."
→ "At [price], you're getting [X hrs/week] back. At [hourly rate], that's [annual value]. Most clients see ROI in 6 weeks."
```

## EXPANSION STRATEGY (the real goal)
```
First sale: 1 agent → foot in the door
Expansion: audit the other 3–5 broken workflows → sell next agent
Target: become the "agent vendor" for the company — ERP-like relationship
```

## OUTPUT FORMAT
Full agent product kit: pitch, demo script, pricing page brief, 3 email hooks, objection sheet.
Save to: `~/Downloads/[AgentName]-Sales-Kit-[Date].md`
