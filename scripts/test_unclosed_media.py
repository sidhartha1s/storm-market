"""Self-check for lint_timeline's unclosed-media check: python3 scripts/test_unclosed_media.py

Fixture: Camille's index.html at 339244b6^ (branch claude/ep-camille-1969-rebased), where
<video id="ins-paul-6" ...> was never closed and draft 1 rendered black after 625 s. It must be named; the same file
with the tag closed (what 339244b6 did) must be clean.
"""
import sys
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import lint_timeline  # noqa: E402

broken = (S / "fixtures" / "unclosed_media" / "ep-camille-1969-339244b6-parent.html").read_text(encoding="utf-8")
start = broken.index('<video id="ins-paul-6"')
end = lint_timeline.MEDIA_TAG.search(broken, start).end()
fixed = broken[:end] + "</video>" + broken[end:]
FAILS = []


def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


check("Camille 339244b6^ names ins-paul-6", lint_timeline.unclosed_media(broken) == ["ins-paul-6"])
check("Camille with ins-paul-6 closed is clean", lint_timeline.unclosed_media(fixed) == [])
check("a commented-out open tag is ignored", lint_timeline.unclosed_media('<!-- <audio id="x"> --><audio id="y"></audio>') == [])
check("an audio left open at the end is named", lint_timeline.unclosed_media('<audio id="a" src="a.wav">') == ["a"])

if FAILS:
    sys.exit(f"{len(FAILS)} check(s) failed")
print("all unclosed-media checks passed")
