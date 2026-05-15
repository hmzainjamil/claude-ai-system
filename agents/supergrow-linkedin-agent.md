---
name: SuperGrow LinkedIn Agent
description: LinkedIn content creation, scheduling, and personal branding via Supergrow.ai patterns
triggers:
  - supergrow
  - linkedin content
  - linkedin scheduling
  - linkedin personal brand
  - hook generator
  - viral linkedin
  - carousel post
  - linkedin post ideas
---

# SuperGrow.ai Capability Stack (April 2026)

## Core Platform Features (mapped to local equivalents)

| Supergrow Feature | Local Equivalent | How to use |
|---|---|---|
| AI Post Writer | LinkedIn Content Agent (n8n) | Import linkedin_content_agent_hmz.json to n8n |
| Hook Generator | llm-burst "write 5 hooks for [topic] LinkedIn" | Runs Gemini+Groq+DeepSeek simultaneously |
| Post Scheduler | n8n Schedule Trigger (every 6h built-in) | LinkedIn Content Agent auto-schedules |
| Carousel Builder | canvas-design + canva-automation skills | Generate visual carousels |
| Analytics | linkedin-cli + posthog-automation | Track post performance |
| Idea Generator | llm-burst "10 LinkedIn post ideas for [niche]" | Free, instant |
| Ghostwriting | pd-linkedin-content-writer skill | HMZ's voice, calibrated |
| Profile Optimizer | pd-linkedin-profile-optimizer skill | Full profile audit |
| Content Repurposing | linkedin-personal-branding skill | Thread → carousel → email |

## HMZ LinkedIn Strategy (Pakistan-based, Global Clients)
- Niche: Google/Meta Ads, PPC, Performance Marketing
- Geo: UK, USA, Canada, Australia (NOT India, Pakistan mentions avoid)
- Voice: Expert, data-driven, no fluff
- Cadence: 1 post/day via n8n LinkedIn Content Agent (Gemini 2.0 Flash)
- Hook style: Controversy → Insight → CTA

## One-command LinkedIn post
```bash
~/.claude/bin/llm-burst "Write a viral LinkedIn post about [META ADS INSIGHT]. Pakistani PPC expert voice. Hook + 3 bullets + CTA. No hashtag spam."
```
