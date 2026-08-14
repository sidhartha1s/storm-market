import re, sys

def ts_to_sec(ts):
    h, m, s = ts.split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)

def sec_to_hms(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = int(sec % 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"

def clean_line(line):
    # remove inline timing tags like <00:00:12.639><c>
    line = re.sub(r"<[^>]+>", "", line)
    return line.strip()

def main(vtt_path, out_path):
    with open(vtt_path, encoding="utf-8") as f:
        content = f.read()

    blocks = re.split(r"\n\n+", content)
    entries = []  # (start_sec, text)
    for block in blocks:
        lines = block.strip().splitlines()
        if not lines:
            continue
        # find timing line
        timing_idx = None
        for i, l in enumerate(lines):
            if "-->" in l:
                timing_idx = i
                break
        if timing_idx is None:
            continue
        timing = lines[timing_idx]
        m = re.match(r"(\d+:\d+:\d+\.\d+)\s*-->\s*(\d+:\d+:\d+\.\d+)", timing)
        if not m:
            continue
        start = ts_to_sec(m.group(1))
        text_lines = [clean_line(l) for l in lines[timing_idx+1:]]
        text_lines = [l for l in text_lines if l]
        if text_lines:
            entries.append((start, " ".join(text_lines)))

    # Dedupe: rolling captions repeat previous line(s). Keep only new tail text per timestamp.
    # Strategy: track last emitted full text; for each entry, if it's a superset continuation,
    # emit only the new words compared to previous entry's text.
    out_lines = []
    prev_text = ""
    for start, text in entries:
        if text == prev_text:
            continue
        if prev_text and text.startswith(prev_text):
            new_part = text[len(prev_text):].strip()
        else:
            new_part = text
        if new_part:
            out_lines.append((start, new_part))
        prev_text = text

    # Merge consecutive fragments into readable lines grouped by ~8 sec gaps into sentences is optional.
    with open(out_path, "w", encoding="utf-8") as f:
        for start, text in out_lines:
            f.write(f"[{sec_to_hms(start)}] {text}\n")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
