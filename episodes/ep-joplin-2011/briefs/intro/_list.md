# INTRO · Hook, hook tail, intro (H1, T1, I1) · motion-graphics list (briefs written 17 Oct 26)

Source of every Picture line: `episodes/ep-joplin-2011/edit_script.md` H1-S1, T1-S1 to T1-S3, I1-S1 to I1-S9. Numbers:
`research/facts.md` rows only. Cues: `audio/<seg>.words.json`. Builders: DEEP = Opus 5.5 high, STANDARD = Sonnet 5.5 high
(CLAUDE.md "Chain of command"). Every builder's brief carries `references/mg-quickref.md` and `references/mg-brief-template.md` §6 to §8.

## Conventions (every brief in this folder uses them)
- **Cue notation** `i1-s3 "once" 2.24` = that word's `start` in `audio/i1-s3.words.json`, seconds from the start of that segment's
  wav. Words are written the way whisper spelled them: digits ("135", "25", "50" ",000."), `i1-s6` "missed" (spoken "NIST"),
  `i1-s2` "If we lived" (script: "If you lived"). Comp-local time = (`nx-<seg>` data-start − host data-start) + word time; the
  data-starts come from the narration mounts in `index.html` (not built yet; the orchestrator mounts hosts before dispatch).
  Put the spoken cue in a comment beside each tween (`/* ONCE i1-s3 2.24 */`).
- **Shared bases this act owns** (first use on screen is here; copy the base file and retune, never rebuild):
  - **MASTER MAP** = the `<!--BASEMAP:g-master-map--> … <!--/BASEMAP-->` block inside `g-intro-map` (T1-S2). It owns all
    geography: grid, city outline, streets, the damage path, the 25 siren icon positions, the Table 4-3 location markers, the
    siren ring and the below-ground line. The a3 briefs copy this block by that marker (they say "`compositions/g-master-map.html`":
    the block lives in `compositions/g-intro-map.html`; see "For the orchestrator").
  - **SIREN RING**: defined in `g-intro-map.md` §3 (colour, radius rule, pulse). `g-a2-countdown` and `g-a1-second-siren` copy it.
  - **BELOW-GROUND LINE**: defined in `g-intro-map.md` §3, the same values `g-a2-map-close` already states (2 px `#93a3b2`, label "Below ground").
  - **SIREN ICON**: the glyph drawn in `g-intro-map`'s base (placed and revealed in `g-intro-strip`). `g-a6-siren` enlarges it.
  - **DOT LAYER** (154 Table 4-3 dots): `<!--DOTS:g-intro-map-dots-->` block in `g-intro-map-dots`. Its end state (I1-S8) is the
    "lit 135-dot state" `g-a6-map135` copies (a6 calls it I1-S9; it is the I1-S8 end state).
  - **PAGE UNDERLINE**: defined in `g-intro-page-sirens.md` §2 and §3 (page crop card, shadow, underline bar). `g-a1-gutter`,
    `g-a1-numb` and the other a1 page comps copy it; `g-intro-page-survivors` is the first copy.
- **Shared bases this act copies** (owned elsewhere, already briefed):
  - **SIREN STRIP**: px table in `briefs/a1/g-a1-strip-sirens.md` §2 and §3, used here unchanged so the two acts share one
    table. The warnings row uses the `g-a1-strip-warnings` recount pitch (64 px, x 200 to 944, band y 670 to 740).
  - **HOUSE SECTION**: geometry in `briefs/a3/g-a3-house-section.md` §2 and §3. `g-intro-nobasement` draws it first on screen,
    so that base is built and read full-size before `g-intro-nobasement` (same Opus builder).
- **Chips**: glass chips (`references/editing-patterns/ep6-glasscard-popfig-bfmg.html`), one at a time, top centre x 960, y 96 to 166
  on map and strip scenes; centre-left on Paul's clip. Never a red popfig over a map or card.
- **Source lines** inside comps: bottom-left, x 96, baseline 1010, Arial 700 20 `#c8d3e0`, never in the presenter corner (x ≥ 1600, y ≥ 680).

## Open numbers and open items (left out of every drawing until a facts.md row or the orchestrator supplies them)
1. **Siren split "23 in the city · 1 Duenweg · 1 Airport Drive"** (I1-S2 Picture line, "NIST Sec. 4.3.1"): no facts.md row; facts.md
   line 440 says no siren count other than 25 is claimed. The source line says 25 only.
2. **NIST Fig. 4-2** (siren positions) is not in `media/candidates/intro/`. The 25 icon positions are traced from it, so the siren
   layer is BLOCKED until the orchestrator extracts that page from NIST NCSTAR 3 (public domain) into `media/candidates/intro/`.
3. **"2010 Census"** on the city label (I1-S1): X21 quotes only "with a population of 50,150". The label cites NIST Sec. 1.1, no census year.
4. **Positions of the Table 4-3 locations** (11 named buildings, the apartment complexes, homes, outside): no coordinates in
   facts.md (a3 and a4 lists carry the same open). The orchestrator writes `research/map-positions.md` (location, address, lat/lon,
   source) before `g-intro-map` is built. A location without a row is not drawn. Residential and outside dots are spread
   schematically in the lit path area and the dot layer carries "Schematic positions" in its source line.
5. **Dates of the 12 warnings** (S13 gives only 10 May 2008): the I1-S4 warnings row is an undated count, as in `g-a1-strip-warnings`.
6. **Cue clock for H1-S1**: the cues are from `audio/h1-s1.words.json`. If Paul's Flow clip (`ins-paul-1`) carries its own audio,
   re-transcribe the clip and shift every `g-intro-hook` cue to it; the clip is the clock.

## Comps

| comp id | segments | what it shows | DEEP/STANDARD | exemplar | cue span s |
|---|---|---|---|---|---|
| g-intro-hook | h1-s1 | Overlay on Paul's clip: date/place popfig, glance chips TORNADO SIREN, 135 INDOORS, 0 BELOW GROUND, source chips Finding 40 and 46 | STANDARD | `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` | h1-s1 "Okay," 0.00 to clip cut after "ground." (end 16.90) |
| g-intro-161 | t1-s1 | Overlay on the flattened-street photo: popfig "161" / "Lives lost", source line Finding 28 | STANDARD | `ep6-glasscard-popfig-bfmg.html` (`.popfig`) | t1-s1 "161" 7.32 to wav end 9.52 |
| g-intro-map | t1-s2, t1-s3 | MASTER MAP base, first appearance: city draws, two siren rings stamped 5:11 PM / 5:38 PM, chip SOUNDED TWICE, source line; then the empty "Below ground" line and the push onto it | DEEP | `episodes/ep-enderlin-2025/compositions/g-master-map.html` (BASEMAP block pattern), `references/editing-patterns/ep3-map-route-fit.html` | t1-s2 "You" 0.00 to t1-s3 wav end 5.24 |
| g-intro-nobasement | i1-s1 | House section with the empty basement ghost, chip 8 IN 10: NO BASEMENT; master map with no shelter anywhere (scan), city label, the path draws W to E with "6 miles" / "about 15 minutes"; a small house-with-basement inset, stair lit and empty | DEEP | HOUSE SECTION (`g-a3-house-section`), MASTER MAP base | i1-s1 "about" 3.52 to wav end 14.56 |
| g-intro-strip | i1-s2, i1-s3, i1-s4 | Master map: 25 siren icons appear; SIREN STRIP (2007) slides in under it with the test label; map leaves, strip stretches to May 2011, 4 red marks, gap bracket, chip ABOUT ONCE A YEAR; name card; separate amber row of 12 warnings; source lines | DEEP | SIREN STRIP table (`g-a1-strip-sirens`), MASTER MAP base, `library/inhouse/stat-timeline.html` | i1-s2 0.00 to i1-s4 wav end 6.96 |
| g-intro-page-sirens | i1-s5 | PAGE UNDERLINE base: NWS Assessment page, "hear sirens all the time and [sirens] go off for dark clouds" underlined in two strokes; source line Finding 2b | STANDARD | `library/official/vox-annotate.html` | i1-s5 "But" 0.00 to wav end 6.20 |
| g-intro-nist | i1-s6 | NIST NCSTAR 3 cover card, name card NIST, source line 154 of 155 placed · Table 4-3 | STANDARD | `library/official/lt-kicker-name.html`, `library/inhouse/title-card.html` | i1-s6 "missed" 4.28 to wav end 9.80 |
| g-intro-map-dots | i1-s7, i1-s8 | MASTER MAP copy: 154 dots land one location type at a time with a label each (7 spoken + 4 unspoken); lit state 135 inside / 19 outside (12 vehicles), "154 placed · 1 not placed" label; rail card 135 of 155; "0" on the empty below-ground line | DEEP | MASTER MAP base, `library/inhouse/examples/joplin-stat-panel.html` (rail card) | i1-s7 "They" 0.00 to i1-s8 wav end 6.12 |
| g-intro-strip-back | i1-s9 | SIREN STRIP copy in its I1-S3 finished state: Monday ticks dim, red marks pulse lit, label "Outside the weekly test" | STANDARD | `g-intro-strip` (copy) | i1-s9 "So," 0.00 to "why" 4.46 |
| g-intro-page-survivors | i1-s9 | PAGE UNDERLINE copy: NWS Assessment p7 (printed 1), slow push, "interviewed over 60 survivors" underlined; source line | STANDARD | `g-intro-page-sirens` (copy) | i1-s9 "After" 7.46 to wav end 14.48 |

There are 10 comps: 4 DEEP and 6 STANDARD. One Opus builder takes `g-intro-map`, `g-intro-strip`, `g-intro-map-dots` and
`g-intro-nobasement` (the base and its first copies; `g-a3-house-section` first). The base is read full-size before any copy is made (template 7a).
`g-intro-strip-back` is built only after `g-intro-strip` passes its frame read; `g-intro-page-survivors` after `g-intro-page-sirens`.

## Every intro Picture-line graphic, and where it lives

| seg | graphic on the Picture line | comp |
|---|---|---|
| h1-s1 | popfig "Joplin, Missouri · May 22, 2011"; chips TORNADO SIREN, 135 INDOORS + source chip Finding 40, 0 BELOW GROUND + source chip Finding 46 | g-intro-hook |
| t1-s1 | "161 lives lost"; source line Finding 28 | g-intro-161 |
| t1-s2 | master map first appearance; two siren rings stamped 5:11 PM, 5:38 PM; flash on "twice"; chip SOUNDED TWICE; source line "NWS timeline · 3 minutes each" | g-intro-map |
| t1-s3 | thin "below ground" line under the map, empty; push in until it fills the frame | g-intro-map |
| i1-s1 | house cross-section, no basement, label 82 % · Finding 20; chip 8 IN 10: NO BASEMENT | g-intro-nobasement |
| i1-s1 | map with no shelter icons, label "no community shelters or safe rooms"; city label population 50,150; path W to E, "6 miles in Joplin", "about 15 minutes in the city"; source line Sec. 1.3 | g-intro-nobasement |
| i1-s1 | smaller cross-section with a basement, stairs lit and empty | g-intro-nobasement |
| i1-s2 | 25 siren icons at once (Fig. 4-2); source line 25 sirens; calendar strip slides in, Monday ticks, label "test · 10 AM · 1 minute · weather permitting" | g-intro-strip |
| i1-s3 | strip stretches to 2007 to 2011; 3 red marks + gap to May 22, 2011; source line Finding 31 and Sec. 4.3.4; chip ABOUT ONCE A YEAR | g-intro-strip |
| i1-s4 | name card "Joplin-Jasper County emergency manager"; second separate strip, 12 warnings; label "not every warning got a siren · NIST Sec. 4.3.4" | g-intro-strip |
| i1-s5 | NWS page, residents' words underlined; source line Finding 2b | g-intro-page-sirens |
| i1-s6 | NIST cover, name card "NIST · National Institute of Standards and Technology · federal investigators"; source line 154 of 155 · Table 4-3 | g-intro-nist |
| i1-s7 | master map, dots land by location type, a label each (7 spoken, 4 unspoken) | g-intro-map-dots |
| i1-s8 | whole map lit, 135 in / 19 out (12 vehicles), "154 placed · 1 not placed · location unknown"; empty below-ground line; figure 135 of 155 · 87 % · Finding 40; "0" on the line · Finding 46 | g-intro-map-dots |
| i1-s9 | calendar strip returns, ticks dimmed, red marks lit, "outside the weekly test" | g-intro-strip-back |
| i1-s9 | NWS page, slow push; source line "NWS assessment team · interviewed over 60 survivors" | g-intro-page-survivors |

Not graphics (sourced in parallel; named so the builder knows what sits under or beside a comp):
- h1-s1: Paul's full-frame clip `ins-paul-1` under `g-intro-hook` (siren SFX is index audio).
- t1-s1: the flattened-street still under `g-intro-161`, pick `media/candidates/intro/t1-s1_c1_usace-flattened-neighborhood.jpg`
  (USACE, not NIST: `candidates.md` says NIST has no usable ground photo). A still over 6 s needs a slow push in index.html (sweep check 9).
- i1-s1: CLIP 1 `i1-s1_c1_dvids-aerial-residential-a.mp4`, i1-s1 0.00 to "about" 3.52 (burned-in Guard credit: crop or cover).
- i1-s6: CLIP 2 before `g-intro-nist`, i1-s6 0.00 to "missed" 4.28: safe pick `i1-s6_c2_dvids-aerial-bigbox-lot.mp4`; `c1` (KSHB) is not cleared (no transcript).
- i1-s9: CLIP 3 between the two i1-s9 comps, "why" 4.46 to "After" 7.46: `i1-s9_c2_noaa-aerial-st-johns-area.jpg` (no survey-team footage exists).
- Page and cover images, mounted inside their comps: `i1-s5_c1_nws-assessment-p13-sirens-quote.png`, `i1-s6_cover_nist-ncstar3.png`,
  `i1-s9_c1_nws-assessment-p7-60-survivors.png` (all 1105 × 1430, in `media/candidates/intro/`).

## Picture-line readings the orchestrator should confirm
- **H1-S1 popfig**: the Picture line puts it top left with five words; `mg-quickref` says a popfig is 3 words or fewer, mid-screen.
  The brief splits it: big "May 22, 2011" (3 words), Arial sub "Joplin, Missouri", top left, clear before "TORNADO SIREN" lands (DESIGN.md "Cold-open hook contract").
- **H1-S1 "0 BELOW GROUND"** lands on "below" 16.26 and the clip cuts on the last word (end 16.90): about 0.7 s on screen. An option
  is to land it on "not" 14.14; the brief follows the Picture line.
- **I1-S1 order**: the Picture line opens on the cross-section but also puts CLIP 1 "under the first sentence". The brief runs the
  clip to "about" 3.52 and the cross-section from there. The "smaller cross-section with a basement" is read as an inset card over the map.
- **I1-S1 label vs chip**: "no basement · 82% of Joplin homes" and "8 IN 10: NO BASEMENT" are one fact twice. The brief keeps the chip
  and moves "82% of Joplin homes · NIST Finding 20" into the source line.
- **I1-S4 warnings row**: the Picture line says "2007 to 2011"; S13 says "the five years before 22 May 2011". The row label uses the
  S13 wording, the same as `g-a1-strip-warnings`.
- **I1-S9 order**: the Picture line lists clip, strip, page; the voice says the strip line first ("hardly ever sounded" 2.02) and
  the survivors line last. The brief follows the voice: strip 0.00 to 4.46, clip 4.46 to 7.46, page from 7.46.
- **I1-S9 page**: the Picture line pushes in "on the word 'sirens'", but page p7 (the one with "interviewed over 60 survivors")
  has no "sirens" on it. The push lands on "interviewed over 60 survivors". The framing stays off the page's "158" (NWS count, T26).
- **T1-S2 times**: this comp stamps 5:11 PM and 5:38 PM (the Picture line asks); `g-a1-second-siren` §0 assumes A2 reveals them first. Its no-times rule still stands for its own comp.

## For the orchestrator (cross-act paths to fix in the other acts' briefs; not edited here)
- `briefs/a3/*` say the base file is `compositions/g-master-map.html`; it is the BASEMAP block inside `compositions/g-intro-map.html`.
- `briefs/a5/g-a5-map-sjrmc.md` points at `briefs/i1/_list.md`; the folder is `briefs/intro/`. a5 says the map is first drawn at I1-S2; it is T1-S2.
- `briefs/a6/g-a6-map135.md` copies "the I1-S9 lit state": that is the end state of `g-intro-map-dots` (I1-S8).
