"""Self-check for scripts/hook_shape.py: python3 scripts/test_hook_shape.py

Runs the pure check on plain values, and reads the menu from the REAL script-quickref.md so a
menu edit that breaks the parser fails here.
"""
import sys
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
print("test_hook_shape PASS")
