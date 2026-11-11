# MG BRIEF TEMPLATE (storm-episode lane, owner-ordered 2026-09-12) — a diagram is a claim

Every bespoke motion graphic gets this brief before anyone draws. Sections 0–4 are the meaning layer and are written
FIRST, from CONFIRMED numbers (no `[verify]` inside a brief) and a published figure the drawing traces; the reviewer
checks §4 before layout, and any §4 failure ends the review. Sections 5–8 are the production layer. The worked example
(`references/mg-brief-example-g-slope.md`) is g-slope from Krakatau #5, the graphic that was drawn with the island underwater when the brief lacked §2/§4.
When no reference image exists: derive geometry from numbers through a stated scale, draw the blueprint yourself
(a 20-line SVG, screenshot it) and cite it; label anything without confirmed numbers SCHEMATIC, NOT TO SCALE.

## 0-5. The meaning layer (fill each from CONFIRMED numbers; worked example: `references/mg-brief-example-g-slope.md`)
- 0. What this graphic claims: the one or two facts that carry the beat; everything else on screen serves them.
- 1. SOURCE: the published figure(s) the drawing traces, with the confirmed text and numbers quoted.
- 2. DATUM, SCALE, ORIENTATION: fixed px numbers the reviewer measures against (datum line, px-per-unit, exaggeration, compass sides).
- 3. GEOMETRY: every shape in px, before and after states, hit within ±10 px.
- 4. MUST BE TRUE IN THE PICTURE: numbered truths with ratios; the reviewer checks these FIRST and any failure = FIX. §4 wins over §3 when they conflict, and the builder reports the conflict.
- 5. PANEL TEXT (exact) and CUES in seconds from words.json.

## 6. CONTRACT
- One file, `<template>` wrapping `<style>` + `<div id="root" data-composition-id="COMPID" data-width="1920" data-height="1080">` + `<script>`
  building a PAUSED gsap timeline registered as `window.__timelines["COMPID"] = tl;` (create `window.__timelines` if missing). gsap is provided
  by the host; do not include it. All element ids prefixed with your suffix. Root transparent.
- Type and motion: `references/mg-quickref.md` "Type tiers" and "Motion and exits" (the one home; do not restate them here).
- Nothing overlaps text or shapes; all text at least 96 px from the left/right edges and 54 px from top/bottom; every label next to the
  thing it names. Every other rule: `references/mg-quickref.md`.
- Mount only the trimmed cut files named in this brief, never a full source clip. Edit only your own `compositions/` file(s), never
  another builder's or index.html: the orchestrator mounts your host div in index.html before dispatch, so §7 finds your comp.
  How files may be changed: CLAUDE.md "do not write code for what reasoning already does" (ep-nepal: full clips, crossed files, script splices).

## 7. TOOLS (run from your episode worktree root; paths are repo-relative)
Pre-render look: `node scripts/freeze_scan.mjs episodes/<slug> --comp <COMPID>` writes a contact sheet (a tile every 3 s) to
`episodes/<slug>/sheets-pre/`. Read it and check §4 first, then overlaps/cut-offs. `python3`, never `python`.
Gates: `node scripts/graphics_qc.mjs episodes/<slug> <your comp ids>` checks only your graphics, on the real folder: no private stage copy, no grep for your ids. `python3 scripts/run_gates.py episodes/<slug>` is the orchestrator's pre-render run over every comp, not yours (rules: `references/mg-quickref.md`).

## 7a. DONE LINE (all seven, before the receipt; why: `learnings/mg.md` 10 Oct 26)
1. Gates on the real folder after the last edit, each run on its own: `graphics_qc ... <your comp ids>` 0 errors, and none of your comps named by `python3 scripts/sweep_episode.py episodes/<slug>` ("graphic window fits its timeline"), `node scripts/blank_scan.mjs <absolute path of episodes/<slug>>` (it opens the path as given, so a relative one fails), `node scripts/overlap_check.mjs episodes/<slug>` or `node scripts/occlusion_check.mjs episodes/<slug>` (the gates of `scripts/run_gates.py` that name a comp). An overlay's host starts on its first mark. A repeat or a touch is declared only after a frame read (`data-repeat-ok`, `data-overlap-ok`: `references/mg-quickref.md`).
2. Fill: `references/mg-quickref.md` "Frame coverage". State the figure you measured.
3. Frame 0 shows the opening state, and a full-frame host has its ground on from frame 0 (no dark empty frame after the cut).
4. Seek order: each cue second captured twice (fresh page forward only; then seek 0, past it, back to it) and the two frames match. Never `autoAlpha`, `opacity` or `svgOrigin` only in the from vars of a deferred tween.
5. No label under a line, ring, arrow, dot, rain or another label, including the first half second of every entrance.
6. Shared numbers (road layout, scales, counts) are computed from the brief's table by a script and stated in the receipt, never placed by eye.
7. Overlay comps: one frame composited over the real picture mounted under them at that second; a transparent span names the clip that sits under it. A label that names a place, a date or an event is a claim about that picture: the file under every second of the label is footage of that place and date by its `provenance.csv` row, never stock.
A family built on one base: send the base alone for a full-size read before copying it.

## 7b. TIME BOX AND PRE-FLIGHT (owner 11 Nov 26; test: `learnings/mg.md` 11 Nov 26)
The builder gets a clock, not an open end: turn 1 is 15 minutes, a second turn 10, a third 8, then the graphic ships
with what is open listed (owner: "a maximum number of two to three turns ... The turns should be shorter than the last
one"). Turn 1: the whole file written once by minute 6 (never a partial file grown by edits), gates and the contact
sheet by minute 11, one fix pass, stop at 15 with an honest list. A later turn gets only the verifier's fix order and
touches nothing else. The brief's writer checks these before dispatch, the builder before the receipt:
1. The brief states the MOUNTED host length and the cue offset when the host starts inside its narration (cue = wav
   time minus the offset), and every text is at opacity 0, or the exit done, by the host's last 0.05 s.
2. No rule in the brief contradicts another (a push and "the last frame is P0"; a label at a radius the needle
   sweeps; a chip that cannot fit its size inside the safe zone; a credit that would be false on that ground).
3. `freeze_scan.mjs --comp` passes: no stretch of 6 s or more where nothing visibly moves. A shimmer its detector
   cannot see does not count; name the motion that carries each long hold in the brief.
4. Every text node reaches full opacity at some sampled second (a source line left hidden is a fail).
5. Last frame: every pin and label that the brief gives a final position sits within 10 px of it.
6. Basemap: at both ends of every camera move the visible box is inside the map's own coverage.

## 8. RECEIPT (final message, ≤15 lines)
start/end times (`date +%H:%M:%S` first and last tool call) · loops · per loop: which §4 truths failed and the fix · gate line · final PNG folder.
