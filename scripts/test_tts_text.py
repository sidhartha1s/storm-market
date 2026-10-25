"""tts_clone.unsafe_spans: the lines Camille 1969 shipped broken are refused, clean narration passes.
Run: python3 scripts/test_tts_text.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from tts_clone import unsafe_spans

BROKEN = {  # real lines from episodes/ep-camille-1969 (25 Oct 26), with what must be caught
    "Dr. J. H. Gamble of Lovingston was in charge.": {"Dr.", "J.", "H."},
    "where it came ashore late on the night of August seventeenth, 1969.": {"1"},
    "Next door, Mrs. Wood used a wheelchair. But Mr. Wood would feel better.": {"Mrs.", "Mr."},
    "a 1968 Ford, and tried to get out.": {"1"},
    "The U.S. Weather Bureau said ninety percent of St. Louis flooded at 7 a.m.": {"U.", "S.", "St.", "7", "a."},
    "It rose 40% in an hour & kept going.": {"4", "%", "&"},
}
SAFE = [
    "Doctor Jay Aitch Gamble of Lovingston was in charge of identifying the people who were lost.",
    "late on the night of August seventeenth, nineteen sixty-nine. A hundred forty-three people lost their lives.",
    "Next door, Missus Wood used a wheelchair, and the Woods figured they'd take a chance.",
    "It's a small place on the Tye River, along Route fifty-six. Was it? No. Not one.",
    "The roof held, but the walls didn't. Thirty-five people were inside.",  # Moore 1999 h1-s2: the "t." of a contraction is not an initial
    "It won’t. Then the siren stopped.",
]

fails = 0
for line, want in BROKEN.items():
    got = {s[0] if s.isdigit() else s for s, _ in unsafe_spans(line)}
    if not want <= got:
        fails += 1; print(f"FAIL missed {sorted(want - got)} in {line!r}")
for line in SAFE:
    if unsafe_spans(line):
        fails += 1; print(f"FAIL false alarm {unsafe_spans(line)} in {line!r}")
print("test_tts_text:", "FAIL" if fails else f"PASS ({len(BROKEN)} broken caught, {len(SAFE)} clean passed)")
sys.exit(1 if fails else 0)
