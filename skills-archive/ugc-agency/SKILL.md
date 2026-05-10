# UGC Agency — AI Ad Production Skill (Arcads + Claude Code)

## Trigger Phrases (auto-activates on any of these)
- "ugc ads", "ugc agency", "arcads", "ai actors", "ai ugc"
- "generate ugc", "ugc video", "ugc brief", "ugc batch"
- "ai ad videos", "ugc retainer", "ugc pipeline"
- "generate 20 ads", "batch ads", "actor selection"
- "ai video ads", "ugc scripts", "lip sync ads"

---

## OVERVIEW

One prompt → 20 finished UGC ads. No actors. No studio. No editor.

| Tool | Role |
|---|---|
| **Arcads API** | AI actor library + lipsync + render engine |
| **Claude Code** | Script writing + actor selection + job orchestration |
| **arcads-claude-code skills** | Pre-built agent for the full pipeline |

**Agency math:** $1,500/mo in · ~$150/mo in tools · **90% gross margin**

---

## SETUP (one-time)

### 1. Get Arcads API Key
- Go to **arcads.ai** → create account → API settings → copy key
- Free tier: enough credits to test end-to-end

```bash
export ARCADS_API_KEY="your-key-here"
echo 'export ARCADS_API_KEY="your-key-here"' >> ~/.zshrc
```

### 2. Install Skills Repo (already cloned)
```bash
# ALREADY INSTALLED at:
ls ~/installed-repos/ads-creative/arcads-claude-code/
# AGENTS.md · CLAUDE.md · README.md · scripts/ · shared/ · references/

# Run setup to configure API key:
cd ~/installed-repos/ads-creative/arcads-claude-code
./scripts/setup.sh
```

### 3. Get Arcads API Key
- Sign up: **arcads.ai** (free tier to test)
- API key: **app.arcads.ai/settings/api**
- Add to env: `export ARCADS_API_KEY="your-key-here"`

---

## WORKFLOW — 4 STEPS

### STEP 1 — WRITE THE BRIEF (3 sentences)
```
Template:
"Product is [X]. Audience is [Y who care about Z].
Offer is [price/promo/CTA].
Generate 20 UGC ads — different hooks, different actors, different angles."
```

**Example (works immediately):**
> "Product is a $29 magnesium sleep supplement. Audience is stressed founders 25–40 who can't fall asleep. Offer is 30% off the first bottle with free shipping. Generate 20 UGC ads — different hooks, different actors, different angles."

Rules for clean briefs:
- State the PRICE (anchors hooks)
- State the PAIN (what keeps them up at night)
- State the CTA (what you want them to do)
- Vague brief → vague hooks → bad ads

### STEP 2 — CLAUDE WRITES 20 SCRIPTS
Claude auto-generates hook variations:
- Testimonial ("I haven't slept this well in 3 years...")
- Direct response ("If you're waking up at 3am...")
- Pattern interrupt ("Stop taking melatonin — here's why...")
- Problem/agitate/solve ("Founders work 16 hours then can't sleep...")
- Social proof ("10,000 people have switched to this...")

Each script: 30–60 seconds, hook in first 3 words.

### STEP 3 — ACTOR SELECTION + PARALLEL RENDER
Claude matches each script to an Arcads actor:
- Serious script → authoritative actor
- Casual testimonial → relatable peer
- Young audience → younger actor
- B2B → professional appearance

Then fires all 20 jobs to Arcads **simultaneously** (parallel API calls).
Render time: ~10–15 minutes for 20 videos.

### STEP 4 — COLLECT OUTPUT
```
~/ugc-output/
├── hook_01_testimonial_actor_sarah.mp4
├── hook_02_direct_response_actor_mike.mp4
├── hook_03_pattern_interrupt_actor_james.mp4
...
└── hook_20_social_proof_actor_elena.mp4
```

Drag straight into Meta Ads Manager. Done.

---

## ARCADS API — DIRECT USAGE

```python
import anthropic, requests, os, time

ARCADS_KEY = os.environ["ARCADS_API_KEY"]
BASE = "https://api.arcads.ai/v1"

def generate_ugc_ad(script: str, actor_id: str) -> dict:
    """Fire a single UGC render job"""
    r = requests.post(f"{BASE}/videos/generate",
        headers={"Authorization": f"Bearer {ARCADS_KEY}"},
        json={"script": script, "actor_id": actor_id, "format": "mp4"})
    return r.json()  # returns {"job_id": "...", "status": "queued"}

def poll_job(job_id: str, max_wait=600) -> str:
    """Poll until video ready, return download URL"""
    start = time.time()
    while time.time() - start < max_wait:
        r = requests.get(f"{BASE}/videos/{job_id}",
            headers={"Authorization": f"Bearer {ARCADS_KEY}"})
        data = r.json()
        if data["status"] == "completed":
            return data["download_url"]
        time.sleep(15)
    raise TimeoutError(f"Job {job_id} timed out")

def batch_generate(briefs: list[dict], output_dir="~/ugc-output"):
    """briefs = [{"script": "...", "actor_id": "..."}, ...]"""
    import concurrent.futures, urllib.request, pathlib
    out = pathlib.Path(output_dir).expanduser()
    out.mkdir(exist_ok=True)

    # Fire all jobs in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as ex:
        jobs = {ex.submit(generate_ugc_ad, b["script"], b["actor_id"]): i
                for i, b in enumerate(briefs)}

    # Poll and download
    for future, idx in jobs.items():
        job_id = future.result()["job_id"]
        url = poll_job(job_id)
        fname = out / f"hook_{idx+1:02d}.mp4"
        urllib.request.urlretrieve(url, fname)
        print(f"✅ {fname}")
```

---

## AGENCY OFFER STRUCTURE

### The $1,500/mo Retainer
- **Deliver:** 20 fresh UGC ads within 24 hours of brief
- **Weekly:** Iterate hooks based on Meta performance data
- **Monthly cost to you:** ~$150 (Arcads + Claude Code)
- **Margin:** 90%

### Landing the First Client (7-day plan)

| Day | Action |
|---|---|
| 1 | Set up stack · run test brief · verify output |
| 2 | Pick ONE niche (e.g., "DTC sleep supplements") |
| 3 | Generate 10 free ads for a real brand in that niche |
| 4 | DM founder on Instagram/LinkedIn with the videos |
| 5 | Repeat for 20 brands (1 in 20 replies) |
| 6 | Offer 7-day free trial → $1,500/mo after |
| 7 | Deliver 20 ads by EOD · they're locked in |

**DM template (no pitch, just proof):**
> "Made these 10 UGC ads for [BRAND] in an hour. Want 20 more?"

### Best Niches (2026)
1. Supplements (sleep, focus, weight)
2. Skincare / beauty DTC
3. Fitness equipment
4. DTC food / snacks
5. Pet products

---

## PROMPT TEMPLATES

### Batch Brief Prompt (paste directly into Claude)
```
I need 20 UGC ads for the following brief:
PRODUCT: [name + price + what it does]
AUDIENCE: [age range, pain point, lifestyle]
OFFER: [discount / trial / CTA]

For each ad:
1. Write a 30-60 second script with a strong hook in the first 3 words
2. Label the hook type (testimonial / DR / pattern interrupt / problem-solution / social proof)
3. Recommend an actor type (age/vibe/energy)
4. Fire to Arcads API using ARCADS_API_KEY env var
5. Save all MP4s to ~/ugc-output/ named by hook type + number

Use parallel rendering — fire all 20 jobs simultaneously.
```

---

## ACTORS REFERENCE (Arcads library)
- List all available actors: `GET /v1/actors`
- Filter by gender, age range, language, style
- Each actor has: `id`, `name`, `preview_url`, `tags`

```bash
curl -H "Authorization: Bearer $ARCADS_API_KEY" \
  https://api.arcads.ai/v1/actors | jq '.[].name'
```

---

## QUALITY CHECKLIST

- [ ] Hook lands in first 3 words (no slow intros)
- [ ] Script ≤ 60 seconds when read aloud at normal pace
- [ ] Actor vibe matches product tone
- [ ] CTA clear and specific (not "learn more" — use "get 30% off today")
- [ ] All 20 files downloaded and named before delivery
- [ ] Preview 3–5 before sending to client

---

## AUTO-AGENTS ACTIVATED WITH THIS SKILL

- **Ad Creative Strategist** — hook writing, angle variation, DR copy
- **Content Creator** — script tone, storytelling, pattern interrupts
- **Paid Social Strategist** — Meta Ads Manager upload, A/B test design
- **Sales Coach** — cold DM scripts, retainer close, trial offer framing
