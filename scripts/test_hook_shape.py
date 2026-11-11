"""Self-check for scripts/hook_shape.py: python3 scripts/test_hook_shape.py

Runs the pure check on plain values, and reads the menu from the REAL script-quickref.md so a
menu edit that breaks the parser fails here.
"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hook_shape as h

menu = h.menu_tags((Path(__file__).resolve().parent.parent / "references" / "script-quickref.md").read_text(encoding="utf-8"))
assert len(menu) >= 6 and "belief-question" in menu and "clock" in menu, menu

assert h.parse_tag("## H1\nHook shape: clock (2026-10-26)\n> line") == ("clock", "2026-10-26")
assert h.parse_tag("Hook shape: `pair` (2026-10-20)") == ("pair", "2026-10-20")
assert h.parse_tag("no tag here") is None

# episodes not numbered yet (number None) follow tag-date order among themselves
others = {"a": ("pair", "2026-10-20", None), "b": ("clock", "2026-10-22", None), "c": ("drop-in", "2026-10-25", None)}
# the 2 newest others are c (drop-in) and b (clock); a (pair) is older and free to reuse
assert h.check(("pair", "2026-10-26", None), others, menu) == []
assert h.check(("clock", "2026-10-26", None), others, menu) == ["hook shape `clock` repeats b (2026-10-22)"]
assert h.check(("drop-in", "2026-10-26", None), others, menu) == ["hook shape `drop-in` repeats c (2026-10-25)"]
assert h.check(None, others, menu)[0].startswith("no `Hook shape")
assert "not on the menu" in h.check(("riddle", "2026-10-26", None), others, menu)[0]
assert h.check(("pair", "2026-10-26", None), {}, menu) == []
# a hook dated before the others has no "last 2" among them (a later episode never blocks an earlier one)
assert h.check(("drop-in", "2026-10-01", None), others, menu) == []
# equal dates: the slug breaks the tie, so "last 2" never depends on worktree order
assert [s for s, _ in h.last_two({"x": ("pair", "2026-10-26", None), "y": ("clock", "2026-10-26", None), "z": ("flip", "2026-10-01", None)})] == ["y", "x"]

# G3: ship order is the E number, not the tag date. E08 and E09 were tagged 26 Oct, a day before E07 (27 Oct), so the
# date rule compared the next episode with E07 + E09 and never with E08 (repro-gates/seed/ep-e10-test).
shipped = {"ep-buffalo-2022": ("record", "2026-10-27", 7), "ep-appalachian-1950": ("drop-in", "2026-10-26", 8),
           "ep-galveston-1900": ("object", "2026-10-26", 9), "ep-mayfield-2021": ("pair", "2026-10-20", 6)}
assert h.check(("drop-in", "2026-11-11", None), shipped, menu) == ["hook shape `drop-in` repeats ep-appalachian-1950 (2026-10-26)"]
assert h.check(("record", "2026-11-11", None), shipped, menu) == []
assert h.check(("drop-in", "2026-11-11", 10), shipped, menu) != [] and h.check(("record", "2026-11-11", 10), shipped, menu) == []
# E07 is judged against E05/E06, never against E08/E09 that shipped after it
assert h.check(("object", "2026-10-27", 7), shipped, menu) == [] and h.check(("pair", "2026-10-27", 7), shipped, menu) != []
# an episode not numbered yet comes after every numbered one, whatever its tag date
assert [s for s, _ in h.last_two(dict(shipped, **{"ep-wip": ("flip", "2026-10-01", None)}))] == ["ep-wip", "ep-galveston-1900"]

# other_tags over two fake checkouts: own slug skipped, newest date per slug wins, untagged skipped
with tempfile.TemporaryDirectory() as d:
    def es(root, slug, body):
        p = Path(d) / root / "episodes" / slug
        p.mkdir(parents=True, exist_ok=True)
        (p / "edit_script.md").write_text(body, encoding="utf-8")
    es("main", "ep-a", "Hook shape: pair (2026-10-01)\n")
    es("wt", "ep-a", "Hook shape: clock (2026-10-20)\n")
    es("wt", "ep-me", "Hook shape: flip (2026-10-26)\n")
    es("wt", "ep-old", "## H1 no tag\n")
    got = h.other_tags([Path(d) / "main", Path(d) / "wt", Path(d) / "missing"], "ep-me")
    assert got == {"ep-a": ("clock", "2026-10-20", None)}, got
    # the E number comes from whichever checkout holds the metadata file (main, once the episode shipped)
    (Path(d) / "main" / "episodes" / "ep-a" / "E07-a-metadata.md").write_text("x", encoding="utf-8")
    got = h.other_tags([Path(d) / "main", Path(d) / "wt"], "ep-me")
    assert got == {"ep-a": ("clock", "2026-10-20", 7)}, got
print("test_hook_shape PASS")
