"""One-shot: apply the v8 grader's fixes (research/script_review_v8.md) -> v9; doctrine tempo line."""
import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
p = root / "edit_script.md"
t = p.read_text(encoding="utf8")

pairs = [
    ("Script v8\n(v1 graded", "Script v9\n(v1 graded"),
    ("act seam chronology, opener cap; owner\nlength decision: natural 19 to 20 min).",
     "act seam chronology, opener cap; v9 applies the v8 grade, `research/script_review_v8.md`, 7/10, hook 8: A4 death\ncounts scoped, A2 seam chronology, A6 thesis said once, fragments; owner length decision: natural 19 to 20 min)."),
    # H: the verbless fragment
    ("[VE g-scale seven bars slam in]\nThree hundred and thirty people dead. [RS]",
     "[VE g-scale seven bars slam in]\nIt killed three hundred and thirty people. [RS]"),
    # A2-S4: Cincinnati came before Xenia
    ("and fifty miles away in Cincinnati the afternoon was about to get worse.",
     "and fifty miles west, in Cincinnati, another F5 had crossed the river eight minutes before Xenia was hit."),
    # A3-S2: dangling pronoun; Freedom Hall
    ("and then, at 5:40 PM, his\noffice went dark.", "and then, at 5:40 PM, the\noffice went dark."),
    ("It tore the\nroof off Freedom Hall", "It tore part of the\nroof off Freedom Hall"),
    # A3-S5: interval
    ("Four states inside two hours, all off one\nstorm system,", "Four states inside three hours, all off one\nstorm system,"),
    # A4-S1: scope both death counts
    ("Twenty eight people died along those miles, from Lawrence County through Limestone, and the\nneighbors",
     "Twenty eight people died along that first tornado's fifty two miles, from Lawrence County into\nLimestone, and the neighbors"),
    ("Sixteen people died in Limestone County that night, [verify] and about fifty in that one stretch\nof north Alabama. [verify]",
     "Between the two of them, sixteen people died in Limestone County alone, [verify] and about fifty across\nthat stretch of north Alabama. [verify]"),
    # A6: thesis once
    ("[Q Q-A6b] It will happen again, and what decides the count is whether the warning reaches you.",
     "[Q Q-A6b]"),
    ("[verify] What changed is the warning. [VE two columns]", "[verify] [VE two columns]"),
    ("Today the warning buys you minutes. [VE card,\nthree rows] A storm shelter or an inside room on the lowest floor you can reach in that time, and a car\ntrying to outrun a mile-wide tornado is the one thing you can't. [RS]",
     "[VE card,\nthree rows] Today those minutes get you to a storm shelter or an inside room on the lowest floor, and they\ndo not get a car past a mile-wide tornado. [RS]"),
]
for a, b in pairs:
    n = t.count(a)
    assert n == 1, (n, a[:70])
    t = t.replace(a, b)
p.write_text(t, encoding="utf8")
print("v9 applied:", len(pairs), "edits")

d = root.parent.parent / "references" / "script-os.md"
s = d.read_text(encoding="utf8")
old = "Documentaries keep the natural 150-158 wpm."
assert s.count(old) == 1
s = s.replace(old, "Documentaries run atempo 1.10 too (owner 20 Sep 26, on the ep-1974 hook probe).")
d.write_text(s, encoding="utf8")
print("script-os tempo line updated")
