import re, os
p = r'C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ms-krakatoa-1883\episodes\ms-krakatoa-1883\_build\kk_build.py'
s = open(p, encoding='utf-8').read()

s = s.replace('''man = json.load(open(os.path.join(E, "audio", "manifest.json")))''', '''def probe(path):
    return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",path],capture_output=True,text=True).stdout.strip())
FPS = 30
def fa(t): return round(math.ceil(t * FPS - 1e-6) / FPS, 3)   # frame-aligned (round up)
_order = ["h1-s1","i1-s1","i1-s2","c1-s1","c2-s1","c3-s1","c4-s1","c5-s1","c6-s1","c7-s1","c8-s1","c8-s2","z1-s1"]
man = {k: {"duration": round(probe(os.path.join(E,"audio",f"{k}.wav")),3)} for k in _order}''')

s = s.replace('''S = {}; t = 0.0
for k in order:
    if k == "c5-s1":
        t = round(t + 1.0 + CTA_DUR + 1.0 + 0.5, 3)      # dip in 1 s, CTA, dip out 1 s, breath
    S[k] = round(t, 3); t = round(t + man[k]["duration"] + GAP, 3)
CTA_IN = round(S["c4-s1"] + man["c4-s1"]["duration"] + 0.5, 3)   # blackout starts
CTA_AT = round(CTA_IN + 1.0, 3)
CTA_OUT = round(CTA_AT + CTA_DUR, 3)''', '''S = {}; t = 0.0
for k in order:
    if k == "c5-s1":
        t = fa(CTA_OUT + 0.5)                              # dip out 0.5 s, then narration
    S[k] = fa(t); t = round(S[k] + man[k]["duration"] + GAP, 3)
    if k == "c4-s1":
        CTA_IN = fa(S[k] + man[k]["duration"] + 0.5)       # black dips in (1.0 s, track 2)
        CTA_AT = fa(CTA_IN + 0.9)                          # clip audio starts 0.1 s under the black: "Most people" intact
        CTA_OUT = round(CTA_AT + CTA_DUR, 3)''')

s = s.replace('''id="bo-cta-in" data-start="{CTA_IN}" data-duration="1.0" data-track-index="1"''', '''id="bo-cta-in" data-start="{CTA_IN}" data-duration="1.0" data-track-index="2"''')
s = s.replace('''id="bo-cta-out" data-start="{CTA_OUT}" data-duration="{round(S["c5-s1"]-CTA_OUT,3)}" data-track-index="1"''', '''id="bo-cta-out" data-start="{CTA_OUT}" data-duration="{round(S["c5-s1"]-CTA_OUT,3)}" data-track-index="2"''')

s = s.replace('''# ---- overlays: per segment, list of (type, id, big, sub, rel_at, hold). type: pf popfig, ch chip, lab source label, q quote''', '''# ---- word cues: every overlay time comes from audio/<seg>.words.json, never from an estimate ----
def tokens(k):
    w = json.load(open(os.path.join(E,"audio",f"{k}.words.json"))); out = []
    for x in w:
        t = re.sub(r"[^a-z0-9]", "", x["text"].lower())
        if out and (x["text"].startswith(",") or x["text"].startswith("-")) and t and out[-1][0][-1:].isdigit():
            out[-1] = (out[-1][0] + t, out[-1][1]); continue
        if t: out.append((t, float(x["start"])))
    return out
def cue(k, phrase, lead=0.12):
    if isinstance(phrase, (int, float)): return float(phrase)
    want = [re.sub(r"[^a-z0-9]", "", p.lower()) for p in phrase.split()]
    toks = tokens(k)
    for i in range(len(toks) - len(want) + 1):
        if [t for t, _ in toks[i:i+len(want)]] == want: return max(0.0, round(toks[i][1] - lead, 3))
    raise SystemExit(f"cue not found in {k}: '{phrase}'  (tokens: {' '.join(t for t,_ in toks)[:400]})")
# ---- overlays: per segment, list of (type, id, big, sub, CUE, hold). CUE = word phrase in the transcript (or a float = seconds into the segment)''')

a = s.index('OV = {'); b = s.index('}\n', s.index('"z1-s1":[', a)) + 2
OV = open(os.path.join(os.path.dirname(p), 'ov_v2.txt'), encoding='utf-8').read()
s = s[:a] + OV + s[b:]
s = s.replace('''        typ, oid = o[0], o[1]; at = round(S[k] + o[-2], 3); hold = o[-1]''', '''        typ, oid = o[0], o[1]; at = round(S[k] + cue(k, o[-2]), 3); hold = min(o[-1], round(S[k] + man[k]["duration"] + GAP - at, 3))''')
open(p, 'w', encoding='utf-8').write(s)
assert 'cue(k, o[-2])' in s and 'fa(CTA_IN + 0.9)' in s and 'data-track-index="2"></section>' in s
print('builder patched')
