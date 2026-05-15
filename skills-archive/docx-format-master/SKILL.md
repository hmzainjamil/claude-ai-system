# DOCX Format Master — Zero Repeat Errors

## ACTIVATION
Triggers: docx, word document, .docx, report word, doc format, word report

---

## UNIVERSAL RULE BEFORE ANY DOCX BUILD
Run this checklist mentally before writing a single line of python-docx code:

- [ ] Page margins set explicitly — never rely on defaults
- [ ] All table column widths set explicitly in Inches — never auto
- [ ] No `\n` inside cell text — use separate paragraphs/runs
- [ ] Paragraph spacing set explicitly — `space_after = Pt(0)` unless intentional
- [ ] Font name + size set on every run — never assume style inheritance
- [ ] Images sized explicitly — never insert without width/height
- [ ] Tables always have header row repeated on page break (`tbl.repeat_header_row`)
- [ ] QA: open doc with `python-docx`, count pages, scan for empty sections
- [ ] Output → `~/Downloads/` always
- [ ] Print full output path after saving

---

## LAW 1 — SET MARGINS EXPLICITLY

```python
from docx.shared import Inches, Pt, Cm
from docx import Document

doc = Document()
section = doc.sections[0]
section.page_width  = Inches(8.27)   # A4
section.page_height = Inches(11.69)
section.left_margin   = Cm(2.0)
section.right_margin  = Cm(2.0)
section.top_margin    = Cm(2.0)
section.bottom_margin = Cm(2.0)
```

Never start a doc without setting these. Default margins vary by Word version and locale.

---

## LAW 2 — TABLE COLUMN WIDTHS MUST BE EXPLICIT

```python
# ❌ WRONG — columns auto-size unpredictably
table = doc.add_table(rows=1, cols=3)

# ✅ CORRECT — explicit widths that sum to usable page width
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def set_col_widths(table, widths_cm):
    """widths_cm: list of floats, must sum to usable page width"""
    for row in table.rows:
        for i, cell in enumerate(row.cells):
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            tcW = OxmlElement('w:tcW')
            tcW.set(qn('w:w'), str(int(widths_cm[i] * 567)))  # 567 twips/cm
            tcW.set(qn('w:type'), 'dxa')
            tcPr.append(tcW)

# A4 with 2cm margins: usable = 21 - 4 = 17cm
# 3-col table: widths must sum to ≤ 17cm
set_col_widths(table, [4.0, 9.0, 4.0])  # = 17cm exactly
```

---

## LAW 3 — NEVER USE \n IN CELL TEXT

```python
# ❌ WRONG — creates invisible overflow, not a new row
cell.text = "Line 1\nLine 2"

# ✅ CORRECT — separate paragraphs within cell
p1 = cell.paragraphs[0]
p1.text = "Line 1"
p2 = cell.add_paragraph("Line 2")
```

---

## LAW 4 — FONT MUST BE EXPLICIT ON EVERY RUN

```python
# ❌ WRONG — inherits random style from template
run = para.add_run("Important text")

# ✅ CORRECT
run = para.add_run("Important text")
run.font.name = 'Calibri'
run.font.size = Pt(11)
run.font.bold = False
run.font.color.rgb = RGBColor(0x1A, 0x1A, 0x1A)
```

---

## LAW 5 — PARAGRAPH SPACING MUST BE CONTROLLED

```python
from docx.oxml.ns import qn

def tight_para(para):
    """Zero space before/after, single line spacing"""
    pf = para.paragraph_format
    pf.space_before = Pt(0)
    pf.space_after  = Pt(0)
    pf.line_spacing = Pt(14)

# Apply to every paragraph in tables especially
for row in table.rows:
    for cell in row.cells:
        for para in cell.paragraphs:
            tight_para(para)
```

---

## LAW 6 — IMAGES MUST HAVE EXPLICIT SIZE

```python
# ❌ WRONG — image fills page or renders at 1px
doc.add_picture('chart.png')

# ✅ CORRECT
doc.add_picture('chart.png', width=Inches(6.0), height=Inches(3.5))
```

Always calculate aspect ratio first:
```python
from PIL import Image
img = Image.open('chart.png')
w, h = img.size
target_width = Inches(6.0)
target_height = target_width * h / w
doc.add_picture('chart.png', width=target_width, height=target_height)
```

---

## LAW 7 — CHART/DIAGRAM DATA MUST MATCH DISPLAY

When embedding matplotlib/plotly charts into DOCX:
```python
import matplotlib
matplotlib.use('Agg')  # non-interactive backend — ALWAYS set this
import matplotlib.pyplot as plt
import io

# Generate chart
fig, ax = plt.subplots(figsize=(8, 4), dpi=150)
ax.bar(labels, values)
ax.set_title(title, fontsize=14, fontweight='bold')
plt.tight_layout()

# Save to buffer — never save temp file
buf = io.BytesIO()
fig.savefig(buf, format='png', dpi=150, bbox_inches='tight')
buf.seek(0)
plt.close(fig)

# Insert with correct size
doc.add_picture(buf, width=Inches(6.0))
```

Chart data and table data MUST come from the same source variable — never copy-paste numbers.

---

## LAW 8 — REPEAT HEADER ROW ON PAGE BREAKS

```python
# After creating table with header row:
def repeat_table_header(table):
    tr = table.rows[0]._tr
    trPr = tr.get_or_add_trPr()
    tblHeader = OxmlElement('w:tblHeader')
    tblHeader.set(qn('w:val'), 'true')
    trPr.append(tblHeader)

repeat_table_header(table)
```

---

## LAW 9 — QA BEFORE DELIVERY

```python
import os
output_path = os.path.expanduser('~/Downloads/report.docx')
doc.save(output_path)

# QA: re-open and verify
from docx import Document as D
qa = D(output_path)
para_count = len(qa.paragraphs)
table_count = len(qa.tables)
print(f"QA: {para_count} paragraphs, {table_count} tables")
for i, tbl in enumerate(qa.tables):
    print(f"  Table {i+1}: {len(tbl.rows)} rows × {len(tbl.columns)} cols")

print(f"\nSaved: {output_path}")
assert os.path.getsize(output_path) > 5000, "File too small — likely broken"
```

---

## STANDARD HELPER TEMPLATE

```python
import os, io
from docx import Document
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUTPUT = os.path.expanduser('~/Downloads/report.docx')

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.27), Inches(11.69)
sec.left_margin = sec.right_margin = sec.top_margin = sec.bottom_margin = Cm(2.0)

USABLE_CM = 17.0  # 21 - 2*2

def add_heading(doc, text, level=1, color='1A1A2E'):
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = RGBColor.from_string(color)
    h.paragraph_format.space_before = Pt(12)
    h.paragraph_format.space_after  = Pt(4)
    return h

def add_table(doc, headers, rows, col_widths_cm):
    assert abs(sum(col_widths_cm) - USABLE_CM) < 0.5, \
        f"Columns {sum(col_widths_cm):.1f}cm ≠ {USABLE_CM}cm"
    tbl = doc.add_table(rows=1+len(rows), cols=len(headers))
    tbl.style = 'Table Grid'
    # Header row
    hdr = tbl.rows[0]
    for i, h in enumerate(headers):
        cell = hdr.cells[i]
        cell.text = h
        run = cell.paragraphs[0].runs[0]
        run.font.bold = True
        run.font.size = Pt(10)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        cell._tc.get_or_add_tcPr()
    # Data rows
    for ri, row_data in enumerate(rows):
        row = tbl.rows[ri+1]
        for ci, val in enumerate(row_data):
            row.cells[ci].text = str(val)
            for para in row.cells[ci].paragraphs:
                para.paragraph_format.space_before = Pt(0)
                para.paragraph_format.space_after  = Pt(0)
    # Set widths
    for row in tbl.rows:
        for i, cell in enumerate(row.cells):
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            tcW = OxmlElement('w:tcW')
            tcW.set(qn('w:w'), str(int(col_widths_cm[i] * 567)))
            tcW.set(qn('w:type'), 'dxa')
            tcPr.append(tcW)
    return tbl

def add_chart(doc, fig, width_inches=6.0):
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=150, bbox_inches='tight')
    buf.seek(0)
    plt.close(fig)
    doc.add_picture(buf, width=Inches(width_inches))

doc.save(OUTPUT)
print(f"Saved: {OUTPUT} ({os.path.getsize(OUTPUT):,} bytes)")
```
