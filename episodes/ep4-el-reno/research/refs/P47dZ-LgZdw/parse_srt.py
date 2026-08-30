import re

with open("vid.en.srt", encoding="utf-8") as f:
    content = f.read()

blocks = content.strip().split("\n\n")
lines = []
last_text = None
for b in blocks:
    parts = b.split("\n")
    if len(parts) < 3:
        continue
    time_line = parts[1]
    text = " ".join(parts[2:]).strip()
    if not text:
        continue
    start = time_line.split(" --> ")[0]
    # dedupe rolling captions: keep only new text vs last cumulative block
    lines.append((start, text))

# reconstruct unique word stream: since rolling captions repeat previous line + add new,
# take the LAST line of each timestamp group as it's most complete, then dedupe consecutive near-duplicates
dedup = []
prev = ""
for start, text in lines:
    if text == prev:
        continue
    dedup.append((start, text))
    prev = text

with open("srt_dedup.txt", "w", encoding="utf-8") as f:
    for start, text in dedup:
        f.write(f"[{start}] {text}\n")

# word count estimate: total words in raw srt / 2 (rolling double-count), per instructions
raw_words = sum(len(text.split()) for _, text in lines)
print("raw total word-tokens (all caption lines, includes repeats):", raw_words)
print("dedup lines:", len(dedup))
print("first 5 dedup lines:")
for start, text in dedup[:5]:
    print(start, text)
print("last line time:", dedup[-1][0] if dedup else None)
