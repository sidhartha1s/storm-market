# A1 · Sirens: belief against record · motion-graphics list (briefs written 17 Oct 26)

Source of every Picture line: `episodes/ep-joplin-2011/edit_script.md` A1-S1 to A1-S11. Numbers: `research/facts.md`
rows only. Cues: `audio/a1-s*.words.json`. Builders: DEEP = Opus 5.5 high, STANDARD = Sonnet 5.5 high (CLAUDE.md
"Chain of command"). Every builder's brief carries `references/mg-quickref.md` and `references/mg-brief-template.md` §6 to §8.

## Conventions (every brief in this folder uses them)
- **Cue notation** `a1-s4 "three" 5.18` = that word's `start` in `audio/a1-s4.words.json`, in seconds from the start of that
  segment's wav. Words are written the way whisper spelled them (`a1-s2` "Theatre", "Willy"; digits such as "18", "2007").
  Comp-local time = (`nx-a1-sN` data-start − host data-start) + the word's time. The data-starts come from the narration
  mounts in `index.html`. Put the spoken cue in a comment beside each tween (`/* THREE a1-s4 5.18 */`).
- **Shared bases, never redrawn.** The brief of a base's first use owns it. Copy the base file and retune it; never rebuild it:
  - MASTER MAP: the Joplin case-board map, first built for T1-S2 (intro briefs). It owns all geography: streets,
    building outlines (Stained Glass Theater included), the city outline, the 25 siren icons from I1-S2 (NIST Fig. 4-2).
    A1 map comps add layers to a copy and add no geography.
  - SIREN RING: the ring drawn over the city when the sirens sound. Its style and radius are set in `briefs/a2` `g-a2-countdown`
    (the 5:11 ring). `g-a1-second-siren` copies it. One Opus builder builds `g-a1-theater-map`, `g-a1-second-siren` and
    the a2 map comps, all on the same base.
  - SIREN STRIP: the 2007 to 2011 calendar strip, first used I1-S2/I1-S3 (intro). A1 uses it twice (`g-a1-strip-sirens`,
    `g-a1-strip-warnings`). Its geometry table is in `g-a1-strip-sirens.md` §2 and §3. If the intro brief fixes different px,
    the intro's table wins and both a1 strip comps follow it. Either way the two acts must use one table, and the orchestrator checks this.
  - PAGE UNDERLINE: a public-domain report page with a phrase underlined on the voice, first used I1-S5 (intro). The a1
    copies are `g-a1-gutter`, `g-a1-numb` (page half), `g-a1-finding31` and `g-a1-bubble-page`. Exemplar `library/official/vox-annotate.html`, the same one a2 uses.
  - COMMENT CARD: the viewer-comment card. **Its first use is A1-S3 and this folder owns it** (`g-a1-numb.md` §3 defines it).
    It is copied in a1 (`g-a1-quote-58`) and in a2, a4 and a5. Send the card alone for a full-size read before any copy is made (template 7a).
- **Approximate counts keep their "about"** where the source says approximately: S4 "approximately 52 times per year", so the
  chip reads "ABOUT 52 TESTS A YEAR" (the Picture line wrote "52 TESTS A YEAR"). The orchestrator may restore the
  Picture-line text: it is a writer's line, not the owner's.
- **Source lines** inside comps sit bottom-left (x 96, baseline ≤ 1026), never in the presenter corner (x ≥ 1600, y ≥ 680).
- **Photo credit lines** under the NIST and NOAA stills are not comps. "(credit line checked)" on the A1-S1 and A1-S2
  Picture lines means sourcing checked the caption credit (NIST's own, not GeoEye). If a credit shows on screen, the
  orchestrator mounts it as an index `.srclab` from the file's `provenance.csv` row.
- **Chips** are glass chips (`references/editing-patterns/ep6-glasscard-popfig-bfmg.html`), drawn inside the comp of
  their beat, never a red popfig over a card or map (`mg-quickref` "Palette and surfaces").

## Open numbers and open claims (left out of every drawing until a facts.md row carries them)
1. **Comment like counts**: 3,000 (RODALCO2007, `angle.md` only) and 824 ("The sad part…", `research/comments-for-writer.md`
   only). Neither is in facts.md. The cards keep an empty likes slot.
2. **"NIST Interview 58"** (A1-S9): no facts.md row holds the interview number or the quote text. The script cites
   factcheck-A1-A3, which is not in this worktree. The attribution is drawn as "a Joplin native · NIST interview" with no
   number. The quote text is an open claim: the orchestrator confirms it before the build.
3. **Stained Glass Theater position**: it belongs to the MASTER MAP base. If the base has no theater outline, the only
   location on record is the 1318 W 26th St geocode in `media/candidates/a1/candidates.md`, which is not a facts.md row.
4. **Dates of the 18 tornado warnings** (NIST Fig. 4-3): facts.md has only the counts (S10, S12, S13) and one date (10 May 2008,
   S13). So the warnings row is an outcome tally, not a dated strip, and it does not carry the Picture line's
   "last five years zoom in" as a camera zoom (see `g-a1-strip-warnings.md` §0).
5. **Positions of the 182 tornadoes** within 80 miles: facts.md has only the count (S37). Dot positions are illustrative, and the source line says so.

## Comps

| comp id | segments | what it shows | DEEP/STANDARD | exemplar | cue span s |
|---|---|---|---|---|---|
| g-a1-gutter | a1-s1 | NWS Assessment page, Finding 2b: three resident phrases underlined on the voice; source line | STANDARD | PAGE UNDERLINE base; `library/official/vox-annotate.html` | a1-s1 "Here's" 0.00 to "attention." 13.04 (host 0.00 to 14.04) |
| g-a1-quote-120 | a1-s2 | Glass quote card (NIST Interview 120, the actor) over the NOAA aerial of the 26th St site | STANDARD | `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (`.quotecard.glasscard`); `library/inhouse/quote-card.html` (phrase reveal) | a1-s2 "One" 0.00 to "Three" 10.26 |
| g-a1-theater-map | a1-s2 | MASTER MAP copy: short push to the Stained Glass Theater, 3 markers light; chip 3 LOST HERE; source line | DEEP | MASTER MAP base; `references/editing-patterns/ep3-map-route-fit.html` | a1-s2 "Three" 10.26 to wav end 15.96 |
| g-a1-numb | a1-s3 | COMMENT CARD (RODALCO2007, its first and only card) + NWS Preface page with "desensitized or complacent" underlined; chip NUMB TO SIRENS; source line | STANDARD | COMMENT CARD base (defined here); PAGE UNDERLINE base | a1-s3 "You've" 0.64 to "off?" 17.14 (host 0.00 to 17.92) |
| g-a1-strip-sirens | a1-s4 | SIREN STRIP: 229 grey Monday test ticks 2007 to May 2011, 3 red soundings with labels, the empty gap, the 22 May 2011 mark; chips ABOUT 52 TESTS A YEAR, 3 REAL SOUNDINGS; source line | DEEP | SIREN STRIP base; `library/inhouse/stat-timeline.html`, `library/inhouse/event-timeline.html` | a1-s4 "In" 0.00 to "2011." 13.68 (host 0.00 to 14.64) |
| g-a1-finding31 | a1-s6 | NIST Executive Summary page, Finding 31 sentence underlined in three strokes; chip NO FALSE-ALARM PROBLEM; source line | STANDARD | PAGE UNDERLINE base; `library/official/vox-annotate.html` | a1-s6 "I" 0.00 to "from?" 12.14 (host 0.00 to 12.96) |
| g-a1-strip-warnings | a1-s7, a1-s8 | SIREN STRIP copy (finished state) above a separate amber tally of 18 warnings, 4 verified, then a recount of 12 warnings, 1 verified; chips 14 OF 18 · NO TORNADO, 11 OF 12, TWO DIFFERENT COUNTS; name card; source lines | DEEP | SIREN STRIP base; `library/inhouse/split-shared-scale.html` (two sets never merged) | a1-s7 "They" 0.00 to a1-s8 "evening." 16.56 (host to a1-s8 wav end 17.36) |
| g-a1-quote-58 | a1-s9 | Beige cite card (Joplin native, TV said north of town), COMMENT CARD copy ("The sad part…"), then the NIST media sentence on the cite card; chip TRACK: NORTH OF TOWN | STANDARD | `library/inhouse/quote-card.html`; COMMENT CARD base | a1-s9 "Then," 0.00 to "that?" 11.14 (host 0.00 to 11.72) |
| g-a1-bubble-page | a1-s10 | NWS Assessment page, Finding 2b, "protective bubble" underlined; source line | STANDARD | PAGE UNDERLINE base | a1-s10 "A" 0.00 to "Since" 8.76 |
| g-a1-ring | a1-s10 | Regional map: Joplin's outline, the one 1971 dot inside, an 80-mile ring, 182 dots; rail chips 1 IN THE CITY, 182 WITHIN 80 MILES; source line | DEEP | `library/inhouse/master-map-us-canada.html` (Natural Earth states, public domain) | a1-s10 "Since" 8.76 to "strength." 18.50 (host 8.76 to 19.56) |
| g-a1-second-siren | a1-s11 | MASTER MAP copy: two siren rings, labelled First siren and Second siren, the second one pulsing | DEEP | MASTER MAP base + SIREN RING (`g-a2-countdown`) | a1-s11 "The" 0.50 to "meant." 5.18 (host 0.00 to 5.88) |

There are 11 comps: 5 DEEP and 6 STANDARD. One Opus builder takes `g-a1-strip-sirens` and `g-a1-strip-warnings` (one strip table). One Opus
builder takes the two master-map comps with the a2 map comps. `g-a1-ring` stands alone.

## Every A1 Picture-line graphic, and where it lives

| seg | graphic on the Picture line | comp |
|---|---|---|
| a1-s1 | NWS page Finding 2b, three lines underlined; source line | g-a1-gutter |
| a1-s2 | quote card + attribution over the theater picture | g-a1-quote-120 |
| a1-s2 | three markers on the theater outline on the master map; chip 3 LOST HERE | g-a1-theater-map |
| a1-s3 | RODALCO2007 comment card; NWS page "desensitized or complacent" underline; chip NUMB TO SIRENS; source line | g-a1-numb |
| a1-s4 | calendar strip 2007 to 2011, grey weekly ticks, three red marks with labels (plus the 22 May 2011 mark from the chapter card's Visual event, landing on "May"); chips 52 TESTS A YEAR, 3 REAL SOUNDINGS; source line | g-a1-strip-sirens |
| a1-s5 | Paul full frame, no chip | (no graphic) |
| a1-s6 | NIST page Finding 31 underline; chip NO FALSE-ALARM PROBLEM; source line | g-a1-finding31 |
| a1-s7 | second strip, different colour, 18 marks, 4 verified; chip 14 OF 18 · NO TORNADO; last five years: 12 marks, 1 verified; chip 11 OF 12; source line with 74.7 % | g-a1-strip-warnings |
| a1-s8 | both strips; name card over the gap; chip TWO DIFFERENT COUNTS; source lines Sec. 4.3.4, then Finding 44 · Sec. 4.7.3 | g-a1-strip-warnings |
| a1-s9 | quote card + attribution; comment card "The sad part…"; NIST sentence as on-screen text; chip TRACK: NORTH OF TOWN | g-a1-quote-58 |
| a1-s10 | NWS page "protective bubble" underline | g-a1-bubble-page |
| a1-s10 | 80-mile ring map, 182 dots, one city dot "May 5, 1971"; chips 1 IN THE CITY, 182 WITHIN 80 MILES; source line | g-a1-ring |
| a1-s11 | master map, two siren rings, the second pulsing | g-a1-second-siren |

Not graphics (sourced in parallel, named so the builder knows what sits under or beside a comp):
- a1-s1: the NIST ground photograph of a street in the path (`a1-s1_c3_nist-fig4-14-demolished-home.jpg` or c4) after `g-a1-gutter`.
- a1-s2: the NOAA NGS aerial crop `a1-s2_c1_noaa-ngs-aerial-26th-st-crop.jpg` under `g-a1-quote-120`. A still held over 6 s
  needs a slow push in index.html (sweep check 9).
- a1-s4: the civil-defense siren SFX, one second (index.html audio).
- a1-s5: Paul full frame (`ins-paul-*`).
- a1-s9: the live TV broadcast pull (FagzNHuI5JI) after `g-a1-quote-58`. It is still a GAP in `candidates.md`.
- Page images, mounted inside their comps: `a1-s1_c1_nws-p13-finding2b-quotes.jpg`, `a1-s3_c1_nws-p4-preface-desensitized.jpg`,
  `a1-s6_c1_nist-exec-summary-finding31.jpg`, `a1-s10_c1_nws-p13-protective-bubble.jpg` (all in `media/candidates/a1/`).

## Picture-line readings the orchestrator should confirm
- **A1-S1 photo:** the page carries all three quotes up to "attention." (word end 13.44, wav end 14.04). That leaves the
  NIST photo 0.6 s plus whatever gap the editor leaves before a1-s2. Either the gap opens, or the photo moves.
- **A1-S2 markers:** the Picture line puts the 3 markers on the master map. `candidates.md` offers them on the aerial
  instead. The brief follows the Picture line.
- **A1-S10 order:** the Picture line lists the page last, but the voice says "protective bubble" (5.14) before the ring
  numbers (8.76 on). The comps follow the voice: page first, then the map.
- **A1-S10 182:** NIST says 182 "within an 80-mile radius of the City". This brief reads that as including the 1971
  city tornado, so the map has 181 dots outside the outline and 1 inside, 182 in all.
