# LifeUSA logo signal monitoring check

Checked September 20, 2026 at approximately 12:20 Europe/Istanbul. This run made read-only web and Zoho Mail checks. No publisher contact, form, feedback submission, account change, APR, RESUME, or escalation was executed.

## Executive result

- The three established retired-logo sources still publish the retired crescent. Their direct images returned `200` and had decoded-pixel absolute error `0` against the July 15 captures.
- The English Google Images benchmark still fails: Kids That Do Good ranked 5, Arab Info Mall 7, and the old WordPress archive 10 in the first loaded result set. The retired Kids and Arab marks were visible in the initial viewport, and the WordPress result was present in the same loaded set.
- The exact Arabic query `لايف للإغاثة والتنمية` and contextual `LifeUSA logo` Images query had no tracked retired-source result in their loaded sets. Neither initial viewport showed the retired crescent.
- The canonical Wix files and primary approved authority avatars remain current. The Southfield Business Profile and a serving LifeUSA sponsored result showed current Life branding.
- Stable-check count remains **0 of 3**. The next scheduled check is **Sunday, September 27, 2026 at 10:00 Europe/Istanbul**.

## Mail: reply and delivery are separate states

Zoho account `hello@saiaf.me` was searched read-only for exact sender addresses and subjects with spam and trash included, plus common delivery-failure subjects. The four exact sent-message records were present. Searches returned no verified publisher reply and no failure tied to these messages. A separate unrelated bounce was excluded.

| Record | Exact sent ID and subject | September 20 observation |
|---|---|---|
| RESUME-001 | `1788853905198013500`, `Follow-up: retired LifeUSA logo is still live` | Sent item retains `mailDeliveryStatus: success`; no verified reply or related bounce |
| RESUME-002 | `1788854081131013500`, `Correction request for Life for Relief and Development profile 879` | Sent item retains `mailDeliveryStatus: success`; no verified reply or related bounce |
| SENT-001 | `1784122643723013500`, `Please update the Life for Relief and Development logo` | Historical sent item present; no verified reply; current API delivery field says `not_available` |
| SENT-002 | `1784122678410013500`, `Please update the Life for Relief and Development profile logo` | Historical sent item present; no verified reply; current API delivery field says `not_available` |

The September 8 delivery record remains historical evidence. Neither sending nor successful delivery proves a publisher changed a source or Google refreshed a result.

## Retired public sources and direct files

| Source | Page | Direct image | July reference comparison | State |
|---|---|---|---|---|
| [Old WordPress archive](https://lifeusaorg.wordpress.com/where-we-are/) | `200`; references `life-logo-hd_white.png` | [PNG](https://lifeusaorg.files.wordpress.com/2015/05/life-logo-hd_white.png), `200`, 1500 by 1500, 514,944 bytes, SHA-256 `281840637b1241b09371d2c0adf19d4a7b683fbc8683d0af39e4ad42afc66850` | Decoded-pixel AE `0` | Retired crescent unchanged |
| [Kids That Do Good](https://kidsthatdogood.com/causes/life-relief-development/) | `200`; visible image and `og:image` still reference the retired file | [PNG](https://kidsthatdogood.com/wp-content/uploads/2019/06/life-for-relief-and-development-logo.png), `200`, 200 by 200, 12,523 bytes, SHA-256 `22591875a477835091e32614b06482bdce8e89ffae49625dde13cbed5e614c49` | Decoded-pixel AE `0` | Retired crescent unchanged despite prior re-encoding |
| [Arab Info Mall](https://arabinfomall.bibalex.org/En/Index.aspx?orgid=879&sectionid=1) | `200`; references `10751.gif` | [GIF](https://arabinfomall.bibalex.org/Attachments/Logos/10751.gif), `200`, 200 by 200, 12,092 bytes, SHA-256 `9296fe04f8808f906310433494959417a290d2933d5603362e40e25fce3bcb88` | Decoded-pixel AE `0` | Retired crescent unchanged |

## Owned and authority identity

- [Canonical Wix square](https://static.wixstatic.com/media/af2a6c_49a4190c354746b493c123d311222fb5~mv2.png): `200`, 1800 by 1800, 29,393 bytes, SHA-256 `d3d830b08effb1202b1ded8bc26bec91f78dfb8b89c97ef59f892b2ea88a77cb`, decoded-pixel AE `0` against the preserved master.
- [Canonical Wix horizontal](https://static.wixstatic.com/media/af2a6c_1bd1137d792b44c3855d26ee4cfcced0~mv2.png): `200`, 4101 by 1201, 51,861 bytes, SHA-256 `14819312d534ee94bcb625a87a15ab76cd05ad77ec9d09a2b514bf8c308cd867`. The [Brand Resources page](https://www.lifeusa.org/brand-resources) still references both files.
- [Homepage](https://www.lifeusa.org/): three parseable JSON-LD blocks, one `NGO` node using the canonical square and two `WebSite` nodes. The duplicate `WebSite` cleanup remains open.
- [GreatNonprofits](https://greatnonprofits.org/org/life-for-relief-and-development): `200`; approved 266 by 266 blue-globe file retains SHA-256 `2d1de086aa753d889f32d05b3fabc232e76f1fe16f4c9a4ad0f64f6d67108117` and pixel AE `0`.
- [Candid / GuideStar](https://www.guidestar.org/profile/95-4402149): `200`; approved 1500 by 1500 blue-globe file retains SHA-256 `f440247655ec4a13196be3ee40b291c361de42e596a05941395fc22dd42b6328` and pixel AE `0`; the website URL remains HTTP.
- [LinkedIn](https://www.linkedin.com/company/life-for-relief-and-development/), [Instagram](https://www.instagram.com/life4relief/), and [X](https://x.com/LIFEforRELIEF): public profile images returned `200` and matched their approved July reference pixels at 200 by 200, 100 by 100, and 400 by 400 respectively. LinkedIn still contains an HTTP LifeUSA link.
- [YouTube](https://www.youtube.com/channel/UCRTkW2TMw344eC562GSK1nA): `200`; its 900 by 900 avatar remains the approved blue-globe artwork. A small decoded difference from the July JPEG (AE 22,017 across 3,240,000 channel values) is consistent with recompression and is not treated as a new logo.
- [Linktree](https://linktr.ee/LIFEUSA): `200`; current Life branding remains public. Its Facebook destination still references Somali profile ID `61563961181765`.
- English and Somali Facebook pages returned `400` in logged-out direct retrieval, so their own current profile images remain inconclusive in this run. [ReliefWeb](https://reliefweb.int/organization/life) returned `200`, exposes no logo in public markup, and retains an HTTP LifeUSA website link.
- [Find-Us-Here](https://www.find-us-here.com/businesses/Life-for-Relief-and-Development-Southfield-Michigan-USA/34560214/), [A-Z Business Finder](https://www.a-zbusinessfinder.com/business-directory/Life-for-Relief-and-Development-Southfield-Michigan-USA/34560214/), [Nextdoor](https://nextdoor.com/pages/life-for-relief-and-development-southfield-mi/), and [ProvenExpert](https://www.provenexpert.com/lifeusa/) returned `200` with current profile signals. Nextdoor's 1800 by 1800 image matched the canonical square at pixel AE `0`. Idealist still lacks a verified public LifeUSA profile and is not counted.

## Google Search, Images, paid, favicon, Business Profile, and Maps

The observed requests used `hl=en`, `gl=us`, `pws=0`; Images additionally used `udm=2`. The required Arabic query used `hl=ar`, `gl=us`, `pws=0`, `udm=2`. Results were inspected in the browser as visible result sets, not inferred from search snippets.

| Query or surface | September 20 observation |
|---|---|
| [English Images benchmark](https://www.google.com/search?q=Life+for+Relief+and+Development+logo&hl=en&gl=us&pws=0&udm=2) | Kids That Do Good position 5, Arab Info Mall position 7, WordPress position 10 in the first loaded set; retired marks visibly persist. A PNGEgg result also appeared at position 11, but its source returned `403`, so its underlying file and correction status were not classified. |
| [English Images context](https://www.google.com/search?q=LifeUSA+logo&hl=en&gl=us&pws=0&udm=2) | No tracked retired-source result in the first loaded set; initial viewport showed current LifeUSA and unrelated same-name logos, with no retired crescent. |
| [Exact Arabic Images query](https://www.google.com/search?q=%D9%84%D8%A7%D9%8A%D9%81+%D9%84%D9%84%D8%A5%D8%BA%D8%A7%D8%AB%D8%A9+%D9%88%D8%A7%D9%84%D8%AA%D9%86%D9%85%D9%8A%D8%A9&hl=ar&gl=us&pws=0&udm=2) | No tracked retired-source result in the first loaded set. The initial viewport showed current LifeUSA social and press imagery; no retired crescent. Retired-result source, type, and position: none observed. |
| [Branded Google Search](https://www.google.com/search?q=Life+for+Relief+and+Development&hl=en&gl=us&pws=0) | Organic `lifeusa.org` result used the current blue `Life` favicon. A LIFE USA sponsored result served lower on the page with the same current blue `Life` icon. No separate Knowledge Panel appeared. |
| Southfield Business Profile and [Maps](https://www.google.com/maps/search/Life+For+Relief+%26+Development+Southfield+MI?hl=en&gl=us) | 4.3 stars, 20 reviews, `17300 W 10 Mile Rd, Southfield, MI 48075`, `(800) 827-3543`, and an HTTP website link. The cover and first gallery photos showed current Life branding, with no retired crescent in the inspected media. |

The browser displayed the signed-in `sgamal2593@gmail.com` account while Google Search's footer said `Results are not personalized`. The query parameters and footer support a controlled comparison, but the observation is not represented as a logged-out baseline. The public source blockers independently keep the campaign open.

## Publication and decision

At the start of this run, `origin/main` contained the September 13 update (`ebc2fed`), but the cache-busted GitHub Pages status HTML differed from that commit and its September 13 evidence URL returned `404`. GitHub's Pages API still reported that build as `building`, with no new Pages run after September 9. The repository state and public state must be reported separately until the deployment is verified.

RESUME-001 and RESUME-002 remain delivered, without verified reply or source correction. RESUME-003 remains outside the active action queue because no authorized WordPress owner is known. RESUME-004 remains cancelled. The September 15 Kids escalation remains unapproved and was not executed. No action status advanced. Stable checks remain **0 of 3**.
