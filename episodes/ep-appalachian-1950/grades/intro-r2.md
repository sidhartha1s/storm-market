SCORE: 8/10 (confidence 70%)
HOOK SCORE: 8/10 (confidence 70%), H1-S1 to H1-S5

# Grade: ep-appalachian-1950, intro round 2 (whole opening: hook H1-S1 to H1-S5 + intro I1-S1 to I1-S4)
Grader: skeptic grader, fresh read (no earlier grade files opened), 26 Oct 26.
Read: `acts/intro.md` (graded text), `angle.md`, `edit_script.md` (spec, act outline, loop table; its hook/intro and loop rows are superseded and were ignored), `references/script-quickref.md`.
Working title to pay: "1950 Appalachian Storm: 2 Feet of Snow, 108 mph Wind".

Timing basis (measured, not estimated): 219 spoken words in total; a word-count script gives cumulative ends at 150 wpm of H1-S1 9.2 s, H1-S2 17.2 s, H1-S3 22.4 s, H1-S4 35.6 s, H1-S5 46.0 s, I1-S1 60.8 s, I1-S2 71.2 s, I1-S3 84.8 s, I1-S4 87.6 s. The opening runs about 1:28; the hook runs about 46 s.

## Verdict in one paragraph
The opening locks at the bar. Both title facts are said aloud by about 17 s: "a hundred eight miles an hour" in H1-S1 and "more than two feet of snow" in H1-S2, each sourced (PHI/JKL Newark gust, PBZ 27.4 in). The toll lands by about 20 s. The drop-in shape is real: "you", present tense, Newark, stakes before cause. H1-S4 hands over a belief (north is worse) and breaks it with the record. That is the strongest beat. The intro does its WHAT job (coast flooding, Pittsburgh's record, cold reaching Kentucky, a carried loop) and stays on the Claim. It loses points in three places. H1-S5 recaps the hook and ends on a soft decode-me phrase. I1-S1 and I1-S2 read as a coast/inland tour with no fresh question for about 25 s. The L4 exit promises a gust payoff that Act 1 must land on the same day and with a fair comparison.

## 1. Per-minute axes (1 to 5)
| Minute | New info | Curiosity | Stakes | Visual change | Payoff | Exit hook |
|---|---|---|---|---|---|---|
| 0:00 to 1:00 (H1-S1 to I1-S1) | 5 | 5 | 5 | 4 | 4 | 4 |
| 1:00 to 1:28 (I1-S2 to I1-S4) | 4 | 3 | 3 | 4 | 4 | 4 |
No two low minutes in a row. Minute 2 curiosity is the soft spot: "a long way south" is a thin tease, though it is paid about 8 s later.

## 2. Register ("a person talking to you"): 8/10
Strong: "You're in Newark", "You'd figure Buffalo...", "The number I didn't expect was down in Kentucky", "when I checked the city's November records". The first-person line earns its place with a present-day finding (the record still stands). Contractions are used throughout.
Three worst lines:
1. I1-S2: "On the inland side, Pittsburgh's snow went down as the city's biggest snowstorm on record." It reads like a report entry, and the superlative has no spoken unit or comparator.
2. I1-S1: "On the coast side of the storm, that wind drove the tide in until the New Jersey shore flooded." It reads like a report, and "On the X side" frames the intro as a tour.
3. H1-S5: "...and from where you're standing in Newark, there's no way to see how." It is soft and the viewer has to decode it: see how what?

## 3. Rule breaks (exact lines)
- **Summary tag / fact spent twice (soft), H1-S5:** "It's one storm bringing hurricane wind and deep snow on the same Saturday". H1-S2 already said this ("That's a hurricane-force gust. Inland, that storm is burying Pittsburgh..."). The loop line restates the hook instead of opening the gap with new words. "hurricane" is spent twice (H1-S2, H1-S5).
- **Decode-me (soft), H1-S5:** "there's no way to see how". The object of "see how" is implied, not named.
- **Decode-me (mild), H1-S2:** "is burying Pittsburgh under what will be more than two feet of snow". Present and future tense in one clause make a small parse cost at 0:12. The wording is kept from the fact-checked round, so fix only if a cleaner wording stays inside the confirmed fact.
- **Superlative without comparator/unit (spoken), I1-S2:** "the city's biggest snowstorm on record". The chip carries "27.4 IN", but the spoken line has no unit. The voice rule wants every superlative to carry its comparator and unit.
- **Hook timing rule (soft):** the first break (a winter storm with a hundred-eight gust) completes at about word 22 to 23, about 9 s at 150 wpm. That is just past the ~8 s target unless Paul's clip runs faster. The "second break at once" is in effect H1-S4 Buffalo at about 25 to 35 s. The snow line in H1-S2 pays the title but does not break a belief.
- **Hook length:** 46 s from 0:00 to the L1 gap. This is acceptable for a doc, but H1-S5's recap is the part that does not earn time.
- **Tag hygiene:** I1-S1 is tagged [PAY], but no loop was open for flooding, so it pays nothing. Retag it as stakes, or drop the tag.
- No banned words, no em dashes in spoken lines, no rhetorical questions, no anaphora run (the "On the coast side / On the inland side" pair is 2, under 3), no thesis opener, no roadmap phrase, no structure self-reference. No digits or abbreviations in spoken lines (grep of `> ` lines: 0 digits). Sentences over 24 words: H1-S5 (26) and I1-S3 (25), and both split at commas. Hard flag words: none; the toll uses "lose their lives". `scripts/flag_words.py episodes/ep-appalachian-1950` exit 0, but that script reads `edit_script.md`, not `acts/intro.md`, so the act file was checked by eye only.

## 4. Loop audit
| Loop | Opened | Paid | Status |
|---|---|---|---|
| Hook gap: winter storm with a hurricane gust | H1-S1 (~9 s) | H1-S2 names it hurricane-force; the cause rides into L1 | ok |
| Buffalo belief (north is worse) | H1-S4 first sentence | H1-S4 second sentence (~35 s) | paid. It opens an unvoiced "why is Buffalo warm?", which is carried only implicitly (the Act 2 cta-hinge names Buffalo). Not tagged. |
| L1 episode loop (how one storm does both at once) | H1-S5 (~46 s) | Act 3 opener | carried on purpose, ok |
| L2 how far south the cold reached | I1-S2 (~71 s) | I1-S3 (~80 s) | paid fast; the tease is weak |
| L4 which gust beat Newark's | I1-S4 (~88 s) | Act 1 (Bear Mountain 140, Mount Washington 160) | carried, ok, but see fix 4 |
- Open-question gaps: 46 s to 71 s has only L1 open, with no fresh question the viewer would ask right then (about 25 s). This is under the 30 s ceiling but misses the "new question about every 20 s" target from the hook's end to the intro's end.
- Dropped-loop risk: the Buffalo oddity. If Act 3 does not say why Buffalo was warm, it is a dropped loop.

## 5. Does it serve the Claim?
Yes. Claim: "It wasn't one storm hazard but two at once: hurricane-force gusts on the East Coast on one side of the storm, record snow and cold inland on the other." The hook sets coast wind against inland snow on one Saturday. The intro gives the coast side (shore flooding, LaGuardia) and then the inland side (Pittsburgh record, Kentucky record cold). The ruled-out leads (land hurricane, Snow Bowl) are absent. Buffalo is a third beat, but it serves the mechanism behind the Claim (the warm side pulled northwest).

## 6. Ranked fixes (max 8)
1. **H1-S5:** replace the recap clause with a line that names the gap with new words (what one storm cannot normally do at once). Drop the second "hurricane", and end on a concrete object instead of "there's no way to see how".
2. **I1-S1:** open it with a question the viewer has right then (for example, what that wind did when it reached the water) instead of "On the coast side of the storm". That closes the 46 to 71 s fresh-question gap and breaks the coast/inland tour frame.
3. **I1-S2:** give the spoken superlative its unit and comparator in the same sentence (twenty-seven point four inches, the most the city has on record), and replace "a long way south" with a sharper tease that names a direction or a state line without the number.
4. **I1-S4 / Act 1:** scope L4 so the payoff is fair. If Bear Mountain's 140 is not from the same day as Newark's 108, say "that weekend" or "in this storm" in I1-S4. Make Act 1 land the payoff as more than "a mountaintop is windier", or the loop will feel cheap.
5. **H1-S4 / L1 note:** tag the Buffalo oddity as part of L1 (or as its own carried loop) and confirm that Act 3 explicitly pays why Buffalo sat in the forties, so the hook's best beat is not a dropped loop.
6. **H1-S1:** trim two or three words so the contradiction lands by about 8 s at Paul's pace (for example, drop "New Jersey" from the spoken line; the popfig already carries "NEWARK, NJ").
7. **H1-S2:** if the fact-check allows, settle the tense ("is burying Pittsburgh under more than two feet of snow by the time it's over") so the line parses in one pass.
8. **I1-S1:** retag [PAY] as stakes, or drop the tag. Nothing is paid there.
