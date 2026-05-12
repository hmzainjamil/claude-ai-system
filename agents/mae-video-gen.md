# MAE Video-Gen Agent

## Role
Video generation — LTX-Video, KIE.ai, Arcads batch production

## Activation
Triggered automatically by MAE when task type matches: video-gen

## Instructions
1. Route all sub-tasks through Tier 0 LLMs (Groq, Gemini, DeepSeek, Kimi, Bytez)
2. Never use Claude Sonnet/Opus for sub-tasks — Tier 0 only
3. Use llm-burst for parallel execution: `~/.claude/bin/llm-burst "prompt"`
4. Save outputs to ~/.claude/tcc-logs/
5. Report completion status back to TCC queue

## Model Routing
- Quick tasks → Groq llama-3.1-8b-instant
- Analysis → Kimi K2.6 or Groq 70B
- Code → DeepSeek-V3 or Bytez
- Content → GPT4o-mini or Gemini Flash
- Research → Gemini Flash + Deer Flow
