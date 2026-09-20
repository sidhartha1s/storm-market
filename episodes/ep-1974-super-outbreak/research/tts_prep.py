"""Build audio/<id>.txt for every narration segment of edit_script.md (this episode's inline-tag format).

Strips [tags], *(stage directions)* and **segment headers**, spells clock times and numbers as words,
respells the known pocket-TTS homographs, and prints a per-segment word count. Segment ids: h, i-1, i-2,
a1-s1, a1-s1b, ... z. Run: python3 research/tts_prep.py   (from anywhere; paths are relative to this file)
"""
import re, pathlib

ep = pathlib.Path(__file__).resolve().parent.parent
md = ep / "edit_script.md"
out = ep / "audio"
out.mkdir(exist_ok=True)

script = md.read_text(encoding="utf8").split("### H · hook", 1)[1].split("## Fact register", 1)[0]
script = "### H · hook" + script

ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "zero ten twenty thirty forty fifty sixty seventy eighty ninety".split()


def n2w(n):
    n = int(n)
    if n < 20:
        return ONES[n]
    if n < 100:
        return TENS[n // 10] + ("" if n % 10 == 0 else " " + ONES[n % 10])
    if n < 1000:
        return ONES[n // 100] + " hundred" + ("" if n % 100 == 0 else " and " + n2w(n % 100))
    if n < 10000:
        return ONES[n // 1000] + " thousand" + ("" if n % 1000 == 0 else " " + n2w(n % 1000))
    return str(n)


def year(n):
    n = int(n)
    if 1900 <= n <= 1999:
        return "nineteen " + (n2w(n % 100) if n % 100 else "hundred")
    if 2000 <= n <= 2009:
        return "two thousand" + ("" if n == 2000 else " and " + ONES[n % 100])
    if 2010 <= n <= 2099:
        return "twenty " + n2w(n % 100)
    return n2w(n)


def clock(m):
    h, mi, ap = m.group(1), m.group(2), m.group(3)
    ap = "A M" if ap.upper() == "AM" else "P M"
    if mi == "00":
        return f"{n2w(h)} {ap}"
    if mi.startswith("0"):
        return f"{n2w(h)} oh {n2w(mi[1])} {ap}"
    return f"{n2w(h)} {n2w(mi)} {ap}"


def ordinal(m):
    n = int(m.group(1))
    words = {1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth", 7: "seventh", 8: "eighth",
             9: "ninth", 10: "tenth", 27: "twenty seventh"}
    return words.get(n, n2w(n) + "th")


HOMOGRAPHS = [(r"\bI read all of\b", "I reed all of"), (r"\bread all of them\b", "reed all of them")]


def clean(text):
    text = re.sub(r"\*\([^)]*\)\*", " ", text)          # stage directions
    text = re.sub(r"\[[^\]]*\]", " ", text)             # tags
    text = re.sub(r"\*\*[^*]*\*\*", " ", text)          # bold segment headers
    text = re.sub(r"`[^`]*`", " ", text)
    text = re.sub(r"(\d{1,2}):(\d{2}) ?(AM|PM|am|pm)\b", clock, text)
    text = re.sub(r"\b(\d{1,2})(?:st|nd|rd|th)\b", ordinal, text)
    text = re.sub(r"\b(1[89]\d\d|20\d\d)\b", lambda m: year(m.group(1)), text)
    text = re.sub(r"\b(\d{1,3}),(\d{3})\b", lambda m: n2w(m.group(1) + m.group(2)), text)
    text = re.sub(r"\b(\d+)\b", lambda m: n2w(m.group(1)), text)
    text = text.replace("F5", "F five").replace("F4", "F four").replace("F6", "F six").replace("EF5", "E F five")
    text = text.replace("WHAS", "W H A S").replace("NOAA", "Noah")
    text = text.replace("north-east", "northeast").replace("mile-wide", "mile wide").replace("well-built", "well built")
    text = text.replace("&", " and ")
    for a, b in HOMOGRAPHS:
        text = re.sub(a, b, text)
    text = re.sub(r"[“”]", '"', text).replace("’", "'")
    text = re.sub(r"\s+", " ", text).strip()
    return text


segs = []
for chunk in re.split(r"\n(?=### )", script):
    head, _, body = chunk.partition("\n")
    hid = re.match(r"### ([A-Z]\w*)", head).group(1)
    if hid == "CTA":
        continue
    # split acts into their **A1-S1 (...)** sub-segments; hook / intro / close are paragraphs
    parts = re.split(r"\n(?=\*\*[A-Z]\d-S\d[a-z]?\b)", body)
    if len(parts) > 1 and parts[0].strip() == "":
        parts = parts[1:]
    if hid in ("H", "I", "Z"):
        paras = [p for p in body.split("\n\n") if p.strip()]
        for k, p in enumerate(paras, 1):
            sid = hid.lower() if len(paras) == 1 else f"{hid.lower()}-{k}"
            segs.append((sid, clean(p)))
    else:
        for p in parts:
            m = re.match(r"\*\*([A-Z]\d-S\d[a-z]?)\b", p)
            if not m:
                continue
            segs.append((m.group(1).lower(), clean(p)))

total = 0
for sid, text in segs:
    if not text:
        continue
    (out / f"{sid}.txt").write_text(text, encoding="utf8")
    total += len(text.split())
    print(f"{sid:8s} {len(text.split()):4d}w  {text[:70]}")
leftover = [(sid, re.findall(r"\d", t)) for sid, t in segs if re.search(r"\d", t)]
print("segments", len(segs), "words", total, "digits left:", leftover)
