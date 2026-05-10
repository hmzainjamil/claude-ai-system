---
name: agency-rescue
description: 6-month survival plan for services agencies facing AI disruption or slow growth. Week-by-week execution: niche selection → ICP → productized offer → outreach → brand positioning. Based on Ashar Samdani framework.
allowed-tools: Read, Grep, Glob, Bash, WebFetch, WebSearch, Write, Agent
triggers: ["agency rescue", "6 month plan", "save my agency", "agency survival", "rescue my business", "slow down", "no clients", "losing clients", "runway", "services not selling", "staff augmentation not working"]
---

# /agency-rescue — 6-Month Agency Survival Plan

> **Trigger**: "save my agency" / "6 month plan" / "agency survival" / "no clients" / "losing clients"
> **No command needed** — auto-activates.

## WHAT THIS DOES
Produces a complete 6-month week-by-week rescue plan for a struggling services agency.
Output: prioritized actions, templates, outreach scripts, positioning docs.

## DIAGNOSIS FIRST (answer these or I'll infer)
1. Team size + monthly burn rate
2. Current services sold (staff aug / custom dev / automation / etc)
3. Last 5 clients — industry + deal size
4. Current monthly revenue vs target
5. Runway remaining (months)
6. What outreach have you tried?

## THE 6-MONTH PLAN

### MONTH 1 — STOP THE BLEEDING + FIND THE SIGNAL
```
Week 1: Customer matrix (run /customer-matrix on all past clients)
Week 2: Pick ONE niche. Kill all others for now. Say "no" to out-of-niche work.
Week 3: Productize ONE offer for that niche (run /service-productizer)
Week 4: Build proof — write 1 case study, update LinkedIn + website headline

DELIVERABLES BY EOW4:
  ✅ Niche chosen (micro-ICP defined)
  ✅ 1 productized package designed + priced
  ✅ 1 case study written
  ✅ LinkedIn + website updated for niche
  ✅ Apollo/LinkedIn search query built
```

### MONTH 2 — LAUNCH OUTREACH
```
Week 5:  Set up email infrastructure (Smartlead/Instantly, 3 inboxes, warm-up)
Week 6:  Write 3 cold email variants + LinkedIn DM sequence
Week 7:  Launch — target 200 emails/day minimum (1,000/week)
Week 8:  Review open/reply rates. A/B test subject lines.

DELIVERABLES:
  ✅ Email infra live (3 warmed inboxes)
  ✅ 3 email variants + 1 LinkedIn sequence
  ✅ 1,000+ emails sent
  ✅ Replies tracked in simple CRM (Notion/Airtable)
  ✅ First calls booked
```

### MONTH 3 — DOUBLE DOWN ON WHAT WORKS
```
Week 9:  Analyze which email angle gets replies. Kill the other two.
Week 10: Add LinkedIn outreach (founder posts + DMs). 1 post/day.
Week 11: Launch Meta ad experiment ($10–20/day, productized offer, lead form)
Week 12: Close first 2–3 productized deals. Document delivery process.

DELIVERABLES:
  ✅ Winning email angle identified + scaled
  ✅ LinkedIn content rhythm established
  ✅ First Meta ad live
  ✅ 2–3 deals closed
  ✅ Delivery checklist documented
```

### MONTH 4 — SYSTEMIZE + SCALE
```
Week 13: Build sub-brand for niche (run /sub-brand-generator) if niche is working
Week 14: Hire/assign 1 person to delivery. Founder stays in sales.
Week 15: Build referral ask into delivery process ("Who else do you know with this problem?")
Week 16: Launch second niche experiment (test #2 from customer matrix)

DELIVERABLES:
  ✅ Sub-brand live (optional but powerful)
  ✅ Delivery systemized (SOP doc)
  ✅ Referral loop built in
  ✅ Niche #2 outreach started (separate from main)
```

### MONTH 5 — BUILD RECURRING REVENUE
```
Week 17: Productize a retainer offer (outcome-based pricing, run /outcome-pricing)
Week 18: Pitch retainer to all Month 3 clients
Week 19: SEO + content — 4 articles targeting niche pain keywords
Week 20: Webinar or workshop for niche (lead magnet, builds list)

DELIVERABLES:
  ✅ Retainer offer designed + priced
  ✅ At least 1 retainer signed
  ✅ 4 SEO articles published
  ✅ Webinar/workshop planned
```

### MONTH 6 — OPTIMIZE + PROJECT NEXT 6 MONTHS
```
Week 21: Full funnel audit — where are leads dropping off?
Week 22: Fix biggest drop-off point
Week 23: Hire for the role that's bottlenecking growth
Week 24: Project Month 7–12 plan with new baseline

DELIVERABLES:
  ✅ Funnel audit complete
  ✅ Team structure for scale
  ✅ Month 7–12 plan written
  ✅ Monthly recurring revenue target set
```

## FOUNDER RULES (NON-NEGOTIABLE)
```
❶ Founder leads sales for all of Month 1–3. No delegation.
❷ "No" to out-of-niche work in Month 1–2 unless it pays 2x your rate.
❸ Email volume = truth. Less than 500 emails/week = not enough data.
❹ Pick 3 niches to bet on. Go deep on 1. Surface-test the other 2.
❺ If a channel gets replies in 4 weeks, double it. If not, cut it.
```

## OUTPUT FORMAT
Full 6-month Gantt-style plan + week-by-week checklist.
Save to: `~/Downloads/[AgencyName]-Rescue-Plan-[Date].md`
