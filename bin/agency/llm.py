"""
AGENCY LLM Router — 7-Tier, Task-Aware (zero Claude tokens)

LOCAL (offline, zero cost):
  0a-FAST:  GPT4All DeepSeek R1 1.5B / Llama 3.2 3B  → scoring, short tasks
  0a-MID:   GPT4All Phi-3 Mini / Mistral 7B           → emails, FB comments
  0a-SMART: GPT4All Nous Hermes 2 / Llama 3.1 128k    → proposals, audits
  0b:       Ollama llama3:latest                       → fallback

CLOUD (zero Claude tokens):
  0c: G0DM0D3 pro   — 12-model race, 1000 req/day
  0d: DeepSeek V3   — best quality/cost
  0e: Groq          — fastest cloud
  0f: OpenAI mini   — reliable
  0g: OpenRouter    — 50 req/day free

TASK TYPES → model selection:
  "fast"     → FAST tier  (scoring, BDM match, FB comment subjects)
  "copy"     → MID tier   (email bodies, proposal text, short copy)
  "audit"    → SMART tier (full audits, long proposals, reasoning)
  None/auto  → tries best available in order
"""

import os, warnings
warnings.filterwarnings("ignore")
import requests

# ── GPT4ALL MODEL REGISTRY ────────────────────────────────────────────────────
_MODELS_DIR = os.path.expanduser("~/Library/Application Support/nomic.ai/GPT4All/")

GPT4ALL_MODELS = {
    # tier → [preferred, fallback...] — uses first that exists on disk
    "fast": [
        "DeepSeek-R1-Distill-Qwen-1.5B-Q4_0.gguf",
        "Llama-3.2-3B-Instruct-Q4_0.gguf",
        "Llama-3.2-1B-Instruct-Q4_0.gguf",
        "Meta-Llama-3-8B-Instruct.Q4_0.gguf",  # fallback to large
    ],
    "copy": [
        "Phi-3-mini-4k-instruct.Q4_0.gguf",
        "mistral-7b-instruct-v0.1.Q4_0.gguf",
        "Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf",
        "Meta-Llama-3-8B-Instruct.Q4_0.gguf",
    ],
    "audit": [
        "Nous-Hermes-2-Mistral-7B-DPO.Q4_0.gguf",
        "Meta-Llama-3.1-8B-Instruct-128k-Q4_0.gguf",
        "DeepSeek-R1-Distill-Qwen-7B-Q4_0.gguf",
        "Meta-Llama-3-8B-Instruct.Q4_0.gguf",
    ],
    "code": [
        "qwen2.5-coder-7b-instruct-q4_0.gguf",
        "DeepSeek-R1-Distill-Qwen-7B-Q4_0.gguf",
        "Meta-Llama-3-8B-Instruct.Q4_0.gguf",
    ],
    "reason": [
        "DeepSeek-R1-Distill-Qwen-7B-Q4_0.gguf",
        "DeepSeek-R1-Distill-Llama-8B-Q4_0.gguf",
        "DeepSeek-R1-Distill-Qwen-1.5B-Q4_0.gguf",
        "Meta-Llama-3-8B-Instruct.Q4_0.gguf",
    ],
}

# Default task order when task_type=None
GPT4ALL_AUTO = ["copy", "fast", "audit"]

# Lazy-loaded instances cache: filename → GPT4All instance
_gpt4all_cache = {}


def _find_model(task_type=None):
    """Return (filepath, filename) for best available model for task."""
    tiers = GPT4ALL_AUTO if not task_type else [task_type]
    for tier in tiers:
        for fname in GPT4ALL_MODELS.get(tier, []):
            fpath = os.path.join(_MODELS_DIR, fname)
            if os.path.exists(fpath):
                return fpath, fname
    return None, None


def _get_gpt4all(filepath):
    """Lazy-load + cache GPT4All model instance."""
    if filepath in _gpt4all_cache:
        return _gpt4all_cache[filepath]
    try:
        from gpt4all import GPT4All
        instance = GPT4All(filepath, verbose=False)
        _gpt4all_cache[filepath] = instance
        return instance
    except Exception:
        _gpt4all_cache[filepath] = None
        return None


# ── CLOUD API CONFIG ──────────────────────────────────────────────────────────
OLLAMA_URL   = "http://localhost:11434/api/generate"
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3:latest")

G0DM0DE_BASE = os.environ.get("G0DM0D3_API", "http://localhost:7860")
G0DM0DE_URL  = f"{G0DM0DE_BASE}/v1/ultraplinian/completions"
G0DM0DE_KEY  = os.environ.get("G0DM0D3_KEY", "")

DEEPSEEK_KEY   = os.environ.get("DEEPSEEK_API_KEY", "")
DEEPSEEK_URL   = "https://api.deepseek.com/chat/completions"

GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GROQ_URL     = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL   = "llama-3.1-8b-instant"

OPENAI_KEY   = os.environ.get("OPENAI_API_KEY", "")
OPENAI_URL   = "https://api.openai.com/v1/chat/completions"

OPENROUTER_KEY = os.environ.get("OPENROUTER_API_KEY", "")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_FREE_MODELS = [
    "google/gemma-3-4b-it:free",
    "meta-llama/llama-3.2-3b-instruct:free",
    "deepseek/deepseek-r1-distill-llama-70b:free",
    "mistralai/mistral-small-3.1-24b-instruct:free",
]


# ── MAIN ROUTER ───────────────────────────────────────────────────────────────

def call_llm(prompt, max_tokens=400, temperature=0.7, task_type=None):
    """
    Route to best available LLM. task_type: 'fast'|'copy'|'audit'|'code'|'reason'
    Falls through all 7 tiers until one succeeds.
    """

    # ── 0a: GPT4All (local GGUF, fully offline) ───────────────────────────────
    fpath, fname = _find_model(task_type)
    if fpath:
        model = _get_gpt4all(fpath)
        if model:
            try:
                with model.chat_session():
                    response = model.generate(
                        prompt,
                        max_tokens=max_tokens,
                        temp=temperature,
                        streaming=False
                    )
                if response and len(response.strip()) > 2:
                    return response.strip()
            except Exception:
                pass

    # ── 0b: Ollama ────────────────────────────────────────────────────────────
    try:
        r = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL, "prompt": prompt, "stream": False,
            "options": {"num_predict": max_tokens, "temperature": temperature}
        }, timeout=60)
        if r.status_code == 200:
            return r.json().get("response", "").strip()
    except Exception:
        pass

    # ── 0c: G0DM0D3 pro ───────────────────────────────────────────────────────
    if G0DM0DE_KEY and G0DM0DE_KEY.startswith("g0d_"):
        try:
            r = requests.post(G0DM0DE_URL, json={
                "model": "fast",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": max_tokens, "temperature": temperature, "stream": False
            }, headers={"Authorization": f"Bearer {G0DM0DE_KEY}"}, timeout=30)
            if r.status_code == 200:
                data = r.json()
                return (data.get("response") or
                        data["choices"][0]["message"]["content"]).strip()
        except Exception:
            pass

    # ── 0d: DeepSeek V3 ───────────────────────────────────────────────────────
    if DEEPSEEK_KEY:
        try:
            r = requests.post(DEEPSEEK_URL, json={
                "model": "deepseek-chat",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": max_tokens, "temperature": temperature
            }, headers={"Authorization": f"Bearer {DEEPSEEK_KEY}"}, timeout=25)
            if r.status_code == 200:
                return r.json()["choices"][0]["message"]["content"].strip()
        except Exception:
            pass

    # ── 0e: Groq ──────────────────────────────────────────────────────────────
    if GROQ_API_KEY:
        try:
            r = requests.post(GROQ_URL, json={
                "model": GROQ_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": max_tokens, "temperature": temperature
            }, headers={"Authorization": f"Bearer {GROQ_API_KEY}"}, timeout=20)
            if r.status_code == 200:
                return r.json()["choices"][0]["message"]["content"].strip()
        except Exception:
            pass

    # ── 0f: OpenAI gpt-4o-mini ────────────────────────────────────────────────
    if OPENAI_KEY:
        try:
            r = requests.post(OPENAI_URL, json={
                "model": "gpt-4o-mini",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": max_tokens, "temperature": temperature
            }, headers={"Authorization": f"Bearer {OPENAI_KEY}"}, timeout=20)
            if r.status_code == 200:
                return r.json()["choices"][0]["message"]["content"].strip()
        except Exception:
            pass

    # ── 0g: OpenRouter free tier ──────────────────────────────────────────────
    if OPENROUTER_KEY and OPENROUTER_KEY.startswith("sk-or-"):
        for model in OPENROUTER_FREE_MODELS:
            try:
                r = requests.post(OPENROUTER_URL, json={
                    "model": model,
                    "messages": [{"role": "user", "content": prompt}],
                    "max_tokens": max_tokens, "temperature": temperature
                }, headers={
                    "Authorization": f"Bearer {OPENROUTER_KEY}",
                    "HTTP-Referer": "https://digiminds.org",
                    "X-Title": "DigiMinds Agency"
                }, timeout=30)
                if r.status_code == 200:
                    return r.json()["choices"][0]["message"]["content"].strip()
                if r.status_code == 429:
                    break
            except Exception:
                continue

    return None


def llm_status():
    """Print status of all models — downloaded + available."""
    print("\n=== GPT4All Models ===")
    for tier, models in GPT4ALL_MODELS.items():
        for fname in models:
            fpath = os.path.join(_MODELS_DIR, fname)
            exists = os.path.exists(fpath)
            size = f"{os.path.getsize(fpath)//1024//1024}MB" if exists else "not downloaded"
            status = "✓" if exists else "✗"
            print(f"  {status} [{tier:6}] {fname.split('.')[0][:35]:<35} {size}")
    print()
