# ep-buffalo-2022 · intro section · motion-graphics list

Section `intro` = H1-S1, H1-S2, T1-S1, I1-S1, I1-S2, I1-S3, I1-S4 (`edit_script.md`). Voiced provisionally (`audio/<seg>.wav`, tempo 0.94).
The hook is a PROVISIONAL pick (`edit_script.md` H1 note). If the owner picks another hook shape, only g-intro-1 and g-intro-2 are redone (the hook's graphics). T1 and I1 graphics stand unless the intro is rewritten too.

Cue times in every brief are seconds from the START OF THAT SEGMENT's wav (`audio/<seg>.words.json`). The orchestrator adds the segment's timeline start at mount.

| comp id | segments | what it shows | depth | builder model | library exemplar to start from | footage under it |
|---|---|---|---|---|---|---|
| `g-intro-1-popfig` | H1-S1 | Red Abril date/place popfig "BUFFALO, NY / DEC 23, 2022" over Paul's first frame | standard | Sonnet 5.5, high | `.popfig` in `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` and `library/inhouse/snippets/cards.css` | Paul full-frame clip 1 (`ins-paul-1`, Santa hat), not generated yet |
| `g-intro-2-toll-chips` | H1-S2 | Four glass chips, one per sentence: 46 / 12 / 18 OF 46 / +4, with the WIVB source line | standard | Sonnet 5.5, high | `.glasscard` + `.lt` in `references/editing-patterns/ep6-glasscard-popfig-bfmg.html`; counter from `library/inhouse/numbers-rollup.html` | DVIDS 7576030 still (Guard soldier at a front door, Buffalo, 30 Dec 2022) |
| `g-intro-3-asos-log` | T1-S1 | Full-frame airport weather-log card: rows 7:24, 8:06, 8:39 tick in, chip "FRIDAY · DEC 23". BASE for g-intro-4's card | standard | Sonnet 5.5, high | `library/inhouse/numbers-rollup.html` (Courier rows, source close) on the glass panel of `library/inhouse/stat-panel.html` | none: full-frame designed ground |
| `g-intro-4-morning-map` | I1-S1 | Real map Lake Erie to Buffalo with Erie County outline and the airport pin, push into the pin, the log card returns, 7:24 rain tag, 8:39 row lights, red DRIVING BAN 9:30 AM chip, 51 MIN bracket | deep | Opus 5.5, high | `library/inhouse/master-map-us-canada.html` (real basemap + camera move, `logZoom` from `library/inhouse/snippets/helpers.js`) + the card from `g-intro-3-asos-log` | none: full-frame designed ground |
| `g-intro-5-wind-chips` | I1-S2 | Three glass chips, one per sentence: GUSTS 69 MPH / HUNDREDS STRANDED / 37 STRAIGHT HOURS, each with its own source line | standard | Sonnet 5.5, high | same chip as `g-intro-2-toll-chips` (build g-intro-2 first, copy it) | DVIDS 7572837 still (827th Engineer Co recovering an AMR ambulance, Buffalo, 26 Dec 2022) |
| `g-intro-6-count-tally` | I1-S3 | Full-frame running tally: 27 DEC 17 OF 31, 28 DEC 17 OF 37, 30 DEC 17 OF 39, LAST REPORTED 18 OF 46; the OUTSIDE bar against the NEXT LARGEST GROUP bar, to one shared scale | deep | Opus 5.5, high | `library/inhouse/ranked-bars.html` | none: full-frame designed ground |
| `g-intro-7-afd-card` | I1-S4 | NWS Buffalo Area Forecast Discussion card, 4:10 AM Sun 18 Dec 2022, the verbatim "very large and powerful storm system" sentence typed on the voice, chip "5 DAYS OUT", slow fade toward the Act 1 blackout | standard | Sonnet 5.5, high | `library/inhouse/bulletin-typewriter.html` | none: full-frame designed ground |

Count: 7 graphics. Deep 2 (Opus 5.5): g-intro-4, g-intro-6. Standard 5 (Sonnet 5.5, high): g-intro-1, 2, 3, 5, 7.
Build order: g-intro-3 before g-intro-4 (family base, send it alone for a full-size read first); g-intro-2 before g-intro-5.

## Open items for the orchestrator (not the builders')
1. Paul clip 1 does not exist yet (Santa hat needs a new start frame, `edit_script.md` "Paul on camera"). g-intro-1 can be built on the TTS cues but cannot be frame-verified or finally cued until the clip and its own words.json exist; re-cue to the clip's words.
2. H1-S2 (13.1 s) and I1-S2 (15.7 s) each sit on ONE DVIDS still. `sweep_episode.py` check 9 fails stills over 6 s: the index needs a slow push or a second picture per beat. That is index work, not these comps.
3. DVIDS licence line: `research/response.md` section 7 marks the copyright-page terms UNCONFIRMED. Both chip beats depend on it.
4. Numbers on screen without a research row (see each brief's section 1): `g-intro-3`/`g-intro-4` show "5 MI" (7:24 visibility) and gusts in mph (24, 60, 67 MPH) converted from the knots in `research/nws.md` 2.2 and 2.3. I read the 5 MI and the knots from the live IEM ASOS feed on 26 Oct 26 (URL in each brief); no research or fact-check row holds 5 MI or the mph figures yet. Add them to `research/nws.md` 2.2/2.3 or tell the builder to drop the column.
5. Footage files are not in `media/` yet; each brief names the DVIDS image id. The orchestrator writes the final path into the mount.
