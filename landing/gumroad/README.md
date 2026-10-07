# Gumroad surfaces — custom product landing page + storefront profile

Two hand-authored pages published to Gumroad with the `gumroad` CLI. They carry the same
field-manual identity as `landing/index.html` (the Cloudflare Pages funnel), so a buyer who
crosses from `paulraymond.pages.dev` to Gumroad never sees a design seam.

| File | Publishes to | What it is |
|---|---|---|
| `landing.html` | `https://paulraymond.gumroad.com/l/ebook` | **Replaces the entire native product page**, price and "I want this!" button included. |
| `profile.html` | `https://paulraymond.gumroad.com/` | The storefront home page — author masthead, the book, how it's made. |
| `pagecheck.mjs` | — | **Gate.** Loads a published URL in headless Chrome and asserts the custom HTML actually rendered. |

## The funnel

```
paulraymond.pages.dev  ──[Get My Copy]────────►  gumroad.com/l/ebook?wanted=true  ──►  checkout
          │                                                 ▲
          └──[Send My State Packet — Free]──►  /l/packet     │      ($0, all 51 packets in one zip)
                                                             │
              gumroad.com/  ──[Read what's inside]───────────┘
```

`/l/packet` is why this project has no backend. The free packets used to go through a Cloudflare
Pages Function into Kit; it 500'd on every real submit because its API key never existed. Gumroad
already does email capture and delivery, so the lead magnet became a $0 product and the function
was deleted. See `landing/README.md` § "No mail provider, deliberately".

`landing/index.html` sets `GUMROAD_URL` and rewrites the offer button + exit-intent popup to
`?wanted=true`, which opens Gumroad's checkout directly rather than the product page. Verify
that path with `node landing/buycheck.mjs` — it reads the button's *resolved* href in a real
browser, which is the only check that fails when the money path breaks.

## Publishing

```bash
PRODUCT=cYjHuPgp7BYJuqTbibM1tA==     # `gumroad products list --json` → .products[].id

# ALWAYS preview first — this runs the real server-side sanitizer without publishing.
gumroad products page preview $PRODUCT ./landing.html --json --no-input --non-interactive
gumroad pages preview ./profile.html  --json --no-input --non-interactive
#   → .sanitization_report must be {removed_tags: [], removed_attributes: [], total_removed: 0}
#   → .warning must be null. "no buy element" there means the product becomes unpurchasable.

gumroad products page publish $PRODUCT ./landing.html --json --no-input --non-interactive
gumroad pages push profile ./profile.html --json --no-input --non-interactive

node pagecheck.mjs https://paulraymond.gumroad.com/l/ebook   # must exit 0
```

Roll back to Gumroad's default product page with
`gumroad products page clear $PRODUCT --yes --json --no-input --non-interactive`.

## Two constraints that shape these files

1. **Images may only come from the Gumroad media library.** Every other host is blocked, and
   files from `gumroad files upload` are private and fail page moderation. Upload with
   `gumroad media upload ./assets/<name>.jpg` and paste the returned
   `public-files.gumroad.com/...` URL into the HTML. Current uploads:

   | Asset | URL |
   |---|---|
   | cover.jpg | `https://public-files.gumroad.com/2zwvwohyrk5s6bfcwhguofdnae4y` |
   | paul-tornado-selfie.jpg | `https://public-files.gumroad.com/c0p9i90w0cfsstukjcfgx3ydjiru` |
   | paul-plywood.jpg | `https://public-files.gumroad.com/5wqgovjx42ub2wuiftjzp6x9kzib` |
   | paul-binder.jpg | `https://public-files.gumroad.com/yje8sd8i8o2vjsx8enuzwb3zu84o` |
   | paul-stage.jpg | `https://public-files.gumroad.com/ljt6m4oky07sr5pfwjhtdmdt2lj0` |
   | field-kit.jpg | `https://public-files.gumroad.com/lnoi087hti6pgxds415fp1qp835b` |
   | avatar.jpg (profile masthead) | `https://public-files.gumroad.com/r3cx5p1zrtzn27kolqhitw0ha0jn` |

   `avatar.jpg` is a square crop of `headshot.jpg`, generated with Pillow — see the command in
   the git history for this file. It is committed rather than left as a one-off so the masthead
   image stays regenerable if the cover art ever changes.

2. **A custom product page replaces the native buy button**, so `landing.html` must carry its
   own. Every CTA is `data-gumroad-action="buy"`; live values use
   `data-gumroad-field="name|price"`. **`rating` and `review-count` are deliberately absent**
   — with zero reviews they render "Be the first to rate it · no reviews yet" directly beneath
   the testimonials, which reads as Gumroad contradicting them. The markup to restore them sits
   commented in `landing.html` at the end of the reviews section; put it back once reviews exist.

## Why pagecheck.mjs exists rather than a curl

Gumroad serves the product page as a React shell and mounts the custom HTML in a
**cross-origin sandboxed iframe**. `curl` sees none of it, and neither does a script that walks
`iframe.contentDocument` from the parent — that is `null` by design. `pagecheck.mjs` uses CDP
`Target.setAutoAttach` to get a session per out-of-process frame and reads each one. Both
failure modes were hit while building this; the checker is the record of that.

Screenshots have a third trap. A full-page capture of the parent yields only the fold (the
parent's `scrollHeight` is just its viewport), forcing a tall viewport makes the host app paint
**blank white**, and capturing the frame's own session is refused outright — CDP answers
`Command can only be executed on top-level targets`. What works: read the frame's `location.href`
(a real route, `…/l/<permalink>/landing/embed`) and load *that* as a top-level page. The custom
HTML carries its own `<style>`, so it renders standalone exactly as it does embedded.
`VIEW_W` sets the capture width for responsive checks.

## Not doable from the CLI

The **profile picture / avatar** is dashboard-only — `gumroad user update` exposes `--name` and
`--bio` and nothing else. Set it at gumroad.com/settings/profile. Everything else here
(seller name, bio, both pages, media) is scripted above.
