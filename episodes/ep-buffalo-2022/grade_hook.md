# ep-buffalo-2022 · grade_hook.md (independent skeptic grade, hook + tail + intro)

Grader: separate skeptic agent, 26 Oct 26. Has not seen the writer's reasoning. Graded text: `edit_script.md` H1-S1 to I1-S4 (below the "HOOK, TAIL, INTRO" marker), against `angle.md`, `references/script-quickref.md` and `learnings/script-process.md` (2026-09-20 entries). Viewer: a skeptical 45 to 75 year-old American who knows the Buffalo blizzard happened.

## Verdict

**Hook score: 6 / 10 · confidence 70 %**

**NOT LOCK-READY**

What would move it to 8: fix the inverted first contradiction in H1-S2 and pull the warning-came-early contradiction up into the first 15 s (fix 1), then kill the 30+ s dead stretch in I1-S2/S3 and replace the structural exit line in I1-S4 (fixes 2 and 3).

Timing basis: word counts measured from the file (awk over the `>` lines, `[verify]` markers stripped): H1-S1 22, H1-S2 43, H1-S3 31, H1-S4 25, T1-S1 29, I1-S1 66, I1-S2 55, I1-S3 54, I1-S4 37; total 362 words. Seconds below assume about 2.5 spoken words per second. That pace is NOT measured (no probe TTS exists yet), so every second figure here is an estimate; the order of events is exact.

## 1. Six script-os axes (hook + tail + intro as one section)

| Axis | Score (1 to 5) | Why |
|---|---|---|
| New info | 4 | Toll, the outside count, the three-day warning, the fifty-one minutes, the tally at every count date. Dense and sourced. Loses a point for telling "the forecast was early" three times (H1-S3, T1-S1, I1-S4). |
| Curiosity | 3 | Loop E is strong and L0 ("came down to minutes") is the best line in the section. Then I1-S2 and I1-S3 run about 30 to 55 s with no real open question (see section 2). |
| Stakes | 3 | Toll lands around 17 s. After that the stakes go flat: no person, no face, no human moment anywhere in about 2:25. The intro never names who the story is about. |
| Visual change | 4 | Paul, a hard cut to stalled cars, chips, a typed forecast card, the ASOS log, the map, the tally bars. I1-S2's three stacked stat chips are a list, not a beat. |
| Payoff | 3 | L0 pays cleanly and fast (good). I1-S3 "pays" a question the hook already answered at about 20 s, so it re-spends the hook instead of paying something new. |
| Exit hook | **2** | I1-S4 ends on "is where this starts", a line about the video's own structure, and its question (what the forecasters saw) is one the viewer has been told the answer to three times: they saw it coming. |

One axis is under 3, so the section fails the lock rule on the axes alone, independent of the hook score.

## 2. Hook mechanics

- **Delete-test on sentence one (H1-S1, Paul): PASS.** Cut it and H1-S2's "the record says otherwise" has nothing to be otherwise than. Sentence one is load-bearing. Note: H1-S2's first sentence nearly FAILS its own delete test. Cut "In Buffalo, New York, two days before Christmas in twenty twenty-two, the record says otherwise." and the hook still works once the place moves into the next sentence. It is a pivot line with no information in it.
- **Does the hook break the viewer's own belief? PARTLY, and the first break is inverted.** H1-S1 sets the belief "the safest place to ride it out is home". H1-S2 then says "the record says otherwise" and gives eighteen found outside. But people being found outside does not say home was unsafe. It CONFIRMS home was the safer place. What the record really breaks is the next step: you would stay home, and yet the biggest group was outside. As written, "otherwise" tells the viewer home was not safe, which (a) is not what the eighteen-outside fact shows, and (b) spends Act 5's "home was not safe either" in the first 15 s. A sharp 60 year-old hears "otherwise", then "eighteen outside", and thinks "so they should have stayed home, like I said". The contradiction lands on the wrong belief.
- **Second contradiction before about 8 s: FAIL.** The second contradiction (the weather service called it once in a generation three days early) is H1-S3, which starts at word 66, about 26 s, and lands its quote around 35 s. Even the first break ("the record says otherwise") ends at word 37, about 15 s. The 8 s bar cannot be met while Paul's line is 22 words (about 9 s by itself). The fix below lands both breaks by about 15 to 20 s, which is the best this structure allows; a full 8 s would need Paul's line under 12 words.
- **Promise lands in the hook: PASS.** The angle's Claim (eighteen of forty-six found outside, four more in cars) is said aloud in H1-S2, about 17 to 25 s. Toll and twist sit at the edge of the 20 s post-mortem bar.
- **Hook length vs the 27 Sep rule:** the rule is a 3 to 5 s hook then a 5 to 15 s tail. Here H1 alone is 121 words, about 48 s, and T1 follows it. In practice H1-S2 to H1-S4 is a 40 s tail before the labelled tail. Not a lock blocker by itself, but it is where the 30 to 40 s the owner trims by hand lives.
- **30 s stretch with no open question: FAIL.** L0 is paid at the end of I1-S1 (word 216, about 86 s). The next genuine new question is I1-S4's close (word 362, about 145 s). In between, I1-S2 has no question at all, and I1-S3's "Where they found them is the part that stopped me" is not a real gap: the viewer was told where they were found about 20 s into the video. Counting I1-S3 generously, the gap is about 30 s (86 to 116 s); counting honestly, about 55 s. Loop E stays open the whole time, but the rule asks for a fresh micro-question about every 20 s.
- **Loops planted and paid as tagged:**
  - E: `[loop E open]` H1-S1, stated aloud H1-S4, paid A3 + A5 per the table. OK.
  - L0: `[loop L0 open]` T1-S1, `[loop L0 closes]` I1-S1. Paid inside about 25 s. OK, and it is the strongest loop in the section.
  - L1: `[loop L1 open]` I1-S4. Weak: the question it plants is already answered (see exit hook).
  - The loop table rows for L0 and L1 still read "(writer sets ...)". The writer did not write the loop lines into the table. Every row needs both ends written in.
- **Hook claim held at least 60 s:** yes, the outside count stays the subject through I1-S3.

## 3. Register, fluff, banned shapes, load, angle drift

**Register (target 9 of 10, a person talking to you).** Writer self-scores: 8, 8, 8, 9, 8, 8, 8, 9, 8. Grader agrees with an 8 average. The two 9s (H1-S4, I1-S3) are the only segments in first person. The 8s read as a careful narrator, not an old friend:
- H1-S2 "the record says otherwise" is report voice. A friend says what happened, not what "the record" says.
- I1-S1 "Buffalo sits at the eastern end of Lake Erie, in western New York." is an encyclopedia sentence.
- I1-S2 "The state counted thirty-seven straight hours of blizzard conditions in Erie County." is fine as a fact, but three stats in a row make it a stat block.

**Fluff (sentence-level delete test).**
- T1-S1 sentence 1, "The forecast was right, and it was early." Third time in about 60 s the viewer hears the warning was early (H1-S3 says it, then this). Cut.
- I1-S2 "Then the storm settled in." Decoration. Cut.
- I1-S2 "Fifty-one minutes doesn't sound like much." A stock setup line. Weak, can go.
- I1-S3 "more than anywhere else" after "the largest group in every single one". Says the same thing twice. Cut the tail.
- I1-S3 "Where they found them is the part that stopped me." Promises a reveal the viewer already has.
- I1-S4 "And the forecasters saw it coming even earlier than that." The early-warning point a fourth time.

**Banned shapes.**
- "not X, it's Y" flips: none. Clean.
- Rhetorical questions: one, H1-S4 ("Why were so many people out there in it, and why couldn't anybody get to them in time?"). It is the dominant question stated aloud, which is defensible, but the allowed exception is the chapter-exit question. Turning it into a statement keeps the loop and removes the risk (fix 5).
- Summary tags: none. "That's fifty-one minutes after the whiteout reached the airport." is a computed payoff, not a tag. Keep.
- Roadmap / structure phrases: two. H1-S4 "So I went looking for two things." is a light roadmap. I1-S4 "is where this starts" refers to the video's own structure (CLAUDE.md: the script never refers to its own structure).
- Opener variety: "And" opens H1-S3 and I1-S4; "So" opens H1-S4. Fine on count, but both "And" lines carry the same early-forecast point, which makes them read as a repeat.

**Cognitive load (lines the viewer must decode).**
- H1-S2 "the record says otherwise": otherwise than what? The viewer has to work out that it refers back to Paul's line, and then gets the wrong meaning (home was not safe).
- "fifty-one minutes" (I1-S1 end, I1-S2 start) then "fifty-one point nine inches" three sentences later. Two different fifty-ones back to back. The ear will tangle them.
- I1-S4 "even earlier than that": "that" points back about 90 s to H1-S3's three-day warning.
- H1-S2 "the largest group of them, eighteen, were found outside": the number tucked into an aside. Better as its own clause.

**Angle drift and overclaim.**
- No "most" anywhere. "largest group" and "more than anywhere else" match the Claim's wording. Good.
- **Overclaim: "the record says otherwise" (H1-S2)** implies home was not the safer place. The angle does not claim that; Act 5's "home was not safe either" is a later beat. Fix 1.
- **Overclaim: "it was enough to leave people on the road" (I1-S2)** makes the fifty-one minutes the cause of people being out. Nothing in the angle or the act briefs sources that cause; the Act 2 brief only says people were already on the road when the ban came. Fix 2.
- **Dual scope: H1-S2** puts "two days before Christmas in twenty twenty-two" in the same sentence chain as "Forty-six people lost their lives in Erie County". A viewer can hear forty-six on December twenty-third; the count covers the whole storm and the days after. Name the scope ("in that storm") or drop the date from that sentence (the popfig carries it).
- **Drift: I1-S2 "fifty-one point nine inches of snow"** is the snow-total line the angle rules out as a lead. It is not the lead here, but it is a stat-block beat that serves the default story, not the angle. The thirty-seven hours and the sixty-nine mile an hour gusts serve "why nobody could come"; the snow total does not, and it collides with "fifty-one minutes".
- Mild: H1-S4 "why couldn't anybody get to them in time" suggests every one of the eighteen could have been reached. It matches angle arc 3 and Act 4, so it stays, but the act must earn it.

TTS check on the current text: no digits, no "killed", "died" or "dead" in narration, no paired dashes. Longest sentence: H1-S2 "Forty-six people lost their lives ... in the snow." at 22 words, under 24. Clean.

## 4. Ranked fixes (wording only rearranges or cuts what is already in the file; TTS-safe)

**1. Re-aim the hook's first break and pull the second break forward (H1-S1 to H1-S3). Blocker.**
Why: the first contradiction lands on the wrong belief, the second lands at about 30 s, and the date sits next to the toll.
- H1-S1 (Paul, 15 words, about 6 s):
  > A blizzard warning hits your town the week of Christmas, and you'd ride it out at home.
- H1-S2 (replaces both sentences of the old H1-S2 opener; 19 + 17 words):
  > In Buffalo, New York, in twenty twenty-two, the largest group of people who lost their lives were found outside, in the snow.
  > That was eighteen of the forty-six in Erie County, and four more were found in their cars.
- H1-S3 (the second contradiction, moved up; 8 + 21 words):
  > And this storm did not sneak up on anybody. Three days before it hit, the weather service in Buffalo called it a once in a generation type of event.
- Effect: belief at about 6 s, first break ("found outside") at about 14 s, second break at about 26 s instead of 35 s. Keep the popfig "BUFFALO, NY · DEC 23, 2022" for the date, so the spoken line no longer ties forty-six to one day. Carry the existing `[verify]` markers over unchanged.
- Faster option if the owner wants the 8 s bar: cut H1-S3's first sentence and start H1-S3 at "Three days before it hit". Saves about 3 s.

**2. Fix the dead stretch, the causal overclaim and the fifty-one collision (I1-S2 and I1-S3). Blocker.**
- I1-S2 (cut "Fifty-one minutes doesn't sound like much.", "Then the storm settled in." and the snow total; 15 + 20 words):
  > On the last workday before Christmas, people were already on the road when it hit.
  > The state counted thirty-seven straight hours of blizzard conditions in Erie County, with gusts at the airport up to sixty-nine miles an hour.
  Drop the "51.9 IN AT THE AIRPORT" chip; keep "37 STRAIGHT HOURS" and "GUSTS 69 MPH".
- I1-S3 (replace the already-answered question with the real one, the tally that never changed; 16 + 17 + 12 words):
  > As the National Guard and the road crews dug the city out, they started finding people.
  > I went through every county count that listed where people were found, and one thing never changed.
  > Outside, in the snow, was the largest group in every single one.
  The new gap ("one thing never changed") opens and pays inside about 5 s over the building tally bars, and nothing is re-spent from the hook.

**3. Replace the structural exit with a real chapter-exit question (I1-S4). Blocker (exit axis is 2).**
- I1-S4 (14 + 14 words; the one allowed chapter-exit question):
  > The weather service in Buffalo flagged this storm on the Sunday before, five days out.
  > How does a warning that early still end with people out on the road?
  Removes "is where this starts" and "even earlier than that". The question is the one Act 1 and Act 2 answer (the warning products, then Friday morning), so it carries L1. Update the L1 row in the loop table to this line.

**4. Cut the repeat in the tail (T1-S1).**
> What went wrong that Friday morning came down to minutes, and the airport's own weather station logged every one of them.
Cut "The forecast was right, and it was early." With fix 1 the viewer has just heard it.

**5. Turn H1-S4's question into a statement and drop the roadmap opener (H1-S4).**
> I wanted to know two things, why so many people were out in it, and why nobody could get to them in time.
22 words. Keeps loop E stated aloud in first person, removes the rhetorical question and "So I went looking for".

**6. Compress the geography line (I1-S1).**
Cut "Buffalo sits at the eastern end of Lake Erie, in western New York." from the narration; the self-made map already labels Lake Erie and western New York, and New York was said in H1-S2. Start I1-S1 at:
> Before dawn on Friday, December twenty-third, it was raining at the Buffalo airport, at about thirty-eight degrees.
Keep the `[verify]` marker for the Friday date; drop the Lake Erie marker with the cut sentence.

**7. Housekeeping (not a lock blocker).**
Write the actual L0 and L1 lines into the loop table rows that still read "(writer sets ...)".

**8. Gap the grade cannot fix with existing text: no human in the first 2:25.**
Stakes stay at 3 until a person appears. The Act 3 brief already holds Anndel Taylor, twenty-two, about six minutes from home, who called nine one one. A one-sentence plant of her in I1-S3 or I1-S4 would lift stakes and curiosity, but she is outside the hook and intro text as written, so it is the orchestrator's call, with a `[verify]` marker on the line.

## Expected grade after fixes 1 to 6

Estimate 8 / 10 (confidence 60 %): both breaks land inside about 26 s on the right belief, no stretch over about 20 s without a question, exit axis to 3 or 4. Fix 8 would likely add one more point to stakes. The re-grade must be a fresh grader pass on the rewritten text, not this estimate.
