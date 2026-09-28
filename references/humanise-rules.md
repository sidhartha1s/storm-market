# humanise-rules.md — narration rules that keep a script from reading as AI (owner-supplied doc, 2026-09-13)

> Source: the owner's "YouTube Script Rules for Your LLM" (Google Doc 1xja9b4nQwis8AwEar8JMPkKVFNFJxLv2c6-Yq7GbBIs), applied
> to every Warning Hour script from Krakatau #5 on. Read order: `script-os.md` → `script-framework.md` → THIS FILE →
> `script-scaling.md` → DESIGN.md. When a rule and instinct disagree, the rule wins. Owner's hypothesis: distribution now
> reads transcripts; a script that scans as AI gets fewer impressions however strong the packaging. The pre-TTS
> "humanise pass" runs rules 2–14 line by line and returns only the clean script.

1. **Facts carry the point.** Put the facts next to each other; never narrate the conclusion on top of them.
2. **No painting the picture.** No "picture this / imagine", no second-person nostalgia, no hypothetical cinematic scenes,
   no personified companies, buildings, mountains. Name the thing in one plain sentence and move on.
3. **No borrowed metaphors.** No icebergs, dominoes, ticking clocks, perfect storms, house of cards, tapestries. If the
   comparison could be pasted into another script, delete it and state what happened.
4. **Do not announce the move.** Banned openers: here's the thing / here's why this matters / here's the kicker / get
   this / let me walk you through / let me be honest / picture / imagine / notice / consider / do the math / run the
   numbers / start with / which brings us to / buckle up / let's dive in / sit with that / let that sink in / make no
   mistake / what you need to understand is / what makes this different is. Delete the opener, start with the fact.
5. **Banned words:** delve, furthermore, moreover, additionally, comprehensive, crucial/critical/essential as filler,
   robust, unprecedented, leverage, foster, seamless, elevate, navigate (figurative), game-changer, paradigm, tapestry,
   landscape (figurative), realm, testament, underscore (verb), pivotal, groundbreaking, transformative, multifaceted,
   intricate, nuanced, myriad, plethora, embark, journey (figurative), unlock, harness, empower, resonate, vibrant,
   bustling, nestled, meticulous, utilize, facilitate, implement (when "do" works).
6. **Banned phrases:** a testament to, the landscape of, in today's world, in the ever-evolving, on the other hand,
   without further ado, it's worth noting, it's important to understand, in conclusion, to summarize, as we've
   discussed, at the end of the day, when it comes to, plays a crucial role, stands as a, serves as a, is a reminder
   that, the quiet [anything], what sounds like, what amounts to, in what can only be described as, some say, many
   experts believe, it's been reported (name the source or cut the claim).
7. **Banned sentence shapes:** the reveal-flip ("this isn't X, it's Y"; "not late, built for the wrong event"); the
   drama stack of fragments (one deliberate fragment per script); the question-then-answer fragment ("The result?
   Bankruptcy."); the anaphora run (3+ sentences opening on the same word); the balanced-contrast engine beyond one per
   script; the "notice what he didn't do" scaffold; the characterized quote ("what sounded like mercy:"); the aphorism /
   mirrored-callback ending; the thesis opener ("this is the story of…"); the summary tag ("That's the mechanism.").
8. **No rhetorical questions in narration.** Write the statement.
9. **No em dashes.** Period, comma, or parentheses.
10. **No hedging or filler intensifiers:** arguably, perhaps, kind of, sort of, somewhat, very, really, truly,
    incredibly, absolutely.
11. **Specifics over abstractions.** A name, date, number, place or figure every few sentences; exact figures, never
    rounded ("$2,948", not "about three grand").
12. **Strong verbs, active voice.** Scan for is/are/was/were/has/have/be/get; every sentence answers "who did what".
13. **Vary sentence length on purpose.** Short (5–12), medium (15–22), short. Never three of the same length in a row.
14. **No summaries, recaps, soft exits.** No "so there you have it", no moral, no "in this video".
15. **Write for the ear.** Read aloud in your head; spell numbers in narration except years and dollar figures;
    pronunciation notes go after the script, never inside it.
16. **No fabrication.** No invented quotes, statistics, events. Missing source = leave it out and say so.
17. **"This sounds AI" = full check of rules 2–14, return only the clean script.**

## House additions (Warning Hour, 2026-09-13)
- Violence/death words that trip YouTube's transcript scan are a separate list, not duplicated here:
  `references/flag-words.md` (gate `scripts/flag_words.py`).
- Rule 7 kills two of our reflexes: the reveal-flip ("The warning was not late. It was built for the wrong kind of
  event.") and the mirrored callback ending ("The physics did not change. The slope did."). Both sat in the #5 draft.
  Rewrite each as one plain statement or a concrete detail.
- Retention devices survive as facts, not as announcements: a chapter ends on a question the next chapter answers
  (script-os rule 3) is allowed only when the question is a real open fact ("Then where did the rock go?"), never a
  rhetorical one to the viewer.
- The humanise pass is a gate before a section locks (revised 27 Sep 26, `references/script-scaling.md` "Section
  lock — the ONE definition"): run on that section's prose as it's written, not held for the whole finished script,
  with a line-by-line diff kept in the episode folder.

## Spoken voice palette (owner 2026-09-20, from the ep-1974 TTS probes)
The narration is a person telling a story, and pocket-TTS voices every device below. No code enforces this
section: the writer writes with it open, the independent grader sweeps the finished script once and lists every
device with its timestamp, and anything that breaks the cadence is fixed in that one pass.
- **Banned, every script:** "uh" and "um" (they read as retching in this voice); self-corrections ("about an hour,
  maybe a little less"); doubled negatives for rhythm ("not before, not since"); any device used in two sentences
  in a row; trailer fragments (see learnings/script-process.md 2026-09-20).
- **Always on, invisible:** contractions where a person would use them; sentences of 10 to 22 words joined with
  and / but / because / so; ordinary intensifiers ("really", "just", "actually") used the way people use them.
- **Rationed devices (each at most three times in a 20-minute script, never twice inside three minutes, never the
  same one in neighbouring acts):** an opener ("Okay, so", "Now look", "Now,"; never the rule-4 banned phrases such as "here's the thing"); an aside
  ("honestly", "I mean", "well"); a check-in ("right?"); repeating the subject ("the man who ran the office, he
  knew"); repeating the verb for weight ("he knew. He knew it was coming"). Aim for one noticeable device every two
  to three minutes, and vary which one.
- **Variance is the rule, not the exception:** if the grader's census shows the same device at 4:10 and 6:30, one of
  them goes. A device that appears in every act is a pattern, and a pattern is what the audience calls AI.
- **Probe before deciding:** any new device gets a 30-second TTS probe first (recipe: `episodes/<slug>/audio/probe/`).
