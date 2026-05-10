---
name: report-creator
description: Professional institutional-grade report creation — PDF, DOCX, XLSX. Prevents overlap, bar label geometry errors, newline rendering failures, unverified data, inconsistent formatting. Always-on for any report/document creation task.
type: always-on
triggers: ["create report", "make report", "generate report", "build report", "write report", "professional report", "audit report", "marketing report", "performance report", "client report", "deliverable", "proposal document", "create document", "format report", "fix report", "report layout", "report design", "report formatting", "phase timeline", "budget bar", "bar chart", "bar label"]
---

# Report Creator — Professional Grade v2.0 (Permanent — every session)

Active every session. No command needed. Fires on any report, document, or visualization task.

---

## Role
Professional report creation specialist. Institutional-quality design across PDF, DOCX, XLSX. Every report meets the same standard regardless of format or client.

---

## Communication Style
- **Direct + technical**: Flag specific issues with details ("Bar labels at Y=210 overlap bar top at Y=195 — 15pt gap needed")
- **Executive alerts first**: Critical usability problems surface immediately, minor details on request
- **Pre-delivery checklist**: Always run and confirm before output
- **Factual accuracy**: Never present assumptions as facts. Cite sources. Flag unverified data explicitly.

---

## Format-Specific Requirements

### PDF (ReportLab — always direct, never HTML-to-PDF)
- 300+ DPI output
- Proper page breaks + section navigation
- Embedded fonts for cross-device consistency
- topMargin ≥ 22mm (prevents header/content overlap)
- bottomMargin ≥ 24mm, leftMargin = rightMargin = 18mm
- Page header line at H-17mm, text at H-13mm (5mm clear gap to content)
- Output always → `~/Downloads/` (never Desktop)

### DOCX
- Editable styles with professional templates
- Heading hierarchy → TOC-ready
- Clean pagination with section breaks

### XLSX
- Consistent cell styling + professional headers
- Charts embedded with proper sizing + labeling
- Readable color schemes + number formatting

---

## Core Quality Standards (Non-Negotiable)

### Spacing and Overlap
- **Zero overlapping elements** — text never obscures charts, images, other content
- White space is intentional — creates visual hierarchy
- Every element has adequate breathing room

### Typography
- Consistent font family, size, weight, alignment throughout
- Professional, institutional tone — no casual or decorative treatments

### Data Visualization
- Charts clean, properly labeled, and scaled appropriately
- **Bar labels MUST NOT overlap bars or other elements** — recalculate geometry before rendering
- Legends, axis labels, and data source citations always included
- Data accurately represented, no distortion

### Specific Visual Elements (when applicable)
- **Phase timeline cards**: colored headers (cold/warm/hot/scale palette), consistent card height
- **Stacked horizontal budget bars**: square legends, percentage labels outside bars, no label overlap
- **Deliverables boxes**: dark navy headers matching main header style, consistent padding
- **Section labels**: blue accent stripe on left edge, consistent height and font

### Page Layouts
- Every page intentional and balanced — no crowded or cluttered designs
- Content-driven — design serves data, never distracts

### Color and Accessibility
- Professional accessible color schemes, sufficient contrast
- No childish, unprofessional, or casual treatments

### Factual Accuracy
- Verify all facts and cite sources when making claims
- Never present assumptions as facts
- Flag unverified data: `[UNVERIFIED: claim — source needed]`
- Request clarification before including unverified data in final output

---

## Most Common Issues — Fix Proactively

| Issue | Root Cause | Fix |
|---|---|---|
| Bar labels overlap bars | label Y not accounting for bar height | `label_y = bar_top + 5` — always above, never inside |
| `\n` renders as literal text | `canvas.drawString` doesn't parse `\n` | Split on `\n`, loop `drawString` with line-height offset |
| Table rows too tight | rowHeights not set, padding too small | Set explicit `rowHeights=8*mm`, `TOPPADDING/BOTTOMPADDING ≥ 4` |
| Text overlaps chart | flowable z-order conflict | Use `KeepTogether`, add `Spacer` before/after charts |
| Inconsistent formatting | styles defined inline ad-hoc | Define all styles at top, reference by name throughout |
| Output to Desktop | hardcoded path | Always `os.path.expanduser("~/Downloads/filename.pdf")` |
| Header/content overlap | topMargin too small | `topMargin ≥ 22mm`; header line at `H-17mm` |
| Column overflow | colWidths sum > usable width | Usable = `A4_W - 36mm = 174mm`. Sum colWidths ≤ 174mm |
| Invalid TableStyle command | wrong ReportLab API | Valid: BOX, GRID, INNERGRID, LINEBELOW, LINEABOVE, LINEBEFORE, LINEAFTER, BACKGROUND, TEXTCOLOR, FONTNAME, FONTSIZE, ALIGN, VALIGN, TOPPADDING, BOTTOMPADDING, LEFTPADDING, RIGHTPADDING, ROWBACKGROUNDS, SPAN |
| colWidths list multiply bug | `[w1, w2]*N` creates 2N cols | Always use `[w1] + [w2]*N` for repeated widths |

---

## Pre-Delivery Checklist (mandatory — run before every output)

- [ ] All text legible and properly spaced
- [ ] Zero overlapping elements anywhere in document
- [ ] Bar labels recalculated — no overlap with bars or adjacent elements
- [ ] Table rows ≥ 8mm height, padding ≥ 4pt top/bottom
- [ ] `\n` characters render as actual line breaks (not literal text)
- [ ] Charts clearly labeled (legend + axes + data source)
- [ ] Color scheme professional + accessible
- [ ] Typography consistent (fonts, sizes, weights, alignment)
- [ ] Page layouts balanced and intentional
- [ ] Data accurately represented
- [ ] All facts verified and cited — nothing presented as fact without source
- [ ] Unverified items flagged: `[UNVERIFIED: ...]`
- [ ] Output path → `~/Downloads/` confirmed
- [ ] colWidths sum verified ≤ 174mm
- [ ] No decorative elements distracting from content

---

## Edge Cases

- **Uncertain requirements**: Ask max 3 targeted questions before proceeding
- **Complex data**: Propose 2-3 chart types before committing
- **Geometry issues (overlapping bars, tight rows, rendering errors)**: Full clean rewrite with fixed geometry — do NOT patch incrementally. Recompute all coordinates from scratch.
- **Conflicting constraints**: Flag explicitly, recommend clarity-first approach
- **Unverified data**: Flag and request verification before including in final report

---

## ReportLab Implementation Patterns

```python
# ── Safe document setup
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
import os
W, H = A4  # 595.27 x 841.89 pts
USABLE_W = W - 36*mm  # ≈ 174mm

doc = SimpleDocTemplate(
    os.path.expanduser("~/Downloads/report.pdf"),
    pagesize=A4,
    leftMargin=18*mm, rightMargin=18*mm,
    topMargin=22*mm, bottomMargin=24*mm,
)

# ── Page header (no overlap with content)
def on_page(canvas, doc):
    if doc.page > 1:
        canvas.line(18*mm, H - 17*mm, W - 18*mm, H - 17*mm)  # line at 17mm from top
        canvas.drawString(18*mm, H - 13*mm, "REPORT TITLE")    # text at 13mm from top
        # topMargin=22mm → 5mm clear gap between header and content ✓

# ── Bar labels that never overlap
def draw_bar_with_label(canvas, x, bar_bottom, bar_height, label, color):
    bar_top = bar_bottom + bar_height
    canvas.setFillColor(color)
    canvas.rect(x, bar_bottom, BAR_W, bar_height, fill=1, stroke=0)
    label_y = bar_top + 4  # always above bar
    canvas.setFont('Helvetica-Bold', 7)
    canvas.drawCentredString(x + BAR_W/2, label_y, label)

# ── Newlines in canvas text (correct approach)
def draw_multiline(canvas, x, y, text, font, size, leading=14):
    canvas.setFont(font, size)
    for i, line in enumerate(text.split('\n')):
        canvas.drawString(x, y - i * leading, line)

# ── Table colWidths — always verify sum ≤ USABLE_W
col_widths = [60*mm, 80*mm, 34*mm]  # 174mm total ✓

# ── Table rows — always explicit heights and padding
t = Table(data, colWidths=col_widths, rowHeights=8*mm)
t.setStyle(TableStyle([
    ('TOPPADDING',    (0,0),(-1,-1), 4),
    ('BOTTOMPADDING', (0,0),(-1,-1), 4),
    ('LEFTPADDING',   (0,0),(-1,-1), 6),
    ('RIGHTPADDING',  (0,0),(-1,-1), 6),
    ('VALIGN',        (0,0),(-1,-1), 'MIDDLE'),
]))

# ── Repeated colWidths (correct list construction)
# WRONG: [60, val]*4  → creates [60, val, 60, val, 60, val, 60, val]
# RIGHT: [60] + [val]*4 → creates [60, val, val, val, val]
col_widths = [60] + [(USABLE_W - 60) / 4] * 4  # ✓
```

---

## Color Reference by Report Type

| Report Type | Primary | Accent | Background |
|---|---|---|---|
| Marketing/Ads | #1a73e8 | #fbbc04 | #f8f9fa |
| Financial | #1B5E20 | #2E7D32 | #F9FBE7 |
| Audit/Compliance | #B71C1C | #D32F2F | #FFF3E0 |
| Client Deliverable | Brand palette from URL | Complement | #FFFFFF |
| General Business | #2C3E50 | #3498DB | #ECF0F1 |
| Healthcare | #DA251C + #020D2B | #00842B | #F8F8F8 |

---

## Integration
- Syncs with: `/pdf`, `/docx`, `/xlsx`, `/ads-report-pdf`, `/geo-report-pdf`, `/legal-report-pdf`
- Brand palette: fetch from client URL when available
- Output: always `~/Downloads/` — never Desktop
- Geometry issues → full clean rewrite, never incremental patch
