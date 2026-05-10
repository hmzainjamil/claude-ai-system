# Terminology — Definitions for This System

## Skill / SKILL.md

A **Skill** is a self-contained instruction module that tells Claude Code how to perform a specific capability. It is a Markdown file (`SKILL.md`) that contains:

- A YAML frontmatter block with the skill name, description, and allowed tools
- Trigger keywords (phrases that auto-activate the skill)
- Step-by-step instructions for Claude to follow
- References to MCP tools, agents, and sub-skills to invoke

Skills are loaded on demand — either manually via `skill-on <name>` or automatically via `skill-auto-activate` when the user's prompt contains a trigger keyword. After the task completes, skills are deactivated to prevent context bloat.

**Real example — `lead-gen-ai`:**
```
skills/lead-gen-ai/SKILL.md
Triggers: "find leads", "lead gen", "extract leads"
What it does:
  1. Calls Vibe Prospecting MCP to search business entities
  2. Calls Apollo MCP to enrich with verified emails
  3. Exports to Excel via Airtable SDK
  4. Generates 5-touch outreach sequence
```

---

## AI Agent

An **AI Agent** is a persistent persona with a specialized role, domain knowledge, and behavioral instructions. Unlike a skill (which describes a workflow), an agent embodies a professional identity — it has a job title, expertise, communication style, and defined scope.

Agents are stored as `.md` files in `agents/` and loaded into Claude's context when that specialization is needed. The `all-agents` skill can load all 210 simultaneously for comprehensive tasks.

**Real example — from `agents/engineering-backend-architect.md`:**
```
Role: Senior Backend Architect
Expertise: System design, API architecture, database optimization,
           microservices, scalability patterns
Behavior: Reviews code for architectural debt, suggests patterns,
          estimates complexity, flags security issues
Activated by: all-agents skill or direct reference
```

---

## AI Actor

An **AI Actor** is one stage in a multi-step pipeline where each stage performs a distinct transformation. Unlike an agent (which has a persistent identity), an actor is a discrete processing unit — it takes input, performs its job, and passes structured output to the next actor.

The term comes from the actor model in computer science: independent units that communicate via messages.

**Real example — website-builder 5-actor pipeline:**
```
Actor 1: Google Stitch MCP      → prompt → design mockup (PNG/SVG)
Actor 2: ui-ux-promax skill     → mockup → styled design system
Actor 3: framer-motion-builder  → design → animated React components
Actor 4: premium-web-design     → components → production codebase
Actor 5: website-builder-setup  → codebase → deployed site
```
Each actor has clear inputs, outputs, and failure modes. They can be swapped independently.

---

## Workflow

A **Workflow** is a scheduled, autonomous execution of skills and agents triggered by cron or an external event — not by a human prompt. Workflows run without user interaction and produce deliverables (reports, Excel files, emails) on a defined schedule.

This system has 4 workflows, all stored in `workflows/` as `SKILL.md` files executed by Claude's remote trigger system.

**Real example — `workflows/hmz-daily-leads/SKILL.md`:**
```
Schedule: 7:00 AM PKT daily
Trigger: Remote cron via Claude scheduled tasks
Pipeline:
  1. Apollo MCP → search for businesses with paid ad budgets
  2. Vibe Prospecting → enrich entity data
  3. Apify → supplemental data extraction
  4. Score all leads (80+ threshold gate)
  5. Export top 10 to Excel
  6. Draft Gmail email with Excel attachment
  7. Send to hmzainjamil@gmail.com
Zero human input required. Fully autonomous.
```

---

## Automation

An **Automation** is a system-level script or hook that runs outside of Claude's conversation context — triggered by OS events, file changes, git hooks, or LaunchAgent daemons. Automations wire the entire system together at the infrastructure level.

**Real examples from this system:**

| Automation | Trigger | What It Does |
|---|---|---|
| `skill-auto-activate` | `UserPromptSubmit` hook (every prompt) | Keyword-matches prompt → loads exact skills needed |
| `session-learn` | `Stop` hook (session end) | Writes learnings from session to persistent memory |
| `skill-guardian` | File watcher daemon | Detects zombie skills, auto-deactivates |
| `skill-watcher` | LaunchAgent | Watches `~/.claude/skills/` for new files |
| `github-sync` | Manual or keyword trigger | Copies latest skills/agents to GitHub repo |
| `tier0-prompt-inject` | `UserPromptSubmit` hook | Injects model routing rules into every prompt |

The key distinction: Automations run at the OS/shell level. They are invisible to Claude during conversations but shape what Claude sees and does.
