# LifeUSA logo signal monitoring log

Monitoring started July 15, 2026. Scheduled checks run every Sunday at 10:00 Europe/Istanbul under automation `lifeusa-logo-signal-monitor`. External communication, submissions, access requests, and client-account changes remain human-gated.

## Completion rule

The program is not complete until the approved current logo is consistently shown across the defined owned, Google, and authoritative third-party surfaces, retired source references are corrected or removed, and three consecutive scheduled checks show no regression.

Current stable-check count: **0 of 3**. Source corrections are still incomplete.

## July 21 owned-placement and homepage verification

The user reported completing the favicon, header, footer, and Brand Resources navigation work. Cache-busted, logged-out public verification proved:

- the header and footer use the same approved 4101 by 1201 horizontal master, with byte-identical SHA-256 `14819312d534ee94bcb625a87a15ab76cd05ad77ec9d09a2b514bf8c308cd867`;
- the favicon source is byte-identical to the approved 1800 by 1800 square, with SHA-256 `d3d830b08effb1202b1ded8bc26bec91f78dfb8b89c97ef59f892b2ea88a77cb`;
- the visible header and footer logos use the descriptive alt text `Life for Relief and Development logo`; and
- `Brand Resources` is present in the expanded About submenu and its `https://www.lifeusa.org/brand-resources` destination returns HTTP `200`.

`LOGO-006` is **Done**. `APR-007` remains approved and partially executed only because the two homepage `WebSite` nodes still require consolidation. Full evidence: [July 21 LOGO-006 and navigation verification](../2026-07-21/logo-006-and-navigation-verification.md).

This ad hoc owned-site verification does not prove a Google refresh and does not increment the scheduled stable-check count, which remains **0 of 3**.

## July 20 owned brand-resources publication

The user confirmed publication of `https://www.lifeusa.org/brand-resources`. A logged-out public check returned `200` and verified native Wix heading, introductory copy, and a two-item Wix Pro Gallery.

- The live 1800 by 1800 square PNG is byte-for-byte identical to the approved square master.
- The initial check found a derived 3000 by 879 horizontal JPG; a second cache-busted check proved it was replaced by the approved 4101 by 1201 canonical PNG.
- The square has descriptive alt text. The horizontal image alt field remains empty, but its official title is visible.
- The project owner explicitly confirmed that direct download links are not required and accepted the current page as complete for this action.

`LOGO-004` is **Done**. The owned page and both canonical assets are verified live under the project owner's acceptance criteria. Full evidence: [July 20 LOGO-004 brand-page verification](../2026-07-20/logo-004-brand-page-live-verification.md).

This ad hoc owned-site change does not increment the scheduled stable-check count, which remains **0 of 3**.

## July 20 owned structured-data correction

The user explicitly approved `APR-007`, manually published the prepared homepage NGO markup, and reported completion. A cache-busted public-source verification proved the following:

- one parseable `NGO` node now uses `https://www.lifeusa.org/#organization`;
- `alternateName`, the verified official `sameAs` list, address, and contact point are present;
- the NGO logo is the canonical colored 1800 by 1800 Wix square;
- the former white-logo URL is absent from the fetched homepage HTML; and
- the canonical square still returns HTTP `200` with the documented dimensions and checksum.

`LOGO-005` is now **Done**. `APR-007` remains approved and partially executed because two `WebSite` nodes and remaining visual placements are still open; the brand-resources portion is complete under `LOGO-004`. Full evidence: [July 20 LOGO-005 verification](../2026-07-20/logo-005-live-verification.md).

This ad hoc correction does not increment the scheduled stable-check count, which remains **0 of 3**.

## July 19 logo classification decision

The client confirmed that the blue-globe logo used on Facebook and matching official profiles is an acceptable current variant. It is not an outdated-logo blocker. The canonical yellow-ray square remains preferred for new placements. The retired crescent mark remains the source-removal target. SENT-002 is preserved as a historical sent-message record, but GreatNonprofits no longer requires a logo correction.

## July 19 scheduled check

The first scheduled weekly check is complete. No publisher reply, source correction, account change, or Google refresh was proved.

### Verified unchanged

- Zoho Mail: exact and broad read-only searches, including spam and trash, found no reply to SENT-001 or SENT-002. The original message IDs and successful delivery records remain unchanged.
- Retired-crescent sources: Kids That Do Good, the old WordPress archive, and Arab Info Mall still reference their documented legacy images. Each direct image returned `200` and matched the preserved July 15 evidence with decoded-pixel absolute error `0`.
- Acceptable blue-globe variants: GreatNonprofits and Candid/GuideStar remain pixel-identical to the preserved evidence. LinkedIn, YouTube, and X direct profile images also remain pixel-identical. Both public Facebook profiles visibly retain the acceptable current variant. These are observations, not correction blockers.
- Other authority signals: the English Linktree still points its Facebook destination to the Somali profile, and ReliefWeb still links to `http://www.lifeusa.org`. Charity Navigator still exposes no LifeUSA profile logo.
- Owned signals: both canonical Wix assets returned `200` with unchanged dimensions and SHA-256 checksums. The homepage still uses the separate white `NGO.logo` and separate favicon source.
- Google Maps: the logged-out Southfield listing still shows 4.3 stars, 20 reviews, the correct address, a stale HTTP website link, and blue-globe imagery. The HTTP link remains actionable; matching blue-globe imagery is acceptable.

### Inconclusive surfaces

The signed-out Google Search and Images queries were requested with `hl=en`, `gl=us`, and `pws=0`, but Google returned an anti-automation challenge. The paid-result logo, organic favicon, Knowledge Panel state, and ranked Images set were not directly observable. Their July 15 verified state remains the last proved state; no current claim was inferred.

Instagram returned a logged-out public-page load error. TikTok and Threads remain unavailable for reliable logged-out image verification. Their statuses were not changed.

Full dated measurements, checksums, and evidence interpretation: [July 19 monitoring check](../2026-07-19/monitoring-check.md).

### Decision

- SENT-001 and SENT-002 remain **Already sent**, with no verified reply.
- LOGO-008 and LOGO-011 remain **Waiting**.
- LOGO-004 through LOGO-007, LOGO-009, LOGO-012, LOGO-014 through LOGO-016, and LOGO-018 remain **In progress**.
- APR-001 through APR-008 remain pending approval; no item was executed.
- Stable-check count remains **0 of 3** because source corrections are incomplete.

## July 15 control check

### Zoho delivery and reply state

| Record | Delivery | Reply search | Evidence |
|---|---|---|---|
| SENT-001, Kids That Do Good | Delivered successfully | No reply found from `info@kidsthatdogood.com` | Zoho message `1784122643723013500`; exact subject and sender search, including spam and trash |
| SENT-002, GreatNonprofits | Delivered successfully | No reply found from `support@greatnonprofits.org` | Zoho message `1784122678410013500`; exact subject and sender search, including spam and trash |

No new message was sent during this monitoring check.

### Public publisher state

| Source | Public page state | Direct image state | Result |
|---|---|---|---|
| Kids That Do Good | Page, Open Graph image, X/Twitter image, and visible profile image still reference `life-for-relief-and-development-logo.png` | 200 by 200 PNG; decoded pixels exactly match the captured retired crescent image with ImageMagick absolute-error count `0` | Unchanged; awaiting publisher correction |
| GreatNonprofits | Organization JSON-LD, Open Graph image, X/Twitter image, and visible profile still reference `org_logo_513389_1711518504.png` | 266 by 266 PNG; SHA-256 remains `2d1de086aa753d889f32d05b3fabc232e76f1fe16f4c9a4ad0f64f6d67108117` | Unchanged; awaiting publisher correction |

The Kids file-level SHA-256 differs from the stored evidence copy because of PNG encoding or metadata, but decoded-pixel comparison proves that the visible logo itself is identical. This avoids treating harmless CDN re-encoding as a correction.

### Canonical Wix asset health

| Asset | Public state | Dimensions | SHA-256 comparison |
|---|---|---|---|
| Square | HTTP `200`, immutable cache | 1800 by 1800 | Remote and local both `d3d830b08effb1202b1ded8bc26bec91f78dfb8b89c97ef59f892b2ea88a77cb` |
| Horizontal | HTTP `200`, immutable cache | 4101 by 1201 | Remote and local both `14819312d534ee94bcb625a87a15ab76cd05ad77ec9d09a2b514bf8c308cd867` |

Both approved canonical files remain healthy and byte-for-byte identical to the documented local masters.

### Google Images source check

Repeatable query:

`https://www.google.com/search?q=Life+for+Relief+and+Development+logo&hl=en&gl=us&pws=0&udm=2`

The first loaded Google Images result set still includes Kids That Do Good and the old LifeUSA WordPress archive alongside current LifeUSA, Facebook, SHARE Detroit, social, and unrelated sources. Because the underlying Kids and WordPress sources still publish the retired mark, Google continues to have crawlable legacy-logo inputs for this exact logo-focused query.

### Decision

- SENT-001 remains **Already sent**, not completed.
- SENT-002 remains **Already sent**, not completed.
- LOGO-008 remains **Waiting**.
- LOGO-014 remains **In progress**.
- LOGO-018 moves to **In progress** because the scheduled monitor is active and this control check is recorded.
- Stable-check count remains **0 of 3**.

## Next scheduled check

Sunday, July 26, 2026 at 10:00 Europe/Istanbul. The run will repeat reply, source, authority-profile, canonical-asset, Google Search, Images, Business Profile, paid-result, favicon, and Maps checks without executing pending approval items.
