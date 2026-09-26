# WebGL tornado template (`tornado.html`)
Stylised funnel + wall cloud + debris + dust skirt + storm sky, ~32k triangles, seeded, driven only by the paused GSAP timeline. No text: labels go on a fixed HUD comp above it.

**Mount in an episode**
1. Copy `tornado.html` to `episodes/<slug>/compositions/tornado-<name>.html` and `vendor/three.classic.js` to `episodes/<slug>/vendor/` (paths are root-relative; `gsap.min.js` must load in index.html).
2. Rename the id in the copy: `sed -i 's/g-tornado/g-tornado-<name>/g' tornado-<name>.html` (root `data-composition-id` + `CONFIG.id`).
3. Host tag: `<div id="host-tornado-<name>" data-composition-id="g-tornado-<name>" data-composition-src="compositions/tornado-<name>.html" data-start="6" data-duration="6" data-track-index="1" data-width="1920" data-height="1080"></div>`. Keep `data-duration` = root `data-duration` = `CONFIG.duration`.
4. One copy per look; two mounts of the same copy would share element ids and a timeline key.

**CONFIG fields** (top of the script, the only block to edit)
- `scheme`: `day` (grey) | `night` (blue) | `dusk` (amber). `seed`: noise + debris layout.
- `funnelWidth` top radius (base ~20 %), `height` cloud base, world units. `rotationSpeed` rad/s at the base.
- `path.startX` / `path.endX`: base x at t=0 and t=duration (linear; frame spans about -45..45 at the default camera).
- `debrisDensity`: 0 none, 1 = 900 chunks. `duration` s. `cameraMove`: `static` | `slow-push` | `orbit`.

**Presets** (worked copies in `episodes/demo-webgl-tornado/compositions/`)
- Night approach: `{ scheme: "night", cameraMove: "orbit", duration: 6, path: { startX: -12, endX: -3 }, seed: 1974 }`
- Dusk push: `{ scheme: "dusk", cameraMove: "slow-push", duration: 6, path: { startX: -2, endX: 8 }, seed: 2011 }` (raise `funnelWidth` to ~9 for a wedge; untested)

**Limits**: one funnel per copy; no lightning, rain or damage path; debris is points (pixel-sized chunks); frames checked with `hyperframes snapshot`, not yet rendered.
