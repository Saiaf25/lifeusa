# LifeUSA logo signal monitoring check

Checked August 2, 2026 from 12:20 to 12:40 Europe/Istanbul. This was the third scheduled weekly check under automation `lifeusa-logo-signal-monitor`.

## Decision summary

- No verified publisher reply arrived for SENT-001 or SENT-002.
- The old WordPress archive, Kids That Do Good, and Arab Info Mall still publish the retired crescent logo.
- The approved Wix square and horizontal assets remain healthy and byte-for-byte identical to the documented masters.
- Owned homepage and Brand Resources signals remain correct. The homepage still emits two `WebSite` nodes, which keeps the remaining APR-007 cleanup open.
- Candid/GuideStar, GreatNonprofits, LinkedIn, both Facebook pages, Instagram, YouTube, and X show approved current blue-globe variants. Linktree shows the preferred yellow-ray avatar.
- The English Linktree Facebook destination still resolves to the Somali Facebook profile. ReliefWeb still exposes no LifeUSA logo and still links to `http://www.lifeusa.org/`.
- Google Search and Images returned Google's anti-automation page for the required English, United States, personalization-disabled queries. Paid-result logo, organic favicon, Knowledge Panel state, and ranked Images state are therefore inconclusive for August 2.
- The logged-out Southfield Google Maps listing remained observable with 4.3 stars, 20 reviews, the correct address, the stale HTTP website link, and current LifeUSA-branded media.
- Find-Us-Here, A-Z Business Finder, and Nextdoor remain publicly verified qualifying profiles. Directory progress remains 3 of 20.
- Stable-check count remains **0 of 3** because the retired source references are still live and the required Google result surfaces were not fully observable.

No external message, form, access request, approval, account change, or paid action was performed.

## Zoho Mail reply check

Mailbox: `hello@saiaf.me`, read-only.

| Record | Exact sent record | Reply result |
|---|---|---|
| SENT-001, Kids That Do Good | Subject `Please update the Life for Relief and Development logo`; message ID `1784122643723013500`; successful delivery record retained | No inbound message from `info@kidsthatdogood.com` and no inbound message in the exact subject search, including spam and trash |
| SENT-002, GreatNonprofits | Subject `Please update the Life for Relief and Development profile logo`; message ID `1784122678410013500`; successful delivery record retained | No inbound message from `support@greatnonprofits.org` and no inbound message in the exact subject search, including spam and trash |

The successful sent records remain historical facts. No reply, source correction, or Google refresh is inferred from delivery.

## Retired-source comparison

| Source | Public reference on August 2 | Direct file | Comparison with July 15 evidence | Result |
|---|---|---|---|---|
| Old WordPress archive | Page returned `200` and still referenced `life-logo-hd_white.png` | `200`, 1500 by 1500 PNG, SHA-256 `281840637b1241b09371d2c0adf19d4a7b683fbc8683d0af39e4ad42afc66850` | Decoded-pixel absolute error `0` | Retired crescent unchanged |
| Kids That Do Good | Page returned `200` and referenced `life-for-relief-and-development-logo.png` three times | `200`, 200 by 200 PNG, SHA-256 `007d9b603111684bd0142feb1dae5e41ce144e500d68bbc1ea6af14051f4e26f` | Decoded-pixel absolute error `0` | Retired crescent unchanged; SENT-001 still awaiting publisher action |
| Arab Info Mall | Page returned `200` and still referenced `10751.gif` | `200`, 200 by 200 GIF, SHA-256 `9296fe04f8808f906310433494959417a290d2933d5603362e40e25fce3bcb88` | Decoded-pixel absolute error `0` | Retired crescent unchanged; APR-001 remains pending |

The WordPress image still redirects from the documented files-domain URL to the equivalent WordPress uploads URL. The redirect is not a source correction because the page reference and decoded image remain unchanged.

## Acceptable authority-profile state

| Surface | Logged-out August 2 result |
|---|---|
| GreatNonprofits | Page and Open Graph data still reference `org_logo_513389_1711518504.png`; the 266 by 266 PNG retains SHA-256 `2d1de086aa753d889f32d05b3fabc232e76f1fe16f4c9a4ad0f64f6d67108117` and decoded-pixel absolute error `0` |
| Candid / GuideStar | Page still embeds `https://docs.candid.org/edoc/11078205`; the 1500 by 1500 PNG retains SHA-256 `f440247655ec4a13196be3ee40b291c361de42e596a05941395fc22dd42b6328` and decoded-pixel absolute error `0`; the public website link remains HTTP |
| LinkedIn | Public company page exposed a 200 by 200 approved blue-globe avatar and still lists the website as HTTP |
| Facebook, English | Logged-out page exposed the approved blue-globe avatar and current organization identity |
| Facebook, Somali | Logged-out page exposed the approved blue-globe avatar; this remains the destination used by the English Linktree Facebook button |
| Instagram | Logged-out Open Graph data exposed the approved blue-globe profile avatar |
| YouTube | Logged-out channel exposed the approved blue-globe avatar and its LifeUSA website destination |
| X | Logged-out profile exposed the approved blue-globe avatar |
| Linktree | Public page exposed the preferred yellow-ray avatar and canonical HTTPS LifeUSA link, but its English Facebook destination still resolves to profile ID `61563961181765` |
| ReliefWeb | Public profile returned `200`, exposed no LifeUSA logo, and still linked to `http://www.lifeusa.org/` |

Social CDN URLs rotate. The visible logo-family classification, not URL continuity alone, is the correctness test for these approved current variants.

## Owned signal and canonical asset health

| Asset or signal | August 2 result |
|---|---|
| Canonical square | `200`, 1800 by 1800 PNG, SHA-256 `d3d830b08effb1202b1ded8bc26bec91f78dfb8b89c97ef59f892b2ea88a77cb`, byte-for-byte and pixel-identical to the approved local master |
| Canonical horizontal | `200`, 4101 by 1201 PNG, SHA-256 `14819312d534ee94bcb625a87a15ab76cd05ad77ec9d09a2b514bf8c308cd867`, byte-for-byte and pixel-identical to the approved local master |
| Homepage structured data | Three JSON-LD blocks parsed with zero errors; one `NGO` node uses `https://www.lifeusa.org/#organization` and the canonical colored square; two `WebSite` nodes remain |
| Visible owned placements | Header and footer retain approved current horizontal-logo placements and expose two occurrences of `Life for Relief and Development logo` alt text |
| Favicon | Public `icon`, `shortcut icon`, `apple-touch-icon`, and `mask-icon` links still derive from approved square source `6df904_3ba0b63af7e945f0a92fbe9978934569~mv2.png` |
| Brand Resources | Page returned `200` and referenced both canonical square and horizontal Wix files |

## Directory-profile regression check

| Profile | August 2 public result |
|---|---|
| Find-Us-Here | `200`; correct organization details, approved 300 by 300 current-logo rendition, and canonical `https://www.lifeusa.org/` backlink remain visible |
| A-Z Business Finder | `200`; 1800 by 1800 profile image has decoded-pixel absolute error `0` against the canonical square, and the canonical backlink remains visible |
| Nextdoor | `200`; logged-out page continues to resolve under the LifeUSA organization slug and exposes the public organization identity |

All three continue to meet the strict Done definition. No additional profile was counted.

## Google property check

Required Search query:

`https://www.google.com/search?q=Life+for+Relief+and+Development+Southfield+MI&hl=en&gl=us&pws=0`

Required Images query:

`https://www.google.com/search?q=Life+for+Relief+and+Development+logo&hl=en&gl=us&pws=0&udm=2`

Both queries redirected to `google.com/sorry/` in a fresh isolated logged-out browser context. The paid-result logo, organic favicon, separate Knowledge Panel state, and ranked Images set were not directly observable and are recorded as **inconclusive**, not unchanged.

The public Maps listing remained directly observable at CID `0xd5173b8aa5409446`:

- 4.3 stars and 20 reviews;
- Non-profit organization;
- 17300 W 10 Mile Rd, Southfield, MI 48075;
- public website link still `http://www.lifeusa.org/`;
- public photo gallery remained available; and
- visible gallery media includes current LifeUSA branding.

This proves the current Maps state only. It does not prove the August 2 Search, paid-result, favicon, Knowledge Panel, or Images state.

## Status decisions

- SENT-001 and SENT-002 remain **Already sent**, with no verified publisher reply.
- LOGO-007 and LOGO-009 remain **In progress**.
- LOGO-008 and LOGO-011 remain **Waiting**.
- LOGO-014, LOGO-015, LOGO-016, LOGO-018, and LOGO-019 remain **In progress**.
- APR-001 through APR-006 and APR-008 remain pending. APR-007 remains approved and partially executed only for the duplicate `WebSite` cleanup. No approval item was executed.
- Stable-check count remains **0 of 3**.

## Next scheduled check

Sunday, August 9, 2026 at 10:00 Europe/Istanbul.
