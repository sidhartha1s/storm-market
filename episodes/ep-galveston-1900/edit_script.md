# ep-galveston-1900 · edit_script.md (TTS segment format)

Status: DRAFT 1, hook + hook tail + intro only (phase 3 owner gate). Acts below are briefs, no prose yet.
Angle: `episodes/ep-galveston-1900/angle.md` (owner lock, devq save 26 Oct 26 02:09:38, `t_galveston` "a3" + note).
Research: `episodes/ep-galveston-1900/research/` (sources-cline.md, sources-cuba.md, teardowns.md, footage-inventory.md).

## Packaging (drafted after the lock, per `references/packaging-rules.md`)
- Title: **Galveston 1900: He Said It Was Safe. It Was Not.** (48 characters; Name + Year in the first 16; `title_fre.py` 101.9)
- Thumbnail: school A (Name + Year documentary card): the Library of Congress ruins photograph, place name in frame, one fact line in two words ("ABSURD DELUSION"), with a Field Notes Paul variant for Test and Compare. Not drafted this round.
- Promise the hook must say aloud: the city's own weatherman wrote that a storm seriously damaging Galveston was "an absurd delusion"; nine years later the storm came.

## Runtime and structure
- Target: about 20 to 24 minutes (to be confirmed by the owner; no word budget run yet: needs two probe TTS segments, and this round has no TTS).
- Architecture: Detective (who told Galveston it was safe, and who said otherwise).
- Dominant question: if the warnings existed, why did Galveston go to bed on Friday night thinking it was fine?

## Hook sound (reasoned, DESIGN.md "Cold-open hook contract")
No siren: this is not a tornado-siren story, and 1900 had none. The hook runs on wind and surf rising under Paul's line, a telegraph-key click on the 1891 newspaper reveal, and a low swell into the ruins film. No archive audio (none exists for 1900).

## Paul on camera (planned, NOT generated this round; 6 full-frame clips of at most about 26 words each)
1. P1 = H1-S1, frame one, the hook sentence only.
2. P2 = end of A1 (the 1891 article turns from opinion into the city's belief).
3. P3 = end of A2 (Havana says Gulf, Washington says recurve).
4. P4 = the `cta-hinge` tease, last line before the book ad.
5. P5 = A5 turn (Cline's own report against his later story).
6. P6 = editor's choice, held for the close.
Budget per `references/mg-quickref.md` "Paul on screen": 6 clips x 15 credits = 90 credits, one take each. Owner sign-off needed before any clip runs.

## CTA hinge (DESIGN.md "CTA contract", `config.yaml channel.cta.window` 0.40 to 0.60)
- Segment before: last A3 segment, ending on the tease (P4, at most 25 words): the telegram Isaac Cline sent Washington at half past three on Saturday afternoon.
- Segment after: A4-S1 opens with the telegram's words as the payoff.
- Estimated position: about 10:30 of about 22:00 (0.48).

## Loop registry (plant / pay)
| Loop | Planted | Paid |
|---|---|---|
| E1 episode loop: why did Galveston feel safe on Friday night? | H1 | A6 close |
| L-intro (set by the writer below) | intro | A1 |
| cta-hinge: what Cline told Washington at three thirty | A3 last segment | A4-S1 |

## H · Hook (0:00)
(writer: hook segments here)

## HT · Hook tail
(writer: hook tail segments here)

## I · Intro
(writer: intro segments here)

## Act briefs (text only, written before prose; `references/script-scaling.md` "Act brief")
- **A1 · "An absurd delusion" (1891).** Purpose: show the belief was given to the city by its expert, in print. Question: why would a weatherman say that? Reveal: his reasoning (the shallow shelf and the low land to the north would spread the water). Visual: the 16 July 1891 Galveston Daily News page, the island elevation map (highest point about 8.7 ft). Exit hook: nine years later, the same man was in charge of warning the city.
- **A2 · Havana.** Purpose: the people who read the storm right. Belen Observatory, Father Benito Vines, Father Lorenzo Gangoiti; the US Weather Bureau moves its warning centre to Cuba after the war; NOAA: the Bureau "decreed that only its forecasts would be carried over the telegraph". Exit hook: Havana says northwest into the Gulf; Washington says it will turn.
- **A3 · The turn that never came (4 to 7 September).** Meteorology layer: why storms near that latitude usually recurve, and why this one did not. The steamer Louisiana passes through the centre in the Gulf on 6 September. Warnings from Washington on 4 to 8 September; storm warning at Galveston on the 7th. Ends on the `cta-hinge` tease.
- **CTA** (book ad, `config.yaml channel.cta`).
- **A4 · Saturday (8 September).** Payoff: "Gulf rising, water covers streets of about half of city." Cline drives to the Gulf and times the swells; barometer falls to twenty-eight point four eight inches; Cora Cline lost.
- **A5 · Two stories.** The Library of Congress films of the ruins. At least six thousand lives lost in Cline's own count (eight thousand most cited; six to twelve thousand range). Cline's own report against his later memoir; what Larson disputes. Cuban press criticism of the Bureau in October and November 1900.
- **A6 · After.** The seawall and the grade raising (to be researched and verified before writing). Close: answer E1, dated forward window, signature line.
