# g-a2-countdown · DEEP (Opus 5.5, high) · act a2, segments a2-s1, a2-s2, a2-s3, a2-s5, a2-s6

**Open numbers (left out of the drawing):** polygon 30 and polygon 31 vertices (facts.md gives coverage text only,
E4, E9): build everything else first; draw the polygons only once the orchestrator supplies the lat/lon vertices.
Pin coordinates for Webb City and Carl Junction come from the master map base's place layer; if it has none, report.
**Open claim:** "WHOLE CITY" rests on E9 "(and Joplin)"; the stronger NIST Sec. 1.2 wording is not a facts.md row.

**Base, never redrawn:** the master map of Joplin and its siren ring, first built for T1-S2 (intro briefs; the base id
named there wins). Copy the base into this comp and add layers. If the base is not built yet, stop and report.
**Host:** one host from a2-s1's first frame to the end of a2-s6. a2-s4's NIST photograph and its quote card
(g-a2-quote-108) sit on higher tracks over this host for a2-s4; keep the map drifting underneath, change no state there.
**Cue clock:** every cue is `segment offset + word start`. Segment offset = `data-start` of a2-sN's narration audio in
index.html minus this host's `data-start`, read at dispatch. Word starts below are from `audio/a2-sN.words.json`
(Whisper writes "1 .30", "509", "Web City"; the spelling on screen follows the script).
**Over:** designed full-frame map, no footage. Corner circle stays on: nothing enters x >= 1600, y >= 680.

## 0. What this graphic claims
The evening ran on a clock nobody on the ground could see whole: the first warning (5:09) was for a storm north of
the city that never made a tornado; the first siren (5:11) sounded mostly for funnel reports in Kansas and was heard as
meant for the north; the city-wide warning (5:17) came with no siren, while the news still said the storms were
passing north.

## 1. SOURCE (confirmed rows, quoted)
- E1 (NWS Table 1): "130 pm CDT - NWS/SPC Tornado Watch issued for Southwest Missouri". Use 1:30, never NIST's 3:00 (E2, facts.md CONFLICT).
- E3 (NIST E.3): "At 4:33 p.m., NWS forecasters in Springfield, Missouri, briefed the Joplin-Jasper County Emergency Manager (EM) on severe storms to the west".
- E4 (NWS Table 1): "509 pm CDT - WFO Springfield Tornado Warning Polygon #30 issued for Western Jasper County MO (including northeastern Joplin)".
- E5 (NIST Sec. 2.2.2): "the storm that prompted TO. W 30 did not produce a tornado and the warning only included a small portion of the city of Joplin."
- E6 (NWS Table 1): "511 pm CDT - Initial 3 minute siren alert sounded for Jasper County and Joplin".
- E8 (NWS Sec. 3): "resulted primarily from funnel cloud reports to the west of Joplin in southeastern Kansas."
- E8b (NWS Sec. 3): "assumed the activation was for the area to the north."
- E9 (NWS Table 1): "517 pm CDT - WFO Springfield Tornado Warning Polygon #31 issued for southwest Jasper County MO (and Joplin), northwest Newton County MO and southeast Cherokee County (KS)".
- E10 (NIST Sec. 1.2): "the outdoor siren system was not activated again for the 5:17 p.m. warning, probably because Joplin's emergency manager had already sounded the system 6 min earlier".
- E11 (NIST Sec. 1.2): "related to a storm that weather forecasters were tracking to the north of Joplin, that was heading toward Webb City or Carl Junction".
- E12 (NIST Sec. 1.2): "the media continued to report on storms said to be passing to the north and missing Joplin, or moving away from the City."
- Map geometry: the master map base (its own cited basemap). Polygons: NWS warning archive vertices (open, above).

## 2. DATUM, SCALE, ORIENTATION
- North up, the base's projection and scale unchanged; every new layer is projected through the base's own lon/lat function, never placed by eye.
- HUD (fixed, never rides the camera): clock card left 96, top 54, 380 x 150. Chip slot left 110, bottom 110. Source line right 96, top 54, right-aligned.
- Camera: one continuous drift over the whole host, scale 1.00 to 1.04, ease none, origin the city centroid; a pan of at most 120 px toward Kansas during a2-s3 and toward the north during a2-s6 (`logZoom` not needed under 1.5x).

## 3. GEOMETRY
- Clock card (glass, tokens.md surface): dial circle r 40 at card-local (78, 75), one hand rotating 360 deg per 12 s, ease none, finite repeat to the host end (the comp's always-moving element, 21 px/s at the tip). Time text left edge at card x 140: "5:09" Arial Black 900 84 px #f2f5f8, "PM" Arial 700 30 px #dfe7ee, "CDT" Arial 700 20 px #93a3b2 tracking 4 under "PM". One pre-authored leaf group per time; a change rolls: old group y 0 to -40 + autoAlpha 0, new group y 40 to 0, 0.45 s power3.out.
- Chips: glass, text Arial Black 900 40 px #f2f5f8 tracking 2, padding 18 x 28; in x -40 to 0 + autoAlpha 0.4 s power3.out; a new chip replaces the old one (old out y -20, autoAlpha 0, 0.3 s) so one chip shows at a time.
- Source line: glass pill, Arial 700 20 px #c8d3e0 tracking 2; swaps like the chips.
- Polygon 30: amber `#d8a13a` stroke 4 px, fill rgba(216,161,58,.14), stroke draws (strokeDashoffset, ceil(len)+1) 0.9 s then fill in 0.3 s. Label "polygon 30" diagram label (Arial 700 22 #93a3b2 tracking 3) at the polygon's south-west edge, outside the city outline.
- Polygon 31: red `#e74c3c` stroke 4 px, fill rgba(231,76,60,.16), same draw. Label "polygon 31" at its south edge. When 31 draws, 30 dims to 40 % opacity and stays.
- Siren ring: the base's ring, centred on the city centroid. Lit state = the base's pulse. Dark state = `#4a5560` stroke 3 px, dash 10/8, no pulse. Flashback state = the lit ring at 50 % with its stamp "5:11 PM".
- Arrow west: amber-2 `#e8c56a` 5 px, from the city's west edge to a point at least 60 px west of the MO-KS state line, head 22 px; label "Funnel cloud reports · SE Kansas" Arial 700 26 px #dfe7ee just above the arrow shaft, inside Kansas.
- Cite card (a2-s6): beige cite card (tokens.md), x 140 to 1180, y 690 to 960 (stays left of 1600), dark text #2a2622: quote Georgia italic 34 px in three pre-authored lines, attribution "NIST NCSTAR 3, Sec. 1.2" Arial 700 20 px #6b6257.
- Arrow north: `#dfe7ee` 4 px from the city's north edge to the Webb City and Carl Junction pins; label "Webb City · Carl Junction" Arial 700 26 px beside the pins, never on the cite card.

## 4. MUST BE TRUE IN THE PICTURE (reviewer checks first)
1. Polygon 30 covers only part of the city outline, and that part is in the north-east (E4 "including northeastern Joplin", E5 "only a small portion").
2. Polygon 31 contains the whole city outline (E9; open claim above).
3. The siren ring covers the whole city outline (E6 "for Jasper County and Joplin").
4. The west arrow's head ends in Kansas, west of the state line (E8).
5. The north arrow ends at Webb City and Carl Junction, both north of the city outline (E11).
6. The clock shows one time at a time, in this order only: 1:30, 4:33, 5:09, 5:11, 5:17 (E1, E3, E4, E6, E9). 3:00 never appears.
7. From the a2-s5 "sirens" cue to the a2-s6 "six" cue the ring is dark. The flashback is a past state (50 %, stamped "5:11 PM") and returns to dark; it never reads as a third sounding (E10).
8. "polygon 30" and "polygon 31" are screen-only labels; no other polygon numbers appear.
9. No chip, label or line enters x >= 1600, y >= 680.

## 5. PANEL TEXT (exact) and CUES
| cue (segment · word · start s) | what happens |
|---|---|
| a2-s1 · "I" · 0.00 | map up from the base's opening state, drift starts, clock card in empty (dial only) |
| a2-s1 · "1" · 3.02 | clock "1:30 PM CDT"; source line "NWS Assessment, Table 1" |
| a2-s1 · "tornado" · 5.14 | chip "TORNADO WATCH" |
| a2-s1 · "4" · 10.80 | clock rolls to "4:33 PM"; source line "NIST E.3" |
| a2-s1 · "briefed" · 14.12 | chip "NWS BRIEFING" |
| a2-s2 · "509," · 1.28 | clock "5:09 PM"; source line "NWS Table 1 · NIST Sec. 2.2.2"; chip out |
| a2-s2 · "warning" · 2.50 | polygon 30 draws; label "polygon 30" after the stroke closes |
| a2-s2 · "corner" · 5.04 | overlap with the city outline brightens; chip "WARNING · NE CORNER" |
| a2-s3 · "5" · 0.92 | clock "5:11 PM"; source line "NWS Assessment, Sec. 3"; chip out |
| a2-s3 · "sirens" · 2.98 | siren ring pulses over the city (the SFX lands here in index.html, 3 s) |
| a2-s3 · "three" · 3.86 | chip "FIRST SIREN · 3 MIN" |
| a2-s3 · "funnel" · 5.66 | arrow west draws, 0.7 s |
| a2-s3 · "southeast" · 6.96 | label "Funnel cloud reports · SE Kansas" |
| a2-s3 · "north," · 10.92 | polygon 30 lights again (stroke to 100 %, fill pulse twice); arrow and its label fade out |
| (a2-s4) | covered by g-a2-quote-108; drift and dial continue, no state change |
| a2-s5 · "5" · 0.76 | clock "5:17 PM"; source line "NIST Sec. 1.2"; chip out |
| a2-s5 · "warning" · 2.70 | polygon 31 draws; polygon 30 dims to 40 %; label "polygon 31" |
| a2-s5 · "whole" · 3.60 | chip "WHOLE CITY" |
| a2-s5 · "sirens" · 5.76 | ring shows in its dark state |
| a2-s5 · "quiet." · 6.26 | chip "NO SIREN" replaces WHOLE CITY |
| a2-s6 · "six" · 2.42 | flashback: ring to the 5:11 state twice (0.3 s on, 0.3 s off), back to dark; chip "6 MIN EARLIER" |
| a2-s6 · "media" · 4.50 | chip out; top-right source line hides (the cite card carries it); cite card in, line 1 "the media continued to report on storms" |
| a2-s6 · "passing" · 8.22 | line 2 "said to be passing to the north"; arrow north starts drawing |
| a2-s6 · "north." · 8.78 | line 3 "and missing Joplin, or moving away from the City." |
| a2-s6 · "Carl" · 12.68 | label "Webb City · Carl Junction" |
| a2-s6 · "How" · 14.20 | hold with drift; exit: fade-through to the g-a2-lead-time ground over the last 0.6 s of a2-s6 (host end = a2-s6 end) |

Cite card lines quote E12 verbatim; the first word stays lowercase because the sentence is cut mid-sentence in the source.

## 6 to 8
As `references/mg-brief-template.md` §6 (contract), §7 (tools), §7a (done line, all seven), §8 (receipt). File
`compositions/g-a2-countdown.html`, timeline `window.__timelines["g-a2-countdown"]`, root id `a2cd-root`.
Before the gates, send the clock card alone at full size for a read (g-a2-radar copies it).
