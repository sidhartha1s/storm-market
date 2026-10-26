# ep-galveston-1900 · intro section graphics (H1-S1 to H1-S5, T1-S1, I1-S1 to I1-S5) · 26 Oct 26
Briefs written from `edit_script.md` (DRAFT 5, voiced provisionally) and `audio/<seg>.words.json`. Rules every brief shares: `_shared.md`. The hook is PROVISIONAL: a different hook redoes g-intro-1 to g-intro-5 only.
10 graphics: 3 deep (Opus 5.5, high), 7 standard (Sonnet 5.5, high). Build order: g-intro-4 (base) first and read it full size, then g-intro-8 copies it; g-intro-2 before g-intro-10 (shared chip).

| comp id | segments | what it shows | depth | builder | library exemplar | footage under it |
|---|---|---|---|---|---|---|
| g-intro-1-pop1891 | H1-S1 | popfig "JULY 1891" with "GALVESTON, TEXAS", left column clear of Paul's face | standard | Sonnet 5.5 high | `references/editing-patterns/ep6-glasscard-popfig-bfmg.html`, cards.css `.popfig` | `ins-paul-1` (not generated; start frame stand-in) |
| g-intro-2-cline1891 | H1-S2 | lower-third ISAAC CLINE / Galveston Weather Office, then chip ABSURD DELUSION with red rule, source line | standard | Sonnet 5.5 high | official `lt-dark-card`; `ep-1974-super-outbreak/compositions/g-cite-paper.html` | 1891 Galveston Daily News page scan, push to the column |
| g-intro-3-sept8 | H1-S3 | popfig "SEPT 8, 1900" / SATURDAY, then chip AT LEAST 6,000 LIVES (count-up) / Cline's own count | standard | Sonnet 5.5 high | `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` | LoC ruins photograph, Galveston 1900 |
| g-intro-4-wire-map | H1-S4 | Gulf map: Belen Observatory pin, Havana arrow NW into the Gulf; pull-out to Washington; telegraph lines, Washington lit, Havana dark | DEEP | Opus 5.5 high | `library/inhouse/master-map-us-canada.html` (rig, projection), `ep6-katrina-2005/compositions/g-track.html` | none (full-frame map) |
| g-intro-5-src-mwr | H1-S5 + T1-S1 0 to 0.88 | source line only: Isaac Cline, Monthly Weather Review, Sept. 1900 | standard | Sonnet 5.5 high | cards.css `.srclab` | 1891 page dimming, then MWR page push to the wife line |
| g-intro-6-island | T1-S1 | island cross-section on a sea-level datum (40 px/ft), 8.7 ft bracket, chips ABOUT 38,000 PEOPLE, HIGHEST POINT ABOUT 8.7 FT, WARNED, FEW HAD LEFT | DEEP | Opus 5.5 high | `ep6-katrina-2005/compositions/g-surge-ms.html`, `library/inhouse/then-now-scale.html` | none (full-frame diagram) |
| g-intro-7-clines | I1-S1 0 to 8.10 | lower-third ISAAC CLINE / Local Forecast Official, Galveston, swapped to JOSEPH CLINE / Observer · his brother | standard | Sonnet 5.5 high | `ep-1974-super-outbreak/compositions/g-person-allen.html`, official `lt-stack-bars` | MWR Sept 1900 page at Cline's byline |
| g-intro-8-track | I1-S1 8.10 to I1-S3 end | storm ring across Cuba (chip CROSSES CUBA · SEPT 4), Washington's recurve path, Moore lower-third, real track into the Gulf (chip STEAMER LOUISIANA · SEPT 6), on toward Galveston, Washington wire pulsing | DEEP | Opus 5.5 high | base `g-intro-4-wire-map`; `ep6-katrina-2005/compositions/g-track.html` | none (full-frame map) |
| g-intro-9-warnings | I1-S4 | five day tiles SEPT 4 to 8 with message bars, STORM WARNING band on the 7th, chip MODERATE STORM / Washington, Friday midday | standard | Sonnet 5.5 high | `library/inhouse/stat-timeline.html`, `library/inhouse/numbers-rollup.html` | MWR page push to the warning-messages line |
| g-intro-10-delusion | I1-S5 | popfig "JULY 16, 1891", then the ABSURD DELUSION chip back on | standard | Sonnet 5.5 high | chip from `g-intro-2-cline1891`; cards.css `.popfig` | 1891 Galveston Daily News page, slow return |

## Changes from the Picture lines (the orchestrator decides; each brief says why)
1. Maps (H1-S4, I1-S1 to I1-S3) are drawn on a Natural Earth basemap with a stated projection, not on the 1900 NOAA weather-map scans: no scan is on disk and pins on a 1900 projection would be placed by eye. The scans can come in as stills before the maps.
2. "BELEN OBSERVATORY, HAVANA" is a map pin label, not a popfig (popfigs carry dates and figures only).
3. "'MODERATE STORM'" loses its quote marks: the only row is OSU's summary, not the warning's text.
4. T1-S1 "sea level line rising to the island's top" is drawn as a measuring bracket rising from sea level; the sea itself never rises (that would claim an 8.7 ft surge).
5. Source lines sit top-left in this whole section (bottom-right is the presenter circle's corner, bottom-left the lower-third's).
6. I1-S3 "track line running toward the island elevation graphic" is drawn as the track stopping offshore of the Galveston pin; the island diagram does not return.

## Open items that hold a graphic
- 1891 page scan: the Commons file is cited in sources-cline.md, but footage-inventory.md says no scan was found, and the edit script still lists the human check of the scan as open. This holds g-intro-2 and g-intro-10 (the on-screen quote) and is the footage under g-intro-2, g-intro-5 and g-intro-10.
- Track positions (g-intro-8): there is no research row for the 1900 storm's 6-hourly track. The builder takes HURDAT2 AL011900 and checks it against the four sourced anchors, or falls back to "Track: schematic".
- Paul clip 1 is not generated: g-intro-1 is timed to the TTS stand-in and must be retimed to the clip.
- g-intro-3: a date popfig over aftermath photos (taken 24 Sep to 15 Oct 1900) needs the orchestrator's call under mg-quickref 7a item 7.
