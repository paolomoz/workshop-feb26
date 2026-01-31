#!/usr/bin/env python3
"""Generate a styled PDF from the podcast script markdown."""

from fpdf import FPDF
import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(SCRIPT_DIR, "podcast-script.md")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "podcast-script.pdf")

# macOS system fonts (Arial supports full Unicode)
FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_ITALIC = "/System/Library/Fonts/Supplemental/Arial Italic.ttf"
FONT_BOLD_ITALIC = "/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf"


class PodcastPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("body", "I", 8)
            self.set_text_color(140, 140, 140)
            self.cell(0, 8, "The Engineer of 2026 Doesn\u2019t Write Code", align="R")
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("body", "I", 8)
        self.set_text_color(140, 140, 140)
        self.cell(0, 10, f"{self.page_no()}", align="C")


def parse_and_render(pdf, md_path):
    with open(md_path, "r") as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].rstrip("\n")

        # Skip metadata block (lines starting with >)
        if line.startswith("> **Format**") or line.startswith("> **Voice**") or line.startswith("> **Thesis**"):
            i += 1
            continue

        # Horizontal rule
        if line.strip() == "---":
            pdf.ln(4)
            # Draw a subtle line
            y = pdf.get_y()
            pdf.set_draw_color(200, 200, 200)
            pdf.line(pdf.l_margin + 50, y, pdf.w - pdf.r_margin - 50, y)
            pdf.ln(6)
            i += 1
            continue

        # H1 title
        if line.startswith("# "):
            title = line[2:].strip()
            pdf.set_font("body", "B", 24)
            pdf.set_text_color(20, 20, 20)
            pdf.ln(20)
            pdf.multi_cell(0, 12, title, align="C")
            pdf.ln(4)

            # Subtitle
            pdf.set_font("body", "I", 10)
            pdf.set_text_color(120, 120, 120)
            pdf.cell(0, 6, "A 10-Minute Podcast Script on AI-Native Engineering", align="C")
            pdf.ln(14)
            i += 1
            continue

        # Empty lines
        if line.strip() == "":
            i += 1
            continue

        # Italic attribution at end
        if line.startswith("*Based on"):
            pdf.ln(8)
            pdf.set_font("body", "I", 9)
            pdf.set_text_color(120, 120, 120)
            text = line.strip("*").strip()
            pdf.multi_cell(0, 5, text, align="C")
            i += 1
            continue

        # Regular paragraph
        pdf.set_font("body", "", 11)
        pdf.set_text_color(40, 40, 40)
        pdf.multi_cell(0, 6.5, line.strip(), markdown=True)
        pdf.ln(3.5)
        i += 1


def main():
    pdf = PodcastPDF()
    pdf.set_auto_page_break(auto=True, margin=22)

    # Register Unicode TTF fonts
    pdf.add_font("body", "", FONT_REGULAR, uni=True)
    pdf.add_font("body", "B", FONT_BOLD, uni=True)
    pdf.add_font("body", "I", FONT_ITALIC, uni=True)
    pdf.add_font("body", "BI", FONT_BOLD_ITALIC, uni=True)

    pdf.add_page()
    pdf.set_margins(28, 22, 28)
    pdf.set_x(28)

    parse_and_render(pdf, INPUT_FILE)

    pdf.output(OUTPUT_FILE)
    print(f"PDF generated: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
