# PPTX Format Master — Zero Repeat Errors

## ACTIVATION
Triggers: pptx, powerpoint, presentation, .pptx, slide deck, slides, deck

---

## UNIVERSAL RULE BEFORE ANY PPTX BUILD
Checklist before writing any python-pptx code:

- [ ] Slide dimensions set explicitly — never default
- [ ] Every text box has explicit left/top/width/height
- [ ] Every text frame has explicit font name, size, color on every run
- [ ] Text overflow prevention: calculate char count vs box width before placing
- [ ] Margins on text frames set explicitly — default is too large
- [ ] Charts use the same data variable as slide tables — never separate hardcoded sets
- [ ] Chart data synced with title/subtitle text — manually verified
- [ ] Images sized to fit placeholder — never raw insert
- [ ] No auto-fit text — disable word_wrap where wrapping would break layout
- [ ] QA: open pptx with python-pptx, verify slide count and text on each slide
- [ ] Output → `~/Downloads/` always

---

## LAW 1 — SLIDE DIMENSIONS MUST BE EXPLICIT

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor

prs = Presentation()

# ✅ ALWAYS set slide size explicitly
prs.slide_width  = Inches(13.33)   # Widescreen 16:9
prs.slide_height = Inches(7.5)

# OR for standard 4:3
prs.slide_width  = Inches(10)
prs.slide_height = Inches(7.5)

# NEVER use prs.slide_layouts[x] without checking what layout x actually is
layout = prs.slide_layouts[6]  # 6 = blank — safest for custom layouts
slide = prs.slides.add_slide(layout)
```

---

## LAW 2 — ALL SHAPES MUST HAVE EXPLICIT POSITION AND SIZE

```python
# ❌ WRONG — position undefined, overlaps other elements
txBox = slide.shapes.add_textbox(0, 0, 0, 0)

# ✅ CORRECT — every dimension explicit
from pptx.util import Inches, Pt

left   = Inches(0.5)
top    = Inches(1.0)
width  = Inches(12.33)   # slide width (13.33) - margins (0.5+0.5)
height = Inches(1.0)

txBox = slide.shapes.add_textbox(left, top, width, height)
```

Position math for 16:9 slide (13.33" × 7.5"):
```
Safe zone: left=0.4", top=0.3", right=12.93", bottom=7.2"
Usable width = 12.53"
Usable height = 6.9"
```

---

## LAW 3 — FONT MUST BE EXPLICIT ON EVERY RUN

```python
# ❌ WRONG — inherits random font from template
tf = txBox.text_frame
tf.text = "Revenue Growth"

# ✅ CORRECT
tf = txBox.text_frame
tf.word_wrap = False  # disable for headlines; enable for body
tf.margin_left   = Pt(6)
tf.margin_right  = Pt(6)
tf.margin_top    = Pt(3)
tf.margin_bottom = Pt(3)

p = tf.paragraphs[0]
p.alignment = PP_ALIGN.LEFT

run = p.add_run()
run.text = "Revenue Growth"
run.font.name  = 'Calibri'
run.font.size  = Pt(28)
run.font.bold  = True
run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
```

---

## LAW 4 — TEXT OVERFLOW PREVENTION

Before placing text, calculate if it fits:
```python
def fits_in_box(text, font_size_pt, box_width_inches, box_height_inches,
                chars_per_inch=9.5, lines_per_inch=None):
    """Rough fit check — use before placing text"""
    if lines_per_inch is None:
        lines_per_inch = 72 / (font_size_pt * 1.3)
    chars_per_line = box_width_inches * chars_per_inch * (12 / font_size_pt)
    lines_needed   = max(1, len(text) / chars_per_line)
    height_needed  = lines_needed / lines_per_inch
    return height_needed <= box_height_inches

# Example
if not fits_in_box(long_text, 14, 12.33, 2.0):
    # Split text or reduce font size
    long_text = long_text[:200] + '...'
```

---

## LAW 5 — CHARTS MUST MATCH ALL SLIDE TEXT

When a slide shows "CTR: 3.2%" in a text box AND a chart:
```python
# ❌ WRONG — two separate data sources
chart_data.add_series('CTR', (0.031, 0.042, 0.028))  # from API
slide_text = f"Average CTR: {avg_ctr:.1%}"            # calculated separately

# ✅ CORRECT — one source, one calculation
raw_ctrs = [0.031, 0.042, 0.028]  # ONE source
avg_ctr  = sum(raw_ctrs) / len(raw_ctrs)
chart_data.add_series('CTR', tuple(raw_ctrs))         # same list
slide_text = f"Average CTR: {avg_ctr:.1%}"            # same calculation
```

---

## LAW 6 — CHARTS MUST FIT IN THEIR BOUNDING BOX

```python
from pptx.util import Inches
from pptx.chart.data import ChartData
from pptx import Presentation
from pptx.enum.chart import XL_CHART_TYPE

# Always specify chart size to fit the slide zone
chart_data = ChartData()
chart_data.categories = ['Jan', 'Feb', 'Mar']
chart_data.add_series('Revenue', (120000, 145000, 132000))

left   = Inches(0.5)
top    = Inches(2.5)
width  = Inches(6.0)    # explicit
height = Inches(4.0)    # explicit

chart = slide.shapes.add_chart(
    XL_CHART_TYPE.COLUMN_CLUSTERED, left, top, width, height, chart_data
).chart

# Format chart
chart.has_title = True
chart.chart_title.text_frame.text = "Monthly Revenue"
chart.chart_title.text_frame.paragraphs[0].runs[0].font.size = Pt(14)
chart.chart_title.text_frame.paragraphs[0].runs[0].font.bold = True
```

---

## LAW 7 — BACKGROUND COLOR ON EVERY SLIDE

```python
from pptx.dml.color import RGBColor
from pptx.oxml.ns import qn
from lxml import etree

def set_slide_background(slide, hex_color='FFFFFF'):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = RGBColor.from_string(hex_color)
```

---

## LAW 8 — TABLE COLUMN WIDTHS IN PPTX

```python
from pptx.util import Inches

# Adding a table — ALWAYS set column widths
rows, cols = len(data)+1, len(headers)
left, top = Inches(0.5), Inches(2.0)
width, height = Inches(12.33), Inches(0.4 * (rows))

tbl = slide.shapes.add_table(rows, cols, left, top, width, height).table

# Set column widths — must sum to `width`
col_widths = [Inches(3.0), Inches(2.0), Inches(2.0), Inches(2.0), Inches(3.33)]
for i, w in enumerate(col_widths):
    tbl.columns[i].width = w

# Set row heights
for i in range(rows):
    tbl.rows[i].height = Inches(0.4)
```

---

## LAW 9 — QA BEFORE DELIVERY

```python
import os
from pptx import Presentation as P

output = os.path.expanduser('~/Downloads/presentation.pptx')
prs.save(output)

# QA: re-open and verify
qa = P(output)
print(f"Slides: {len(qa.slides)}")
for i, slide in enumerate(qa.slides):
    texts = [s.text_frame.text[:40] for s in slide.shapes if s.has_text_frame]
    print(f"  Slide {i+1}: {texts[:3]}")

print(f"\nSaved: {output} ({os.path.getsize(output):,} bytes)")
assert os.path.getsize(output) > 10000, "File too small — likely broken"
```

---

## STANDARD HELPER TEMPLATE

```python
import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.chart.data import ChartData
from pptx.enum.chart import XL_CHART_TYPE

OUTPUT = os.path.expanduser('~/Downloads/presentation.pptx')

prs = Presentation()
prs.slide_width  = Inches(13.33)
prs.slide_height = Inches(7.5)

SLIDE_W  = Inches(13.33)
SLIDE_H  = Inches(7.5)
MARGIN   = Inches(0.4)
USABLE_W = SLIDE_W - 2*MARGIN
USABLE_H = SLIDE_H - 2*MARGIN

BRAND_DARK  = RGBColor(0x1A, 0x1A, 0x2E)
BRAND_BLUE  = RGBColor(0x16, 0x21, 0x3E)
BRAND_ACCENT= RGBColor(0x0F, 0x3A, 0x60)
WHITE       = RGBColor(0xFF, 0xFF, 0xFF)
DARK_TEXT   = RGBColor(0x1A, 0x1A, 0x1A)

def blank_slide(prs):
    layout = prs.slide_layouts[6]
    slide  = prs.slides.add_slide(layout)
    bg = slide.background; bg.fill.solid()
    bg.fill.fore_color.rgb = BRAND_DARK
    return slide

def add_text(slide, text, left, top, width, height,
             font_name='Calibri', font_size=14, bold=False,
             color=WHITE, align=PP_ALIGN.LEFT, wrap=True):
    txb = slide.shapes.add_textbox(left, top, width, height)
    tf  = txb.text_frame
    tf.word_wrap = wrap
    tf.margin_left = tf.margin_right = Pt(4)
    tf.margin_top  = tf.margin_bottom = Pt(2)
    p = tf.paragraphs[0]
    p.alignment = align
    r = p.add_run()
    r.text = str(text)
    r.font.name  = font_name
    r.font.size  = Pt(font_size)
    r.font.bold  = bold
    r.font.color.rgb = color
    return txb

prs.save(OUTPUT)
print(f"Saved: {OUTPUT} ({os.path.getsize(OUTPUT):,} bytes)")
```
