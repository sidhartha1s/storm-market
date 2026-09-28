// Self-check for library/inhouse/snippets/helpers.js's logLerpScale: node scripts/test_log_zoom.mjs
// The one-frame-pair check the PR promises: the midpoint of a 1->4x zoom must read 2 (the
// geometric mean, log-space t=0.5), never 2.5 (the naive linear/additive mean) -- that's the
// whole reason this helper exists (mg-quickref.md "Motion and exits").
import assert from "node:assert/strict";
import { logLerpScale } from "../library/inhouse/snippets/helpers.js";

assert.equal(logLerpScale(1, 4, 0), 1, "t=0 must be exactly fromScale");
assert.equal(logLerpScale(1, 4, 1), 4, "t=1 must be exactly toScale");
assert.ok(Math.abs(logLerpScale(1, 4, 0.5) - 2) < 1e-9,
  `midpoint of 1->4 must be 2 (geometric mean), got ${logLerpScale(1, 4, 0.5)}`);
assert.ok(Math.abs(logLerpScale(1, 4, 0.5) - 2.5) > 0.1,
  "midpoint must NOT be 2.5 (that would be plain linear interpolation, the bug this fixes)");

// Pull-out case: 4->1 must be symmetric with the push-in, midpoint still the geometric mean, 2.
assert.ok(Math.abs(logLerpScale(4, 1, 0.5) - 2) < 1e-9,
  `midpoint of 4->1 pull-out must be 2 (geometric mean), got ${logLerpScale(4, 1, 0.5)}`);
assert.ok(Math.abs(logLerpScale(4, 1, 0.5) - 2.5) > 0.1,
  "pull-out midpoint must NOT be 2.5 (that would be plain linear lerp, the bug this fixes)");

console.log("test_log_zoom: ALL PASS");
