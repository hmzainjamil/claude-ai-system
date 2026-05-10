---
name: client-hunting
description: Client hunting via Claude Connectors (Indeed + Yelp + Direct Outreach). Turns job posts into warm freelance leads. Auto-activates on: "find clients", "client hunt", "job leads", "indeed connector", "find companies hiring".
type: active
triggers: ["find clients", "client hunt", "job leads", "indeed connector", "find companies hiring", "hunt for clients", "freelance leads", "outreach leads", "yelp leads", "local service clients"]
---

# Client Hunting with Claude Connectors (Indeed + Direct Outreach)

## Core Logic
Target **companies actively hiring** for your skill = they have budget + immediate need + decision-maker thinking about it now.
Job posts = warm leads, not cold outreach.

---

## Setup (One-time)
1. Claude sidebar → "+" → Connectors → Browse → **Indeed** → Install → Link Gmail/Indeed
2. Free plan: 1 connector active. Paid: multiple simultaneous (Indeed + Yelp + others)

---

## Base Prompt Template (Indeed Connector Active)

```
"Use the Indeed connector. Give me a list of 5 companies that are based in [region]
and are actively hiring [your role/skill]. The company must have an [industry condition].
Include: company name, job title, short description, direct Indeed job link."
```

---

## Filters

| Filter | How to Add |
|---|---|
| Location | "based in [city/state/country]" |
| Remote | "listing must mention 'remote' or 'work from home'" |
| Vertical | "e-commerce", "HVAC", "SaaS", "local service business" |
| Budget signal | "company has 10-200 employees" |

---

## Ready-to-Use Prompts

**1. US Remote Digital Marketing:**
> "Use the Indeed connector. Give me 5 companies in the United States actively hiring digital marketers. Prioritize remote/WFH roles for e-commerce or DTC businesses. Include company name, job title, summary, and Indeed URL."

**2. Local Services (PPC):**
> "Use the Indeed connector. Find 5 HVAC or plumbing companies in Florida hiring for PPC / Google Ads / lead generation. Listing should mention remote, hybrid, or flexible. Return company name, job title, description, job URL."

**3. City-Level Specialist:**
> "Use the Indeed connector. List 5 companies in Dallas, Texas hiring a Performance Marketing Specialist, PPC Specialist, or Paid Social Specialist. Note if remote/hybrid."

**4. Yelp — Local Service Businesses Running Ads:**
> "Find 5 solar installation companies in California on Yelp that are running Yelp Ads. Give me business name, Yelp URL, website URL, and any ad indicators."

---

## Converting a Job Post → Client

1. Open the Indeed job link Claude returns
2. Find company website → About / Team / Leadership page
3. Find owner / marketing director / decision-maker
4. Contact via: contact form → public email → LinkedIn DM

**Ask Claude to help:**
> "Here is the company: [URL]. Help me identify the owner or marketing decision-maker and draft a short outreach email referencing their current job post."

---

## Outreach Script Template

> "I saw you're hiring a [role from Indeed] on Indeed. I specialize in [your skill] for [their industry] and have helped similar businesses achieve [concrete result].
>
> Rather than waiting weeks to hire and onboard, I can [specific quick win: audit / campaign setup / first deliverable] in the next [X days], on a flexible 1099 basis.
>
> If helpful, I'd be happy to send 2–3 tailored ideas for [business name] or jump on a quick call."

---

## Workflow

```
1. Activate Indeed connector in Claude
2. Run filtered prompt (region + role + vertical + remote)
3. Get company list + job URLs
4. Find website + decision-maker for each
5. Contact via email/form/LinkedIn — reference their hiring need
6. Optional: Add Yelp layer for businesses already running ads
```

---

## Vertical-Specific Hunting

| Vertical | Signal to Look For | Platform |
|---|---|---|
| E-commerce/DTC | Hiring "paid media", "growth marketer" | Indeed |
| Local services | HVAC/plumbing/roofing/solar hiring "lead gen" | Indeed + Yelp |
| SaaS | Hiring "demand gen", "performance marketer" | Indeed + LinkedIn |
| Agencies | Hiring "PPC specialist" (they need white-label) | Indeed |

---

## Notes
- Free Claude: 1 connector active at a time
- Paid Claude: multiple connectors simultaneously (Indeed + Yelp + others)
- Each job post = warm lead (they have budget, active need, decision-maker available)
- Combine Indeed (intent) + Yelp (ad spend signal) for highest-quality leads
