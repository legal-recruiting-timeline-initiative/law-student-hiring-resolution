#!/usr/bin/env python3
"""Build the two-page, double-sided A4 handout.

Front (page 1): the pamphlet, exactly as built by render_pamphlet.py.
Back  (page 2): page 1 of the filed resolution, stamped with the resolution
                number in the upper right, the way ABA resolutions carry it.

Both pages are emitted at identical A4 dimensions so the two sides register
when printed double-sided on one sheet. The filed resolution is US Letter, so
its page is scaled to fit A4 (about 97%) and centred; nothing is cropped and
the operative text is untouched.

documents/Resolution.pdf is never modified - the stamp is applied to an
in-memory copy and written only into the handout.

Run from inside this folder:

    python build_handout.py

Requires: pip install pymupdf
"""
import fitz

REPO = ".."
PAMPHLET = f"{REPO}/documents/Pamphlet - A4 color (print this).pdf"
RESOLUTION = f"{REPO}/documents/Resolution.pdf"
OUT = f"{REPO}/documents/Handout - pamphlet + Resolution 403 (A4, double-sided).pdf"

RESOLUTION_NUMBER = "403"

# Right edge of the resolution's body text, so the number lines up with it.
BODY_RIGHT_X = 543.0
NUMBER_BASELINE_Y = 112.0
NUMBER_SIZE = 14

pamphlet = fitz.open(PAMPHLET)
resolution = fitz.open(RESOLUTION)

# Page 1 of the resolution, on its own, so we can stamp it without touching
# the filed document.
res_page = fitz.open()
res_page.insert_pdf(resolution, from_page=0, to_page=0)
page = res_page[0]

# The filed document is set in Arial; Helvetica is metrically compatible and is
# a base-14 font, so it needs no embedding.
box = fitz.Rect(BODY_RIGHT_X - 140, NUMBER_BASELINE_Y - 18, BODY_RIGHT_X, NUMBER_BASELINE_Y + 6)
page.insert_textbox(
    box,
    RESOLUTION_NUMBER,
    fontname="hebo",
    fontsize=NUMBER_SIZE,
    color=(0, 0, 0),
    align=fitz.TEXT_ALIGN_RIGHT,
)

out = fitz.open()

# Front: the pamphlet is already exactly A4, so copy it through untouched -
# this keeps its vector text and the embedded seal at full quality.
out.insert_pdf(pamphlet, from_page=0, to_page=0)
a4 = out[0].rect
a4_w, a4_h = a4.width, a4.height

# Back: place the Letter-sized resolution page onto an identical A4 page,
# scaled to fit and centred.
back = out.new_page(width=a4_w, height=a4_h)
src = res_page[0].rect
scale = min(a4_w / src.width, a4_h / src.height)
w, h = src.width * scale, src.height * scale
x0, y0 = (a4_w - w) / 2, (a4_h - h) / 2
back.show_pdf_page(fitz.Rect(x0, y0, x0 + w, y0 + h), res_page, 0)

out.set_metadata({
    "title": f"Resolution {RESOLUTION_NUMBER}: pamphlet and resolution",
    "subject": "Bar Association of the District of Columbia",
})
out.save(OUT, deflate=True, garbage=4)

print(f"Wrote {OUT}")
print(f"  pages: {out.page_count}")
for i, p in enumerate(out):
    print(f"  page {i + 1}: {p.rect.width:.2f} x {p.rect.height:.2f} pt")
