"""Build the reels study page (v2: the accounts the owner named, last 45 days, views against each
account's own median). Usage: python3 build_v2.py <v2_dir> <devq_dir>"""
import json, os, sys, html, glob
from PIL import Image

V2, DEVQ = sys.argv[1], sys.argv[2]
IMG = os.path.join(DEVQ, "shorts-study-v2")
os.makedirs(IMG, exist_ok=True)
E = html.escape

# What each account does, written after viewing its contact sheets (which ones: see VIEWED).
ACCOUNTS = [
    ("oddhourtales", "Interactive horror serial. You are the lighthouse keeper. A rule sheet, a clock in the corner, "
     "'Night 1 of 7'. Each reel ends on a choice; the comments vote; the next reel opens 'You chose to…'.", "serial"),
    ("dontopenit.stories", "Same machine as oddhourtales: 'Night 1/7', clock, 'Help in 7 days', a phone emergency alert, "
     "numbered rules. Ends 'Comment STAY or LEAVE. The most votes decides.'", "serial"),
    ("charles.zhengg", "One everyday thing followed end to end as an animated journey with a running counter in the corner "
     "(milliseconds, kilometres). Title on frame one names something of yours: 'THE PHOTO YOUR MOM JUST SENT is 4,000 m under the Pacific right now'. "
     "His face appears for about two seconds mid-video, not at the start.", "journey"),
    ("zhscience", "One body or household question per reel ('Why does your leg bounce when you sit?'), flat illustration of "
     "an ordinary person, two-line captions with one bold word, a study cited in the middle. 10 posts, 2,607 followers.", "question"),
    ("canwebuildthis", "Two recurring 3D characters: a woman and a small orange AI. Skits about working with AI, speech-bubble "
     "dialogue, a whiteboard that fills in. 'Explain it like I'm five: what's an API? No technical words allowed.'", "skit"),
    ("factloree", "Stick figure and simple line shapes on a dark background, one idea per reel, almost no text. "
     "One reel did 5.2M against a 5.5K median; the other 56 did not.", "minimal"),
    ("elipsi.studio", "A motivational line turned into a diagram: headlights show 50 m, a counter runs to 917 km, "
     "'50 meters is enough'. One reel at 790K on 1,312 followers; median is 2K.", "minimal"),
    ("realm.of.many", "A village that grows with the account: every follower gets a cabin with their handle on it; comments "
     "ask for buildings and get built. 'Follow → your cabin · Comment → we build'.", "world"),
    ("ameliagonzamonte", "Talking head that takes apart someone else's viral video. The video being discussed sits in a small "
     "frame under her chin the whole time, with words circled and underlined as she names them.", "breakdown"),
    ("kallawaymarketing", "See the script and frame-one sections below.", "teacher"),
]
VIEWED = ("Sheets I opened myself: the top reel of every account, two each for charles.zhengg and dontopenit.stories, "
          "three for Kallaway, two SFX reels. The other sheets were built but not opened.")

# Kallaway, sentence by sentence. (seconds, sentence, why it is there)
K1 = ("De_5mQ0R8PE", [
    (0, "Here's how to write a hook so good, it is scientifically impossible to skip.",
     "Topic and outcome in one line. At the same moment the title 'How To Create a Killer Hook' is on screen and a script page lights its hook lines green: the topic is said, written and shown at once."),
    (4, "This is called the triple hook method.",
     "Gives it a name. A named method is a thing you can own, and 'triple' tells you the cost: three parts."),
    (6, "And if you do this right, it will hypnotize a viewer such that they physically cannot scroll away.",
     "What you get. A second pull before any teaching starts."),
    (11, "All right, step one is the context.", "Signpost: you are at 1 of 3."),
    (13, "And this is the basic step, but so many people still get this wrong.",
     "Blocks the 'I know this' exit: admits it is basic, then says you probably fail it."),
    (16, "Viewers only watch content where they have a vested interest in the topic.", "The reason, in one sentence."),
    (20, "So the first line of your hook must establish context on what the video is gonna be about.", "The rule."),
    (24, "You can say it in the audio. […example clip…] Show it in the visuals, write it in the text or caption, ideally all three, but the context must be established immediately.",
     "How to do it, with a real clip played in the middle of the sentence."),
    (34, "We have data that shows even delaying the context to the back half of the first sentence increases the skip rate dramatically.",
     "Proof, and a specific nobody expects (the back half of one sentence)."),
    (40, "So priority number one is to set immediate context as soon as possible.", "One-line recap. Step one is closed."),
    (44, "Now step two in the triple hook is where most people mess up.", "New reason to stay, placed exactly at the step change."),
    (47, "This is called the lean.", "Names it."),
    (48, "What you're trying to do is get someone curious in a certain direction. You wanna make them lean in on the context to actively want to hear more.", "Defines it."),
    (56, "You can give some proof or stat validating the incoming claim, reference a specific pain point they have or a benefit they want, or share something interesting, shocking, or unexpected.",
     "The usable part: three ways to do it today."),
    (69, "But regardless of what you pick, the viewer must lean in instead of opt out.", "The rule again, as a pass/fail."),
    (73, "So when you read back that first one to two sentences just on its own, is the context immediately clear and is there some curiosity inducement that makes the viewer want to lean in for more?",
     "A test the viewer can run on their own script."),
    (83, "It's called the context lean. This is what opens the curiosity loop you hear everybody talk about.", "Recap, tied to a term the viewer already knows."),
    (88, "Now step three in the triple hook is really where the money's made. Like 1% of people know how to do this.",
     "The strongest pull is saved for the last step."),
    (93, "I call it the contrarian snapback.", "Names it."),
    (94, "To catch a fish, you gotta get the hook in its mouth swimming one way and then yank the line going another direction.",
     "One picture that explains the idea."),
    (100, "Not to be morbid, but storytelling works the exact same way.", "A human aside that carries the picture back to the topic."),
    (102, "The goal is to say something in the contrarian snapback that pulls the viewer away from the direction they were leaning.", "Defines it."),
    (111, "That triple combination of rapidly buying into the context, leaning in based on some curiosity and then getting snapped back in another direction is the God tier hook formula that works every single time.",
     "The whole method in one sentence: the thing promised in line one, delivered."),
    (121, "Now, if you wanna learn how to actually do this in practice with examples, I've linked a video where I explain it in more detail.",
     "Opens a new gap right after the payoff: you have the theory, not the practice."),
    (127, "Over 700,000 people have watched this and I'm telling you, it's probably the best hook training on the internet.", "Proof for the offer."),
    (132, "Comment hooks and I'll send it to you so you can watch it.", "One action, one word."),
])
K2 = ("DfPXiP0RhNl", [
    (0, "This is the best database in the world for short form video references.", "What it is, with a superlative. The thing itself is on screen."),
    (4, "There are over a hundred different collections across formats, editing styles, visual hooks, and signature series.", "Size, with a number."),
    (8, "Within each collection, there are tons of examples from top creators across a variety of different niches.", "'Different niches' means: this includes yours."),
    (14, "So this has been hand curated as one of the best visual reference libraries on the internet.", "Why trust it."),
    (18, "Inside of each collection, you can click into any video, get the full transcript as well as deep analysis on the idea topic, hook, and format.", "What you can do with it."),
    (26, "If you want to get more exposure to the top videos that are crushing across different niches, this will be super valuable.", "Who it is for."),
    (31, "Comment collections and I'll send through the link.", "One action, one word."),
])
K_SKELETON = [
    ("Line 1", "The topic plus the outcome the viewer wants, with a superlative.", "“Here's how to write a hook so good, it is basically unskippable.”"),
    ("Line 2", "Name the method.", "“This is called the desire hook method.”"),
    ("Line 3", "What you get if you do it.", "“And if you do this right, it'll turn viewers into buyers at a crazy rate.”"),
    ("Each step", "Signpost → why most people fail it → the rule → an example → one-line recap.", "“Step one is to lead with the desired outcome. Most hooks tease secret information. But…”"),
    ("Each step change", "A fresh reason to stay, stronger each time.", "“Now step two… is where most people mess up.” → “step three… is really where the money's made.”"),
    ("Once", "A picture from outside the topic.", "The fish on the line; the casino dealing the next hand."),
    ("Before the end", "The whole method in one sentence.", "“This combination, stakes, the big question, the head fake and the rehook is all you need…”"),
    ("End", "A new gap, proof for the offer, then one word to comment.", "“Over 100,000 people have watched this… Comment storytelling and I'll send it through.”"),
]
SHEETS = [  # (handle, code, kind, caption) shown full width
    ("kallawaymarketing", "De_5mQ0R8PE", "open", "Kallaway, first 3 seconds (a frame every 0.25 s). Title on top, a script page whose hook lines turn green, then a phone playing an example reel; one-word captions; his face in a box on the bottom third. 905K views."),
    ("kallawaymarketing", "Dewd5EDO-16", "open", "Kallaway, first 3 seconds. Title 'This Is The Reason Why Your Video Fails'; a retention graph draws its falling curve while he says the line; full-frame face only from about 1.75 s. 224K views."),
    ("kallawaymarketing", "DefOCNPs10U", "open", "Kallaway, a weak one (0.41x his median). Same layout, but the middle is unreadable chips floating around: nothing is about to happen and nothing can be read."),
    ("charles.zhengg", "DeRGuEtBk3m", "whole", "charles.zhengg, 11.7M views. Twelve frames across the video: the title, then a millisecond counter in the corner all the way through, his face once."),
    ("dontopenit.stories", "DerRE1gstj_", "whole", "dontopenit.stories, 7.5M views. Clock, 'Night 1/7', 'Help in 7 days', the emergency alert, rule tags, a note."),
    ("oddhourtales", "DfQTUGYxxyb", "whole", "oddhourtales, 3.9M views. A lighthouse in a storm, the rule sheet, the clock, the radio."),
    ("zhscience", "DfbCFfAIQj1", "whole", "zhscience, 3.0M views on 2,607 followers."),
    ("ameliagonzamonte", "De2nFEHx4Uy", "whole", "ameliagonzamonte, 7.0M views. The video under discussion stays pinned under her chin, with words underlined as she names them."),
    ("realm.of.many", "Demvtlfirc8", "whole", "realm.of.many, 277K views (33x its median). Cabins carry followers' handles."),
]
DIRECTIONS = [
    ("1", "The Warning Hour, played by the viewer", "copies oddhourtales + dontopenit.stories",
     "A real storm, told as a serial where the viewer is in it. Frame one: a clock, the date, the town, a phone alert. "
     "Rules on a card are the real safety rules for that storm. Each reel ends on the choice real people faced "
     "(stay or drive, basement or bathtub, leave the island or wait). Comments vote. The next reel opens 'Most of you chose to drive' "
     "and shows what happened to the people who did, from the record. Paul is the voice on the radio that cuts in with the forecast: "
     "the brand is present in every reel without a face on frame one.",
     "Why first: it is the only format here where every recent reel is large (the two serial accounts' medians are the two highest in the table), "
     "the name of the channel already describes it, and the vote is a comment, which is what the comment-to-DM funnel needs. "
     "Nobody found here is doing it with true events."),
    ("2", "Right now, above you", "copies charles.zhengg",
     "One storm object followed end to end with a counter in the corner. Frame-one title names something of the viewer's: "
     "'THE HAIL THAT HITS YOUR CAR TONIGHT is 9 km up right now'. The counter runs (height, temperature, seconds to the ground). "
     "Paul appears once, for two seconds, in the middle.",
     "Why second: two reels in 45 days at 119x and 157x the account's median, and the format is a pure animation job. Needs a real number at every step."),
    ("3", "One question about your own body or house in weather", "copies zhscience",
     "'Why do your ears pop before a storm?' 'Why does the sky go green?' 20–30 s, flat illustration, a study in the middle, answer at the end.",
     "Why third: cheapest to make daily; 3.0M on an account with 2,607 followers. Lowest ceiling for the brand because nothing in it is ours."),
    ("4", "Paul in the box (Kallaway's layout)", "copies kallawaymarketing",
     "Title on top, a diagram that draws itself in the middle, Paul in a rounded box on the bottom third, one-word captions. "
     "Script on Kallaway's skeleton: outcome line, named method, steps with a reason to stay at each change.",
     "Use for authority pieces and for the giveaway reels. Kallaway's own median is 53K on 240K followers: it converts (thousands of comments), it does not spread like the three above."),
    ("5", "Storm Town (wild card)", "copies realm.of.many, bent",
     "Every follower gets a house with their handle in one animated town. Each Friday a real historical storm hits the town at its real strength; "
     "houses whose owners commented the right preparation that week are standing on Saturday.",
     "Untested anywhere. It turns the follow into a stake in the story. One reel of realm.of.many did 277K; its median is 8K, so the mechanic alone is not enough."),
]


def thumb(handle, code):
    src = os.path.join(V2, "media", handle, f"{code}.whole.jpg")
    dst = os.path.join(IMG, f"{code}.jpg")
    if os.path.exists(src) and not os.path.exists(dst):
        Image.open(src).crop((0, 0, 270, 480)).save(dst, quality=82)
    return f"shorts-study-v2/{code}.jpg" if os.path.exists(dst) else ""


def sheet(handle, code, kind):
    src = os.path.join(V2, "media", handle, f"{code}.{kind}.jpg")
    dst = os.path.join(IMG, f"{code}.{kind}.jpg")
    if not os.path.exists(dst):
        Image.open(src).save(dst, quality=80)
    return f"shorts-study-v2/{code}.{kind}.jpg"


def first_words(handle, code, limit=7.0):
    p = os.path.join(V2, "media", handle, f"{code}.mp4.tr.json")
    if os.path.exists(p):
        segs = json.load(open(p, encoding="utf-8"))["segments"]
        said = " ".join(s["text"] for s in segs if s["start"] < limit).strip()
        if said:
            return "said: " + said
    p = os.path.join(V2, "media", handle, f"{code}.info.json")
    if os.path.exists(p):
        cap = (json.load(open(p, encoding="utf-8")).get("description") or "").split("\n")[0].strip()
        if cap:
            return "caption: " + cap[:160]
    return ""


def fmt(n):
    return f"{n/1e6:.1f}M" if n >= 1e6 else f"{n/1e3:.0f}K" if n >= 1e3 else str(int(n))


def load(handle):
    p = json.load(open(os.path.join(V2, "media", handle, "picks.json"), encoding="utf-8"))
    for r in p["picks"]:
        dj = os.path.join(V2, "media", handle, f"{r['code']}.dur.json")
        r["dur"] = json.load(open(dj))["duration"] if os.path.exists(dj) else None
    foll = next((l for l in p["header"].splitlines() if "followers" in l), "")
    return p, foll


rows, cards = [], []
for handle, what, _ in ACCOUNTS:
    p, foll = load(handle)
    top = [r for r in p["picks"] if r["x_median"] and r["x_median"] >= 1][:6]
    rows.append((p["median_views"], handle, foll, p["recent_n"], top[0] if top else None))
    reels = "".join(
        f'<a class="reel" href="https://www.instagram.com/reel/{r["code"]}/" target="_blank">'
        f'<img src="{thumb(handle, r["code"])}" loading="lazy"><b>{fmt(r["views"])}</b> · {r["x_median"]}x'
        f'<span>{r["date"][5:]}{" · " + str(round(r["dur"])) + " s" if r["dur"] else ""}</span>'
        f'<em>{E(first_words(handle, r["code"])[:150])}</em></a>' for r in top)
    cards.append(f'<section class="card"><h3>@{handle} <small>{E(foll)} · {p["recent_n"]} reels in 45 days · median {fmt(p["median_views"])}</small></h3>'
                 f'<p>{E(what)}</p><div class="reels">{reels}</div></section>')

table = "".join(
    f"<tr><td>@{h}</td><td>{E(f)}</td><td>{n}</td><td>{fmt(m)}</td><td>{fmt(t['views']) + ' (' + str(t['x_median']) + 'x)' if t else ''}</td></tr>"
    for m, h, f, n, t in sorted(rows, reverse=True))


def breakdown(code, lines):
    p, _ = load("kallawaymarketing")
    r = next(x for x in p["picks"] if x["code"] == code)
    body = "".join(f"<tr><td>{s} s</td><td>{E(t)}</td><td>{E(w)}</td></tr>" for s, t, w in lines)
    return (f'<h3><a href="https://www.instagram.com/reel/{code}/" target="_blank">{fmt(r["views"])} views · {r["x_median"]}x his median · '
            f'{round(r["dur"])} s</a></h3><table class="bd"><tr><th>At</th><th>Sentence</th><th>Why it is there</th></tr>{body}</table>')


kp, _ = load("kallawaymarketing")
k_first = "".join(
    f'<tr><td>{fmt(r["views"])}</td><td>{r["x_median"]}x</td><td>{round(r["dur"]) if r["dur"] else ""} s</td>'
    f'<td>{E(first_words("kallawaymarketing", r["code"], 4.5)[6:])}</td></tr>' for r in kp["picks"])
skeleton = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in K_SKELETON)
sheets = "".join(f'<figure><img src="{sheet(h, c, k)}" loading="lazy"><figcaption>{E(cap)}</figcaption></figure>' for h, c, k, cap in SHEETS)
directions = "".join(
    f'<section class="card dir"><h3><span class="n">{n}</span> {E(t)} <small>{E(src)}</small></h3><p>{E(a)}</p><p class="why">{E(b)}</p></section>'
    for n, t, src, a, b in DIRECTIONS)
sfx = sorted(os.path.basename(f) for f in glob.glob(os.path.join(V2, "sfx", "named", "*.wav")))

page = f"""<!doctype html><meta charset="utf-8"><title>Reels study v2</title>
<style>
body{{font:15px/1.5 system-ui,sans-serif;background:#0f1115;color:#e6e8ec;max-width:1180px;margin:0 auto;padding:28px}}
h1{{font-size:26px;margin:0 0 4px}} h2{{font-size:20px;margin:38px 0 10px;border-bottom:1px solid #2a2f3a;padding-bottom:6px}}
h3{{font-size:16px;margin:0 0 6px}} small{{color:#8d95a5;font-weight:400}} a{{color:#8ab4ff}} p{{margin:6px 0}}
.card{{background:#171a21;border:1px solid #262b36;border-radius:10px;padding:16px;margin:12px 0}}
.reels{{display:flex;gap:10px;flex-wrap:wrap;margin-top:10px}}
.reel{{width:150px;color:#e6e8ec;text-decoration:none;font-size:13px}} .reel img{{width:150px;border-radius:6px;display:block;margin-bottom:4px}}
.reel span{{display:block;color:#8d95a5}} .reel em{{display:block;color:#b9c0cc;font-size:12px;line-height:1.35}}
table{{border-collapse:collapse;width:100%;margin:8px 0}} td,th{{border-bottom:1px solid #262b36;padding:6px 8px;text-align:left;vertical-align:top}}
th{{color:#8d95a5;font-weight:500}} .bd td:first-child{{white-space:nowrap;color:#8d95a5}} .bd td:nth-child(2){{width:48%}}
figure{{margin:14px 0}} figure img{{width:100%;border-radius:8px}} figcaption{{color:#b9c0cc;font-size:13px;margin-top:4px}}
.dir .n{{display:inline-block;background:#e0b33c;color:#111;border-radius:50%;width:24px;height:24px;text-align:center;line-height:24px;font-size:14px}}
.why{{color:#b9c0cc}} .note{{color:#8d95a5;font-size:13px}}
</style>
<h1>Reels study, second pass</h1>
<p class="note">The ten accounts you named, read on Instagram itself. Last 45 days only. Each reel is measured against its own account's median views.
The first pass (hashtag pages, faceless) is kept at <a href="shorts-study-v1.html">shorts-study-v1.html</a>.</p>

<h2>Where to take Paul's reels: five directions, in order</h2>
<p class="note">Nothing here is built. Every storm fact in these lines still has to come from an episode fact sheet.</p>
{directions}

<h2>The accounts, by median views per reel</h2>
<table><tr><th>Account</th><th>Followers</th><th>Reels in 45 days</th><th>Median views</th><th>Best reel</th></tr>{table}</table>
{''.join(cards)}

<h2>Kallaway: how one of his scripts is built</h2>
<p>18 of his reels from the last 45 days were transcribed: his 14 best and his 4 weakest that are at least 3 days old. Two are taken apart here line by line.</p>
{breakdown(*K1)}
{breakdown(*K2)}
<h3>The same skeleton, as a template</h3>
<table><tr><th>Where</th><th>Job</th><th>His words</th></tr>{skeleton}</table>
<h3>First line of all 18, best to worst</h3>
<table><tr><th>Views</th><th>vs median</th><th>Length</th><th>First words</th></tr>{k_first}</table>
<p>What this table shows: the first-line template does not separate his hits from his misses. “This is the number one social media strategy…” sits at 0.41x with the same
opening shape as his best. What changes is the subject and the frame-one picture. The top of the table is hooks, storytelling and tools he gives away; the bottom is
strategy talk, a sales pitch and a podcast clip that starts mid-thought. His reels are also long: the best one runs over two minutes.</p>

<h2>Frame one, from Kallaway and the others</h2>
{sheets}

<h2>Sound effects from subhangfx82</h2>
<p>{len(sfx)} sounds cut from four of his demo reels, one file per on-screen name, in <code>{E(os.path.join(V2, 'sfx', 'named'))}</code>:<br>
<span class="note">{E(', '.join(s[:-4] for s in sfx))}</span></p>
<p class="note">Cut where the on-screen name changes, so a tail of the next sound may be on some files. Not listened to. These are rips of a reel's audio; where he got the
sounds and whether they may be reused is not known. His actual pack is sent by DM to people who comment “SFX”.</p>

<h2>What is weak here</h2>
<ul>
<li>{E(VIEWED)}</li>
<li>Views are the numbers Instagram shows on the Reels tab, rounded by Instagram (907K, 1.2M).</li>
<li>Several of these accounts are weeks old (8, 10, 14 posts). A format that is new can fade as fast as it rose.</li>
<li>For charles.zhengg and factloree the 45-day list may be incomplete: the grid was read by scrolling and stops when no new reels load.</li>
<li>Only two Kallaway reels are taken apart line by line; the other 16 were read, not annotated.</li>
</ul>
"""
open(os.path.join(DEVQ, "shorts-study.html"), "w", encoding="utf-8").write(page)
print("accounts", len(cards), "| sheets", len(SHEETS), "| sfx", len(sfx), "| bytes", len(page))
