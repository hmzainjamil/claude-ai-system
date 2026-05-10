---
name: reportlab-pdf-master
description: "Universal ReportLab PDF builder skill — auto-activates on ANY report/PDF/document task. Enforces 12 hard laws learned from real failures. Foolproof, flawless, zero repeat errors. Covers: column widths, cell wrapping, blank pages, style registry, padding math, pymupdf QA, branding."
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

# ReportLab PDF Master — Universal Auto-Activated Skill

**TRIGGER:** Activates on ANY prompt containing: report, pdf, audit, xlsx, docx, pptx, document, diagnostic, deliverable, one-pager, deck, guide, format, layout, design

**MANDATE:** Apply ALL 12 laws below BEFORE writing a single line of PDF code. No exceptions. No skipping. These were learned from real, repeated failures that wasted hours.

---

## PRE-BUILD CHECKLIST (run mentally before every script)

```
[ ] Margins set to 12mm → UW_MM ≈ 186mm
[ ] cw() asserts total ≤ UW_MM − 0.5
[ ] ALL long cell text wrapped in P() objects
[ ] No explicit PageBreak() between sections — use CondPageBreak(80*mm)
[ ] Style registry uses getSampleStyleSheet() + idempotent reg()
[ ] Section headers use counter-based unique style names
[ ] Narrow accent columns have zero padding
[ ] pymupdf QA block at end of every script
[ ] Branding = Hafiz Muhammad Zulqarnain (never DigiMinds)
[ ] Output → ~/Downloads/ always
[ ] pt vs mm units correct (padding in TABLE is POINTS, not mm)
[ ] CondPageBreak imported from reportlab.platypus
```

---

## MANDATORY BOILERPLATE — START EVERY SCRIPT WITH THIS

```python
#!/usr/bin/env python3
import os
import fitz  # pymupdf — for QA verification at end
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
    TableStyle, PageBreak, KeepTogether, HRFlowable, CondPageBreak)
from reportlab.lib.colors import HexColor

OUT = os.path.expanduser("~/Downloads/YourReport.pdf")
PW, PH = A4

# ── MARGINS — always 12mm ─────────────────────────────────────────
LM = RM = 12 * mm          # → UW_MM ≈ 186mm
TM = 30 * mm
BM = 28 * mm
UW    = PW - LM - RM       # points (~527pt)
UW_MM = UW / mm            # mm (~186mm)

# ── COLUMN WIDTH HELPER — asserts before crash ────────────────────
def cw(*mm_vals):
    total = sum(mm_vals)
    assert total <= UW_MM - 0.5, f"colWidths {total:.1f}mm EXCEEDS {UW_MM:.1f}mm limit — fix columns"
    return [v * mm for v in mm_vals]

# ── STYLE REGISTRY — idempotent, no duplicate name crashes ────────
ss = getSampleStyleSheet()
def reg(name, parent='Normal', **kw):
    try:
        ss.add(ParagraphStyle(name, parent=ss[parent], **kw))
    except KeyError:
        pass  # already registered — safe to ignore
    return ss[name]

# ── PARAGRAPH SHORTCUT ────────────────────────────────────────────
def P(text, style='Body'):
    return Paragraph(text, ss[style])

# ── SECTION HEADER — unique counter prevents name collision ───────
_sec_n = [0]
def section(title, color=HexColor('#1a237e')):
    _sec_n[0] += 1
    n = _sec_n[0]
    pstyle = ParagraphStyle(f'SH_{n}', fontSize=13, fontName='Helvetica-Bold',
        textColor=color, leading=17, spaceBefore=0, spaceAfter=0)
    data = [['', Paragraph(title, pstyle)]]
    t = Table(data, colWidths=[5*mm, UW - 5*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(0,0), color),
        ('LEFTPADDING',   (0,0),(0,0), 0),   # ← ZERO PADDING on narrow bar (prevents negative availWidth)
        ('RIGHTPADDING',  (0,0),(0,0), 0),
        ('TOPPADDING',    (0,0),(0,0), 0),
        ('BOTTOMPADDING', (0,0),(0,0), 0),
        ('LEFTPADDING',   (1,0),(1,0), 10),
        ('RIGHTPADDING',  (1,0),(1,0), 8),
        ('TOPPADDING',    (1,0),(1,0), 8),
        ('BOTTOMPADDING', (1,0),(1,0), 8),
        ('VALIGN',        (0,0),(-1,0), 'MIDDLE'),
    ]))
    return [Spacer(1, 6*mm), t, Spacer(1, 4*mm)]

# ── TABLE BUILDER — all cells auto-wrap via Paragraph ─────────────
def tbl(rows, widths_mm, hdr_rows=1, alt=True, hdr_bg=HexColor('#1a237e'),
        hdr_fg=colors.white, alt_bg=HexColor('#f8f9fa')):
    pad = [
        ('TOPPADDING',    (0,0),(-1,-1), 5),   # 5pt NOT 5mm
        ('BOTTOMPADDING', (0,0),(-1,-1), 5),
        ('LEFTPADDING',   (0,0),(-1,-1), 7),
        ('RIGHTPADDING',  (0,0),(-1,-1), 7),
        ('VALIGN',        (0,0),(-1,-1), 'TOP'),
        ('GRID',          (0,0),(-1,-1), 0.5, HexColor('#dee2e6')),
    ]
    for ri in range(hdr_rows):
        pad += [
            ('BACKGROUND', (0,ri),(-1,ri), hdr_bg),
            ('TEXTCOLOR',  (0,ri),(-1,ri), hdr_fg),
            ('FONTNAME',   (0,ri),(-1,ri), 'Helvetica-Bold'),
            ('FONTSIZE',   (0,ri),(-1,ri), 9),
            ('ALIGN',      (0,ri),(-1,ri), 'CENTER'),
        ]
    if alt:
        for ri in range(hdr_rows, len(rows)):
            if (ri - hdr_rows) % 2 == 1:
                pad.append(('BACKGROUND', (0,ri),(-1,ri), alt_bg))
    t = Table(rows, colWidths=cw(*widths_mm), repeatRows=hdr_rows)
    t.setStyle(TableStyle(pad))
    return t

# ── ALERT BOX — full width, no overflow ──────────────────────────
def alert(text, style='AlertR', bg=HexColor('#ffebee'), border=HexColor('#c62828')):
    data = [[P(text, style)]]
    t = Table(data, colWidths=[UW])   # UW in points — always correct width
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0),(-1,-1), bg),
        ('BOX',           (0,0),(-1,-1), 1.5, border),
        ('TOPPADDING',    (0,0),(-1,-1), 9),
        ('BOTTOMPADDING', (0,0),(-1,-1), 9),
        ('LEFTPADDING',   (0,0),(-1,-1), 12),
        ('RIGHTPADDING',  (0,0),(-1,-1), 12),
    ]))
    return [t, Spacer(1, 3*mm)]

# ─────────────────────────────────────────────────────────────────
# REGISTER STYLES HERE (all at top, once, idempotent)
# ─────────────────────────────────────────────────────────────────
NAV  = HexColor('#1a237e')
RED  = HexColor('#c62828')
GRN  = HexColor('#2e7d32')
ORG  = HexColor('#e65100')
BODY = HexColor('#212529')
DGRY = HexColor('#6c757d')
WHITE = colors.white

reg('Body',    fontSize=10.5, leading=15, textColor=BODY, spaceAfter=4)
reg('BodyJ',   fontSize=10.5, leading=15, textColor=BODY, spaceAfter=4, alignment=TA_JUSTIFY)
reg('Bold',    fontSize=10.5, leading=15, textColor=BODY, fontName='Helvetica-Bold')
reg('Small',   fontSize=9,    leading=13, textColor=DGRY)
reg('Cell',    fontSize=9.5,  leading=13, textColor=BODY, spaceAfter=1, spaceBefore=1)
reg('CellB',   fontSize=9.5,  leading=13, textColor=BODY, fontName='Helvetica-Bold', spaceAfter=1)
reg('CellR',   fontSize=9.5,  leading=13, textColor=RED,  fontName='Helvetica-Bold', spaceAfter=1)
reg('CellG',   fontSize=9.5,  leading=13, textColor=GRN,  fontName='Helvetica-Bold', spaceAfter=1)
reg('CellO',   fontSize=9.5,  leading=13, textColor=ORG,  fontName='Helvetica-Bold', spaceAfter=1)
reg('CellW',   fontSize=9.5,  leading=13, textColor=WHITE,fontName='Helvetica-Bold', spaceAfter=1, alignment=TA_CENTER)
reg('CellSm',  fontSize=8.5,  leading=12, textColor=BODY, spaceAfter=1)
reg('CellSmR', fontSize=8.5,  leading=12, textColor=RED,  fontName='Helvetica-Bold', spaceAfter=1)
reg('CellSmG', fontSize=8.5,  leading=12, textColor=GRN,  fontName='Helvetica-Bold', spaceAfter=1)
reg('CellSmO', fontSize=8.5,  leading=12, textColor=ORG,  fontName='Helvetica-Bold', spaceAfter=1)
reg('AlertR',  fontSize=10,   leading=14, textColor=RED,  fontName='Helvetica-Bold')
reg('AlertG',  fontSize=10,   leading=14, textColor=GRN,  fontName='Helvetica-Bold')
reg('AlertN',  fontSize=9.5,  leading=13, textColor=BODY)
reg('AlertO',  fontSize=10,   leading=14, textColor=ORG,  fontName='Helvetica-Bold')
```

---

## THE 12 HARD LAWS — NEVER VIOLATE

### LAW 1 — EVERY LONG CELL = Paragraph() OBJECT

Plain strings do NOT word-wrap. They overflow the page silently.

```python
# ❌ KILLS THE PAGE — text flies off right edge
['retirement calculator, 401k calculator, nerdwallet, ramsey, savings...']

# ✅ WRAPS CLEANLY
[P('retirement calculator, 401k calculator, nerdwallet, ramsey, savings...', 'CellSm')]
```

**Threshold:** Any cell text > ~15 characters MUST be a `P()` object.
Short values (`'0'`, `'YES'`, `'$1.55'`, `'64'`) can stay as plain strings.

---

### LAW 2 — COLUMN WIDTHS MUST ACCOUNT FOR CELL PADDING

Padding in ReportLab Table `TableStyle` commands is in **POINTS, not mm**.
`('TOPPADDING', ..., 5)` = 5pt = 1.76mm, NOT 5mm.

**Available text width formula:**
```
available_mm = column_mm - (leftPad_pt + rightPad_pt) / 2.835
```

With standard 7+7pt padding: `available = column_mm - 4.94mm`

| Column mm | Available text mm | Max chars at 8.5pt |
|---|---|---|
| 13mm | 8.06mm | ~5 chars |
| 16mm | 11.06mm | ~7 chars |
| 20mm | 15.06mm | ~10 chars |

**Known minimums:**
- `"ENABLED"` (7 chars, 8.5pt) → needs **20mm** column minimum
- `"PAUSED"` (6 chars, 8.5pt) → needs **18mm** column minimum
- `"$270.74"` (7 chars, 8.5pt) → needs **20mm** column minimum
- `"1,302"` (5 chars, 8.5pt) → needs **15mm** column minimum

---

### LAW 3 — ALWAYS ASSERT COLUMN TOTAL IN cw() HELPER

```python
def cw(*mm_vals):
    total = sum(mm_vals)
    assert total <= UW_MM - 0.5, f"colWidths {total:.1f}mm EXCEEDS {UW_MM:.1f}mm"
    return [v * mm for v in mm_vals]
```

**A4 usable widths by margin:**
| Margins | UW_MM | Max table |
|---|---|---|
| LM=RM=12mm | ~186mm | 185.5mm |
| LM=RM=15mm | ~180mm | 179.5mm |
| LM=RM=20mm | ~170mm | 169.5mm |

**Always use 12mm margins.** Wider margins eat too much space.

---

### LAW 4 — NEVER USE PageBreak() BETWEEN SECTIONS — USE CondPageBreak

`PageBreak()` between sections creates blank pages when a section fits on one page.

```python
# ❌ CREATES BLANK PAGE if section fits on current page
story += my_section_content
story.append(PageBreak())       # → blank next page, content pushed 2 pages ahead

# ✅ ONLY BREAKS if <80mm remains — no blank pages ever
story += my_section_content
story.append(CondPageBreak(80*mm))
```

**Rules:**
- `PageBreak()` → only for cover page or the very first page
- `CondPageBreak(80*mm)` → between ALL other sections
- `CondPageBreak(50*mm)` → for tighter sections that should stay closer

---

### LAW 5 — STYLE REGISTRY: getSampleStyleSheet() + IDEMPOTENT reg()

Never create `ParagraphStyle('name', ...)` twice with the same name.
Second call crashes or silently overwrites.

```python
# ❌ CRASHES on second call
ParagraphStyle('Body', fontSize=10)  # call 1
ParagraphStyle('Body', fontSize=11)  # call 2 → KeyError or wrong style

# ✅ SAFE — idempotent, skip if already registered
ss = getSampleStyleSheet()
def reg(name, parent='Normal', **kw):
    try:
        ss.add(ParagraphStyle(name, parent=ss[parent], **kw))
    except KeyError:
        pass
    return ss[name]
```

For **section headers** called in a loop → use counter:
```python
_sec_n = [0]
def section(title):
    _sec_n[0] += 1
    pstyle = ParagraphStyle(f'SH_{_sec_n[0]}', ...)  # always unique
```

---

### LAW 6 — NARROW ACCENT COLUMNS = ZERO PADDING

A 5mm color-bar column with 6pt left+right padding = negative available width → crash.

```python
# ❌ CRASHES — 5mm col, 6pt padding each side = negative space
t.setStyle(TableStyle([('LEFTPADDING', (0,0),(0,-1), 6)]))

# ✅ CORRECT — zero padding on narrow decorative columns
t.setStyle(TableStyle([
    ('LEFTPADDING',   (0,0),(0,-1), 0),
    ('RIGHTPADDING',  (0,0),(0,-1), 0),
    ('TOPPADDING',    (0,0),(0,-1), 0),
    ('BOTTOMPADDING', (0,0),(0,-1), 0),
]))
```

---

### LAW 7 — ROW HEIGHT MATH (plan before you code)

```
row_height_mm = (top_pad_pt + bottom_pad_pt + font_leading_pt) / 2.835
```

With standard tbl() padding (5pt + 5pt) and CellSm (leading=12pt):
```
row_height = (5 + 5 + 12) / 2.835 = 7.76mm per row
```

A4 usable content height with TM=30mm, BM=28mm:
```
content_height = 841.8pt - (30+28)*2.835 = 677.8pt = 239mm
```

**Max rows per page** at 7.76mm/row = `239 / 7.76 = ~30 rows`
For large tables (>25 rows), expect multi-page overflow — that's fine, just don't force-keep-together.

---

### LAW 8 — ALWAYS VERIFY WITH pymupdf AFTER BUILD

This QA block is MANDATORY at the end of every PDF script:

```python
# ── QA CHECK ─────────────────────────────────────────────────────
doc_qa = fitz.open(OUT)
issues = []
for pn in range(len(doc_qa)):
    txt = doc_qa[pn].get_text().strip()
    if len(txt) < 80:
        issues.append(f"BLANK PAGE {pn+1} — only {len(txt)} chars!")
doc_qa.close()

if issues:
    print("⚠ QA FAILED:")
    for i in issues: print(f"  {i}")
else:
    print(f"✓ QA PASSED — {len(doc_qa)} pages, no blank pages")
print(f"✓ PDF → {OUT}  ({os.path.getsize(OUT)//1024}KB)")
```

**If any page < 80 chars → STOP, do not deliver. Fix the blank page first.**

Also render suspect pages for visual check:
```python
import fitz
doc = fitz.open(path)
page = doc[page_number - 1]  # 0-indexed
pix = page.get_pixmap(matrix=fitz.Matrix(2.5, 2.5))
pix.save(f"/tmp/check_page_{page_number}.png")
# Then: Read tool → view the PNG
```

---

### LAW 9 — STANDARD BRANDING (Hafiz Muhammad Zulqarnain)

Every report uses:
```python
# Header right
'Hafiz Muhammad Zulqarnain  ·  May 20XX  ·  Confidential'

# Cover bar
'HAFIZ MUHAMMAD ZULQARNAIN  ·  PERFORMANCE INTELLIGENCE UNIT'

# Cover subtitle
'Prepared by Hafiz Muhammad Zulqarnain  ·  Data via Windsor.ai MCP Connector  ·  Confidential & Proprietary'

# PDF metadata
author='Hafiz Muhammad Zulqarnain'
```

**NEVER use 'DigiMinds' anywhere in any report.**

---

### LAW 10 — OUTPUT PATH ALWAYS ~/Downloads/

```python
OUT = os.path.expanduser("~/Downloads/FolderName/ReportName.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
```

Never Desktop, never /tmp, never current directory.

---

### LAW 11 — alert() MUST USE UW (points), NOT UW_MM

```python
# ❌ WRONG — UW_MM is in mm, not points
Table(data, colWidths=[UW_MM])         # crashes or wrong size

# ✅ CORRECT — UW is already in points
Table(data, colWidths=[UW])            # correct
```

The `cw()` helper converts mm → points. For single full-width cells, use `UW` directly (already in points).

---

### LAW 12 — MULTI-PAGE TABLES: USE repeatRows, NOT KeepTogether

Large tables (>15 rows) should split naturally across pages with repeating headers.

```python
# ✅ CORRECT — table splits, header repeats on each page
t = Table(rows, colWidths=cw(*widths_mm), repeatRows=1)

# ❌ WRONG — KeepTogether on large tables creates blank pages or pushes entire table off page
story.append(KeepTogether([large_table]))  # DO NOT do this for big tables
```

`KeepTogether` is only for small elements (section header + first 2 rows, alert + following paragraph).

---

## COMMON COLUMN LAYOUTS (tested, validated)

### 4-column audit table (186mm usable):
```python
tbl(rows, [34, 16, 110, 24])   # Category | Priority | Keywords | Savings = 184mm ✓
tbl(rows, [58, 32, 46, 48])    # Metric | Value | Status | Action = 184mm ✓
tbl(rows, [8, 72, 80, 22])     # # | Issue | Evidence | Priority = 182mm ✓
```

### 5-column:
```python
tbl(rows, [10, 32, 66, 52, 22])   # # | Fix | Steps | Result | Timeline = 182mm ✓
tbl(rows, [32, 22, 22, 32, 74])   # Targeting | Allowed | Prec | Phase | Notes = 182mm ✓
```

### 3-column:
```python
tbl(rows, [10, 36, 138])   # Step | Action | Instructions = 184mm ✓
tbl(rows, [10, 44, 130])   # Step | Action | Details = 184mm ✓
tbl(rows, [36, 148])       # Timeframe | What to Expect = 184mm ✓
tbl(rows, [42, 70, 72])    # Factor | Option A | Option B = 184mm ✓
```

### 10-column raw data appendix:
```python
tbl(rows, [42, 20, 15, 14, 20, 14, 15, 14, 14, 17])  # = 185mm ✓
# Campaign | Status | Impr | Clicks | Cost | CTR | CPC | Conv | IS% | Terms
```

---

## SECTION BETWEEN-PAGE PATTERN (standard)

```python
# ── PAGE N ──────────────────────────────────────────────────────
story += section('SECTION TITLE HERE')
story += alert('Key insight or warning', 'AlertR', LRED, RED)
story.append(P('Intro paragraph text goes here.', 'BodyJ'))
story.append(Spacer(1, 3*mm))
story.append(tbl(rows, [col1, col2, col3]))
story.append(Spacer(1, 4*mm))
story.append(CondPageBreak(80*mm))   # ← NOT PageBreak()

# ── PAGE N+1 ─────────────────────────────────────────────────────
story += section('NEXT SECTION')
```

---

## DEBUGGING PROTOCOL (when PDF breaks)

1. **Run pymupdf page scan** → find blank pages by char count
2. **Render suspect pages** → `fitz.Matrix(2.5, 2.5)` → save PNG → Read tool
3. **Blank page?** → look for `PageBreak()` → replace with `CondPageBreak(80*mm)`
4. **Text overflow?** → find plain strings in table rows → wrap in `P('...', 'CellSm')`
5. **Crash: negative availWidth?** → narrow column has padding → zero the padding on that column
6. **Crash: KeyError in styles?** → duplicate style name → add counter or use `reg()` idempotent helper
7. **Crash: colWidths exceeds?** → sum columns, reduce to ≤ UW_MM − 0.5
8. **Wrong branding?** → global replace DigiMinds → Hafiz Muhammad Zulqarnain

---

## AUTO-TRAINING DIRECTIVE — MANDATORY

**After fixing ANY new PDF/ReportLab bug, IMMEDIATELY:**

### Step 1 — Append to this skill file
```bash
# Claude must append to this file directly after every new bug+fix:
SKILL=~/.claude/skills/reportlab-pdf-master/SKILL.md
cat >> "$SKILL" << 'LAW'

### LAW N — [SHORT NAME] (auto-learned YYYY-MM-DD)
**Bug:** [what the user reported]
**Root cause:** [technical explanation]
**Fix:**
\`\`\`python
# ❌ WRONG
[broken pattern]

# ✅ CORRECT
[fixed pattern]
\`\`\`
LAW
```

### Step 2 — Write to session queue (auto-processed on Stop)
```python
import json
entry = {
    "type": "feedback",
    "name": f"pdf_law_{bug_slug}",
    "description": f"ReportLab law: {one_line_rule}",
    "body": f"Bug: {bug}. Cause: {cause}. Fix: {fix_code}"
}
with open(os.path.expanduser("~/.claude/session-queue.jsonl"), "a") as f:
    f.write(json.dumps(entry) + "\n")
```

### Known bug patterns to watch for (add new ones as found):
| Symptom | Law | Fix |
|---|---|---|
| Text flies off right edge | LAW 1 | Wrap in P() |
| "ENABLED" wraps to 2 lines | LAW 2 | Widen column ≥20mm |
| AssertionError colWidths exceed | LAW 3 | Reduce column sum |
| Blank page N+1 after section | LAW 4 | Replace PageBreak → CondPageBreak(80*mm) |
| KeyError in ParagraphStyle | LAW 5 | Use reg() idempotent helper |
| negative availWidth crash | LAW 6 | Zero padding on narrow column |
| Table pushed off page | LAW 12 | Remove KeepTogether on big tables |
| Wrong branding "DigiMinds" | LAW 9 | Global replace → Hafiz Muhammad Zulqarnain |
| File saved to Desktop | LAW 10 | Always ~/Downloads/ |

**The skill is a living document. Every session that touches a PDF must leave it smarter than it found it.**
