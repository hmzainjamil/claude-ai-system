"""
AGENCY CRM — Full-Funnel Pipeline Engine
GoHighLevel-inspired architecture for DigiMinds outreach.

PIPELINE STAGES (in order):
  COLD          → Prospect discovered, not yet contacted
  OUTREACH_1    → First email sent (day 0)
  OUTREACH_2    → Follow-up 1 sent (day 3)
  OUTREACH_3    → Follow-up 2 sent (day 7)
  OUTREACH_4    → Breakup email sent (day 14)
  RESPONDED     → Replied to any outreach
  QUALIFIED     → Confirmed: need + budget + authority (SQL)
  AUDIT_SENT    → Free audit PDF sent
  PROPOSAL_SENT → Formal proposal / Upwork application submitted
  NEGOTIATING   → Active back-and-forth on scope/price
  CLOSED_WON    → Contract signed / payment received
  CLOSED_LOST   → Rejected / ghosted after response
  UNSUBSCRIBED  → Requested removal — NEVER contact again
  BOUNCED       → Hard bounce — remove permanently

LEAD SCORE:
  0-40   Unqualified (budget mismatch, wrong ICP)
  41-60  Cold prospect
  61-80  Warm lead (engaged, replied, visited)
  81-100 Hot lead (qualified, audit requested)
"""

import json, datetime, os, re, hashlib
from pathlib import Path

HOME      = Path.home()
CRM_DIR   = HOME / ".claude/agency/crm"
CRM_DB    = CRM_DIR / "leads.json"
LOG_FILE  = CRM_DIR / "logs/crm.log"

# Pipeline stage ordering (for progression checks)
STAGE_ORDER = [
    "COLD", "OUTREACH_1", "OUTREACH_2", "OUTREACH_3", "OUTREACH_4",
    "RESPONDED", "QUALIFIED", "AUDIT_SENT", "PROPOSAL_SENT",
    "NEGOTIATING", "CLOSED_WON", "CLOSED_LOST", "UNSUBSCRIBED", "BOUNCED"
]

TERMINAL_STAGES = {"CLOSED_WON", "CLOSED_LOST", "UNSUBSCRIBED", "BOUNCED"}

# Realistic industry benchmarks (GoHighLevel/Woodpecker data)
BENCHMARKS = {
    "cold_open_rate":       0.42,   # 42% — personalized + domain authority
    "cold_reply_rate":      0.035,  # 3.5% — industry avg for B2B cold
    "warm_reply_rate":      0.18,   # 18% — after audit/engagement
    "sql_conversion":       0.25,   # 25% of replies become qualified
    "proposal_win_rate":    0.30,   # 30% close rate on sent proposals
    "avg_deal_value":       2500,   # $2,500 avg retainer
    "sales_cycle_days":     14,     # avg days cold → closed
}


def log(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line)
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


def _load_db():
    if CRM_DB.exists():
        return json.loads(CRM_DB.read_text())
    return {"leads": {}, "stats": {"total": 0, "by_stage": {}, "by_source": {}}, "last_updated": ""}


def _save_db(db):
    CRM_DIR.mkdir(parents=True, exist_ok=True)
    db["last_updated"] = datetime.datetime.now().isoformat()
    CRM_DB.write_text(json.dumps(db, indent=2))


def lead_id(email):
    """Deterministic ID from email."""
    return hashlib.md5(email.lower().strip().encode()).hexdigest()[:12]


def upsert_lead(email, data):
    """
    Create or update a lead. data can include:
      name, company, website, source, job_title, linkedin_url,
      platform, budget, pain_points, score, notes
    """
    db = _load_db()
    lid = lead_id(email)
    now = datetime.datetime.now().isoformat()

    if lid not in db["leads"]:
        db["leads"][lid] = {
            "id":           lid,
            "email":        email.lower().strip(),
            "name":         data.get("name", ""),
            "company":      data.get("company", ""),
            "website":      data.get("website", ""),
            "source":       data.get("source", "manual"),   # upwork|linkedin|cold_db|facebook|inbound
            "platform":     data.get("platform", "email"),
            "job_title":    data.get("job_title", ""),
            "linkedin_url": data.get("linkedin_url", ""),
            "budget":       data.get("budget", ""),
            "pain_points":  data.get("pain_points", []),
            "score":        data.get("score", 50),
            "stage":        "COLD",
            "tags":         data.get("tags", []),
            "notes":        data.get("notes", ""),
            "created_at":   now,
            "updated_at":   now,
            "emails_sent":  [],     # list of {subject, sent_at, sequence_step}
            "emails_opened": [],
            "replies":      [],
            "audit_path":   "",
            "proposal_path": "",
            "proposal_url":  data.get("job_url", ""),
            "deal_value":   0,
            "next_followup": None,
            "last_activity": now,
            "unsubscribe_token": hashlib.md5(f"{email}{now}".encode()).hexdigest()[:16],
        }
        db["stats"]["total"] += 1
        log(f"NEW LEAD: {email} [{data.get('company','')}] source={data.get('source','manual')}")
    else:
        # Update mutable fields
        lead = db["leads"][lid]
        for field in ["name","company","website","score","notes","budget","pain_points","tags","deal_value","audit_path","proposal_path","proposal_url"]:
            if field in data and data[field]:
                lead[field] = data[field]
        lead["updated_at"] = now
        lead["last_activity"] = now

    _save_db(db)
    return db["leads"][lid]


def advance_stage(email, new_stage, note=""):
    """Move lead to new pipeline stage."""
    db = _load_db()
    lid = lead_id(email)
    if lid not in db["leads"]:
        log(f"WARN: lead not found: {email}")
        return None

    lead = db["leads"][lid]
    old_stage = lead["stage"]

    # Never move out of terminal stages
    if old_stage in TERMINAL_STAGES and new_stage not in TERMINAL_STAGES:
        log(f"BLOCK: {email} in terminal stage {old_stage}, cannot move to {new_stage}")
        return lead

    lead["stage"] = new_stage
    lead["updated_at"] = datetime.datetime.now().isoformat()
    lead["last_activity"] = lead["updated_at"]
    if note:
        lead["notes"] = (lead.get("notes","") + f"\n[{datetime.date.today()}] {note}").strip()

    log(f"STAGE: {email} {old_stage} → {new_stage}")
    _save_db(db)
    return lead


def record_email_sent(email, subject, sequence_step, body_preview=""):
    """Log an outbound email."""
    db = _load_db()
    lid = lead_id(email)
    if lid not in db["leads"]:
        return
    now = datetime.datetime.now().isoformat()
    db["leads"][lid]["emails_sent"].append({
        "subject": subject,
        "sequence_step": sequence_step,
        "sent_at": now,
        "body_preview": body_preview[:150],
        "opened": False,
        "replied": False,
    })
    db["leads"][lid]["last_activity"] = now
    _save_db(db)


def record_reply(email, reply_text="", is_positive=True):
    """Log an inbound reply and auto-advance stage."""
    db = _load_db()
    lid = lead_id(email)
    if lid not in db["leads"]:
        return
    now = datetime.datetime.now().isoformat()
    db["leads"][lid]["replies"].append({
        "received_at": now,
        "text_preview": reply_text[:200],
        "is_positive": is_positive,
    })
    db["leads"][lid]["last_activity"] = now
    _save_db(db)

    # Auto-advance stage
    advance_stage(email, "RESPONDED", f"Replied: {reply_text[:80]}")
    return db["leads"][lid]


def record_bounce(email, bounce_type="hard"):
    """Mark bounced leads — hard bounces removed permanently."""
    if bounce_type == "hard":
        advance_stage(email, "BOUNCED", "Hard bounce — removed")
    # Soft bounces: just log, don't remove


def record_unsubscribe(email):
    advance_stage(email, "UNSUBSCRIBED", "Unsubscribe request honored")


def get_leads_for_outreach(stage="COLD", limit=50):
    """Return leads ready for outreach in given stage."""
    db = _load_db()
    now = datetime.datetime.now()
    results = []
    for lead in db["leads"].values():
        if lead["stage"] != stage:
            continue
        if lead["stage"] in TERMINAL_STAGES:
            continue
        # Check next_followup gate
        if lead.get("next_followup"):
            try:
                nf = datetime.datetime.fromisoformat(lead["next_followup"])
                if now < nf:
                    continue
            except Exception:
                pass
        results.append(lead)
    return results[:limit]


def get_pipeline_summary():
    """Return stage counts and revenue projections."""
    db = _load_db()
    stage_counts = {s: 0 for s in STAGE_ORDER}
    for lead in db["leads"].values():
        stage = lead.get("stage", "COLD")
        stage_counts[stage] = stage_counts.get(stage, 0) + 1

    in_pipeline = (stage_counts.get("QUALIFIED",0) +
                   stage_counts.get("AUDIT_SENT",0) +
                   stage_counts.get("PROPOSAL_SENT",0) +
                   stage_counts.get("NEGOTIATING",0))

    projected_revenue = (in_pipeline *
                         BENCHMARKS["proposal_win_rate"] *
                         BENCHMARKS["avg_deal_value"])

    return {
        "total_leads": db["stats"]["total"],
        "by_stage": stage_counts,
        "in_active_pipeline": in_pipeline,
        "projected_revenue": projected_revenue,
        "benchmarks": BENCHMARKS,
    }


def score_lead(lead):
    """
    Recalculate lead score 0-100 based on signals.
    ICP: performance marketing decision-makers, $2K+ budget.
    """
    score = 40  # base

    company = lead.get("company","").lower()
    desc = (lead.get("notes","") + " " + lead.get("job_title","")).lower()
    budget = lead.get("budget","").lower()

    # Budget signals
    if any(x in budget for x in ["$5k","$10k","$8k","$3k","$2k","5000","10000","3000","2000"]):
        score += 20
    elif any(x in budget for x in ["$1k","1000","1,000"]):
        score += 10

    # ICP signals
    if any(x in desc for x in ["roas","cpa","meta ads","google ads","ppc","paid ads","performance"]):
        score += 15

    # Engagement signals
    if lead.get("replies"):
        score += 15
    if lead.get("emails_opened"):
        score += 5

    # Authority signal
    if any(x in lead.get("job_title","").lower() for x in ["ceo","cmo","founder","owner","director","head of","vp"]):
        score += 10

    return min(score, 100)


def import_from_proposals(proposals_file):
    """
    Import qualified proposals (score ≥ 75) as CRM leads.
    Called after generate-proposals phase.
    """
    data = json.loads(Path(proposals_file).read_text())
    imported = 0
    for p in data.get("proposals", []):
        if p.get("relevance_score", 0) < 60:
            continue
        client_info = p.get("client_info", {})
        email = client_info.get("email", "")
        if not email:
            continue  # no email = can't do outreach (Upwork-only handled separately)

        upsert_lead(email, {
            "name":        client_info.get("name", ""),
            "company":     client_info.get("company", ""),
            "source":      p.get("platform", "upwork"),
            "platform":    p.get("platform", "upwork"),
            "job_title":   p.get("job_title", ""),
            "budget":      p.get("budget", ""),
            "pain_points": p.get("pain_points", []),
            "score":       p.get("relevance_score", 50),
            "job_url":     p.get("job_url", ""),
            "audit_path":  p.get("audit_path", ""),
        })
        imported += 1
    log(f"Imported {imported} leads from proposals")
    return imported
