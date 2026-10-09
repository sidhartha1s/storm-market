# angle.md: the angle is locked before anything else (owner 9 Oct 26)

Owner, 9 Oct 26, on a plan that offered one angle with its title, thumbnail and hook already built:

> It's not the subject. It's the angle which matters. Then, once that is locked, only then and then you will get the hook, the title, the thumbnail, everything else.

"Make a purple cow effect." And: "Without a amazing angle or an amazing video, no matter the thumbnail or the motion graphics or the cuts or the quality of whatever we are doing won't matter." And: "we are only doing the legitimate thing. So we are not fluffing anything for the sake of views."

This file is the one home of that rule. `CLAUDE.md`, the episode skills, `references/script-quickref.md` and `references/packaging-rules.md` point here.

## Subject and angle
- The **subject** is the event: El Reno 2013.
- The **angle** is one true claim that changes what a viewer who already knows the event believes about it. It has the shape "it wasn't X, it was Y".
- The fact every video on the subject already leads with is not an angle. It is the subject's default line, and it is ruled out as the lead.

## Order of work (documentaries and minis)
Owner 9 Oct 26, asked whether minis follow the rule: "yes minis too." A mini's lock is `episodes/ms-<slug>/angle.md`, and its skill has the gate as step 0.

Angle first. Then structure, then title and thumbnail, then the hook that pays them (`references/script-quickref.md` "The hook"), then the script. His sentence lists hook, title and thumbnail as what follows the lock; it does not order them. No title, thumbnail, hook or script line is written before the owner locks the angle. Work done earlier is thrown away, not adapted.

## How the candidates are found
1. **Rule out the default.** From the teardowns of the top videos on the subject, write down what each one leads with. Those leads are the list of angles we do not take.
2. **Mine the primary sources** (service assessments, survey papers, fatality tables, hearing records) for facts no retelling leads with. Count things the sources only list.
3. **Write at least four candidates.** Each is one sentence a viewer could repeat, with its source and what is still unverified.
4. **Test each one:**
   - Would a viewer who watched the top three videos on the subject still learn this? If not, drop it.
   - Can you name at least three acts it needs? An angle that fills one act is a segment, not an angle.
   - Does the primary source say it, in full, without stretching? If the claim needs a softened word to stay true, write the softened version or drop it.
   - Can the footage and graphics we may legally use carry it?
5. **Show the owner all candidates with one recommendation and the reason.** Never one angle alone. Candidates may be combined: one as the spine, others as arcs inside it.

## The lock (OWNER GATE)
The owner's words lock the angle. Silence, or approval of something built on it, is not a lock. The lock is recorded in `episodes/<slug>/angle.md`, written the moment he locks it. That file existing is the lock:

```
## Angle (locked by the owner, <DD Mon YY>: "<his words>")
Claim: <one sentence>
Spine / arcs: <which candidate carries the video, which sit inside it>
Source: <document, section or table>
Ruled out as the lead: <what the top videos lead with>
Still unverified: <list, or none>
```

A writer's brief carries this block, pasted from that file. A brief without it is not ready.

A fact check may tighten the Claim's wording: whoever ran the check updates the file and tells the owner what moved. A changed meaning needs a new lock.

## Worked example: El Reno 2013 (locked 9 Oct 26)
- His locking words, on a list of four candidates: "Do a mix of number one and number five. And eventually number two will also be included there. Like as a small arc or something like that." The list had four, so "five" was read as candidate four, the two vehicles: the agent's reading. The review page he answered next stated it back ("Angle locked by you: nobody lost their life indoors. Two crews in the middle. The tornado inside the tornado as the science."); on that page he ticked the hook and the title and wrote, on starting the script, "go ahead will share 2nd omni later." He has not restated the mix in his own words. The lock is `episodes/ep4-el-reno/angle.md` on the episode's branch.
- Ruled out: "radar near 300 mph, rated EF3" and "the widest tornado ever recorded". Every top video leads with one of them.
- Locked: all 21 people who lost their lives on the night of May 31 were in a vehicle or sheltering in a drainage ditch, none in a building (NWS Service Assessment, Appendix C, counted row by row). Two vehicles inside the same tornado minutes apart, one crew surviving and one not, carry the middle; the small fast vortices inside the wide one are the science arc that explains them.
- What the fact check changed after the lock: the two vehicles were on different roads, and the count holds for that night only (one more flood death the next morning is outside the table). Both were wording, not meaning, so the lock stood and he was told.
