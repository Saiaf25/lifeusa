# LifeUSA authority and social profile logo audit

Captured July 15, 2026, with the classification corrected July 19. The yellow-ray logo used on `lifeusa.org` is the preferred canonical asset. The client confirmed that the blue-globe Life logo used on Facebook is an acceptable current variant. The retired crescent mark remains the obsolete logo family.

## Executive finding

The three retired-crescent pages remain correction targets. Candid/GuideStar, GreatNonprofits, LinkedIn, the main English Facebook page, Instagram, YouTube, X, and Somali Facebook expose the acceptable current blue-globe variant. Those images are not stale-logo sources and do not require replacement for correctness. The English Linktree avatar is canonical, but its Facebook button points to a Somali-language page instead of the main English page; that destination mismatch remains actionable.

Charity Navigator and ReliefWeb contain current Life for Relief and Development organization information but do not expose a LifeUSA logo in their public profile markup. They are profile-enhancement targets, not stale-logo sources.

## Profile matrix

| Surface | Verified public URL | Logo state on July 15 | Evidence | Required action |
|---|---|---|---|---|
| Candid / GuideStar | `https://www.guidestar.org/profile/95-4402149` | Acceptable current blue-globe variant | `legacy-blue-candid-guidestar-logo.png`, 1500 by 1500; filename retained as historical evidence label | Keep or optionally standardize; verify website and organization details |
| GreatNonprofits | `https://greatnonprofits.org/org/life-for-relief-and-development` | Acceptable current blue-globe variant | `legacy-blue-greatnonprofits-logo.png`, 266 by 266; filename retained as historical evidence label | Keep; verify website and social links |
| LinkedIn | `https://www.linkedin.com/company/life-for-relief-and-development/` | Acceptable current blue-globe variant | `legacy-blue-linkedin-logo.jpg`, 200 by 200; filename retained as historical evidence label | Keep or optionally standardize after separate approval |
| Facebook, English | `https://www.facebook.com/Life4ReliefEN/` | Acceptable current blue-globe variant | `legacy-blue-facebook-english-logo.jpg`, 720 by 720; filename retained as historical evidence label | Keep; verify About links |
| Facebook, Somali | `https://www.facebook.com/profile.php?id=61563961181765` | Acceptable current blue-globe variant; incorrectly linked from the English Linktree | `legacy-blue-facebook-somali-logo.jpg`, 720 by 720; filename retained as historical evidence label | Keep the logo; repair the English Linktree destination |
| Instagram | `https://www.instagram.com/life4relief/` | Acceptable current blue-globe variant in July 15 evidence | `legacy-blue-instagram-logo.jpg`, 100 by 100 public preview; filename retained as historical evidence label | Keep or optionally standardize; verify logged out when available |
| YouTube | `https://www.youtube.com/channel/UCRTkW2TMw344eC562GSK1nA` | Acceptable current blue-globe variant | `legacy-blue-youtube-logo.jpg`, 900 by 900; filename retained as historical evidence label | Keep or optionally standardize after separate approval |
| X | `https://x.com/LIFEforRELIEF` | Acceptable current blue-globe variant | `legacy-blue-x-logo.jpg`, 400 by 400; filename retained as historical evidence label | Keep or optionally standardize after separate approval |
| Linktree, English | `https://linktr.ee/LIFEUSA` | Current yellow-ray logo family | `lifeusa-official-social-avatar.png`, 1000 by 1000 | Keep the avatar; repair its Facebook destination |
| TikTok | `https://www.tiktok.com/@life4relief.usa` | Public profile image could not be read in the logged-out browser | Official Linktree destination verified | Check while signed in; change only if it uses the retired crescent mark or optional standardization is approved |
| Threads | `https://www.threads.com/@life4relief` | Public profile redirected to login | Official Linktree destination verified | Check while signed in; change only if it uses the retired crescent mark or optional standardization is approved |
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

## Correction and enhancement order

1. Repair the English Linktree Facebook destination.
2. Verify website, mission, and contact fields on Candid/GuideStar, GreatNonprofits, LinkedIn, Facebook, Instagram, YouTube, and X; keep the acceptable blue-globe variant unless optional standardization is separately approved.
3. Check TikTok and Threads while signed in and classify their logos using the three-state model.
4. Update ReliefWeb's homepage URL to HTTPS and add the canonical logo where supported.
5. Recheck every changed profile logged out and capture the public result before requesting any Google recrawl.

## Acceptance rule

A profile is complete when the logged-out public URL exposes either approved current logo variant, links to the correct canonical website, contains accurate identity details, and has a dated verification. New profiles should use the canonical yellow-ray square. A matching blue-globe variant on an existing profile is not a blocker.
