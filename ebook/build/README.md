# Book build pipeline

Zero dependencies beyond Node and Chrome. No npm install, no external assets, no image API.

| File | What |
|---|---|
| `book.css` | The print stylesheet. 6×9 trim, system fonts only, all figures code-drawn SVG. |
| `sample.html` | 12-page sample spread — cover, legal, TOC, region finder, two protections, chapter opener, decision tree, the money page, a binder form, a 60-day week, the state directory. |
| `fitcheck.mjs` | **Hard gate.** Fails the build if any page overflows its box. |
| `sample.pdf` | Rendered output. Open this. |

## Build

```bash
# render to PDF (absolute output path — Chrome refuses relative paths here)
"C:/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --disable-gpu \
  --no-pdf-header-footer --print-to-pdf="<ABSOLUTE>/sample.pdf" \
  "file:///<ABSOLUTE>/sample.html"

# overflow gate — must exit 0 before any render is considered done
node fitcheck.mjs sample.html
```

## Why the gate exists

Every `.page` is a fixed 6×9 box with `overflow: hidden`. Content that does not fit is **silently
clipped** — no error, no warning, it simply is not in the PDF. On the first render of this
12-page sample, 8 pages overflowed and only 2 of them were visible to the eye. Across ~490 pages
that failure mode is fatal, so the gate is not optional.

`fitcheck.mjs` drives Chrome over raw CDP (no puppeteer), measures every child box against the
reserved footer band, and exits 1 with the offending element and the overflow in pixels.

**Do not use `scrollHeight` for this.** It adds the box's bottom padding after the last in-flow
child, so a page that fits perfectly reports ~58px of phantom overflow. Geometry against the
footer band is the real test. This is documented in the source because it wasted a cycle.

### If it fails with "Chrome DevTools endpoint never came up"

That is **not** a layout failure and not a Chrome-path problem. The Bash tool's sandbox blocks
Chrome from binding its remote-debugging port, so `endpoint()` times out after 15 seconds while the
HTML is perfectly fine. Re-run the same command with the sandbox disabled and it passes. The same
applies to `landing/widthcheck.mjs` and `landing/shot.mjs`. Verified 2026-07-29 — a run that failed
this way passed unchanged outside the sandbox.

## Measured page density — where the page count comes from

The 12-page sample's 11 body pages carry **2,673 words**, i.e. **243 words per page** average,
already including pages that hold SVG diagrams and tables. That is the multiplier to use for any
page projection, and it is measured rather than assumed.

Current manuscript: **117,554 words**, of which 114,637 are prose (the Binder's 2,917 words are laid
out as fixed forms, not poured text). That is 472 prose pages, plus 80 binder pages and 18 appendix
pages — **about 570**. The published figure of 488 is therefore a **floor**: the book is now
materially longer than advertised, because closing all 130 citations added ~23,600 words of quoted
primary material. Still a projection from density rather than a count of laid-out pages. **Recount
after layout and reset the landing page figure before launch.**

## Layout rules that follow from the fixed-page model

- Every page is authored to fit. There is no reflow, so there are no widows, orphans, or
  surprise repagination — and no automatic pagination either. Prose pages are laid out, not poured.
- The `.folio` is the last child of every page, so the last *content* block is `nth-last-child(2)`.
  Its trailing margin is zeroed in CSS; otherwise it reads as overflow.
- Full-bleed pages carry `.cover` and are exempt from the footer-band check.
- Figures that need height control take an inline `height: Xin; width: auto` — `svg { width: 100% }`
  will otherwise blow the page.

## Constraints held

- **No stock imagery, no external fonts, no CDN.** System serif stack, code-drawn SVG only.
- **No image API needed to ship.** DeAPI illustration slots get added later; the book lays out
  complete without them.
- **No federal seal, emblem, or logo** anywhere in the book — see the copyright page and the
  legal section of the design spec.
