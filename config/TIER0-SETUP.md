# Tier 0 Setup — Zero Claude Token Config

Run `~/.claude/bin/tier0-check` to see current status.

## Priority order (cheapest → most capable)

### 1. Ollama — FREE, local, offline (BEST)
```bash
# Install
curl -fsSL https://ollama.ai/install.sh | sh

# Pull models
ollama pull llama3          # general tasks
ollama pull codellama       # code
ollama pull mistral         # fast general
ollama pull deepseek-coder  # code (best)

# Test
ollama run llama3 "hello"
```
Cost: $0.00 forever.

---

### 2. Groq — FREE tier, fastest cloud
```bash
# Get key: https://console.groq.com (free)
echo 'export GROQ_API_KEY="gsk_..."' >> ~/.zshrc
source ~/.zshrc
```
Cost: Free tier = 14,400 req/day.

---

### 3. Gemini — FREE tier, Google
```bash
# Get key: https://aistudio.google.com/app/apikey (free)
echo 'export GEMINI_API_KEY="AIza..."' >> ~/.zshrc
source ~/.zshrc
```
Cost: Free tier = 1,500 req/day gemini-2.0-flash.

---

### 4. OpenRouter — Pay-per-use, 100+ models
```bash
# Get key: https://openrouter.ai/keys
echo 'export OPENROUTER_API_KEY="sk-or-..."' >> ~/.zshrc
source ~/.zshrc
```
Cost: DeepSeek-V3 = $0.14/MTok (vs Claude Sonnet $3/MTok = 21x cheaper).

---

### 5. GPT-4o-mini — OpenAI cheap fallback
```bash
echo 'export OPENAI_API_KEY="sk-..."' >> ~/.zshrc
source ~/.zshrc
```
Cost: $0.15/MTok input.

---

## Quick start (minimum tokens, maximum speed)
```bash
# Step 1: Install Ollama (zero cost)
curl -fsSL https://ollama.ai/install.sh | sh && ollama pull llama3

# Step 2: Get Groq free key (fastest cloud)
# → https://console.groq.com

# Step 3: Verify
~/.claude/bin/tier0-check
```

## Current status
Run: `~/.claude/bin/tier0-check`
