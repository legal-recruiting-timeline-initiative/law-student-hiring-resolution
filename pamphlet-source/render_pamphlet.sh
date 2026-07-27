#!/usr/bin/env bash
# Render pamphlet.html to Pamphlet.pdf via headless Chrome.
set -euo pipefail
cd "$(dirname "$0")"

CHROME=""
for candidate in \
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  "/Applications/Chromium.app/Contents/MacOS/Chromium" \
  "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"
do
  if [[ -x "$candidate" ]]; then
    CHROME="$candidate"
    break
  fi
done

if [[ -z "$CHROME" ]]; then
  echo "Google Chrome (or Chromium / Edge) not found." >&2
  exit 1
fi

HTML_URI="file://$(pwd)/pamphlet.html"
# --prefer-css-page-size prevents Chrome from shrink-to-fitting the page
# (which leaves the content looking small with empty margins).
"$CHROME" \
  --headless=new \
  --disable-gpu \
  --no-pdf-header-footer \
  --prefer-css-page-size \
  --virtual-time-budget=10000 \
  --print-to-pdf="Pamphlet.pdf" \
  "$HTML_URI"

echo "Wrote Pamphlet.pdf"
