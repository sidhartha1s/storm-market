# ep-moore-1999 · motion-graphics plan

Each graphic, its segments, the library start point and the builder model (CLAUDE.md "Chain of command for motion
graphics": Opus 5.5 high for the deep ones, Sonnet 5.5 high with a full `references/mg-brief-template.md` brief for the
rest). Builders start only once their act's VO is final (TTS done, words.json read); a graphic built before that gets
retimed. Briefs are written per act as each act locks. The orchestrator reads a settled frame of every graphic over its
real footage before any render; a Sonnet graphic that fails twice goes to Opus.

Per-act variants follow the Enderlin pattern (`g-master-map-a1.html` ... one file per act state, same base).

## Deep (Opus 5.5, high)
| graphic | segments | start from | what it must show |
|---|---|---|---|
| g-path-map (+ -i1, -a1, -a2, -a3, -a4, -a5) | I1-S1, A1-S1, A1-S8, A1-S10, A2-S1, A2-S5, A3-S1, A3-S2, A3-S6, A3-S7, A3-S10, A3-S11, A4-S1, A4-S2, A4-S10, A5-S7 | `library/inhouse/master-map-us-canada.html` zoomed to central Oklahoma; track from `media/stills/oun-19990503_overview_filled.kml` | A9 track drawing Amber to Midwest City on the clock; county lights (Comanche, Caddo, Grady, McClain, Cleveland, Oklahoma); pins and labels named in each Picture line; car icons (A3-S7/S8, reused A5-S8); 2013 track crossing it (A5-S7) |
| g-leadtime | I1-S2 | `library/inhouse/ranked-bars.html` | 4 county bars 65/18/31/13 min, one per sentence, then 32 MIN AVERAGE beside a grey 10–15 min band; two source lines |
| g-dow | A2-S3 | `library/inhouse/radar-beam.html` | radar-truck icon, beam on the funnel, 6:54 PM, ABOUT 302 MPH ± 11 at ABOUT 100 FT UP, then the small 318 MPH · ANNOUNCED 1999 chip; never Wurman's Figure 1 |
| g-risk-ladder | A1-S2, A1-S3 | `library/inhouse/ef-ladder.html` | SLIGHT · MODERATE · HIGH, marker one rung per sentence, time chips 6:30 AM, LATE MORNING, 3:49 PM; watch box #195 4:30 PM |
| g-cellar | H1-S2, H1-S3, T1-S1, A2-S7 | scratch (no exemplar fits): cellar door over a Grady County map | door opens on the F5 line and is held open; no town marked; chip 35 IN ONE CELLAR |
| g-ages | A5-S1 | `library/inhouse/ranked-bars.html` axis, scratch dots | 36 dots on an age axis 0–94 from the Brooks list; the 5–23 band empties; chip DIRECT LOSSES · AGES 5 TO 23 · NONE |
| g-estimates | A5-S3 | `library/inhouse/split-shared-scale.html` | 36 solid bar vs hatched ~700 (NOAA Report, no warnings) and ~540 (B&D 2002, crude); labelled as estimates |

## Standard (Sonnet 5.5, high, full brief)
| graphic | segments | start from |
|---|---|---|
| g-clock (4:47 PM, ticking) | I1-S3, A1-S1 | `episodes/ep-enderlin-2025/compositions/g-clock.html` |
| g-bulletin-541 (5:41 PM text, "EXERCISE YOUR TORNADO SAFETY PROCEDURES!") | A1-S7 | `library/inhouse/bulletin-typewriter.html` |
| g-bulletin-657 (Tornado Emergency text) | A3-S2 | `library/inhouse/bulletin-typewriter.html` |
| g-timeline-541 (5:41 to 7:22 PM bar) | A1-S7 | `library/inhouse/stat-timeline.html` |
| g-counter (32 SPOTTER CLASSES · 3 MONTHS) | A1-S5 | `library/inhouse/numbers-rollup.html` |
| g-spotter (silhouette, phone to ear; desk phone NO SERVICE reused A3-S4) | A1-S5, A3-S4 | scratch |
| g-waterbill (envelope, insert slides out) | A1-S6 | scratch |
| g-tv-override (speaker icon pulsing, no banner) | A1-S6 | scratch |
| g-wx-radio (alert light, 1050 Hz tone) | A3-S3 | scratch |
| g-tv-tiles (TORNADO EMERGENCY across unbranded tiles over the radar loop) | A3-S4 | scratch |
| g-get-out (blank TV, station name withheld) | A3-S7 | scratch |
| g-mh-risk (two rows of icons, both marked estimate) | A2-S5 | `library/inhouse/split-shared-scale.html` |
| g-chassis (14 x 60 ft outline slides ~200 yd) | A2-S4 | scratch |
| g-basement (cutaway, concrete ceiling) | A2-S6 | scratch |
| g-westmoore (locker core + stairwell plan, figures move inward; only if no FEMA photo) | A4-S2 | scratch |
| g-corridor (Kelly Elementary hallway, high windows) | A4-S3 | scratch |
| g-walls (BATHROOM 81% · CLOSET 75% · KITCHEN ~16%, header 89 WALL CLUSTERS) | A4-S8, A4-S10 | `library/inhouse/ranked-bars.html` |
| g-lives-cards (4 cards, no names) | A4-S7 | `library/inhouse/quote-card.html` |
| g-quotes (SA p15, SA p11 pair, Doswell-Brooks paraphrase, McCarthy, 2013 tweet, 2013 survivor) | A3-S5, A3-S8, A4-S9, A5-S5, A5-S8, A5-S9 | `library/inhouse/quote-card.html` |
| g-te-timeline (1999 · 2014 · 2017) | A5-S6 | `library/inhouse/event-timeline.html` |
| chips and source lines | all | `references/mg-quickref.md` glass card + tokens |
| title card, outro | A5-S11 | `library/inhouse/title-card.html`, `outro-brand.html` |

Count: 7 deep (Opus), 21 standard (Sonnet), plus chips. One builder per graphic, all in parallel once their act's VO is final.
