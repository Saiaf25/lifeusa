# LifeUSA logo source audit

Captured and verified July 15, 2026.

## Capture protocol

- Query: `LifeUSA`
- Surface: Google Images
- Locale: English (`hl=en`), United States (`gl=us`)
- Personalization parameter: disabled (`pws=0`)
- Result order: first 20 external source links in Google Images document order
- Supporting capture: `google-images-lifeusa-desktop.jpg`

Google results can vary by time, location, device, and interface behavior. This inventory is a dated baseline, not a permanent ranking claim.

## First-20 result summary

| Classification | Count | Interpretation |
|---|---:|---|
| LifeUSA-owned pages | 9 | Current LifeUSA content on `lifeusa.org` |
| Official LifeUSA social sources | 5 | Instagram and Linktree results using the current brand family |
| Unrelated same-name businesses | 4 | `lifeusa.international` and `lifeusaonline.com`; not Life for Relief and Development |
| Related third-party marketplace results | 2 | One eBay listing shown twice; the product imagery uses the current LifeUSA mark |
| Retired crescent logo in this exact top 20 | 0 | No retired mark appeared in this broad-query sample |

## First-20 source inventory

| Rank | Source | Relationship | Logo observation | Required action |
|---:|---|---|---|---|
| 1 | [LifeUSA homepage](https://www.lifeusa.org/) | Owned | Current mark | Keep; strengthen canonical logo signals |
| 2 | [LifeUSA media page](https://www.lifeusa.org/media) | Owned | Current mark | Keep; align image metadata |
| 3 | [LifeUSA International](https://lifeusa.international/) | Unrelated language school | Different organization and mark | Exclude from correction campaign |
| 4 | [LifeUSA homepage](https://www.lifeusa.org/) | Owned | Current horizontal mark | Keep; use one canonical asset URL |
| 5 | [LifeUSA homepage](https://www.lifeusa.org/) | Owned | Current event imagery | No removal action |
| 6 | [LifeUSA about page](https://www.lifeusa.org/about) | Owned | Current mark in program imagery | No removal action |
| 7 | [Lebanon emergency relief](https://www.lifeusa.org/lebanon-emergency-relief) | Owned | Current mark | No removal action |
| 8 | [33-year anniversary article](https://www.lifeusa.org/post/building-a-better-world-for-33-years) | Owned | Current brand family | No removal action |
| 9 | [Official Instagram profile](https://www.instagram.com/life4relief/) | Official social | Current mark | Keep profile image and canonical website aligned |
| 10 | [LifeUSA International](https://lifeusa.international/) | Unrelated language school | Different organization and mark | Exclude from correction campaign |
| 11 | [LifeUSA International](https://lifeusa.international/) | Unrelated language school | Different organization and mark | Exclude from correction campaign |
| 12 | [eBay prayer-card listing](https://www.ebay.com/itm/267626351569) | Third-party marketplace | Current LifeUSA mark on donation cards | Monitor only; not a retired-logo source |
| 13 | [Official Instagram post](https://www.instagram.com/p/DYCx5sVGgfD/) | Official social | Current mark | No removal action |
| 14 | [LifeUSA homepage](https://www.lifeusa.org/) | Owned | Current mark | No removal action |
| 15 | [LifeUSA Online](https://lifeusaonline.com/) | Unrelated language-product business | Different organization and mark | Exclude from correction campaign |
| 16 | [Official Instagram profile](https://www.instagram.com/life4relief/) | Official social | Current mark | Keep aligned |
| 17 | [eBay prayer-card listing](https://www.ebay.com/itm/267626351569) | Third-party marketplace | Current LifeUSA mark on donation cards | Monitor only; duplicate source |
| 18 | [Official Linktree](https://linktr.ee/LIFEUSA) | Official social directory | Current brand family | Keep official destinations and avatar aligned |
| 19 | [Gaza relief page](https://www.lifeusa.org/gaza) | Owned | Current mark | No removal action |
| 20 | [Official Instagram post](https://www.instagram.com/p/DYCx5sVGgfD/) | Official social | Current mark | No removal action |

## Owned-site signal audit

The live homepage was rechecked on July 15, 2026.

| Signal | Live value | Finding | Correction specification |
|---|---|---|---|
| Visible header logo | Wix asset `6df904_1fd130d48c554b8c8109e6acd206c435` | Current horizontal mark, 4101 x 1201 source | Retain as horizontal master candidate; publish under a stable owned brand URL |
| `NGO.logo` | Wix asset `6df904_2bb6857d9c8b49ae91789ad75efbc8b8` | Current white-on-transparent variant, 4250 x 2514; weak on white surfaces | Replace with a colored square logo that stays visible on white |
| Favicon source | Wix asset `6df904_3ba0b63af7e945f0a92fbe9978934569` | Current blue square mark, 1800 x 1800 source | Used as the verified source for the dedicated official square upload |
| Wix Business Profile logo | Wix asset `af2a6c_49a4190c354746b493c123d311222fb5` | Current square mark, 1800 x 1800; assigned July 15 | Complete; use this official asset for corrections and remaining owned signals |
| Canonical horizontal Wix file | Wix asset `af2a6c_1bd1137d792b44c3855d26ee4cfcced0` | Current horizontal mark, 4101 x 1201; uploaded and checksum-verified July 15 | Complete; use this official asset for wide placements |
| `NGO.@id` | Missing | Entity graph lacks a stable identifier | Add `https://www.lifeusa.org/#organization` |
| `NGO.sameAs` | Missing | Official profiles are not connected from the entity node | Add only verified official LifeUSA profile URLs |
| `WebSite` nodes | Two separate nodes | Duplicated website identity | Consolidate if Wix permits |
| Open Graph image | Program photograph | Appropriate for sharing, but not a canonical logo | Keep separate from `NGO.logo` |

The current square source was uploaded to the LifeUSA Wix Media Manager and assigned to the site's Business Profile logo field on July 15. The current horizontal source was uploaded to the same owned Media Manager, and its remote checksum exactly matches the approved local source. Both dedicated Wix URLs are live. The custom homepage `NGO.logo` still points to the separate white asset and remains a distinct editor-only correction task.

## Confirmed live retired-logo sources

The following three source pages and direct files were rechecked on July 15, 2026. All three still return and display the retired crescent mark.

| Source | Direct image | Dimensions | Source state | Next action |
|---|---|---:|---|---|
| [Old LifeUSA WordPress site](https://lifeusaorg.wordpress.com/where-we-are/) | [Retired WordPress logo](https://lifeusaorg.files.wordpress.com/2015/05/life-logo-hd_white.png) | 1500 x 1500 | Live | Recover ownership; replace/delete the file or retire the archive |
| [Kids That Do Good](https://kidsthatdogood.com/causes/life-relief-development/) | [Retired profile logo](https://kidsthatdogood.com/wp-content/uploads/2019/06/life-for-relief-and-development-logo.png) | 200 x 200 | Live | Send a correction request with the canonical square asset |
| [Arab Info Mall](https://arabinfomall.bibalex.org/En/Index.aspx?orgid=879&sectionid=1) | [Retired organization logo](https://arabinfomall.bibalex.org/Attachments/Logos/10751.gif) | 200 x 200 | Live | Request a full profile correction or removal |

These sources do not appear in the broad-query first 20 captured above, but they remain discoverable public files and therefore remain valid correction targets.

## Source-level decision

- Do not contact or attempt to suppress unrelated same-name businesses.
- Do not ask Google to remove current, accurate LifeUSA imagery.
- Correct the three retired-logo sources at the publisher or account level first.
- Publish a colored canonical square asset and reference the same stable URL from the homepage `NGO` structured data.
- Request recrawling or outdated-content refresh only after the source change is verified live.

## Execution packages

- [Wix implementation specification](wix-implementation-spec.md): stable asset contract, corrected NGO markup, website-node cleanup, and acceptance checklist.
- [Publisher correction pack](publisher-correction-pack.md): ready-to-review drafts and acceptance checks for the three verified retired-logo sources.
- [Wix owned-logo change log](wix-owned-logo-change-log.md): before-and-after proof for the Media Manager upload and Business Profile logo assignment.

## Evidence asset checksums

| File | SHA-256 |
|---|---|
| `current-square-favicon-source.png` | `d3d830b08effb1202b1ded8bc26bec91f78dfb8b89c97ef59f892b2ea88a77cb` |
| `current-schema-logo-white-transparent.png` | `bb30a770e4970eb0f206a3aac09e21af8fdfbd1d01c26c99b52c04260d9106d1` |
| `retired-wordpress-logo.png` | `281840637b1241b09371d2c0adf19d4a7b683fbc8683d0af39e4ad42afc66850` |
| `retired-kids-that-do-good-logo.png` | `007d9b603111684bd0142feb1dae5e41ce144e500d68bbc1ea6af14051f4e26f` |
| `retired-arab-info-mall-logo.gif` | `9296fe04f8808f906310433494959417a290d2933d5603362e40e25fce3bcb88` |
