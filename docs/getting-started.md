# Getting Started

## Prerequisites

- Claude Code installed (`npm install -g @anthropic-ai/claude-code`)
- macOS (the automation scripts are macOS-native)
- API keys for the models you want to use (see `.env` setup below)

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/claude-ai-system.git
cd claude-ai-system
```

### 2. Copy skills to your Claude config

```bash
# Copy all skills to your Claude skills directory
cp -r skills/* ~/.claude/skills/

# Copy all agents
cp agents/*.md ~/.claude/agents/
cp agents/*.yaml ~/.claude/agents/ 2>/dev/null

# Copy automation scripts
mkdir -p ~/.claude/bin
cp automations/* ~/.claude/bin/
cp bin/* ~/.claude/bin/
chmod +x ~/.claude/bin/*
```

### 3. Set up environment variables

Create `~/.env` (never commit this file):

```bash
# Tier 0 models (use these first — cheapest/fastest)
export GROQ_API_KEY="your-groq-key"
export GEMINI_API_KEY="your-gemini-key"
export DEEPSEEK_API_KEY="your-deepseek-key"
export MOONSHOT_API_KEY="your-kimi-key"          # Kimi K2.6
export OPENROUTER_API_KEY="your-openrouter-key"
export MISTRAL_API_KEY="your-mistral-key"
export OPENAI_API_KEY="your-openai-key"

# Optional — only if using these features
export LUMA_API_KEY="your-luma-key"              # Luma image/video
export AIRTABLE_API_KEY="your-airtable-pat"      # Airtable integration

# Never needed for sub-tasks (only Claude handles final output)
# ANTHROPIC_API_KEY is managed by Claude Code itself
```

### 4. Set up the UserPromptSubmit hook

Add to your Claude Code `settings.json`:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      "~/.claude/bin/skill-auto-activate",
      "~/.claude/bin/tier0-prompt-inject"
    ],
    "Stop": [
      "~/.claude/bin/session-learn"
    ]
  }
}
```

### 5. Add the CLAUDE.md instructions

Copy the contents of your CLAUDE.md to `~/.claude/CLAUDE.md` to enable:
- L99 max performance mode
- OODA loop decision framework
- Model routing enforcement
- Skill activation protocol

---

## Quick Reference

### Skill Management

```bash
# Activate a skill manually
~/.claude/bin/skill-on lead-gen-ai

# Deactivate a skill
~/.claude/bin/skill-off lead-gen-ai

# Search for a skill by keyword
~/.claude/bin/skill-search "pdf"

# Check what's active
~/.claude/bin/skill-status
```

### Run llm-burst

```bash
# Burst mode — 15 models in parallel, judge picks best
llm-burst "Your prompt here"

# Fast mode — first available Tier 0 model
llm-burst --fast "Your prompt here"
```

### Sync to GitHub

```bash
# Manual sync
~/.claude/bin/github-sync

# Auto-sync happens when you say "new skill" or "added agent"
```

---

## First Tasks to Try

### Lead Generation
```
In Claude Code, type:
"Find 30 dentists in Chicago with owner phone and email"
```
The `lead-gen-ai` and `vibe-prospecting` skills auto-load. You get an Excel file in `~/Downloads/`.

### Website Builder
```
"Build a premium landing page for a digital marketing agency — dark theme, professional"
```
The `website-builder`, `ui-ux-promax`, and `framer-motion-builder` skills auto-load.

### PDF Audit Report
```
"Create a branded PDF audit report for a client named Acme Marketing"
```
The `reportlab-pdf-master` skill auto-loads. You get a branded 11-page PDF.

### Multi-Model Burst
```bash
llm-burst "Write 10 cold email subject lines for a PPC agency targeting ecom brands"
```
15 models respond in parallel. Best output returned in under 3 seconds.

---

## Troubleshooting

**Skill not auto-loading?**
Check that `skill-auto-activate` is in your `UserPromptSubmit` hook and has execute permission:
```bash
chmod +x ~/.claude/bin/skill-auto-activate
```

**llm-burst returning nothing?**
Check that at least one API key is set:
```bash
echo $GROQ_API_KEY  # Should print your key
```

**GitHub sync failing?**
Check that you have a remote set:
```bash
cd /Users/mc/claude-ai-system
git remote -v  # Should show origin
```
