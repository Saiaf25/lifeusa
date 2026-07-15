# LifeUSA authority and social profile logo audit

Captured July 15, 2026. The approved current identity is the yellow-ray logo used on `lifeusa.org` and the official English Linktree avatar. This audit distinguishes that current identity from both the retired crescent mark and the later blue-globe Life mark.

## Executive finding

The mixed Google signal is broader than the three retired-crescent pages. Candid/GuideStar, GreatNonprofits, LinkedIn, the main English Facebook page, Instagram, YouTube, and X all still expose the older blue-globe Life logo as their profile image. The English Linktree avatar is current, but its Facebook button points to a Somali-language page instead of the main English page; that Somali page also uses the older blue-globe logo.

Charity Navigator and ReliefWeb contain current Life for Relief and Development organization information but do not expose a LifeUSA logo in their public profile markup. They are profile-enhancement targets, not stale-logo sources.

## Profile matrix

| Surface | Verified public URL | Logo state on July 15 | Evidence | Required action |
|---|---|---|---|---|
| Candid / GuideStar | `https://www.guidestar.org/profile/95-4402149` | Older blue-globe logo | `legacy-blue-candid-guidestar-logo.png`, 1500 by 1500 | Replace through the claimed Candid nonprofit profile and verify the public image |
| GreatNonprofits | `https://greatnonprofits.org/org/life-for-relief-and-development` | Older blue-globe logo | `legacy-blue-greatnonprofits-logo.png`, 266 by 266 | Replace through the nonprofit account or GreatNonprofits support |
| LinkedIn | `https://www.linkedin.com/company/life-for-relief-and-development/` | Older blue-globe logo | `legacy-blue-linkedin-logo.jpg`, 200 by 200 | Update the company profile photo in LinkedIn Page administration |
| Facebook, English | `https://www.facebook.com/Life4ReliefEN/` | Older blue-globe logo | `legacy-blue-facebook-english-logo.jpg`, 720 by 720 | Replace the main English Page profile image |
| Facebook, Somali | `https://www.facebook.com/profile.php?id=61563961181765` | Older blue-globe logo; incorrectly linked from the English Linktree | `legacy-blue-facebook-somali-logo.jpg`, 720 by 720 | Update the Somali Page image and repair the English Linktree destination |
| Instagram | `https://www.instagram.com/life4relief/` | Older blue-globe logo | `legacy-blue-instagram-logo.jpg`, 100 by 100 public preview | Replace the profile photo and verify the logged-out preview |
| YouTube | `https://www.youtube.com/channel/UCRTkW2TMw344eC562GSK1nA` | Older blue-globe logo | `legacy-blue-youtube-logo.jpg`, 900 by 900 | Replace the channel picture in YouTube Studio |
| X | `https://x.com/LIFEforRELIEF` | Older blue-globe logo | `legacy-blue-x-logo.jpg`, 400 by 400 | Replace the profile image and verify the public preview |
| Linktree, English | `https://linktr.ee/LIFEUSA` | Current yellow-ray logo family | `lifeusa-official-social-avatar.png`, 1000 by 1000 | Keep the avatar; repair its Facebook destination |
| TikTok | `https://www.tiktok.com/@life4relief.usa` | Public profile image could not be read in the logged-out browser | Official Linktree destination verified | Check while signed in and replace if it is not the current square mark |
| Threads | `https://www.threads.com/@life4relief` | Public profile redirected to login | Official Linktree destination verified | Check while signed in and replace if it is not the current square mark |
| Charity Navigator | `https://www.charitynavigator.org/ein/954402149` | Correct organization profile; no LifeUSA logo exposed | Four-Star, 94%, EIN 95-4402149; profile marked managed by nonprofit | Add or refresh the logo only if the managed profile permits it |
| ReliefWeb | `https://reliefweb.int/organization/life` | Active organization profile; no LifeUSA logo exposed | 180 published reports; profile homepage still uses `http://www.lifeusa.org` | Change the homepage to HTTPS and add the current logo if ReliefWeb supports it |

## Stable third-party image sources

- Candid image: `https://docs.candid.org/edoc/11078205`
- GreatNonprofits image: `https://cdn.greatnonprofits.org/images/logos/org_logo_513389_1711518504.png`

Checksums:

- Candid / GuideStar: `f440247655ec4a13196be3ee40b291c361de42e596a05941395fc22dd42b6328`
- GreatNonprofits: `2d1de086aa753d889f32d05b3fabc232e76f1fe16f4c9a4ad0f64f6d67108117`

Social platforms use temporary CDN URLs, so the downloaded files above are the dated evidence copies. The durable references are the profile URLs in the matrix.

## Official social identity destinations

The English Linktree publicly associates LifeUSA with these destinations:

- Facebook: currently points to the Somali-language page and must be corrected to the intended English destination
- Instagram: `https://instagram.com/life4relief`
- TikTok: `https://tiktok.com/@life4relief.usa`
- YouTube: `https://www.youtube.com/channel/UCRTkW2TMw344eC562GSK1nA`
- X: `https://x.com/LIFEforRELIEF`
- Threads: `https://www.threads.com/@life4relief`
- LinkedIn: `https://www.linkedin.com/company/life-for-relief-and-development`

## Correction order

1. Replace the profile photos on the controlled English social accounts: Facebook, Instagram, LinkedIn, YouTube, and X.
2. Repair the English Linktree Facebook destination and update the Somali Facebook logo.
3. Replace Candid/GuideStar and GreatNonprofits through the organization-controlled profiles or support routes.
4. Check TikTok and Threads while signed in and normalize them if needed.
5. Update ReliefWeb's homepage URL to HTTPS and add a logo where supported.
6. Recheck every profile logged out, capture the new public image, then request Google recrawling only after the source changes are live.

## Acceptance rule

A profile is not complete when an administrator uploads a file. It is complete only when the logged-out public URL exposes the current yellow-ray square mark, the old direct image is no longer referenced, and a dated verification is stored.
