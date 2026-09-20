"""One-shot: apply research/fact_qc.md (9 CORRECTED + 5 UNSOURCED rewrites) -> script v10. Prints the segment ids touched."""
import pathlib, re

root = pathlib.Path(__file__).resolve().parent.parent
p = root / "edit_script.md"
t = p.read_text(encoding="utf8")

pairs = [
    ("Script v9\n(v1 graded", "Script v10\n(v1 graded"),
    ("fragments; owner length decision: natural 19 to 20 min).",
     "fragments; owner hook + intro edits 21 Sep 26; v10 applies `research/fact_qc.md`, 9 corrected, 5 unsourced\nrewritten; owner length decision: natural 19 to 20 min)."),
    # I-1
    ("[RS] After it was over, the Weather Bureau found that most people didn't know it could forecast a tornado at all, or what a tornado watch was. [verify wording]",
     "[RS] Nine years earlier the Weather Bureau had found that people did not know it could forecast a tornado at all. This time the surveys found the opposite. Most people knew the storms were coming, and most of them did the right thing."),
    # A1-S2
    ("from a town\nof seventeen hundred, [verify population] and thirty one people were dead along its path.",
     "from a town\nof sixteen hundred people, and thirty one people were dead along its path."),
    ("Fifteen minutes is\nenough to get below ground, but few homes in Brandenburg had a below ground to get to. [verify] [HUMAN]",
     "Fifteen minutes is\nenough to get below ground, and at Brandenburg a hundred and twenty eight homes were levelled or swept away\nanyway. [HUMAN]"),
    # A2-S3
    ("They spent the night\npulling people out of the houses on Windsor Park and Arrowhead, street by street, with the power out and the\nrain still coming down. [verify rescue detail]",
     "They stayed for weeks,\nhelping with the rescue and the clean up, and standing guard over what was left of the houses on Windsor Park\nand Arrowhead."),
    # A3-S2
    ("[RS] Twenty seven minutes later the hook it was looking at\ncame through Sayler Park on the west side of Cincinnati, and four people died in that county. [verify] By then",
     "[RS] The county stayed under that warning, and the office\nrenewed it at 4:45 PM. An hour and a half after the first one went out, the hook came through Sayler Park on the\nwest side of Cincinnati, and four people died in that county. By then"),
    # A3-S2b
    ("Somewhere in that evening, fifteen\ntornadoes were on the ground at the same time. [verify: Wikipedia only, no clock time in any source]",
     "Somewhere in that evening the outbreak\npeaked, and the counts from that night put as many as fifteen tornadoes on the ground at once."),
    # A4-S1
    ("At 6:20 PM, Central time,\na tornado formed near Moulton, Alabama, and stayed on the ground for fifty two miles. [verify duration: table 6:20 to 7:21 PM, prose about\n90 min] [VE track] Twenty eight people died along that first tornado's fifty two miles, from Lawrence County into\nLimestone,",
     "At about 6:30 PM, Central\ntime, a tornado came down in north Alabama, and it stayed on the ground county after county, all the way\nfrom Lawrence into Limestone. [VE track] Twenty eight people died along that first tornado's path,"),
    ("Between the two of them, sixteen people died in Limestone County alone, [verify] and about fifty across\nthat stretch of north Alabama. [verify]",
     "Between the two of them, sixteen people died in Limestone County alone, and fifty five in all, and that was\nwell over half of everyone Alabama lost that day."),
    # A4-S2
    ("a town of about two thousand five hundred people, [verify population] and it got there in full dark,\nabout two hours after sunset. [verify strike time]",
     "a town of about two thousand two hundred people, and it got there in full dark, about two hours\nafter sunset."),
    ("Seven hundred and thirty seven houses\nwere destroyed in Guin that night, and twenty eight people died. [verify: 28 official / 32 revised]",
     "Twenty three people died in Guin that night.\nAlong the whole hundred mile track the tornado destroyed seven hundred and thirty seven houses and killed twenty\neight."),
    # A5-S3
    ("off. That ran from Indiana to Alabama, all afternoon and all night. [verify synoptic summary] Every storm that formed\nin that column had the same engine. One machine made all of them, and it ran for the better part of a day. [RS]",
     "off. That set up stretched from Indiana to Alabama, and it held all afternoon and all night. The storms came up\nin three long lines, and every one of them ran on the same engine. [RS]"),
    # A6-S2
    ("April third can happen again, because\nthe ingredients were ordinary spring weather for that part of the country arriving on the same\nday, and every few decades they do. [verify]",
     "April third can happen again, because\nthe ingredients were ordinary spring weather for that part of the country arriving on the same\nday."),
    ("and today it's the phone in your pocket, and it will wake you up. [verify\nWEA]",
     "and today a tornado warning sets off the phone in your pocket, with a tone and a buzz that most phones\nwill play even on silent."),
    ("and today the average warning\nruns eight to fifteen minutes everywhere. [verify: national average lead time]",
     "and today the average tornado\nwarning gives you about thirteen minutes."),
    # A6-S3
    ("It was just a bad day, he said, and days like it come back every few decades.",
     "It was just a bad day, he said, and the same ground has already taken another one."),
]
for a, b in pairs:
    n = t.count(a)
    assert n == 1, (n, a[:70])
    t = t.replace(a, b)
p.write_text(t, encoding="utf8")
print("v10 applied:", len(pairs), "edits; verify tags left:", len(re.findall(r"\[verify", t.split("### H · hook", 1)[1].split("## Fact register", 1)[0])))
