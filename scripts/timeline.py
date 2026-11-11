"""How the gates read index.html's timed elements: the one owner.

Each gate used to read tag attributes with its own regex that assumed one attribute order, so a valid tag written
in another order (every data-cut-by mount puts the attribute between id and src) dropped out of the check silently
(audit G1, G5, G6, G7, G11). Gates read tags through here instead: attributes as a dict, any order, and a
commented-out tag is not mounted.
"""
import hashlib
import re

ATTR = re.compile(r'([\w-]+)(?:="([^"]*)")?')
STAMP = "gates_passed.marker"  # run_gates.py writes digest() here when every gate is green; gitignored (*.marker)


def digest(ep):
    """The one hash of the timeline the gates check (run_gates.py stamps it, render_preflight.py compares it): index.html,
    compositions/*.html and audio/*.words.json, as bytes with their names. words.json is in because the gates time
    against it and every TTS run rewrites it with its wav; wav and media bytes are out (GBs per episode, and
    render_preflight.py runs media_budget.py on the media itself)."""
    h = hashlib.sha256()
    for p in sorted([*ep.glob("index.html"), *ep.glob("compositions/*.html"), *ep.glob("audio/*.words.json")]):
        h.update(p.relative_to(ep).as_posix().encode() + b"\0" + hashlib.sha256(p.read_bytes()).digest())
    return h.hexdigest()


def live(html):
    """The page without its comments: a commented-out tag is not mounted."""
    return re.sub(r"<!--.*?-->", "", html, flags=re.S)


def mounts(html, names="audio|video"):
    """(tag, {attribute: value}) for every <names> tag outside comments, in page order; a bare attribute maps to ''."""
    tag = re.compile(rf'<({names})\b((?:[^>"]|"[^"]*")*)>', re.I)
    return [(t.lower(), dict(ATTR.findall(attrs))) for t, attrs in tag.findall(live(html))]


def window(attrs):
    """(start, end) in timeline seconds."""
    start = float(attrs["data-start"])
    return start, start + float(attrs["data-duration"])


def windows(html):
    """Every element on a track (data-start, data-duration, data-track-index), outside comments, in page order:
    dict(kind, attrs, tag, at, dur, tr, src). `src` is the element's own src or, for a src-less element that is not a
    composition host, the first src inside its OWN body: reading ahead 900 chars took the next element's file, so a
    designed <section> was reported as the film cut after it (Galveston A5, 30 Oct 26)."""
    page = live(html)
    out = []
    for m in re.finditer(r'<(section|video|div|img)\b((?:[^>"]|"[^"]*")*)>', page, re.I):
        kind, a = m.group(1).lower(), dict(ATTR.findall(m.group(2)))
        if not ("data-start" in a and "data-duration" in a and "data-track-index" in a):
            continue
        src = a.get("src")
        if not src and not a.get("data-composition-id"):
            close = re.search(rf"</{kind}>", page[m.end():m.end() + 900])
            inner = re.search(r'src="([^"]+)"', page[m.end():m.end() + (close.start() if close else 900)])
            src = inner.group(1) if inner else None
        out.append(dict(kind=kind, attrs=a, tag=m.group(0), at=float(a["data-start"]), dur=float(a["data-duration"]),
                        tr=int(a["data-track-index"]), src=src))
    return out


PICTURE_TRACKS = (1, 2)  # 1 = stills and clips, 2 = full-frame graphics; tracks above are overlays, not picture
# One frame at the 30 fps render (config.yaml render.fps) is 0.033 s: a hole wider than this can render a black frame.
# Narrower than a frame is float noise. Lint used 0.03, sweep and clip_report 0.05 (a 0.04 s hole passed sweep, R7).
COVER_TOLERANCE = 0.03


def picture_holes(wins, total):
    """(start, end) of every stretch of [0, total] that no picture-track window covers (windows() dicts)."""
    cur, holes = 0.0, []
    for w in sorted((w for w in wins if w["tr"] in PICTURE_TRACKS), key=lambda w: w["at"]):
        if w["at"] > cur + COVER_TOLERANCE:
            holes.append((cur, w["at"]))
        cur = max(cur, w["at"] + w["dur"])
    if cur < total - COVER_TOLERANCE:
        holes.append((cur, total))
    return holes


def is_narration(eid):
    """The narrator's segments are `nx-*`; `nx-ins*` is an insert (another voice) that kept the nx- prefix."""
    return bool(re.match(r"nx-(?!ins)", eid))


def is_insert(eid):
    """Archival or outside audio and voiced clips: `ins-*`, and `nx-ins*` (see is_narration)."""
    return bool(re.match(r"(?:nx-)?ins", eid))


def muted(tag):
    """The bare `muted` attribute on a tag string; a class or attribute that merely contains "muted" is not it."""
    return bool(re.search(r"\smuted(?=[\s>/=]|$)", re.sub(r'"[^"]*"', '""', tag)))


def voiced(attrs):
    """A clip whose own sound plays at full level (data-volume="1"): Paul's lines, the CTA, voiced inserts."""
    return bool(re.fullmatch(r"1(?:\.0+)?", attrs.get("data-volume", "")))
