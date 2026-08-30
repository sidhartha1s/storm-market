import re

with open("vid.en.srt", encoding="utf-8") as f:
    content = f.read()

blocks = content.split("\n\n")
entries = []
for b in blocks:
    lines = b.strip().split("\n")
    if len(lines) < 3:
        continue
    time_line = lines[1]
    m = re.match(r"(\d{2}):(\d{2}):(\d{2}),\d+", time_line)
    if not m:
        continue
    h, mi, s = int(m.group(1)), int(m.group(2)), int(m.group(3))
    start = h*3600+mi*60+s
    text = " ".join(lines[2:]).strip()
    entries.append((start, text))

# Rolling captions: each entry contains overlapping words with previous.
# Take the last line of each caption block progressively - approximate dedup by
# picking new words only.
seen_text = ""
out = []
for start, text in entries:
    if text and text not in seen_text:
        # find new suffix
        words = text.split()
        seen_words = seen_text.split()
        # find overlap
        overlap = 0
        maxo = min(len(words), len(seen_words))
        for k in range(maxo, 0, -1):
            if seen_words[-k:] == words[:k]:
                overlap = k
                break
        new_words = words[overlap:]
        if new_words:
            out.append((start, " ".join(new_words)))
        seen_text = text

full_text = ""
last_ts = -999
timestamped = []
for start, chunk in out:
    full_text += chunk + " "
    if start - last_ts >= 15:
        timestamped.append((start, chunk))
        last_ts = start
    else:
        if timestamped:
            timestamped[-1] = (timestamped[-1][0], timestamped[-1][1] + " " + chunk)

with open("narration_full.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

with open("narration_timestamped.txt", "w", encoding="utf-8") as f:
    for start, chunk in timestamped:
        mm = start // 60
        ss = start % 60
        f.write(f"[{mm:02d}:{ss:02d}] {chunk}\n")

words_total = len(full_text.split())
print("TOTAL WORDS (raw dedup):", words_total)
print("DURATION seconds approx:", entries[-1][0] if entries else 0)
