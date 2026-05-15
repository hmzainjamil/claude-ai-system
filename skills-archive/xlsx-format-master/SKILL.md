# XLSX Format Master — Zero Repeat Errors

## ACTIVATION
Triggers: xlsx, excel, spreadsheet, .xlsx, excel report, workbook, openpyxl, xlsxwriter

---

## UNIVERSAL RULE BEFORE ANY XLSX BUILD
Checklist before writing any openpyxl/xlsxwriter code:

- [ ] Column widths set explicitly on every column that has content
- [ ] Row heights set explicitly for header rows and chart rows
- [ ] `wrap_text=True` on all cells with text > 20 chars
- [ ] Charts use the SAME data range the table uses — never hardcoded values
- [ ] Chart dimensions set explicitly in pixels/units — never default
- [ ] Charts anchored to specific cells — never floating
- [ ] Number formats applied — never leave raw floats in currency/percent cells
- [ ] Freeze panes on header row
- [ ] Auto-filter on data tables
- [ ] QA: open file, verify sheet count, row/col counts, chart existence
- [ ] Output → `~/Downloads/` always

---

## LAW 1 — COLUMN WIDTHS MUST BE EXPLICIT

```python
# ❌ WRONG — columns collapse or expand randomly
ws['A1'] = 'Campaign Name'

# ✅ CORRECT — set width after writing data
def auto_col_widths(ws, min_width=8, max_width=50):
    for col in ws.columns:
        max_len = 0
        col_letter = col[0].column_letter
        for cell in col:
            if cell.value:
                max_len = max(max_len, len(str(cell.value)))
        ws.column_dimensions[col_letter].width = min(max(max_len + 2, min_width), max_width)

auto_col_widths(ws)
```

For fixed-layout reports, set explicitly:
```python
ws.column_dimensions['A'].width = 30  # Campaign name
ws.column_dimensions['B'].width = 15  # Spend
ws.column_dimensions['C'].width = 12  # Clicks
ws.column_dimensions['D'].width = 10  # CTR
ws.column_dimensions['E'].width = 10  # CPC
```

---

## LAW 2 — WRAP TEXT ON LONG CELLS

```python
from openpyxl.styles import Alignment

wrap = Alignment(wrap_text=True, vertical='top')

# Apply to all header cells
for cell in ws[1]:
    cell.alignment = wrap
    ws.row_dimensions[1].height = 30  # explicit height for wrapped headers

# Apply to all data cells with text
for row in ws.iter_rows(min_row=2):
    for cell in row:
        if isinstance(cell.value, str) and len(cell.value) > 20:
            cell.alignment = wrap
```

---

## LAW 3 — NUMBER FORMATS — NEVER RAW FLOATS

```python
from openpyxl.styles import numbers

# ❌ WRONG
cell.value = 0.0312  # displays as 0.031199999...

# ✅ CORRECT
cell.value = 0.0312
cell.number_format = '0.00%'       # percentage
# OR
cell.number_format = '$#,##0.00'   # currency
cell.number_format = '#,##0'       # integer with commas
cell.number_format = '0.00'        # decimal
cell.number_format = '#,##0.00'    # decimal with commas
```

---

## LAW 4 — CHARTS MUST USE SAME DATA AS TABLES

```python
from openpyxl.chart import BarChart, Reference

# Data already written to ws, rows 2-20, cols A-E
# Chart MUST reference these exact cells — never hardcode values

chart = BarChart()
chart.type = "col"
chart.title = "Campaign Performance"
chart.y_axis.title = "Spend ($)"
chart.x_axis.title = "Campaign"

# Reference the exact data range
data = Reference(ws, min_col=2, min_row=1, max_col=2, max_row=20)
cats = Reference(ws, min_col=1, min_row=2, max_row=20)
chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)

# Size explicitly
chart.width  = 20   # cm
chart.height = 12   # cm

# Anchor to specific cell — never let it float
ws.add_chart(chart, "G2")
```

---

## LAW 5 — CHARTS MUST NOT OVERLAP DATA OR EACH OTHER

Plan chart placement BEFORE writing:
```python
# Layout grid:
# Data: cols A-F, rows 1-30
# Chart 1: anchor G2,  size 20cm × 12cm → occupies G2:R22
# Chart 2: anchor G24, size 20cm × 12cm → occupies G24:R44
# Never overlap. Calculate cell positions before adding.

# Cell width ≈ 0.89cm per unit, height ≈ 0.53cm per unit
# 20cm wide chart ≈ 20/0.89 ≈ 22 columns
# 12cm tall chart ≈ 12/0.53 ≈ 23 rows
```

---

## LAW 6 — FREEZE PANES AND AUTOFILTER

```python
# Always freeze header row
ws.freeze_panes = 'A2'

# Always add autofilter on data range
ws.auto_filter.ref = f"A1:{get_column_letter(ws.max_column)}{ws.max_row}"
```

---

## LAW 7 — HEADER STYLE MUST BE CONSISTENT

```python
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

HEADER_FILL  = PatternFill("solid", fgColor="1A1A2E")
HEADER_FONT  = Font(bold=True, color="FFFFFF", size=11, name='Calibri')
HEADER_ALIGN = Alignment(horizontal='center', vertical='center', wrap_text=True)
BORDER_SIDE  = Side(border_style='thin', color='DDDDDD')
CELL_BORDER  = Border(left=BORDER_SIDE, right=BORDER_SIDE, top=BORDER_SIDE, bottom=BORDER_SIDE)

def style_header_row(ws, row=1, height=28):
    ws.row_dimensions[row].height = height
    for cell in ws[row]:
        cell.font      = HEADER_FONT
        cell.fill      = HEADER_FILL
        cell.alignment = HEADER_ALIGN
        cell.border    = CELL_BORDER
```

---

## LAW 8 — MULTIPLE SHEETS — NEVER WRITE TO WRONG SHEET

```python
# ❌ WRONG — ws might be wrong sheet after tab switches
wb = Workbook()
ws1 = wb.active
ws1.title = "Summary"
ws2 = wb.create_sheet("Raw Data")
# ... later ...
ws.append(row)  # Which ws? Race condition in loops

# ✅ CORRECT — always use explicit sheet variable
for sheet_name, data in sheets.items():
    ws = wb[sheet_name]  # always explicit
    for row in data:
        ws.append(row)
```

---

## LAW 9 — QA BEFORE DELIVERY

```python
import os
from openpyxl import load_workbook

output = os.path.expanduser('~/Downloads/report.xlsx')
wb.save(output)

# QA: re-open and verify
qa = load_workbook(output)
for name in qa.sheetnames:
    ws = qa[name]
    print(f"Sheet '{name}': {ws.max_row} rows × {ws.max_column} cols")

print(f"\nSaved: {output} ({os.path.getsize(output):,} bytes)")
assert os.path.getsize(output) > 3000, "File too small — likely broken"
```

---

## STANDARD HELPER TEMPLATE

```python
import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side, numbers
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.utils import get_column_letter

OUTPUT = os.path.expanduser('~/Downloads/report.xlsx')
wb = Workbook()

# Remove default sheet
if 'Sheet' in wb.sheetnames:
    del wb['Sheet']

# Styles
H_FILL  = PatternFill("solid", fgColor="1A1A2E")
H_FONT  = Font(bold=True, color="FFFFFF", size=11, name='Calibri')
H_ALIGN = Alignment(horizontal='center', vertical='center', wrap_text=True)
D_FONT  = Font(size=10, name='Calibri')
D_ALIGN = Alignment(vertical='top', wrap_text=False)
BORDER  = Border(*[Side(border_style='thin', color='DDDDDD')]*4)

def write_sheet(wb, title, headers, rows, col_widths, num_formats=None):
    ws = wb.create_sheet(title)
    ws.freeze_panes = 'A2'
    ws.row_dimensions[1].height = 28
    
    # Headers
    for ci, h in enumerate(headers, 1):
        c = ws.cell(1, ci, h)
        c.font = H_FONT; c.fill = H_FILL
        c.alignment = H_ALIGN; c.border = BORDER
        ws.column_dimensions[get_column_letter(ci)].width = col_widths[ci-1]
    
    # Data
    for ri, row in enumerate(rows, 2):
        ws.row_dimensions[ri].height = 18
        for ci, val in enumerate(row, 1):
            c = ws.cell(ri, ci, val)
            c.font = D_FONT; c.alignment = D_ALIGN; c.border = BORDER
            if num_formats and ci-1 < len(num_formats) and num_formats[ci-1]:
                c.number_format = num_formats[ci-1]
    
    # Autofilter
    ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{len(rows)+1}"
    return ws

wb.save(OUTPUT)
print(f"Saved: {OUTPUT} ({os.path.getsize(OUTPUT):,} bytes)")
```
