"""Every static check I can make against the episode, in one pass.

Each check prints PASS/FAIL and the offending items. No check depends on a render.
"""
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path
from comp_consts import fold

ep = Path(sys.argv[1])
h = (ep / "index.html").read_text(encoding="utf-8", errors="replace")
fails = []


def report(name, bad, detail=lambda x: str(x)):
    if bad:
        fails.append(name)
        print(f"FAIL {name}: {len(bad)}")
        for b in bad[:40]:  # a truncated report hid 16 of 24 family findings once — print them all
            print("      ", detail(b))
    else:
        print(f"PASS {name}")


# ---- windows -------------------------------------------------------------
wins = []
for m in re.finditer(r'<(section|video|div)\b([^>]*)>', h):
    a = m.group(2)
    st, du, tr = (re.search(r'data-start="([\d.]+)"', a),
                  re.search(r'data-duration="([\d.]+)"', a),
                  re.search(r'data-track-index="(\d+)"', a))
    if not (st and du and tr):
        continue
    cid = re.search(r'data-composition-id="([^"]+)"', a)
    src = re.search(r'src="([^"]+)"', a)
    cls = re.search(r'class="([^"]*)"', a)
    is_black = bool(cls and "blackout" in cls.group(1))
    if not src and not cid and not is_black:
        inner = h[m.end():m.end() + 900]
        s2 = re.search(r'src="([^"]+)"', inner)
        src = s2
    wins.append(dict(at=float(st.group(1)), dur=float(du.group(1)), tr=int(tr.group(1)),
                     name="[blackout]" if is_black else
                          (cid.group(1) if cid else (src.group(1) if src else "?"))))

pic = sorted([w for w in wins if w["tr"] in (1, 2)], key=lambda w: w["at"])

# 1. picture coverage
total = float(re.search(r'data-duration="([\d.]+)"', h).group(1))   # not rounded: 1050.9 rounded to 1051 invented a 0.1 s hole past the end
cur, holes = 0.0, []
for w in sorted(pic, key=lambda w: w["at"]):
    if w["at"] > cur + 0.05:
        holes.append((round(cur, 2), round(w["at"], 2)))
    cur = max(cur, w["at"] + w["dur"])
if cur < total - 0.05:
    holes.append((round(cur, 2), total))
report("picture coverage (no black)", holes, lambda x: f"{x[0]}s -> {x[1]}s")

# 2. same-track overlap
ov = []
for tr in {w["tr"] for w in wins}:
    t = sorted([w for w in wins if w["tr"] == tr], key=lambda w: w["at"])
    for a, b in zip(t, t[1:]):
        if a["at"] + a["dur"] - b["at"] > 0.005:
            ov.append((tr, a["name"], b["name"], round(a["at"] + a["dur"] - b["at"], 3)))
report("same-track overlap", ov, lambda x: f"track {x[0]} {x[1]} over {x[2]} by {x[3]}s")

# 3. adjacent duplicate cuts on track 1 (blackouts are structure, not footage)
t1 = [w for w in pic if w["tr"] == 1 and w["name"] != "[blackout]"]
dup = [(a["at"], a["name"]) for a, b in zip(t1, t1[1:]) if a["name"] == b["name"]]
report("adjacent duplicate cuts", dup, lambda x: f"{x[0]}s {Path(x[1]).name}")

# 4. reuse ceiling (3 uses)
uses = Counter(w["name"] for w in t1)
report("asset reuse <= 3", [(n, c) for n, c in uses.items() if c > 3],
       lambda x: f"{Path(x[0]).name} x{x[1]}")

# 5. missing media
miss = [w["name"] for w in t1 if not (ep / w["name"]).exists()]
report("media files exist", sorted(set(miss)))

# 5b. duplicate element ids — hyperframes keys frame placement by id; a duplicate
# renders one window BLACK while every attribute-level check passes (ep5 v1, 8s hole)
ids = Counter(re.findall(r' id="([^"]+)"', h))
report("element ids unique", sorted(n for n, c in ids.items() if c > 1))

def _gate_lines(proc, name):
    """FAIL lines of a sub-gate; a crash (any exit other than 0/1, or exit 1 with no FAIL line) is a failure, never a pass."""
    fails = [l for l in proc.stdout.splitlines() if l.startswith("FAIL")]
    if proc.returncode not in (0, 1) or (proc.returncode == 1 and not fails):
        last = ((proc.stderr or "").strip().splitlines() or ["no stderr"])[-1]
        fails.append(f"FAIL {name} crashed (exit {proc.returncode}): {last}")
    return fails


# 5c2. host/comp class collision (17 Sep 26): hyperframes mounts comps inside index.html, so a shared
# class name lets the page stylesheet restyle the comp. Deterministic; scripts/css_collision.py.
_cc = subprocess.run([sys.executable, str(Path(__file__).resolve().parent / "css_collision.py"), str(ep)],
                     capture_output=True, text=True)
report("comp classes disjoint from index.html", _gate_lines(_cc, "css_collision.py"))

# 5c3. runtime text-write bug classes (17 Sep 26): textContent on a parent deletes its children; text set in
# onStart/onComplete is invisible to the seek-based gates. Deterministic; scripts/comp_lint.py.
_cl = subprocess.run([sys.executable, str(Path(__file__).resolve().parent / "comp_lint.py"), str(ep)],
                     capture_output=True, text=True)
report("comp text writes safe (leaf targets, no callback text)", _gate_lines(_cl, "comp_lint.py"))

# 5d. CTA present + placed (owner order 2026-08-30, DESIGN.md "CTA contract"): the ebook CTA is a
# must-keep element of every episode. Deterministic part only — file/duration/window/labels from
# config.yaml channel.cta; the hinge (tease -> CTA -> payoff) stays editorial.
import yaml  # noqa: E402
_cfg = yaml.safe_load((Path(__file__).resolve().parent.parent / "config.yaml").read_text(encoding="utf-8"))
cta = (_cfg.get("channel") or {}).get("cta")
if not cta:
    sys.exit("config.yaml has no channel.cta block — the CTA contract needs it (DESIGN.md)")
cta_name = Path(cta["file"]).name
cta_bad = []
_slug = ep.resolve().name
_cta_applies = bool(re.match(r"(ep\d*-|ms-)", _slug)) and _slug not in (cta.get("exempt") or [])
_cta_window = (cta.get("window_by_slug") or {}).get(_slug) or (cta["window_ms"] if _slug.startswith("ms-") else cta["window"])   # news lane ~90 % (owner 17 Sep 26); per-episode owner placements in window_by_slug
cm = re.search(r'<video\b[^>]*src="([^"]*' + re.escape(cta_name) + r')"[^>]*>', h)
if not _cta_applies:
    # episodes shipped before the contract (config channel.cta.exempt) and demo-* dirs are not re-wired
    print(f"SKIP CTA present + placed — {_slug} is exempt (shipped pre-contract) or not an epN / ms- episode")
elif not cm:
    cta_bad.append(f"no <video> whose src ends in {cta_name} (config channel.cta.file)")
else:
    a = cm.group(0)
    st = re.search(r'data-start="([\d.]+)"', a)
    du = re.search(r'data-duration="([\d.]+)"', a)
    if not (st and du):
        cta_bad.append("CTA element lacks data-start / data-duration")
    else:
        s, d = float(st.group(1)), float(du.group(1))
        if abs(d - float(cta["duration"])) > 0.05:
            cta_bad.append(f"data-duration {d} != config {cta['duration']}")
        lo, hi = _cta_window
        if not (lo <= s / total <= hi):
            cta_bad.append(f"starts at {s}s = {s / total:.0%} of {total}s — outside {lo:.0%}-{hi:.0%}")
        for n in re.finditer(r'<audio\b[^>]*id="(nx-(?!ins)[^"]*)"[^>]*>', h):
            ns, nd = (re.search(r'data-start="([\d.]+)"', n.group(0)),
                      re.search(r'data-duration="([\d.]+)"', n.group(0)))
            if ns and nd and float(ns.group(1)) < s + d and float(ns.group(1)) + float(nd.group(1)) > s:
                cta_bad.append(f"narration {n.group(1)} overlaps the CTA (must be silent under it)")
        for o in re.finditer(r'<(?:audio|video)\b[^>]*id="(?:nx-)?ins[^"]*"[^>]*>', h):
            os_ = re.search(r'data-start="([\d.]+)"', o.group(0))
            muted = o.group(0).startswith("<video") and not re.search(r'data-volume="1(?:\.0+)?"', o.group(0))
            if cta_name not in o.group(0) and not muted and os_ and -60 < float(os_.group(1)) - s < d + 60:
                print(f"WARN  another insert within 60s of the CTA: {o.group(0)[:80]}")
if cm and _cta_applies:
    a = cm.group(0)
    if not re.search(r'data-volume="1(?:\.0+)?"', a):
        cta_bad.append('CTA needs data-volume="1" (it carries its own VO)')
    if 'data-srt-label="' not in a:
        cta_bad.append("CTA needs data-srt-label (its SRT cue)")
    staged = ep / cm.group(1)
    asset = Path(__file__).resolve().parent.parent / cta["file"]
    if not staged.exists():
        cta_bad.append(f"staged file missing: {staged}")
    elif hashlib.md5(staged.read_bytes()).hexdigest() != hashlib.md5(asset.read_bytes()).hexdigest():
        cta_bad.append(f"staged {cm.group(1)} differs from {cta['file']} (md5)")
if _cta_applies:
    report("CTA present + placed (config channel.cta)", cta_bad)

# 5e. every <video> declares its audio (El Reno v3 post-mortem, 20 Sep 26): hyperframes plays a video's
# track unless the element is `muted`, and audio_levels.py used to skip videos with no data-volume as
# "muted by convention" — so stock footage mounted with neither was audible in the mix and no gate saw it.
_undeclared = [v[:100] for v in re.findall(r"<video\b[^>]*>", h)
               if not re.search(r"\smuted(?=[\s>/=])", v) and not re.search(r'\sdata-volume="', v)]
report("video audio declared (`muted` or data-volume on every <video>)", _undeclared)

# 5c. visual-identity repeats — the viewer sees SOURCES, not filenames. Cuts a/b/c of one
# homogeneous source read as the same clip (ep5 v1: burnaer02 family 16x, fire02 4x in
# the first five minutes). Flag any source family appearing twice within 60s, or >6/episode.
fam_uses = {}
for w in t1:
    fam = re.sub(r'-[a-f]\.mp4$', '', Path(w["name"]).name).replace(".mp4", "")
    # victim portraits deliberately RETURN within their own vignette (namecard -> face ->
    # quote); that is narrative continuation, not a b-roll repeat — the owner's complaint
    if fam.startswith("portrait-"):
        continue
    fam_uses.setdefault(fam, []).append((w["at"], w["at"] + w["dur"]))
fam_bad = []
for fam, fwins in fam_uses.items():
    fwins.sort()
    # a cut that CONTINUES the same source (next window starts as the last ends) is one
    # sequence, not a repeat — the sin is interruption-and-return, not a split shot
    tight = [(a[0], b[0]) for a, b in zip(fwins, fwins[1:])
             if b[0] - a[0] < 60 and b[0] - a[1] > 0.5
             # the hook montage's cold-open -> payoff return (owner-approved v4 shape:
             # the signature shot opens at 0s and lands again on the thesis line before
             # the title) is structure, not a footage-shortage repeat
             and not (a[0] < 35 and b[0] < 35)]
    ats = [w[0] for w in fwins]
    if tight:
        fam_bad.append((fam, f"{len(ats)}x, {len(tight)} pair(s) <60s apart at {int(tight[0][0])}s"))
    elif len(ats) > 6:
        fam_bad.append((fam, f"{len(ats)}x across the episode"))
report("source-family repeats (viewer identity)", fam_bad, lambda x: f"{x[0]}: {x[1]}")

# 6. authored but unmounted compositions
authored = {p.stem for p in (ep / "compositions").glob("*.html")}
mounted = {w["name"] for w in wins if w["name"] in authored}   # overlay comps ride tracks 3-4
report("no unmounted compositions", sorted(authored - mounted))
report("no missing compositions", sorted(mounted - authored))

# 7. graphic window vs its own timeline length
overrun = []
for gid in sorted(mounted):
    src = fold((ep / "compositions" / f"{gid}.html").read_text(encoding="utf-8", errors="replace"))
    pos_matches = list(re.finditer(r'tl\.\w+\([^;]*?,\s*([\d.]+)\s*\);', src))
    # coverage: a position that survives fold() as anything but a bare number (a loop
    # variable, an unfolded identifier — `CUES.seven + i * 0.12`, g-scale-hook.html) never
    # reaches pos_matches. Unparseable is not the same claim as defective (review 24 Sep 26:
    # loop-driven positions can never be literals and hit 3/3 real episodes as a false FAIL) —
    # print the coverage honestly instead so a real hole is never silently capped, but only a
    # confirmed overrun among the tweens actually resolved below fails the sweep.
    calls_total = len(re.findall(r'tl\.(?:to|from|fromTo|set|add)\s*\(', src))
    if calls_total:
        unresolved = calls_total - len(pos_matches)
        note = f"; {unresolved} loop/expression positions not checked" if unresolved else ""
        print(f"      check 7: resolved {len(pos_matches)}/{calls_total} tween positions in {gid}{note}")
    ends = [float(m.group(1)) + max([float(d) for d in re.findall(
        r'duration:\s*([\d.]+)', m.group(0))] or [0])
        for m in pos_matches]
    if not ends:
        continue
    tl_end = max(ends)
    # The last DISCRETE beat, not the end of the timeline. Clipping the tail of a
    # continuous element loses nothing a viewer can name; cutting a reveal does. The two
    # are told apart by HOW they are eased, not by how long they run: a continuous element
    # is a long linear drift (ease "none" — the grain drift, the map push, g-metmap's 14s
    # zone rotation), while a beat lands with an entrance ease. A duration-fraction rule
    # got this wrong, which is how this check first cried wolf on g-metmap.
    beats = []
    for m in pos_matches:
        body = m.group(0)
        d = max([float(x) for x in re.findall(r'duration:\s*([\d.]+)', body)] or [0])
        if d > 4.0 and re.search(r'ease:\s*"none"', body):
            continue                      # continuous, not a beat
        beats.append(float(m.group(1)) + d)
    last_beat = max(beats) if beats else 0.0
    for w in wins:
        if w["name"] != gid:
            continue
        if w["dur"] - tl_end > 4.0:
            overrun.append(("holds", gid, round(w["dur"], 1), round(tl_end, 1)))
        # the direction this check used to ignore entirely: a mount SHORTER than the
        # composition cuts off its own authored reveals
        elif last_beat - w["dur"] > 0.30:
            overrun.append(("cuts a beat", gid, round(w["dur"], 1), round(last_beat, 1)))
report("graphic window fits its timeline", overrun,
       lambda x: f"{x[0]:9} {x[1]} window {x[2]}s vs timeline {x[3]}s")

# NOTE: there is deliberately no "cue alignment" check here. One used to sit at this
# spot; it initialised an empty findings list, never appended to it, and printed PASS on
# every input. A gate that cannot fail is worse than no gate, because it is counted as
# coverage. Reveal-vs-spoken-word alignment is still verified by reading words.json when
# a composition is authored — it is not, and must not pretend to be, automated here.

# 8. luma gate — owner 2026-08-13 (ep5 v4 shipped one near-black taillight source TEN times):
# any mounted video whose mid-file frame reads YAVG < 25 is unwatchably dark. Probes are cached
# by (path, mtime) in media/.luma-cache.json so repeat sweeps stay fast.
luma_cache_p = ep / "media" / ".luma-cache.json"
try:
    # drop legacy -1.0 "failed probe" entries — failures are reported, never cached
    luma_cache = {k: v for k, v in json.loads(luma_cache_p.read_text()).items() if v >= 0}
except Exception:
    luma_cache = {}

probe_failed = []  # a failed probe is a FAILED gate, never a silent pass

def cached_yavg(key, ffmpeg_args):
    """Run an ffmpeg probe whose output contains a signalstats YAVG line; cache by key.
    Failures are NOT cached (retried next run) and land in probe_failed — fail loud."""
    if key not in luma_cache:
        try:
            r = subprocess.run(["ffmpeg"] + ffmpeg_args, capture_output=True, text=True,
                               timeout=60)
            mm = re.search(r"YAVG=([\d.]+)", r.stdout + r.stderr)
            if not mm:
                probe_failed.append((key, "no YAVG in ffmpeg output"))
                return None
            luma_cache[key] = float(mm.group(1))
        except Exception as e:
            probe_failed.append((key, repr(e)[:80]))
            return None
    return luma_cache[key]

# videos play from FILE START: a window of duration d shows file[0..d], so the
# representative frame is at d/2 of the SHORTEST mounted window — not the file middle.
still_ok_srcs = set()
for m2 in re.finditer(r'<video[^>]*data-still-ok="[^"]*"[^>]*>', h):
    s2 = re.search(r'src="([^"]+)"', m2.group(0))
    if s2:
        still_ok_srcs.add(s2.group(1))
shortest = {}
for w in t1:
    if w["name"].endswith(".mp4") and w["name"] not in still_ok_srcs:
        shortest[w["name"]] = min(shortest.get(w["name"], 1e9), w["dur"])
dark = []
for name, sdur in sorted(shortest.items()):
    p = ep / name
    if not p.exists():
        continue
    y = cached_yavg(f'{name}|{int(p.stat().st_mtime)}|{round(sdur / 2, 1)}',
                    ["-ss", str(round(sdur / 2, 2)), "-i", str(p), "-frames:v", "1",
                     "-vf", "signalstats,metadata=print:file=-", "-f", "null", "-"])
    if y is not None and y < 25:
        dark.append((name, y))
report("luma gate (no near-black sources, YAVG>=25)", dark,
       lambda x: f"{Path(x[0]).name} YAVG={x[1]:.1f}")

# 8b. motion gate — ep5 v5 shipped 5 dozerreel cuts that were FROZEN STILLS at the source
# (cut from a 911-audio reel's photo-slideshow sections). A mounted video whose first and
# last shown frames differ by YAVG < 0.6 is a still pretending to be a clip. Same cache file.
def _frame(p, t, out):
    # -ss BEFORE -i: keyframe seek, not a linear decode of the whole source
    Path(out).unlink(missing_ok=True)  # stale frame from the previous clip must never be diffed
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", str(t), "-i", str(p),
                    "-frames:v", "1", out], capture_output=True, timeout=60)
    return Path(out).exists()

# pid-scoped: two sweep_episode.py runs against two different episodes share the OS temp
# dir. A bare filename here meant one process's ffmpeg frame extract could overwrite the
# other's file mid-diff — no exception, just a silently wrong motion-gate result on
# whichever process read the swapped frame. PID makes collision impossible instead of just
# unlikely (23 Sep 26 review: root-caused while chasing a reported concurrent-run false pass).
_tmpa = str(Path(tempfile.gettempdir()) / f"_sweep_ma_{__import__('os').getpid()}.png")
_tmpb = str(Path(tempfile.gettempdir()) / f"_sweep_mb_{__import__('os').getpid()}.png")
frozen = []
for name, sdur in sorted(shortest.items()):
    p = ep / name
    if not p.exists() or sdur < 2.0:
        continue
    key = f'MOTION|{name}|{int(p.stat().st_mtime)}|{round(sdur, 1)}'
    if key not in luma_cache:
        if not (_frame(p, 0.4, _tmpa) and _frame(p, sdur - 0.4, _tmpb)):
            probe_failed.append((key, "frame extraction failed"))
            continue
    y = cached_yavg(key, ["-hide_banner", "-i", _tmpa, "-i", _tmpb, "-lavfi",
                          "blend=all_mode=difference,signalstats,metadata=print:file=-",
                          "-frames:v", "1", "-f", "null", "-"])
    if y is not None and y < 0.6:
        frozen.append((name, y))
try:
    luma_cache_p.write_text(json.dumps(luma_cache))
except Exception:
    pass
report("motion gate (no frozen-still sources, frame diff >= 0.6)", frozen,
       lambda x: f"{Path(x[0]).name} diff={x[1]:.3f}")
report("media probes succeeded", probe_failed, lambda x: f"{x[0]}: {x[1]}")

# 9. long stills — owner 2026-08-12: stills are 3-6s with motion, "not a PowerPoint"
long_still = [(w["at"], w["name"], w["dur"]) for w in t1
              if w["dur"] > 6.0 and not w["name"].endswith(".mp4")]
report("no still over 6s", long_still, lambda x: f"{x[0]}s {Path(x[1]).name} {x[2]}s")

# 10. narration freshness (CLAUDE.md: "words.json must be younger than its wav") — ep3-tristate
# shipped 3 segments where a stale words.json (made from a longer take) ran past the real wav,
# and the data-duration copied straight from it also outran the audio: a3-s7 48.6s vs a
# 41.72s wav. mtime alone is not enough (a words.json made from a re-tempo'd wav that is STILL
# too long stays newer than the wav and would pass an mtime-only gate) — the duration compare
# below is the part that actually catches it.
def _wav_duration(p):
    try:
        r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                            "-of", "csv=p=0", str(p)], capture_output=True, text=True, timeout=30)
        return float((r.stdout or "").strip() or "nan")
    except Exception:
        return None

stale = []
for m in re.finditer(r'<audio\b[^>]*id="(nx-(?!ins)[^"]*)"[^>]*>', h):
    a, eid = m.group(0), m.group(1)
    src = re.search(r'src="([^"]+)"', a)
    du = re.search(r'data-duration="([\d.]+)"', a)
    if not (src and du):
        continue
    wav = ep / src.group(1)
    if not wav.exists():
        continue  # "media files exist" already flags this
    words_p = wav.with_name(wav.stem + ".words.json")
    wav_dur = _wav_duration(wav)
    if wav_dur is None or wav_dur != wav_dur:  # nan = ffprobe failed
        stale.append((eid, "wav duration unreadable (ffprobe failed)"))
        continue
    html_dur = float(du.group(1))
    if abs(html_dur - wav_dur) > 0.1:
        stale.append((eid, f"data-duration {html_dur}s vs wav {wav_dur:.2f}s (diff {html_dur - wav_dur:+.2f}s)"))
    if words_p.exists():
        if words_p.stat().st_mtime < wav.stat().st_mtime - 0.001:
            stale.append((eid, f"{words_p.name} is older than its wav"))
        try:
            words = json.loads(words_p.read_text(encoding="utf-8"))
            last_end = max((float(wd.get("end", 0.0)) for wd in words), default=0.0)
            if last_end > wav_dur + 0.05:
                stale.append((eid, f"last word ends at {last_end:.2f}s, wav is only {wav_dur:.2f}s ({words_p.name} is stale)"))
        except Exception as e:
            stale.append((eid, f"{words_p.name} unreadable: {e!r}"))
    else:
        stale.append((eid, f"{words_p.name} missing"))
report("narration freshness (words.json + data-duration match the real wav)", stale,
       lambda x: f"{x[0]}: {x[1]}")

print()
print("SWEEP", "FAIL" if fails else "PASS", "-", len(fails), "failing checks")
sys.exit(1 if fails else 0)
