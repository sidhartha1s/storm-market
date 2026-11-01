SCORE: 7/10 (confidence 70%)
HOOK SCORE: 7/10 (confidence 70%)

# ep-galveston-1900 · intro round 3 · skeptic grade (26 Oct 26)

Graded: `episodes/ep-galveston-1900/acts/intro.md` (hook H1-S1..S5, tail T1-S1, intro I1-S1..S5) as one opening. Context read: `angle.md`, `edit_script.md` (header, registry, act briefs), `references/script-quickref.md`. Earlier grade files not read.
Measured: 315 spoken words, about 2:06 at 150 wpm, 1:51 at 170 wpm (awk count over the `>` lines). Longest sentence 23 words (I1-S2). No digits in spoken lines. `hook_shape.py`: PASS (`object`; last two: buffalo `missing`, appalachian `drop-in`). `flag_words.py`: PASS, 0 hard, 0 soft.

## Verdict in one paragraph
A real, working opening. The object hook is concrete (Paul holding the 1891 page), the title is paid aloud in order ("He said it was safe": H1-S1 + H1-S2; "It was not": H1-S3 toll + H1-S5 wife), both angle arcs are on screen inside 45 s, and q1 and q2 open and close cleanly. It does not reach 8 because: the hook runs about 47 s and its fourth segment is a 46-word bureaucratic block; the telegraph decree is spent three times (H1-S4 twice, I1-S3 again); two lines need decoding ("that fear", "part of it"); the tail's "The city had been warned. Still, few people left." leans toward the very reading the Claim denies; and the register is closer to a careful report than an old friend (6 of 10).

## Hook (H1-S1..S5) on its own: 7/10
- Sentence one is the payoff in the chosen shape; delete-test passes (cut it and H1-S2 has no "it").
- Twist ("Galveston's own weatherman ... absurd delusion") lands about 12 s: good. Toll ends at word 59, about 21 to 24 s: just past the 20 s post-mortem bar.
- Order costs it: toll (S3), then a 15 s detour to Havana and the telegraph (S4), then back to the toll for the wife (S5). The wife line pays the title personally, but it is cut off from the toll it belongs to.
- H1-S4 jumps backward in time from landfall to Havana with no time stamp ("Over in Havana ... said the storm was moving"): the viewer must work out that this was days earlier.

## Per-minute axes (1 to 5)
| Minute | New info | Curiosity | Stakes | Visual change | Payoff | Exit hook |
|---|---|---|---|---|---|---|
| 0:00 to 1:00 (H1-S1 .. T1-S1) | 5 | 4 | 5 | 5 | 4 | 4 |
| 1:00 to 2:06 (I1-S1 .. I1-S5) | 4 | 3 | 3 | 4 | 4 | 4 |
No low minute; no two low minutes in a row. Minute 2 curiosity dips because q1 and q2 are short procedural loops (which track, what did the wire say) under an E1 that is already half answered.

## Register: "a person talking to you" 6/10
Only one "you" line (I1-S1), no first-person line, two contractions in 315 words. Worst three:
1. H1-S4: "But the Weather Bureau in Washington ruled that the telegraph would carry only its forecasts." (agency memo voice)
2. I1-S4: "Washington's messages reached Galveston every day from the fourth to the eighth." (a log read aloud)
3. I1-S1: "His brother Joseph worked beside him as the observer." (roster line, nothing at stake)

## Rule breaks (exact lines)
- Fact spent twice (consecutive): H1-S4 "But the Weather Bureau in Washington ruled that the telegraph would carry only its forecasts." then "So the only forecasts on the wire to Galveston were Washington's." The second is a restatement, close to a summary tag. Spent a third time at I1-S3 "And Washington's wire was telling Galveston what to expect."
- Decode-me: H1-S2 "He called that fear an absurd delusion." H1-S1 names a claim (no hurricane could badly damage the city), never a fear, so "that fear" has no antecedent.
- Decode-me / hedge: H1-S2 "The man who wrote part of it" ("part of it" makes the viewer wonder who wrote the rest).
- Decode-me: H1-S4 "Over in Havana, the Jesuit forecasters ... said the storm was moving northwest" directly after landfall and deaths: an unstamped seam backward in time (quickref: seams are time-stamps).
- Rhetorical question rule: I1-S5 "Why would he once have called the fear of a storm like this an absurd delusion?" is a legal chapter-exit question, but the rule pairs it with one affirming line, and none follows.
- Repetition: "Washington" spoken 5 times in about 100 s (H1-S4 twice, I1-S1, I1-S3, I1-S4); "Friday" twice in I1-S4.
- None found: banned words or phrases, reveal-flip, anaphora, thesis opener, roadmap phrases, structure self-reference, digits or spoken abbreviations, hard flag words, sentences over 24 words.

## Loop audit
| Loop | Opens | Closes | Status |
|---|---|---|---|
| hook implicit (who said it was safe) | H1-S1 (0:00) | H1-S2 (about 0:12) | paid |
| E1 why did so few leave a warned city | T1-S1 (about 0:55) | A6 (carried) | carried on purpose, but half answered at I1-S4 ("moderate storm") at about 1:50: the episode loop is partly spent in the intro |
| q1 which track did Washington expect | I1-S1 (about 1:15) | I1-S2 (about 1:25) | paid |
| q2 what did the wire tell Galveston | I1-S3 (about 1:40) | I1-S4 (about 1:50) | paid |
| L-intro why would he call it an absurd delusion | I1-S5 (about 2:05) | A1 (carried) | carried on purpose |
No stretch of 30 s or more without an open question (the Havana line carries "what did Washington say" from about 0:30 to the tail).
Bookkeeping, not a script fault: `edit_script.md` still holds the superseded hook and intro (I1-S6) and its loop registry plants L-intro at "intro (I1-S6)"; in `acts/intro.md` it is I1-S5.

## Does it serve the Claim?
Yes on all three parts: the 1891 "absurd delusion" in print (H1-S1, H1-S2, I1-S5), Havana kept off the telegraph (H1-S4), Washington's own warning called it moderate (I1-S4). One line works against it: T1-S1 "The city had been warned. Still, few people left." Heard right after "only Washington's forecasts were on the wire", it reads as "they were warned and ignored it", the reading the Claim ("Galveston did not ignore a warning") exists to deny, until I1-S4 corrects it 50 s later.

## Ranked fixes
1. H1-S4: cut the last sentence ("So the only forecasts on the wire to Galveston were Washington's."), and open the segment with a time stamp ("Days before," in place of "Over in Havana,"), so the decree is spent once and the backward jump is signposted.
2. H1-S2: name the fear instead of "that fear" (say "the fear that a storm would one day badly damage the city", as the 1891 text has it) and drop "part of" from "The man who wrote part of it" (keep the part-authorship on the on-screen source line); this also pulls the toll closer to 20 s.
3. Hook order: move H1-S5 (the wife) to directly after H1-S3, so "It was not" lands as toll then wife inside about 30 s, and Havana (H1-S4) becomes the second break that hands into the tail.
4. T1-S1: change "The city had been warned." to say whose warning it was (Washington's storm warning), so E1 asks why few left a warned city without implying the city ignored a warning.
5. I1-S3: replace "Washington's wire was telling Galveston what to expect" with a q2 line that does not restate the wire (third spend) and does not say "Washington" again.
6. I1-S5: add one short affirming line after the exit question, taken from the A1 brief (Cline had a reason, the shallow shelf and the low land), so the question follows the chapter-exit rule.
7. I1-S1: cut "His brother Joseph worked beside him as the observer." (no payoff in the opening; the A4 brief does not use him); keep the lower-third if the edit wants him seen.
8. I1-S4: put the viewer in the place once more ("your city", following I1-S1's "If you lived in Galveston") and say "Friday" once; raises register without a new first-person line.
