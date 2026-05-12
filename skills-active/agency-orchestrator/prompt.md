# agency-orchestrator — AI Agency Master Workflow
**Elementec Digital Agency | Full Pipeline Coordinator**

The master command that coordinates all agency operations — visual production, client acquisition, proposal writing, delivery, and billing. Routes to the right sub-skill automatically.

---

## USAGE
`/agency-orchestrator [task]`

**Auto-detects and routes:**
- "create [visual type] for [brand]" → `/elementec-visuals`
- "find clients for [niche]" → `/client-acquisition`
- "write proposal for [job]" → `/proposal-writer`
- "generate image [prompt]" → `/wan-image-gen`
- "full campaign for [brand]" → orchestrates ALL skills in sequence

---

## AGENT TEAM STRUCTURE

```
┌─────────────────────────────────────────────────────┐
│              AGENCY ORCHESTRATOR                     │
│         (Claude + OpenClaw + Agent37)               │
└──────────┬──────────────────────────────────────────┘
           │
    ┌──────┴───────┐
    │              │
    ▼              ▼
INTAKE AGENT   OUTREACH AGENT
(qualifies      (LinkedIn +
 leads)          cold email)
    │              │
    ▼              ▼
VISUAL AGENT   PROPOSAL AGENT
(Elementec      (personalized
 prompts +       winning
 Wan2.7)         proposals)
    │              │
    └──────┬───────┘
           │
    ▼──────┘
DELIVERY AGENT
(packages +
 invoices +
 follow-up)
```

---

## FULL CAMPAIGN WORKFLOW

When given: `/agency-orchestrator full campaign [brand] [brief]`

### Step 1 — Brief Extraction
- Extract: brand name, niche, target audience, color palette, key product
- Identify: campaign type needed (launch/retainer/one-off)
- Set pricing tier

### Step 2 — Visual Production (elementec-visuals)
Generate all 6 Elementec deliverables:
1. Campaign Moodboard
2. Launch Poster
3. Instagram Creative (3 variations)
4. Packaging Mockup
5. Finance/Analytics Dashboard (if relevant)
6. Brand Infographic

### Step 3 — Image Generation (wan-image-gen)
- Convert each Elementec prompt → Wan2.7 API call
- Batch generate all images
- Save to `~/Downloads/elementec-output/[brand]/`

### Step 4 — Delivery Package
- ZIP all images with source prompts
- Create delivery email template
- Generate invoice

---

## OPENCLAW AGENT CONFIG

For running as autonomous OpenClaw agent:

```yaml
# ~/.claude/agents/agency-agent.yaml
name: ElementecAgency
model: claude-sonnet-4-6
memory: true
tools:
  - wan_image_gen
  - elementec_prompts
  - apollo_prospecting
  - gmail_outreach
  - google_drive_upload
  - invoicing

workflows:
  new_client:
    trigger: "new client brief received"
    steps:
      - extract_brief
      - generate_visuals
      - package_delivery
      - send_proposal
      - create_invoice

  lead_outreach:
    trigger: "daily 9am IST"
    steps:
      - pull_prospects_from_apollo
      - personalize_messages
      - send_linkedin_connections
      - send_cold_emails
      - log_to_crm

  content_retainer:
    trigger: "weekly Monday"
    steps:
      - check_client_brief
      - generate_weekly_creatives
      - upload_to_gdrive
      - send_delivery_email
```

---

## SERVICE PACKAGES (ready to sell)

### Starter Package — $200
- 3 Instagram creatives
- 1 campaign moodboard
- Delivery: 48 hours

### Growth Package — $500
- Full Elementec suite (all 6 types)
- 3 variations each
- Source prompts included
- Delivery: 5 days

### Agency Retainer — $800/month
- 8 creatives/month
- 2 campaign moodboards
- Priority 24hr turnaround
- Monthly strategy call

### AI Agent Build — $1500 one-time + $200/mo
- Custom OpenClaw/Agent37 bot
- Telegram/WhatsApp integration
- Trained on client's brand
- 1 month support included

---

## OPENCLAW INTEGRATION

Your existing setup at `wss://openclaw-ba7f3aivag.h86.openclaw.agent37.com/gateway`:

```javascript
// Deploy agency agent to OpenClaw
const agentConfig = {
  name: "ElementecAgencyBot",
  channels: ["telegram", "whatsapp"],
  model: "claude-sonnet-4-6",
  skills: ["elementec-visuals", "client-acquisition", "proposal-writer"],
  memory: true,
  confirmRequired: ["send_email", "generate_invoice", "upload_file"]
}
```

Run: `openclaw deploy agency-agent.yaml` from `~/.claude/agents/`

---

## DAILY OPERATIONS CHECKLIST

**Morning (9am IST):**
- [ ] Check new Upwork job posts (5 proposals)
- [ ] Send 10 LinkedIn connections
- [ ] Send 20 cold emails (Apollo MCP)
- [ ] Check OpenClaw bot messages + respond

**Afternoon (2pm IST):**
- [ ] Work on active client deliverables
- [ ] Run `/elementec-visuals` for pending projects
- [ ] Upload completed work to Google Drive

**Evening (8pm IST — US overlap):**
- [ ] Check and respond to US/UK client messages
- [ ] Follow up on pending proposals
- [ ] Log completed work + income

---

## MONTHLY INCOME TARGETS

| Month | Target | Strategy |
|-------|--------|----------|
| Month 1 | $500 | 1 retainer + 2 one-off projects |
| Month 2 | $1000 | 2 retainers + 3 one-off |
| Month 3 | $2000 | 3 retainers + agent builds |
| Month 6 | $5000 | 5 retainers + 2 agent builds/mo |
