# homographs.md — heteronyms that change pronunciation by sense, weighted to this channel

**Why.** pocket-TTS (Kyutai) picks a pronunciation from spelling alone. A word whose sound
depends on meaning ("lives" as a plural noun vs. "lives" as a verb) can come out wrong even
when the script's wording is exactly right, and a wrong-tense or wrong-sense homograph reads
as AI slop to the audience (CLAUDE.md Voice). Measured 2026-09-28: pocket-TTS said "lives" (as
in "lost their lives") as /lɪvz/; an earlier respelling "lyvz" also produced /ɪ/. Plain "lives"
on its own measured F1 769 Hz / 215 ms vowel = /aɪ/, the correct sound. The rule this table
exists to enforce: **never guess a respelling.** Probe it with the TTS and measure (F1 onset,
vowel length) or listen, then pick — a respelling is picked by measurement, never by guess.

**Scope.** `scripts/homograph_scan.py` reads this table and reports every occurrence in an
episode's narration (`edit_script.md`) with the sentence it sits in. It never fails the
render gate on its own (WARN level, matching how `scripts/flag_words.py` treats a soft hit):
whether a given occurrence actually needs a respell depends on the sense in that sentence, a
script cannot judge that, and hard-failing every hit would block a render on lines that are
already correct. The builder probes each reported occurrence before the render and, only when
the default reading is wrong, respells the TTS copy phonetically while the script keeps the
owner's exact wording (CLAUDE.md Voice).

| Word(s) | Sense A | Sense B | Hint |
|---|---|---|---|
| live | adj./adv. "a live broadcast" /laɪv/ | verb, present tense "I live here" /lɪv/ | Broadcast/adjective sense is common in disaster coverage narration; verb (reside) sense is the one to check. |
| lives | noun, plural of "life": "lost their lives" /laɪvz/ | verb, 3rd person singular of "live": "he lives here" /lɪvz/ | The exact trap measured on this channel 2026-09-28: pocket-TTS said "lives" in "lost their lives" as /lɪvz/ (wrong); plain "lives" on its own measured correct (F1 769 Hz, 215 ms vowel = /aɪ/). Never respell blind, probe and measure first. |
| wind / winds / wound | noun "the wind picked up" /wɪnd/ | verb "wind down", past "wound up" /waʊnd/ | Weather noun is almost always /wɪnd/; only the idiom needs the long-i verb form. |
| lead / led | verb "lead the recovery" /liːd/ | metal "lead paint" /lɛd/ | Metal sense is rare here (flood debris, old paint); default is /liːd/. |
| tear / tears | verb "tear apart" /tɛr/ | noun "tears" (crying) /tɪr/ | Storm damage is /tɛr/; survivor emotion is /tɪr/. |
| close | adj. "a close call" /kloʊs/ | verb "close the shelter" /kloʊz/ | Adjective vs. verb; check which one the sentence needs. |
| minute | noun "one minute" /ˈmɪnɪt/ | adj. "minute damage" /maɪˈnjuːt/ | Adjective sense (tiny) is rare; default is the time noun. |
| record | noun "a record flood" /ˈrɛkərd/ | verb "record the interview" /rɪˈkɔːrd/ | Stress shift; noun front-stressed, verb back-stressed. |
| desert | verb "desert the town" /dɪˈzɜːrt/ | noun "the desert" /ˈdɛzərt/ | Evacuation sense is the verb; the landform is the noun. |
| row | noun "a row of houses" /roʊ/ | noun "a row broke out" /raʊ/ | Argument sense is rare/British; default is the line-of-things noun. |
| bow | verb "bow down" /baʊ/ | noun "bow and ribbon" /boʊ/ | Rare in this niche; check context if it appears. |
| read | present "read the report" /riːd/ | past "she read it" /rɛd/ | Tense-dependent; the owner's flagged trap ("I read all of them" = past). |
| object | noun "a flying object" /ˈɒbdʒɪkt/ | verb "object to the plan" /əbˈdʒɛkt/ | Debris/projectile sense is the noun, front-stressed. |
| present | noun/adj. "present conditions" /ˈprɛzənt/ | verb "present the findings" /prɪˈzɛnt/ | Stress shift; check which the sentence needs. |
| content | adj. "content with the outcome" /kənˈtɛnt/ | noun "the content of the report" /ˈkɒntɛnt/ | Rare in narration; check before shipping if it appears. |
| produce | noun "farm produce" /ˈproʊduːs/ | verb "produce a report" /prəˈduːs/ | Noun sense almost never fits this channel; default is the verb. |
| refuse | noun "refuse and debris" /ˈrɛfjuːs/ | verb "refuse to leave" /rɪˈfjuːz/ | Debris sense is the noun, front-stressed; the verb is more common here. |
| invalid | adj. "an invalid claim" /ɪnˈvælɪd/ | noun "an invalid" /ˈɪnvəlɪd/ | Noun sense is dated and should be avoided in the script entirely. |
| moderate | adj. "a moderate risk" /ˈmɒdərət/ | verb "moderate the panel" /ˈmɒdəreɪt/ | SPC risk-category language is the adjective; verb sense is rare here. |
| estimate | noun "the estimate" /ˈɛstɪmət/ | verb "estimate the toll" /ˈɛstɪmeɪt/ | Final vowel differs (schwa vs. long a); check which the sentence needs. |
| separate | adj. "separate cells" /ˈsɛprət/ | verb "separate the debris" /ˈsɛpəreɪt/ | Adjective drops the middle vowel; verb keeps it. |
| project | noun "the recovery project" /ˈprɒdʒɛkt/ | verb "project the storm's path" /prəˈdʒɛkt/ | Forecast usage is the verb, back-stressed. |
| polish | verb "polish the script" /ˈpɒlɪʃ/ | adj. "Polish forecasters" /ˈpoʊlɪʃ/ | Capitalized nationality sense is rare here; check if it appears. |
| bass | noun "bass" (fish) /bæs/ | noun "bass" (low tone) /beɪs/ | Audio-mix sense (low tone) is the likelier one on this channel. |
| dove | noun "a dove" (bird) /dʌv/ | verb "the chaser dove for cover" /doʊv/ | Storm-chaser action is the verb (past tense of dive). |
| sow | verb "sow doubt" /soʊ/ | noun "a sow" (female pig) /saʊ/ | Figurative-speech sense is the verb; check before shipping. |
| use | noun "no use in waiting" /juːs/ | verb "use the shelter" /juːz/ | Noun voices the s unvoiced; verb voices it (z). |
| house | noun "the house" /haʊs/ | verb "house the survivors" /haʊz/ | Verb sense (shelter someone) voices the s (z); common in recovery narration. |
| excuse | noun "no excuse" /ɪkˈskjuːs/ | verb "excuse the delay" /ɪkˈskjuːz/ | Same s-voicing pattern as use/house. |
| survey | noun "the damage survey" /ˈsɜːrveɪ/ | verb "the NWS team surveys the damage" /sərˈveɪ/ | Frequent in this niche (NWS damage surveys); stress shift noun vs. verb. |
| increase | noun "a sharp increase" /ˈɪŋkriːs/ | verb "wind speeds increase" /ɪnˈkriːs/ | Storm-intensity narration uses both; stress shift front vs. back. |
| decrease | noun "a steady decrease" /ˈdiːkriːs/ | verb "pressure decreases" /dɪˈkriːs/ | Same pattern as increase. |
