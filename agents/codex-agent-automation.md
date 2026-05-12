# Codex Agent Automation Pattern

## Role
Delegate complex coding tasks to OpenAI Codex agent — reads codebase, edits files, runs tests, proposes diffs. Activated automatically when task involves: refactor, large codebase edits, multi-file changes, test generation.

## Activation Triggers
- "codex review" / "codex agent" / "delegate to codex"
- Multi-file refactor requests
- "adversarial review" / "codex rescue"
- Any task in `~/installed-repos/ads-creative/codex-plugin-cc/`

## Execution Pattern (ReAct loop)
```
1. THINK — analyze task, read relevant files, identify scope
2. ACT   — make targeted edits via file tools
3. OBS   — run tests, check output, verify correctness
4. LOOP  — repeat until task complete or needs escalation
```

## Commands
```bash
# Via codex-plugin-cc (installed at ~/installed-repos/ads-creative/codex-plugin-cc/)
cd ~/installed-repos/ads-creative/codex-plugin-cc && node index.js review <file>

# Via Claude Code skill invocation
# /codex:review    → full code review with Codex
# /codex:adversarial-review → stress-test code logic
# /codex:rescue    → fix broken/stuck code
```

## Model Routing
- Code review → OpenAI Codex (gpt-4o / o3)
- Quick fixes → DeepSeek-V3 via OpenRouter
- Test gen → GPT-4o-mini
- Architecture review → Kimi K2.6 (262K context)

## Instructions
1. Never use Claude tokens for sub-tasks — route to Codex/DeepSeek/GPT4o-mini
2. Always read existing code before suggesting changes
3. Run tests after every edit — never ship untested diffs
4. Output: structured diff + test results + confidence score
5. Escalate to Claude Sonnet only if all Tier 0 models fail

## Integration with MAE
Auto-triggered by MAE when task_type = "code" or "refactor":
```bash
mae run "refactor auth module to use JWT"
# → MAE detects code task → routes to codex-agent → DeepSeek-V3 executes → synthesizes
```
