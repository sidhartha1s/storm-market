"""One-shot: split the 19 run-on sentences (>34 words) in edit_script.md at natural breaks."""
import pathlib, re

p = pathlib.Path(__file__).resolve().parent.parent / "edit_script.md"
t = p.read_text(encoding="utf8")

pairs = [
    ("and the charts for the third of April scared him enough that he called every weather\noffice in the eastern half of the country and told them to fix their radar that night and bring in extra\npeople the next day.",
     "and the charts for the third of April scared him. So he called every weather office in the\neastern half of the country and told them to fix their radar that night and bring in extra people the\nnext day."),
    ("He was right about the day and he was right\nabout the place, the watches went out, the warnings went out, and people still died, because in 1974 a\nwarning was a voice on the radio and a radio has to be switched on.",
     "He was right about the day and he was right\nabout the place. The watches went out, the warnings went out, and people still died, because in 1974 a\nwarning was a voice on the radio, and a radio has to be switched on."),
    ("Seven\nof those tornadoes sat at the top of a scale that was only three years old, and the man who invented that\nscale was about to fly over every one of those miles and doubt his own numbers.",
     "Seven\nof those tornadoes sat at the top of a scale that was only three years old. And the man who invented that\nscale was about to fly over every one of those miles and doubt his own numbers."),
    ("He spent that night carrying people out of the wreckage, a hundred and sixty\nnine of them by his own count, [RS] [VE popfig counter ticking to 169 over a Brandenburg still] including a\nbaby he had to take from a mother's arms so he could get her to safety.",
     "He spent that night carrying people out of the wreckage, a hundred and sixty\nnine of them by his own count. [RS] [VE popfig counter ticking to 169 over a Brandenburg still] One of them\nwas a baby he had to take from a mother's arms so he could get her to safety."),
    ("and at 4:40 it was in the middle of the city,\nhalf a mile to a mile wide, going through Windsor Park and Arrowhead, streets full of the houses people had\nbought after the war.",
     "and at 4:40 it was in the middle of the city,\nhalf a mile to a mile wide. It went through Windsor Park and Arrowhead, streets full of the houses people\nhad bought after the war."),
    ("[VE the scope, one sweep at a time] so a tornado showed up only as a hook on the edge of a storm, if it showed\nup at all.",
     "[VE the scope, one sweep at a time] So a tornado showed up only as a hook on the edge of a storm, if it showed\nup at all."),
    ("[VE the track advancing with his words; insert audio] while it\ntore the roof off Freedom Hall at the fairgrounds and wrecked the Crescent Hill water station.",
     "[VE the track advancing with his words; insert audio] It tore the\nroof off Freedom Hall at the fairgrounds and wrecked the Crescent Hill water station while he talked."),
    ("[VE popfig \"121\nMILES\"] and a railroad bridge over the Tippecanoe River was lifted off its footings and twisted.",
     "[VE popfig \"121\nMILES\"] A railroad bridge over the Tippecanoe River was lifted off its footings and twisted."),
    ("So two F5 tornadoes hit one small town an hour apart, and to this day nobody\ncan say for certain which one killed whom, because the people who could have told you were the ones under the\nsecond one.",
     "So two F5 tornadoes hit one small town an hour apart. To this day nobody can\nsay for certain which one killed whom, because the people who could have told you were the ones under the\nsecond one."),
    ("seven in nine\nhours from Indiana to Alabama, and by midnight there was nothing left to count but the dead, three hundred and\nthirty of them by the government's number, and five thousand four hundred and eighty four hurt.",
     "seven in nine\nhours from Indiana to Alabama. By midnight there was nothing left to count but the dead, three hundred and\nthirty of them by the government's number, and five thousand four hundred and eighty four hurt."),
    ("Now he had a hundred and forty eight tornadoes to\ngrade at once, so he flew, for ten months and more than ten thousand miles, low and slow, with every track\ndrawn by hand onto one map.",
     "Now he had a hundred and forty eight tornadoes to\ngrade at once, so he flew. Ten months, more than ten thousand miles, low and slow, with every track drawn\nby hand onto one map."),
    ("A well-built house with its walls gone is an F4,\nand the same house swept clean off its foundation, with the cars a hundred yards away and the trees stripped\nof their bark, is an F5.",
     "A well-built house with its walls gone is an F4.\nThe same house swept clean off its foundation, with the cars a hundred yards away and the trees stripped\nof their bark, is an F5."),
    ("run a jet stream above that to turn the whole column, and send a cold front through to set it\noff, from Illinois to Alabama, all afternoon and all night.",
     "run a jet stream above that to turn the whole column, and send a cold front through to set it\noff. That ran from Illinois to Alabama, all afternoon and all night."),
    ("Every storm that formed\nin that column had the same engine, and that's what an outbreak is, I mean, not a lot of tornadoes but one\nmachine making them for the better part of a day.",
     "Every storm that formed\nin that column had the same engine. That's what an outbreak is, I mean, not a lot of tornadoes but one\nmachine making them for the better part of a day."),
    ("[VE the card: rotation pattern vs straight-line pattern] and a tornado can't do that, because a\ntornado turns things.",
     "[VE the card: rotation pattern vs straight-line pattern] A tornado can't do that, because a\ntornado turns things."),
    ("Nothing in the science of 1974 explained it, so a few years later he gave it a name, the\nmicroburst, and it went on to explain why airliners were falling out of the sky near thunderstorms.",
     "Nothing in the science of 1974 explained it, so a few years later he gave it a name, the\nmicroburst. It went on to explain why airliners were falling out of the sky near thunderstorms."),
    ("[VE row lights] and the case\nfor a radar that could see wind finally had its evidence, and the Doppler network that watches the same sky\ntoday grew out of days like this one.",
     "[VE row lights] The case\nfor a radar that could see wind finally had its evidence, and the Doppler network that watches the same sky\ntoday grew out of days like this one."),
    ("[RS] [VE popfig \"132 MILES · 72 DEAD\"] and in Limestone County it ran straight down the\n1974 Tanner corridor.",
     "[RS] [VE popfig \"132 MILES · 72 DEAD\"] In Limestone County it ran straight down the\n1974 Tanner corridor."),
    ("A storm shelter is thirty seconds away, an inside room on the lowest floor is a minute, and a car\ntrying to outrun a mile-wide tornado is the one thing every survivor on this map would tell you not to do.",
     "A storm shelter is thirty seconds away, and an inside room on the lowest floor is a minute. A car\ntrying to outrun a mile-wide tornado is the one thing every survivor on this map would tell you not to do."),
]
for a, b in pairs:
    assert t.count(a) == 1, a[:60]
    t = t.replace(a, b)
p.write_text(t, encoding="utf8")
print("splits applied:", len(pairs))
