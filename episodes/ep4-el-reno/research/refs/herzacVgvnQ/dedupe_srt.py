import re

path = r"C:\Users\Sidhartha\Automation Projects\storm-market\episodes\ep4-el-reno\research\refs\herzacVgvnQ\vid.en.srt"
with open(path, encoding="utf-8") as f:
    content = f.read()

blocks = content.strip().split("\n\n")
seen_last_line = None
out_lines = []
timestamps = []

for b in blocks:
    lines = b.split("\n")
    if len(lines) < 3:
        continue
    time_line = lines[1]
    text_lines = [l for l in lines[2:] if l.strip() and not l.strip().startswith(">>")]
    text_lines_full = [l for l in lines[2:] if l.strip()]
    # take last text line of block (the newest line, since caption is rolling)
    if not text_lines_full:
        continue
    last = text_lines_full[-1]
    if last != seen_last_line:
        start = time_line.split(" --> ")[0]
        out_lines.append(f"[{start}] {last}")
        seen_last_line = last

with open(r"C:\Users\Sidhartha\Automation Projects\storm-market\episodes\ep4-el-reno\research\refs\herzacVgvnQ\narration.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print(len(out_lines))
