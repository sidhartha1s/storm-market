# Protection cross-reference audit

Map: 130 headings "### N · Title" found, none missing (1-130). Scope: every .md in ebook/manuscript/ (P0 through P8, README). Heading numbers treated as source of truth.

Count: about 540 numeric citations checked (regex count, includes a few non-protection numbers such as MMWR volume numbers); 10 mismatches found (9 high, 1 medium confidence, plus 3 watch items below).

| file:line | cited | sentence describes | protection actually titled | correct | conf |
|---|---|---|---|---|---|
| P1-C1-six-mechanisms.md:162 | 112 | leave-early trigger written before the season | 112 = The out-of-area contact | 95 (The trigger plan) | high |
| P1-C1-six-mechanisms.md:163 | 108 | two evacuation routes chosen when calm | 108 = The five-minute list and the thirty-minute list | 106 (Two routes out, driven) | high |
| P1-C1-six-mechanisms.md:164 | 116 | never entering moving water on foot or in a vehicle | 116 = Coming back | 115 (Driving in it; "never drive into water" is there) | medium |
| P2-C2-food.md:264 | 110 | pet food does not solve evacuation; carriers, records, animal-accepting places | 110 = Fuel discipline | 109 (Pets, planned properly) | high |
| P2-C2-food.md:262 | 111 | livestock and large animals covered elsewhere | 111 = Where you are going, specifically | none covers livestock (P4-C1:221 and P5-C3:122 say it is out of scope); nearest is 109 | medium |
| P2-C4-power.md:239 | 107 | half-tank fuel discipline | 107 = The go-bag, per person | 110 (Fuel discipline) | high |
| P3-02-hurricane-surge.md:165 | 41 | generator outdoors, CO ("Protections 32 and 41") | 41 = Small-scale solar | 47 (CO alarms) | high |
| P5-C3-evacuation.md:57 | 61 | go-bag medication supply | 61 = Dialysis, oxygen, infusion contingency | 59 (thirty-day prescription buffer) | high |
| P5-C3-evacuation.md:363 | 41 | generators and heaters run indoors kill people | 41 = Small-scale solar | 32 (Generator siting and CO clearance; 33 for heaters) | high |
| P5-C4-electronics-radiological.md:47 | 39, 45 | refrigeration and medical equipment power | 39 = Generator sizing/transfer switch; 45 = Refuel and recharge cadence | 15 (fridge) and 42 (medical device power) | medium |

Note: the last row is the weakest; 39 and 45 do supply power to those loads, so treat as a judgment call.

## Watch items (judged correct, listed for transparency)
- P1-C1:162 vs P5-C1:235: the P1-C1 line 162 is the same "Protection 112" for the trigger error as the already-fixed P5-C1 bug, so it is a second instance.
- P4-C1-people.md:156 cites 111 for the county voluntary assistance registry. 111 is "Where you are going"; P5-C3:174 discusses the registry in that chapter so left as OK.
- P2-C3:43 "See Protection 24" for manufactured homes: 24 body covers manufactured homes, OK.

## Checked and fine
All "- **N — title**" list items in the P3 hazard playbooks (P3-01 to P3-23), the P7 day-by-day list (every "(N)"), P6 trade checklist, P8 figure table, P0 front matter, and all other prose citations in P1, P2, P4, P5 matched their headings.

Method limit: matching is by reading each extracted sentence against the heading title; citations to a protection's body detail (not its title) were judged only where the title made a mismatch plausible.
