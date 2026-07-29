#!/usr/bin/env python3
"""Render pamphlet.html to a print-ready A4 PDF.

pamphlet.html references qr_site.png by relative path, so run this from inside
this folder (both files must sit together). Output is Pamphlet.pdf; when it looks
right, use it to replace both checked-in copies of the pamphlet:

    documents/Pamphlet - A4 color (print this).pdf
    assets/Pamphlet_ABA_Resolution.pdf   (the website links to this exact name)

Both copies must stay identical to each other.

Requires: pip install weasyprint
(WeasyPrint needs system libraries pango and cairo; on macOS: brew install pango)
"""
from weasyprint import HTML

HTML("pamphlet.html").write_pdf("Pamphlet.pdf")
print("Wrote Pamphlet.pdf")
