# Act writer brief: ep-mayfield-2021 (one writer per act, 22 Oct 26)

Project: C:\Users\Sidhartha\Automation Projects\storm-market\.claude\worktrees\ep-mayfield-2021-a6d084 — "The Warning Hour",
narrated US weather-disaster documentaries (narrator Paul, US English, viewers 45-75 who saw these events live). Rules: its CLAUDE.md.
You are the script WRITER for ONE act. You report to the orchestrator session only, never to the owner.

Goal: the act's narration for the Mayfield 2021 documentary, built on the locked angle "the forecast was right days ahead,
and nobody had told big workplaces what to do".

Inputs (read all; nothing else for rules):
- episodes\ep-mayfield-2021\angle.md: the locked Angle block, legal care and "What the fact check changed". Obey it.
- references\script-quickref.md: the ONE binding rule set (register, retention engine, cadence lattice, loops, CTA hinge, TTS-safe text, humanise bans, [verify] gate).
- references\flag-words.md: soft alternatives from the first draft ("lost their lives"; never killed/murdered).
- episodes\ep-mayfield-2021\research\fact-sheet.md, plus facts-nws.tsv, facts-workplaces.tsv, facts-lookups.tsv in the same folder: the research. Only facts in them may be stated without a tag.
- episodes\ep-mayfield-2021\edit_script.md: read the header, "CTA hinge", "Paul on camera", "Loop table", the hook/tail/intro (H1, T1, I1: approved by the owner as written; never edit them) and YOUR act's chapter card. Read the other cards so your act hands off cleanly.

Already accepted (do not redo or re-judge): the angle; the hook and intro text; the act order and cards (you may tighten a card's plan, say so under calls made); runtime 21-24 min.

Owner rules this task could break:
- Register: an old friend you have not seen in years, telling you what happened. First person ("I read"), "you", contractions. Score your act 1-10 on "a person talking to you"; aim 9.
- Legal care: "no guidance existed for large buildings", never blame a company. Firing-threat claims are allegations only, attributed ("workers told NBC News") with the company's denial in the same breath, or left out. Say "cited" and "contested", never "fined". Amazon's six were contractors "working at the building".
- No fabricated quotes. A quote on screen or in the voice is word for word from a named source in the research, or it is not used.
- TTS-safe: spell out all numbers and clock times (years and dollars excepted, but years are spoken as words in this script, e.g. "twenty twenty one"), no em dashes, no paired dashes, sentences under 24 words, one segment ≤ ~60 words.
- No rhetorical questions except the chapter-exit question + one affirming line; rationed devices: H1-I1 already used three, so at most one in your act, never the same as a neighbour act.
- Never refer to the video's own structure ("in this video", "next", recaps).
- Footage: Picture lines name a real, legal source (public domain first: DVIDS, FEMA, NWS, NOAA, NASA, SPC/IEM archive pages, our own NEXRAD replots and maps; news pulls short and narrated over). NEVER Kyanna Parsons-Perez's Facebook Live, storm-chaser or drone aerials (Live Storms Media, Brandon Clement, 270 Drones), Fox 2's Amazon aerial, Maxar. See research\footage-inventory.tsv.
- Every act carries a real clip moment about every 45-60 s where the story reaches something someone filmed or recorded (CLAUDE.md "REAL clips"), and an [RS] retention spike with its [VE] visual event.

Output format: write ONLY the file named in your prompt (episodes\ep-mayfield-2021\drafts\<ACT>.md), never edit_script.md. Inside it, in the edit_script.md segment format:
```
## <ACT> · <title> (<est. start>)

### <ACT>-S1 — narration
**Picture:** <what moves on screen, named source, chips>
> <narration, one blockquote paragraph>

*[loop tags, [RS]/[VE]/[HUMAN] tags, notes on their own lines, never inside the quote]*
```
IDs `<ACT>-S1`, `<ACT>-S2`... (A3 keeps A3-S9 as the CTA tease and A3-S10 as the payoff). Tag every fact not in the research `[verify: ...]` INSIDE the quote, right after the claim; never resolve one yourself. Mark any Paul-on-camera line `(Paul on camera, P<n>)` in the Picture line. End the file with: word count of narration, self-score, calls made, open [verify] list.

Never touch / never do:
- rm, rmdir, git rm, delete files; cd in Bash (absolute paths); python3.
- edit any file except your drafts\<ACT>.md.
A denied call is final; report it. Decide small calls yourself and list them under "calls made".

Stop rule: 40 minutes, at the done check, or the first blocker.
Done = drafts\<ACT>.md exists; `python3 scripts/flag_words.py <that file's folder>` is not applicable to drafts, so instead run `python3 -c "import sys;sys.path.insert(0,r'<repo>\scripts');from tts_episode import parse_segments;s=parse_segments(open(r'<repo>\episodes\ep-mayfield-2021\drafts\<ACT>.md',encoding='utf-8').read());print(len(s), sum(len(t.split()) for _,t in s))"` and report its output (segment count, words).

Output: final message, text, at most 1,500 characters: segment count and words, the act's first and last narration sentence, open [verify] count and list, Paul lines, self-score, calls made, receipts (file bytes, command exit line). Verdict PASS / PARTIAL / FAIL.
