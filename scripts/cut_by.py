"""The cut-by mount: one rule for sweep_episode.py and lint_timeline.py.

A narration or graphic mounted with data-cut-by="<id>" was built for the whole line and is cut where the voiced
Paul clip <id> takes it over (references/mg-quickref.md "Gate-readable authoring"). Its data-duration is shorter than the wav or the
graphic's timeline by design, so the freshness, last-words and graphic-window checks exempt it, and only it.
"""
import re


def cut_by_ok(tag, html):
    """True when `tag` carries data-cut-by="<id>" and <id> is a <video> that starts within 0.1 s of the mount's
    end (start + duration). A cut-by that names nothing, or whose clip starts elsewhere, is not exempt."""
    cb = re.search(r'data-cut-by="([^"]+)"', tag)
    st, du = re.search(r'data-start="([\d.]+)"', tag), re.search(r'data-duration="([\d.]+)"', tag)
    if not (cb and st and du):
        return False
    end = float(st.group(1)) + float(du.group(1))
    tgt = re.search(r'<video\b[^>]*\bid="%s"[^>]*>' % re.escape(cb.group(1)), html)
    if not tgt:
        return False
    ts = re.search(r'data-start="([\d.]+)"', tgt.group(0))
    return bool(ts) and abs(float(ts.group(1)) - end) <= 0.1
