"""One-shot: apply the v5 grader's fixes (research/script_review_v5.md) to edit_script.md -> v6."""
import pathlib

p = pathlib.Path(__file__).resolve().parent.parent / "edit_script.md"
t = p.read_text(encoding="utf8")

pairs = [
    # header
    ("Script v5\n(v1 graded", "Script v6\n(v1 graded"),
    ("v5 is the spoken-sentence pass on the palette in\n`references/humanise-rules.md`; owner length decision: natural 19 to 20 min).",
     "v5 is the spoken-sentence pass on the palette in\n`references/humanise-rules.md`; v6 applies the v5 grade, `research/script_review_v5.md`, 7/10: six fact\nerrors, opener cap, comma splices; owner length decision: natural 19 to 20 min)."),
    # hook: popfig time + "worst ones"
    ('[VE g-radar: five hooks on one scope, popfig "4:45 PM"] Five\ntornadoes on one radar screen at once, and the worst ones hadn\'t even formed yet.',
     '[VE g-radar: five hooks on one scope, popfig "5 HOOKS · ONE SCREEN"] Five\ntornadoes on one radar screen at once, and the worst of the night hadn\'t even formed yet.'),
    # I: opener + watch claim sourced; first F5 line
    ("[RS] Here's the thing. Many people that\nyear didn't even know what a tornado watch was. [verify]",
     "[RS] After it was over, the Weather Bureau found that most people didn't know\nit could forecast a tornado at all, or what a tornado watch was. [verify wording]"),
    ("The first tornado\ntouched down at 2:16 PM over empty ground, where there was nobody to warn, and that was the last time that\nwould be true all day. [Q]",
     "The first F5 touched\ndown at 2:16 PM over farm country, and for the next eight hours every one that followed found a town. [Q]"),
    # A1-S1: 74 minutes
    ("Ninety\nminutes later a town with a warning, with fifteen minutes to get ready, would lose thirty one people.",
     "An hour and\na quarter later a town with a warning, with fifteen minutes to get ready, would lose thirty one people."),
    # A1-S1b: doubled negative, squall line, fluff
    ("and on that campus nobody died, not one person. The\ncollege still calls it a miracle, and nobody has ever fully explained it. Down the hill in the town of Madison\nseven people died, eleven along that one track, and it was the same wind in the same minutes.",
     "and on that campus nobody died. The college still calls\nit a miracle. Down the hill in the town of Madison seven people died from the same line of storms, in the\nsame minutes."),
    # A1-S2: fluff + population verify
    ("they had fifteen minutes, [VE clock] and that was good for 1974.", "they had fifteen minutes. [VE clock]"),
    ("from a town\nof seventeen hundred,", "from a town\nof seventeen hundred, [verify population]"),
    # A1-S3: north-east
    ("to the north-east, in Xenia", "to the northeast, in Xenia"),
    # A2-S1: check-in + fragment
    ("And Xenia still became the worst-hit town of the whole day, right? [Q Q-A2] So why? At\n4:33",
     "Xenia still became the worst-hit town of the whole day. [Q Q-A2] At\n4:33"),
    # A2-S3: four minutes + fluff; add the Guard beat
    ("thirty two of them inside the city, in about four minutes, and about twelve\nhundred were hurt.",
     "thirty two of them inside the city, and about twelve hundred were\nhurt."),
    ("[PAY Q-A2] Thirty minutes was enough time, but it wasn't enough shelter, and Xenia is still the tornado\npeople mean when they talk about that day.",
     "[PAY Q-A2] Thirty minutes was enough time, but it\nwasn't enough shelter. [HUMAN g-person Gilligan] That same evening Governor John Gilligan sent two hundred\nand fifty National Guardsmen into Xenia, and by midnight fourteen hundred and forty five were on duty across\nOhio, more than half of them in this one town. [RS] [VE popfig \"1,445 GUARDSMEN\"] They spent the night\npulling people out of the houses on Windsor Park and Arrowhead, street by street, with the power out and the\nrain still coming down. [verify rescue detail]"),
    ("**A2-S3 (100 w)", "**A2-S3 (170 w)"),
    # A2-S4: fifty miles
    ("and forty miles away in Cincinnati", "and fifty miles away in Cincinnati"),
    # A3-S1: fluff
    ("Xenia stayed an F5,\nand the afternoon wasn't over.", "Xenia stayed an F5."),
    # A3-S2: opener, comma splice, verbatim card
    ("Now look at the\nradar at the Cincinnati weather office. It was built in 1960, and it could see rain but it couldn't see wind,\n[VE the scope, one sweep at a time] So a tornado",
     "The radar at the\nCincinnati weather office was built in 1960, and it could see rain but it couldn't see wind.\n[VE the scope, one sweep at a time] So a tornado"),
    ("and the reason it gave was one line: [VE citation\ncard, verbatim] based on hook echoes on the radar. [RS]",
     "and the reason it gave was hook echoes on the radar. [VE citation\ncard: the 4:05 PM warning, full clause] [RS]"),
    # A3-S2b: fluff + 15 tornadoes unpinned
    ("and it also recorded seven dead in its area, and both of those were true. Across the\nmap at that hour, fifteen tornadoes were on the ground at the same time. [verify]",
     "and it also recorded seven dead in its area. Somewhere in that evening, fifteen\ntornadoes were on the ground at the same time. [verify: Wikipedia only, no clock time in any source]"),
    # A3-S3: comma splice
    ("where it was and where it was going,\n[VE the track advancing with his words; insert audio] It tore the",
     "where it was and where it was going.\n[VE the track advancing with his words; insert audio] It tore the"),
    ("5:37 PM, Eastern time, [verify] and the radar", "5:37 PM, Eastern time, [verify: fact_sheet table converts 21:37 UTC to 4:37, the addendum says 5:37; 21:37 UTC is 5:37 PM EDT] and the radar"),
    # A3-S4: comma splice
    ("fell straight through to the first, [VE popfig \"121\nMILES\"] A railroad bridge",
     "fell straight through to the first. [VE popfig \"121\nMILES\"] A railroad bridge"),
    # A3-S5: distance + four states
    ("And about four hundred miles south, in Georgia,", "And more than four hundred miles south, in Georgia,"),
    ("That was five states in one\nhour, from one storm system, and the sun was still up.",
     "That was four states between five\no'clock and seven, all off one storm system, and the sun was still up."),
    # A4-S1: Tanner deaths, flashlights, neighbours
    ("Twenty eight people died, most of them in and around the town of Tanner, and by 7:30 PM the\nneighbours were out in the wreckage with flashlights pulling people out.",
     "Twenty eight people died along its fifty two miles, from Lawrence County through Limestone, and by\n7:30 PM the neighbors were out in the wreckage pulling people out."),
    # A4-S2: Guin population, strike time, in the dark
    ("a town of about two thousand five hundred people, and it got there at about 9 PM.",
     "a town of about two thousand five hundred people, [verify population] and it got there in full dark,\nabout two hours after sunset. [verify strike time]"),
    # A4-S3: McGuire, nine hours
    ("The town's\npharmacist, Mildred McGuire, survived", "Mildred\nMcGuire, who ran McGuire Drugs, survived"),
    ("seven in nine\nhours from Indiana to Alabama.", "seven between two in\nthe afternoon and eleven at night, from Indiana to Alabama."),
    # A5-S2: opener, fluff
    ("Here is what he was reading. [VE card: a house in two states]", "He was grading by what was left. [VE card: a house in two states]"),
    ("That is what an F5 looks like from the ground, and Fujita read ten thousand miles of it from the\nair, and seven times he wrote the top of his scale.",
     "Fujita read ten thousand miles of that from the air, and seven times he wrote the top of his\nscale."),
    # A5-S3: Illinois, aside, roadmap
    ("off. That ran from Illinois to Alabama, all afternoon and all night.", "off. That ran from Indiana to Alabama, all afternoon and all night."),
    ("That's what an outbreak is, I mean, not a lot of tornadoes but one\nmachine making them for the better part of a day. [RS]",
     "One machine made all of them, and it ran for the better part of a day.\nThat's an outbreak. [RS]"),
    ("another off the same column] But the map's biggest finding wasn't the engine.", "another off the same column]"),
    # A5-S4: comma splices
    ("like hair that had been\ncombed, [RS] [VE the card: rotation pattern vs straight-line pattern] A tornado",
     "like hair that had been\ncombed. [RS] [VE the card: rotation pattern vs straight-line pattern] A tornado"),
    ("and weather offices got backup power, [VE row lights] The case", "and weather offices got backup power. [VE row lights] The case"),
    # A6-S1: 2011 birthplace, comma splice, source in the mouth
    ("an EF5 tornado came out of Mississippi,\ncrossed Alabama for a hundred and thirty two miles and killed seventy two people, the deadliest single tornado\nin the state's history, [RS] [VE popfig \"132 MILES · 72 DEAD\"] In Limestone County",
     "an EF5 tornado came down at Hackleburg,\nAlabama, and ran a hundred and thirty two miles across five counties, and it killed seventy two people, the\ndeadliest single tornado in the state's history. [RS] [VE popfig \"132 MILES · 72 DEAD\"] In Limestone County"),
    ("and afterward they said the paths matched almost exactly. [HUMAN citation\ncard]",
     "and afterward the local paper quoted them saying the paths matched almost exactly. [HUMAN citation\ncard]"),
    # A6-S1b: hedge, channel reference, first Tanner
    ("and the researchers, they said why in two words: better warnings. That's the whole story of this channel in\none county, and it's why the 1974 map still matters. [PAY L4]",
     "and the researchers, they said why in two words, most likely: better warnings. [PAY L4]"),
    ("where the second Tanner\ntornado ended,", "where the first Tanner\ntornado ended,"),
    # A6-S2: average lead time, thesis
    ("and today fifteen minutes is about\nthe average. [verify]", "and today a warning gives you\neight to fifteen. [verify: national average lead time]"),
    ("and three hundred and thirty people died because a correct warning couldn't\ntravel. Today the warning travels, and the houses moved into the path instead.",
     "and three hundred and thirty people still died, because a warning is only as good as the\nradio it plays on and the basement you can reach. Today the warning reaches you, and the houses moved into\nthe path instead."),
    # A6-S3: worry line, fifteen minutes, invented seconds, attribution
    ("It was just a bad day, he said, and that's the part that should worry you, because the day\nwasn't rare.",
     "It was just a bad day, he said, and days like it come back every few decades."),
    ("and today the warning buys you fifteen minutes. [VE card,\nthree rows] A storm shelter is thirty seconds away, and an inside room on the lowest floor is a minute. A car\ntrying to outrun a mile-wide tornado is the one thing every survivor on this map would tell you not to do.\n[RS] [VE third row: the car, struck through] Fifteen minutes is enough to get below ground and not enough to\nget out of town, so know which one your house is before the day comes.",
     "and today the warning buys you minutes. [VE card,\nthree rows] A storm shelter or an inside room on the lowest floor is close enough to reach in that time. A car\ntrying to outrun a mile-wide tornado is not. [RS] [VE third row: the car, struck through] A few minutes is\nenough to get below ground and not enough to get out of town, so know which one your house is before the day\ncomes."),
]
for a, b in pairs:
    n = t.count(a)
    assert n == 1, (n, a[:70])
    t = t.replace(a, b)
p.write_text(t, encoding="utf8")
print("v6 applied:", len(pairs), "edits")
