# Move library
Seeded, seek-safe GSAP building blocks lifted from the showcase MG `g-tanker-throw` (demo-mg-showcase). Each move is `move(tl, targets, at, opts)`, adds literal tweens to one paused timeline, and routes per-frame work through `onFrame` (one onUpdate). Copy `moves.js` inline into the composition (library convention, like `snippets/helpers.js`); the host loads gsap + `vendor/` DrawSVGPlugin, CustomEase, SplitText. Worked example: `demo.html` (10 s roof panel, illustrative numbers).

| Move | What it does |
|---|---|
| `cameraRig` / `camMove` / `shake` | world camera proxy over depth layers (bg 0.4, world 1, fg 1.4) with handheld drift; push-in/pull-back; seeded decaying shake |
| `arcThrow` (+ `arcPath`) | body on a true parabola: anticipation squash, tumble, landing squash + spring, speed-driven blur, ghosts, clipped trail |
| `counter` | HUD number driven by a proxy (e.g. `arcThrow().fly.u`), exact final text, landing punch |
| `slamFig` | red popfig slam in, hold, slide out |
| `dustPuff` / `debrisBurst` / `impactRing` | seeded landing dust, ballistic chips, expanding ground ring |
| `rain` / `lightning` | seeded wrapping streaks; flicker-and-decay sky flash behind the world |
| `measureDraw` / `bandCompare` | DrawSVG ruler, ticks, brackets + labels; equal 1x/2x/3x bands laid end to end |
| `kineticText` | SplitText word stagger; throws unless the words settle `minHold` s before `exitAt` |
| `finishLayer` | seeded grain tiles, vignette, depth-of-field blur per layer |
| `cleanExit` | HUD slides up and out (autoAlpha 0), optional camera push, fade to black |
| `rng` / `onFrame` / `renderNow` | mulberry32; the one onUpdate hub; force-render the build frame (fixes frame 0) |

```js
const tl = gsap.timeline({ paused: true });
tl.to({}, { duration: 10 }, 0);                       // literal clock; see Gates
const rig = M.cameraRig(tl, { shake: $('rig'), layers: [[$('w-bg'), 0.4], [$('w-world'), 1]] }, { z: 1.8 });
const A = { x0: 470, y0: 567, x1: 1724, y1: 792, apex: 220, duration: 1.6, ox: 60, oy: 8 };
const th = M.arcThrow(tl, { pos: $('b-pos'), rot: $('b-rot'), sq: $('b-sq') }, 3.1, A);
M.camMove(tl, rig, 3.0, { fx: 1010, fy: 560, z: 1 });
M.counter(tl, $('cnt'), 3.15, { driver: th.fly, to: 114, format: (v) => Math.floor(v) + ' ft', punchAt: th.land, rig });
M.shake(tl, rig, th.land, { amp: 22 });
M.renderNow(tl);
window.__timelines['my-comp'] = tl;
```

## Text vs motion rules the moves enforce
- Text lives on the HUD, outside `rig.shake`; `counter`, `slamFig`, `kineticText` throw when passed `rig` and the text sits inside it.
- World labels (ruler, bracket) reveal only after the last shake ends; flashes sit behind the world; grain and vignette sit below the HUD.
- Keep the flight arc under the counter and payoff bands: check the apex screen y at the camera zoom during flight, not only at rest.

## Gates
- `beat_density.py` counts only literal `tl.<call>(..., <number>)` in the composition source; beats inside moves are invisible to it. A literal whole-window clock passes the gate, so mount it only when a continuous move (drift, rain, grain) really runs. Root fix: count beats from the built timeline, not a regex.
- Drive with `tl.time()` / `tl.progress()`; `tl.seek()` suppresses onUpdate by default.
