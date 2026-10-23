# Preview render: an act or a time window at 360p, before the whole episode is green

Status: design + sketch (23 Oct 26). Nothing is wired: `scripts/render.cmd` is unchanged, `scripts/derive_preview.py`
has `NotImplementedError` bodies. Building it needs the owner's yes on the rule changes at the bottom.

## Problem

The owner wants a first look at act 1 while acts 3 to 5 are still being composed, at about 360p, and cheap
re-renders while iterating. Today the only path is `scripts\render.cmd <slug> draft`: the whole episode, 1920x1080,
15 fps, after every gate is green. El Reno's draft (1333 s, ZBook, 3 workers, learnings/render.md 10 Oct 26) took
34.6 min: compile 20 s, audio mix 255 s, capture 1511 s, assemble 282 s.

What the shape has to live with:
- hyperframes 0.8.185 has no time-range or frame-range flag (`render --help`), and acts are not compositions: an
  episode is one flat `index.html` with absolute `data-start` on every element and one GSAP timeline with absolute
  times, registered as `window.__timelines[<root id>]`.
- The renderer cannot capture below the composition size through any flag (see "What is impossible").
- The producer schedules audio and video node-side from the DOM attributes `data-start`, `data-duration`,
  `data-media-start` (chunk-IVEFOUZI.js about line 6866), and seeks the page through the registered timeline.
- render.cmd stays the one recipe (preflight, render_busy worker fit, GPU pin, env lines); one heavy job at a time;
  every background command hidden; no script authors `index.html` or `compositions/*.html`.

## Usage (caller's view)

```
REM first look at act 3 while acts 4-5 are still being built (hidden schtasks launch, as for any render)
set RENDER_WINDOW=a3
scripts\render.cmd ep4-el-reno preview
REM -> episodes\ep4-el-reno\renders\ep4-el-reno-preview-546.10-830.50.mp4   (640x360, 15 fps)

REM iterate on one graphic around 9:12: a 40 s window, re-rendered after each fix
set RENDER_WINDOW=9:05-9:45
scripts\render.cmd ep4-el-reno preview

REM whole episode at 360p (replaces a second full-size render when only a look is needed)
set RENDER_WINDOW=all
scripts\render.cmd ep4-el-reno preview
```

The file name carries the effective window: an owner timestamp on a preview maps back as `episode time = preview
time + t0`. `RENDER_FPS=8` (already read by render.cmd) halves capture again when motion does not matter.

Inside render.cmd the `preview` branch runs, in order: sweep `_*_tmp.html`; `python derive_preview.py <ep>
%RENDER_WINDOW% %RENDER_HEIGHT%` (default 360; writes `_preview_tmp.html` and its manifest); `render_preflight.py <ep>
preview` (busy box, pin drift, media budget of the staged page only; skips the LAYERS table, since a half-built episode
lacks layers by definition); `render_busy.py --launch` unchanged; then
`npx hyperframes@<pin> render . -c _preview_tmp.html --gpu --browser-gpu --experimental-fast-capture=true --quality draft --crf 32 --fps %_FPS% --workers N`.

## Shape

One module, `scripts/derive_preview.py`, one public operation `stage_preview(ep, spec, height)`. Everything else is a
pure function of `(index_html, timeline_rows, spec, height)`. Data first (`Window`, `Timed`, `Root`, `PreviewPlan` in
the sketch). The derive changes exactly this and nothing else:

1. Snap t0 left until no sub-composition host straddles it (sub-compositions cannot be trimmed; `data-media-start`
   trims media only). Terminates: t0 only decreases over a finite set of starts, and 0 is always safe.
2. Drop every timed element fully outside the window: fewer probes, a smaller audio mix, and out-of-window comps are
   never compiled, so builders may keep editing them.
3. Shift every kept element: `data-start -= t0`. Media straddling t0 get start 0 and `data-media-start += t0 - start`;
   anything straddling t1 is cut to t1.
4. Root: `data-duration = t1 - t0`; at 360, `data-width=640 data-height=360`.
5. Inject one fixed block first in `<head>`: `html { zoom: 0.333333 }` and a clock shim, a `Proxy` on
   `window.__timelines` that wraps only the root id as `outer.add(tl.tweenFromTo(T0, T1, {ease: "none"}), 0)`.
   Sub-composition timelines pass through: their hosts were shifted in step 3.

Why the shim and the attribute shift are both needed: the page clock comes from the timeline, the sound and video from
the attributes. Either alone puts picture and sound at different times.

Content-blind by construction: the plan reads tag, id, time attributes, whether `data-composition-src` is present,
and byte spans. It never reads text, classes, styles, `src` or script bodies, and writes only time attributes, whole
element drops, root size and duration, and the fixed block. `assert_content_blind` (reverse the plan, require the
original bytes) and `assert_identity` (window `all` at 1080 changes only the block) run on every call.
Validation sits at the boundary: a non-numeric time, a host without `data-duration`, a time attribute the plan does
not model, or a second root is a refusal naming the element, never a guess.

Interface depth: one command and two env knobs in render.cmd's existing style (`RENDER_WINDOW`, `RENDER_HEIGHT`)
hide snapping, dropping, trimming, the shim and the self-checks.

## The one safety fact

A preview is only safe if frame n of the window equals frame n + t0*fps of the whole render. The prototype checks
exactly that on demo-pin (WebGL comp, burned-timecode video, audio) with SSIM, at 1080 and at 360 against a
downscaled whole render (table below, rows w1-w3). The same check belongs in `pin_ritual.py`, so a hyperframes bump
that breaks the shim fails the ritual, never a preview.

## Synthesis decision

Two structurally different candidates were drawn (architect arena, two Opus runners, one Sonnet cross-judge):
- A, no derived HTML: segmented capture with black placeholder segments seeded outside the wanted act, so `--resume`
  (which checks only hash, byte size and frame count) skips them; ffmpeg downscale to 360p after.
- B, a content-blind derive of a gitignored window page at a 640x360 viewport.

Base: B. The judge scored B higher on the owner's asks (window cuts audio, capture and assemble; 360p cuts capture,
which A cannot) and on interface depth, A higher on rule fit and correctness risk. The prototype settled the open
B risks it could (zoom renders, rho measured); A's core trick depends on two undocumented internals (the resume
validation rule and a temp `audio.m4a`), pays the whole-episode audio mix twice per act, and captures at 1080.
Grafted from A: the preflight split (preview keeps busy, pin and media budget, skips the LAYERS table) and the
pin-ritual re-check of every renderer behaviour the design leans on. Rejected from A: placeholder seeding (fooling
the renderer's resume check is a mask, not a path), the probe-and-kill launch, the progressive per-act watcher.

## Measured prototype (23 Oct 26)

demo-pin copy (MG with CSS 3D + three.js WebGL comp + video + audio), cut to 8 s unless noted. 1 worker (2 workers
needs 2.9 GB by `render_busy.need_gb`, over the 2 GB run budget), `--quality draft --crf 32 --gpu --browser-gpu
--experimental-fast-capture=true` as render.cmd. Wall = launch to the renderer's "rendered in" line. RAM = private
bytes of the render tree plus headless Chrome. Scratch harness, not committed.

| Run | Box | Setup | Wall s | Result |
|---|---|---|---|---|
| r1 | ASUS | 24 s, seg, 60-frame segments, 15 fps | 82.5 (killed) | free RAM 3.32 to 1.28 GB with other sessions' gates live; killed at frame 177/360 |
| r3 | ASUS | 8 s, seg cold, 8 fps | 64.6 | compile 3.9, audio 2.7, capture 24.9, assemble 6.3; 3 segments (HF_SEGMENT_FRAMES=16 clamps to the 30 minimum); peak 1.39 GB |
| r2, r4 | ASUS | seg runs | killed at 5-32 s | box under the 0.9 GB free floor (other sessions); moved to the ZBook |
| z1 | ZBook | 8 s, seg cold, 8 fps | 39.2 | compile 2.3, capture 32.4, encode 23.6 (overlapped), assemble 0.8; node lingered to the 180 s cap after "Render complete" |
| z2 | ZBook | same, unchanged, --resume | not recorded | ZBOOK_Z2 |
| z3 | ZBook | one-line `index.html` edit, --resume | cap | 0 segments skipped |
| z4 | ZBook | one-line edit in `compositions/g-tanker-throw.html`, --resume | 34.6 | 0 segments skipped: full recapture |
| z5 | ZBook | 1080, 15 fps | 35.8 | peak 1.41 GB |
| z6 | ZBook | 1080, 8 fps | 25.7 | peak 1.35 GB |
| z7 | ZBook | 1080, 8 fps, --low-memory-mode | 26.6 | no gain over z6 |
| z8 | ZBook | 640x360 root + `transform: scale(1/3)` on hosts, 8 fps | 20.9 | peak 1.06 GB |
| z9 | ZBook | 640x360 root + `html { zoom: 1/3 }`, 8 fps | 21.0 | peak 1.11 GB |
| z10 | ZBook | 640x360 zoom, 15 fps | 24.2 | peak 0.98 GB |
| w1-w3 | ZBook | 24 s whole vs hand-derived window [14, 20] at 1080 and 360, 8 fps, SSIM at window frames 8/24/40 | WINDOW_ROWS | WINDOW_SSIM |

Two-point fit (frames = 120 at 15 fps, 64 at 8 fps): 1080 costs 0.180 s per frame over 14.2 s fixed; 360 costs
0.057 s per frame over 17.3 s fixed. So **rho = 0.32**: a 360p frame costs a third of a 1080p frame. Lower fps scales
the frame count linearly. `--low-memory-mode` buys nothing. Segmented capture costs more than plain capture on a short
comp (z1 39.2 s vs z6 25.7 s) and, by z3/z4 and the source, reuses nothing after any HTML edit.

### First-look estimate

`T(W) = 20 + W * (0.191 + 1.345 * (fps / 15) * rho)` seconds, from El Reno's ZBook draft per composition second
(audio 0.191, capture + assemble 1.345) and the measured rho. Audio scales with W because out-of-window media are
dropped.

| Window W | Today (draft, 1080, 15 fps) | Preview 360p, 15 fps | Preview 360p, 8 fps |
|---|---|---|---|
| 60 s iteration | 1.9 min (not possible today) | 1.0 min | 0.8 min |
| 270 s act | 7.2 min (not possible today) | 3.1 min | 2.2 min |
| 1333 s whole | 34.5 min | 14.1 min | 9.6 min |

Assumptions to recheck on the first real preview: rho came from a 1-worker 8 s MG comp; El Reno is video-heavy and
renders at 3 workers; assemble is scaled with pixels like capture.

## What is impossible, and the line that says so

- A capture smaller than the composition through the CLI: `resolveDeviceScaleFactor` returns 1 with no
  `--resolution`, else `Math.max(target.width / compositionWidth, target.height / compositionHeight)`
  (chunk-IVEFOUZI.js), and the presets are landscape 1920x1080 and up, "the scale must be an integer multiple".
  So 360p needs a 640x360 root (the derive's zoom block), not a flag.
- A time range through the CLI: `render --help` (0.8.185) has no start, end or range option. `-c` renders one
  composition file, and acts are not compositions.
- Segment reuse across an edit: `computeSegmentPlanHash` hashes `compositionHash` = sha256 of the whole compiled
  HTML, and sub-compositions are inlined before hashing (`inlineSubCompositions2`, then
  `computeCompositionObservabilityHash(compiled.html)`). Any one-line edit, root or sub-composition, moves every
  segment to a new plan directory (z3, z4: 0 skipped). `totalFrames` is in the hash too, so any duration change does the same.
- Media bytes are not in that hash. A replaced clip under the same file name would be reused stale by `--resume`.
  One more reason not to build iteration on resume.

## Tradeoffs accepted

- We accept a window that opens up to one graphic early (t0 snapped to a host start) in exchange for never trimming a
  sub-composition, which the runtime cannot do.
- We accept a preview that skips the editorial gates in exchange for a look before they pass. It is never a review
  cut and never a gate result; the draft still waits for `run_gates.py` green.
- We accept GSAP "target not found" warnings for tweens on dropped elements, in exchange for never reading the
  timeline script. El Reno's script reaches the DOM only through GSAP selectors (0 `querySelector` /
  `getElementById` in its `index.html`).
- We accept that a WebGL canvas still draws at its own size under zoom; only the captured pixels shrink.

## Alternatives considered

- Segment seeding (candidate A). Lost: relies on fooling `validateCompletedSegments`, pays the audio mix twice per
  act, and capture stays 1080 (360p is a file-size change only).
- Whole episode at 360p with no window. Kept as `RENDER_WINDOW=all`; alone it still waits for the last act's media.
- Segmented capture with `--resume` for iteration. Lost: zero reuse after any edit (source + z3/z4).
- Split acts into separate compositions. Lost: an authoring change to every episode, and the tripwire forbids a script doing it.
- `transform: scale()` on hosts instead of `zoom` on `html`. Same speed (z8 vs z9); lost because it fights any tween
  on a host's own transform.

## Open questions and risks

- Does `render -c _preview_tmp.html` also discover `index.html` and mix its audio? If so, stage under `.preview/`
  with `<base href="../">` as `stage_comp.mjs` does. (w2/w3 rendered `index.html` beside the window page: WINDOW_AUDIO.)
- `filmLayer(tl, DUR)` and any `onUpdate` on the root timeline run under `tweenFromTo`; the grain must be checked on the first real preview.
- On the ZBook, node stayed alive more than 140 s after "Render complete" in every run of this prototype. If that
  holds for render.cmd too, its done marker lands minutes late. Not checked on a real render.
- The ZBook stopped answering ssh ("Connection reset") during the window check at 12:47; see the run notes.

## Next implementation step

Write `read_timed` and `plan_preview` with both self-checks, run them on El Reno's `index.html` (read only) for
`a3` and `all`, then render demo-pin through the preview branch and add the frame-equality check to `pin_ritual.py`.

## Rule changes needed (owner's decision; none is made here)

1. CLAUDE.md, "HARD RULE: the render is the LAST step". Current:
   > Never use a render as a diagnostic. All green before ANY render, from the worktree:

   Proposed:
   > Never use a draft or full render as a diagnostic. All green before ANY draft or full render, from the worktree:
   > (...) A preview (`scripts\render.cmd <slug> preview`, 360p, one time window) needs only its own preflight
   > green (busy box, pin, media budget of the window). It is a look, never a review cut and never a gate result.

2. CLAUDE.md, "HARD RULE: do not write code for what reasoning already does", after the TRIPWIRE. Current:
   > TRIPWIRE: no script may author episode HTML (`index.html`, `compositions/*.html`): cuts, holds, graphics, text,
   > asset picks, timing design. Delete it on sight. The test: if the script must know what a beat MEANS, it is authoring.

   Proposed (append):
   > A derive that writes a gitignored page beside them (`_preview_tmp.html`, `.qc-tmp/`) is not authoring when it
   > only drops, shifts and trims timed elements by their numbers and injects the fixed preview block. Its own check
   > runs on every call: the window `all` at 1080 changes nothing but that block.

3. CLAUDE.md, same render section. Current:
   > Do not start a render while any builder is still editing. No live subagent, quiet `git status`, then launch.

   Proposed:
   > Do not start a draft or full render while any builder is still editing. No live subagent, quiet `git status`,
   > then launch. A preview may run while builders edit other acts, if no builder is editing a file in its manifest
   > (`_preview_tmp.html.json`).

4. CLAUDE.md, same section. Current:
   > Render only with `scripts\render.cmd <slug> <draft|full> [out-basename]`.

   Proposed:
   > Render only with `scripts\render.cmd <slug> <draft|full|preview> [out-basename]`; a preview takes
   > `RENDER_WINDOW` (`a3`, `9:05-9:45`, `552-830.5` or `all`) and `RENDER_HEIGHT` (default 360).

5. CLAUDE.md, "Owner gates". Current:
   > Every review cut is a DRAFT render at 98 % production quality

   Proposed (append after that sentence):
   > A preview is not a review cut: post it as "preview <window>", never in place of the draft.

6. `.gitignore`: add `_preview_tmp.html*` beside `_blank_tmp.html*`.
