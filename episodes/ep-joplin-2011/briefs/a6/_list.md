# Act a6 graphics list (ep-joplin-2011, "What changed and what did not")

Written 17 Oct 26 from `edit_script.md` A6-S1 to A6-S7 Picture lines, `research/facts.md`, `audio/a6-s*.words.json`.
Briefs follow `references/mg-brief-template.md`; every builder also gets `references/mg-quickref.md` and `library/inhouse/snippets/tokens.md`.

## Open numbers (not in facts.md, so left out of every drawing until a facts.md row exists)
| # | Number / text | Wanted by | Where the script got it |
|---|---|---|---|
| N1 | "14" school safe rooms | g-a6-saferoom chip "14 SAFE ROOMS" | FEMA case study (edit_script A6-S2 Rows), no facts.md row |
| N2 | "250 MPH" school safe-room rating | g-a6-saferoom chip "250 MPH" | same FEMA case study |
| N3 | "Jul 30, 2024" | g-a6-saferoom source line | same FEMA case study |
| N4 | "RISK CATEGORY III, IV" | g-a6-usmap ASCE chip | not in R12 |
| N5 | The highest tornado zone outline / which 22 states | g-a6-usmap zone fill | R13 gives only the count "parts of 22 states"; no published figure in facts.md to trace |
| N6 | "IBC Section 423", "423.4", "2024 IBC", "Feb 2023" (FEMA Recovery Advisory 1), "Jul 2024" (NIST news) | g-a6-usmap, g-a6-board-half source lines | not in facts.md Sources |
| N7 | Mercy "250 mph" window system, "2015" | g-a6-mercy card and chip (all its text) | mercy.net, no facts.md row |
| N8 | "2018", "NIST TN 2008" | g-a6-siren chips | NIST TN 2008, no facts.md row |
| N9 | Like counts 3,600 / 28 / 482 | the three comment cards | verbatim in `research/comment-beats.json`, not facts.md. Orchestrator may rule comment-beats.json the record for comment cards and release them. The digits inside two quotes ("15:15", "250mph") are verbatim comment text, not claims, and are kept in the quotes under that same ruling |
| N10 | Text "located in tornado hazard areas" (not a number) | g-a6-doc-rec7 underline | past the 50-word R3 quote; check on the page render |

## Bases reused from other acts (same base composition, never redrawn; ids per that act's `_list.md`)
- Recommendation board: first built for A5-S11 (16 grey tiles, chip "16 RECOMMENDATIONS"), `briefs/a5/`.
- Document page with underline: first used A1-S6 (NIST page, Finding 31), `briefs/a1/`.
- Comment card: first used A1-S3, `briefs/a1/`.
- Siren icon: I1-S2 (25 icons from NIST Fig. 4-2), `briefs/intro/`.
- Master map of Joplin, 135-dot state: T1-S2 first appearance, lit in I1-S9, `briefs/intro/`.

## Comps
Cue span = segment-local seconds from the named words.json (`s3 20.54` = a6-s3 word start 20.54). Host-local time = that segment's narration `data-start` in index.html + word start − host `data-start`.

| comp id | segments | what it shows | DEEP/STANDARD | exemplar | cue span s |
|---|---|---|---|---|---|
| g-a6-board-r7 | a6-s1 | Recommendation board returns, tile 7 lifts out and zooms through to the page | DEEP | base: A5 board; `library/official` stagger-cascade (grid) | s1 0.00 to s1 6.30 |
| g-a6-doc-rec7 | a6-s1 | NIST page, Recommendation 7, four occupancies underlined on the voice; chip "RECOMMENDATION 7"; source line | STANDARD | base: A1-S6 doc page; `library/inhouse/bulletin-typewriter.html`, official hw-underline | s1 6.30 to s1 17.80 |
| g-a6-cmt-thriving | a6-s2 | Comment card "By the way, Joplin is thriving..." over the safe-room clip (CLIP NEEDED) | STANDARD | base: A1-S3 comment card | s2 0.46 to s2 5.92 |
| g-a6-saferoom | a6-s2 | Our schematic of a school safe room, wind held off; chip "NEIGHBORS WITH NOWHERE ELSE MAY USE THEM · FEMA" (N1, N2 chips held) | DEEP | `references/editing-patterns/ep2-met-explainer.html` | s2 5.92 to s2 17.80 |
| g-a6-usmap | a6-s3 | US map; ASCE 7-22 chip; safe-room inset (from g-a6-saferoom) with capacity and walking path; chip "22 STATES · NEW SCHOOLS"; zone fill held (N5) | DEEP | `library/inhouse/master-map-us-canada.html` | s3 0.00 to s3 20.54 |
| g-a6-cmt-mandatory | a6-s3, a6-s4 | Comment card "I wonder why commercial buildings..." on the question it asks | STANDARD | base: A1-S3 comment card | s3 20.54 to s4 1.68 |
| g-a6-board-half | a6-s4 | Board, tile 7 lifted and half lit: Schools lit, Apartments and Stores grey; chip "STORES, APARTMENTS: NOTHING LISTED" | DEEP | base: A5 board (state of g-a6-board-r7) | s4 1.68 to s4 8.66 |
| g-a6-cmt-nurse | a6-s4, a6-s5 | Comment card "Asked a nurse why the windows..." over the West Tower photo | STANDARD | base: A1-S3 comment card | s4 8.66 to s5 3.80 |
| g-a6-mercy | a6-s5 | Glass text card with Mercy's own words, then chip "DESIGNED FOR 250 MPH"; ALL TEXT HELD (N7) | STANDARD | `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` | s5 3.80 to s5 8.22 |
| g-a6-siren | a6-s5, a6-s6 | Siren icon with pulsing arcs; chip "NO NATIONAL STANDARD · 2011" (N8 chips held) | STANDARD | base: I1-S2 siren icon | s5 9.86 to s6 14.56 |
| g-a6-doc-nwsrec2 | a6-s6 | NWS page, Recommendation 2, two phrases underlined; chip "STRONG AND VIOLENT TORNADOES · NWS REC. 2"; source line | STANDARD | base: A1-S6 doc page | s6 14.56 to s6 24.16 |
| g-a6-empty | a6-s7 | Chip "EMPTY THAT EVENING" over the NIST Joplin High School photograph | STANDARD | `library/inhouse/snippets/cards.css` `.glasscard` | s7 9.76 to s7 9.76 + 2.6 |
| g-a6-map135 | a6-s7 | Master map, 135 dots inside buildings; chip "MOST WERE INDOORS" | DEEP | base: master map, I1-S9 state | after the CCTV clip, 5.0 s (no narration) |

Totals: 13 comps, 5 DEEP (Opus 5.5 high), 8 STANDARD (Sonnet 5.5 high). Build order: g-a6-board-r7 before g-a6-board-half (same state); g-a6-saferoom before g-a6-usmap (the inset is its drawing).

## Not graphics in a6 (footage, named so overlays know what sits under them)
- s1 17.80 to end: NIST ground photograph of the Walmart refuge area (reused from A4, needs `data-callback`).
- s2 0.46 to 5.92: CLIP NEEDED, moving footage inside a Joplin school safe room (under g-a6-cmt-thriving).
- s3 20.54 to s4 1.68: footage under g-a6-cmt-mandatory, not named by the script (editor picks; a Joplin store or apartment street).
- s4 8.66 to s5 end: NIST photograph of the West Tower fifth floor (reused from A5-S5, needs `data-callback`).
- s7 0.00 to the CCTV cut: NIST ground photograph of Joplin High School; then the CCTV clip (YouTube 64covicCcIY), its own sound, school to be confirmed before any caption names it.

## Ambiguous in the Picture lines
1. The chapter card ticks Recommendations 7, 8 and 13, but facts.md ties an adoption to a recommendation number only for 7 (R14) and 9 (R18). a6 lights only tile 7; the A5 and Z1 board owners should know.
2. A6-S4 puts the comment card first, but the answer starts at s4 1.68 ("nothing"). The card is moved onto the question it asks (s3 20.54 "What about a new store or apartment building?"), so g-a6-usmap exits there.
3. Chip "MINIMUM SIZE · MAX WALKING DISTANCE": R16 says "minimum shelter capacity and maximum travel distance". Kept as written; the reviewer may prefer "MINIMUM CAPACITY".
4. Chip "ASCE 7-22 · ... · TORNADO-PRONE REGION": R12 confirms ASCE 7-22 and tornado loads, not the term "tornado-prone region".
5. A6-S5: card and chip both say 250 MPH; sequenced so only one shows at a time (g-a6-mercy).
6. A6-S6's one source line covers two comps; split as "NIST Finding 39" (g-a6-siren) and "NWS Assessment, Recommendation 2" (g-a6-doc-nwsrec2).
7. A6-S7's master map is about 30 s before Z1-S1's master map: Z1's mount needs `data-callback`.
8. Whisper heard "cupboard" (s3 12.64, script "code") and "veteran" (s6 8.94, script "federal"): listen to both wavs; cues use the words as written in words.json.
