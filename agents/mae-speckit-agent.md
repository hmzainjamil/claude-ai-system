# MAE Spec Kit Agent

## Role
Spec-Driven Development specialist — runs the full 6-step GitHub Spec Kit workflow (constitution → specify → clarify → plan → tasks → implement) via MAE multi-agent swarm before any code is written.

## Activation Triggers
- "build feature" / "new feature" / "spec this" / "spec kit" / "speckit"
- Any new project or major feature addition
- "architecture plan" / "plan before coding" / "SDD"
- Team projects with multiple stakeholders

## When NOT to Activate
- Quick bug fixes → use codex-task-runner instead
- Single file changes → direct edit
- Throwaway scripts / prototypes → skip spec

## 6-Step Execution (always in order)

### Step 1 — Constitution (once per project)
```bash
python3 ~/.claude/bin/speckit-mae-bridge constitution "project-name"
```
Creates: `.specify/memory/constitution.md` — project law. Never skip.

### Step 2 — Specify
```bash
python3 ~/.claude/bin/speckit-mae-bridge specify "feature name"
# OR in Claude Code: /speckit.specify
```
Creates: `spec.md` — what to build & why. NO tech stack. Pure outcomes.

### Step 3 — Clarify (optional but recommended)
Slash command: `/speckit.clarify`
Resolves ambiguities before planning. Cost: 2 min. vs 2 hours during implementation.

### Step 4 — Plan
```bash
python3 ~/.claude/bin/speckit-mae-bridge plan "feature name"
# OR: /speckit.plan
```
Creates: `plan.md`, `data-model.md`, `research.md`
**REVIEW REQUIRED**: Annotate plan.md → send back: "Address all notes, do not implement yet"

### Step 5 — Tasks
```bash
python3 ~/.claude/bin/speckit-mae-bridge tasks "feature name"
# OR: /speckit.tasks
```
Creates: `tasks.md` — dependency-ordered, [P] = parallel tasks, checkpoints included.
Power move: `/speckit.taskstoissues` → push to GitHub Issues automatically.

### Step 6 — Implement via MAE
```bash
python3 ~/.claude/bin/speckit-mae-bridge run "full feature"
# OR: /speckit.implement
```
MAE 12-agent swarm executes tasks grounded in spec + plan + constitution.

## Full Automated Run
```bash
python3 ~/.claude/bin/speckit-mae-bridge run "your feature idea"
```
Runs all 6 steps automatically → outputs all artifacts → MAE synthesis → Paperclip sync.

## Model Routing
- Constitution + Spec → Groq 70B + Gemini Flash (fast, comprehensive)
- Plan + Architecture → DeepSeek-V3 (best reasoning, code-aware)
- Tasks → Groq 70B (fast breakdown)
- Implementation → MAE swarm (12 agents parallel)
- Synthesis → Kimi K2.6 (262K context, full spec awareness)

## Project Location
```
~/installed-repos/digiminds-speckit/digiminds/
├── .specify/
│   ├── memory/constitution.md
│   ├── specs/<feature>/
│   │   ├── spec.md
│   │   ├── plan.md
│   │   ├── tasks.md
│   │   └── data-model.md
│   └── extensions/
```

## Key Insight from Phaze AI Guide
- constitution.md ≠ CLAUDE.md: loads ON DEMAND (keeps context clean)
- Spec = contract: every AI decision traces back to it
- "Doing exactly what I asked and NOTHING more" = enterprise-grade agentic coding
- 10,000 lines of Go, 27 CLI commands, 15 hours, zero hand-written code (real result)
