---
name: redflame-daily-ops
description: RedFlame daily ops: MRR check + content queue + churn pulse via MAE
---

Run RedFlame AI Academy daily operations check. Do all 3 steps:

1. **MRR check** — run: bash ~/.claude/workflows/redflame/redflame-mae-tasks.sh "revenue report"
   Report the output. If STRIPE_SECRET_KEY is set, hit the real API. Otherwise report stub status.

2. **Content queue check** — check if ~/Downloads/redflame-output/content-queue.json exists. If not, trigger: bash ~/.claude/workflows/redflame/redflame-mae-tasks.sh "weekly content" "AI workflow automation for creative directors"

3. **Churn pulse** — check if BREVO_API_KEY is set in env. If set, report it's active. If not, report: "BREVO_API_KEY missing — wire at brevo.com free tier to activate churn monitoring"

Output a caveman-style daily ops summary:
- MRR status
- Content queue status  
- Churn monitoring status
- 1 action item for today

Save summary to ~/Downloads/redflame-output/daily-ops-YYYY-MM-DD.md