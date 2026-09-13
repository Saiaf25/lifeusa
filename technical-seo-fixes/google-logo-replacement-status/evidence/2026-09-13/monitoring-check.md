# LifeUSA logo signal monitoring check

Checked September 13, 2026 from Europe/Istanbul. This scheduled run was read-only outside the repository. No message, form, access request, account change, publisher contact, Google submission, or approval item was executed.

## Executive result

- No verified reply or delivery failure was found for the September 8 Kids That Do Good or Arab Info Mall messages. No reply was found for the historical July Kids That Do Good or GreatNonprofits messages.
- The old WordPress archive, Kids That Do Good, and Arab Info Mall still publish the retired crescent. All three direct files returned `200` and had decoded-pixel absolute error `0` against the July evidence.
- Kids That Do Good re-encoded its PNG again. The file is now 12,523 bytes with SHA-256 `22591875a477835091e32614b06482bdce8e89ffae49625dde13cbed5e614c49`, but the decoded pixels remain identical to the retired-logo reference.
- The canonical Wix square and horizontal files returned `200` with unchanged dimensions, checksums, and decoded pixels.
- The Google Images benchmark still fails. Kids That Do Good, Arab Info Mall, and the old WordPress archive appeared at positions 5, 8, and 11 in the first loaded result set, and their retired crescents were visible in the initial viewport.
- The exact Arabic query `لايف للإغاثة والتنمية` and the contextual `LifeUSA logo` query had no tracked retired-source result in their loaded sets and no retired crescent in the initial viewport.
- Organic Search and the Southfield Business Profile showed current Life branding. No LifeUSA paid result or separate Knowledge Panel was observed. Maps retained current campaign imagery, 4.3 stars, 20 reviews, correct contact details, and a public LifeUSA website link.
- Stable-check count remains **0 of 3**. All three retired public sources are still live, and the benchmark Images query still surfaces them.

## Zoho Mail reply and delivery check

Read-only searches covered exact subjects, exact sender domains, spam, trash, broader domain mentions, and common delivery-failure subjects.

| Record | Verified sent evidence | September 13 result |
|---|---|---|
| RESUME-001, Kids That Do Good | Subject `Follow-up: retired LifeUSA logo is still live`; message ID `1788853905198013500`; Zoho delivery state `success` | No inbound message from `info@kidsthatdogood.com`; no delivery-failure notice |
| RESUME-002, Arab Info Mall | Subject `Correction request for Life for Relief and Development profile 879`; message ID `1788854081131013500`; Zoho delivery state `success` | No inbound message from `arf@bibalex.org` or `info.mall@bibalex.org`; no delivery-failure notice |
| SENT-001, Kids That Do Good | Subject `Please update the Life for Relief and Development logo`; message ID `1784122643723013500`; historical delivery state `success` | No verified publisher reply |
| SENT-002, GreatNonprofits | Subject `Please update the Life for Relief and Development profile logo`; message ID `1784122678410013500`; historical delivery state `success` | No verified publisher reply |

Delivery remains a distinct historical fact. No reply, source correction, or Google refresh is inferred from it.

## Retired-logo sources

| Source | Public page evidence | Direct file evidence | Comparison | Result |
|---|---|---|---|---|
| Old WordPress archive | `200`; still references `life-logo-hd_white.png` | `200`; 1500 by 1500 PNG; 514,944 bytes; SHA-256 `281840637b1241b09371d2c0adf19d4a7b683fbc8683d0af39e4ad42afc66850` | Decoded-pixel AE `0` against `retired-wordpress-logo.png` | **Unchanged legacy** |
| Kids That Do Good | `200`; the visible profile image still references `life-for-relief-and-development-logo.png` | `200`; 200 by 200 PNG; 12,523 bytes; SHA-256 `22591875a477835091e32614b06482bdce8e89ffae49625dde13cbed5e614c49` | Decoded-pixel AE `0` against `retired-kids-that-do-good-logo.png` | **Re-encoded, visually unchanged legacy** |
| Arab Info Mall | `200`; still references `10751.gif` and retains legacy organization information | `200`; 200 by 200 GIF; 12,092 bytes; SHA-256 `9296fe04f8808f906310433494959417a290d2933d5603362e40e25fce3bcb88` | Decoded-pixel AE `0` against `retired-arab-info-mall-logo.gif` | **Unchanged legacy** |

## Owned LifeUSA signals

| Signal | September 13 evidence | Result |
|---|---|---|
| Homepage | `200`; three JSON-LD blocks; one `NGO` node references the canonical square; two `WebSite` nodes remain | **Current; duplicate WebSite cleanup remains open** |
| Brand Resources | `200`; still presents the approved square and horizontal assets | **Current** |
| Canonical square | `200`; 1800 by 1800 PNG; 29,393 bytes; SHA-256 `d3d830b08effb1202b1ded8bc26bec91f78dfb8b89c97ef59f892b2ea88a77cb`; decoded-pixel AE `0` | **Unchanged current** |
| Canonical horizontal | `200`; 4101 by 1201 PNG; 51,861 bytes; SHA-256 `14819312d534ee94bcb625a87a15ab76cd05ad77ec9d09a2b514bf8c308cd867`; decoded-pixel AE `0` | **Unchanged current** |

## Authority profiles and directories

| Surface | Public evidence | Classification |
|---|---|---|
| GreatNonprofits | `200`; the 266 by 266 approved blue-globe file retained SHA-256 `2d1de086aa753d889f32d05b3fabc232e76f1fe16f4c9a4ad0f64f6d67108117` and decoded-pixel AE `0` | **Current** |
| Candid / GuideStar | `200`; the 1500 by 1500 approved blue-globe file retained SHA-256 `f440247655ec4a13196be3ee40b291c361de42e596a05941395fc22dd42b6328`; website link remains HTTP | **Current logo; stale link** |
| LinkedIn | `200`; first-party 200 by 200 Open Graph image retained decoded-pixel AE `0` against the approved evidence | **Current** |
| YouTube | `200`; first-party 900 by 900 avatar remained visually consistent with the approved blue-globe evidence | **Current** |
| X | `200`; a new first-party avatar URL served a 400 by 400 image with decoded-pixel AE `0` against the approved evidence | **Current; delivery URL changed** |
| Instagram | `200`; account-specific 100 by 100 Open Graph image had decoded-pixel AE `0` against the approved evidence | **Current** |
| Linktree | `200`; current Life-branded Open Graph identity remains public; Facebook destination still references Somali profile ID `61563961181765` | **Current identity; wrong destination** |
| ReliefWeb | `200`; no LifeUSA logo exposed in public markup; website remains `http://www.lifeusa.org` | **No logo; stale link** |
| Facebook, English and Somali | Both logged-out public requests returned `400` without account-specific image metadata | **Inconclusive** |
| Find-Us-Here | `200`; public LifeUSA identity and approved logo reference remained available | **Counted profile remains live** |
| A-Z Business Finder | `200`; direct 1800 by 1800 image had decoded-pixel AE `0` against the canonical square | **Counted profile remains live** |
| Nextdoor | `200`; direct 1800 by 1800 image had decoded-pixel AE `0` against the canonical square | **Counted profile remains live** |
| ProvenExpert | `200`; redirected to the public English-US LifeUSA profile and retained the approved logo and canonical profile identity | **Counted profile remains live** |
| Idealist | An exact-name `site:idealist.org` search returned other organizations but no matching public LifeUSA profile | **Still not verified logged out; does not count** |

## Google surfaces

The following public requests used the documented query, language, United States country, and `pws=0` controls:

- Google Search: `Life for Relief and Development`, `hl=en`, `gl=us`, `pws=0`
- Google Images benchmark: `Life for Relief and Development logo`, `hl=en`, `gl=us`, `pws=0`, `udm=2`
- Google Images context: `LifeUSA logo`, `hl=en`, `gl=us`, `pws=0`, `udm=2`
- Exact Arabic Images query: `لايف للإغاثة والتنمية`, `hl=ar`, `gl=us`, `pws=0`, `udm=2`
- Southfield Maps route: `Life For Relief & Development`, `hl=en`, `gl=us`

### Search, paid result, favicon, and entity panel

- The organic LifeUSA result displayed the approved current blue `Life` favicon.
- No LifeUSA sponsored result served in the observed result set. Paid-logo presentation was therefore not classifiable in this run.
- The right-side entity surface was the established Southfield Business Profile with current campaign imagery, 4.3 stars, 20 reviews, correct address and phone, and a public LifeUSA website link.
- No separate LifeUSA Knowledge Panel was observed.

### Google Images

- Benchmark result order: Kids That Do Good at position 5, Arab Info Mall at position 8, and the old WordPress archive at position 11 in the first loaded result set. Retired crescents from the tracked sources were visible in the initial viewport.
- `LifeUSA logo`: no tracked retired-source result appeared in the loaded set, and no retired crescent was visible in the initial viewport.
- `لايف للإغاثة والتنمية`: no tracked retired-source result appeared in the loaded set, and no retired crescent was visible in the initial viewport. The visible sources were current LifeUSA social and press imagery.

The browser session displayed a signed-in Google account even though `pws=0` was applied. The main Search accessibility state also exposed a personalized-recommendations label. These observations are useful for current presentation evidence, but they are not represented as a strictly signed-out baseline. This limitation does not affect the campaign decision because the public source blockers and benchmark failure are independently proved.

### Maps

- The Southfield profile remained public at 4.3 stars and 20 reviews.
- Address and phone remained `17300 W 10 Mile Rd, Southfield, MI 48075` and `(800) 827-3543`.
- The visible cover retained current blue and yellow Life branding. No retired crescent was visible in the inspected state.

## Decision and next date

- No action status advanced.
- RESUME-001 and RESUME-002 remain delivered with no verified reply or source correction.
- RESUME-003 remains outside the active action queue because no authorized WordPress owner is known.
- RESUME-004 remains cancelled. The exact Arabic query is now part of the monitoring matrix.
- No APR, RESUME, escalation, email, feedback submission, or account change was executed.
- The September 15 Kids That Do Good escalation remains a future, separately human-gated option. It is not approved or executed.
- Stable-check count remains **0 of 3**.
- Next scheduled check: **Sunday, September 20, 2026 at 10:00 Europe/Istanbul**.

## Publication QA

- HTML validation passed with no errors.
- All 15 local `href` and `src` references resolved; no duplicate IDs were found.
- Responsive checks passed at 375, 768, and 1440 CSS pixels with no horizontal overflow, missing images, console warnings, or console errors.
- `git diff --check` passed, and the scoped update contains no U+2014 em dash characters.
