SCORE: 7/10 (confidence 75%)
HOOK (H1-S1 to H1-S5): 7/10 (confidence 70%)

Section: `acts/intro.md` round 2, graded as one opening (hook H1-S1..S5, tail T1-S1, intro I1-S1..S5). Bar to lock is 8; it does not lock.
Measured: 324 spoken words. At about 150 words a minute that is about 2:10 of voice, plus picture holds, so call it 2:15. The hook is 116 words (about 47 s). The toll ("at least six thousand") ends at word 64, about 26 s in.

## 1. Overall
- The opening has a strong spine: one object (the 1891 page), the man who wrote it, the storm, the Havana forecast kept off the wire, and his wife. The title's two halves ("He said it was safe", "It was not") are both paid aloud by H1-S3. The Claim's three parts all land by I1-S4.
- Four things hold it under 8:
  - I1-S2 still carries an open `[verify]` marker, which blocks the lock on its own.
  - I1-S4 opens with the exact kind of first-person line the quickref says to cut.
  - H1-S4 reads like a report, and the hook never says what the decree meant for Galveston.
  - The toll lands at about 26 s, past the 20 s post-mortem rule.
- Hook alone: the open is strong and passes the delete-test, and the wife line is a good human close. It loses points for the late toll, the report-voice H1-S4, no "you" anywhere in the hook, and the nine-year gap never spoken (1891 is only on the popfig).

## 2. Six axes per minute (1 to 5)
| Minute | New info | Curiosity | Stakes | Visual change | Payoff | Exit hook |
|---|---|---|---|---|---|---|
| 0:00-1:00 (H1-S1 to T1-S1) | 5 | 4 | 5 | 5 | 4 | 4 |
| 1:00-2:00 (I1-S1 to I1-S4) | 4 | 3 | 3 | 4 | 4 | 4 |
| 2:00-2:15 (I1-S5) | 2 | 4 | 3 | 2 | 2 | 4 |
There are no two low minutes in a row. Minute 2 has the lowest curiosity score: q1 asks "where did Washington think it would go?", and the hook (H1-S4) already told the viewer Washington disagreed with Havana.

## 3. Register: "a person talking to you" = 6/10
- The script has 1 "you" (I1-S1) and 1 first-person line (I1-S4). Most other lines are past-perfect reportage ("had said", "had decreed", "had been warned").
- Worst 3 lines:
  1. I1-S4 "I read Cline's own report, and Galveston wasn't left in the dark." This is the generic first-person line the quickref names to cut. "Left in the dark" is a stock idiom.
  2. H1-S4 "But the Weather Bureau in Washington had decreed that only its own forecasts would be carried over the telegraph." Passive, bureaucratic, said in NOAA's words rather than Paul's.
  3. H1-S3 "In nineteen hundred, on the evening of Saturday the eighth of September, a hurricane came ashore at Galveston." Four stacked date pieces before the verb. The popfig already carries the date.

## 4. Rule breaks
- **First-person line that could sit in any episode** (quickref Voice/Register): I1-S4 "I read Cline's own report". Paul says he read a report, not what he found in it.
- **Open `[verify]` gate:** the I1-S2 Rows line still has `[verify: "out in the eastern Gulf" as the spoken form of MWR "middle-eastern part of the Gulf" ...]`. "Eastern Gulf" is also wider than "middle-eastern part".
- **Toll later than 20 s** (channel post-mortem): the toll in H1-S3 ends at about 26 s by word count. The hook's own Picture note claims "about 20 s".
- **Borderline reveal-flip:** I1-S4 "Galveston wasn't left in the dark ... But even Friday's midday warning called it a moderate storm." This is the "not X ... but Y" contrast shape.
- **Fact spent twice:** H1-S4 says the decree. I1-S3 "the only forecasts on the wire to Galveston were Washington's" says it again. The second line adds the consequence the hook left out. Put that consequence in the hook and cut the repeat.
- **Same word repeated:** "own" is spoken 5 times in about 2 minutes (H1-S2 "Galveston's own weatherman", H1-S4 "its own forecasts", H1-S5 "Isaac Cline's own wife", I1-S1 "its own idea", I1-S4 "Cline's own report"). "That night" is spoken twice (H1-S3, H1-S5). This is a tic, not a formal anaphora run.
- **Lines the viewer has to decode:**
  - I1-S2 "the way many storms did near that latitude": which latitude is never said aloud.
  - H1-S4 leaves the viewer to work out that the decree meant Galveston never heard Havana's forecast.
- **US state never spoken in the first 60 s:** "Texas" appears only on the popfig. The rule may accept on-screen text, but the 45 to 75 audience often listens without watching.
- **TTS risk:** I1-S1 "it'd" needs a probe or should be written as "it would".
- **Sentences over 24 words:** I1-S1 has 25 and I1-S4 has 25. Both split at commas, so they are acceptable.
- **Clean:** no digits, abbreviations, banned words, hard flag words, roadmap phrases or structure self-reference. The I1-S5 question is the allowed chapter-exit question.
- **Accuracy:** the hook shape "object" was not run through `hook_shape.py` (I am a read-only grader).
- **Accuracy note, not a break:** I1-S5 "called a storm like this an absurd delusion". The 1891 text calls the *belief* that the city would be seriously damaged a delusion, not the storm. factcheck-D rated it fair; keep the wording close to H1-S2 "that fear".

## 5. Loop audit
| Loop | Opens | Closes | Gap |
|---|---|---|---|
| Hook implicit (what happened after the page) | H1-S1 0:00 | H1-S3 about 0:26 | paid |
| E1 (why so few left a warned city) | T1-S1 about 0:58, spoken | carried to A6 | on purpose |
| q1 (where Washington thought it would go) | I1-S1 about 1:15 | I1-S2 about 1:22 | paid, but weak (already implied by H1-S4) |
| q2 (what the wire told Galveston) | I1-S3 about 1:38 | I1-S4 about 1:58 | paid |
| L-intro (why he called it an absurd delusion) | I1-S5 about 2:10 | carried into A1 | on purpose |
- E1 stays open from about 0:58, so there is no stretch of 30 s or more without an open question.
- Between 0:26 and 0:58 the only open thread is the Havana decree's unstated consequence. That works only if the viewer infers it, which is the H1-S4 decode problem above.

## 6. Does it serve the Claim?
Yes, all three parts:
- His own weatherman said it in print: H1-S1 and H1-S2.
- Havana was kept off the telegraph: H1-S4.
- The city did not ignore a warning, because the warning it got called it a moderate storm: I1-S4.

One risk: T1-S1 "The city had been warned. Still, few people left." frames the default "they ignored it" story for about 50 s until I1-S4 answers it. That is acceptable as the E1 setup, but I1-S4's payoff line has to stay the strongest line in the intro. Right now it is.

## 7. Ranked fixes
1. **I1-S4:** cut "I read Cline's own report, and Galveston wasn't left in the dark." Open on the record itself ("Washington's messages reached Galveston every day from the fourth to the eighth"). If Paul speaks in first person, he says what he found in the report, not that he read it.
2. **I1-S2:** resolve the open `[verify]` marker. Safest is to change "out in the eastern Gulf" to "far out in the Gulf" so it fits MWR "middle-eastern part of the Gulf".
3. **H1-S4:** end the decree sentence on its consequence for Galveston (for example "so Galveston heard only Washington's forecast"), in active voice. Then trim I1-S3 to its first sentence plus the q2 question, so the decree is spent once.
4. **H1-S3:** cut the spoken date stack to "Nine years later, on a Saturday night in September, ..." so the toll lands near 20 s. This also speaks the nine-year gap the promise needs; the popfig keeps the full date.
5. **Whole opening:** keep "own" at most twice. Keep it in H1-S2 "Galveston's own weatherman" and H1-S5 "Isaac Cline's own wife". Cut it from H1-S4, I1-S1 and I1-S4.
6. **I1-S1/I1-S2:** sharpen q1 so it asks something the hook did not already answer (for example how sure Washington was). Change "near that latitude" to "once they got that far north".
7. **T1-S1:** speak "Texas" once (for example "an island city off the Texas coast").
8. **I1-S5:** match the H1-S2 wording ("call that fear an absurd delusion") rather than "called a storm like this", and drop "already" (it repeats "Long before").
