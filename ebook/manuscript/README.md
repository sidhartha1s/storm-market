# Manuscript status

Outline: `../OUTLINE.md` · Design contract: `../../docs/superpowers/specs/2026-07-25-ebook-funnel-design.md`

**Draft 1 of the whole book is complete: 93,969 words, all 130 protections, all 23 hazard
playbooks.** The remaining work is citation sourcing, layout, and the state-directory research —
not writing.

Page figures use the **measured** density from the rendered sample: **243 words per page**, taken
from the 11 body pages of `../build/sample.html` (2,673 words), which already includes pages
carrying SVG figures and tables. The earlier "350 words/page" estimate in this file was replaced
because it was a guess and the measurement exists.

| Part | Files | Words | pp @243 | Budget | Protections | Refs open |
|---|---|---|---|---|---|---|
| Zero — front matter | 1 | 2,179 | 9 | 12 | — | 0 |
| One — why people die | 2 | 7,127 | 29 | 26 | — | 11 |
| Two — the core six + structure | 7 | 18,731 | 77 | 62 + 16 | 1–84 | 38 |
| Three — hazard playbooks | 23 | 42,703 | 176 | 204 | cross-referenced | 77 |
| Four — people and places | 2 | 4,909 | 20 | 34 | cross-referenced | 3 |
| Five — warning, documents, evacuation, electronics | 4 | 12,293 | 51 | 30 | 85–130 | 21 |
| Six — the Binder (41 form specs, laid out as 80 form pages) | 1 | 2,885 | 80 | 80 | — | 0 |
| Seven — the 60 days | 1 | 3,142 | 13 | 22 | 45 scheduled | 0 |
| Appendix B — state directory | generated | — | 18 | 18 | — | — |
| **Total** | **41** | **93,969** | **~487** | **488** | **130/130** | **150** |

**The 488-page claim on the landing page is therefore accurate to within one page** — but it is a
projection from measured density, not a count of laid-out pages. Recount after layout.

Part Three ran shorter than its 204pp budget and Parts Two and Five ran longer. That is fine and it
was the right trade: the protections carry the detail and the playbooks stay navigable under stress,
each ending in a one-page version. Do not pad Part Three to hit a number.

## What is actually outstanding

1. **150 open `«CITE:»` markers.** Each one gets a primary source and a retrieval date, or the claim
   is cut. This is the gating item for the whole product and it is research, not writing.
2. **Layout** — hand-laying 41 markdown files into fixed 6×9 pages, with `fitcheck` exit 0.
3. **The state directory data** — ~51 rows × ~20 sourced fields. See `../appendix/README.md`; the
   generator refuses to render placeholder rows.
4. **Illustration slots** — the book lays out complete on code-drawn SVG. DeAPI figures are additive.

## Protection-block format (established in P2-C1, hold it)

```
### N · Name
**Prevents:** one line, names the failure mode.
**Cost:** band · **Time:** honest · **Materials:** buyable without a second search
· **Regions:** which of the five rank it, with rank where known.

Body prose. Numbered steps only where order is load-bearing.

**What this does not do:** the honesty line. Non-negotiable — this is the trust mechanism,
and it is where the book earns the right to be believed on everything else.
```

**Hard rule discovered while writing the water chapter:** dosing ratios, temperatures, and safe-time
thresholds are **never written from memory** — they go in as `«CITE:»` markers naming the authority,
even when the number feels well known. A wrong bleach ratio or a wrong danger-zone temperature hurts
a reader. Both chapters flag this at the top of the file.

## Citations — the marker, and how they render

**In the manuscript** a claim needing a primary source carries a `«CITE: description»` marker naming
what to pull. **No invented numbers appear anywhere.** At the research pass each marker is either
replaced with a sourced figure and a retrieval date, or **the claim is cut** — never softened into a
vague version of itself. Same rule as the money chapter; see `../MONEY-CHAPTER-RESEARCH.md`.

**In the reader-facing book they render as numbered references** — a superscript `[n]` in the text,
the source itself in the **Sources** chapter at the back, grouped by chapter and numbered
continuously. `../build/review_pdf.py` already does this: it strips every marker, banks the
description, and builds the Sources chapter automatically. Nothing marker-shaped ever reaches a
reader's page, and there is no highlighting in the output.

Do not put the marker convention in a note at the top of a chapter file. That was done in 38 files
and every one of those notes was itself picked up as a citation, inflating the count by 38 — the real
figure was 150, not 188. The convention is documented here, in one place.

Count the markers before layout. A chapter that reaches layout with an open marker is not finished.

## Layout

Prose is drafted in markdown, then hand-laid into fixed 6×9 `.page` boxes — the model in
`../build/book.css`. There is no reflow and no automatic pagination, which is deliberate: it gives
total control over where figures, protection blocks and forms land, at the cost of manual
pagination.

**`node ../build/fitcheck.mjs <file.html>` must exit 0 before any render is considered done.**
Content that overflows a page is silently clipped. On the first render of the 12-page sample, 8
pages overflowed and only 2 were visible to the eye.

## Voice notes (established in Part One — hold these)

- Declarative and forensic. No hype, no doom, no survivalist register.
- Name the mechanism, then the mistake, then the fix. In that order.
- Say the uncomfortable thing plainly rather than implying it — the isolation statistics, the
  income problem, the fact that the reader may be the highest level of care available for some hours.
- Absolutes stay absolute where the failure mode is fatal and the exception is always invented at
  2am by a tired person: generators, combustion indoors, moving water.
- State the boundary of competence explicitly and say why. No dosing, no suturing, no fracture
  reduction, no gas or panel work.
- Cross-reference protections by number, always. The numbers are the book's spine.
