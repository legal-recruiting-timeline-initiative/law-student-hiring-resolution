# How to edit and rebuild the pamphlet

This folder holds the editable source for the pamphlet. The finished pamphlet is a PDF, which
cannot be edited directly. To change it, you edit the template here and rebuild the PDF. This
takes a one-time software setup and is best done by someone comfortable running commands on a
computer. If that is not you, hand this folder to a technical helper.

## What is in this folder

- `pamphlet.html` - the pamphlet template. This is where the words, layout, and colors live.
- `qr_site.png` - the QR code image embedded in the pamphlet.
- `render_pamphlet.sh` - the simplest rebuild script (uses Google Chrome).
- `render_pamphlet.py` - alternate rebuild script (WeasyPrint, or Chrome fallback).
- `generate_qr.py` - the script that regenerates the QR code (only needed if the website
  address changes).

## One-time setup (Mac)

You need either Google Chrome (simplest) or WeasyPrint:

**Option A — Chrome (recommended if you already have it)**  
No extra install. The render script will use headless Chrome automatically.

**Option B — WeasyPrint**

    brew install pango
    pip install weasyprint

(`brew` is Homebrew, from https://brew.sh. `pip` comes with Python.)

To regenerate the QR code later, also install:

    pip install "qrcode[pil]"

## To change the pamphlet's words or design

1. Edit `pamphlet.html`. The text is plain and readable; change the words you want.
2. Rebuild the PDF:

       ./render_pamphlet.sh

   Or, if you prefer Python and have WeasyPrint set up:

       python render_pamphlet.py

   Either command writes a new `Pamphlet.pdf` in this folder.
3. Review the new `Pamphlet.pdf`. When it looks right, use it to replace the two copies in
   the repository:
   - `documents/Pamphlet - A4 color (print this).pdf`
   - `assets/Pamphlet_ABA_Resolution.pdf` (keep this exact name; the website links to it)
4. Save your changes (commit and push). The website updates automatically.

## To change the QR code (only if the website address changes)

The QR code points to the live website. You only need this if the site moves to a new
address (for example, a different repository name or a custom domain).

1. Open `generate_qr.py` and change the `URL` line to the new address.
2. Run:

       python generate_qr.py

   This rewrites `qr_site.png`.
3. Rebuild the pamphlet so it picks up the new QR:

       ./render_pamphlet.sh

4. Replace the pamphlet PDFs as described above, and reprint the pamphlet.

## Important

Do not rename the repository or the file `assets/Pamphlet_ABA_Resolution.pdf`. The QR code
and the website both depend on the current names.
