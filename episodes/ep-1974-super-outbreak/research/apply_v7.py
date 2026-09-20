"""One-shot: apply the v6 grader's fixes (research/script_review_v6.md) -> v7; fix the fact-sheet UTC rows."""
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
p = root / "edit_script.md"
t = p.read_text(encoding="utf8")

pairs = [
    ("Script v6\n(v1 graded", "Script v7\n(v1 graded"),
    ("comma splices; owner length decision: natural 19 to 20 min).",
     "comma splices; v7 applies the v6 grade, `research/script_review_v6.md`, 7/10, hook 8: Tanner\ntimeline, rhetorical questions, anaphora, balanced-contrast reflex; owner length decision: natural 19 to 20 min)."),
    # 1 Tanner timeline (fact sheet table 6:20–7:21 PM CDT wins over the prose "about 90 minutes")
    ("stayed on the ground for ninety minutes and fifty two miles.", "stayed on the ground for about an hour and fifty two miles."),
    # 2 rhetorical questions
    ("[Q Q-A3] How do you warn a city when your radar can't see the thing you're warning about? At 4:05 PM",
     "[Q Q-A3] So the office had to warn a city off a shape on the edge of a storm. At 4:05 PM"),
    ("[HUMAN citation\ncard] So what happened the second time?", "[HUMAN citation\ncard] The second time, the numbers went the other way."),
    ("Could April third happen again? Yes, it\ncould, because the ingredients", "April third can happen again, because\nthe ingredients"),
    ("[PAY EPISODE] So if he knew, why did so many people die? Because in 1974 knowing a day early\nbought you nothing without a radio and a basement, and today the warning buys you minutes.",
     "[PAY EPISODE] Pearson knew a day early, and it bought nobody anything without a radio and a\nbasement, and today the warning buys you minutes."),
    # 3 anaphora in A6-S2 and A6-S3
    ("In 1974 the warning was\na radio you had to have switched on, and today it's the phone in your pocket, and it will wake you up.",
     "Back then the warning was\na radio you had to have switched on, and today it's the phone in your pocket, and it will wake you up."),
    ("In 1974 a good warning was fifteen minutes and most places got less, and today a warning gives you\neight to fifteen.",
     "A good warning in 1974 was fifteen minutes and most places got less, and today a warning gives you\neight to fifteen."),
    ("A storm shelter or an inside room on the lowest floor is close enough to reach in that time. A car\ntrying to outrun a mile-wide tornado is not. [RS] [VE third row: the car, struck through] A few minutes is\nenough to get below ground and not enough to get out of town, so know which one your house is before the day\ncomes.",
     "A storm shelter or an inside room on the lowest floor you can reach in that time, and a car\ntrying to outrun a mile-wide tornado is the one thing you can't. [RS] [VE third row: the car, struck through]\nKnow before the day comes which room in your house is the one you run to."),
    # 4 balanced contrast in A2-S3
    ("[PAY Q-A2] Thirty minutes was enough time, but it\nwasn't enough shelter. [HUMAN g-person Gilligan]",
     "[PAY Q-A2] Xenia got its thirty minutes and still had nowhere to put the people. [HUMAN g-person Gilligan]"),
    # 5 Georgia kicker
    ("That was four states between five\no'clock and seven, all off one storm system, and the sun was still up.",
     "Four states inside two hours, all off one\nstorm system, and the sun was still up."),
    # 6 + 9 Brandenburg toll and the misrouted promise (A1-S1)
    ("would lose thirty one people. [Q Q-A1]\nThe warning worked there, but the warning wasn't the thing that saved anybody, and the reason why starts on a\nhill above the Ohio River.",
     "would lose twenty eight people, and thirty one along the whole path. [Q Q-A1]\nThe warning reached that town in time, and it still lost twenty eight people, and the reason is what was under\nthe houses."),
    # 7 + 8 A4-S3 toll line
    ("By midnight there was nothing left to count but the dead, three hundred and\nthirty of them by the government's number, and five thousand four hundred and eighty four hurt.",
     "Three hundred and thirty people were dead by NOAA's count, and five thousand four\nhundred and eighty four were hurt."),
    # 8 decoration lines
    ("One machine made all of them, and it ran for the better part of a day.\nThat's an outbreak. [RS]",
     "One machine made all of them, and it ran for the better part of a day. [RS]"),
    ("while he talked. One man, one\nhelicopter and one radio station, and that was the warning. [PAY Q-A3] Two people died",
     "while he talked. [PAY Q-A3] Two people died"),
    # 10 A6-S1b garble
    ("and the researchers, they said why in two words, most likely: better warnings.",
     "and the researchers said the reason was most likely better warnings."),
    # Indiana clock: Monticello 5:17 PM is local (Indiana kept EST in 1974); drop the zone claim
    ('g-clock "5:17 PM EDT" · Monticello', 'g-clock "5:17 PM" · Monticello'),
    ("At 5:17 PM it went through the middle of Monticello,", "At 5:17 PM, local time, [verify: Indiana on EST in 1974] it went through the middle of Monticello,"),
]
for a, b in pairs:
    n = t.count(a)
    assert n == 1, (n, a[:70])
    t = t.replace(a, b)
p.write_text(t, encoding="utf8")
print("v7 applied:", len(pairs), "edits")

# fact sheet: the timeline table converted 21:37 UTC with UTC-5; EDT is UTC-4 (v6 grader)
f = root / "research" / "fact_sheet.md"
s = f.read_text(encoding="utf8")
old = "| 21:37–21:59 | 4:37–4:59 PM EDT | Louisville, KY"
assert s.count(old) == 1
s = s.replace(old, "| 21:37–21:59 | 5:37–5:59 PM EDT | Louisville, KY")
f.write_text(s, encoding="utf8")
print("fact sheet Louisville row fixed (21:37 UTC = 5:37 PM EDT)")
