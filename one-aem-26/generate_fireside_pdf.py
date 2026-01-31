#!/usr/bin/env python3
"""Generate a styled PDF from the fireside chat podcast script."""

from fpdf import FPDF
import re
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(SCRIPT_DIR, "fireside-chat-script.md")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "fireside-chat-script.pdf")

# macOS system fonts
FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_ITALIC = "/System/Library/Fonts/Supplemental/Arial Italic.ttf"
FONT_BOLD_ITALIC = "/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf"

# Speaker styling
SPEAKER_COLORS = {
    "MOD": (80, 80, 80),     # Dark gray for moderator
    "TL": (25, 25, 25),      # Near-black for thought leader
}


class FiresidePDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("body", "I", 8)
            self.set_text_color(140, 140, 140)
            self.cell(0, 8, "Building the AI-Native Organization", align="R")
            self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("body", "I", 8)
        self.set_text_color(140, 140, 140)
        self.cell(0, 10, f"{self.page_no()}", align="C")


def render_dialogue_line(pdf, speaker, text):
    """Render a single dialogue line with speaker label and content."""
    label_w = 14

    # Speaker label
    if speaker == "MOD":
        pdf.set_font("body", "B", 9)
        pdf.set_text_color(100, 100, 100)
    else:
        pdf.set_font("body", "B", 9)
        pdf.set_text_color(40, 40, 40)

    x_start = pdf.get_x()
    y_start = pdf.get_y()
    pdf.cell(label_w, 6.5, speaker, new_x="RIGHT")

    # Content
    r, g, b = SPEAKER_COLORS.get(speaker, (40, 40, 40))
    pdf.set_text_color(r, g, b)
    pdf.set_font("body", "", 11)
    pdf.multi_cell(0, 6.5, text, markdown=True)
    pdf.ln(3)


def parse_and_render(pdf, md_path):
    with open(md_path, "r") as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].rstrip("\n")

        # Skip metadata lines
        if line.startswith("> **Format") or line.startswith("> **Speaker") or line.startswith("> **Thesis"):
            i += 1
            continue

        # Horizontal rule
        if line.strip() == "---":
            pdf.ln(3)
            y = pdf.get_y()
            pdf.set_draw_color(200, 200, 200)
            pdf.line(pdf.l_margin + 50, y, pdf.w - pdf.r_margin - 50, y)
            pdf.ln(5)
            i += 1
            continue

        # H1 title
        if line.startswith("# "):
            title = line[2:].strip()
            pdf.set_font("body", "B", 24)
            pdf.set_text_color(20, 20, 20)
            pdf.ln(16)
            pdf.multi_cell(0, 12, title, align="C")
            pdf.ln(3)

            # Subtitle
            pdf.set_font("body", "I", 10)
            pdf.set_text_color(120, 120, 120)
            pdf.cell(0, 6, "A Fireside Chat on AI-Native Product, Engineering & Culture", align="C")
            pdf.ln(4)

            # Speaker legend
            pdf.set_font("body", "", 9)
            pdf.set_text_color(150, 150, 150)
            pdf.cell(0, 5, "MOD = Moderator  \u00b7  TL = Thought Leader", align="C")
            pdf.ln(12)
            i += 1
            continue

        # Empty lines
        if line.strip() == "":
            i += 1
            continue

        # Italic attribution at end
        if line.startswith("*Based on"):
            pdf.ln(6)
            pdf.set_font("body", "I", 9)
            pdf.set_text_color(120, 120, 120)
            text = line.strip("*").strip()
            pdf.multi_cell(0, 5, text, align="C")
            i += 1
            continue

        # Dialogue line: **MOD:** or **TL:**
        dialogue_match = re.match(r"\*\*(MOD|TL):\*\*\s*(.*)", line)
        if dialogue_match:
            speaker = dialogue_match.group(1)
            text = dialogue_match.group(2)
            render_dialogue_line(pdf, speaker, text)
            i += 1
            continue

        # Regular paragraph (non-dialogue)
        pdf.set_font("body", "", 11)
        pdf.set_text_color(40, 40, 40)
        pdf.multi_cell(0, 6.5, line.strip(), markdown=True)
        pdf.ln(3.5)
        i += 1


def main():
    pdf = FiresidePDF()
    pdf.set_auto_page_break(auto=True, margin=22)

    # Register Unicode TTF fonts
    pdf.add_font("body", "", FONT_REGULAR)
    pdf.add_font("body", "B", FONT_BOLD)
    pdf.add_font("body", "I", FONT_ITALIC)
    pdf.add_font("body", "BI", FONT_BOLD_ITALIC)

    pdf.add_page()
    pdf.set_margins(28, 22, 28)
    pdf.set_x(28)

    parse_and_render(pdf, INPUT_FILE)

    pdf.output(OUTPUT_FILE)
    print(f"PDF generated: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
