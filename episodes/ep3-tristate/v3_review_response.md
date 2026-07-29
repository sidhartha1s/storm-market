# ep3 v3 — response to the 2/10 review

Every claim below was verified against the code or a measured artifact. Where something is
not fixed, it says so.

---

## 1. The eleven defects you named

| # | Your note | Disposition | Evidence |
|---|---|---|---|
| 1 | "Rain and Strong shifting winds. That's five words, not seven" | **Fixed** | `g-forecast.html`: `PH = "rains and strong shifting winds"`, stamp reads FIVE / WORDS, five bars in the row. |
| 2 | 3:48 "warm gulf air garbled… make those lines wavy and in-motion to show air. no motion in your motion graphics" | **Fixed** | `g-metmap`: four warm ribbons draw then advect 19.6s, three cold ribbons 29.5s, jet stream 33.1s, dew-point readout reads "FLOWING NE". 70 timed events over a 36.1s window. |
| 3 | 4:35 "'what they knew' is quite ambiguous… what the hell is that cone? a tornado? yeah no shit" | **Fixed** | `g-scale` now reads WHAT THEY EXPECTED → "ROPE FUNNEL / ~100 FT WIDE" against WHAT ARRIVED → "A WALL OF DEBRIS", headline "NOT A FUNNEL. A WALL." |
| 4 | 5:16 "wont a map show it better than the fucking mountain broll?" | **Fixed** | New `g-lone` composition — see §2. |
| 5 | 5:48 "you are making the viewer 'look at stuff' while you were supposed to 'show'" | **Fixed — same defect as #4** | Mapped against the v2 build: 5:16 and 5:48 both sit inside ONE 33.4s stock cloud clip (`stock-cloudsrolling-03.mp4`, 323.50s +33.40s) covering the whole "not a squall line / one lone supercell / 400 miles / seven hours" passage. `g-lone` replaces that clip. |
| 6 | 6:35 "a fucking minute long… NO FUCKING FRAME CHANGE" | **Fixed** | `g-track-1`: 10 timed events, largest motionless interval **0.91s** across a 24.8s window. |
| 7 | 14:16 "text is garbled again. murphysboro" | **Fixed at the root** | Cause was tweening reflow properties (`letterSpacing`, `width`) which snap per frame under fast-capture. Zero `letterSpacing` / `width` / `textIndent` tweens remain anywhere in the repo; all converted to `scaleX`/`scaleY` with an explicit `transformOrigin`. |
| 8 | 17:52 "why is a white dot running ahead here? remove that" | **Fixed** | `g-baro`: the pen is no longer keyframed. It reads the trace's own `strokeDashoffset` each frame and is placed with `getPointAtLength`, so its position is `min(tot, DASH - offset)` — identical to the drawn length. It cannot lead the line. |
| 9 | "your town line graph and death poll counter don't have all town names… the later it gets, the more towns you are missing" | **Fixed** | All seven map instances render all twelve towns with hand-placed collision-free label anchors; all nine narrated towns appear in every map. Labels are appended to the SVG **after** the storm marker — paint order is document order, and with the marker last it slid over "De Soto" and ate the word. |
| 10 | 20:55 "another 2 hour long fucking segment" | **Fixed** | `g-track-7`: 87 timed events, largest motionless interval **1.55s** across 30.8s. |
| 11 | 28:04 "image crop is shit" | **Fixed** | v2 ran `fujita-portrait-01.jpg` (1500×1660, aspect 0.904) full-frame for **163.5 seconds**, stretched into 16:9. It now sits inside `g-fujita` in a bordered 520×600 frame with `object-fit: contain`. Separately, four stills at 1.58–1.75 aspect were being pillarboxed for no reason and now fill the frame. |

**On #5 and #11:** you were right that mapping your v2 timestamps onto v3 was my job, not
yours. The v2 draft was built from a commit still in the tree, so `git show
<sha>:episodes/ep3-tristate/index.html` plus the window ledger answers it exactly. Both are
resolved above from that mapping, not from guesswork.

---

## 2. The 5:16 map (`g-lone`)

The narration makes a spatial argument, so it gets a map:

- A squall line of nine cells builds across the three states, labelled "A SQUALL LINE · MANY STORMS".
- On the spoken word **"squall"** (8.66s) a strike line draws through them; the whole group dies.
- **"one lone supercell"** (10.22s) — a single cell remains, labelled ONE CELL.
- It then crosses Missouri → Illinois → Indiana on the same geometry the track maps use, for
  the rest of the window, while two counters run to **412 MI** and **7.0 HR**, started on the
  spoken "400 miles" (12.64s) and "seven hours" (14.78s).

37 timed events, no motionless stretch. Snapshotted and inspected at six points before
rendering; three defects found and fixed at that stage (a stray dash from a mis-set dash
length, a label that outlived the elements it described, and the route marker landing on top
of its own caption).

---

## 3. What I found that you did not have to

- **63 pure-black frames.** The scheduler advanced by `seg_dur + 0.75` but only ever covered
  `seg_dur` with picture windows, so the breath between narration segments had nothing on the
  picture tracks. `ffmpeg blackdetect` on the draft: **81 black spans, 63 at segment
  boundaries.** Four sampled frames were pure black. ep2, the shipped reference, has 2 such
  gaps; ep1 has 6. Now **0**.
- **15.9 seconds of black at the end** — a redundant `+14s` credits tail after `g-close` had
  already faded out. My first attempt extended `g-close` to cover it, which just *held* the
  black. Replaced with the real fix.
- **A 0.75s hole inside `g-close`** between the last closing line and the title card, found by
  the pre-render blank scan.
- **The render crash** (run 6): one 365 MB 3840×2160 stock clip feeding 12.9s of a 1080p comp,
  10× every other asset, blew the `video_extract` ffprobe deadline. Transcoded to 1080p,
  365 → 54 MB. Retrying would have hit it again.

---

## 4. Clip lengths

Full ledger with every window's start, length, track and source: **`clip_ledger_v3.md`**.

| | v3 | ep2 (shipped) |
|---|---|---|
| picture windows | 266 | 187 |
| median length | 7.00s | 10.00s |
| mean length | 9.55s | 13.31s |
| longest window | 44.8s (`g-fujita`) | 82.7s |
| uncovered picture gaps | 0 | 2 |

34 windows run 15s or longer; all are graphics, and none has a motionless stretch over 1.6s.

---

## 5. Still open — no asset exists

1. **No verified John Park Finley portrait.** That window carries his documents. I will not
   generate a likeness of a real named person and run it under his name.
2. **No 2025 centennial footage** for `a6-s3b`.
3. **`a6-s4` narrates "the faces in these photographs"** and there are no usable faces in the
   pool. Generating AI faces there would imply they are the 1925 archive — the closest this
   episode could come to a fabricated witness. Recommend rewriting the beat or sourcing real
   archival portraits.
4. **Residual match-cut softness in acts 4–6** — individual shots that do not contradict the
   narration but do not reinforce it either.

---

## 6. Gates, promoted out of scratch

Every check invented reactively during this round now runs in seconds:

| script | what it catches |
|---|---|
| `scripts/sweep_episode.py` | picture coverage (black), track overlap, adjacent duplicate cuts, reuse ceiling, missing media, unmounted/missing compositions, graphic window vs its own timeline, over-long stills |
| `scripts/blank_scan.mjs` | seeks every composition at 0.25s and measures on-screen ink — a pre-render blackdetect |
| `scripts/beat_density.py` | largest motionless interval per composition |
| `scripts/clip_report.py` | the full window ledger |

The lesson, in one line: **exhaust the static gates, then render once.** A render is the last
step, not a diagnostic tool.
