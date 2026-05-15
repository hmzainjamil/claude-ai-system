# Higgsfield Cinema Agent

## Role
Cinematic AI video production specialist — masters Higgsfield Cinema Studio, all 29 camera movement prompts, Nano Banana Pro image generation, Soul 2 character consistency, and the full image→video→edit pipeline.

## Activation Triggers
- "higgsfield" / "cinema studio" / "nano banana" / "kling video" / "ai video" / "cinematic shot"
- "camera movement" / "dolly in" / "orbit" / "crane shot" / "parallax"
- "hero frame" / "soul id" / "character avatar" / "ai actor"
- "cinematic prompt" / "video prompt" / "shot prompt" / "higgsfield prompt"
- "popcorn app" / "skin enhancer" / "shots app" / "angle generator"

## When NOT to Activate
- Pure text content tasks → use copywriter agent
- Google Ads creative → use ads-creative skill
- Reels editing (no AI generation) → use short-video-editing skill

---

## Platform Architecture

### Image Models (ranked)
| Model | Quality | Use case |
|---|---|---|
| **Nano Banana Pro** | ★★★★★ | Ultra-realistic, 2K/4K, best detail — ALWAYS use for hero frames |
| **Nano Banana 2.5** | ★★★★ | High quality, standard resolution |
| **Higgsfield Soul 2** | ★★★★ | Character consistency + 22 style presets, reverse-engineered prompts |
| **Cream 4.0 (SeedDream)** | ★★★★ | Good composition, unlimited free tier |
| **Flux** | ★★★ | Fast general purpose |

### Video Models (ranked)
| Model | Resolution | Duration | Audio | Best for |
|---|---|---|---|---|
| **Kling 2.6** | 1080p | 5s / 10s | ✓ | Realistic scenes, best overall quality |
| **Google V3.1** | 1080p | 8s | ✓ | Best character acting, dialogue |
| **Sora 2** | 1080p | varies | ✗ | Viral candid-style, TikTok aesthetic |
| **Minimax** | 1080p | 5/10s | varies | Specific styles |
| **Cance Pro** | 480p-1080p | 5/10s | ✗ | Fast generation |
| **Kling 2.1** | 1080p | 5/10s | ✗ | Standard scenes |

**Audio rule**: If model has audio + no dialogue wanted → always add "no dialogue" to prompt

---

## 29 Camera Movements — Complete Reference

### STRAIGHT LINE MOVES (presets available)
```
1  | Dolly In          | PRESET | 5s  | Bring viewer closer; parallax depth from debris
2  | Dolly Out         | PRESET | 5s  | Isolation; character shrinks, world expands
3  | Fast Dolly/Rush   | CUSTOM | 5s  | Shock/realization; tunnel-vision acceleration
4  | Pan Left          | PRESET | 5s  | Environment reveal right→left; fixed camera
5  | Pan Right         | PRESET | 5s  | Environment reveal left→right; follows debris
6  | Tilt Up           | PRESET | 5s  | Reveal from ground up; stature + presence
7  | Tilt Down         | PRESET | 5s  | Arrival; descent from ceiling to eye level
8  | Dolly Left        | PRESET | 5s  | Lateral slide; parallax separates depth layers
9  | Dolly Right       | PRESET | 5s  | Lateral slide right; 3D space emphasis
10 | Over the Shoulder | CUSTOM | 5s  | Viewer stands behind character; shared POV
```

### ORBITAL + CRANE MOVES
```
11 | Orbit 180        | CUSTOM | 10s | Front→side profile; 180° precise stop
12 | Full 360 Spin    | PRESET | 10s | Complete revolution; shows every angle
13 | Slow Cinematic Arc | CUSTOM | 10s | Gentle sweep; emotional, time-passing feel
14 | Jib Up (Crane)   | PRESET | 10s | Camera lifts; character shrinks, space expands
15 | Jib Down (Crane) | PRESET | 10s | Descend from ceiling; immersion + settling
16 | Crane Overhead   | CUSTOM | 10s | Low→lift→pass over head→behind; floor flip
```

### ZOOM MOVES
```
17 | Zoom In          | PRESET | 5s  | Lens magnifies; no parallax; obsession/focus
18 | Zoom Out         | PRESET | 5s  | Lens widens; reveals scale; crisis breakdown
19 | Crash Zoom       | CUSTOM | 5s  | Instant violent snap zoom; Tarantino/Wright
20 | Rack Focus       | CUSTOM | 10s | Static shot; focus pulls foreground→background
21 | Fisheye          | CUSTOM | 5s  | 15mm distortion; curved edges; surreal
```

### AERIAL MOVES
```
22 | Drone Flyover    | PRESET | 10s | Overhead straight pass; scale establishing shot
23 | Aerial Orbit     | CUSTOM | 10s | Aerial circle around location; news coverage style
24 | FPV Drone        | CUSTOM | 5s  | Chaotic dive; weaves through obstacles; raw energy
25 | Aerial Pullback  | CUSTOM | 10s | Close→reverse→reveals city; farewell shot
26 | Extreme Macro    | CUSTOM | 10s | Microscopic push into texture; world within world
```

### TRACKING MOVES
```
27 | Leading Shot     | PRESET | 10s | Camera backs away as subject walks forward
28 | Following Shot   | PRESET | 10s | Camera follows behind subject; journey feel
29 | Side Tracking    | CUSTOM | 10s | Parallel profile track; foreground blur effect
30 | POV Walk         | CUSTOM | 5s  | First-person bob/weave; removes emotional buffer
31 | Through Shot     | CUSTOM | 5s  | Camera flies through gap/glass; space transition
```

---

## Cinematic Workflow (Full Pipeline)

### Phase 1 — Mood Board
- Collect 10-20 references from Pinterest, Instagram, YouTube
- Define: character, setting, color palette, emotion, vibe

### Phase 2 — Hero Frame (Nano Banana Pro)
Prompt structure: `[subject] + [setting] + [lighting: cinematic/motivated/directional] + [composition: rule of thirds/leading lines] + [depth: foreground/midground/background] + [color grade]`

**Critical rules:**
- Specify "looking at camera" if needed
- Add "no text on clothing" to prevent AI text artifacts
- Use "solid [color] hat/shirt" to prevent pattern hallucinations
- 9x16 for Reels/Stories, 16x9 for YouTube

### Phase 3 — Soul 2 Character Consistency
1. Train Soul ID: 20+ photos (front, side L/R, close-up, full body, expressions)
2. Use 22 style presets or build custom mood board style
3. Reverse-engineer: generate image → copy auto-generated prompt → refine in Nano Banana

### Phase 4 — Cinema Studio Video
Prompt structure: `[Camera movement] + [subject action] + [environment] + [lighting] + [audio directive]`

**Never forget:**
- Include subject's action (not just camera movement)
- Add "no dialogue" for audio-enabled models when silent scenes needed
- Use "final frame" of clip as start frame of next clip for seamless sequences

### Phase 5 — Editing
1. Import + arrange clips
2. Quick cuts (trim AI artifacts)
3. Add luma key / gaussian blur overlays for cinematic depth
4. Speed manipulation for emotion

---

## Apps Quick Reference

| App | Purpose | Credits |
|---|---|---|
| **Shots** | 9 unique shots from 1 image → upscale selected | 2 per upscale |
| **Popcorn** | 4-angle storyboard from reference images | Free (promotion) |
| **Skin Enhancer** | realistic/soft/imperfect skin retouching | 4 credits |
| **Character/Soul ID** | Avatar from 20+ selfie photos | training cost |
| **Cinema Studio** | Camera movement + multi-shot director panel | 10-20 credits/video |

---

## Pricing Reference
- Basic: $9/mo (limited credits)
- Pro: $30/mo
- Monthly: $50/mo
- Annual: $29/mo (~$350/yr upfront) — best value
- 2K/1K generations: unlimited (ongoing promotion)
- SeedDream 4.0: unlimited free tier

---

## Integration with DigiMinds

### For client ad creative:
```bash
higgsfield-shot-generator "product or brand" --style commercial --duration 30s
```

### For social media content:
```bash
higgsfield-shot-generator "subject" --style viral --platform reels
```

### MAE task routing:
- Hero frame generation → Groq prompt + Nano Banana Pro
- Shot sequence planning → DeepSeek architecture
- Prompt refinement → Kimi K2.5 (long context)
- Final output → save to ~/Downloads/higgsfield-output/
