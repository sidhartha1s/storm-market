# library/breaking — templates for the fast lane (`/storm-breaking`)

Sub-compositions (copy into `episodes/<slug>/compositions/`, re-prefix ids, hand-retune per cut;
never script-generate episode HTML):

| file | what | mount |
|---|---|---|
| `chapter-card.html` | 1.6 s caps chapter card on black, glitch in, hard cut out | track 2 over a 1.6 s track-1 blackout |
| `breaking-bug.html` | lower-third red kicker + channel wordmark + rotating headline strip | track 3, whole chapter or whole video |
| `stat-card.html` | left glass list, 4 numbered rows revealed on spoken cues | track 2 over footage |

The rest of the grammar is inline in `index.html` (copy from `episodes/br-elnino-california/index.html`):

- **popfig** (red Abril figure, ≤3 words, top 38 %): `.popfig .pf-big` CSS from ep6 + `pop(sel, at, hold)` (slam in 0.35 s, fade-up out).
- **data chip** (bottom-left running stat): `.chip` glass pill above the bug strip; `chipSet(text, at)`.
- **still-kenburns**: `<section class="clip still-wrap"><img>` + `kb(sel, at, dur, s0, s1, x0, x1, y0, y1)`; use it for a quick punch zoom in/out on the narration beat (short dur, bigger s0→s1), never a slow 3–6 % drift over the hold (DESIGN.md "Footage motion").
- **vertical-embed-credit**: `<section class="clip still-wrap contain-wrap">` holding a blurred cover copy (`img.blurfill` / `video.blurfill`) under the contained 9:16 clip, plus `.credit` lower-left `@handle · platform` for the clip's whole duration.
- **overlay-vignette**: `#vignette`, `#grade` (cold steel soft-light). The `#grain` canvas (`grain.js`, `filmLayer`) is retired: no grain on new work (DESIGN.md "Look: no grain"); shipped episodes keep theirs.
- **data-feed hold**: a labelled PD loop (`.srclab` "SOURCE: NOAA CPC") held 20–40 s with a slow push; one every 2–3 min.
- **captions**: burned word-highlight captions are NOT in v1 (needs a words.json → caption comp); add when the owner asks.

Pools: `library/breaking/<event>/` + `provenance.csv` — reused across every angle on that event, reordered, never the same sequence twice.
