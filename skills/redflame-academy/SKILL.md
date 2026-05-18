# RedFlame AI Workflow Academy — Full Automation Stack

## WHAT THIS IS (from actual content)
Teaching community: **1 image → full AI commercial video** using structured storyboard workflow.
Core tool: **Weavy** (workflow orchestration) + **Seedance 2** (video generation).
Subscription: €49/month. Price rises as community grows.
Promise: Stop randomly generating AI outputs. Start building controlled production systems.

## WHAT MEMBERS LEARN
- 35+ structured workflow lessons (updated weekly)
- 10+ full production pipelines (real commercial use cases)
- Prompt system building for image, video & animation
- Scalable content systems: idea → concept → execution → output
- Automated AI pipelines
- Visual consistency systems (characters, scenes, products, styles)
- Cinematic visuals + professional-level output
- Weekly live calls, Q&A, feedback
- Real project breakdowns + hands-on guidance

## THE CORE WORKFLOW (8 Steps — "1 Image → AI Commercial")

### Step 1 — Upload Product Image + Short Description
- Input: 1 product image (or multiple for higher consistency)
- Works for: luxury products, fashion, jewelry, tech, any commercial product
- Also provide: short creative brief (atmosphere + style — can be 2 sentences or detailed)

### Step 2 — System analyzes product + description
- Weavy workflow ingests image + text
- Prepares foundation for storyboard generation

### Step 3 — Automatic Prompt Generation
- Click "Run Model"
- AI auto-generates structured storyboard prompt from product + description
- No manual prompt writing needed

### Step 4 — 12-Frame Cinematic Storyboard
- AI generates 12-panel contact sheet (16:9 each)
- Connected visual storytelling
- Matching atmosphere, coherent transitions, product-focused compositions
- Controls: shot progression, pacing, visual consistency, camera logic, cinematic flow
- Layout reads left→right, top→bottom (no numbers/labels — pure visual sequence)

### Step 5 — Character Generation (Optional)
- Describe character → AI generates:
  - Full body views
  - Facial close-ups
  - Multiple angles
  - Detailed character grids
- Result: reusable consistent identity across entire campaign (no random faces)

### Step 6 — Auto Animation Prompting for Seedance 2
- Do NOT write animation prompts manually
- Custom-built system prompt analyzes:
  - Storyboard frames
  - Product
  - Visual progression
  - Scene descriptions
- Auto-generates cinematic animation prompt for Seedance

### Step 7 — One-Click Pipeline Execution
- Select entire pipeline → "Run Selected"
- Auto-executes in sequence:
  1. Prompt generation
  2. Storyboard creation
  3. Scene preparation
  4. Animation prompting
  5. Seedance video generation
- Zero manual intervention after trigger

### Step 8 — Final Commercial Video Output
- Structured, intentional, consistent commercial
- Not random AI output — controlled cinematic sequence
- Ready for: product commercials, fashion campaigns, luxury ads, social media

---

## MASTER STORYBOARD PROMPT TEMPLATE (extracted from PDF)

```
Create a 12-frame storyboard contact sheet for a short product advertisement,
designed as a clean visual overview for video development.

Use the uploaded product image as the exact product reference.
Preserve the product's shape, packaging, label design, colors, logo placement,
proportions, materials, finish, and key branding details consistently in every
frame where it appears. Do not redesign, simplify, rename, recolor, or invent
new label elements.

Use the uploaded style reference image as the visual-style guide. Apply its
mood, framing logic, lighting language, color treatment, texture, camera feel,
polish level, and overall ad aesthetic across the storyboard.

[BRAND CONCEPT]: {product_description}

Visual style: {visual_style — e.g. cinematic, handheld, natural light, bold colors}

Video intent: The storyboard should feel like a real commercial sequence designed
for a future video edit. Each panel composed as a believable 16:9 widescreen shot.

Storyboard format: One clean 12-panel contact sheet. Consistent spacing.
No frame numbers, captions, arrows, callouts, annotation marks, or labels.

Panel aspect-ratio rule: Every individual panel must be framed as a distinct
16:9 widescreen shot.

Sequence logic: Communicate progression through layout, action, screen direction,
subject movement, product interaction, and visual continuity — not numbering.

Story arc: {story_arc — e.g. hero shot build, lifestyle payoff, brand world reveal}

Frame-by-frame direction:
01 — {establishing shot}
02 — {product close-up}
03 — {character + product medium shot}
04 — {wide lifestyle shot}
05 — {detail/texture close-up}
06 — {character action shot}
07 — {environment/context wide shot}
08 — {product hero shot}
09 — {emotional payoff medium}
10 — {secondary product detail}
11 — {pre-resolution shot}
12 — {commercial closing frame — intentional, memorable, brand-resolving}

Composition rules:
- Vary shot size, lens feel, angle, camera perspective throughout
- Product visible often enough for branding, integrated naturally
- Think like a director planning a short ad
- Final frame: deliberate commercial closing (hero shot / use-case payoff /
  emotional payoff / brand-world closing / end-card composition)

Output rules: Output only the final polished prompt. No internal instructions.
No placeholders unless truly needed. No follow-up questions.
Make reasonable creative decisions. Stay faithful to product image + style ref.
```

---

## AUTOMATION PIPELINE (Claude Code wiring)

### Tools Used in Actual Workflow
| Tool | Role |
|---|---|
| **Weavy** | Workflow orchestration — connects all steps |
| **Seedance 2** | AI video generation from storyboard frames |
| **Image generator** (GPT-4o / Gemini / DALL-E 3) | 12-frame storyboard creation |
| **Kimi K2.5 / Claude** | Prompt generation + storyboard logic |

### Our Equivalent Pipeline (from existing inventory)

| Weavy Step | Our Tool | Command |
|---|---|---|
| Upload + ingest | Local file + Kimi K2.5 | `llm-burst --models kimi-k2` |
| Auto prompt gen | Kimi K2.5 | API call with storyboard template |
| 12-frame storyboard | GPT-4o image / DALL-E 3 / Gemini | `openai-image-gen` skill |
| Character gen | Higgsfield Soul 2 / Nano Banana | `higgsfield-ai` skill |
| Animation prompt | Kimi K2.5 (auto) | Template injection |
| Video generation | Seedance 2 via KIE.ai | `kie-ai-ad-builder` repo |
| One-click pipeline | MAE run | `mae run "redflame campaign [product]"` |

### KIE.ai → Seedance 2 Connection
```bash
# KIE.ai supports Seedance 2 directly
cd ~/installed-repos/ads-creative/kie-ai-ad-builder
# Set KIE_API_KEY in ~/.zshrc
# Trigger: "kie video" / "seedance" / "kie ad builder"
```

---

## MAE COMMANDS

```bash
# Full commercial from 1 image
mae run "redflame commercial [product_name] [image_path]"

# Generate storyboard only
mae run "redflame storyboard [product_name] [brief]"

# Generate character sheet
mae run "redflame character [description]"

# Full weekly content batch
mae run "redflame weekly content"

# Revenue + community ops
mae run "redflame daily ops"
```

---

## CONTENT STRATEGY (what RedFlame teaches publicly)

Hook formula used:
- "Playing with AI" (random outputs, wasting time) vs "Working with AI" (structured systems)
- Pain: most creators don't control AI properly
- Solution: storyboard-first workflow = predictable cinematic output
- CTA: Join RedFlame AI Workflow Academy — €49/month

Distribution:
- LinkedIn: "Playing vs Working with AI" angle
- Instagram: Before/after carousels (random AI output vs storyboard-controlled)
- YouTube/TikTok: Workflow breakdown videos
- Email: Weekly lesson + workflow teardown

---

## PAPERCLIP EMPLOYEES (RedFlame department)

| Employee | Role | Tools |
|---|---|---|
| Storyboard Director | 12-frame storyboard generation per client brief | Kimi K2.5 + image gen |
| Cinematic Animator | Seedance 2 video generation from storyboard | KIE.ai / Higgsfield |
| Content Factory | Weekly lesson + social content | Kimi + postiz |
| Acquisition Manager | Meta/Google ads driving €49/mo signups | Meta Ads MCP |
| Revenue Analyst | MRR, churn, engagement tracking | Stripe + Brevo |

---

## MISSING INVENTORY (blockers)

| Missing | Priority | Fix |
|---|---|---|
| **Weavy account** | 🔴 HIGH — core orchestration tool | Sign up at weavy.com |
| **Seedance 2 API / KIE.ai key** | 🔴 HIGH — video generation | kie.ai → API settings |
| **BREVO_API_KEY** | 🔴 HIGH — email sequences | brevo.com free tier |
| **STRIPE_SECRET_KEY** | 🔴 HIGH — €49/mo payments | Stripe Dashboard |
| **GoKollab API** | 🟡 MED — member enrollment | Contact gokollab.com |
| **GPT-4o image gen key** | 🟡 MED — storyboard frames | OpenAI API (OPENAI_API_KEY exists?) |
| **SLACK_WEBHOOK_REDFLAME** | 🟡 MED — ops alerts | Slack → new channel → webhook |

---

## AUTO-ACTIVATION KEYWORDS
`redflame` · `weavy workflow` · `storyboard commercial` · `1 image to commercial` ·
`seedance` · `ai commercial workflow` · `12 frame storyboard` · `ai ad from image` ·
`kollab academy` · `€49 community` · `playing vs working with ai`
