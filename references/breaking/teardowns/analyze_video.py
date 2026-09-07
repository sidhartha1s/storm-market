import json, re, sys, glob, os, statistics

def main(dir_path, vid_id):
    out = {}
    # --- info.json ---
    info_files = glob.glob(os.path.join(dir_path, f"{vid_id}*.info.json"))
    info = {}
    if info_files:
        with open(info_files[0], "r", encoding="utf-8") as f:
            info = json.load(f)
    out["title"] = info.get("title")
    out["channel"] = info.get("channel") or info.get("uploader")
    out["channel_id"] = info.get("channel_id")
    out["channel_url"] = info.get("channel_url") or info.get("uploader_url")
    out["channel_follower_count"] = info.get("channel_follower_count")
    out["duration"] = info.get("duration")
    out["upload_date"] = info.get("upload_date")
    out["view_count"] = info.get("view_count")
    out["like_count"] = info.get("like_count")
    out["chapters"] = info.get("chapters")
    desc = info.get("description") or ""
    out["description_600"] = desc[:600]

    comments = info.get("comments") or []
    comments_sorted = sorted(comments, key=lambda c: c.get("like_count") or 0, reverse=True)
    top30 = [{"text": (c.get("text") or "").strip().replace("\n", " ")[:500],
              "likes": c.get("like_count") or 0} for c in comments_sorted[:30]]
    out["top_comments"] = top30
    out["comment_count_seen"] = len(comments)

    # --- duration.txt (ffprobe, more reliable) ---
    dur_file = os.path.join(dir_path, "duration.txt")
    dur = None
    if os.path.exists(dur_file):
        try:
            dur = float(open(dur_file).read().strip())
        except Exception:
            pass
    if dur is None:
        dur = info.get("duration")
    out["duration_sec"] = dur

    # --- srt ---
    srt_files = glob.glob(os.path.join(dir_path, f"{vid_id}*.srt"))
    hook_text = ""
    total_words_raw = 0
    if srt_files:
        with open(srt_files[0], "r", encoding="utf-8", errors="ignore") as f:
            srt = f.read()
        blocks = re.split(r"\n\n+", srt.strip())
        entries = []
        for b in blocks:
            lines = b.split("\n")
            if len(lines) < 3:
                continue
            m = re.match(r"(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)", lines[1]) if len(lines) > 1 else None
            if not m:
                continue
            def to_sec(t):
                h, mi, rest = t.split(":")
                s, ms = rest.split(",")
                return int(h)*3600 + int(mi)*60 + int(s) + int(ms)/1000
            start = to_sec(m.group(1))
            text = " ".join(lines[2:])
            text = re.sub(r"<[^>]+>", "", text)
            entries.append((start, text))
            total_words_raw += len(text.split())
        entries.sort(key=lambda x: x[0])
        hook_lines = [t for (s, t) in entries if s <= 45]
        # dedupe consecutive identical lines (common in rolling captions)
        dedup = []
        for l in hook_lines:
            if not dedup or dedup[-1] != l:
                dedup.append(l)
        hook_text = " ".join(dedup)
    out["total_words_raw"] = total_words_raw
    out["total_words_est"] = round(total_words_raw / 2)
    out["wpm_est"] = round((total_words_raw/2) / (dur/60), 1) if dur else None
    out["hook_45s"] = hook_text.strip()

    # --- cuts ---
    cuts_file = os.path.join(dir_path, "cuts_raw.log")
    cut_times = []
    if os.path.exists(cuts_file):
        with open(cuts_file, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                m = re.search(r"pts_time:(\d+\.?\d*)", line)
                if m:
                    cut_times.append(float(m.group(1)))
    cut_times = sorted(set(cut_times))
    out["cuts_total"] = len(cut_times)
    bounds = [0.0] + cut_times + ([dur] if dur else [])
    shot_lens = [bounds[i+1]-bounds[i] for i in range(len(bounds)-1) if bounds[i+1] > bounds[i]]
    out["median_shot_len"] = round(statistics.median(shot_lens), 2) if shot_lens else None
    first60_cuts = [0.0] + [c for c in cut_times if c <= 60] + [60.0]
    first60_lens = [first60_cuts[i+1]-first60_cuts[i] for i in range(len(first60_cuts)-1) if first60_cuts[i+1] > first60_cuts[i]]
    out["hook_median_shot_len"] = round(statistics.median(first60_lens), 2) if first60_lens else None
    out["hook_cut_count"] = len([c for c in cut_times if c <= 60])

    # write detail files
    with open(os.path.join(dir_path, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    with open(os.path.join(dir_path, "comments_top.md"), "w", encoding="utf-8") as f:
        for c in top30[:10]:
            f.write(f"- ({c['likes']} likes) {c['text']}\n")

    with open(os.path.join(dir_path, "hook_transcript.txt"), "w", encoding="utf-8") as f:
        f.write(hook_text.strip())

    # print compact summary only
    compact = {k: out[k] for k in ["title","channel","channel_id","channel_url","channel_follower_count",
                                     "duration_sec","upload_date","view_count",
                                     "like_count","cuts_total","median_shot_len","hook_median_shot_len",
                                     "hook_cut_count","total_words_est","wpm_est","comment_count_seen"]}
    print(json.dumps(compact, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
