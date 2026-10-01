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
Gates: `node scripts/graphics_qc.mjs episodes/<slug>`, then `python3 scripts/run_gates.py episodes/<slug>` (rules: `references/mg-quickref.md`).

## 8. RECEIPT (final message, ≤15 lines)
start/end times (`date +%H:%M:%S` first and last tool call) · loops · per loop: which §4 truths failed and the fix · gate line · final PNG folder.
