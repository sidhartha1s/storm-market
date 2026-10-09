# flag-words.md — violence/death vocabulary that trips YouTube's transcript scan

**Why.** YouTube's automated caption/transcript scan appears to down-rank videos that use
violent or death-heavy language, even in a factual disaster documentary — and a down-ranked
upload never gets the early seed-audience push it needs to find its real audience. This table
exists so a script never has to relearn that lesson per episode.

**Scope.** The whole narration script, every piece of on-screen text (lower-thirds, popfigs,
chapter cards, titles inside `compositions/*.html`), and the video's own title/description in
`metadata.md`. A word banned in narration is banned on screen too — a caption pass does not
launder a word the voice track was not allowed to say.

**Severity.** `hard` = never use it, anywhere, no exception — gate `scripts/flag_words.py`
fails the build. `soft` = the word is not banned outright (it is often the plainest, most
factual choice, or genuinely hard to avoid in a disaster documentary), but the alternative
is the default (owner 9 Oct 26: YouTube flags these words and can suppress the video) and reads better in TTS narration; the gate warns, does not fail.

**Inflections.** The gate matches every listed term plus its plain English suffixes
(s/es/d/ed/ing) automatically — "kill" also catches "kills" and "killing" without a separate
row. A word whose inflection isn't plain concatenation (bloody -> bloodied, terror -> terrorized)
is listed as its own extra form in that row instead of being left to the suffix rule.

**Quotes.** A real quote from an NWS Service Assessment, a NIST report, a news archive or a
survivor that contains a flagged word gets paraphrased ("the report called it the deadliest
tornado on record" instead of quoting the flagged word verbatim) — never fabricate a cleaner
quote that was not actually said.

| Term(s) | Severity | Alternatives | Reason |
|---|---|---|---|
| kill / killed / killing / killer | hard | lost their lives; did not survive; the storm claimed [n] lives | The single highest-risk word in the niche; always has a plain alternative. |
| murder | hard | took the life of; was responsible for the death of | Never accurate for a weather event; if it appears it is almost always a wrong word choice. |
| suicide | hard | took his/her own life; did not survive the aftermath | Sensitive-topic term regardless of algorithm risk; paraphrase the fact instead of naming the act. |
| massacre | hard | the deadliest day on record; the worst-hit town | Sensational, implies intent a storm does not have. |
| slaughter | hard | wiped out; destroyed | Only shows up as a lazy metaphor (crops, livestock); the plain verb says the same thing. |
| carnage | hard | the destruction; the wreckage | Tabloid word, no factual content of its own. |
| bloodbath | hard | the worst losses on record; a sharp, sudden decline | Metaphor only (markets, damage totals); reads as sensational, not informative. |
| blood / bloody / bloodied | hard | seriously injured; hurt badly | Literal injury detail we do not need to name the scene. |
| gore / gruesome | hard | difficult to look at; the kind of scene rescuers do not forget | Descriptive intensifier, not a fact; also a "narrator adjective" the humanise rules already discourage. |
| mutilated | hard | severely injured | Graphic beyond what the story needs. |
| decapitated | hard | suffered a fatal head injury | Paraphrase to the plain fact of a fatal injury; the anatomical detail adds nothing. |
| crushed to death | hard | was pinned and did not survive; did not survive being trapped under debris | Names the mechanism without the algorithm-risk verb. |
| burned alive | hard | did not escape the flames; was overtaken by the fire before help arrived | Same fact, no "alive" pairing with a violent verb. |
| bomb / explode | hard | hit with sudden, overwhelming force; tore through in an instant; leveled the block in seconds | Almost always a lazy simile for storm force in this niche, not a literal event; the literal force is easy to describe directly. |
| explosion | soft | (as above, when it IS a simile) hit with sudden force; tore through in an instant | Literal event word OK; never as a simile. A volcanic explosion (ms-krakatau) or a sourced quote naming one is a real, citable event, not a metaphor for storm force. |
| war zone | hard | looked unrecognizable; resembled a demolition site | Cliché comparison, also banned by humanise-rules' "no borrowed metaphors". |
| shooting | hard | filming; recording | Rare in this niche outside "storm chasers were filming" — say "filming", not "shooting", and the ambiguity never comes up. |
| gun | hard | (no legitimate use in this niche) | No weather-documentary sentence needs this word; if it appears, rewrite the sentence. |
| horror / horrific | hard | photographs show [specific detail]; witnesses described [specific, sourced detail] | Narrator adjective already banned by CLAUDE.md ("fear only as a sourced fact"); doubles as an algorithm risk. |
| terror / terrifying / terrorized | hard | survivors described [specific detail] | Same as above — replace the adjective with the sourced specific it is standing in for. "Terrorized" is not a plain suffix of "terror" (-ize infix), so it is its own listed form, not left to the suffix rule. |
| nightmare | hard | the worst hour of their lives; [specific, literal detail] | Cliché metaphor, already covered by humanise-rules' banned-metaphor list. |
| apocalypse / apocalyptic | hard | the scale of the destruction; the extent of the damage | Hyperbole with no factual content. |
| doom / doomed | hard | the outlook worsened; the odds turned against them | Sensational framing; the underlying fact is usually a plain probability or forecast statement. |
| execute | soft | carried out; put into action | Ambiguous word (business sense vs. violent sense); the plain verb removes the ambiguity outright. |
| destroy / destroyed | soft | leveled; reduced to rubble; wiped out | Plain, factual, and usually the right word — vary it for rhythm, not for risk. |
| dead | soft | did not survive; lost their lives | Owner 9 Oct 26: soft wording is the default; the plain word stays only where precision needs it. |
| death / deaths | soft | the toll; the lives lost | Owner 9 Oct 26: the alternative is the default. The plain noun may stay where a sourced count needs it, never sentence after sentence. |
| death toll | soft | the number who did not survive; the toll | Owner 9 Oct 26: the alternative is the default; the plain phrase only for a sourced count. |
| died | soft | lost their lives; did not survive | Owner 9 Oct 26: "use it in a soft way because YouTube flags those and can suppress it. Maybe something like lost life." Write the alternative by default. The plain word may stay once or twice where a count needs it, never stacked. |
| body / bodies | soft | remains; those who did not survive | Necessary in recovery-effort narration; keep it factual, avoid stacking with other hard terms in the same sentence. |
| corpse | hard | the remains; the person who did not survive | More clinical/graphic than "body" with no added information — always replaceable. |
| drowned | soft | did not survive the rising water; was lost to the floodwaters | Plain cause-of-death term, necessary for flood and storm-surge episodes (Katrina); vary it, do not chase it out. |
| casualties | soft | the toll; people affected | Official NWS/NIST report language; safe but clinical — prefer a human-scale phrase when the sentence allows it. |
| fatal / fatalities | soft | did not survive; claimed [n] lives | Official/clinical register; fine in a sourced-report sentence, vary elsewhere. |
| victims | soft | those who lost their lives; survivors and their families | Hard to avoid entirely (especially "victims' families"); name individuals per script-os rule 12 instead of repeating this word. |

## On-screen text rule
Every row above applies identically to on-screen text: lower-thirds, popfigs, chapter cards,
titles, and any text baked into a `compositions/*.html` graphic. A word that would fail
narration fails a graphic caption too.
