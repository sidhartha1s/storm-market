// Cloudflare Pages Function — POST /api/subscribe
//
// Takes an email + two-letter state code from the free-state-packet form and forwards the
// subscriber to Kit (api.kit.com, formerly ConvertKit) — see landing/README.md "Mail provider"
// for why Kit was picked. This function never sends the packet itself; it only adds the person
// to the list with their state recorded as a custom field. Actually delivering the right packet
// is a Kit automation the owner builds in the dashboard, keyed off that field.
//
// Required environment variable: KIT_API_KEY (Pages project → Settings → Environment variables).
// Missing/empty KIT_API_KEY is a hard failure (500), never a silent success — see the
// "fails loudly" check below.

const VALID_STATES = new Set([
  "AL","AK","AZ","AR","CA","CO","CT","DE","DC","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA",
  "ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR",
  "PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY",
]);

// RFC-5322-ish, deliberately not exhaustive — good enough to reject typos and junk without
// rejecting real addresses.
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

// Same-IP throttle. Fixed window, per isolate. This is best-effort, not a distributed guarantee —
// a Cloudflare Worker/Pages Function can run in many isolates at once at the edge, and each one
// keeps its own Map. That's still a real, working throttle against a single abusive client hitting
// a single edge location, which is what an open form on a static page needs day one.
//
// [FALLBACK] If the Pages project later binds a Cloudflare Rate Limiting binding named
// SUBSCRIBE_RATE_LIMIT (declarative, in wrangler.toml — see README), that binding is used instead
// and gives a real cross-isolate limit. Every request that runs on the in-memory path logs a
// [FALLBACK] line so the gap is visible, not silent.
const RATE_LIMIT_WINDOW_MS = 10 * 60 * 1000; // 10 minutes
const RATE_LIMIT_MAX = 5; // requests per IP per window
const ipHits = new Map();

function inMemoryRateLimit(ip) {
  console.log("[FALLBACK] SUBSCRIBE_RATE_LIMIT binding not configured — using in-memory per-isolate throttle.");
  const now = Date.now();
  const entry = ipHits.get(ip);
  if (!entry || now > entry.resetAt) {
    ipHits.set(ip, { count: 1, resetAt: now + RATE_LIMIT_WINDOW_MS });
    return true;
  }
  if (entry.count >= RATE_LIMIT_MAX) return false;
  entry.count += 1;
  return true;
}

async function isAllowed(ip, env) {
  if (env.SUBSCRIBE_RATE_LIMIT && typeof env.SUBSCRIBE_RATE_LIMIT.limit === "function") {
    const { success } = await env.SUBSCRIBE_RATE_LIMIT.limit({ key: ip });
    return success;
  }
  return inMemoryRateLimit(ip);
}

function json(body, status) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "content-type": "application/json; charset=utf-8" },
  });
}

// Never put the full address in a log line.
function maskEmail(email) {
  const at = email.indexOf("@");
  if (at <= 1) return "***";
  return `${email.slice(0, 2)}***${email.slice(at)}`;
}

async function readFields(request) {
  const contentType = request.headers.get("content-type") || "";
  if (contentType.includes("application/json")) {
    const body = await request.json().catch(() => ({}));
    return { email: body.email, state: body.state };
  }
  // Native <form method=post> without JS falls back to this — same endpoint, same validation.
  const form = await request.formData().catch(() => null);
  if (!form) return { email: undefined, state: undefined };
  return { email: form.get("email"), state: form.get("state") };
}

export async function onRequestPost(context) {
  const { request, env } = context;

  const ip = request.headers.get("cf-connecting-ip") || "unknown";
  if (!(await isAllowed(ip, env))) {
    return json({ error: "Too many attempts from this connection. Try again in a few minutes." }, 429);
  }

  const { email, state } = await readFields(request);

  if (typeof email !== "string" || !EMAIL_RE.test(email.trim())) {
    return json({ error: "That doesn't look like a valid email address." }, 400);
  }
  const stateCode = typeof state === "string" ? state.trim().toUpperCase() : "";
  if (!VALID_STATES.has(stateCode)) {
    return json({ error: "Pick a state from the list." }, 400);
  }

  // Fail loud, not quiet: an unset key must never look like a successful subscribe. A silent
  // success here loses a real lead with zero trace, which is worse than a visible error.
  if (!env.KIT_API_KEY) {
    console.error("[subscribe] KIT_API_KEY is not set. Rejecting submission instead of faking success.");
    return json(
      { error: "Sign-ups aren't working right now. Please try again later." },
      500,
    );
  }

  const cleanEmail = email.trim();
  let kitRes;
  try {
    kitRes = await fetch("https://api.kit.com/v4/subscribers", {
      method: "POST",
      headers: {
        "X-Kit-Api-Key": env.KIT_API_KEY,
        "content-type": "application/json",
      },
      body: JSON.stringify({
        email_address: cleanEmail,
        fields: { state: stateCode },
      }),
    });
  } catch (err) {
    console.error(`[subscribe] Kit request threw for ${maskEmail(cleanEmail)}:`, err.message);
    return json({ error: "Couldn't reach the mail provider. Try again in a moment." }, 502);
  }

  if (!kitRes.ok) {
    const errBody = await kitRes.text().catch(() => "");
    console.error(`[subscribe] Kit rejected ${maskEmail(cleanEmail)} (${kitRes.status}): ${errBody}`);
    return json({ error: "Couldn't complete sign-up. Try again in a moment." }, 502);
  }

  return json({ ok: true, state: stateCode }, 200);
}

// Any method other than POST/OPTIONS is not part of this API.
export async function onRequestGet() {
  return json({ error: "Use POST." }, 405);
}
