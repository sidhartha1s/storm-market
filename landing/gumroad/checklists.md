# Gumroad free product — `/l/checklists` (the printable pack)

**Owner action required (one-time, ~5 min):** create this product on Gumroad so every "Email me
the pack" button on `/resources/*` resolves. Until it exists those buttons 404 on Gumroad.

- **URL slug:** `checklists` → `https://paulraymond.gumroad.com/l/checklists`
- **Price:** $0 (or "$0+" to allow tips). Free product = Gumroad collects the email + adds the
  buyer to your Gumroad audience, same as `/l/packet`.
- **Name:** The Storm-Ready Home — The Printable Pack (7 checklists + 3 binder forms)
- **Cover image:** `landing/assets/cover-square.jpg` (reuse) or a 1:1 shot of `inside-binder.png`
- **Files to attach (build once):** one PDF containing the seven checklist pages printed from
  `/resources/*` (use each page's Print → Save as PDF; they are print-styled) + three binder forms
  from `ebook/binder/out/The-Storm-Ready-Home-Binder.pdf` (pick: household communication plan,
  home inventory, medication record).
- **Description (paste):**

> Seven working storm checklists, torn straight out of *The Storm-Ready Home* — the trigger plan,
> the tornado safe room, the go-bag, the emergency binder, the hurricane and tornado checklists,
> and the home inventory for insurance — laid out for the fridge door, plus three fillable forms
> from the manual's 61-page binder. Free. One email; unsubscribe any time.
>
> The book these came from carries all 130 numbered protections, 23 hazard playbooks, the 60-day
> sequence and the whole binder: https://paulraymond.online/#offer — $9.99, instant PDF, 7-day
> money-back guarantee.

- **After creating:** run `node gumroad/pagecheck.mjs https://paulraymond.gumroad.com/l/checklists product`
  and click one "Email me the pack" button on the live site.
- **Follow-up email (Gumroad → Emails → Workflow, trigger: purchase of `checklists`):** day 0 =
  the pack + one line about the book; day 3 = the Joplin dispatch link; day 7 = the $9.99 offer.
