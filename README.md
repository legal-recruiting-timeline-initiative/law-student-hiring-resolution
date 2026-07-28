# BADC / ABA Resolution: Let Law Students Become Law Students First

This is the home for everything in the Bar Association of the District of Columbia (BADC)
campaign for a resolution before the ABA House of Delegates on accelerated law-firm
recruiting timelines. It holds the live website, the printable pamphlet, the resolution
draft, and the editable source files.

**You do not need any technical background to use most of this.** This page explains what
is here and how to make simple changes.

## The live website

    https://legal-recruiting-timeline-initiative.github.io/law-student-hiring-resolution/

This is the address the pamphlet's QR code opens. It updates automatically a minute or two
after any change is saved here.

## What is in this repository

Think of this repository as a shared folder. Here is what each part is:

| Folder or file | What it is | Can I edit it easily? |
| --- | --- | --- |
| `index.html` | The website's main page (what the QR code opens). Its main button links directly to `documents/Resolution.pdf`, the complete, unaltered resolution and report | Yes, see "Editing the website" below |
| `documents/` | Ready-to-use files: the printable pamphlet and the resolution (the full resolution, report, and addenda) | These are finished files, download and use them |
| `pamphlet-source/` | The editable "template" the pamphlet is built from, for a technical helper | Editing here needs some setup, see that folder's guide |
| `assets/` | A copy of the pamphlet the website links to (leave this one alone) | Do not rename |

The site intentionally links straight to the PDF for the full resolution and report,
rather than reproducing the text on a web page, so nothing about the filed document can be
transcribed incorrectly or look altered.

### The `documents/` folder holds

- **Pamphlet - A4 color (print this).pdf** - the final print file. Double-sided A4.
- **Resolution.pdf** - the resolution, report, and addenda as a PDF (for reading and sharing).

## Editing the website (no technical background needed)

You can change the words on the website right here in your browser:

1. Open `index.html` (the main page). Click its name in the file list above.
2. Click the **pencil icon** (top right of the file) to edit.
3. Make your change. The text is surrounded by tags that look like `<p>...</p>`. Just edit
   the words between the tags and leave the tags alone.
4. Scroll down, add a short note about what you changed, and click **Commit changes**.
5. Wait one to two minutes, then refresh the live website to see your edit.

If something looks wrong, you can always undo: the site keeps a full history of every change.

## Editing the pamphlet (needs a technical helper)

The pamphlet is a finished PDF. You cannot edit its text or design directly in your browser.
To change it, a technical helper edits the template in the `pamphlet-source/` folder and
rebuilds the PDF on their own computer. Step-by-step instructions are in
`pamphlet-source/HOW-TO-EDIT.md`. Once they produce a new pamphlet PDF, it replaces the two
copies (the one in `documents/` and the one in `assets/`).

## Two things to never rename

1. **Do not rename this repository** (`law-student-hiring-resolution`). The pamphlet's QR
   code points to the current address; renaming breaks it.
2. **Do not rename `assets/Pamphlet_ABA_Resolution.pdf`.** The website links to it by that
   exact name.

## Questions

- Philippe Lin, plin@vasquezlawdc.com, (812) 345-7083.
- Lorie Masters, lmasters@hunton.com, (202) 595-4600.
