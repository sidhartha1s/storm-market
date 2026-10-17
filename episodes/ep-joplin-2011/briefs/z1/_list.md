# Act z1 graphics list (ep-joplin-2011, "Close")

Written 17 Oct 26 from `edit_script.md` Z1-S1 and Z1-S3 Picture lines, `research/facts.md`, `audio/z1-s1.words.json`.
Briefs follow `references/mg-brief-template.md`; every builder also gets `references/mg-quickref.md` and `library/inhouse/snippets/tokens.md`.
Builders: DEEP = Opus 5.5 high, STANDARD = Sonnet 5.5 high (CLAUDE.md "Chain of command").

## Open numbers and open items (left out of every drawing until a facts.md row or the orchestrator supplies them)
| # | Number / item | Wanted by | Why it is open |
|---|---|---|---|
| Z1 | "2027" in chip "2027 BUILDING CODE" and source line "2027 International Building Code · ICC store page, Oct 2026" | g-z1-board | No facts.md row. edit_script Z1-S3 cites the ICC store page and carries its own `[verify]` (re-check the week of render). The chip slot stays empty and no 2027 text is drawn. |
| Z2 | Every z1-s3 cue time and the host length | g-z1-board | `audio/z1-s3.wav` and `z1-s3.words.json` do not exist (audio/ holds z1-s1 only, 17 Oct 26). The brief names the cue words from the script; times are filled from words.json once Z1-S3 is voiced. |

## Bases reused from other acts (same base composition, never redrawn)
- SIREN STRIP + warnings tally: the finished state of `g-a1-strip-warnings` (`briefs/a1/`), px table in `g-a1-strip-sirens.md` §2 and §3.
- MASTER MAP: the BASEMAP block in `g-intro-map` (T1-S2), the DOT LAYER of `g-intro-map-dots`, the T1-S3 push values in `g-intro-map.md` §3, the state `g-a6-map135` opens on (`briefs/intro/`, `briefs/a6/`).
- Recommendation board: the A5-S11 base (`briefs/a5/g-a5-recs-board.md`) in the half-lit tile 7 state of `g-a6-board-half` (`briefs/a6/`).

## Comps
Cue notation as `briefs/intro/_list.md`: `z1-s1 "inside," 12.98` = that word's `start` in `audio/z1-s1.words.json`. Comp-local time = (`nx-z1-s1` data-start − host data-start) + word time.

| comp id | segments | what it shows | DEEP/STANDARD | exemplar | cue span s |
|---|---|---|---|---|---|
| g-z1-strip | z1-s1 | SIREN STRIP one last time: grey Monday ticks dim, 4 red marks pulse; the amber warnings tally below, separate; chip ONCE A YEAR SINCE 2007 · NIST FINDING 31 | STANDARD | base: `g-a1-strip-warnings` end state; `library/inhouse/split-shared-scale.html` (two sets that never merge) | z1-s1 "Joplin's" 0.00 to "That" 10.06 |
| g-z1-map | z1-s1 | MASTER MAP, the [RS]: 135 inside dots stamp in, chip 135 INDOORS; push onto the empty below-ground line, chip NONE FOUND BELOW GROUND; chip 8 IN 10: NO BASEMENT; pull back out over the whole city | DEEP | base: master map + dot layer + T1-S3 push (`g-intro-map`, `g-intro-map-dots`, `g-a6-map135`) | z1-s1 "That" 10.06 to wav end 22.92 |
| g-z1-board | z1-s3 | Recommendation board, tile 7 lifted and half lit (SCHOOLS lit; APARTMENTS, STORES, ASSEMBLY grey); STORES and APARTMENTS pulse on the voice; 2027 chip held (Z1) | STANDARD | base: `g-a6-board-half` held state | z1-s3 start to z1-s3 wav end (times open, Z2) |

Totals: 3 comps, 1 DEEP (Opus 5.5 high), 2 STANDARD (Sonnet 5.5 high). Build order: none inside z1; each copies a base built in an earlier act, so each waits for its base's frame read.

## Every z1 Picture-line graphic, and where it lives
| seg | graphic on the Picture line | comp |
|---|---|---|
| z1-s1 | calendar strip one last time: grey Monday ticks, four red marks | g-z1-strip |
| z1-s1 | the warnings strip below it, separate | g-z1-strip |
| z1-s1 | chip "ONCE A YEAR SINCE 2007 · NIST FINDING 31" | g-z1-strip |
| z1-s1 | [RS] master map, all 135 dots, the empty below-ground line | g-z1-map |
| z1-s1 | chips "135 INDOORS", "NONE FOUND BELOW GROUND", "8 IN 10: NO BASEMENT" | g-z1-map |
| z1-s1 | source lines Finding 40, Finding 46, Finding 20 | g-z1-map |
| z1-s3 | recommendation board, tile 7 half lit | g-z1-board |
| z1-s3 | chip "2027 BUILDING CODE"; source line "2027 International Building Code · ICC store page, Oct 2026" | g-z1-board (HELD, Z1) |

## Not graphics in z1 (named so builders know what sits under or after a comp)
- The chapter blackout from a6 into z1 is hand-placed before g-z1-strip (it follows `g-a6-map135`).
- z1-s1 last sentence ("But" 15.88 to "county." 22.26): a few seconds of real Joplin sound (siren ambience or the CCTV clip's room tone), editor's pick. Audio only; no picture changes for it.
- After z1-s3: the signature line, Paul on camera full frame (edit_script). No graphic over it.

## Ambiguous in the Picture lines
1. **Last clause of z1-s1** ("there wasn't a single public shelter anywhere in the city or the county", 18.66 to 22.26, H3/H4) has no chip or label on the Picture line. g-z1-map carries it with motion only (pull-out to the whole city, city outline brightens on "city" 21.36). If the orchestrator wants text, `g-intro-nobasement`'s "no community shelters or safe rooms" label (H3) is the existing wording; it would replace chip 3, never stack with it.
2. **"NONE FOUND BELOW GROUND" is never spoken in z1.** The voice says "right where you'd have gone"; the chip lands on "gone." 14.76 with the push onto the line. Whisper heard "right? Where" (13.92, 14.32) for the script's "right where": listen to the wav; cues use the words as written.
3. **Finding 46 source line** reworded from "no evidence any were underground" to "no evidence any of those killed were underground · NIST Finding 46" so it never reads as "no one was below ground" (facts.md NOTE under B49: the Macadoodles cellar had 12 people below ground who all survived).
4. **135 twice in one frame**: chip "135 INDOORS" with source line "135 of 155 impact-related" is the pairing `g-intro-hook` already uses (chip + its base). If `overlap_check` reports dup-fact, declare `data-repeat-ok` on the source-line leaf after a frame read.
5. **Copied map labels**: the copied lit state drops the "0" on the line, the rail card and the "154 placed" label, so Finding 46 and 135 each show once.
6. **Signature line**: edit_script says Paul full frame; DESIGN.md "Signature closing footnote" says it plays over the title card. Not a z1 Picture-line graphic; the orchestrator picks before the mount.
7. **Repeat of the master map**: `g-a6-map135` shows it about 30 s before g-z1-map. If the close is not inside the last 90 s of the episode, the mount needs `data-callback="close: the case board one last time"`. The strip and board repeats need the same check.
