# LifeUSA logo signal monitoring check

Checked August 9, 2026 from 16:25 to 16:55 Europe/Istanbul. This was the fourth scheduled weekly check under automation `lifeusa-logo-signal-monitor`.

## Decision summary

- No verified publisher reply arrived for SENT-001 or SENT-002.
- The old WordPress archive, Kids That Do Good, and Arab Info Mall still publish the retired crescent logo.
- The approved Wix square and horizontal assets remain healthy and byte-for-byte identical to the documented masters.
- Google Search and Images were observable in a fresh signed-out browser session using English, United States, and personalization-disabled parameters.
- Google Search showed the approved current favicon, an approved blue-globe paid-result logo, and the Southfield entity panel without a retired logo. Google Images still visibly ranked the retired Kids That Do Good crescent result in the first loaded result set and also exposed the old WordPress archive as a result source.
- The Southfield entity panel still links to `http://www.lifeusa.org/`; its public photo gallery continues to show current LifeUSA-branded media.
- Candid/GuideStar, GreatNonprofits, LinkedIn, both Facebook pages, Instagram, YouTube, and X retain approved current variants. Linktree retains the preferred yellow-ray avatar but still sends its English Facebook button to the Somali Facebook page.
- Find-Us-Here, A-Z Business Finder, and Nextdoor remain publicly available qualifying profiles. Directory progress remains 3 of 20.
- Stable-check count remains **0 of 3** because the retired source references remain live and a retired source is still visible in Google Images.

No external message, form, access request, approval, account change, or paid action was performed.

## Zoho Mail reply check

Mailbox: `hello@saiaf.me`, read-only.

| Record | Exact sent record | Reply result |
|---|---|---|
| SENT-001, Kids That Do Good | Subject `Please update the Life for Relief and Development logo`; message ID `1784122643723013500`; successful delivery record retained | No inbound message from `info@kidsthatdogood.com` and no inbound message in the exact subject search, including spam and trash |
| SENT-002, GreatNonprofits | Subject `Please update the Life for Relief and Development profile logo`; message ID `1784122678410013500`; successful delivery record retained | No inbound message from `support@greatnonprofits.org` and no inbound message in the exact subject search, including spam and trash |

The successful sent records remain historical facts. No reply, source correction, or Google refresh is inferred from delivery.

## Retired-source comparison

| Source | Public reference on August 9 | Direct file | Comparison with July 15 evidence | Result |
|---|---|---|---|---|
| Old WordPress archive | Page returned `200` and still referenced `life-logo-hd_white.png` | `200`, 1500 by 1500 PNG, 514,944 bytes, SHA-256 `281840637b1241b09371d2c0adf19d4a7b683fbc8683d0af39e4ad42afc66850` | Byte-for-byte identical | Retired crescent unchanged |
| Kids That Do Good | Page returned `200`; visible image, Open Graph, and X/Twitter metadata referenced `life-for-relief-and-development-logo.png` three times | `200`, 200 by 200 PNG, 12,519 bytes, SHA-256 `007d9b603111684bd0142feb1dae5e41ce144e500d68bbc1ea6af14051f4e26f` | Byte-for-byte identical | Retired crescent unchanged; SENT-001 still awaiting publisher action |
| Arab Info Mall | Page returned `200` and still referenced `10751.gif` | `200`, 200 by 200 GIF, 12,092 bytes, SHA-256 `9296fe04f8808f906310433494959417a290d2933d5603362e40e25fce3bcb88` | Byte-for-byte identical | Retired crescent unchanged; APR-001 remains pending |

The WordPress image still redirects from the documented files-domain URL to the equivalent WordPress uploads URL. The redirect is not a source correction because the page reference and image bytes remain unchanged.

## Acceptable authority-profile state

| Surface | Logged-out August 9 result |
|---|---|
| GreatNonprofits | Page still references `org_logo_513389_1711518504.png`; the 266 by 266 PNG remains byte-for-byte identical with SHA-256 `2d1de086aa753d889f32d05b3fabc232e76f1fe16f4c9a4ad0f64f6d67108117` |
| Candid / GuideStar | Page still embeds `https://docs.candid.org/edoc/11078205`; the 1500 by 1500 PNG remains byte-for-byte identical with SHA-256 `f440247655ec4a13196be3ee40b291c361de42e596a05941395fc22dd42b6328`; the public website link remains HTTP |
| LinkedIn | Public page exposed a 200 by 200 approved current company avatar and still lists the website as HTTP |
| Facebook, English | Logged-out page exposed the official organization identity and approved current avatar |
| Facebook, Somali | Logged-out page exposed the Somali organization identity and approved current avatar; it remains the destination used by the English Linktree Facebook button |
| Instagram | Logged-out profile and sign-up preview visibly exposed the approved blue-globe avatar |
| YouTube | Logged-out channel metadata exposed the approved 900 by 900 blue-globe avatar and its LifeUSA website destination |
| X | Logged-out profile metadata exposed the approved current avatar |
| Linktree | Public page exposed the preferred yellow-ray identity and canonical HTTPS LifeUSA link, but its English Facebook destination still resolves to profile ID `61563961181765` |
| ReliefWeb | Public profile returned `200`, exposed no LifeUSA logo, and still linked to `http://www.lifeusa.org/` |

Social CDN URLs can rotate. The visible logo-family classification, not URL continuity alone, is the correctness test for approved current variants.

## Owned signal and canonical asset health

| Asset or signal | August 9 result |
|---|---|
| Canonical square | `200`, 1800 by 1800 PNG, 29,393 bytes, SHA-256 `d3d830b08effb1202b1ded8bc26bec91f78dfb8b89c97ef59f892b2ea88a77cb`, byte-for-byte identical to the approved local master |
| Canonical horizontal | `200`, 4101 by 1201 PNG, 51,861 bytes, SHA-256 `14819312d534ee94bcb625a87a15ab76cd05ad77ec9d09a2b514bf8c308cd867`, byte-for-byte identical to the approved local master |
| Homepage structured data | Three JSON-LD blocks remained present; one `NGO` node used the canonical colored square and two `WebSite` nodes remained |
| Visible owned placements | Header and footer retained two occurrences of `Life for Relief and Development logo` alt text |
| Favicon | Public `icon`, `shortcut icon`, `apple-touch-icon`, and `mask-icon` links still derived from approved square source `6df904_3ba0b63af7e945f0a92fbe9978934569~mv2.png` |
| Brand Resources | Page returned `200` and referenced both canonical square and horizontal Wix files |

## Directory-profile regression check

| Profile | August 9 public result |
|---|---|
| Find-Us-Here | `200`; correct organization profile, approved 300 by 300 current-logo rendition, and canonical HTTPS backlink remained in the public page |
| A-Z Business Finder | `200`; its 1800 by 1800 profile image had decoded-pixel absolute error `0` against the canonical square, and the canonical backlink remained in the public page |
| Nextdoor | `200`; logged-out page continued to resolve under the LifeUSA organization slug and exposed the public organization identity and approved profile image metadata |

All three continue to meet the strict Done definition. No additional profile was counted.

## Google property check

Required Search query:

`https://www.google.com/search?q=Life+for+Relief+and+Development+Southfield+MI&hl=en&gl=us&pws=0`

Required Images query:

`https://www.google.com/search?q=Life+for+Relief+and+Development+logo&hl=en&gl=us&pws=0&udm=2`

The fresh isolated browser initially received Google's anti-automation page for Search, but both Search and Images became directly observable after repeating the exact URLs in the same signed-out isolated context. The footer could not determine a physical location, so `gl=us` is the evidence for the requested United States result context; no stronger location claim is made.

Directly observed Search state:

- the primary LifeUSA organic result displayed the approved current blue `Life` favicon;
- the Southfield entity panel showed 4.3 stars, 20 reviews, the correct address and phone, and no retired-logo identity image;
- the entity panel website link remained `http://www.lifeusa.org/`;
- the visible public photo gallery showed current LifeUSA blue-globe branding; and
- the serving LIFE USA sponsored result displayed an approved blue-globe logo.

Directly observed Images state:

- the first loaded result set included current LifeUSA-owned and approved social imagery;
- the retired Kids That Do Good crescent result remained visibly present in the first loaded result set; and
- the old WordPress archive remained present as a result source.

This is a partial Google refresh signal only: current favicon, paid, and entity signals are healthy, but the ranked retired source proves that Google Images is not stable.

## Status decisions

- SENT-001 and SENT-002 remain **Already sent**, with no verified publisher reply.
- LOGO-007 and LOGO-009 remain **In progress**.
- LOGO-008 and LOGO-011 remain **Waiting**.
- LOGO-014, LOGO-015, LOGO-016, LOGO-018, and LOGO-019 remain **In progress**.
- APR-001 through APR-006 and APR-008 remain pending. APR-007 remains approved and partially executed only for the duplicate `WebSite` cleanup. No approval item was executed.
- Stable-check count remains **0 of 3**.

## Next scheduled check

Sunday, August 16, 2026 at 10:00 Europe/Istanbul.
