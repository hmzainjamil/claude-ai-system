# wan-image-gen — Wan2.7 Image Generation via Dashscope
**Alibaba Cloud Dashscope API | Wan2.7-image & Wan2.7-image-pro**

Generate high-quality AI images using Wan2.7 models — free with your Dashscope API key.
Best for: product mockups, campaign visuals, luxury photography style, editorial images.

---

## USAGE
`/wan-image-gen [prompt] [--model pro|standard] [--size 1024x1024]`

---

## API DETAILS
- **Endpoint:** `https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis`
- **Key:** from `$DASHSCOPE_API_KEY` in `~/.claude/tier0.env`
- **Models:** `wanx2.1-t2i-plus` (pro), `wanx2.1-t2i-turbo` (standard)
- **Sizes:** 1024×1024, 720×1280, 1280×720

---

## GENERATION SCRIPT

```python
#!/usr/bin/env python3
"""wan-image-gen — Generate images via Wan2.7 Dashscope API"""
import os, sys, json, time, urllib.request

API_KEY = os.environ.get("DASHSCOPE_API_KEY", "")
BASE_URL = "https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis"

def generate(prompt, model="wanx2.1-t2i-plus", size="1024x1024", n=1):
    w, h = size.split("x")
    payload = json.dumps({
        "model": model,
        "input": {"prompt": prompt},
        "parameters": {"size": f"{w}*{h}", "n": n, "style": "<photography>"}
    }).encode()
    req = urllib.request.Request(
        BASE_URL,
        data=payload,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "X-DashScope-Async": "enable"
        }
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        result = json.loads(r.read())
    task_id = result["output"]["task_id"]
    print(f"Task ID: {task_id} — polling...")
    # Poll for result
    for _ in range(30):
        time.sleep(3)
        poll = urllib.request.Request(
            f"https://dashscope.aliyuncs.com/api/v1/tasks/{task_id}",
            headers={"Authorization": f"Bearer {API_KEY}"}
        )
        with urllib.request.urlopen(poll, timeout=10) as r:
            status = json.loads(r.read())
        if status["output"]["task_status"] == "SUCCEEDED":
            urls = [r["url"] for r in status["output"]["results"]]
            return urls
        elif status["output"]["task_status"] == "FAILED":
            return {"error": status["output"].get("message", "Failed")}
    return {"error": "Timeout"}

if __name__ == "__main__":
    prompt = " ".join(sys.argv[1:]) or "luxury jewellery campaign poster, dark emerald green"
    urls = generate(prompt)
    print("Generated images:")
    for url in urls:
        print(f"  {url}")
```

---

## ELEMENTEC PROMPT EXAMPLES FOR WAN2.7

### Luxury Campaign Poster
```
Premium luxury jewellery campaign poster, deep emerald green velvet background,
champagne gold necklace with diamonds, cinematic soft lighting, editorial fashion photography,
4K ultra-detailed, luxury brand advertisement, clean negative space, serif typography space,
professional commercial photography, aspirational Indian elegance
```

### Instagram Creative
```
Square format luxury product photography, single elegant gold necklace on white marble surface,
soft natural lighting, minimal composition, luxury fashion editorial style,
champagne gold and ivory color palette, high-end jewelry brand social media post,
ultra-detailed, premium commercial photography
```

### Finance Dashboard UI
```
Premium dark-theme personal finance mobile app dashboard, modern UI design,
dark navy background, neon accent colors, circular charts showing expense categories,
clean typography, minimal icons, premium fintech app aesthetic, 4K sharp render
```

### Packaging Mockup
```
Luxury jewelry packaging flat lay photography, deep emerald green box with gold embossed logo,
matching shopping bag, thank you card, satin ribbon, velvet interior,
soft studio lighting, white marble background, premium product photography style,
editorial composition, high-end brand unboxing experience
```

---

## INTEGRATION WITH ELEMENTEC WORKFLOW

When `/elementec-visuals` is called, this skill is auto-invoked to:
1. Convert the filled Elementec prompt → Wan2.7 optimized version
2. Generate via Dashscope API
3. Return image URLs for download/delivery
4. Save to `~/Downloads/elementec-output/` with timestamp
