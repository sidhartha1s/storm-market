# homographs.md — heteronyms that change pronunciation by sense, weighted to this channel

**Why.** pocket-TTS (Kyutai) picks a pronunciation from spelling alone. A word whose sound
depends on meaning ("lives" as a plural noun vs. "lives" as a verb) can come out wrong, and a
wrong-sense homograph reads as AI slop to the audience (CLAUDE.md Voice). Measured 2026-09-27
on ep-enderlin (`learnings/audio-tts.md`): the TTS copy had respelled "lives" as "lyvz", which
voiced /ɪ/ (wrong); the PLAIN word "lives" measured correct (F1 769 Hz / 215 ms vowel = /aɪ/)
across all 9 re-recorded segments. **The blind respelling caused the defect — the plain word
was already right.** The rule this table exists to enforce: **never guess a respelling.**
Probe it with the TTS and measure (F1 onset, vowel length) or listen, then pick — a respelling
is picked by measurement, never by guess, and the default (unrespelled) reading is very often
already correct.

**Scope.** `scripts/homograph_scan.py` reads the **Scan = yes** rows of this table and reports
one line per flagged word (occurrence count + its first sentence) in an episode's narration
(`edit_script.md`). It never fails the render gate on its own (WARN level, matching how
`scripts/flag_words.py` treats a soft hit): whether a given occurrence actually needs a
respell depends on the sense in that sentence, a script cannot judge that, and hard-failing
every hit would block a render on lines that are already correct. The builder probes each
flagged word before the render and, only when the default reading is wrong, respells the TTS
copy phonetically while the script keeps the owner's exact wording (CLAUDE.md Voice).

**Scan column.** `yes` = this row is small enough in count and real enough in risk to be worth
a per-episode probe checklist; the gate builds a regex for every literal form listed and warns
on a match. `no` = a genuine heteronym, kept here for reference and for a human writing a
script, but not gated — most of these are rare in this niche or produce noise far out of
proportion to the risk (a chain-wide scan of every listed word warned 0-53 times per episode,
dominated by low-risk rows like "survey" and "house"; scanning only the ones known to actually
go wrong keeps the report short enough to read).

| Word(s) | Scan | Sense A | Sense B | Hint |
|---|---|---|---|---|
| read / reads | yes | present "read the report" /riːd/ | past "she read it" /rɛd/ | Tense-dependent; the owner's flagged trap ("I read all of them" = past). |
| lives | yes | noun, plural of "life": "lost their lives" /laɪvz/ | verb, 3rd person singular of "live": "he lives here" /lɪvz/ | The plain word is usually already correct (measured 2026-09-27, all 9 ep-enderlin segments); the risk is a blind respelling pushing it to the wrong sense, not the plain word itself. |
| live / lived / living | yes | adj./adv. "a live broadcast" /laɪv/ | verb, "I live here" / "we lived through it" /lɪv/ | Broadcast/adjective sense is common in disaster coverage narration; verb (reside) sense is the one to check. |
| lead / leads | yes | verb "lead the recovery" /liːd/ | metal noun "lead paint" /lɛd/ | Metal sense is rare here (flood debris, old paint); default is /liːd/. ("led", the ordinary past tense of "lead", is always /lɛd/ and is not itself ambiguous — not scanned.) |
| tear / tears | yes | verb "tear apart" /tɛr/ | noun "tears" (crying) /tɪr/ | Storm damage is /tɛr/; survivor emotion is /tɪr/. |
| close / closes / closed | yes | adj. "a close call" /kloʊs/ | verb "close the shelter" /kloʊz/ | Adjective vs. verb; check which one the sentence needs. |
| record / records | yes | noun "a record flood" /ˈrɛkərd/ | verb "record the interview" /rɪˈkɔːrd/ | Stress shift; noun front-stressed, verb back-stressed. |
| present / presents | yes | noun/adj. "present conditions" /ˈprɛzənt/ | verb "present the findings" /prɪˈzɛnt/ | Stress shift; check which the sentence needs. |
| wind / winds | yes | noun "the wind picked up" /wɪnd/ | verb "wind down" /waɪnd/ | Weather noun is almost always /wɪnd/; only the idiom needs the long-i verb form. |
| wound / wounds | yes | noun/verb, injury: "a gunshot wound" /wuːnd/ | past tense of "wind": "the road wound uphill" /waʊnd/ | Recovery-injury narration is the noun/verb sense; the past-tense-of-wind sense is rare here. |
| minute | no | noun "one minute" /ˈmɪnɪt/ | adj. "minute damage" /maɪˈnjuːt/ | Adjective sense (tiny) is rare; default is the time noun. |
| desert | no | verb "desert the town" /dɪˈzɜːrt/ | noun "the desert" /ˈdɛzərt/ | Evacuation sense is the verb; the landform is the noun. |
| row | no | noun "a row of houses" /roʊ/ | noun "a row broke out" /raʊ/ | Argument sense is rare/British; default is the line-of-things noun. |
| bow | no | verb "bow down" /baʊ/ | noun "bow and ribbon" /boʊ/ | Rare in this niche; check context if it appears. |
| object | no | noun "a flying object" /ˈɒbdʒɪkt/ | verb "object to the plan" /əbˈdʒɛkt/ | Debris/projectile sense is the noun, front-stressed. |
| content | no | adj. "content with the outcome" /kənˈtɛnt/ | noun "the content of the report" /ˈkɒntɛnt/ | Rare in narration; check before shipping if it appears. |
| produce | no | noun "farm produce" /ˈproʊduːs/ | verb "produce a report" /prəˈduːs/ | Noun sense almost never fits this channel; default is the verb. |
| refuse | no | noun "refuse and debris" /ˈrɛfjuːs/ | verb "refuse to leave" /rɪˈfjuːz/ | Debris sense is the noun, front-stressed; the verb is more common here. |
| invalid | no | adj. "an invalid claim" /ɪnˈvælɪd/ | noun "an invalid" /ˈɪnvəlɪd/ | Noun sense is dated and should be avoided in the script entirely. |
| moderate | no | adj. "a moderate risk" /ˈmɒdərət/ | verb "moderate the panel" /ˈmɒdəreɪt/ | SPC risk-category language is the adjective; verb sense is rare here. |
| estimate | no | noun "the estimate" /ˈɛstɪmət/ | verb "estimate the toll" /ˈɛstɪmeɪt/ | Final vowel differs (schwa vs. long a); check which the sentence needs. |
| separate | no | adj. "separate cells" /ˈsɛprət/ | verb "separate the debris" /ˈsɛpəreɪt/ | Adjective drops the middle vowel; verb keeps it. |
| project | no | noun "the recovery project" /ˈprɒdʒɛkt/ | verb "project the storm's path" /prəˈdʒɛkt/ | Forecast usage is the verb, back-stressed. |
| polish | no | verb "polish the script" /ˈpɒlɪʃ/ | adj. "Polish forecasters" /ˈpoʊlɪʃ/ | Capitalized nationality sense is rare here; check if it appears. |
| bass | no | noun "bass" (fish) /bæs/ | noun "bass" (low tone) /beɪs/ | Audio-mix sense (low tone) is the likelier one on this channel. |
| dove | no | noun "a dove" (bird) /dʌv/ | verb "the chaser dove for cover" /doʊv/ | Storm-chaser action is the verb (past tense of dive). |
| sow | no | verb "sow doubt" /soʊ/ | noun "a sow" (female pig) /saʊ/ | Figurative-speech sense is the verb; check before shipping. |
| use | no | noun "no use in waiting" /juːs/ | verb "use the shelter" /juːz/ | Noun voices the s unvoiced; verb voices it (z). |
| house | no | noun "the house" /haʊs/ | verb "house the survivors" /haʊz/ | Verb sense (shelter someone) voices the s (z); common in recovery narration. |
| excuse | no | noun "no excuse" /ɪkˈskjuːs/ | verb "excuse the delay" /ɪkˈskjuːz/ | Same s-voicing pattern as use/house. |
| survey | no | noun "the damage survey" /ˈsɜːrveɪ/ | verb "the NWS team surveys the damage" /sərˈveɪ/ | Frequent in this niche (NWS damage surveys), which is exactly why it is high-noise; keep as reference, not gated. |
| increase | no | noun "a sharp increase" /ˈɪŋkriːs/ | verb "wind speeds increase" /ɪnˈkriːs/ | Storm-intensity narration uses both; stress shift front vs. back. |
| decrease | no | noun "a steady decrease" /ˈdiːkriːs/ | verb "pressure decreases" /dɪˈkriːs/ | Same pattern as increase. |
