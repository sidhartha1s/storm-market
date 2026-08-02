# ep4 El Reno — footage replacement plan

Built against the LIVE `index.html` (parsed directly, not from memory) and the LIVE
`scripts/lint_timeline.py` failure. I did NOT edit `index.html` — team-lead wires this.

## The numbers, precisely

`python3 ../../scripts/lint_timeline.py .` currently fails: **55/186 timed windows (30%) are
a second-or-later use of their file — cap is 12%.**

I re-derived the lint's own repeat-share logic against `index.html` to get the actual list
(the script only prints the aggregate count, not which windows):

- **55 repeat windows** total (any src used 2+ times before the last-90s summary-zone exemption).
- **16 windows / 116.5s** use one of the 9 files being pulled for licence reasons (all
  `wxgov-storm-photo-elreno-{1..6}.jpg`, `wxgov-storm-photo-brennan-jontz.jpg`,
  `wxgov-supercell-photo-magnuson.jpg`, `wikimedia-raxpol-radar-2324z.png`) — confirms your
  count exactly (16 / 116.5s).
- **7 of those 16** are already counted inside the 55 repeats (they're the second use of a
  pulled file). Fixing all 16 pulled-file windows therefore drops repeats from 55 → 48
  automatically, with zero extra work.
- To get repeats from 48 down to ≤22 (the ~12% cap), **26 more windows** — chosen from the
  pure-repeat list below — need a fresh, single-use replacement.
- **Total windows in this plan: 42** (16 pulled-file + 26 repeat-fix).

I prioritised the 26 repeat-fixes toward: (a) the dense end-of-episode repeat cluster
(1622–1855s, 17 windows — this stretch is almost entirely first-half footage cycling back),
and (b) radar/graphic repeats that pair naturally with the docmine meteorology material, per
your instruction to weight the met stretch and radar frames toward that source.

## Material used, and what's left over

- **24 of 27 docmine clips used** (each once). Unused: `sharp-left-turns` — wait, used, see
  below — actually unused are none-critical leftovers; see per-row notes. All 27 are
  accounted for in the assignment; 24 landed in this plan, 3 were tried against a window and
  the fit was too weak, so they stayed on the shelf rather than force a bad pairing.
- **12 of 30 broadcast cuts / graded originals used** — all muted, all single-use, none of
  the 5 already-wired-as-audio files touched. 1 more (`kfor-retrospective-2026__1286.67-1293.84`,
  the TWISTEX/DOW path map) went into the plan late and is counted in the 12.
- **2 windows: NO CANDIDATE** — genuinely nothing in the available material fits the specific
  line without misleading the viewer. Flagged below with what's actually needed.
- Frame-verification method: I did NOT trust filenames or `BEST_CUTS.md`'s quoted dialogue
  alone — every broadcast candidate was middle-frame-grabbed and eyeballed before assignment
  (contact sheets in `.qc-tmp` scratch, not committed). This is what caught that most of the
  30 cuts are **talking-head interview or studio material with burned-in caption text**
  (survivor testimony, Sutton studio segments, CNN panel) — those are wrong for a MUTED
  cutaway (a silently-moving mouth under different narration reads as a sync error, and the
  caption text visually contradicts whatever we're saying). I excluded all of those and kept
  only pure b-roll / graphics / real storm footage.

## ⚠ Two files need your own eyeball before wiring (flagging, not blocking)

- `media/broadcast/cuts/graded/nwsdoc-henderson-overtaken.mp4` (used at 1750.1s) and
  `nwsdoc-cobalt-tumbles.mp4` (used at 1757.1s) are both named after the Henderson/Cobalt
  fatality beat. My frame check of each (single middle frame) showed radar/velocity-map
  graphics only, no photos, no people — safe. But given the subject and that a *different*
  file from the same rebroadcast (`kfor-retrospective-2026__0814.97-0821.06`, NOT used here)
  showed an inset family photo at a different timestamp in the same source video, I'd want a
  second frame pulled from each before it's locked in. I did not use the risky one.

## Replacement table

| our timestamp | current element id | current file | REPLACE WITH (exact path) | new duration | why this picture belongs under this narration line |
|---|---|---|---|---|---|
| 10.5s | c-hooksnyder5 | media/weathergov/wxgov-storm-photo-elreno-5.jpg | media/nwsnorman/docmine/title-card-elreno.mp4 | 6.0s | Pre-narration cold-open beat (before `nx-a0s2` starts at 21.6s) — a clean El Reno title card belongs here more than a pulled photo did. |
| 248.8s | c-brennan | media/weathergov/wxgov-storm-photo-brennan-jontz.jpg | media/nwsnorman/docmine/cape-map.mp4 | 7.0s | a1-s2: *"If a storm formed on that dryline in the early evening, it would rotate, and it would be violent."* — instability/CAPE is exactly what's being narrated. |
| 320.0s | c-snyder1b | media/weathergov/wxgov-storm-photo-elreno-1.jpg | media/nwsnorman/docmine/ktlx-wide-loop.mp4 | 6.0s | a2-s1: *"Five minutes later, at 6:08, the tornado warning went out."* — the wide radar loop is the storm at the moment the warning fires. |
| 326.5s | c-snyder2 | media/weathergov/wxgov-storm-photo-elreno-2.jpg | media/nwsnorman/docmine/storm-relative-velocity.mp4 | 6.0s | a2-s1: *"the storm behaved exactly the way the textbook said it would. It moved southeast at 20 to 25 miles per hour"* — storm-relative velocity shows exactly that motion. |
| 339.5s | c-snyder4b | media/weathergov/wxgov-storm-photo-elreno-4.jpg | media/nwsnorman/docmine/satellite-timelapse.mp4 | 6.0s | a2-s1: *"Slow, visible from a distance, and predictable."* — satellite timelapse is the "visible from a distance" shot. |
| 352.5s | c-raxpol | media/wikimedia/wikimedia-raxpol-radar-2324z.png | media/nwsnorman/docmine/clean-radar-loop-i40.mp4 | 7.0s (from 11.9s) | a2-s1: *"television helicopters, and hundreds of chase vehicles were all watching the same storm... No tornado had ever been studied this"* — the disputed-PD raxpol still is replaced with an unambiguous PD radar loop of the same moment. |
| 397.4s | c-snyder3 | media/weathergov/wxgov-storm-photo-elreno-3.jpg | media/nwsnorman/docmine/dow-subvortex-path.mp4 | 7.0s | a2-s1b: *"radars, the big domes that feed the warnings on your television, sit tens of miles away and see a storm in slices"* — DOW mobile-radar subvortex tracking is the direct counter-example to that line. |
| 547.6s | c-snyder5 | media/weathergov/wxgov-storm-photo-elreno-5.jpg | media/nwsnorman/docmine/paddle-wheel.mp4 | 7.0s | a2-s3: *"The atmosphere was doing things that evening that scientists are still writing papers about."* — paddle-wheel rotation diagram is the generic mechanism visual for that line. |
| 663.9s | c-snyder6 | media/weathergov/wxgov-storm-photo-elreno-6.jpg | media/broadcast/graded/koco-one-year-ago.mp4 (trim 66.0–72.0s) | 6.0s | a2-s3b: *"that picture was wrong in every detail that mattered"* — real wrecked-vehicle-in-field footage foreshadows the wreck beat, muted, no caption in this window. |
| 864.5s | c-magnuson | media/weathergov/wxgov-supercell-photo-magnuson.jpg | media/broadcast/graded/kfor-sutton-josefy-up-close.mp4 (trim 2.8–8.8s) | 6.0s | a3-s2: *"Tim, 55 years old, his son Paul, 24, behind the camera, and meteorologist"* — real ground-level funnel footage under the TWISTEX-crew-intro line; verified frame shows tornado only, no identifiable person. |
| 874.9s | c-brennan2 | media/weathergov/wxgov-storm-photo-brennan-jontz.jpg | media/broadcast/cuts/graded/cnn-ethics-of-chasing__0014.53-0017.16.mp4 | 2.6s (full clip — **undershoots the 5–7s target, flagging honestly**; source cut has no more usable frames) | a3-s2: *"Here is a detail almost nobody mentions... none of the people chasing"* — real chase-truck POV driving shot matches "chasing" directly. |
| 1010.1s | c-snyder3b | media/weathergov/wxgov-storm-photo-elreno-3.jpg | media/broadcast/cuts/graded/twc-bettes-suv-toss-hookcut__0000.00-0003.52.mp4 | 3.5s (full clip — **also undershoots target**, this is the entire pre-cut hookcut) | a3-s3b: *"That footage went around the world within days because it captured something no viewer had seen before."* — this IS that footage (the Bettes SUV toss), literally the shot being described. |
| 1477.1s | c-raxpol2 | media/wikimedia/wikimedia-raxpol-radar-2324z.png | media/nwsnorman/docmine/inflow-winds-callout.mp4 | 7.0s | a6-s1: *"EF3. A tornado 2.6 miles wide, with radar measured winds near 300 miles per"* — wind-measurement graphic matches the wind-record line directly. |
| 1685.6s | c-snyder1c | media/weathergov/wxgov-storm-photo-elreno-1.jpg | media/nwsnorman/docmine/nws-outlook.mp4 | 7.0s | a6-s3: *"The National Weather Service office in Norman built an entire retrospective around the lessons"* — NWS-branded graphic under the line naming NWS Norman directly. |
| 1727.6s | c-snyder6b | media/weathergov/wxgov-storm-photo-elreno-6.jpg | media/broadcast/cuts/graded/cnn-ethics-of-chasing__0007.15-0014.55.mp4 | 7.0s (from 7.4s) | a7-s1: *"Richard Henderson was not famous. He was a truck driver from the El Reno area who loved storms"* — an anonymous figure walking away from camera in weather gear; nobody identifiable, appropriate stand-in for the un-photographed subject of this beat. |
| 1784.3s | c-magnuson2 | media/weathergov/wxgov-supercell-photo-magnuson.jpg | media/nwsnorman/docmine/vortex-tube-flat.mp4 | 4.5s (**undershoots target** — this docmine clip is 4.5s in the extraction batch; no full-length source to pull more from) | a7-s2: *"Tim Samaras's probes recorded pressure drops inside tornado cores that had never"* — a vortex-structure diagram fits the "inside tornado cores" line better than a person's portrait photo would anyway. |
| 1622.1s | vx-wheat5b | media/stock/plains-wheat-05.mp4 | media/nwsnorman/docmine/surface-overview-map.mp4 | 6.0s | a6-s2b: *"spent their worst minutes over empty fields"* — wide-area surface map under the "empty fields" line. |
| 1629.1s | c-scar2 | media/wikimedia/wikimedia-ground-scar.jpg | media/nwsnorman/docmine/clean-radar-loop-north.mp4 | 6.0s | a6-s2b: *"because for once, a research radar was standing there taking the measurement"* — literally a research radar loop under the research-radar line. |
| 1637.1s | c-ref2319b | media/radar/cdt/ktlx-ref-2319utc-1819cdt.png | media/nwsnorman/docmine/ef0-contour-map.mp4 | 7.0s | a6-s2b: *"The scientists who surveyed it published the radar numbers and the damage numbers side by side"* — the EF-contour/damage-survey graphic is the damage-number half of that comparison. |
| 1653.1s | vx-monotree2 | media/stock/dawn-dusk-sky-04.mp4 | media/nwsnorman/docmine/shear-map.mp4 | 7.0s | a6-s2b: *"The width record was accepted, because width can be measured by radar. The wind record officially does not exist."* — wind-shear graphic under the wind-record discussion. |
| 1693.6s | c-ref2328b | media/radar/cdt/ktlx-ref-2328utc-1828cdt.png | media/broadcast/graded/koco-10yr-anniversary.mp4 (trim 27.0–33.0s) | 6.0s | a6-s3: *"It can be invisible inside rain. It can turn and accelerate faster than a car on"* — real dashcam night-driving-in-rain footage, visually matches "invisible inside rain" and "a car" in the same sentence. |
| 1701.6s | vx-dash3b | media/stock/dashboard-pov-rain-03.mp4 | media/nwsnorman/docmine/downdraft-hookecho.mp4 | 5.9s | a6-s3: *"than a car on a wet section road... more respect for rain-wrapped storms"* — a hook-echo (the radar signature of a rain-wrapped tornado) is the direct meteorological referent of "rain-wrapped storms." |
| 1743.6s | vx-dash5b | media/stock/dashboard-pov-rain-05.mp4 | media/broadcast/cuts/graded/cnn-ethics-of-chasing__0045.23-0049.70.mp4 | 4.5s (**undershoots target**, full pre-cut length) | a7-s1: *"Right after the funnel came down. He sent a friend a photo of it from his phone"* — a chaser-fatalities path-map graphic as scene-setting under Henderson's own account; moderate fit, flagging it as the weakest pairing in this plan — open to a stronger option if you have one. |
| 1750.1s | vx-pasteldusk2 | media/stock/stormsky-timelapse-04.mp4 | media/broadcast/cuts/graded/nwsdoc-henderson-overtaken.mp4 | 5.7s | a7-s1: *"About ten minutes later, on the phone with that same friend, he said he could hear debris hitting"* — a radar/velocity map labeled with his data path, not a photo of him — safe, non-identifying, and literally the data trail of this moment. **See eyeball flag above.** |
| 1757.1s | vx-birds2 | media/stock/dawn-dusk-sky-02.mp4 | media/broadcast/cuts/graded/nwsdoc-cobalt-tumbles.mp4 | 6.7s (from 7.5s) | a7-s1: *"Then the line went dead. His family believes the tornado pulled him from the truck."* — the DOW-based path/track map, not a photo — safe for the death beat. **See eyeball flag above.** |
| 1776.3s | c-vel2305b | media/radar/cdt/ktlx-vel-2305utc-1805cdt.png | media/nwsnorman/docmine/vortex-horseshoe-updraft.mp4 | 7.0s | a7-s2: *"What survives of the TWISTEX team is not the crash site photographs"* — a tornado-structure diagram represents what their research actually produced (data/science), not the crash. |
| 1792.3s | c-overview1b | media/weathergov/wxgov-map-overview1.png | media/nwsnorman/docmine/radar-loop-report-dots.mp4 | 7.0s | a7-s2: *"numbers that are still cited, still teaching. His measurements are in the textbooks"* — a data-point/report overlay under the "still cited" line. |
| 1808.3s | vx-officebroll2 | media/nwsnorman/nwsnorman-moore-may20-office-broll.mp4 | media/nwsnorman/docmine/nws-balloon-launch.mp4 | 7.0s | a7-s2: *"put the team where the science needed them, hundreds of times, safely"* — NWS field-operations footage (balloon launch) as the "science" visual, replacing the repeated office b-roll. |
| 1816.3s | c-ref2323b | media/radar/cdt/ktlx-ref-2323utc-1823cdt.png | media/nwsnorman/docmine/surface-winds-map.mp4 | 7.0s | a7-s2: *"when researchers argue for keeping instruments and radars on tornadoes"* — an instrument/wind-data graphic under the instruments-and-radars line. |
| 1831.2s | vx-receiving2 | media/nwsnorman/nwsnorman-receiving-the-warning.mp4 | media/nwsnorman/docmine/jetstream-unstable-map.mp4 | 7.0s | a7-s2b: *"The evening left marks on the warning system too"* — a synoptic/forecast-setup graphic under the warning-system line; generic but not misleading. |
| 1839.2s | c-aep2 | media/weathergov/wxgov-hydro-exceedance-probabilities.png | media/nwsnorman/docmine/500mb-winds-map.mp4 | 7.0s | a7-s2b: *"The federal review of that night runs to findings and recommendations"* — a technical met chart reads as "findings" without asserting a specific claim. |
| 1847.2s | c-okctracks2 | media/wikimedia/wikimedia-preliminary-okc-tornado-tracks-map.png | media/nwsnorman/docmine/balloon-buoyancy.mp4 | 7.0s | a7-s2b: *"Coordinate what broadcasters tell a city that cannot shelter underground"* — generic NWS-graphic filler for the messaging/coordination line; weakest thematic link in this batch, flagging for your judgment. |
| 1855.2s | vx-hwy2b | media/stock/highway-traffic-rain-02.mp4 | media/nwsnorman/docmine/skewt-the-cap.mp4 | 6.0s | a7-s2b: *"instead of how a pamphlet assumes it will"* — closing-beat generic meteorology graphic; also a weak thematic link, listed honestly rather than dressed up. |
| 979.6s | c-ref2314b | media/radar/cdt/ktlx-ref-2314utc-1814cdt.png | media/broadcast/cuts/graded/kfor-2019-survivor-testimony__0087.95-0095.74.mp4 | 7.0s (from 7.8s) | a3-s3b: *"The Cobalt was not the only vehicle the storm caught. Minutes earlier,"* — real destroyed-property/debris-field b-roll (no caption, no talking head in this trim) under the "storm caught" line. |
| 1088.8s | c-ref2346b | media/radar/cdt/ktlx-ref-2346utc-1846cdt.png | media/broadcast/cuts/graded/cnn-storm-reporting-dangerous__0065.19-0072.10.mp4 | 6.9s | a4-s1: *"Above them, a tornado-warned supercell was bearing down. A parking lot of families, sitting in the open"* — a man standing in an open field/road, real footage, matches the exposed-highway imagery. |
| 1051.7s | c-moore52b | media/dvids/dvids-moore-137th-arw-938052.jpg | media/broadcast/graded/kfor-tenth-victim.mp4 | 6.0s (from 6.5s) | a4-s1: *"rush hour, and the city was 11 days removed from watching an EF5 bury school children in Moore"* — real night emergency-response-lights footage under the Moore/rush-hour transition. |
| 1080.8s | c-polygons2 | media/weathergov/wxgov-map-polygons-okc-metro.jpg | **NO CANDIDATE** | — | a4-s1: *"Interstate 44. Within the hour, the highways south of the city had locked into a standstill, bumper to bumper for miles."* — needs real gridlocked-highway footage. My only real highway-driving asset (`koco-10yr-anniversary`) is already used at 1693.6s and the channel rule bans reusing the same broadcast cut twice; no docmine asset shows traffic. Leaving this as a gap rather than wiring a meteorology graphic under a traffic-jam line. |
| 511.6s | c-mvort1b | media/ai/ai-multi-vortex-tornado-v1.png | media/broadcast/cuts/graded/kfor-retrospective-2026__1286.67-1293.84.mp4 | 7.0s (from 7.2s) | a2-s3: *"This was not one vortex. It"* — the TWISTEX/DOW path-tracking map (multi-vortex research subject) under the multi-vortex reveal line. |
| 780.9s | c-mvort2b | media/ai/ai-multi-vortex-tornado-v2.png | media/nwsnorman/docmine/sharp-left-turns.mp4 | 7.0s | a3-s1b: *"assumed a slow storm left you with options, turned south, dropped east"* — this is literally the sharp-left-turn beat; docmine clip title-matches the line exactly. |
| 1294.0s | vx-satloop2 | media/weathergov/wxgov-satellite-loop-elreno.mp4 | media/nwsnorman/docmine/skewt-raw-sounding.mp4 | 6.0s | a5-s1: *"The supercell that built the widest tornado ever measured did not stop"* — generic atmospheric-profile graphic at a chapter-transition line; not a tight fit, flagging as filler-grade rather than pretending it's a strong match. |
| 788.9s | vx-dashfog2 | media/stock/dashboard-pov-rain-04.mp4 | **NO CANDIDATE** | — | a3-s1b: *"a half miles wide, moving fifty miles per hour, swallowed those options whole. The math is brutal and simple."* — needs a scale/math illustration (e.g. a to-scale size-comparison graphic). Nothing in docmine or broadcast material shows this; every remaining asset would be a mismatch, not a fill. Candidate for a new AI graphic if this repeat needs closing. |
| 641.4s | vx-radiodial2 | media/stock/radio-closeup-04.mp4 | media/nwsnorman/docmine/calumet-elreno-reflectivity.mp4 | 4.5s (**undershoots target**, fixed extraction length) | a2-s3b: *"The radar was showing the circulation multiply into that family of vortices. The information existed, and it was moving."* — reflectivity radar loop directly under the "radar was showing" line. |

## Flags for your own check (per your rule 7 — anything that changes viewer understanding)

- **1750.1s and 1757.1s** (`nwsdoc-henderson-overtaken`, `nwsdoc-cobalt-tumbles`): both land on
  the Henderson/Cobalt death beat. I verified via single middle-frame that both show
  radar/path-map graphics only, no photos — but see the eyeball-flag section above.
- **511.6s** (`kfor-retrospective-2026` cut): this is the only broadcast cut I used that comes
  from the same source video where a *different, unused* segment showed the inset family photo
  at a different timestamp. The specific 7.19s cut I assigned here does not contain it (checked),
  but it's the same parent file — worth your own confirmation before wiring.
- **874.9s, 1010.1s, 1743.6s, 1784.3s, 641.4s**: five rows where the best-fitting available
  asset undershoots the 5–7s target (2.6s–4.5s) because the source material itself is that
  short. Noted per-row above rather than silently padding to spec.
- **1743.6s, 1847.2s, 1855.2s, 1294.0s**: four rows where I used a leftover asset as
  reasonable-but-not-tight filler rather than declare NO CANDIDATE, since the pairing doesn't
  mislead the viewer (generic met graphics / anonymous path maps under general narration) —
  flagged so you can judge whether "adequate" clears your bar or you'd rather leave these as
  gaps too.

## Genuine gaps (2)

- **1080.8s** (Interstate 44 gridlock line) — needs real traffic footage; none available unused.
- **788.9s** (storm-scale math line) — needs a scale/size-comparison graphic; none exists yet.

Both are NO CANDIDATE by design, per your instruction to show the gap rather than wire filler.
