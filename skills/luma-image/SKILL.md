---
name: luma-image
description: Luma AI image and video generation via Dream Machine API (uni-1 model). Auto-triggers on any image/video generation request.
type: tool
---

# Luma AI — Dream Machine Image & Video Generator

## API Config
```
Base URL: https://agents.lumalabs.ai/v1
Auth: Bearer $LUMA_API_KEY
Model: uni-1
```

## Endpoints

### Generate Image
```bash
curl -X POST https://agents.lumalabs.ai/v1/generations \
  -H "Authorization: Bearer $LUMA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "<PROMPT>",
    "model": "uni-1",
    "type": "image",
    "aspect_ratio": "16:9"
  }'
```

### Generate Video
```bash
curl -X POST https://agents.lumalabs.ai/v1/generations \
  -H "Authorization: Bearer $LUMA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "<PROMPT>",
    "model": "uni-1",
    "type": "video",
    "aspect_ratio": "16:9"
  }'
```

### Check Generation Status
```bash
curl https://agents.lumalabs.ai/v1/generations/<GENERATION_ID> \
  -H "Authorization: Bearer $LUMA_API_KEY"
```

### List All Generations
```bash
curl https://agents.lumalabs.ai/v1/generations \
  -H "Authorization: Bearer $LUMA_API_KEY"
```

## Aspect Ratios Supported
- `16:9` — widescreen / YouTube / presentations
- `9:16` — vertical / Reels / TikTok / Stories
- `1:1` — square / Instagram posts
- `4:3` — traditional / landscape
- `3:4` — portrait

## Workflow (auto)
1. User gives prompt (text, concept, style)
2. POST to /v1/generations → get generation_id
3. Poll GET /v1/generations/{id} until `state == "completed"`
4. Return `assets.image` or `assets.video` URL
5. Download to ~/Downloads/luma-[timestamp].[ext]

## Python helper (inline — no file needed)
```python
import os, requests, time, urllib.request
from datetime import datetime

API_KEY = os.environ["LUMA_API_KEY"]
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

def luma_generate(prompt, gen_type="image", aspect_ratio="16:9"):
    r = requests.post(
        "https://agents.lumalabs.ai/v1/generations",
        headers=HEADERS,
        json={"prompt": prompt, "model": "uni-1", "type": gen_type, "aspect_ratio": aspect_ratio}
    )
    r.raise_for_status()
    gen_id = r.json()["id"]
    print(f"[Luma] Generation started: {gen_id}")

    # Poll until done
    for _ in range(60):
        time.sleep(3)
        status = requests.get(f"https://agents.lumalabs.ai/v1/generations/{gen_id}", headers=HEADERS).json()
        state = status.get("state")
        print(f"[Luma] State: {state}")
        if state == "completed":
            url = status["assets"].get("image") or status["assets"].get("video")
            ext = "mp4" if gen_type == "video" else "jpg"
            out = os.path.expanduser(f"~/Downloads/luma-{datetime.now().strftime('%Y%m%d-%H%M%S')}.{ext}")
            urllib.request.urlretrieve(url, out)
            print(f"[Luma] Saved: {out}")
            return out
        if state in ("failed", "error"):
            raise Exception(f"Luma generation failed: {status}")
    raise TimeoutError("Luma generation timed out after 3 minutes")
```

## Trigger phrases (auto-activate via skill-auto-activate)
- "generate image" / "create image" / "make image"
- "luma" / "dream machine" / "luma ai"
- "generate video" / "create video" / "luma video"
- "ai image" / "ai video" / "text to image" / "text to video"

## Key — env var
```bash
export LUMA_API_KEY="luma-api-Z_NThE_VEnTrl8j9M1bxoVsziHiDAsf6yRTuWYL5CNU"
```
Already written to ~/.zshrc — available in all new shells.
