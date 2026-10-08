# packaging-rules.md — titles and thumbnails for a US 45–75 audience (audience audit 2026-09-14)

Source: `references/teardowns/2026-09-14-audience-audit/` (two senior personas, packaging designer, skeptic +
refutation, showrunner synthesis). Read with `yt-packaging` before any title or thumb is locked.

## Title
- Searchable Name + Year inside the first 40 characters; whole promise inside 52; nothing load-bearing after 60.
  Cutoffs (hypothesis, verify in Studio): TV grid ~40–60, phone home 45–55, desktop 55–70.
- The title states the episode's script concept (`script-os.md` rule 1), never the bare topic.
- A checkable fact beats an adjective: "Four EF5 Tornadoes in One Day" passed both seniors; superlative adjectives,
  ALL CAPS and "you won't believe" shapes did not.
- **Flesch reading ease 100 or more** (owner 23 Sep 26): one-syllable words, one clause per sentence, numbers as
  digits. `python3 scripts/title_fre.py "<title>" ...` prints the score; 85 to 99 is a rewrite, under 85 is out.
  "The 12-Year EF5 Drought Was a Lie" scores 114; "The Day America Had 7 F5 Tornadoes - 1974 Super Outbreak" scores 53.
- **Negative beats neutral beats positive** (1of10 media, 23 Sep 26: 11 % of titles are negative and they draw 22 % more
  median views). When brainstorming, list the anger, controversy, humour and joy shapes first; a true negative claim
  ("lie", "broken", "wrong", "nobody") beats a neutral description, as long as the film pays it in
  plain words: "I must have missed the part where everything we know is wrong" (159 likes) is the cost of a title the
  script only implies (`teardowns/2026-10-03-titanic-mirage.md`).
- Live minis keep present tense and the place ("Texas, This Winter…" got the best mini CTR at 8 %).

## Thumbnail: three schools, one rule
- **A · Name + Year documentary card** (archive photograph, heavy upright caps, place name in frame, one human-scale
  fact as text: "158 DEAD IN 32 MINUTES"). Use for historical documentaries (the banked four, Joplin, Tri-State).
  A cinematic AI shot is allowed here when it carries the place name and the fact: ep2 shipped an AI tornado with
  text and pulled 6.65 % CTR on 11k impressions (owner 2026-09-14). No BREAKING bar.
- **B · Agency photograph + 2–4 bold words** (NOAA/CPC map or SST globe, white first line, red payoff word, region +
  verdict; map and arrow allowed). Use for forecast explainers (El Niño series).
- **C · Live-wave news style** (map with 3–4 city labels, one red arrow, 2–4 word present-tense text, OUR bug "THE
  WARNING HOUR", never a network chyron). Use for live US minis. Ray: "A lie. I know what a chyron looks like."
- Every thumb carries a place name; no thumb ships with a spelling error (Krakatau #3 shipped "ERRUPTIONS").
- Series identity (10–15 El Niño videos): fixed type family, blue/amber palette, round "EL NIÑO 26-27" badge
  bottom-left; the variable is the state photograph + state name. Title spine `El Niño Winter 2026-27: <State>: <verdict>`.

## Paul on the thumbnail: three candidate systems (study 8 Oct 26; the owner has not picked one)
Owner 7 Oct 26: "i need a design system, not a one off show". Until he picks, the three schools above stay the rule and
none of these ships. Study: `references/teardowns/2026-10-08-thumbnails-13-channels/README.md`. Prompts with their
slots: `references/thumbnail-prompts.md`. Each system fixes everything except the slots, so every video looks like the last.
- **Field Notes**: cream graph paper (#F2EAD8); Paul on the right third, head and shoulders, navy jacket; headline top
  left in Anton caps, line 1 black, line 2 cream on a red brush box (#C8202A); one pencil diagram drawn from real data
  (track, timeline, map) with 2 or 3 hand-written labels; one red circle. From Critical Latitude's paper format. Risk:
  no storm in the frame, and the storm niche's biggest thumbnails are all storm.
- **Witness**: one real photograph full frame, graded darker; Paul cut out on the left third in the white linen shirt;
  year in white over place in red (#E3212B), Montserrat, upper right; one thin red ring on the object that gives scale.
  From Johnny Harris's host cut-out and the tornado documentaries' year-over-place type. Risk: a cut-out head over a
  photograph is the most common look on YouTube.
- **On the Ground**: Paul stands inside one real photograph, waist up in a lower corner, navy jacket, turned to the
  storm, looking back and pointing; headline top left in Anton white caps with a black outline; one red arrow from the
  headline to the storm; a small red place-and-year tag. From the AI avatar channels and HIGH RISK Chris's top video.
  Risk: an AI presenter inside a real disaster photograph reads fake when the blend is off; judge this one hardest by eye.
- All three: made in ChatGPT with two attached images that the prompt names. img1 is Paul's sheet
  `assets/paul/paul-sheet-v2.jpg`. img2 is a real photograph, frame or official map of the event, licence checked first
  (a CC BY photograph needs its credit in the description). Never a CSS mock-up, never the landing-page images, never
  an AI storm scene. Headline: 2 lines, never the title's words. One red mark. One outfit per system.
- Not solved: ChatGPT repainted the real photographs in the Witness and On the Ground demos (a clear Joplin sky came
  back as storm cloud). A published thumbnail needs Paul and the words laid over the untouched photograph; that step
  is not built. Field Notes has no photograph and does not have the problem.
- Not tested: a no-face version of the same video against the Paul version. The study's storm channels win without a host.

## What the Studio export says (2026-09-14)
YouTube tested every US-topic upload with 2–11k impressions; CTR decided the rest: 6.65 % kept going (ep2), 3.5 %
half-lived (Joplin), 1.8 % died (Tri-State). Krakatau never got a test (55–60 impressions). Packaging is the gate.

## Pre-publish checklist (the plumbing that was unshipped on ep2)
Description first URL = channel first_link; no placeholder text ("OWNER TO FILL" is a publish blocker); playlist set;
end screen pointing at the next video in the series; chapters; pinned comment; thumbnail spell-checked at 300 px.
