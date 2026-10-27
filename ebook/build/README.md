# Book build pipeline

Zero dependencies beyond Node and Chrome. No npm install, no external assets, no image API at build time.

| File | What |
|---|---|
| `paginate.mjs` | **The layout pass.** Measures every block in Chrome, fills fixed pages, splices in the prebuilt binder and Appendix B, writes `book.html`. |
| `blocks_pipeline.py` | Flattens the 43 manuscript files into an ordered block stream, resolving `«FIG:»` markers and dropping authoring scaffolding. |
| `frontmatter.mjs` | Prepends cover, title, copyright and contents; writes `book-final.html`. Reads folios off the page, never computes them. |
| `figures.py` | The 24 code-drawn diagrams and 4 raster illustrations (`art/illustrations/*.jpg`, Figures 25-28), plus the manifest tying each to its file and protection. A missing illustration file fails the build. |
| `figures_preview.py` | Renders every figure onto fixed pages for QC without a full book build. |
| `book.css` | The print stylesheet. 6×9 trim, system fonts only, diagrams code-drawn SVG. |
| `book-auto.css` | The supplementary rules the auto-layout needs on top of `book.css`. |
| `front.css` | Cover, title, copyright and contents styling. |
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

## The page count is counted, not projected

**517 pages** (486 before the 2026-10-27 senior review added the start-here page, older-reader paragraphs, 15 figures and their sources). `paginate.mjs` runs `blocks_pipeline.py` to flatten the manuscript into ~3,200 blocks,
measures every one of them at the book's exact content width in headless Chrome, then fills fixed 6x9
pages from those measurements. `frontmatter.mjs` prepends the cover, title page, copyright page and
contents. `fitcheck.mjs` passes on all 517.

```
Front matter (cover, title, copyright, contents)    6
Part Zero — Front Matter                           10
Part One — Why People Die                          26
Part Two — The Core Six                           100
Part Three — The Hazard Playbooks                 177
Part Four — People and Places                      19
Part Five — Warning, Documents, Money              64
Part Six — The Binder (intro + 61 form pages)      62
Part Seven — The 60 Days                           10
Part Eight — Credits                                3
Sources                                            23
Appendix B — State Directory                       17
```

**The old density method was wrong and is kept here only as a warning.** It multiplied the manuscript
word count by 243 words/page, measured off `sample.html`'s 11 hand-laid body pages, and predicted
~570. Those sample pages are dense with wide-format components — spec grids, decision trees, money
bignums, forms — which burn far more vertical space per word than flowing prose. Extrapolating from
them overstated the book by roughly 17%. A page count is a measurement. Lay it out and count it.

## Layout rules that follow from the fixed-page model

- Every page is authored to fit. There is no reflow, so there are no widows, orphans, or
  surprise repagination — and no automatic pagination either. Prose pages are laid out, not poured.
- The `.folio` is the last child of every page, so the last *content* block is `nth-last-child(2)`.
  Its trailing margin is zeroed in CSS; otherwise it reads as overflow.
- Full-bleed pages carry `.cover` and are exempt from the footer-band check.
- Figures that need height control take an inline `height: Xin; width: auto` — `svg { width: 100% }`
  will otherwise blow the page.

## Constraints held

- **No stock imagery, no external fonts, no CDN.** System serif stack. Diagrams are code-drawn SVG; Figures 25-28 are ChatGPT-generated illustrations the owner asked for (2026-10-27), disclosed on the Credits page.
- **No federal seal, emblem, or logo** anywhere in the book — see the copyright page and the
  legal section of the design spec.
