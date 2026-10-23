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
4. Root: `data-duration = t1 - t0`; at 360, `data-width=640 data-height=360`, and the root's children are wrapped
   in one fixed stage div, `<div id="hf-preview-stage" style="position:absolute; left:0; top:0; width:1920px;
   height:1080px; transform:scale(0.333333); transform-origin:0 0">`. A wrapper, not a transform on each child,
   because GSAP writes inline transforms on clips (El Reno's `kb()` Ken Burns moves) and would undo a per-child scale.
   `html { zoom }` was tried and draws only the top-left 213x120 px (z9, z11).
5. Inject one fixed script first in `<head>`: a `Proxy` on `window.__timelines` that wraps only the root id as
   `outer.add(tl.tweenFromTo(T0, T1, {ease: "none"}), 0)`. Sub-composition timelines pass through: their hosts were
   shifted in step 3.

Why the shim and the attribute shift are both needed: the page clock comes from the timeline, the sound and video from
the attributes. Either alone puts picture and sound at different times.

Content-blind by construction: the plan reads tag, id, time attributes, whether `data-composition-src` is present,
and byte spans. It never reads text, classes, styles, `src` or script bodies, and writes only time attributes, whole
element drops, root size and duration, the stage wrapper and the fixed script. `assert_content_blind` (reverse
the plan, require the original bytes) and `assert_identity` (window `all` at 1080 changes only the injected script) run on every call.
Validation sits at the boundary: a non-numeric time, a host without `data-duration`, a time attribute the plan does
not model, or a second root is a refusal naming the element, never a guess.

Interface depth: one command and two env knobs in render.cmd's existing style (`RENDER_WINDOW`, `RENDER_HEIGHT`)
hide snapping, dropping, trimming, the shim and the self-checks.

## The one safety fact

A preview is only safe if frame n of the window equals frame n + t0*fps of the whole render. The prototype checks
exactly that on demo-pin (WebGL comp, burned-timecode video, audio) with SSIM, at 1080 and at 360 against a
downscaled whole render (table below, rows w1-w5). The same check belongs in `pin_ritual.py`, so a hyperframes bump
that breaks the shim fails the ritual, never a preview.

## Synthesis decision

Two structurally different candidates were drawn (architect arena, two Opus runners, one Sonnet cross-judge):
- A, no derived HTML: segmented capture with black placeholder segments seeded outside the wanted act, so `--resume`
  (which checks only hash, byte size and frame count) skips them; ffmpeg downscale to 360p after.
- B, a content-blind derive of a gitignored window page at a 640x360 viewport.

Base: B. The judge scored B higher on the owner's asks (window cuts audio, capture and assemble; 360p cuts capture,
which A cannot) and on interface depth, A higher on rule fit and correctness risk. The prototype then checked B's
open risks frame by frame (table below). A's core trick depends on two undocumented internals (the resume validation
rule and a temp `audio.m4a`), pays the whole-episode audio mix twice per act, and captures at 1080.
Grafted from A: the preflight split (preview keeps busy, pin and media budget, skips the LAYERS table) and the
pin-ritual re-check of every renderer behaviour the design leans on. Changed from B after measuring it:
`html { zoom }` drew a clipped picture, so the 360 viewport is a stage wrapper div (Shape step 4). Rejected from A:
placeholder seeding (fooling the renderer's resume check is a mask, not a path), the probe-and-kill launch, the
progressive per-act watcher.

## Measured prototype (23 Oct 26)

demo-pin copy (MG with CSS 3D + three.js WebGL comp + video + audio), cut to 8 s unless noted. 1 worker (2 workers
needs 2.9 GB by `render_busy.need_gb`, over the 2 GB run budget), `--quality draft --crf 32 --gpu --browser-gpu
--experimental-fast-capture=true` as render.cmd; the comp's CSS 3D turns fast capture off, so every run used
screenshot capture. Render s = the renderer's own "rendered in"; capture s = its capture stage. RAM = private bytes
of the render tree plus headless Chrome. Scratch harness, not committed. ZBook runs used the signed Chrome
(`HYPERFRAMES_BROWSER_PATH`, Smart App Control) through a hidden once-only task.

| Run | Box | Setup | Render s | Result |
|---|---|---|---|---|
| r1 | ASUS | 24 s, seg, 60-frame segments, 15 fps | 82.5 (killed) | free RAM 3.32 to 1.28 GB with other sessions' gates live; killed at frame 177/360 |
| r3 | ASUS | 8 s, seg cold, 8 fps | 64.6 | compile 3.9, audio 2.7, capture 24.9, assemble 6.3; 3 segments (HF_SEGMENT_FRAMES=16 clamps to the 30 minimum); peak 1.39 GB |
| r2, r4 | ASUS | seg runs | killed at 5-32 s | box under the 0.9 GB free floor (other sessions); moved to the ZBook |
| z1 | ZBook | 8 s, seg cold, 8 fps | 39.2 | capture 32.4; node lingered to the 180 s cap after "Render complete" |
| z2 | ZBook | z1's comp unchanged, --resume | 5.5 | "resuming: 3 segments complete", 3 skipped, capture 0.9 |
| z3 | ZBook | one-line `index.html` edit (root background), --resume | 33.2 | 0 skipped, capture 28.8: full recapture |
| z4 | ZBook | then one-line edit in `compositions/g-tanker-throw.html`, --resume | 28.1 | 0 skipped, capture 22.2: full recapture |
| z5 | ZBook | 1080, 15 fps | 30.6 | capture 26.2; peak 1.41 GB |
| z6 | ZBook | 1080, 8 fps | 20.3 | capture 15.9; peak 1.35 GB |
| z7 | ZBook | 1080, 8 fps, --low-memory-mode | 21.2 | capture 16.3: no gain over z6 |
| z8 | ZBook | 640x360 root + `transform: scale(1/3)` on hosts, 8 fps | 16.1 | capture 11.7; frame correct (looked at it); peak 1.06 GB |
| z9 | ZBook | 640x360 root + `html { zoom: 1/3 }` only, 8 fps | 15.9 | capture 10.8; frame WRONG: only the top-left 213x120 px drawn, rest black (root clipped at its 640x360 CSS size) |
| z10 | ZBook | 640x360 zoom, 15 fps | 19.1 | capture 15.2; peak 0.98 GB |
| z11 | ZBook | 640x360 zoom + `[data-composition-id]{width:1920px!important;height:1080px!important}`, 8 fps | 15.4 | capture 10.7; same broken picture as z9 |
| z2b | ZBook | proto-b unchanged after z4, --resume | 12.1 (harness wall) | 3 of 3 segments skipped |
| w1 | ZBook | 24 s whole render, 8 fps (reference) | n/a | capture 39.1 for 192 frames |
| w2 | ZBook | hand-derived window [14, 20] at 1080: dropped tanker host + tone, shifted host and video, shim | 26.2 | capture 12.7 for 48 frames; SSIM vs whole-render frames +112: 0.960 / 0.948 / 0.945 (frames 8/24/40). Frame 24 looked at side by side: same "FRAME 090" WebGL barcode, same video timecode 00:00:02.000, same layout; the gap is crf 32 noise |
| w3, w4 | ZBook | same window at 640x360 with `html { zoom }`, without and with B's root-size override | 20.9, 21.2 | SSIM 0.13-0.16 vs downscaled whole render: the zoom shape is broken |
| w5 | ZBook | same window at 640x360 with the stage wrapper (Shape step 4) | 22.2 | capture 11.6 for 48 frames; SSIM vs downscaled whole render 0.891 / 0.847 / 0.867. Frame 24 looked at side by side: same FRAME 090, same layout and timing; the gap is native 360 drawing vs ffmpeg downscale plus crf 32 at 360. Correct picture. This window is all WebGL, which still draws at 1920x1080 inside the stage: capture 11.6 s vs 12.7 s at 1080 (w2), rho 0.91 |

Two-point fit on the capture stage (120 frames at 15 fps, 64 at 8 fps): 1080 costs 0.184 s per frame (z5, z6), 360
costs 0.079 s per frame (z9, z10; z9's picture was wrong but the pixel count captured is the 360 one, and z8, which
was right, captured in 11.7 s against z9's 10.8). So **rho = 0.43** for SVG/DOM motion graphics: a 360p frame costs well under half a 1080p
frame. A WebGL window gains almost nothing (w5 vs w2: rho 0.91); El Reno has 8 WebGL comps of 69.
`--low-memory-mode` buys nothing. Segment reuse works only for an untouched composition (z2: 5.5 s against 33.2 s);
one edited line anywhere, root or sub-composition, recaptures everything (z3, z4). Segmenting itself cost time on
this short comp (z1 capture 32.4 s against 15.9 s plain at the same fps).

### First-look estimate

`T(W) = 20 + W * (0.191 + 0.212 + 1.133 * (fps / 15) * rho)` seconds, from El Reno's ZBook draft per composition
second (audio 0.191, assemble 0.212, capture 1.133) and rho = 0.43. Audio and assemble scale with W because
out-of-window media are dropped; neither is assumed to get cheaper at 360.

| Window W | Today (draft, 1080, 15 fps) | Preview 360p, 15 fps | Preview 360p, 8 fps |
|---|---|---|---|
| 60 s iteration | 1.9 min (not possible today) | 1.2 min | 1.0 min |
| 270 s act | 7.2 min (not possible today) | 4.3 min | 3.3 min |
| 1333 s whole | 34.5 min | 20.0 min | 15.0 min |

Assumptions to recheck on the first real preview: rho came from a 1-worker 8 s MG comp on the screenshot route;
El Reno is video-heavy, renders at 3 workers, and may take the fast-capture route. WebGL stretches sit near rho 0.9,
so a WebGL-heavy act lands between the 360p and today columns. The window alone (rho 1) still turns a 270 s act into
7.2 min against 34.5 min for the whole draft.

## What is impossible, and the line that says so

- A capture smaller than the composition through the CLI: `resolveDeviceScaleFactor` returns 1 with no
  `--resolution`, else `Math.max(target.width / compositionWidth, target.height / compositionHeight)`
  (chunk-IVEFOUZI.js), and the presets are landscape 1920x1080 and up, "the scale must be an integer multiple".
  So 360p needs a 640x360 root (the derive's stage wrapper), not a flag.
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
- We accept that a WebGL canvas still draws at its own 1920x1080 inside the scaled stage; only the captured pixels
  shrink, so WebGL-heavy windows gain less than rho says.

## Alternatives considered

- Segment seeding (candidate A). Lost: relies on fooling `validateCompletedSegments`, pays the audio mix twice per
  act, and capture stays 1080 (360p is a file-size change only).
- Whole episode at 360p with no window. Kept as `RENDER_WINDOW=all`; alone it still waits for the last act's media.
- Segmented capture with `--resume` for iteration. Lost: zero reuse after any edit (source + z3/z4).
- Split acts into separate compositions. Lost: an authoring change to every episode, and the tripwire forbids a script doing it.
- `html { zoom: 1/3 }` (candidate B's choice). Lost: measured broken, with or without a root-size override (z9, z11, w3, w4).
- `transform: scale()` on each root child. Lost: GSAP's inline transforms on clips would overwrite it.

## Open questions and risks

- Does `render -c _preview_tmp.html` also discover `index.html` and mix its audio? If so, stage under `.preview/`
  with `<base href="../">` as `stage_comp.mjs` does. Untested: the prototype rendered each window page as the
  `index.html` of its own copy, never through `-c`.
- `filmLayer(tl, DUR)` and any `onUpdate` on the root timeline run under `tweenFromTo`; the grain must be checked on the first real preview.
- On the ZBook, node stayed alive more than 140 s after "Render complete" in z1 and z3, the two runs the harness let
  wait (later runs were cut 5 s after the line). If that holds for render.cmd, its done marker lands minutes late.
  Not checked on a real render.
- ZBook ssh answered "Connection reset" 12:47 to 12:54 and around 13:10, both while prototype renders ran in the
  logged-on session. At 12:58 no render or headless Chrome process was left. The repo note blames frozen headless
  Chrome in session 0; that was not what happened here, cause unknown.

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
