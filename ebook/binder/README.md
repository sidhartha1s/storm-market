# The Binder — 61 fillable pages

`build.py` reads `../manuscript/P6-the-binder.md` and generates the forms. **The manuscript file is
the specification and is never edited by this script**: form titles, the "Serves N" lines, and every
field come out of the markdown, so a change to the spec flows into the pages on the next run. Nothing
here is retyped, which is the rule that keeps the forms and the book from drifting apart.

```bash
python3 build.py                    # writes out/binder.html
node ../build/fitcheck.mjs out/binder.html    # hard gate: must exit 0
node roomcheck.mjs out/binder.html            # balance report: flags pages >40% empty
```

`../build/paginate.mjs` splices `out/binder.html` into the book after Part Six's intro page, inlining
`templates/binder.css` as it goes. It reads this output fresh on every run and never edits it.

## Two gates, not one

`fitcheck.mjs` catches content that overflows the 6x9 box, where it would be **silently clipped** out
of the PDF. That is the correctness gate.

`roomcheck.mjs` exists because passing that gate is not the same as being laid out well. A form split
by fixed count rather than by measured content produced pages like Form 11's second page: two fields
and three-quarters blank paper, in a workbook someone paid for. `balanced_split()` now partitions a
form's groups by their actual field counts, and forms with genuine slack get a `.roomy` treatment
that spends it on write-in height rather than leaving it blank.

Four pages still report over 40% empty: the last page of Sections A, B, C and F. A section's forms do
not divide evenly into pages, so its final page is short. That is the one case where the emptiness is
structural rather than a distribution bug, and it is left alone.

## Page count

61 pages — one front sheet plus 60 form pages, covering all 41 forms. The manuscript budgets 80
across its seven sections. Nothing is missing: every form is present, and every explicit multiplier
is honoured (Form 2 four pages, Form 39 six, Form 41 four). Four forms are *longer* than planned and
were split further after measuring as overflowing. The 80 was a per-section estimate written before
anything had been laid out at real scale, and 61 is what 41 well-spaced forms actually take.

Form 23 is the one form whose page count is not stated in the spec ("one page per person", no
number). It prints the same count as Form 2, derived from Form 2's own parsed instruction rather than
hardcoded, and the page tells the reader to photocopy it for a larger household.
