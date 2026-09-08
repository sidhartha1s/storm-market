import re, sys, glob, os

def parse_srt(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        srt = f.read()
    blocks = re.split(r"\n\n+", srt.strip())
    entries = []
    for b in blocks:
        lines = b.split("\n")
        if len(lines) < 3:
            continue
        m = re.match(r"(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)", lines[1])
        if not m:
            continue
        text = " ".join(lines[2:])
        text = re.sub(r"<[^>]+>", "", text).strip()
        entries.append(text)
    return entries

def dedup_stitch(entries):
    """Stitch rolling-caption cues: for each new cue, find the longest suffix of the
    running transcript that matches a prefix of the new cue's words, and append only
    the non-overlapping remainder. Falls back to appending the whole cue if no overlap."""
    words = []
    for text in entries:
        cur = text.split()
        if not cur:
            continue
        if not words:
            words.extend(cur)
            continue
        max_check = min(len(words), len(cur), 40)
        best_k = 0
        for k in range(max_check, 0, -1):
            if words[-k:] == cur[:k]:
                best_k = k
                break
        words.extend(cur[best_k:])
    return words

def naive_halve(entries):
    total = sum(len(t.split()) for t in entries)
    return total / 2

def main(dir_path, vid_id, duration_sec):
    srt_files = glob.glob(os.path.join(dir_path, f"{vid_id}*.srt"))
    if not srt_files:
        print("NO SRT FOUND")
        return
    entries = parse_srt(srt_files[0])
    stitched = dedup_stitch(entries)
    naive = naive_halve(entries)
    dur_min = float(duration_sec) / 60
    print(f"cues={len(entries)} raw_total_words={sum(len(t.split()) for t in entries)}")
    print(f"naive_halved_words={naive:.0f}  naive_wpm={naive/dur_min:.1f}")
    print(f"stitched_unique_words={len(stitched)}  stitched_wpm={len(stitched)/dur_min:.1f}")
    print("--- first 60 stitched words ---")
    print(" ".join(stitched[:60]))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
