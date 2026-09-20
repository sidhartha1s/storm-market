"""One-shot: apply the v7 grader's fixes (research/script_review_v7.md) -> v8."""
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
p = root / "edit_script.md"
t = p.read_text(encoding="utf8")

pairs = [
    ("Script v7\n(v1 graded", "Script v8\n(v1 graded"),
    ("balanced-contrast reflex; owner length decision: natural 19 to 20 min).",
     "balanced-contrast reflex; v8 applies the v7 grade, `research/script_review_v7.md`, 7/10, hook 8: lead-time\nline inverted, Tanner duration left to fact-QC, misattributed quotes, act seam chronology, opener cap; owner\nlength decision: natural 19 to 20 min)."),
    # H: hooks are not tornadoes; stated open fact instead of the "So" opener
    ("Five\ntornadoes on one radar screen at once, and the worst of the night hadn't even formed yet.",
     "Five\ntornado hooks on one radar screen at once, and the worst of the night hadn't even formed yet."),
    ("knew it was coming a full day early. So if he knew, why did so many people die? [Q]",
     "knew it was coming a full day early. He knew, and three hundred and thirty people died anyway. [Q]"),
    # I: opener, overstated bridge
    ("scared him. So he called every weather office", "scared him. He called every weather office"),
    ("and for the next eight hours every one that followed found a town.", "and for the next eight hours most of the ones that followed found a town."),
    # A1-S1b Hanover count
    ("Thirty of the thirty three buildings were damaged", "More than thirty of its thirty three buildings were damaged"),
    # A1-S2 Brandenburg strike time, Haley quote
    ("At 3:30 PM, Central time, in\nBrandenburg, Kentucky, they had fifteen minutes. [VE clock]",
     "The tornado that hit Brandenburg,\nKentucky, formed at 3:30 PM, Central time, and the town had fifteen minutes of warning. [VE clock]"),
    ("He became a soldier later, and he said\nthat was still the hardest thing he ever did.",
     "He became a soldier later, and fifty years\non he called that night pretty, pretty traumatic."),
    # A1-S3 seam: Xenia and Brandenburg were simultaneous
    ("It wasn't yet four o'clock, and about\na hundred and seventy miles to the northeast, in Xenia, Ohio,",
     "While that tornado was still on the ground,\nabout a hundred and seventy miles to the northeast, in Xenia, Ohio,"),
    # A2-S3 payoff with the act's own facts
    ("[PAY Q-A2] Xenia got its thirty minutes and still had nowhere to put the people.",
     "[PAY Q-A2] Xenia got its thirty minutes, and the tornado still took five schools, fourteen hundred buildings\nand thirty four people, because thirty minutes moves you across a room, not out of a city."),
    # A2-S4 superlative
    ("the afternoon was about to get worse than any radar operator alive\nhad seen.", "the afternoon was about to get worse."),
    # A2-S5 hinge matches A3-S1
    ("and decided his own scale was too small.", "and wrote down a number his own scale did not have."),
    # A3-S2 duplicate + opener; invented singular
    ("[VE the scope, one sweep at a time] So a tornado showed up only as a hook on the edge of a storm, if it showed\nup at all. [Q Q-A3] So the office had to warn a city off a shape on the edge of a storm. At 4:05 PM",
     "[VE the scope, one sweep at a time] A tornado showed up only as a hook on the edge of a storm, if it showed up\nat all, so the office was warning a city off a shape. [Q Q-A3] At 4:05 PM"),
    ("By then\nthe man on duty was looking at five hooks at once,", "By then\nthe office was looking at five hooks at once,"),
    # A3-S3 Louisville geography
    ("an F4 came across the river into a city of three hundred and sixty thousand people at\n5:37 PM, Eastern time,",
     "an F4 touched down inside a city of three hundred and sixty thousand people at\n5:37 PM, Eastern time,"),
    # A3-S4 zone-dependent "same hour"
    ("In that same hour, up north, one tornado came down near Otterbein", "That same evening, up north, one tornado came down near Otterbein"),
    # A4-S1 Tanner duration: the sheet's table (61 min) and prose (90 min) disagree; leave it to fact-QC
    ("and stayed on the ground for about an hour and fifty two miles.\n[VE track] Twenty eight people died along its fifty two miles, from Lawrence County through Limestone, and by\n7:30 PM the neighbors were out in the wreckage pulling people out. That's when the second one came.",
     "and stayed on the ground for fifty two miles. [verify duration: table 6:20 to 7:21 PM, prose about\n90 min] [VE track] Twenty eight people died along those miles, from Lawrence County through Limestone, and the\nneighbors were out in the wreckage behind it pulling people out when the second one came."),
    # A4-S2 Becky Todd quote
    ("Becky Todd's family were in their car when it rolled, and she told them to hold on to the seats.",
     "Becky Todd was in the car with her family when it rolled, and she said George told them to grab the seats\nand hold on."),
    # A5-S1 opener
    ("Now he had a hundred and forty eight tornadoes to\ngrade at once,", "He had a hundred and forty eight tornadoes to\ngrade at once,"),
    # A6-S1b reveal-flip
    ("[Q Q-A6b] So the real question isn't whether it happens again, it's whether the warning reaches you.",
     "[Q Q-A6b] It will happen again, and what decides the count is whether the warning reaches you."),
    # A6-S2 lead-time line inverted
    ("A good warning in 1974 was fifteen minutes and most places got less, and today a warning gives you\neight to fifteen. [verify: national average lead time]",
     "Brandenburg got fifteen minutes that day and most towns got nothing at all, and today the average warning\nruns eight to fifteen minutes everywhere. [verify: national average lead time]"),
    # A6-S3 episode answer matches the evidence
    ("[PAY EPISODE] Pearson knew a day early, and it bought nobody anything without a radio and a\nbasement, and today the warning buys you minutes.",
     "[PAY EPISODE] Pearson knew a day early, and the warnings he set up saved the people who heard them, and\nin 1974 hearing one meant a radio that happened to be switched on. Today the warning buys you minutes."),
]
for a, b in pairs:
    n = t.count(a)
    assert n == 1, (n, a[:70])
    t = t.replace(a, b)
p.write_text(t, encoding="utf8")
print("v8 applied:", len(pairs), "edits")
