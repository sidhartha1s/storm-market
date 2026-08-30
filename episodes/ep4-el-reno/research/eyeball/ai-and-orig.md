# media/ai/ + media/_orig/ eyeball index

## Task A — media/ai/ (10 files, all PNG stills — no video files present)

| File | Resolution | Provenance row? | Subject / mood | Anatomy/geometry/text QC | Real-person likeness? | Verdict |
|---|---|---|---|---|---|---|
| ai-multi-vortex-tornado-v1.png | 1920x1080 | **MISSING** | Wide-shot funnel over green farmland, dark wall cloud, rain curtain, farmhouse silhouettes. Menacing, matches doc tone. | No people/hands/faces to fail on. Cloud/funnel geometry coherent, no garbled text, no physics nonsense. | None | OK (provenance gap — CAUTION) |
| ai-multi-vortex-tornado-v2.png | 1920x1080 | **MISSING** | Same composition, alt angle/detail — funnel over field, wildflowers foreground. | Clean, no artifacts. | None | OK (provenance gap — CAUTION) |
| ai-night-city-flooding-v1.png | 1920x1080 | **MISSING** | Flooded street at night, cars with headlights on, heavy rain streaks. Tense/dangerous mood, fits disaster-doc. | Cars rendered plausibly (no melted panels/warped wheels), no readable license plates or garbled signage, reflections consistent. | None (no visible drivers/pedestrians close-up) | OK (provenance gap — CAUTION) |
| ai-night-city-flooding-v2.png | 1920x1080 | **MISSING** | Alt angle, underpass/footbridge, more cars stalled in floodwater, one distant figure silhouette on sidewalk. | Distant silhouette has no resolvable facial detail (not an identifiable likeness); cars consistent; sign in background is blurred/illegible (not garbled, just soft-focus) — acceptable. | None identifiable | OK (provenance gap — CAUTION) |
| ai-rain-wrapped-tornado-v1.png | 1920x1080 | **MISSING** | Supercell shelf cloud with visible rain shaft, power lines/poles in foreground, dusk light break at horizon. | Poles/wires geometrically consistent, no warped structures. | None | OK (provenance gap — CAUTION) |
| ai-rain-wrapped-tornado-v2.png | 1920x1080 | **MISSING** | Country road vanishing point with a single cloud-to-ground lightning bolt, wheat fields either side. | Lightning bolt physically plausible (single coherent branch pattern), road surface/markings clean, no garbled text on the roadside marker box. | None | OK (provenance gap — CAUTION) |
| ai-rural-section-road-v1.png | 1920x1080 | **MISSING** | Same road/lightning motif, alt framing, mailbox visible roadside. | Clean geometry, mailbox shape coherent, no artifacts. | None | OK (provenance gap — CAUTION) |
| ai-rural-section-road-v2.png | 1920x1080 | **MISSING** | Broad shelf-cloud with heavy rain shaft over stubble field, farmhouse at right, dusk glow breaking through. | Clean. | None | OK (provenance gap — CAUTION) |
| ai-supercell-structure-v1.png | **2048x1152** (off-spec) | **MISSING** | Classic mothership supercell structure, wide low-contrast field, dusk. Strong "menacing sky" establishing shot. | Clean cloud structure, no artifacts. | None | CAUTION (res mismatch — 2048x1152 vs project's 1920x1080 comp; needs crop/scale before wiring, and no provenance row) |
| ai-supercell-structure-v2.png | **2048x1152** (off-spec) | **MISSING** | Same motif, tighter framing on the core, dusk light patch under the base. | Clean. | None | CAUTION (same res mismatch + provenance gap) |

**AI counts:** 10/10 OK on content (no anatomy/face/text/physics defects, no real-person likeness in any file). **0 REJECT.**

**CAUTION reasons (systemic, applies to all 10):**
1. **No provenance.csv row exists for any of the 10 `ai/` files** — grepped `provenance.csv` (299 rows total) for `ai-` / `ai/`, zero matches. Per repo convention every sourced/generated asset should have a row (source_url/license/fetched/notes) — these have none, so there's no record of prompt, model, or generation date to audit against.
2. **`ai-supercell-structure-v1.png` and `-v2.png` are 2048x1152**, while the other 8 ai/ files and the project composition are 1920x1080. Per `CLAUDE.md` HARD RULE (media_budget.py / optimize_clips.py gate), any source asset over the composition's resolution must be capped before wiring — these two need a scale/crop pass first.

No REJECTs — content itself is clean and usable, but the CAUTIONs above should be resolved before these ship into a composition.

---

## Task B — media/_orig/ (111 files) — orphan index only, NOT frame-checked

Searched all sibling `media/` subdirs (`ai`, `broadcast`, `dvids`, `fema`, `music`, `noaa`, `nwsnorman`, `radar`, `spc`, `sfx`, `stock`, `stock_frames`, `weathergov`, `wikimedia`) for a same-filename match to every file in `_orig/`.

**Result: all 111 `_orig/` files have a live, same-name optimized counterpart elsewhere in `media/`. Zero orphans.**

| _orig file | found in | orig size (bytes) |
|---|---|---|
| abc-3-storm-chasers-killed.mp4 | broadcast | 8,652,611 |
| cnn-samaras-family-interview.mp4 | broadcast | 8,165,305 |
| dashboard-pov-rain-01.mp4 | stock | 6,591,476 |
| dashboard-pov-rain-02.mp4 | stock | 7,442,065 |
| dashboard-pov-rain-03.mp4 | stock | 60,739,538 |
| dashboard-pov-rain-04.mp4 | stock | 16,462,833 |
| dashboard-pov-rain-05.mp4 | stock | 3,382,595 |
| dawn-dusk-sky-01.mp4 | stock | 6,766,916 |
| dawn-dusk-sky-02.mp4 | stock | 4,791,292 |
| dawn-dusk-sky-03.mp4 | stock | 4,926,870 |
| dawn-dusk-sky-04.mp4 | stock | 2,879,155 |
| dawn-dusk-sky-05.mp4 | stock | 12,355,939 |
| emergency-lights-rain-01.mp4 | stock | 8,487,617 |
| emergency-lights-rain-02.mp4 | stock | 6,200,083 |
| emergency-lights-rain-03.mp4 | stock | 9,862,377 |
| emergency-lights-rain-04.mp4 | stock | 5,356,673 |
| emergency-lights-rain-05.mp4 | stock | 14,921,843 |
| fema-booher-elreno-damage-02.jpg | fema | 4,194,900 |
| fema-booher-elreno-damage-03.jpg | fema | 4,741,445 |
| fema-booher-elreno-damage-04.jpg | fema | 5,404,777 |
| fema-booher-elreno-damage-05.jpg | fema | 4,428,075 |
| fema-booher-elreno-damage-06.jpg | fema | 4,901,602 |
| fema-booher-elreno-damage-07.jpg | fema | 5,009,130 |
| fema-booher-elreno-damage-08.jpg | fema | 4,545,905 |
| fema-booher-elreno-damage-09.jpg | fema | 5,684,093 |
| fema-booher-elreno-damage-10.jpg | fema | 5,076,610 |
| fema-booher-elreno-damage-11.jpg | fema | 3,606,029 |
| highway-traffic-rain-01.mp4 | stock | 13,290,674 |
| highway-traffic-rain-02.mp4 | stock | 4,153,778 |
| highway-traffic-rain-03.mp4 | stock | 17,779,551 |
| highway-traffic-rain-04.mp4 | stock | 22,082,992 |
| highway-traffic-rain-05.mp4 | stock | 25,589,491 |
| highway-traffic-rain-06.mp4 | stock | 4,724,817 |
| kfor-10yr-recap.mp4 | broadcast | 4,022,256 |
| kfor-sutton-josefy-up-close.mp4 | broadcast | 6,090,512 |
| kfor-sutton-very-close-call-hookcut.mp4 | broadcast | 2,297,840 |
| kfor-sutton-very-close-call.mp4 | broadcast | 2,820,764 |
| kfor-tenth-victim.mp4 | broadcast | 11,572,236 |
| koco-reshaped-storm-chasing.mp4 | broadcast | 5,810,280 |
| koco-survivor-testimony-a.mp4 | broadcast | 10,637,389 |
| lessons-most-dangerous-tornado.mp4 | nwsnorman | 89,191,462 |
| lightning-01.mp4 | stock | 25,746,330 |
| lightning-02.mp4 | stock | 15,743,066 |
| lightning-03.mp4 | stock | 22,829,223 |
| lightning-04.mp4 | stock | 39,203,058 |
| lightning-05.mp4 | stock | 17,087,278 |
| night-flood-street-01.mp4 | stock | 9,862,377 |
| night-flood-street-02.mp4 | stock | 45,927,493 |
| night-flood-street-03.mp4 | stock | 7,209,892 |
| night-flood-street-04.mp4 | stock | 37,698,477 |
| night-flood-street-05.mp4 | stock | 14,983,249 |
| nwsnorman-briefing-may17-18-a.mp4 | nwsnorman | 14,511,687 |
| nwsnorman-briefing-may18-20-outlook.mp4 | nwsnorman | 13,600,014 |
| nwsnorman-briefing-may30-noon.mp4 | nwsnorman | 13,395,370 |
| nwsnorman-elreno-may31-745am-update.mp4 | nwsnorman | 11,841,514 |
| nwsnorman-elreno-radar-loop-a.mp4 | nwsnorman | 7,891,045 |
| nwsnorman-elreno-radar-loop-b.mp4 | nwsnorman | 5,704,705 |
| nwsnorman-moore-may20-briefing-a.mp4 | nwsnorman | 21,514,268 |
| nwsnorman-moore-may20-office-broll.mp4 | nwsnorman | 34,624,971 |
| nwsnorman-receiving-the-warning.mp4 | nwsnorman | 17,796,551 |
| nwsnorman-roundtable-staff-recollections.mp4 | nwsnorman | 1,240,494,424 |
| nwsnorman-spotter-training-a.mp4 | nwsnorman | 29,796,791 |
| nwsnorman-spotter-training-b.mp4 | nwsnorman | 108,207,731 |
| nwsnorman-spotter-training-c.mp4 | nwsnorman | 19,660,532 |
| nwsnorman-spotter-training-d.mp4 | nwsnorman | 10,429,006 |
| nwsnorman-spotter-training-e.mp4 | nwsnorman | 6,103,824 |
| nwsnorman-spotter-training-f.mp4 | nwsnorman | 3,062,210 |
| nwsnorman-spotter-training-g.mp4 | nwsnorman | 3,488,374 |
| plains-wheat-01.mp4 | stock | 41,834,979 |
| plains-wheat-02.mp4 | stock | 64,373,967 |
| plains-wheat-03.mp4 | stock | 11,428,534 |
| plains-wheat-04.mp4 | stock | 5,786,520 |
| plains-wheat-05.mp4 | stock | 20,614,444 |
| plains-wheat-06.mp4 | stock | 177,103,909 |
| radio-closeup-01.mp4 | stock | 17,521,811 |
| radio-closeup-02.mp4 | stock | 8,618,178 |
| radio-closeup-03.mp4 | stock | 8,264,247 |
| radio-closeup-04.mp4 | stock | 2,642,689 |
| rainwall-pavement-01.mp4 | stock | 11,062,634 |
| rainwall-pavement-02.mp4 | stock | 10,639,292 |
| rainwall-pavement-03.mp4 | stock | 11,266,556 |
| rainwall-pavement-04.mp4 | stock | 30,664,528 |
| rainwall-pavement-05.mp4 | stock | 23,090,312 |
| rainwall-pavement-06.mp4 | stock | 103,865,032 |
| storm-debris-wind-01.mp4 | stock | 9,583,253 |
| storm-debris-wind-02.mp4 | stock | 9,390,929 |
| storm-debris-wind-03.mp4 | stock | 43,002,279 |
| storm-debris-wind-04.mp4 | stock | 38,876,623 |
| storm-debris-wind-05.mp4 | stock | 1,806,354 |
| stormsky-timelapse-01.mp4 | stock | 32,504,397 |
| stormsky-timelapse-02.mp4 | stock | 5,656,934 |
| stormsky-timelapse-03.mp4 | stock | 5,442,274 |
| stormsky-timelapse-04.mp4 | stock | 15,609,840 |
| stormsky-timelapse-05.mp4 | stock | 25,746,330 |
| supercell-timelapse-01.mp4 | stock | 15,525,309 |
| supercell-timelapse-02.mp4 | stock | 13,623,399 |
| supercell-timelapse-03.mp4 | stock | 9,063,279 |
| supercell-timelapse-04.mp4 | stock | 2,027,202 |
| supercell-timelapse-05.mp4 | stock | 8,663,446 |
| supercell-timelapse-06.mp4 | stock | 15,588,682 |
| twc-bettes-describes-direct-hit.mp4 | broadcast | 8,446,588 |
| twc-bettes-returns.mp4 | broadcast | 9,344,965 |
| twc-bettes-suv-toss-hookcut.mp4 | broadcast | 1,592,886 |
| twc-bettes-suv-toss-marquee.mp4 | broadcast | 4,891,851 |
| wikimedia-ef5-tornado-CCBY-rodriguez.jpg | wikimedia | 5,165,716 |
| wikimedia-ef5-tornado-wedge.jpg | wikimedia | 5,017,659 |
| wikimedia-elreno-radar-2310z.png | wikimedia | 3,502,165 |
| wikimedia-preliminary-ef5-rating-survey.jpg | wikimedia | 736,334 |
| wikimedia-phased-array-radar-reflectivity.mp4 | wikimedia | 5,963,951 |
| wxgov-radar-loop-elreno.mp4 | weathergov | 5,963,951 |
| wxgov-satellite-loop-elreno.mp4 | weathergov | 2,588,143 |

### Orphans (originals with NO live counterpart)
None. 0 of 111.
