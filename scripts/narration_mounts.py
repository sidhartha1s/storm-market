"""The one model of a TTS segment cut around Paul's on-camera clip (references/mg-quickref.md "Partial mounts").

A narration wav may be mounted as several <audio> tags with the same src, each playing
[data-media-start, data-media-start + data-duration] of the wav. The ranges must not overlap and must
stay inside the wav. A part of the wav no mount plays is a hole: it passes only when the mount beside it
declares data-cut-by="ins-paul-<n>", a voiced Paul clip (data-volume="1") that plays in the gap the cut
leaves, starting at most MAX_GAP after that mount ends (or ending at most MAX_GAP before it starts).
A graphic host cut short for Paul declares the same attribute. sweep_episode.py and lint_timeline.py
both read it here; anything undeclared fails as it did before the model existed.
"""
import re

TOL = 0.05     # seconds a declared Paul clip may overlap the mount it replaces (a seam, not a double voice)
MAX_GAP = 4.0  # lint_timeline MAX_QUIET: a longer silence between the cut and Paul is dead air anyway


def num(tag, attr, default=None):
    m = re.search(rf'\s{attr}="([\d.]+)"', tag)
    return float(m.group(1)) if m else default


def paul_lines(html):
    """{id: (start, end)} of every voiced ins-paul clip."""
    out = {}
    for m in re.finditer(r'<video\b[^>]*\sid="(ins-paul-[^"]*)"[^>]*>', html):
        t = m.group(0)
        s, d = num(t, "data-start"), num(t, "data-duration")
        if s is not None and d is not None and re.search(r'data-volume="1(?:\.0+)?"', t):
            out[m.group(1)] = (s, s + d)
    return out


def declared_cut(tag, paul, after=None, before=None):
    """True when tag's data-cut-by names a voiced Paul clip that starts just after `after` (the mount's
    end) or ends just before `before` (its start)."""
    m = re.search(r'\sdata-cut-by="([^"]+)"', tag)
    w = paul.get(m.group(1)) if m else None
    if not w:
        return False
    return ((after is not None and -TOL <= w[0] - after <= MAX_GAP)
            or (before is not None and -TOL <= before - w[1] <= MAX_GAP))


def segment_findings(tags, wav_dur, paul, tol):
    """(kind, message) for every problem with the mounts (tags) of one wav: "past" a mount playing past
    the wav, "overlap" two mounts playing the same words, "hole" wav no mount plays and no Paul cut declares."""
    mounts = sorted((num(t, "data-media-start", 0.0), num(t, "data-start"), num(t, "data-duration"), t) for t in tags)
    out = []
    for ms, s, d, t in mounts:
        if ms + d > wav_dur + tol:
            out.append(("past", f"plays wav {ms:g}-{ms + d:.2f}s, past its end {wav_dur:.2f}s"))
    for (ms1, s1, d1, t1), (ms2, s2, d2, t2) in zip(mounts, mounts[1:]):
        if ms1 + d1 > ms2 + tol:
            out.append(("overlap", f"two mounts both play wav {ms2:g}-{ms1 + d1:.2f}s"))
    # holes: before the first mount, between mounts, after the last
    played = sum(m[2] for m in mounts)
    cur, prev = 0.0, None
    for nxt in mounts + [None]:
        hi = nxt[0] if nxt else wav_dur
        if hi - cur > tol and not ((prev and declared_cut(prev[3], paul, after=prev[1] + prev[2]))
                                   or (nxt and declared_cut(nxt[3], paul, before=nxt[1]))):
            out.append(("hole", f"wav {cur:.2f}-{hi:.2f}s is never played (data-duration {played:g}s vs wav "
                                f"{wav_dur:.2f}s, diff {played - wav_dur:+.2f}s); a cut for Paul declares data-cut-by"))
        if nxt:
            cur, prev = max(cur, nxt[0] + nxt[2]), nxt
    return out
