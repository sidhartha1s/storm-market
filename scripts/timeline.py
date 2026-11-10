"""How the gates read index.html's timed elements: the one owner.

Each gate used to read tag attributes with its own regex that assumed one attribute order, so a valid tag written
in another order (every data-cut-by mount puts the attribute between id and src) dropped out of the check silently
(audit G1, G5, G6, G7, G11). Gates read tags through here instead: attributes as a dict, any order, and a
commented-out tag is not mounted.
"""
import re

ATTR = re.compile(r'([\w-]+)(?:="([^"]*)")?')


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


def is_narration(eid):
    """The narrator's segments are `nx-*`; `nx-ins*` is an insert (another voice) that kept the nx- prefix."""
    return bool(re.match(r"nx-(?!ins)", eid))


def is_insert(eid):
    """Archival or outside audio and voiced clips: `ins-*`, and `nx-ins*` (see is_narration)."""
    return bool(re.match(r"(?:nx-)?ins", eid))


def voiced(attrs):
    """A clip whose own sound plays at full level (data-volume="1"): Paul's lines, the CTA, voiced inserts."""
    return bool(re.fullmatch(r"1(?:\.0+)?", attrs.get("data-volume", "")))
