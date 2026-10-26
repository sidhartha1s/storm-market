SCORE: 7/10 (confidence 70%)
HOOK SCORE: 7/10 (hook H1-S1 to H1-S4 alone)

# Grade: ep-appalachian-1950, opening (HOOK H1-S1..S4 + acts/intro.md I1-S1..S7), round 1
Grader: skeptic grader, batch A, 26 Oct 26. Bar to lock: 8. Not locked.
Rule set used: `.worktrees/ep-appalachian-1950/references/script-quickref.md` (the path in the brief, `.worktrees/hook-shapes/references/`, does not exist on disk).
Old I1 in edit_script.md ignored as superseded, per task.

Length (counted by script): hook 88 words, intro 189 words, 277 total. At about 145 words a minute (estimate, not measured TTS) the hook ends near 0:36 and the intro near 1:55.

## Verdict in one paragraph
The title is paid fast and plainly: "a hundred eight miles an hour" in sentence one (Paul on camera), "more than two feet of snow" by about 0:20, both on chips. The hook has a real double contradiction (a hurricane-force gust from a winter storm; Buffalo, north of Pittsburgh, in the forties with no snow). It misses the 8 s and 20 s timings, opens on a date rather than the viewer's belief, and never says the episode question out loud. The intro is clean on mechanics (no digits, no banned words, no rhetorical questions, all long sentences split at commas) but spends three facts twice, has two decode-me lines, drops first-person Paul entirely, and ends its WHAT on a place list instead of the Claim's two-sides picture.

## Six axes per minute (1 to 5)
| Minute | New info | Curiosity | Stakes | Visual change | Payoff | Exit hook |
|---|---|---|---|---|---|---|
| 0:00-1:00 (H1-S1 to mid I1-S2) | 5 | 4 | 5 | 4 | 4 | 4 |
| 1:00-1:55 (mid I1-S2 to I1-S7) | 4 | 3 | 3 | 4 | 4 | 4 |

No two low minutes in a row. Minute 2 curiosity is 3: its loops (L3, L5) are coy name-withholds paid in under 10 s, and the episode loop L1 is never spoken. Stakes is 3: no person and no toll after the hook.

## Register: "a person talking to you" 7/10
Hook reads like a person (8): "you're in Newark", "the wind just gusted". The intro loses first person entirely (zero "I" lines in hook or intro; the rule wants Paul in first person, and the old I1 had "I read the weather service reports from that weekend").

Worst 3 lines:
1. I1-S3: "Inland, that same weekend came down as snow, and Pittsburgh's two feet went into the city's record book at a spot no storm has taken from it since." (a weekend does not come down; "at a spot no storm has taken from it since" has to be decoded)
2. I1-S6: "That's one storm on one weekend: hurricane-force wind and a flooding tide in New York and New Jersey, record snow in Pennsylvania, Ohio and West Virginia, and record cold reaching down into Kentucky." (a list read off a report; recap shape)
3. I1-S1: "...and at an airport in New York the water is finding a way through." (coy withholding of LaGuardia to make a 5 s loop nobody asked for)

## Rule breaks (exact line)
- Hook opener rule ("Open on the viewer's own belief"; "Sentence one ... not a number or date"): H1-S1 "It's the Saturday of Thanksgiving weekend, you're in Newark, New Jersey..." opens on a date and place. The drop-in shape is the orchestrator's provisional pick (owner pick pending), so this is a known conflict, but it still breaks the written rule.
- Double contradiction before 8 s: the first contradiction ("it's coming from a winter storm", H1-S2) lands about word 34, roughly 0:14.
- Channel post-mortem "toll and twist inside 20 s": toll (H1-S4) lands about word 73, roughly 0:30.
- Hook tail "context plus ONE open curiosity gap": H1-S4 ends on the toll; the gap (how one storm did both) is only implied, never voiced.
- Sound cue mismatch: H1-S4 sound note says "riser ends on 'one storm'", but the line contains no "one storm".
- Belief not anchored: H1-S3 "Buffalo is sitting in the forties with no snow at all" breaks a belief (north is colder) the viewer was never handed; round 5 had "you'd figure it was colder" and that anchor is gone.
- Fact spent twice: (a) tide pushed in: I1-S1 "that wind is pushing the tide in against the coast" and I1-S2 "the wind drove the tide in until the shore flooded"; (b) Pittsburgh rank 1: I1-S3 "at a spot no storm has taken from it since" then I1-S4 "It's still Pittsburgh's biggest snowstorm on record"; (c) Bowling Green record: I1-S4 "still hasn't been beaten" then I1-S5 "a November record that still stands".
- Word repetition: "still" 3 times across I1-S4 and I1-S5; "same storm / same weekend" 3 times (H1-S2, H1-S3, I1-S3).
- Tense jump: I1-S1 present ("is pushing", "is finding") to I1-S2 past ("broke", "drove") within one breath.
- Summary/recap shape: I1-S6 "That's one storm on one weekend: ..." restates places already shown, and echoes H1-S2 "That's a hurricane-force gust".
- Decode-me: I1-S3 (both clauses), quoted above.
- Register rule (first person): no first-person line in the whole opening.
- Clean: no digits or abbreviations in spoken lines, no banned words or phrases, no rhetorical questions, no anaphora run, no reveal-flip, no roadmap phrases, no structure self-reference. Every sentence over 24 words splits at commas into chunks under 24 (I1-S1 30, I1-S3 28, I1-S6 33). `scripts/flag_words.py` on the episode: PASS, 0 hard, 0 soft (it scans edit_script.md; acts/intro.md read by eye, no hard or soft words found).

## Loop audit
| Loop | Opened | Paid | Note |
|---|---|---|---|
| L1 how one storm makes both | H1-S2/S4 (implied) | Act 3 | Carried on purpose, but never spoken as a question in hook or intro. |
| L2 where the water gets through | I1-S1 | I1-S2 (~5 s) | Paid; weak (a question no viewer asks). |
| L3 Pittsburgh's record spot | I1-S3 | I1-S4 (~10 s) | Paid, but the tease gives the answer away. |
| L5 the Kentucky reading | I1-S4 | I1-S5 (~8 s) | Paid, but tease and payoff say the same "still" fact. |
| L4 which gust beat Newark's | I1-S7 | Act 1 | Good exit; carried on purpose. |

No 30 s stretch without an open question. Housekeeping: the LOOP TABLE in edit_script.md is stale (L2 = Buffalo, L4 planted I1-S4, no L3 or L5 rows), and the superseded old I1 is still in edit_script.md.

## Does it serve the angle's Claim?
Partly. Both hazards are on screen and in the voice inside two minutes, and Buffalo makes the "same storm, different worlds" point well. But the Claim's geometry ("on one side of the storm ... on the other") is never said; I1-S6 gives a list of states instead of the two sides. Chicago (west, off the Appalachian frame) is fine as cold but thins the two-sides picture.

## Ranked fixes
1. H1-S1/H1-S2: move the winter-storm contradiction into sentence one so it lands before 8 s (end H1-S1 on "...and it's coming from a snowstorm"), or reopen on the viewer's belief if the owner picks a belief-shape hook.
2. H1-S3: hand the viewer the belief before breaking it, one clause ("you'd figure Buffalo, farther north, got it worse") ahead of "forties with no snow".
3. H1-S4: bring the toll inside 20 s (fold it into H1-S2) and end the hook on the spoken gap (one storm doing both at once); point the sound cue at a word the line actually has.
4. I1-S1/I1-S2: say the tide once (cut the tide clause from I1-S1 or from the New Jersey sentence) and keep one tense across both segments.
5. I1-S3: replace with a plain line ("Inland it fell as snow, and Pittsburgh got two feet."), so L3's tease stops giving away the I1-S4 payoff and the decode-me goes.
6. I1-S4/I1-S5: open L5 on how far south the cold reached, not on "still hasn't been beaten", so "still stands" is said once.
7. I1-S6: say the Claim's two sides (coast side: wind and tide; inland side: record snow and cold) instead of the state list, and drop the "That's ..." recap opener.
8. I1-S2 seam: put back one first-person Paul line ("I read the weather service reports from that weekend"); orchestrator also updates the LOOP TABLE and deletes the superseded old I1 in edit_script.md.
