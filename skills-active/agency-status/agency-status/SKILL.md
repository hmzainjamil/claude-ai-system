# Agency Status — Pipeline & Health Dashboard
## Triggers: agency status, pipeline status, client status, agency health, bdm status, jobs status

## STATUS CHECKS
```bash
# BDM pipeline
~/.claude/bin/hmz-bdm-state-update

# Active clients
~/.claude/bin/agency-run status

# Job sweep status
ls ~/.claude/bdm-state/ 2>/dev/null

# Open Design server
curl -s http://127.0.0.1:51827/health
```

## DASHBOARD ITEMS
- Active clients: count + MRR
- Proposals out: count + value
- Jobs found today: by platform
- Emails sent: response rate
- Retainers closing: pipeline value
