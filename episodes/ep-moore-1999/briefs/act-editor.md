# Act editor brief · ep-moore-1999 (one editor per act, all five in parallel)

You are the editor for ONE act. You build that act's graphics (compositions) and write the act's picture mounts as an
HTML fragment the orchestrator reviews and pastes into index.html. You never edit index.html yourself.

## Inputs
- The act's segments, Picture lines and loop tags: `edit_script.md`, section `## A<n> ·` (locked text; never change a word).
- Graphics plan: `mg_plan.md` (rows naming your segments; library start points; deep vs standard).
- Timeline: every narration start and duration is already in `index.html` (`nx-a<n>-s<k>`), with the act's blackouts,
  holds, inserts, CTA and end ask. Word times: `audio/a<n>-s<k>.words.json` (whisper writes digits; "Moore" may read "more").
  Absolute time of a word = the nx element's data-start + the word's start.
- Footage: `media/stills/` (rows in provenance.csv; read a row before using a file: place, date, credit), `media/stills/sa/`,
  `media/stills/pixabay/` (stock fills, never under a named place or date), `media/clips/cuts/cut-*.mp4` (approved broadcast
  cuts; `cuts.tsv` in `C:\Users\Sidhartha\.claude\scratch\moore-cuts\` says which beat each serves). The three inserts that
  play their own audio are already mounted; every other clip you mount is `muted` and `class="graded"` if broadcast.
- Map family: `briefs/g-path-map-base.html` (KML A9 track, counties, towns, 10.664 px/mile, metro view x3.836) and the
  finished I1 variant `compositions/g-path-i1.html`. Copy, rename (comp id, root id, every class/id prefix), retime.
- Intro comps for style reference: `compositions/g-hook-overlay.html` (glass chips, popfig), `g-leadtime.html` (bars),
  `g-cellar-t1.html` (cellar door, reused in A2-S7).
- Rules: `references/mg-quickref.md` (read first, all of it), `library/inhouse/snippets/tokens.md`,
  `references/mg-brief-template.md` §6-7a, DESIGN.md "Cadence + sync rules" and "Footage motion".

## What you deliver
1. `compositions/g-a<n>-*.html` for every graphic your Picture lines call for (chips and source lines live inside comps,
   never as bare index text). Overlay comps (track 4) sit over footage you mount under them for their whole window.
2. `briefs/a<n>-mounts.html`: the fragment to paste. Contents, in time order, each with a one-line comment giving its
   arithmetic (nx start + word time):
   - picture track 1: `<section class="clip still-wrap" id="c-a<n>-..."><img id="kb-a<n>-..." ...></section>` stills
     (3 to 6 s each, never longer) and muted `<video>` clips (`data-media-start`, up to 12 to 15 s when the clip matches);
   - graphic hosts: `<div id="host-a<n>-..." data-composition-id=... data-composition-src=... data-start data-duration
     data-track-index="2" (full frame) or "4" (overlay) data-width="1920" data-height="1080">`;
   - at the end, a `/* A<n> punches */` list of `punch("#kb-...", <abs s>, <scale>)` lines for the orchestrator's script.
3. Coverage: every second from the act's first nx start to its blackout (or the CTA dip for A2) has picture on track 1
   or 2: no gap. Leave these windows EMPTY of picture (the orchestrator mounts them): the three insert windows, ins-paul-2
   (256.063-265.113), and the Paul segments still waiting for clips: A2-S9 452.709-459.371, A3-S9 626.978-635.112,
   A4-S6 760.747-768.596, A5-S4 917.056-924.454; and for A5 the end-ask window 1081.654-1097.154. A5-S11 (1097.454 to
   1111.052) is the channel title card + signature line: build `g-a5-close` from `library/inhouse/outro-brand.html` (full
   frame, track 2, to 1111.052).
4. Real clips before graphics: wherever the story reaches a moment someone filmed and a cut exists, show the film
   (CLAUDE.md "REAL clips"). A broadcaster's logo is never covered by a chip.

## Rules you could break
- GSAP only, paused timeline `window.__timelines["<comp id>"]`, no CSS keyframes, root id `<comp>-root`, unique ids
  (prefix everything with your comp name); three type tiers; something moves at least every 4 s; text >= 96 px from
  left/right, 54 px top/bottom; corner x >= 1600, y >= 680 empty when the presenter circle may show (any footage or
  overlay window); one text element per zone; numbers on screen only from the act's Picture lines and fact_check.md.
- A graphic starts on its trigger word, never before; reveals follow the voice's order; ~1 s land time after the last beat.
- Never a still over 6 s; never the same file twice in your act; never a stock clip under a named place or time.
- Comp timeline >= host window; a host never outlasts its timeline by > 4 s.

## Checks before you return
- `node scripts/freeze_scan.mjs episodes/ep-moore-1999 --comp <your comps>` and Read the sheets; for each comp read at
  least 2 settled frames; every chip, number and label matches its Picture line.
- `node scripts/graphics_qc.mjs episodes/ep-moore-1999` once at the end (the whole folder; failures in other acts' comps
  are not yours: report only yours). Browser gates one at a time, the laptop is shared.
- Your fragment: list its windows and show the coverage sum (no gap) in the receipt.

## Return (final message, at most 2,000 characters)
Comps (file + bytes), fragment path + byte size, coverage line (act start, act end, gaps = 0), gate line quoted, frames
read (folder), calls made, open items. Verdict PASS / PARTIAL / FAIL. Do not commit; never delete; never cd in Bash;
python3; never edit index.html, edit_script.md, provenance.csv or another act's files.
