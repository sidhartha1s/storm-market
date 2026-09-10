# One-shot builder for ms-krakatoa-1883 index.html. Hand-authored cut list + overlays below; the code only
# computes butt-cut starts, copies the chosen assets, cuts the presenter loops to the window lengths and
# emits the talk toggles from words.json. Never committed (episode/_build is scratch).
import json, os, re, shutil, subprocess, math
E = r"C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ms-krakatoa-1883\episodes\ms-krakatoa-1883"
P = r"C:\Users\Sidhartha\Automation Projects\storm-market\.worktrees\ms-krakatoa-1883\library\mini-storms\krakatau-2026"
man = json.load(open(os.path.join(E, "audio", "manifest.json")))
GAP = 0.45
order = ["h1-s1","i1-s1","i1-s2","c1-s1","c2-s1","c3-s1","c4-s1","c5-s1","c6-s1","c7-s1","c8-s1","c8-s2","z1-s1"]
CTA_DUR = 15.139

# ---- narration schedule ----
S = {}; t = 0.0
for k in order:
    if k == "c5-s1":
        t = round(t + 1.0 + CTA_DUR + 1.0 + 0.5, 3)      # dip in 1 s, CTA, dip out 1 s, breath
    S[k] = round(t, 3); t = round(t + man[k]["duration"] + GAP, 3)
CTA_IN = round(S["c4-s1"] + man["c4-s1"]["duration"] + 0.5, 3)   # blackout starts
CTA_AT = round(CTA_IN + 1.0, 3)
CTA_OUT = round(CTA_AT + CTA_DUR, 3)
Z_END = round(S["z1-s1"] + man["z1-s1"]["duration"], 3)
CLOSE_AT = round(S["z1-s1"] + 19.3, 3)
DUR = float(math.ceil(Z_END + 3.0))
def seg_end(k): return round(S[k] + man[k]["duration"], 3)

# ---- assets (short name -> pool path) ----
A = {
 "viirs":"eruption-2026/nasa-eo-viirs-20260905.jpg","oli":"eruption-2026/nasa-eo-oli-20260905.jpg",
 "s3":"eruption-2026/esa-sentinel3-eruption-20260908.jpg","lava":"eruption-2026/lampungprov-lava-fountain-20260905.jpg",
 "cop0702":"eruption-2026/copernicus-ash-plume-20260702.webp","haze":"eruption-2026/ash-haze-kebumen-central-java-20260907.jpg",
 "litho":"1883/lithograph-eruption-1888.jpg","parker":"1883/parker-coward-plate1-1888.jpg","baro":"1883/royal-society-plate-vii-barograms-1888.png",
 "twilight":"1883/royal-society-twilight-afterglow-1888.jpg","sunset":"1883/sunset-colours-diagram-1888.jpg","locprint":"1883/loc-krakatoa-submerged-print.jpg",
 "aster10":"anak-growth/nasa-aster-2010.jpg","cop19":"anak-growth/copernicus-markuse-20190331.jpg","s2_22":"anak-growth/esa-sentinel2-20220503.jpg",
 "ls20":"anak-growth/usgs-landsat-markuse-20200413.jpg","ls18":"anak-growth/usgs-landsat-post-collapse-20181220.jpg",
 "aft1":"tsunami-2018/aftermath-sunda-strait-1.jpg","aft2":"tsunami-2018/aftermath-sunda-strait-2.jpg","aft3":"tsunami-2018/aftermath-sunda-strait-3.jpg",
 "rescue":"tsunami-2018/lampung-search-rescue.jpg","concert":"tsunami-2018/seventeen-concert-site-aftermath.jpg",
 "chart":"maps/admiralty-chart-sunda-strait-1851.jpg","ctx2000":"maps/satellite-context-map-2000.jpg","outline":"maps/sunda-strait-outline-map.png","reach":"maps/tsunami-reach-map-1883.jpg",
}
BC = lambda n: f"broadcast/{n}.mp4"
for n in ["abcaus_20260906-008","abcaus_20260906-012","abcaus_20260906-014","abcaus_20260906-016","abcaus_20260906-020",
          "aljazeera_20260906-002","aljazeera_20260906-004","aljazeera_20260906-008","aljazeera_20260906-014","aljazeera_20260906-015","aljazeera_20260906-018",
          "ap_20181224-001","bbc_20181227-001","bbc_20181227-003","bbc_20181227-005","bbc_20181227-010","bbc_20181227-012","bbc_20181227-015",
          "cna_20260906-006","cna_20260906-012","cna_20260906-019","cna_20260906-031",
          "reuters_20260906-001","reuters_20260906-002","reuters_20260906-006","reuters_20260906-007","reuters_20260906-009"]:
    A[n.split("_")[0][:3] + n.split("-")[-1]] = BC(n)   # abc008, alj002, ap001, bbc001, cna006, reu001 ...
# kinds: v = video (stock/PD), b = broadcast video (bc grade), s = still cover kenburns, c = still contain + blurfill
# ---- hand-authored cut list: per segment, [(kind, asset, dur)] ; the last entry fills to the next segment ----
CUTS = {
 "h1-s1":[("s","viirs",4.6),("b","cna019",0)],
 "i1-s1":[("c","litho",5.5),("c","parker",5.0),("c","baro",4.5),("c","reach",0)],
 "i1-s2":[("b","reu001",6.0),("b","alj002",4.8),("b","abc008",4.2),("s","haze",4.5),("b","alj018",3.7),("b","bbc001",4.2),("s","s3",0)],
 "c1-s1":[("s","oli",12.0),("b","cna006",3.5),("s","lava",5.0),("s","cop0702",5.0),("b","abc020",3.2),("b","ap001",6.5),("b","cna019",4.9),("s","s3",0)],
 "c2-s1":[("b","abc012",3.2),("b","alj004",6.6),("b","reu007",4.0),("b","abc016",3.6),("b","cna031",3.8),("b","reu006",7.4),("b","reu009",3.7),("b","abc014",3.0),("b","cna012",0)],
 "c3-s1":[("c","parker",5.0),("c","litho",5.0),("c","chart",5.0),("c","baro",6.0),("c","twilight",5.0),("c","sunset",4.0),("c","reach",6.0),("c","locprint",5.0),("b","alj018",3.7),("c","ctx2000",0)],
 "c4-s1":[("s","aster10",5.0),("s","cop19",5.0),("s","s2_22",5.0),("s","ls20",5.0),("b","ap001",6.5),("b","alj014",4.5),("b","bbc001",4.3),("s","ls18",0)],
 "c5-s1":[("b","bbc012",4.5),("b","alj015",3.2),("s","ls18",5.0),("b","bbc015",4.3),("s","aft1",5.0),("s","aft2",5.0),("s","rescue",5.0),("b","bbc005",4.3),("s","concert",5.0),("s","aft3",5.0),("b","bbc010",6.2),("b","bbc003",3.8),("b","alj014",0)],
 "c6-s1":[("s","ls20",6.0),("s","viirs",5.0),("b","abc020",3.2),("b","reu001",6.0),("s","s2_22",5.0),("s","cop19",5.0),("c","ctx2000",5.0),("b","cna006",3.5),("b","abc008",4.2),("s","oli",0)],
 "c7-s1":[("c","outline",10.0),("b","bbc001",4.3),("b","alj015",3.2),("s","haze",5.0),("b","reu002",4.0),("b","alj008",6.0),("b","cna012",6.0),("b","reu009",3.7),("c","outline",0)],
 "c8-s1":[("s","aft3",5.0),("s","aster10",5.0),("b","reu006",7.4),("b","alj004",6.6),("b","abc012",3.2),("s","cop0702",5.0),("b","cna031",3.8),("b","reu007",0)],
 "c8-s2":[("b","abc016",3.6),("b","alj008",5.0),("s","rescue",5.0),("s","concert",5.0),("b","abc014",3.0),("s","aft1",5.0),("s","aft2",0)],
 "z1-s1":[("b","alj002",4.8),("c","chart",5.0),("c","locprint",5.0),("b","bbc012",0)],
}
# ---- overlays: per segment, list of (type, id, big, sub, rel_at, hold). type: pf popfig, ch chip, lab source label, q quote
OV = {
 "h1-s1":[("pf","36k","36,000 DEAD","AUGUST 27, 1883",0.9,3.2),("pf","six","6 ERUPTIONS","IN ONE WEEK · SEPT 4–9",5.3,3.6),("lab","hook","SOURCE: NASA EARTH OBSERVATORY · VIIRS · SEPT 5, 2026",0.1,4.4)],
 "i1-s1":[("pf","20km","20 KM³","OF ROCK",2.4,3.2),("pf","3000","HEARD 3,000 MI","RODRIGUES ISLAND",8.2,3.4),("pf","7x","7 TIMES","AROUND THE PLANET",13.0,3.4),("pf","java","JAVA · SUMATRA","THE SEA, NOT THE ASH",17.5,3.6)],
 "i1-s2":[("ch","sept4","ERUPTING SINCE SEPTEMBER 4",1.0,4.5),("ch","nobody","THE ONE NOBODY FILMED",12.5,5.0),("pf","dec22","DEC 22, 2018","A NIGHT IN DECEMBER",16.2,3.2),("ch","where","COMMENT: WHERE ARE YOU WATCHING FROM?",29.5,5.5)],
 "c1-s1":[("lab","oli","SOURCE: NASA EARTH OBSERVATORY · LANDSAT OLI · SEPT 5, 2026",0.2,11.5),("pf","25h","25 HOURS","SEPT 4, 11:07 PM → SEPT 6",6.0,3.4),("pf","lvl3","LEVEL III","SIAGA · SINCE JULY 2",12.8,3.4),("pf","3km","3 KM","EXCLUSION ZONE",18.0,3.0),("pf","28s","28 SECONDS","WEDNESDAY, 00:47",30.5,3.2),("pf","6er","6 ERUPTIONS","IN ONE WEEK",35.0,3.2),("q","pvmbg","“Volcanic activity remains high, and the possibility of another eruption in the near future remains.”","SITI SUMILAH RITA SUSILAWATI · HEAD OF PVMBG",43.0,8.4)],
 "c2-s1":[("pf","glass","PULVERISED GLASS","NOT SMOKE",3.6,3.2),("pf","ba9","4 ENGINES OUT","BRITISH AIRWAYS 9 · 1982",10.0,3.4),("pf","13m","13 MINUTES","GLIDING",16.0,3.0),("pf","39","39 WARNINGS","TO PILOTS THIS WEEK",24.5,3.2),("pf","15k","15,000 FT","ASH, DRIFTING WEST",29.0,3.0),("pf","8ap","8 AIRPORTS","AFFECTED",34.0,3.0),("pf","209","209 CANCELLED","JAKARTA · SOEKARNO-HATTA",38.0,3.4)],
 "c3-s1":[("pf","aug27","AUG 27, 1883","FOUR EXPLOSIONS",1.0,3.2),("pf","1002","10:02 AM","THE ISLAND TORE APART",6.5,3.2),("ch","rodrigues","RODRIGUES · 3,000 MILES · “HEAVY GUNS”",11.5,5.0),("lab","baro","SOURCE: ROYAL SOCIETY, 1888 · BAROGRAMS",21.0,5.8),("pf","36h","36 HOURS","EVERY PASS OF THE WAVE",22.5,3.2),("pf","c04","−0.4 °C","FOR A YEAR",31.5,3.2),("pf","30m","30 M WAVES","THE KILLER WAS THE SEA",41.0,3.4),("pf","165","165 VILLAGES","ERASED",46.0,3.4)],
 "c4-s1":[("pf","1927","1927","STEAM FROM THE SEA",3.0,3.2),("pf","1930","1930","A NEW CONE",8.5,3.0),("ch","anak","ANAK KRAKATAU · “CHILD OF KRAKATOA”",13.0,5.0),("pf","338","338 M","BY 2018",23.0,3.2),("pf","fell","INTO THE SEA","DECEMBER 22, 2018",33.0,3.4)],
 "c5-s1":[("ch","xmas","SATURDAY NIGHT · TWO DAYS BEFORE CHRISTMAS",1.0,5.0),("pf","noeq","NO EARTHQUAKE","NO WARNING",11.0,3.4),("pf","02","0.2 KM³","OF ROCK",20.5,3.2),("ch","guess","GUESS: HOW MANY MINUTES?",27.0,5.0),("pf","30min","UNDER 30 MIN","IN THE DARK, NO SIREN",34.5,3.6),("pf","437","437 DEAD","DECEMBER 22, 2018",47.5,3.4),("pf","110","338 → 110 M","OVERNIGHT",55.5,3.6)],
 "c6-s1":[("lab","ls20","SOURCE: USGS LANDSAT 8 · APRIL 2020",0.2,5.6),("pf","shape","SHAPE","TOO STEEP, TOO FAST",9.0,3.2),("pf","tremor","TREMOR","HOW MUCH MAGMA MOVES",19.5,3.2),("pf","tilt","TILT","RISING SINCE AUGUST",28.0,3.4),("ch","inflate","RISING TILT = THE MOUNTAIN IS INFLATING",33.0,5.0),("ch","magma","MAGMA INDONESIA · PUBLIC, WITHIN MINUTES",44.5,6.0),("lab","oli2","SOURCE: NASA EARTH OBSERVATORY · SEPT 5, 2026",43.5,8.0)],
 "c7-s1":[("pf","banten","BANTEN","JAVA SIDE",3.5,3.0),("pf","lampung","LAMPUNG","SUMATRA SIDE",7.0,3.0),("ch","only","THE ONLY COAST A KRAKATAU TSUNAMI CAN REACH",11.0,5.0),("pf","jakarta","JAKARTA · ASH","BREATHING AND FLIGHTS",17.5,3.4),("pf","bali","BALI · FLIGHTS","VIA JAKARTA",27.5,3.4),("ch","cancel","A CANCELLED CONNECTION, NOT A WAVE",36.0,6.0)],
 "c8-s1":[],
 "c8-s2":[],
 "z1-s1":[("pf","awake","AWAKE","THE CHILD OF KRAKATOA",1.2,3.2)],
}
BUG_A = ["ANAK KRAKATAU: SIX ERUPTIONS IN ONE WEEK, LEVEL III, 3 KM EXCLUSION",
         "1883: MORE THAN 36,000 DEAD, HEARD 3,000 MILES AWAY",
         "39 ASH WARNINGS TO PILOTS, EIGHT AIRPORTS AFFECTED",
         "PVMBG: 'ANOTHER ERUPTION IN THE NEAR FUTURE REMAINS POSSIBLE'"]
BUG_B = ["DEC 22, 2018: FLANK COLLAPSE, TSUNAMI, 437 DEAD, NO SIREN",
         "TILTMETER AT TANJUNG STATION RISING SINCE EARLY AUGUST",
         "BMKG: NO SEA-LEVEL ANOMALY THIS WEEK",
         "TAMBORA 1815 WAS THE YEAR WITHOUT A SUMMER, NOT KRAKATOA",
         "THREE THINGS TO DO"]

# ---- stage media ----
media = os.path.join(E, "media"); os.makedirs(os.path.join(media, "bc"), exist_ok=True); os.makedirs(os.path.join(media, "stills"), exist_ok=True)
used = {}
def stage(asset):
    src = os.path.join(P, A[asset]); sub = "bc" if A[asset].startswith("broadcast") else "stills"
    dst = os.path.join(media, sub, os.path.basename(A[asset]))
    if not os.path.exists(dst):
        if sub == "stills":
            # cap at 1920 wide, convert webp -> jpg
            base, ext = os.path.splitext(dst)
            if ext.lower() == ".webp": dst = base + ".jpg"
            if not os.path.exists(dst):
                subprocess.run(["ffmpeg","-v","error","-y","-i",src,"-vf","scale='min(1920,iw)':-2",dst], check=True)
        else:
            shutil.copy(src, dst)
    return f"media/{sub}/{os.path.basename(dst)}"

# ---- emit track 1 ----
t1 = []; kbs = []; drifts = []
for k in order:
    start = S[k]; end = S[order[order.index(k)+1]] if k != "z1-s1" else CLOSE_AT
    if k == "c4-s1": end = CTA_IN
    cuts = CUTS[k]; tt = start
    for i, (kind, asset, dur) in enumerate(cuts):
        d = round(end - tt, 3) if i == len(cuts)-1 else dur
        if d <= 0.3: break
        used[asset] = used.get(asset, 0) + 1
        cb = ' data-callback="second use, different chapter"' if used[asset] > 1 else ""
        src = stage(asset); sid = f"{k.replace('-','')}-{i}-{asset}"
        if kind in ("s","c"):
            cls = "clip still-wrap" + (" contain-wrap" if kind == "c" else "")
            blur = f'<img class="blurfill" src="{src}" alt="">' if kind == "c" else ""
            t1.append(f'  <section class="{cls}" id="c-{sid}" data-start="{tt}" data-duration="{d}" data-track-index="1"{cb}>{blur}<img id="kb-{sid}" src="{src}" alt=""></section>')
            j = len(kbs) % 4
            kbs.append(f'  kb("#kb-{sid}", {tt}, {d}, ' + ["1.0, 1.08, 0, -14, 0, -8", "1.08, 1.0, 12, 0, 6, 0", "1.0, 1.07, 0, 12, 0, -6", "1.06, 1.0, -10, 0, 6, 0"][j] + ");")
        else:
            cls = ' class="bc"' if kind == "b" else ""
            t1.append(f'  <video id="vx-{sid}"{cls} src="{src}" data-start="{tt}" data-duration="{d}" data-track-index="1"{cb} muted></video>')
        tt = round(tt + d, 3)
over = {a: n for a, n in used.items() if n > 2}
assert not over, f"assets used more than twice: {over}"

# ---- overlays ----
ov = []; ovjs = []
for k in order:
    for o in OV[k]:
        typ, oid = o[0], o[1]; at = round(S[k] + o[-2], 3); hold = o[-1]
        if typ == "pf":
            ov.append(f'  <section class="clip" id="p-pf-{oid}" data-start="{at}" data-duration="{hold}" data-track-index="5"><div class="popfig" id="pf-{oid}"><span class="pf-big">{o[2]}</span><span class="pf-sub">{o[3]}</span></div></section>')
            ovjs.append(f'  pop("#pf-{oid}", {at}, {hold});')
        elif typ == "ch":
            ov.append(f'  <section class="clip" id="p-chip-{oid}" data-start="{at}" data-duration="{hold}" data-track-index="5"><div class="chip" id="chip-{oid}">{o[2]}</div></section>')
            ovjs.append(f'  chip("#chip-{oid}", {at}, {hold});')
        elif typ == "lab":
            ov.append(f'  <section class="clip" id="p-src-{oid}" data-start="{at}" data-duration="{hold}" data-track-index="4"><div class="srclab">{o[2]}</div></section>')
            ovjs.append(f'  lab("#p-src-{oid} .srclab", {at}, {hold});')
        elif typ == "q":
            ov.append(f'  <section class="clip" id="p-q-{oid}" data-start="{at}" data-duration="{hold}" data-track-index="5"><div class="quotecard" id="q-{oid}"><div class="q">{o[2]}</div><div class="attr">{o[3]}</div></div></section>')
            ovjs.append(f'  tl.fromTo("#q-{oid}", {{ autoAlpha: 0, y: 30 }}, {{ autoAlpha: 1, y: 0, duration: 0.6, ease: "power3.out" }}, {at}); tl.to("#q-{oid}", {{ autoAlpha: 0, y: -20, duration: 0.4 }}, {round(at+hold-0.4,3)});')

# ---- presenter loops cut to windows ----
PIP_A = (S["i1-s1"], round(CTA_IN - S["i1-s1"], 3))
PIP_B = (S["c5-s1"], round(CLOSE_AT - S["c5-s1"], 3))
for tag, (st, du) in (("a", PIP_A), ("b", PIP_B)):
    for loop in ("talk", "idle"):
        out = os.path.join(media, "pip", f"paul-{loop}-{tag}.mp4")
        if not os.path.exists(out):
            subprocess.run(["ffmpeg","-v","error","-y","-stream_loop","-1","-i",os.path.join(media,"pip",f"paul-{loop}.mp4"),"-t",str(du),
                            "-vf","scale=240:240","-an","-c:v","libx264","-crf","31","-pix_fmt","yuv420p","-movflags","+faststart",out], check=True)

# ---- talk toggles from words.json ----
def spans(k):
    w = json.load(open(os.path.join(E,"audio",f"{k}.words.json"))); words = w if isinstance(w,list) else w.get("words", w)
    ws = [(float(x["start"]), float(x["end"])) for x in words]
    out = []
    for a, b in ws:
        if out and a - out[-1][1] < 0.35: out[-1][1] = b
        else: out.append([a, b])
    return out
toggles = []
for k in order:
    if k in ("h1-s1",): continue
    tag = "a" if S[k] < CTA_IN else "b"
    if k == "z1-s1":
        for a, b in spans(k):
            if S[k] + a >= CLOSE_AT: break
            toggles.append(f'  tl.to("#pip-talk-{tag}", {{ autoAlpha: 1, duration: 0.1 }}, {round(S[k]+a,2)}); tl.to("#pip-talk-{tag}", {{ autoAlpha: 0, duration: 0.1 }}, {round(min(S[k]+b, CLOSE_AT-0.2),2)});')
        continue
    for a, b in spans(k):
        toggles.append(f'  tl.to("#pip-talk-{tag}", {{ autoAlpha: 1, duration: 0.1 }}, {round(S[k]+a,2)}); tl.to("#pip-talk-{tag}", {{ autoAlpha: 0, duration: 0.1 }}, {round(S[k]+b,2)});')

# ---- card cue times (relative) ----
def word_at(k, phrase):
    w = json.load(open(os.path.join(E,"audio",f"{k}.words.json"))); words = w if isinstance(w,list) else w.get("words", w)
    txt = [(x["word"].strip().lower().strip(".,;:!?\"'"), float(x["start"])) for x in words]
    first = phrase.split()[0].lower()
    for i,(wd,st) in enumerate(txt):
        if wd == first and " ".join(t[0] for t in txt[i:i+len(phrase.split())]) == phrase.lower(): return st
    raise SystemExit(f"cue not found: {k} '{phrase}'")
notyes_rows = [word_at("c8-s1","nobody is forecasting"), word_at("c8-s1","the ash is not"), word_at("c8-s1","and the year without")]
check_rows = [word_at("c8-s2","if you are on"), word_at("c8-s2","if you are booked"), word_at("c8-s2","and if you are anywhere")]

head = open(os.path.join(E, "_build", "head.html"), encoding="utf-8").read()
html = [head, "<body>", f'<div id="root" data-composition-id="ms-krakatoa-1883" data-start="0" data-width="1920" data-height="1080" data-duration="{DUR}" data-fps="30">', "",
        "  <!-- ============ NARRATION ============ -->"]
for k in order:
    html.append(f'  <audio id="nx-{k.replace("-","")}" src="audio/{k}.wav" data-start="{S[k]}" data-duration="{man[k]["duration"]}" data-volume="1"></audio>')
html += ["", f"  <!-- ============ CTA (channel.cta v5; {CTA_AT} = {round(100*CTA_AT/DUR)} % — after CH4, hook > CTA > payoff) ============ -->",
  f'  <video id="ins-cta-paul" src="media/cta/paul-storm-ready-v5-sep6.mp4" data-start="{CTA_AT}" data-duration="{CTA_DUR}" data-track-index="1" data-volume="1" data-has-audio="true" data-srt-label="[PAUL RAYMOND — STORM-READY HOME · paulraymond.online]"></video>',
  f'  <section class="clip blackout" id="bo-cta-in" data-start="{CTA_IN}" data-duration="1.0" data-track-index="1"></section>',
  f'  <section class="clip blackout" id="bo-cta-out" data-start="{CTA_OUT}" data-duration="1.0" data-track-index="1"></section>', "",
  "  <!-- ============ MUSIC + BEDS (narration above every bed: score 0.13, ambience ≤0.20) ============ -->",
  f'  <audio id="sx-mus-a" src="media/score-act5-tension.mp3" data-bed="" data-start="0" data-duration="{CTA_IN}" data-volume="0.13"></audio>',
  f'  <audio id="sx-mus-b" src="media/score-act3-urgent.mp3" data-bed="" data-start="{CTA_OUT}" data-duration="{round(S["c8-s2"]-CTA_OUT,3)}" data-volume="0.13"></audio>',
  f'  <audio id="sx-mus-c" src="media/score-act6-close.mp3" data-bed="" data-start="{S["c8-s2"]}" data-duration="{round(DUR-S["c8-s2"],3)}" data-volume="0.16"></audio>',
  f'  <audio id="sx-rumble-hook" src="media/04_distant_storm_rumble.mp3" data-bed="" data-start="0" data-duration="{round(S["c1-s1"],3)}" data-volume="0.16"></audio>', "",
  "  <!-- ============ PRESENTER CIRCLE (bare timed videos + ring sections; hidden in hook, CTA, close) ============ -->",
  f'  <video id="pip-idle-a" class="pip" src="media/pip/paul-idle-a.mp4" data-start="{PIP_A[0]}" data-duration="{PIP_A[1]}" data-track-index="6" muted></video>',
  f'  <video id="pip-talk-a" class="pip" src="media/pip/paul-talk-a.mp4" data-start="{PIP_A[0]}" data-duration="{PIP_A[1]}" data-track-index="7" data-callback="presenter loop, talking" muted></video>',
  f'  <video id="pip-idle-b" class="pip" src="media/pip/paul-idle-b.mp4" data-start="{PIP_B[0]}" data-duration="{PIP_B[1]}" data-track-index="6" data-callback="presenter loop, listening" muted></video>',
  f'  <video id="pip-talk-b" class="pip" src="media/pip/paul-talk-b.mp4" data-start="{PIP_B[0]}" data-duration="{PIP_B[1]}" data-track-index="7" data-callback="presenter loop, talking" muted></video>',
  f'  <section class="clip" id="pip-ring-a" data-start="{PIP_A[0]}" data-duration="{PIP_A[1]}" data-track-index="8"><div class="pipring"></div></section>',
  f'  <section class="clip" id="pip-ring-b" data-start="{PIP_B[0]}" data-duration="{PIP_B[1]}" data-track-index="8"><div class="pipring"></div></section>', "",
  "  <!-- ============ NEWS BUG (track 3; off during the CTA and the close) ============ -->",
  f'  <section class="clip" id="bug-a" data-start="{PIP_A[0]}" data-duration="{PIP_A[1]}" data-track-index="3"><div class="bugstrip" id="bugstrip-a"><div class="bk">BREAKING</div><div class="bw">The Warning Hour</div><div class="bh" id="bh-a"></div></div></section>',
  f'  <section class="clip" id="bug-b" data-start="{PIP_B[0]}" data-duration="{PIP_B[1]}" data-track-index="3"><div class="bugstrip" id="bugstrip-b"><div class="bk">BREAKING</div><div class="bw">The Warning Hour</div><div class="bh" id="bh-b"></div></div></section>', "",
  "  <!-- ============ TRACK 1 — hand-authored cut list ============ -->"] + t1 + ["",
  "  <!-- ============ OVERLAYS ============ -->"] + ov + ["",
  "  <!-- ============ CARDS + CLOSE ============ -->",
  f'  <div id="host-notyes" data-composition-id="notyes" data-composition-src="compositions/notyes.html" data-start="{S["c8-s1"]}" data-duration="{man["c8-s1"]["duration"]}" data-track-index="2" data-width="1920" data-height="1080"></div>',
  f'  <div id="host-checklist" data-composition-id="statcard" data-composition-src="compositions/statcard.html" data-start="{S["c8-s2"]}" data-duration="{man["c8-s2"]["duration"]}" data-track-index="2" data-width="1920" data-height="1080"></div>',
  f'  <section class="clip blackout" id="bo-close" data-start="{CLOSE_AT}" data-duration="{round(DUR-CLOSE_AT,3)}" data-track-index="1"></section>',
  f'  <div id="host-close" data-composition-id="g-close" data-composition-src="compositions/g-close.html" data-start="{CLOSE_AT}" data-duration="{round(DUR-CLOSE_AT,3)}" data-track-index="2" data-width="1920" data-height="1080"></div>', "",
  '  <div id="grade"></div>', '  <div id="vignette"></div>', '  <canvas id="grain" width="480" height="270"></canvas>', "</div>",
  '<script src="grain.js"></script>', "<script>", "window.__timelines = window.__timelines || {};", "(function () {",
  "  const tl = gsap.timeline({ paused: true });", f"  const DUR = {DUR};",
  open(os.path.join(E, "_build", "helpers.js"), encoding="utf-8").read(),
  "  /* ---- stills: every hold moves ---- */"] + kbs + ["  /* ---- overlays ---- */"] + ovjs + [
  "  /* ---- presenter talk-sync (audio/*.words.json spans, gap < 0.35 s) ---- */",
  '  tl.set(["#pip-talk-a", "#pip-talk-b"], { autoAlpha: 0 }, 0);'] + toggles + [
  "  /* ---- news bug ---- */",
  f'  bug("#bugstrip-a", "#bh-a", {PIP_A[0]}, {PIP_A[1]}, {json.dumps(BUG_A)});',
  f'  bug("#bugstrip-b", "#bh-b", {PIP_B[0]}, {PIP_B[1]}, {json.dumps(BUG_B)});',
  "  filmLayer(tl, DUR);",
  f'  tl.to(["#vignette", "#grade", "#grain", ".dust"], {{ autoAlpha: 0, duration: 0.3 }}, {CTA_AT});',
  f'  tl.to(["#vignette", "#grade", ".dust"], {{ autoAlpha: 1, duration: 0.3 }}, {CTA_OUT});',
  f'  tl.to("#grain", {{ autoAlpha: 0.10, duration: 0.3 }}, {CTA_OUT});',
  '  window.__timelines["ms-krakatoa-1883"] = tl;', "})();", "</script>", "</body>", "</html>"]
open(os.path.join(E, "index.html"), "w", encoding="utf-8").write("\n".join(html))
# card cue patches
for comp, rows, dur in (("notyes", notyes_rows, man["c8-s1"]["duration"]), ("statcard", check_rows, man["c8-s2"]["duration"])):
    p = os.path.join(E, "compositions", f"{comp}.html"); s = open(p, encoding="utf-8").read()
    s = re.sub(r'(tl\.fromTo\(P\+"r1".*?\}, )[0-9.]+\);', lambda m: f"{m.group(1)}{round(max(rows[0],0.8),2)});", s)
    s = re.sub(r'(tl\.fromTo\(P\+"r2".*?\}, )[0-9.]+\);', lambda m: f"{m.group(1)}{round(rows[1],2)});", s)
    s = re.sub(r'(tl\.fromTo\(P\+"r3".*?\}, )[0-9.]+\);', lambda m: f"{m.group(1)}{round(rows[2],2)});", s)
    s = re.sub(r'(tl\.to\(P\+"card", \{x:-900, autoAlpha:0, duration:0\.5, ease:"power3\.in"\}, )[0-9.]+\);', lambda m: f"{m.group(1)}{round(dur-0.6,2)});", s)
    s = re.sub(r'repeat:\d+', f'repeat:{int(dur/1.4)}', s)
    open(p, "w", encoding="utf-8").write(s)
print("schedule:", {k: S[k] for k in order}); print("CTA", CTA_IN, CTA_AT, CTA_OUT, "close", CLOSE_AT, "DUR", DUR, "pip", PIP_A, PIP_B)
print("uses>1:", {a: n for a, n in used.items() if n > 1}); print("card rows", notyes_rows, check_rows)
