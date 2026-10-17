# Act a3 graphics list (ep-joplin-2011, "Homes with nothing underneath")

Source: `edit_script.md` A3 Picture lines (A3-S1 to A3-S11; A3-S2 is cut). Numbers: `research/facts.md` rows. Cues: `audio/<seg>.words.json`
(seconds from the start of that segment's wav). Briefs: one `<comp-id>.md` per row below, on `references/mg-brief-template.md`.

**Cue clock (every brief):** comp-local t = (data-start of the `nx-a3-sX` narration element in index.html) − (host data-start) + word time.
The orchestrator mounts the hosts, so the builder reads both data-starts from index.html.

## Open items (left out of every drawing until the orchestrator confirms them)
| Item | Where it would go | Why open |
|---|---|---|
| "1 crawl space" (the 27th EF-4 survivor's place) | g-a3-tally | not a facts.md row (only in factcheck-A1-A3); 27 − 11 − 15 = 1 is computed from H13/H14, its place is not |
| 1,600 likes, "1 year ago (edited)" on the step-dad comment | g-a3-comment | from `research/comments-for-writer.md` line 19, not facts.md |
| House foundation "crawl space" | g-a3-house-section | the Picture line says crawl space; no facts.md row says what non-basement homes stood on |
| Location of the early-1980s ranch-home neighborhood | g-a3-map-ranch (pocket layer BLOCKED) | H15 gives no place |
| Per-complex split of the 12, the three complexes' places, which one is Somerset, Somerset's storey count | g-a3-apartments | H19/H20 give none |
| Source figure for residential death positions on the map | g-a3-map-homes, g-a3-apartments | no facts.md row cites a NIST location figure; without one the dot layer is labelled "Schematic · not to scale" |

## Compositions
| comp id | segments | what it shows | DEEP/STANDARD | exemplar | cue span s |
|---|---|---|---|---|---|
| g-a3-house-section | A3-S1 (first part) | BASE of the house family: one-story house cross-section, figure in the middle bathroom, dashed empty basement ghost, chip "8 IN 10: NO BASEMENT", source line | DEEP (Opus) | `episodes/ep8-krakatau-seabed/compositions/g-slope.html` (datum cross-section), `library/inhouse/radar-beam.html` | a3-s1 "For" 0.00 → "to." 9.58 + 0.8 |
| g-a3-map-homes | A3-S1 tail, A3-S3 | master map (base `g-master-map`): scan finds no shelter, chip "NO PUBLIC SHELTER"; then push into the residential area, 59 dots in 51 house outlines, chip "59 LOST IN HOUSES", running label | DEEP (Opus) | base `g-master-map`; pattern `episodes/ep-enderlin-2025/compositions/g-master-map-a3.html` | a3-s1 "to." 9.58 + 0.8 → a3-s3 "Didn't" 8.98 |
| g-a3-apartments | A3-S4 (after the NIST photo) | master map: 3 apartment outlines, 12 dots, chip "12 IN APARTMENTS"; fade-through to a drawn Somerset staircase, three figures under it | DEEP (Opus) | base `g-master-map`; `g-slope.html` for the drawing | a3-s4 "every" 7.96 → "it?" 20.48 + 0.6 |
| g-a3-comment | A3-S5 (opening) | comment card, verbatim step-dad comment | STANDARD (Sonnet) | same base as the A1-S3 comment card (a1 brief); else `library/inhouse/quote-card.html` | a3-s5 "I" 0.48 → "Of" 5.78 |
| g-a3-tally | A3-S5 | 27 survivor pips sort: 11 below a grade line (basement), 15 into closet 3 / hallway 5 / bathroom 7, 1 grey unlabelled; chip "27 SURVIVORS" | STANDARD (Sonnet) | `library/inhouse/numbers-rollup.html`, official `stagger-lattice` | a3-s5 "Of" 5.78 → "up?" 17.16 + 0.8 |
| g-a3-house-joints | A3-S6 (after the NIST photo) | the house base explodes at its joints: roof lifts off the walls, walls lift off the floor, four joint rings; chip "THE JOINTS GAVE" | DEEP (Opus) | `g-a3-house-section` (base), `library/inhouse/moves/demo.html` | a3-s6 "mostly" 2.60 → "floor." 6.90 + 1.0 |
| g-a3-shelter-chip | A3-S7 | overlay over the in-home-shelter photo/clip: chip "IN-HOME SHELTERS HELD", source line | STANDARD (Sonnet) | snippets `popup-chip` + `source-label` (`library/inhouse/snippets/usage-examples.html`), `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` | a3-s7 "shelter" 1.82 → "it." 5.82 + 0.8 |
| g-a3-paul-chip | A3-S8 | overlay over Paul full frame: chip "71 LOST AT HOME", source chip | STANDARD (Sonnet) | snippets `popup-chip` + `source-label` | a3-s8 "71" 1.10 → "three." 6.04 + 0.4 |
| g-a3-stair | A3-S9 | the house base with a lit, empty basement and stair; the house above comes down, the basement stays; chip "2 OF 3 NOT DOWN THERE", source chip | STANDARD (Sonnet, on the Opus base) | `g-a3-house-section` (base) | a3-s9 "At" 0.00 → "help?" 10.44 + 0.8 |
| g-a3-map-ranch | A3-S10 (second sentence), A3-S11 | master map: ranch-home pocket lights with no dots, chip "BASEMENTS HELD"; under the counter, the 20th Street strip glows, then its label | DEEP (Opus) | base `g-master-map`; `g-master-map-a3.html` pattern | a3-s10 "And" 5.10 → a3-s11 "was." 6.08 + 1.0 |
| g-a3-counter | A3-S11 | BASE of the toll counter (visits 2 and 3 in a4, a5 reuse it): glass card top right, "INSIDE A BUILDING 71 of 135" over "BELOW GROUND / NONE FOUND", source line | STANDARD (Sonnet) | `library/inhouse/examples/joplin-stat-panel.html`, `episodes/ep-nepal-floods-2026/compositions/g-toll-counter.html` | a3-s11 "Most" 0.00 → "cover," 4.20 + 0.7 |

DEEP 5, STANDARD 6. Shared bases: `g-master-map` (episode base, owned by the brief that first draws it, I1 or A1; the three a3 map comps copy its `<!--BASEMAP:g-master-map-->` block verbatim, never redraw it); `g-a3-house-section` (a3 house base, read full-size before g-a3-house-joints and g-a3-stair are built); `g-counter` base = g-a3-counter.

## Not comps (listed so nothing is missed)
- NIST photo credit lines under the A3-S4, A3-S6 and A3-S7 photographs: the `source-label` snippet, mounted by the orchestrator once sourcing picks the figure (text is the photo's own credit).
- Clips named in the Picture lines (flattened houses A3-S3 from "Didn't" 8.98; apartments A3-S4 0.00 to 7.96; survivor after A3-S5; house pulled apart A3-S6; shelter A3-S7; basement survivor A3-S10 0.00 to 5.10): footage, sourcing in parallel.
- Book ad: `config.yaml channel.cta`, not drawn.
