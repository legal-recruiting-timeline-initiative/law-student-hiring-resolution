# How to edit and rebuild the pamphlet

This folder holds the editable source for the pamphlet. The finished pamphlet is a PDF, which
cannot be edited directly. To change it, you edit the template here and rebuild the PDF. This
takes a one-time software setup and is best done by someone comfortable running commands on a
computer. If that is not you, hand this folder to a technical helper.

## What is in this folder

- `pamphlet.html` - the pamphlet template. This is where the words, layout, and colors live.
- `qr_site.png` - the QR code image embedded in the pamphlet.
- `badc-logo.png` - the BADC seal shown in the pamphlet header. This is a copy of
  `assets/cropped-BADC-Logo.png`; if the seal is ever replaced, update both files.
- `render_pamphlet.py` - the script that turns `pamphlet.html` into a PDF.
- `generate_qr.py` - the script that regenerates the QR code (only needed if the website
  address changes).

## One-time setup (Mac)

Install the tools the build needs:

    brew install pango
    pip install weasyprint "qrcode[pil]"

(`brew` is Homebrew, from https://brew.sh. `pip` comes with Python.)

## To change the pamphlet's words or design

1. Edit `pamphlet.html`. The text is plain and readable; change the words you want.
2. Rebuild the PDF:

       python render_pamphlet.py

   This writes a new `Pamphlet.pdf` in this folder.
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

       python render_pamphlet.py

4. Replace the pamphlet PDFs as described above, and reprint the pamphlet.

## Important

Do not rename the repository or the file `assets/Pamphlet_ABA_Resolution.pdf`. The QR code
and the website both depend on the current names.
