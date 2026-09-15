"""Shorts competitor scan (radar seat, weekly). Search YouTube's <4 min filter on niche queries, keep clips <=75 s,
pull every candidate channel's full /shorts tab and count HIT RATE (share >=100k / 300k / 1M), never median.
Usage: python3 scripts/shorts_scan.py [out_dir]   -> out_dir/channels.json + a ranked table on stdout. ~25 min."""
import json, subprocess, collections, pathlib, sys
from concurrent.futures import ThreadPoolExecutor
QUERIES = ["tornado warning", "hurricane 2026", "flash flood emergency", "volcano eruption today", "earthquake today",
           "wildfire evacuation", "el nino 2026", "blizzard warning", "NOAA warning", "deadliest tornado", "weather alert",
           "storm surge", "tsunami warning", "krakatau", "heat dome", "extreme weather", "natural disaster news",
           "severe weather outbreak", "dam failure", "sinkhole"]
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "scratch/shorts-scan"); OUT.mkdir(parents=True, exist_ok=True)
def ytdlp(url, *extra, timeout=240):
    cmd = ["yt-dlp", "--flat-playlist", "--no-warnings", "--ignore-errors", *extra, url]
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, encoding="utf-8", errors="replace").stdout
    except subprocess.TimeoutExpired:
        return ""
def search(q):
    out = ytdlp(f"https://www.youtube.com/results?search_query={q.replace(' ', '+')}&sp=EgIYAQ%253D%253D", "-j", "--playlist-end", "80")
    rows = []
    for line in out.splitlines():
        try: r = json.loads(line)
        except Exception: continue
        if 0 < (r.get("duration") or 0) <= 75 and r.get("channel_id"):
            rows.append(dict(q=q, id=r["id"], ch=r.get("channel") or r.get("uploader"), cid=r["channel_id"], views=r.get("view_count") or 0, title=r.get("title")))
    return rows
def channel(item):
    cid, hs = item
    j = json.loads(ytdlp(f"https://www.youtube.com/channel/{cid}/shorts", "-J", "--playlist-end", "200") or "{}") or {}
    views = sorted([(e.get("view_count") or 0) for e in (j.get("entries") or []) if e], reverse=True)
    n = len(views)
    return dict(cid=cid, channel=j.get("channel") or hs[0]["ch"], subs=j.get("channel_follower_count"), n_shorts=n, truncated=n >= 200,
                ge100k=sum(v >= 100_000 for v in views), ge300k=sum(v >= 300_000 for v in views), ge1m=sum(v >= 1_000_000 for v in views),
                median=views[n // 2] if n else 0, top=views[:5], sample_titles=[h["title"] for h in hs][:3], queries=sorted({h["q"] for h in hs}))
with ThreadPoolExecutor(6) as ex:
    hits = [h for rows in ex.map(search, QUERIES) for h in rows]
by = collections.defaultdict(list)
for h in hits: by[h["cid"]].append(h)
cands = [(cid, hs) for cid, hs in by.items() if max(h["views"] for h in hs) >= 100_000]
print(f"{len(hits)} hits, {len(by)} channels, {len(cands)} with a >=100k hit", flush=True)
with ThreadPoolExecutor(6) as ex:
    rows = [r for r in ex.map(channel, cands) if r["n_shorts"] >= 8]
(OUT / "channels.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
rows.sort(key=lambda r: (r["ge300k"] / r["n_shorts"], r["ge300k"]), reverse=True)
for r in rows:
    if (r["subs"] or 0) <= 600_000 and r["ge300k"] >= 2:
        print(f"{r['channel'][:26]:26} subs={r['subs']!s:>7} n={r['n_shorts']:>3} >=300k={r['ge300k']:>3} >=1M={r['ge1m']:>2} med={r['median']:>8} | {r['sample_titles'][0][:50]}")
