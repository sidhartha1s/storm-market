import re

with open("vid.en.srt", "r", encoding="utf-8") as f:
    content = f.read()

blocks = content.strip().split("\n\n")
entries = []
for b in blocks:
    lines = b.split("\n")
    if len(lines) < 3:
        continue
    idx = lines[0]
    timing = lines[1]
    text = " ".join(lines[2:]).strip()
    m = re.match(r"(\d+):(\d+):(\d+),(\d+) --> ", timing)
    if not m:
        continue
    h, mi, s, ms = map(int, m.groups())
    start = h * 3600 + mi * 60 + s + ms / 1000
    entries.append((start, text))

# Dedup rolling captions: keep only the LAST occurrence of each unique text block
# (rolling captions repeat growing text; take the final full line before it changes)
# Simpler: take entries whose text is not a prefix of the next identical growing caption.
# Build a clean transcript by taking unique consecutive full lines, then dedup words.

# Approach: collect all text blocks, join in order, then split into words with timestamps
# by only keeping words that are NEW compared to previous entry (word-level diff).
prev_words = []
transcript = []  # (timestamp, word)
for start, text in entries:
    words = text.split()
    # find how many words overlap with prev (prev_words is suffix-ish rolling)
    # find longest suffix of prev_words that is prefix of words
    max_overlap = min(len(prev_words), len(words))
    overlap = 0
    for k in range(max_overlap, 0, -1):
        if prev_words[-k:] == words[:k]:
            overlap = k
            break
    new_words = words[overlap:]
    for w in new_words:
        transcript.append((start, w))
    prev_words = words

full_text = " ".join(w for _, w in transcript)
word_count = len(transcript)
duration_sec = transcript[-1][0] if transcript else 0

with open("transcript_clean.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("word_count:", word_count)
print("last_ts:", duration_sec)
print("--- first 400 words ---")
print(" ".join(w for _, w in transcript[:400]))
