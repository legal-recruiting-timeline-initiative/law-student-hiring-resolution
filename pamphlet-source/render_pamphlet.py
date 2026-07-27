#!/usr/bin/env python3
"""Render pamphlet.html to a print-ready A4 PDF.

pamphlet.html references qr_site.png by relative path, so run this from inside
this folder (both files must sit together). Output is Pamphlet.pdf; copy it to:
  - documents/Pamphlet - A4 color (print this).pdf
  - assets/Pamphlet_ABA_Resolution.pdf

Prefers WeasyPrint when available; otherwise falls back to headless Chrome.
Requires one of:
  - pip install weasyprint  (and on macOS: brew install pango)
  - Google Chrome installed
"""
from pathlib import Path
from typing import Optional
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
HTML = HERE / "pamphlet.html"
OUT = HERE / "Pamphlet.pdf"


def render_weasyprint() -> bool:
    try:
        from weasyprint import HTML as WeasyHTML
    except Exception:
        return False
    WeasyHTML(str(HTML)).write_pdf(str(OUT))
    return True


def chrome_binary() -> Optional[str]:
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chromium-browser"),
    ]
    for path in candidates:
        if path and Path(path).exists():
            return path
    return None


def render_chrome() -> bool:
    chrome = chrome_binary()
    if not chrome:
        return False
    uri = HTML.as_uri()
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={OUT}",
        uri,
    ]
    subprocess.run(cmd, check=True, cwd=str(HERE))
    return OUT.exists()


def main() -> int:
    if not HTML.exists():
        print(f"Missing {HTML.name}", file=sys.stderr)
        return 1
    if render_weasyprint():
        print(f"Wrote {OUT.name} (WeasyPrint)")
        return 0
    if render_chrome():
        print(f"Wrote {OUT.name} (Chrome)")
        return 0
    print(
        "Could not render PDF. Install WeasyPrint (`pip install weasyprint`) "
        "or install Google Chrome.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
