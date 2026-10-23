# Transcribe one Flow clip and compare its spoken words with the line it was meant to say.
# usage: clip_check.py <jobs.json> [clip.mp4]   (reads jobs[0].line; default clip is raw-01.mp4 beside the json)
# Two passes, because one whole-clip pass drops words that are really spoken (9 Oct 26, clip 2: ten words dropped):
# the whole clip, then each speech island between silences on its own. A word counts as missing only when BOTH miss it.
# Prints: both transcripts, missing / extra words, speech start and end, clip length. Exit 0 = every word heard, none added.
import json, os, re, subprocess, sys
from faster_whisper import WhisperModel

cfg = json.load(open(sys.argv[1], encoding="utf8"))
line = cfg["jobs"][0]["line"]
mp4 = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), "raw-01.mp4")
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()


def spell(n):
    if n < 20:
        return ONES[n]
    if n < 100:
        return TENS[n // 10] + ("" if n % 10 == 0 else " " + ONES[n % 10])
    if n < 1000:
        return ONES[n // 100] + " hundred" + ("" if n % 100 == 0 else " " + spell(n % 100))
    return spell(n // 1000) + " thousand" + ("" if n % 1000 == 0 else " " + spell(n % 1000))


def forms(tok):
    # the transcriber writes spoken numbers as digits: 80 is "eighty", 626 is "six twenty six", 1999 "nineteen ninety nine"
    n = int(tok)
    out = [spell(n)]
    if 100 <= n <= 9999 and n % 100:
        out.append(spell(n // 100) + " " + spell(n % 100))
    return out


ORDINAL = {"one": "first", "two": "second", "three": "third", "five": "fifth", "eight": "eighth", "nine": "ninth", "twelve": "twelfth"}


def ordinal(n):
    # "23rd" as the transcriber writes it, spoken "twenty third"
    words = spell(n).split()
    last = words[-1]
    words[-1] = ORDINAL.get(last) or (last[:-1] + "ieth" if last.endswith("y") else last + "th")
    return " ".join(words)


def norm(text, want=None):
    # Spoken and written numbers meet here: the transcriber writes "23rd" and "110" for a line that spells "twenty-third"
    # and "a hundred and ten" (Camille clip 4, 23 Oct 26). "a hundred" is "one hundred"; the "and" inside a number is dropped,
    # and so is every other "and": a swapped or dropped "and" keeps the meaning (owner retake bar, 18 Oct 26).
    text = text.lower().replace("-", " ")
    text = re.sub(r"\b(\d{1,4})(st|nd|rd|th)\b", lambda m: ordinal(int(m.group(1))), text)
    text = re.sub(r"\ba (hundred|thousand)\b", r"one \1", text)
    toks = []
    for t in re.sub(r"[^a-z0-9 ]", " ", text).split():
        if t == "and":
            continue
        if t.isdigit() and int(t) < 10000:
            fs = forms(t)
            t = next((f for f in fs if want and set(f.split()) <= set(want)), fs[0])
        toks += t.split()
    return toks


model = WhisperModel("small.en", device="cpu", compute_type="int8")
segs, _ = model.transcribe(mp4, word_timestamps=True)
words = [(w.word.strip(), round(w.start, 2), round(w.end, 2)) for s in segs for w in s.words]
json.dump(words, open(mp4.replace(".mp4", ".words.json"), "w"), indent=1)
whole = " ".join(w for w, _, _ in words)

probe = subprocess.run(["ffmpeg", "-v", "info", "-i", mp4, "-af", "silencedetect=n=-35dB:d=0.3", "-f", "null", "-"], capture_output=True, text=True).stderr
length = float(re.search(r"Duration: (\d+):(\d+):([\d.]+)", probe).group(3))
starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", probe)]
ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", probe)]
islands = []  # speech runs from the end of one silence (or the clip start) to the start of the next (or the clip end)
for a in sorted(set([0.0] + ends)):
    nxt = [b for b in starts + [length] if b > a]
    if nxt and min(nxt) - a > 0.2:
        islands = [i for i in islands if i[1] != min(nxt)] + [(a, min(nxt))]  # leading silence and its end share one island
parts = []
tmp = mp4.replace(".mp4", ".island.wav")
for a, b in islands:
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(max(0, a - 0.15)), "-to", str(b + 0.15), "-i", mp4, "-ar", "16000", "-ac", "1", tmp], check=True)
    s, _ = model.transcribe(tmp, beam_size=5, condition_on_previous_text=False)
    parts.append(" ".join(x.text.strip() for x in s))
os.remove(tmp)
by_island = " ".join(parts)

want = norm(line)
missing = [w for w in want if w not in norm(whole, want) and w not in norm(by_island, want)]
extra = [w for w in norm(by_island, want) if w not in want]
print("line      :", line)
print("whole clip:", whole)
print("by island :", " | ".join(parts))
print("missing in both passes:", missing or "none", "| extra words:", extra or "none")
print(f"speech {islands[0][0]:.2f} s to {islands[-1][1]:.2f} s, clip {length:.2f} s")
sys.exit(1 if missing or extra else 0)
