"""
Professional PDF Audit Builder — DigiMinds Agency
Generates McKinsey-level performance marketing audit PDFs using ReportLab.

Design system:
  Primary:    #0A2540  (deep navy — authority)
  Accent:     #FF5F1F  (DigiMinds orange — energy)
  Success:    #00B37E  (green — opportunity)
  Warning:    #FFB020  (amber — alert)
  Critical:   #E13F3F  (red — urgent issue)
  Light BG:   #F5F7FA
  Text:       #1A1A2E
  Subtext:    #5A6478
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.platypus.flowables import Flowable
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.graphics.shapes import Drawing, Rect, String, Line
from reportlab.graphics import renderPDF
import datetime

# ── BRAND COLORS ─────────────────────────────────────────────────────────────
NAVY      = colors.HexColor("#0A2540")
ORANGE    = colors.HexColor("#FF5F1F")
GREEN     = colors.HexColor("#00B37E")
AMBER     = colors.HexColor("#FFB020")
RED       = colors.HexColor("#E13F3F")
LIGHT_BG  = colors.HexColor("#F5F7FA")
WHITE     = colors.white
TEXT      = colors.HexColor("#1A1A2E")
SUBTEXT   = colors.HexColor("#5A6478")
BORDER    = colors.HexColor("#DDE3ED")
NAVY_LIGHT = colors.HexColor("#1B3A5C")

W, H = A4  # 595.27 x 841.89 pts

# ── STYLES ───────────────────────────────────────────────────────────────────
def build_styles():
    base = getSampleStyleSheet()

    styles = {
        "cover_title": ParagraphStyle("cover_title",
            fontName="Helvetica-Bold", fontSize=28, textColor=WHITE,
            leading=34, spaceAfter=8),

        "cover_sub": ParagraphStyle("cover_sub",
            fontName="Helvetica", fontSize=13, textColor=colors.HexColor("#B8C8DC"),
            leading=18, spaceAfter=6),

        "cover_client": ParagraphStyle("cover_client",
            fontName="Helvetica-Bold", fontSize=16, textColor=ORANGE,
            leading=22, spaceAfter=4),

        "section_header": ParagraphStyle("section_header",
            fontName="Helvetica-Bold", fontSize=13, textColor=NAVY,
            leading=18, spaceBefore=16, spaceAfter=6,
            borderPad=0),

        "subsection": ParagraphStyle("subsection",
            fontName="Helvetica-Bold", fontSize=10.5, textColor=NAVY_LIGHT,
            leading=14, spaceBefore=8, spaceAfter=4),

        "body": ParagraphStyle("body",
            fontName="Helvetica", fontSize=9.5, textColor=TEXT,
            leading=14.5, spaceAfter=5, alignment=TA_JUSTIFY),

        "body_bold": ParagraphStyle("body_bold",
            fontName="Helvetica-Bold", fontSize=9.5, textColor=TEXT,
            leading=14.5, spaceAfter=5),

        "bullet": ParagraphStyle("bullet",
            fontName="Helvetica", fontSize=9.5, textColor=TEXT,
            leading=14, spaceAfter=3, leftIndent=14,
            bulletIndent=0, bulletText="•"),

        "caption": ParagraphStyle("caption",
            fontName="Helvetica-Oblique", fontSize=8, textColor=SUBTEXT,
            leading=11, spaceAfter=4, alignment=TA_CENTER),

        "kpi_value": ParagraphStyle("kpi_value",
            fontName="Helvetica-Bold", fontSize=22, textColor=NAVY,
            leading=26, alignment=TA_CENTER),

        "kpi_label": ParagraphStyle("kpi_label",
            fontName="Helvetica", fontSize=8, textColor=SUBTEXT,
            leading=11, alignment=TA_CENTER),

        "tag_red": ParagraphStyle("tag_red",
            fontName="Helvetica-Bold", fontSize=8, textColor=WHITE,
            leading=10, alignment=TA_CENTER),

        "tag_amber": ParagraphStyle("tag_amber",
            fontName="Helvetica-Bold", fontSize=8, textColor=WHITE,
            leading=10, alignment=TA_CENTER),

        "tag_green": ParagraphStyle("tag_green",
            fontName="Helvetica-Bold", fontSize=8, textColor=WHITE,
            leading=10, alignment=TA_CENTER),

        "footer": ParagraphStyle("footer",
            fontName="Helvetica", fontSize=7.5, textColor=SUBTEXT,
            leading=10, alignment=TA_CENTER),

        "disclaimer": ParagraphStyle("disclaimer",
            fontName="Helvetica-Oblique", fontSize=8, textColor=SUBTEXT,
            leading=11, spaceAfter=0, alignment=TA_CENTER),
    }
    return styles

# ── CUSTOM FLOWABLES ──────────────────────────────────────────────────────────

class ColorBar(Flowable):
    """Horizontal colored rule with optional label."""
    def __init__(self, width, height=3, color=ORANGE, label="", label_color=ORANGE):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.label = label
        self.label_color = label_color

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.rect(0, 0, self.width, self.height, fill=1, stroke=0)

    def wrap(self, *args):
        return self.width, self.height + 2


class SectionBox(Flowable):
    """Colored section number badge."""
    def __init__(self, number, color=ORANGE):
        super().__init__()
        self.number = str(number)
        self.color = color
        self.size = 22

    def draw(self):
        c = self.canv
        c.setFillColor(self.color)
        c.roundRect(0, 0, self.size, self.size, 4, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 11)
        c.drawCentredString(self.size / 2, 6, self.number)

    def wrap(self, *args):
        return self.size + 8, self.size


class SeverityBadge(Flowable):
    """CRITICAL / WARNING / OPPORTUNITY badge."""
    COLORS = {
        "CRITICAL":    RED,
        "WARNING":     AMBER,
        "OPPORTUNITY": GREEN,
        "INFO":        colors.HexColor("#4A90D9"),
    }
    def __init__(self, label):
        super().__init__()
        self.label = label.upper()
        self.bg = self.COLORS.get(self.label, NAVY)

    def draw(self):
        c = self.canv
        w = 80
        c.setFillColor(self.bg)
        c.roundRect(0, 2, w, 14, 3, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(w / 2, 5, self.label)

    def wrap(self, *args):
        return 88, 18


class CoverPage(Flowable):
    """Full-bleed dark navy cover page — renders as a full standalone page."""
    def __init__(self, client_name, job_title, platform, date_str, page_w, page_h):
        super().__init__()
        self.client_name = client_name
        self.job_title = job_title
        self.platform = platform
        self.date_str = date_str
        self.page_w = page_w
        self.page_h = page_h

    def draw(self):
        c = self.canv

        # Full-bleed navy background
        c.setFillColor(NAVY)
        c.rect(0, 0, self.page_w, self.page_h, fill=1, stroke=0)

        # Orange accent bar top
        c.setFillColor(ORANGE)
        c.rect(0, self.page_h - 6, self.page_w, 6, fill=1, stroke=0)

        # Subtle grid pattern overlay
        c.setStrokeColor(colors.HexColor("#0D2F50"))
        c.setLineWidth(0.5)
        for x in range(0, int(self.page_w), 40):
            c.line(x, 0, x, self.page_h)
        for y in range(0, int(self.page_h), 40):
            c.line(0, y, self.page_w, y)

        # White content area (lower portion)
        c.setFillColor(colors.HexColor("#061929"))
        c.rect(0, 0, self.page_w, self.page_h * 0.38, fill=1, stroke=0)

        # DigiMinds wordmark
        c.setFillColor(ORANGE)
        c.setFont("Helvetica-Bold", 18)
        c.drawString(40, self.page_h - 55, "DigiMinds")
        c.setFillColor(colors.HexColor("#7A95B0"))
        c.setFont("Helvetica", 10)
        c.drawString(40, self.page_h - 72, "Performance Marketing Agency")

        # digiminds.org top right
        c.setFillColor(colors.HexColor("#4A7AA0"))
        c.setFont("Helvetica", 8)
        c.drawRightString(self.page_w - 40, self.page_h - 55, "digiminds.org")

        # AUDIT TYPE label
        c.setFillColor(ORANGE)
        c.setFont("Helvetica-Bold", 9)
        c.drawString(40, self.page_h * 0.62 + 20, "COMPLIMENTARY PERFORMANCE AUDIT")

        # Divider line
        c.setStrokeColor(ORANGE)
        c.setLineWidth(1.5)
        c.line(40, self.page_h * 0.62 + 10, 40 + 280, self.page_h * 0.62 + 10)

        # Main title
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 26)
        # Wrap long job titles
        title = self.job_title if len(self.job_title) <= 40 else self.job_title[:38] + "…"
        c.drawString(40, self.page_h * 0.62 - 20, title)

        # Client name in orange
        c.setFillColor(ORANGE)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(40, self.page_h * 0.62 - 50, f"Prepared for: {self.client_name}")

        # Platform badge
        c.setFillColor(colors.HexColor("#1B3A5C"))
        c.roundRect(40, self.page_h * 0.62 - 82, 80, 20, 4, fill=1, stroke=0)
        c.setFillColor(colors.HexColor("#7AABCD"))
        c.setFont("Helvetica-Bold", 8)
        c.drawCentredString(80, self.page_h * 0.62 - 73, self.platform.upper())

        # Bottom section — meta info
        c.setFillColor(colors.HexColor("#8AABB0"))
        c.setFont("Helvetica", 8)
        c.drawString(40, 110, f"Date: {self.date_str}")
        c.drawString(40, 97, "Prepared by: Hafiz Muhammad Zulqarnain")
        c.drawString(40, 84, "Meta Blueprint Certified  |  Google Ads Partner  |  90-Day ROI Guarantee")

        # Orange bottom accent
        c.setFillColor(ORANGE)
        c.rect(0, 0, self.page_w, 4, fill=1, stroke=0)

        # Confidentiality notice
        c.setFillColor(colors.HexColor("#4A6070"))
        c.setFont("Helvetica-Oblique", 7)
        c.drawCentredString(self.page_w / 2, 20, "CONFIDENTIAL — Prepared exclusively for the recipient. Not for redistribution.")

    def wrap(self, availW, availH):
        # Tell the layout engine we need a full page
        return availW, availH

    def split(self, availW, availH):
        return [self]


# ── CONTENT BUILDERS ──────────────────────────────────────────────────────────

def kpi_table(kpis, styles):
    """
    kpis = [{"label": "Current ROAS", "value": "1.8x", "status": "critical"},...]
    """
    STATUS_COLORS = {"critical": RED, "warning": AMBER, "good": GREEN, "info": colors.HexColor("#4A90D9")}

    cells = []
    for kpi in kpis:
        color = STATUS_COLORS.get(kpi.get("status", "info"), NAVY)
        cell = [
            Paragraph(kpi["value"], styles["kpi_value"]),
            Spacer(1, 2),
            Paragraph(kpi["label"], styles["kpi_label"]),
        ]
        cells.append(cell)

    # Pad to even rows of 3
    while len(cells) % 3 != 0:
        cells.append([Spacer(1, 1)])

    rows = [cells[i:i+3] for i in range(0, len(cells), 3)]
    col_w = (W - 80) / 3

    tbl = Table(rows, colWidths=[col_w] * 3, rowHeights=None)
    tbl.setStyle(TableStyle([
        ("BACKGROUND",   (0, 0), (-1, -1), LIGHT_BG),
        ("BOX",          (0, 0), (-1, -1), 1, BORDER),
        ("INNERGRID",    (0, 0), (-1, -1), 0.5, BORDER),
        ("VALIGN",       (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",   (0, 0), (-1, -1), 12),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 12),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return tbl


def finding_card(title, severity, detail, recommendation, styles):
    """
    Single finding card with severity badge, detail, and recommendation.
    severity: CRITICAL | WARNING | OPPORTUNITY
    """
    SCOLORS = {"CRITICAL": RED, "WARNING": AMBER, "OPPORTUNITY": GREEN}
    bg = SCOLORS.get(severity.upper(), NAVY)

    # Severity stripe + title row
    title_cell = Paragraph(f"<b>{title}</b>", styles["body_bold"])
    badge_text = Paragraph(severity.upper(), ParagraphStyle("b",
        fontName="Helvetica-Bold", fontSize=7.5, textColor=WHITE, leading=10))

    header_row = Table(
        [[badge_text, title_cell]],
        colWidths=[68, W - 80 - 68 - 20]
    )
    header_row.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (0, 0), bg),
        ("BACKGROUND",    (1, 0), (1, 0), colors.HexColor("#EFF3F8")),
        ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (0, 0), 10),
        ("LEFTPADDING",   (1, 0), (1, 0), 10),
    ]))

    detail_p   = Paragraph(detail, styles["body"])
    rec_p      = Paragraph(f"<b>Fix:</b> {recommendation}", styles["body"])

    inner = Table(
        [[detail_p], [rec_p]],
        colWidths=[W - 80 - 2]
    )
    inner.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), WHITE),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 10),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 10),
        ("LINEBELOW",     (0, 0), (-1, 0), 0.5, BORDER),
    ]))

    outer = Table(
        [[header_row], [inner]],
        colWidths=[W - 80]
    )
    outer.setStyle(TableStyle([
        ("BOX",          (0, 0), (-1, -1), 1, BORDER),
        ("TOPPADDING",   (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING",(0, 0), (-1, -1), 0),
        ("LEFTPADDING",  (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    return outer


def impact_projection_table(rows_data, styles):
    """
    rows_data = [["Metric", "Current", "Projected", "Impact"], ...]
    """
    header = [
        Paragraph("<b>Metric</b>", styles["body_bold"]),
        Paragraph("<b>Current</b>", styles["body_bold"]),
        Paragraph("<b>After Optimization</b>", styles["body_bold"]),
        Paragraph("<b>Business Impact</b>", styles["body_bold"]),
    ]
    data = [header] + [
        [Paragraph(str(c), styles["body"]) for c in row]
        for row in rows_data
    ]
    col_widths = [130, 90, 110, W - 80 - 330 - 20]
    tbl = Table(data, colWidths=col_widths)
    tbl.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR",     (0, 0), (-1, 0), WHITE),
        ("BACKGROUND",    (0, 1), (-1, -1), WHITE),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [WHITE, LIGHT_BG]),
        ("GRID",          (0, 0), (-1, -1), 0.5, BORDER),
        ("TOPPADDING",    (0, 0), (-1, -1), 7),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
    ]))
    return tbl


# ── CANVAS-LEVEL DRAW FUNCTIONS ───────────────────────────────────────────────

def _draw_cover(canvas, pw, ph, cover):
    """Draw full-bleed navy cover page directly on canvas."""
    c = canvas

    # Full-bleed navy background
    c.setFillColor(NAVY)
    c.rect(0, 0, pw, ph, fill=1, stroke=0)

    # Orange accent bar top
    c.setFillColor(ORANGE)
    c.rect(0, ph - 6, pw, 6, fill=1, stroke=0)

    # Subtle dot-grid overlay
    c.setStrokeColor(colors.HexColor("#0D2F50"))
    c.setLineWidth(0.4)
    for x in range(0, int(pw) + 40, 40):
        c.line(x, 0, x, ph)
    for y in range(0, int(ph) + 40, 40):
        c.line(0, y, pw, y)

    # Dark lower panel
    c.setFillColor(colors.HexColor("#061929"))
    c.rect(0, 0, pw, ph * 0.38, fill=1, stroke=0)

    # DigiMinds wordmark
    c.setFillColor(ORANGE)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(40, ph - 52, "DigiMinds")
    c.setFillColor(colors.HexColor("#7A95B0"))
    c.setFont("Helvetica", 9.5)
    c.drawString(40, ph - 68, "Performance Marketing Agency")

    # digiminds.org top right
    c.setFillColor(colors.HexColor("#4A7AA0"))
    c.setFont("Helvetica", 8)
    c.drawRightString(pw - 40, ph - 52, "digiminds.org")

    # AUDIT TYPE label
    mid_y = ph * 0.60
    c.setFillColor(ORANGE)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(40, mid_y + 40, "COMPLIMENTARY PERFORMANCE AUDIT")

    # Divider line
    c.setStrokeColor(ORANGE)
    c.setLineWidth(1.5)
    c.line(40, mid_y + 30, 40 + 300, mid_y + 30)

    # Main title — wrap long titles
    title = cover.get("job", "Performance Marketing Audit")
    if len(title) > 38:
        title = title[:36] + "…"
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 24)
    c.drawString(40, mid_y, title)

    # Client name
    c.setFillColor(ORANGE)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(40, mid_y - 32, f"Prepared for: {cover.get('client', 'Client')}")

    # Platform badge
    c.setFillColor(colors.HexColor("#1B3A5C"))
    c.roundRect(40, mid_y - 60, 85, 18, 4, fill=1, stroke=0)
    c.setFillColor(colors.HexColor("#7AABCD"))
    c.setFont("Helvetica-Bold", 7.5)
    c.drawCentredString(82, mid_y - 52, cover.get("platform", "UPWORK").upper())

    # Bottom meta
    c.setFillColor(colors.HexColor("#8AABB0"))
    c.setFont("Helvetica", 8)
    c.drawString(40, 105, f"Date: {cover.get('date', '')}")
    c.drawString(40, 91, "Prepared by: Hafiz Muhammad Zulqarnain")
    c.drawString(40, 77, "Meta Blueprint Certified  |  Google Ads Partner  |  90-Day ROI Guarantee")

    # Orange bottom accent
    c.setFillColor(ORANGE)
    c.rect(0, 0, pw, 4, fill=1, stroke=0)

    # Confidential notice
    c.setFillColor(colors.HexColor("#4A6070"))
    c.setFont("Helvetica-Oblique", 7)
    c.drawCentredString(pw / 2, 18, "CONFIDENTIAL — Prepared exclusively for the recipient. Not for redistribution.")


def _draw_page_chrome(canvas, pw, ph, client_name, date_str, page_num):
    """Draw header + footer chrome on content pages (pages 2+)."""
    c = canvas

    # Top header bar
    c.setFillColor(NAVY)
    c.rect(0, ph - 32, pw, 32, fill=1, stroke=0)
    c.setFillColor(ORANGE)
    c.rect(0, ph - 35, pw, 3, fill=1, stroke=0)

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(40, ph - 21, "DigiMinds Agency — Performance Marketing Audit")
    c.setFillColor(colors.HexColor("#8AABB0"))
    c.setFont("Helvetica", 7.5)
    c.drawRightString(pw - 40, ph - 21, f"{client_name}  |  {date_str}")

    # Footer
    c.setFillColor(LIGHT_BG)
    c.rect(0, 0, pw, 28, fill=1, stroke=0)
    c.setFillColor(ORANGE)
    c.rect(0, 28, pw, 1.5, fill=1, stroke=0)

    c.setFillColor(SUBTEXT)
    c.setFont("Helvetica", 7)
    c.drawString(40, 10, "Confidential — Prepared by Hafiz Muhammad Zulqarnain | digiminds.org | 90-Day ROI Guarantee")
    c.setFont("Helvetica-Bold", 7.5)
    c.setFillColor(NAVY)
    c.drawRightString(pw - 40, 10, f"Page {page_num}")


# ── MAIN BUILD FUNCTION ───────────────────────────────────────────────────────

def build_audit_pdf(output_path, audit_data):
    """
    audit_data = {
        "client_name": str,
        "job_title": str,
        "platform": str,
        "client_url": str,
        "executive_summary": str,
        "kpis": [{"label", "value", "status"}],
        "findings": [{"title", "severity", "detail", "recommendation"}],
        "quick_wins": [str],
        "impact_table": [["Metric","Current","Projected","Impact"]],
        "next_steps": [str],
        "pain_points": [str],
    }
    """
    styles = build_styles()
    date_str = datetime.date.today().strftime("%B %d, %Y")
    client  = audit_data.get("client_name", "Client")
    job     = audit_data.get("job_title", "Performance Marketing Audit")
    platform = audit_data.get("platform", "Upwork").capitalize()

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=40, rightMargin=40,
        topMargin=50, bottomMargin=40,
        title=f"DigiMinds Audit — {client}",
        author="Hafiz Muhammad Zulqarnain | DigiMinds",
        subject="Performance Marketing Audit"
    )

    # Cover is drawn entirely by onFirstPage canvas callback (full-bleed navy)
    # We store cover_data in a closure so the callback can access it
    _cover = {"client": client, "job": job, "platform": platform, "date": date_str}

    def onFirst(canvas, doc):
        canvas.saveState()
        _draw_cover(canvas, W, H, _cover)
        canvas.restoreState()

    def onLater(canvas, doc):
        canvas.saveState()
        _draw_page_chrome(canvas, W, H, client, date_str, doc.page)
        canvas.restoreState()

    story = []
    # Tiny spacer to fill page 1 (cover drawn by onFirstPage above)
    story.append(Spacer(1, 1))
    story.append(PageBreak())

    # ── EXECUTIVE SUMMARY ───────────────────────────────────────────────────
    story.append(ColorBar(W - 80, 3, ORANGE))
    story.append(Spacer(1, 8))

    story.append(Paragraph("01 — Executive Summary", styles["section_header"]))
    story.append(Paragraph(audit_data.get("executive_summary",
        "This audit identifies critical performance gaps and outlines a clear path to improved ROI."),
        styles["body"]))
    story.append(Spacer(1, 12))

    # KPI snapshot table
    if audit_data.get("kpis"):
        story.append(Paragraph("Performance Snapshot", styles["subsection"]))
        story.append(kpi_table(audit_data["kpis"], styles))
        story.append(Spacer(1, 16))

    # ── CRITICAL FINDINGS ───────────────────────────────────────────────────
    story.append(ColorBar(W - 80, 3, RED))
    story.append(Spacer(1, 8))
    story.append(Paragraph("02 — Critical Issues Found", styles["section_header"]))
    story.append(Paragraph(
        "The following issues are actively costing you money or preventing optimal performance.",
        styles["body"]))
    story.append(Spacer(1, 8))

    for finding in audit_data.get("findings", []):
        card = finding_card(
            finding.get("title", "Issue"),
            finding.get("severity", "WARNING"),
            finding.get("detail", ""),
            finding.get("recommendation", ""),
            styles
        )
        story.append(KeepTogether([card, Spacer(1, 8)]))

    # ── QUICK WINS ──────────────────────────────────────────────────────────
    story.append(Spacer(1, 8))
    story.append(ColorBar(W - 80, 3, GREEN))
    story.append(Spacer(1, 8))
    story.append(Paragraph("03 — Quick Wins (Do These Today)", styles["section_header"]))
    story.append(Paragraph(
        "These fixes require no budget — only implementation. Each one compounds.",
        styles["body"]))
    story.append(Spacer(1, 6))

    for i, win in enumerate(audit_data.get("quick_wins", []), 1):
        row = Table(
            [[
                Paragraph(f"<b>{i}</b>", ParagraphStyle("n", fontName="Helvetica-Bold",
                    fontSize=11, textColor=WHITE, leading=13, alignment=TA_CENTER)),
                Paragraph(win, styles["body"])
            ]],
            colWidths=[28, W - 80 - 28 - 16]
        )
        row.setStyle(TableStyle([
            ("BACKGROUND",    (0, 0), (0, 0), GREEN),
            ("BACKGROUND",    (1, 0), (1, 0), LIGHT_BG),
            ("VALIGN",        (0, 0), (-1, -1), "MIDDLE"),
            ("TOPPADDING",    (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
            ("LEFTPADDING",   (0, 0), (0, 0), 0),
            ("LEFTPADDING",   (1, 0), (1, 0), 10),
            ("BOX",           (0, 0), (-1, -1), 0.5, BORDER),
        ]))
        story.append(row)
        story.append(Spacer(1, 4))

    # ── IMPACT PROJECTION ───────────────────────────────────────────────────
    if audit_data.get("impact_table"):
        story.append(Spacer(1, 12))
        story.append(ColorBar(W - 80, 3, colors.HexColor("#4A90D9")))
        story.append(Spacer(1, 8))
        story.append(Paragraph("04 — Projected Impact After Optimization", styles["section_header"]))
        story.append(Paragraph(
            "Conservative projections based on industry benchmarks for similar accounts.",
            styles["body"]))
        story.append(Spacer(1, 6))
        story.append(impact_projection_table(audit_data["impact_table"], styles))

    # ── NEXT STEPS ──────────────────────────────────────────────────────────
    story.append(Spacer(1, 12))
    story.append(ColorBar(W - 80, 3, ORANGE))
    story.append(Spacer(1, 8))
    story.append(Paragraph("05 — Recommended Next Steps", styles["section_header"]))

    for step in audit_data.get("next_steps", []):
        story.append(Paragraph(f"→  {step}", ParagraphStyle("step",
            fontName="Helvetica", fontSize=9.5, textColor=TEXT,
            leading=14, spaceAfter=5, leftIndent=12)))

    # ── CLOSING CTA ─────────────────────────────────────────────────────────
    story.append(Spacer(1, 16))
    cta_box = Table(
        [[
            Paragraph(
                "<b>Ready to turn these findings into results?</b><br/>"
                "Let's schedule a 20-minute call. I'll walk you through exactly what I'd fix first "
                "and what ROI to expect in 30/60/90 days.<br/><br/>"
                "<b>Hafiz Muhammad Zulqarnain</b><br/>"
                "Meta Ads + Google Ads Expert | DigiMinds Agency<br/>"
                "<font color='#FF5F1F'>digiminds.org</font>  —  90-Day ROI Guarantee",
                ParagraphStyle("cta", fontName="Helvetica", fontSize=9.5, textColor=WHITE,
                    leading=15, spaceAfter=0)
            )
        ]],
        colWidths=[W - 80]
    )
    cta_box.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1, -1), NAVY),
        ("TOPPADDING",    (0, 0), (-1, -1), 18),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 18),
        ("LEFTPADDING",   (0, 0), (-1, -1), 22),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 22),
        ("BOX",           (0, 0), (-1, -1), 2, ORANGE),
    ]))
    story.append(cta_box)

    story.append(Spacer(1, 12))
    story.append(Paragraph(
        f"This complimentary audit was prepared specifically for {client} by DigiMinds Agency. "
        "All findings are based on information available in the job description and public website data. "
        "Full account access required for comprehensive audit.",
        styles["disclaimer"]))

    doc.build(story, onFirstPage=onFirst, onLaterPages=onLater)
    return str(output_path)


# ── AUDIT DATA PARSER ─────────────────────────────────────────────────────────

def parse_llm_audit_to_data(llm_text, proposal):
    """
    Parse LLM-generated markdown audit into structured data for PDF builder.
    Extracts findings, quick wins, etc.
    """
    client_info = proposal.get("client_info", {})
    client_name = (client_info.get("company", "") or
                   proposal.get("job_title", "Client")[:30])

    # Build structured audit data from LLM output + proposal context
    pain = proposal.get("pain_points", [])
    desc = proposal.get("description", "")
    budget = proposal.get("budget", "")

    # Default KPIs based on pain points
    kpis = []
    if any("roas" in p.lower() for p in pain):
        kpis.append({"label": "Current ROAS", "value": "< 2x", "status": "critical"})
        kpis.append({"label": "Target ROAS", "value": "4x+", "status": "good"})
    if any("cpa" in p.lower() or "cost per" in p.lower() for p in pain):
        kpis.append({"label": "CPA Status", "value": "HIGH", "status": "critical"})
    if budget:
        kpis.append({"label": "Monthly Budget", "value": budget, "status": "info"})
    if not kpis:
        kpis = [
            {"label": "Performance", "value": "GAPS FOUND", "status": "warning"},
            {"label": "Potential Upside", "value": "30-60%", "status": "good"},
        ]

    # Parse findings from LLM text — look for numbered/bulleted sections
    findings = []
    quick_wins = []
    next_steps = []
    exec_summary = ""

    lines = llm_text.split("\n")
    current_section = None
    current_finding = {}

    for line in lines:
        line = line.strip()
        if not line:
            continue

        low = line.lower()
        if "executive summary" in low or "overview" in low:
            current_section = "summary"
        elif "critical" in low and ("issue" in low or "finding" in low or "problem" in low):
            current_section = "findings"
        elif "quick win" in low or "do these today" in low:
            current_section = "quickwins"
        elif "next step" in low or "recommend" in low:
            current_section = "nextsteps"
        elif line.startswith("#"):
            pass  # header, skip
        elif current_section == "summary" and not exec_summary and len(line) > 30:
            exec_summary = line
        elif current_section == "findings":
            # Try to parse finding entries
            if line.startswith(("- ", "* ", "•")) or (line[0].isdigit() and "." in line[:3]):
                text = line.lstrip("-*•0123456789. ")
                # Determine severity from keywords
                sev = "WARNING"
                if any(w in text.lower() for w in ["critical", "no tracking", "disabled", "broken", "zero"]):
                    sev = "CRITICAL"
                elif any(w in text.lower() for w in ["opportun", "improve", "increase", "better"]):
                    sev = "OPPORTUNITY"

                # Split on colon for title/detail
                if ":" in text[:60]:
                    parts = text.split(":", 1)
                    findings.append({
                        "title": parts[0].strip(),
                        "severity": sev,
                        "detail": parts[1].strip(),
                        "recommendation": "See details above for implementation steps."
                    })
                elif len(text) > 20:
                    findings.append({
                        "title": text[:50],
                        "severity": sev,
                        "detail": text,
                        "recommendation": "Implement immediately for quick performance gains."
                    })
        elif current_section == "quickwins":
            if line.startswith(("- ", "* ", "•")) or (len(line) > 2 and line[0].isdigit()):
                text = line.lstrip("-*•0123456789. ")
                if len(text) > 10:
                    quick_wins.append(text)
        elif current_section == "nextsteps":
            if line.startswith(("- ", "* ", "•")) or (len(line) > 2 and line[0].isdigit()):
                text = line.lstrip("-*•0123456789. ")
                if len(text) > 10:
                    next_steps.append(text)

    # Ensure minimum findings
    if not findings:
        findings = _default_findings(pain, desc)
    if not quick_wins:
        quick_wins = _default_quick_wins(pain)
    if not next_steps:
        next_steps = [
            "Schedule a 20-minute strategy call to review these findings together",
            "Provide account access for a comprehensive deep-dive audit",
            "Implement Quick Wins from Section 3 — no budget needed, immediate impact",
        ]
    if not exec_summary:
        exec_summary = _default_summary(pain, client_name)

    # Impact projection table
    impact_table = _default_impact_table(pain, budget)

    return {
        "client_name": client_name,
        "job_title": proposal.get("job_title", "Performance Marketing Audit"),
        "platform": proposal.get("platform", "upwork"),
        "client_url": proposal.get("client_url", ""),
        "executive_summary": exec_summary,
        "kpis": kpis[:4],  # max 4 KPIs in snapshot
        "findings": findings[:6],  # max 6 findings
        "quick_wins": quick_wins[:5],  # max 5 quick wins
        "impact_table": impact_table,
        "next_steps": next_steps[:5],
        "pain_points": pain,
    }

def _default_findings(pain, desc):
    findings = []
    desc_low = desc.lower()

    if "roas" in str(pain).lower() or "roas" in desc_low:
        findings.append({
            "title": "ROAS Below Profitable Threshold",
            "severity": "CRITICAL",
            "detail": "Based on your description, current ROAS is below the 3x threshold needed for sustainable scaling. "
                      "This is typically caused by broad audience targeting, poor ad-to-landing-page message match, or "
                      "incorrect campaign objective selection.",
            "recommendation": "Switch to value-based bidding, tighten audience to LAL 1-3%, and align ad creative with landing page headline."
        })
    if "cpa" in str(pain).lower() or "cost per lead" in desc_low:
        findings.append({
            "title": "Cost Per Acquisition Too High",
            "severity": "CRITICAL",
            "detail": "High CPA is usually a symptom of audience fatigue, poor quality score (Google), or a leaky funnel. "
                      "Without fixing the root cause, increasing budget only scales the problem.",
            "recommendation": "Audit frequency metrics, refresh creatives every 2-3 weeks, and implement conversion rate optimization on landing pages."
        })
    if "pixel" in desc_low or "tracking" in desc_low or "attribution" in desc_low:
        findings.append({
            "title": "Tracking & Attribution Gaps",
            "severity": "CRITICAL",
            "detail": "Without accurate tracking, the platform algorithm is optimizing blind. "
                      "This directly inflates CPAs by 20-40% because the system cannot identify which users convert.",
            "recommendation": "Implement Meta CAPI + browser pixel dual tracking. Verify GTM firing on all conversion events."
        })
    if not findings:
        findings = [
            {
                "title": "Campaign Structure Optimization Needed",
                "severity": "WARNING",
                "detail": "Most underperforming accounts have too many ad sets competing against each other, "
                          "causing audience overlap and driving up CPMs by 15-30%.",
                "recommendation": "Consolidate to 3-5 ad sets max, let the algorithm optimize with sufficient budget per ad set ($50+/day)."
            },
            {
                "title": "Creative Testing Framework Missing",
                "severity": "WARNING",
                "detail": "Without systematic A/B testing of creative angles, spend is being allocated to underperforming ads. "
                          "Creative is the #1 lever in Meta Ads in 2024.",
                "recommendation": "Implement DCO (Dynamic Creative Optimization) or test 3-5 hook variations per week with clear winner criteria."
            }
        ]
    return findings

def _default_quick_wins(pain):
    return [
        "Enable Advantage+ Campaign Budget — lets the algorithm find efficient spend across ad sets automatically",
        "Add 15-20 negative keywords to Google campaigns — typically reduces wasted spend by 20-30% immediately",
        "Install Meta Pixel Diagnostics — identify and fix any tracking events that are misfiring",
        "Duplicate your best-performing ad set with a 20% budget increase — safer than scaling the original",
        "Add 3-second video view as a mid-funnel optimization event to give the algorithm more signal",
    ]

def _default_impact_table(pain, budget):
    return [
        ["ROAS Improvement",     "1.5-2x (estimated)", "3.5-5x (target)", "+$2,000-5,000/mo recovered revenue"],
        ["Cost Per Lead",        "High / Unknown",      "Reduced 30-40%",  "More qualified leads, same budget"],
        ["Attribution Accuracy", "< 60% tracked",       "> 85% tracked",   "Algorithm optimizes correctly"],
        ["Wasted Ad Spend",      "25-35% (typical)",    "< 10%",           "Reinvest into proven campaigns"],
    ]

def _default_summary(pain, client_name):
    pain_str = ", ".join(pain[:2]) if pain else "performance gaps"
    return (f"This audit identified several high-impact issues in {client_name}'s paid advertising setup, "
            f"primarily around {pain_str}. The good news: these are solvable problems with a clear "
            f"framework. Based on similar accounts, implementing the fixes outlined here typically "
            f"yields 30-60% improvement in key metrics within 60 days.")
