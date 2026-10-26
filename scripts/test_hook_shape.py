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

others = {"a": ("pair", "2026-10-20"), "b": ("clock", "2026-10-22"), "c": ("drop-in", "2026-10-25")}
# the 2 newest others are c (drop-in) and b (clock); a (pair) is older and free to reuse
assert h.check(("pair", "2026-10-26"), others, menu) == []
assert h.check(("clock", "2026-10-26"), others, menu) == ["hook shape `clock` repeats b (2026-10-22)"]
assert h.check(("drop-in", "2026-10-26"), others, menu) == ["hook shape `drop-in` repeats c (2026-10-25)"]
assert h.check(None, others, menu)[0].startswith("no `Hook shape")
assert "not on the menu" in h.check(("riddle", "2026-10-26"), others, menu)[0]
assert h.check(("pair", "2026-10-26"), {}, menu) == []
# a hook dated before the others has no "last 2" among them (a later episode never blocks an earlier one)
assert h.check(("drop-in", "2026-10-01"), others, menu) == []
# equal dates: the slug breaks the tie, so "last 2" never depends on worktree order
assert [s for s, _ in h.last_two({"x": ("pair", "2026-10-26"), "y": ("clock", "2026-10-26"), "z": ("flip", "2026-10-01")})] == ["y", "x"]

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
    assert got == {"ep-a": ("clock", "2026-10-20")}, got
print("test_hook_shape PASS")
