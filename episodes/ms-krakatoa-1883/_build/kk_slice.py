# Scratch: cut a T0..T0+W visual slice of the real index.html into _test_<name>/ for a draft render.
# Media/audio/compositions are junctioned, small runtime files copied. Elements starting before T0 are
# clamped to 0 (no seek) — the slice is a LAYOUT/placement test, not a sync test.
import os, re, sys, subprocess, shutil
E = r"C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ms-krakatoa-1883\episodes\ms-krakatoa-1883"
name, T0, W = sys.argv[1], float(sys.argv[2]), float(sys.argv[3])
D = os.path.join(E, f"_test_{name}"); os.makedirs(D, exist_ok=True)
for sub in ("media", "audio", "compositions", "fonts"):
    dst = os.path.join(D, sub)
    if not os.path.exists(dst): subprocess.run(["cmd", "/c", "mklink", "/J", dst, os.path.join(E, sub)], capture_output=True)
for f in ("gsap.min.js", "grain.js"): shutil.copy(os.path.join(E, f), os.path.join(D, f))
s = open(os.path.join(E, "index.html"), encoding="utf-8").read()
out = []
for line in s.splitlines():
    m = re.search(r'data-start="([0-9.]+)"', line)
    if m and 'id="root"' not in line:
        st = float(m.group(1)); dm = re.search(r'data-duration="([0-9.]+)"', line); du = float(dm.group(1)) if dm else 0
        if st + du <= T0 or st >= T0 + W: continue
        ns = max(0.0, st - T0); nd = round(min(st + du, T0 + W) - max(st, T0), 3)
        line = line.replace(m.group(0), f'data-start="{round(ns,3)}"')
        if dm: line = line.replace(dm.group(0), f'data-duration="{nd}"')
    elif 'id="root"' in line:
        line = re.sub(r'data-duration="[0-9.]+"', f'data-duration="{W}"', line).replace("ms-krakatoa-1883", f"ms-krakatoa-1883-{name}")
    elif re.match(r'\s+(kb|pop|chip|lab)\(', line):
        args = line[line.index("(")+1:]
        parts = args.split(", ")
        t = float(parts[1]);
        if t + 20 < T0 or t > T0 + W: continue
        parts[1] = str(round(max(t - T0, 0), 3)); line = line[:line.index("(")+1] + ", ".join(parts)
    elif re.match(r'\s+bug\(', line):
        parts = line.split(", "); t = float(parts[2]); parts[2] = str(round(max(t - T0, 0), 3)); line = ", ".join(parts)
    elif re.match(r'\s+tl\.(to|fromTo|set)\(', line) and 'window.__timelines' not in line:
        def shift(mm):
            t = float(mm.group(1)); return f", {round(max(t - T0, 0), 3)});"
        times = [float(x) for x in re.findall(r', ([0-9.]+)\);', line)]
        if times and all(t < T0 - 1 or t > T0 + W for t in times): continue
        line = re.sub(r', ([0-9.]+)\);', shift, line)
    elif "const DUR" in line: line = f"  const DUR = {W};"
    out.append(line.replace('window.__timelines["ms-krakatoa-1883"]', f'window.__timelines["ms-krakatoa-1883-{name}"]'))
open(os.path.join(D, "index.html"), "w", encoding="utf-8").write("\n".join(out))
print(D)
