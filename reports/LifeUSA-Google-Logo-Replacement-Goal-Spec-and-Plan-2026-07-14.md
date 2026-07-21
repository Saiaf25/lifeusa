# LifeUSA Google Logo Replacement Goal Specification and Execution Plan

**Status:** Execution in progress
**Prepared:** 2026-07-14
**Executive sponsor:** Dr. Hany Saqr
**SEO lead:** Saiaf Gamal
**Scope:** Replace or suppress the retired LifeUSA logo across Google-controlled surfaces and the public sources that Google can discover, while strengthening the new logo as the canonical brand asset.

## Execution update: July 15, 2026

- A reproducible `LifeUSA` Google Search and Google Images baseline is published on the live status page.
- The first 20 Google Images source links were inventoried: 14 official LifeUSA results, four unrelated same-name business results, two current-branded marketplace results, and zero retired crescent marks in this exact broad-query sample.
- The old WordPress site, Kids That Do Good, and Arab Info Mall were rechecked directly. All three still serve the retired crescent logo from live public image URLs.
- The homepage logo signals were rechecked. The visible header, `NGO.logo`, and favicon still use three Wix assets. The `NGO.logo` file is white-on-transparent, while the current favicon source provides a stronger 1800 x 1800 colored square candidate.
- The `NGO` node still lacks `@id` and `sameAs`, and the homepage still emits two `WebSite` nodes.
- The verified 1800 x 1800 current square logo was uploaded directly to the published LifeUSA Wix site and assigned to the previously empty Wix Business Profile logo field. The before-and-after Site Properties versions are recorded.
- A post-change live homepage check confirmed that the separate custom `NGO.logo` value did not change, so its white-logo replacement remains an independent Wix SEO task.
- Source evidence, first-20 Markdown and CSV inventories, dimensions, checksums, and the three retired-logo files are stored under `technical-seo-fixes/google-logo-replacement-status/evidence/2026-07-15/`.

The broad top 20 is healthier than the older targeted-query sample, but the campaign is not complete because the retired source files remain live and the owned canonical logo signal is not yet consolidated.

## Executive decision

The directory and third-party profile campaign is an active solution track, but it should not run alone. The fastest credible approach is a coordinated five-track program:

1. Fix the canonical logo signals on `lifeusa.org`.
2. Remove or replace the retired logo at the specific pages and image URLs that still publish it.
3. Update Google-owned surfaces separately: Business Profile, Knowledge Panel if present, favicon/Search, Search Console, and Google Ads if used.
4. Align high-trust, already-indexed nonprofit and social profiles with one approved logo package.
5. Create a controlled set of new, genuine-fit nonprofit, giving, humanitarian, volunteer, and local-business profiles that publish the canonical logo and link to `https://www.lifeusa.org/`.

Google does not provide a single switch that forces one logo everywhere. Its systems select images from the owned website, public web sources, verified Google properties, and direct feedback. The campaign can make the new logo overwhelmingly clearer and more consistent, but it cannot promise a particular image position or a fixed completion date.

The highest-priority defect is on the owned website. The homepage `NGO` structured data currently points to a large white-on-transparent logo. Google says an Organization logo should look correct on a purely white background. This asset becomes effectively invisible on white. The visible header, structured-data logo, and favicon also use three different files, and the `NGO` node has no `sameAs` links to official profiles.

At the same time, a US-located Google Images research snapshot on 2026-07-14 found the retired crescent logo among the first ten image results from at least three live sources: the old WordPress site, Kids That Do Good, and Arab Info Mall. Therefore, both promotion of the current logo and source-level cleanup of the retired logo are necessary.

## 1. Zoho Mail brief

### What Dr. Hany asked for

Source: authorized LifeUSA Zoho Mail thread
Thread: `LifeUSA | Article Planning and Publishing | Ongoing Thread`
Date: 2026-07-05

Dr. Hany reported that a LifeUSA logo retired about ten years ago still appears on the first page of what he called “Google Photos.” He asked whether it can be removed. Saiaf replied that he would investigate the cause, possible fixes, completed actions, and expected timing.

### Evidence limits

- The email contains no screenshot of the Google results.
- Its two inline images are email-signature graphics, not screenshots of the problem.
- “Google Photos” may mean Google Images, a Business Profile photo carousel, a Knowledge Panel image, a search-result favicon, or another Google surface.
- The first execution gate must capture the exact query, country, device, result URL, and visual location Dr. Hany saw.

## 2. Goal specification

### Goal statement

Make the approved current LifeUSA logo the clearest, most consistent, and most authoritative visual identity across LifeUSA-owned web properties, Google-controlled surfaces, and high-trust third-party profiles, while removing or suppressing the retired crescent logo from branded Google results wherever LifeUSA has control or a legitimate correction path.

### Business outcome

Donors, partners, media, employees, and searchers should see a current and consistent LifeUSA identity when they search the organization by name.

### Target outcome

Within a 90-day monitoring window after implementation:

- The retired crescent logo is absent from the top 20 Google Images results for the approved branded query set in three consecutive weekly US checks.
- No retired logo is used as the featured image, logo, or favicon in LifeUSA’s branded Google Search, Maps, Business Profile, Knowledge Panel, or eligible paid-search presentation.
- Every LifeUSA-controlled website and Tier 1 profile uses either the canonical current logo or an approved current variant.
- Every confirmed retired-logo source is either corrected, removed, blocked from Google Images, or recorded as an unresolved third-party dependency with proof of outreach.

These are campaign targets, not guarantees about Google’s algorithm.

### Non-goals

- Do not claim that directory submissions directly force Google to select a logo. Google does not document such a guarantee.
- Do not create dozens of low-quality directory listings. New placements must pass the relevance, logo, website-link, public-verification, and human-approval checks in the directory expansion plan.
- Do not submit removal requests before the source image has actually been removed, replaced, or made unavailable.
- Do not report an accurate but old third-party photo as a policy violation unless it genuinely violates that platform’s policy.
- Do not launch paid ads as if they can repair organic Google Images or Knowledge Panel results. Paid assets affect ads only.
- Do not manufacture a “rebrand announcement” for a logo that changed roughly ten years ago.

## 3. Success metrics

### Primary outcome metrics

| Metric | Target | Evidence |
|---|---:|---|
| Retired logo in top 20 Google Images results | 0 for 3 consecutive weekly checks | Dated desktop and mobile screenshots plus source URLs |
| Retired logo on Google Search, Maps, Business Profile, or Knowledge Panel | 0 | Dated screenshots from a US, signed-out baseline |
| LifeUSA-controlled surfaces using approved logo | 100% | URL and screenshot registry |
| Tier 1 profiles using approved logo | 100% | Profile URL and screenshot |
| Tier 2 confirmed old-logo sources corrected or removed | At least 80%; all others documented | Source status and outreach proof |

### Leading indicators

- One preferred canonical square logo and one preferred canonical horizontal logo for new placements, with documented acceptable current variants.
- Canonical square logo URL returns `200`, is crawlable, indexable, and visible on white.
- Homepage Organization/NGO markup passes validation and points to that canonical image.
- `sameAs` contains only verified official LifeUSA profiles.
- Favicon, header, footer, Open Graph, and social-profile imagery use the same brand family.
- Search Console URL Inspection confirms Google can access the homepage and canonical logo.
- Old owned image URLs return the intended removal state or are blocked specifically from Google Images.
- Google Ads business assets, if used, are approved and record impressions with the current logo.

### Monitoring query set

Run on signed-out US desktop and mobile, with location and date recorded:

- `Life for Relief and Development`
- `Life for Relief and Development logo`
- `Life USA charity`
- `Life USA Southfield`
- `Life for Relief and Development Southfield Michigan`
- `site:lifeusa.org Life for Relief and Development logo`
- Reverse image checks for each confirmed retired-logo URL

## 4. Current-state findings

### 4.1 Owned website signals

Homepage checked: [lifeusa.org](https://www.lifeusa.org/)

| Signal | Current state | Risk | Priority |
|---|---|---|---:|
| Organization type | `NGO` JSON-LD | Appropriate subtype, but the entity node is incomplete | P1 |
| Structured-data logo | `https://static.wixstatic.com/media/6df904_2bb6857d9c8b49ae91789ad75efbc8b8~mv2.png` | White-on-transparent, 4250 x 2514, visually disappears on white | P0 |
| Visible header logo | Different Wix asset: `6df904_1fd130d48c554b8c8109e6acd206c435~mv2.png` | Competing variant and URL | P1 |
| Favicon | Different square Wix asset: `6df904_3ba0b63af7e945f0a92fbe9978934569~mv2.png` | Brand family is related, but the source of truth is fragmented | P1 |
| `sameAs` | Missing from the `NGO` node | Google receives no explicit entity links from this markup | P1 |
| Stable entity `@id` | Missing | Harder to connect the organization node consistently across pages | P1 |
| `WebSite` JSON-LD | Two separate `WebSite` nodes | Unnecessary duplication and weaker graph clarity | P2 |
| Open Graph image | A program/photo image rather than a logo | Fine for social sharing, but it should not be mistaken for the canonical logo | P2 |

[Google’s Organization guidance](https://developers.google.com/search/docs/appearance/structured-data/organization) says the logo image must be crawlable and indexable, at least 112 x 112, and look correct on a purely white background. It also states that structured data can influence visual elements but does not guarantee display.

### 4.2 Confirmed retired-logo sources

| Source | Evidence observed on 2026-07-14 | Control path | Priority |
|---|---|---|---:|
| [Old LifeUSA WordPress site](https://lifeusaorg.wordpress.com/where-we-are/) | Active 2015-era site with title “24 Years Serving Humanity”; retired crescent logo at `https://lifeusaorg.files.wordpress.com/2015/05/life-logo-hd_white.png` | Recover WordPress ownership; replace branding and delete old media, or make archive private if approved | P0 |
| [Kids That Do Good](https://kidsthatdogood.com/causes/life-relief-development/) | Live LifeUSA profile uses a 200 x 200 retired crescent logo | Claim or contact publisher from a `lifeusa.org` address; replace asset and request old file removal | P0 |
| [Arab Info Mall](https://arabinfomall.bibalex.org/En/Index.aspx?orgid=879&sectionid=1) | Live profile uses the retired crescent logo and contains stale contact data | Request a full profile correction or removal | P0 |
| Glassdoor | Image result exposes an indexed company-logo URL; visual recheck required before classification | Employer Center/admin access or support request | P1 |
| ShareDetroit | Image result exposes an indexed profile image; visual recheck required | Profile owner or publisher support | P1 |

### 4.3 Confirmed current-logo sources

| Source | Current state | Action |
|---|---|---|
| [GreatNonprofits](https://greatnonprofits.org/org/life-for-relief-and-development) | Uses a current blue globe logo variant | Keep; align to the final approved square master if necessary |
| [Charity Navigator](https://www.charitynavigator.org/ein/954402149) | Profile is marked as managed by the nonprofit | Use the Nonprofit Portal to verify logo and all general information |
| [LinkedIn](https://www.linkedin.com/company/life-for-relief-and-development) | Existing official company page | Verify current logo and official website link |
| [Facebook](https://www.facebook.com/Life4ReliefEN/) | Existing official page indexed for the organization | Verify profile image and About links |
| [ReliefWeb](https://reliefweb.int/organization/life) | Existing authoritative humanitarian organization page | Verify logo and canonical site link; request correction if needed |

### 4.4 Current logo classification decision, July 19

The blue-globe logo used on the English Facebook page is an **acceptable current variant**, not an outdated or retired logo. Matching blue-globe files on Candid/GuideStar, GreatNonprofits, LinkedIn, Instagram, YouTube, X, Somali Facebook, Google Ads, or Maps are likewise acceptable when visual comparison confirms that they are the same approved variant. They may be changed to the canonical yellow-ray square for consistency, but their presence is not a source defect and does not block campaign completion.

The retired crescent mark remains the only confirmed obsolete logo family in this program. New directory placements should use the canonical yellow-ray square to strengthen a consistent forward-looking signal.

### 4.5 Important interpretation

The retired logo is not merely “cached by Google.” Multiple live webpages still publish it. Google is correctly discovering those source files. Search cleanup will be durable only after those sources are changed or the current logo becomes a stronger and more consistent result.

## 5. Canonical brand asset specification

LifeUSA should approve one brand kit before any edits begin.

### Required master files

| Asset | Specification | Main use |
|---|---|---|
| Canonical square logo | 1200 x 1200 PNG, opaque white or approved light background, current blue/yellow mark, no tiny tagline | Organization markup, Business Profile, Google Ads, directories |
| Square transparent logo | 1200 x 1200 PNG with transparent background | Platforms that supply their own background |
| Horizontal full logo | High-resolution PNG and SVG, current mark plus approved organization name/tagline | Website header, media kit, partner use |
| Favicon set | 48, 96, 192, and 512 px square PNG plus ICO where supported | Browser and Google Search favicon |
| Social preview | 1200 x 630 PNG or JPG with current brand | Open Graph and link sharing |
| Source vectors | SVG, EPS, or PDF master | Future production and resizing |

### Canonical URL rules

- Publish assets from an owned, stable, public LifeUSA URL, ideally under `https://www.lifeusa.org/brand/`.
- Recommended primary URL: `https://www.lifeusa.org/brand/lifeusa-official-logo-square.png`.
- Do not use a white-on-transparent file as the Organization logo.
- Do not overwrite the URL during this project after Google starts crawling it.
- Use descriptive filenames and `alt="Life for Relief and Development official logo"`.
- Add a visible HTML brand page that states the organization’s legal/public name, official website, contact details, and approved current logo downloads.
- Do not display the retired crescent logo on the public brand page. A text note can say that legacy marks are no longer approved.
- Record file dimensions, MIME type, last update, source owner, and checksum in a brand asset register.

[Google Image SEO guidance](https://developers.google.com/search/docs/appearance/google-images) supports high-quality images, descriptive context, standard HTML image elements, stable URLs, and representative image metadata. [Google’s image sitemap guidance](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps) can help Google discover images, including CDN-hosted files when the relevant domains are verified in Search Console.

## 6. Strategy by Google surface

### 6.1 Google Images

**Objective:** Remove the old asset at its sources and make the canonical current logo the strongest branded image.

Actions:

1. Capture the exact old image result URL and its landing page for every branded query.
2. For LifeUSA-controlled pages, delete or replace the old media and confirm the old file’s response.
3. For old images that must remain accessible but should not appear in Google Images, use an image-specific `X-Robots-Tag: noindex` or a `Googlebot-Image` rule when technically possible.
4. Publish the canonical current logo on the brand page and reference the same URL in Organization markup.
5. Add the canonical logo to an image sitemap if Wix or the technical stack permits it.
6. Request recrawling of the homepage and brand page.
7. Use Search Console Removals for owned URLs when rapid temporary hiding is necessary.
8. Use Refresh Outdated Content for third-party URLs only after the source image is gone or materially changed.

[Google’s owned-image removal guidance](https://developers.google.com/search/docs/crawling-indexing/prevent-images-on-your-page) documents emergency removal, `Googlebot-Image` blocking, and `X-Robots-Tag: noindex`. [Search Console Removals](https://support.google.com/webmasters/answer/9689846?hl=en) is temporary for roughly six months unless the source is permanently changed. [Refresh Outdated Content](https://support.google.com/webmasters/answer/7041154?hl=en) is for pages or images not owned by the requester that no longer exist or materially changed, not for content that remains live.

### 6.2 Organic Search logo and Organization entity

**Objective:** Give Google one strong, machine-readable organization identity.

Recommended homepage graph:

- One `NGO` node with `@id: https://www.lifeusa.org/#organization`.
- `name: Life for Relief and Development`.
- Approved `alternateName` values only, such as `LIFE` and `Life USA`, after client confirmation.
- Canonical `url` with one hostname convention.
- `logo` as an `ImageObject` with the canonical square URL, width, and height.
- Current address, telephone, email, founding date, tax identifier where appropriate, and nonprofit identifiers.
- `sameAs` for verified official profiles only.
- One `WebSite` node connected to the organization node.

Validate with Google’s Rich Results Test, Schema Markup Validator, live HTML inspection, and Search Console URL Inspection.

[Schema.org](https://schema.org/Organization) defines `logo` as an associated logo and [`sameAs`](https://schema.org/sameAs) as a URL that unambiguously identifies the same entity. These properties clarify identity; they do not force Google’s presentation.

### 6.3 Favicon in Google Search

**Objective:** Ensure the favicon is visibly part of the same approved brand system.

Actions:

- Use a square, high-contrast favicon that remains recognizable at small sizes.
- Confirm the homepage and favicon are crawlable by Googlebot and Googlebot-Image.
- Keep a stable favicon URL during the campaign.
- Request homepage recrawl after publishing.
- Monitor over several weeks.

[Google’s favicon guidance](https://developers.google.com/search/docs/appearance/favicon-in-search) requires a square favicon, recommends a size larger than 48 x 48, and notes that recrawling can take several days to several weeks.

### 6.4 Google Business Profile and Maps

**Objective:** Replace the profile logo and clean the profile’s photo inventory.

Actions:

1. Confirm whether the Southfield Business Profile is verified and who owns it.
2. Upload or change the logo to the approved square asset.
3. Set a current cover photo, understanding Google may choose another image.
4. Delete owner-uploaded retired-logo media.
5. For customer-uploaded images, report only policy violations. An image being old is not automatically a violation.
6. Align name, website, phone, address, hours, and category with the owned website.
7. Save before-and-after screenshots and photo IDs.

[Google Business Profile photo management](https://support.google.com/business/answer/6103862?hl=en) allows a verified owner to add or change a logo and remove owner media, but says a selected cover is not guaranteed to appear first. [Photo guidelines](https://support.google.com/business/answer/6123536?hl=en) recommend JPG or PNG, 10 KB to 5 MB, 720 x 720, with a 250 x 250 minimum. [Customer-photo reporting](https://support.google.com/business/answer/6130451?hl=en) is limited to policy problems and may take several business days.

### 6.5 Knowledge Panel and Knowledge Graph

**Objective:** Claim the organization panel if it exists and submit a supported current-image correction.

Actions:

1. Determine whether the branded result is an Organization Knowledge Panel or a local Business Profile.
2. If claimable, verify through an official property such as Search Console, YouTube, Facebook, or X.
3. If an image already exists, submit a direct public image URL for the canonical square logo.
4. Explain that the current selection is a retired mark and cite the official brand page plus consistent official profiles.
5. Submit one evidence-backed correction per item and retain confirmation emails.
6. If no image exists, do not promise Google will add one by request.

[Google explains](https://support.google.com/knowledgepanel/answer/9163198?hl=en) that panels are automatically generated from public and partner sources. [Verified representatives can suggest a featured-image replacement](https://support.google.com/knowledgepanel/answer/7534842?hl=en) using a direct, publicly accessible image URL when an image already exists. [Verification](https://support.google.com/knowledgepanel/answer/7534902?hl=en) may use Search Console, YouTube, Facebook, or X. Google reviews suggestions against other public information, which is why consistent third-party profiles matter.

### 6.6 Google Ads and possible paid bridge

**Objective:** If LifeUSA already uses Google Ads or Google Ad Grants, make paid branded results use the current logo while organic remediation continues.

This is optional and requires a separate approval gate.

Actions:

1. Audit advertiser verification and existing account-level, campaign-level, and dynamic business-logo assets.
2. Remove or pause any dynamic or uploaded retired-logo asset.
3. Upload the approved square logo at account and relevant campaign levels.
4. Complete advertiser verification. Use brand verification only if the approved name or logo does not match the verified legal name/domain and LifeUSA has the necessary trademark evidence.
5. If approved, run a tightly scoped US branded Search campaign or Ad Grants branded campaign for organization-name queries.
6. Use the official homepage or brand page and current business-name/logo assets.
7. Track asset approval, impressions, clicks, and actual logo serving.

[Google Ads business information](https://support.google.com/google-ads/answer/12497613?hl=en) supports manually uploaded business logos for Search and Performance Max, but assets are not guaranteed to serve. Google also states that organic-search logos use different crawling guidelines. Asset review can take up to two business days. [Brand verification](https://support.google.com/google-ads/answer/13819790?hl=en) typically takes about three days when required. [Performance Max brand guidelines](https://support.google.com/google-ads/answer/15829354?hl=en) control paid campaign assets only.

## 7. Directory and third-party campaign

### Operating principle

Prioritize existing, authoritative, relevant profiles that already rank for LifeUSA, then add a deliberate set of new genuine-fit profiles. Do not optimize for the number of submissions. Optimize for entity consistency, control, actual branded visibility, and a public canonical website link.

The researched platform list, qualification rules, official capability sources, costs, execution order, and per-placement acceptance fields are documented in [the logo directory and backlink expansion plan](../technical-seo-fixes/google-logo-replacement-status/evidence/2026-07-19/logo-directory-and-backlink-expansion-plan.md).

### Tier 0: Google-controlled surfaces

- Google Business Profile
- Organization/Knowledge Panel feedback
- Search Console
- Google Ads or Google Ad Grants, if active
- YouTube channel branding

### Tier 1: High-trust identity and nonprofit profiles

| Profile | Why it matters | Planned action |
|---|---|---|
| Candid/GuideStar | Nonprofit identity profile syndicated to many charitable sites | Claim or verify profile; update official logo, website, name, mission, contact, and social links |
| Charity Navigator | Highly visible donor-trust profile and currently managed by LifeUSA | Audit through Nonprofit Portal; align logo and general information |
| GreatNonprofits | Already indexed and uses an acceptable current blue-globe variant | Keep the acceptable variant; verify website and social links |
| ReliefWeb | Mission-relevant humanitarian authority | Verify logo, website, and organization description |
| LinkedIn | Official organization identity and a Knowledge Panel verification route | Update through super-admin access; align logo and website |
| Facebook | Existing official page and a Knowledge Panel verification route | Align profile image, About link, and naming |
| Instagram | Existing high-visibility brand profile | Align profile image, biography, and canonical website |
| YouTube | Google-owned identity surface and verification route | Update profile picture, banner, description, and site links |

[Candid’s claim process](https://candid.org/claim-nonprofit-profile/) supports updating a nonprofit profile, including organization identity, and states that Candid distributes profiles across many charitable sites. [Charity Navigator’s portal](https://intercom.help/charity-navigator/en/articles/8695464-the-nonprofit-portal-and-portal-representatives) allows approved nonprofit representatives to manage general profile information. [LinkedIn’s official instructions](https://www.linkedin.com/help/linkedin/answer/a1399545) allow a super admin to replace the Page logo. [YouTube Studio](https://support.google.com/youtube/answer/10456525) allows the channel profile picture to be updated across the channel, videos, and public actions.

### Tier 2: Confirmed old-logo sources and indexed secondary profiles

- Old LifeUSA WordPress site
- Kids That Do Good
- Arab Info Mall
- ShareDetroit
- Glassdoor
- Crunchbase
- DevelopmentAid
- Any additional first-20 Google Images landing page discovered during baseline capture

For each source, record:

- Profile or landing page URL
- Direct image URL
- Current visual classification: canonical current, acceptable current variant, retired, uncertain
- Organization control level
- Login or contact route
- Update request date
- Publisher response
- New image URL after replacement
- Old image HTTP status after replacement
- Google refresh/removal request ID
- Verification date

### Tier 3: New placements

Create a new profile only if it is:

- Relevant to donors, humanitarian organizations, employment, or nonprofit verification
- Claimable by LifeUSA
- Indexed for branded searches or strategically valuable on its own
- Able to show the official website and logo
- Free from spammy link-selling or mass-directory behavior

New low-value directory volume is explicitly out of scope.

Initial new-placement priorities are Every.org, PayPal Giving Fund, Benevity Causes, Idealist, VolunteerMatch, Apple Business Connect, and Bing Places. Google Business Profile, Candid/GuideStar, GreatNonprofits, Charity Navigator, ReliefWeb, Yelp, GlobalGiving, and Dun & Bradstreet are existing, conditional, or cost-sensitive routes that must be handled according to the detailed expansion plan. No listing, claim, application, membership, or paid upgrade may be executed without an exact human approval item.

## 8. Phased execution plan

### Phase 1: Understand the problem

Save the starting Google results, agree which logo versions are approved, and review the first 20 Google Images sources. This creates a clear before record.

### Phase 2: Fix the LifeUSA website

Create the official square and horizontal files, publish the Brand Resources page, fix the logo information on the homepage, and use approved logos in the header, footer, and browser icon.

### Phase 3: Remove retired logo sources

Correct the old WordPress site, Kids That Do Good, Arab Info Mall, and any other website that still publishes the retired crescent logo. Google refresh requests wait until these public sources change.

### Phase 4: Strengthen profiles and directories

Review nonprofit and social profiles, correct wrong links or missing details, and publish approved new directory profiles. Existing profiles must be updated through their owners rather than duplicated.

### Phase 5: Update Google after source fixes

Update the Southfield Business Profile when approved access is available, watch for a separate Knowledge Panel, check the LifeUSA Ads logo settings, and ask Google to recrawl only after source corrections are live.

### Phase 6: Optional paid support

Run a short branded Google Ads test only if LifeUSA separately approves the account, budget, and purpose. Paid visibility does not change normal Google Search or Images results.

### Phase 7: Monitor and close

Check Google and the priority sources every week. Close the program only after retired sources are corrected or accepted as documented exceptions and three consecutive scheduled checks show no regression.

## 9. Work breakdown structure

| ID | Work item | Owner role | Dependency | Evidence of completion |
|---|---|---|---|---|
| LOGO-001 | Capture exact CEO result | SEO lead + executive sponsor | CEO availability | Screenshot and result URL |
| LOGO-002 | Approve current and retired marks | Executive/brand approver | Source brand files | Signed asset decision |
| LOGO-003 | Produce canonical asset kit | Designer/brand owner | LOGO-002 | Asset register and files |
| LOGO-004 | Publish owned brand page | Wix administrator | LOGO-003 | Live page and `200` checks |
| LOGO-005 | Repair Organization/NGO markup | Wix administrator + SEO lead | LOGO-004 | Live JSON-LD and validation |
| LOGO-006 | Align favicon/header/footer | Wix administrator | LOGO-003 | Screenshots and source URLs |
| LOGO-007 | Remove old WordPress asset | WordPress owner | Ownership decision | Old URL state and page screenshot |
| LOGO-008 | Correct Kids That Do Good | Client communications | LOGO-003 | Publisher confirmation and new image |
| LOGO-009 | Correct Arab Info Mall | Client communications | LOGO-003 | Publisher confirmation and new profile |
| LOGO-010 | Audit full first-20 image source set | SEO lead | LOGO-001 | Source inventory |
| LOGO-011 | Update Business Profile | Google property owner | LOGO-003 | Profile screenshot and asset state |
| LOGO-012 | Claim/update Knowledge Panel | Verified representative | LOGO-004 | Claim state and feedback receipt |
| LOGO-013 | Submit indexing/removal requests | Search Console owner | Source changes live | Request IDs and status |
| LOGO-014 | Align Tier 1 profiles | Platform admins | LOGO-003 | URL and screenshot matrix |
| LOGO-015 | Audit and correct Tier 2 profiles | SEO lead + client communications | LOGO-010 | Resolution/outreach matrix |
| LOGO-016 | Audit Ads/Ad Grants assets | Ads admin | LOGO-003 | Asset report and verification state |
| LOGO-017 | Optional branded paid test | Ads admin | Separate approval | Campaign report |
| LOGO-018 | Weekly 12-week monitoring | SEO lead | Major updates live | Dated monitoring log |
| LOGO-019 | Publish approved new directory and business profiles | SEO lead + authorized profile administrators | Canonical asset kit and exact per-platform approval | Live profile, logo URL, canonical backlink, and logged-out screenshot |

## 10. Roles and approvals

| Role | Responsibility |
|---|---|
| Executive approver: Dr. Hany Saqr | Confirms the retired mark, approves the outcome, decides WordPress disposition and paid-campaign gate |
| Brand approver: to be named | Supplies and approves authoritative logo files and tagline rules |
| SEO lead: Saiaf Gamal | Baseline, source inventory, markup specification, removal routing, monitoring, and reporting |
| Wix administrator: to be named | Publishes brand assets and structured-data/site changes |
| Google property owner: to be named | Business Profile, Search Console, Knowledge Panel, YouTube, and account permissions |
| Social/profile administrators: to be named | LinkedIn, Facebook, Instagram, Candid, Charity Navigator, GreatNonprofits, ReliefWeb, and other profile updates |
| Ads administrator: to be named | Ads/Ad Grants verification, business information assets, and optional campaign |

## 11. Decision gates

### Gate A: What exactly did Dr. Hany see?

Choose one or more confirmed surfaces: Google Images, Business Profile, Knowledge Panel, favicon, paid ad, or other.

### Gate B: Which file is the official logo?

Approve the square master, horizontal master, tagline wording, background rules, and retired mark.

### Gate C: What should happen to the old WordPress site?

Options:

1. Modernize and retain it as an archive.
2. Make it private or retire it.
3. Keep selected historical content but remove all retired-logo media and add current branding.

Recommended: option 3 if the archive has useful links or history; otherwise option 2.

### Gate D: Is a paid branded campaign authorized?

Use an existing Google Ads or Ad Grants account only after verifying access, advertiser identity, and current logo assets. This is a bridge, not the organic fix.

### Gate E: Is public brand guidance authorized?

Recommended: publish an evergreen official brand-resources page. Do not publish a false “new rebrand” announcement.

## 12. Risks and controls

| Risk | Impact | Control |
|---|---|---|
| Google keeps an old image after source replacement | Delayed result | Verify old URL state, request refresh, monitor weekly |
| White logo is invisible on white | Google rejects or avoids it | Use approved colored square asset on a safe background |
| Undocumented variants are misclassified | Unnecessary profile changes and false blockers | Maintain a three-state register: canonical current, acceptable current variant, retired |
| Third party does not respond | Old result remains | Follow-up schedule, escalation contact, document exception, strengthen higher-authority sources |
| Business Profile user photo is old but not policy-violating | Removal request rejected | Add strong current owner media and report only genuine policy violations |
| Removal request submitted too early | Request rejected or image returns | Change source first, verify response, then submit |
| Ads show a dynamic old logo | Paid inconsistency | Audit, pause/remove dynamic assets, upload manual approved logo |
| Team mistakes ads for an organic fix | Wrong expectations | Separate paid and organic KPIs in reporting |
| Search results vary by location or personalization | Misleading progress | Use repeatable US signed-out desktop/mobile protocol |
| Mass directory submissions create spam | Brand and SEO risk | Use the expansion-plan qualification filter and exact per-platform approval |
| Access is split across former staff | Delays | Build access matrix before execution and assign named owners |

## 13. Timing expectations

| System | Reasonable planning expectation | Guarantee status |
|---|---|---|
| Google Ads asset review | Up to 2 business days in Google’s documentation | No serving guarantee |
| Google Ads brand verification | Typically about 3 days | Approval not guaranteed |
| Knowledge Panel feedback | Often reviewed within a few days, sometimes longer | Change not guaranteed |
| Business Profile customer-photo report | Several business days | Removal only for policy issues |
| Homepage/brand-page recrawl | A few days to a few weeks | Inclusion not guaranteed |
| Favicon recrawl | Several days to several weeks | Display not guaranteed |
| Google Images ranking replacement | Monitor at 1, 2, 4, 8, and 12 weeks | No fixed Google deadline |
| Third-party profile update | Platform-dependent | Controlled by publisher/access owner |

[Google’s recrawl guidance](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl) states that recrawling can take from a few days to a few weeks and repeated requests do not speed it up.

## 14. Reporting format

Every weekly status should contain:

1. Sources checked
2. Changes completed
3. Removal/indexing requests and IDs
4. Current top-20 image results
5. Google property state
6. Third-party replies and blockers
7. KPI movement
8. Next actions and named owners

Do not report “fixed” until the live result is verified. Distinguish:

- Source fixed
- Google refresh requested
- Google result changed
- Monitoring complete

## 15. Recommended first execution batch

After Gate A and Gate B are approved, execute this batch first:

1. Publish a colored square canonical logo and brand page on `lifeusa.org`.
2. Repair the `NGO` logo and entity graph.
3. Recover the old WordPress site and remove the 2015 retired-logo file.
4. Correct Kids That Do Good and Arab Info Mall.
5. Update Google Business Profile and confirm whether a Knowledge Panel exists.
6. Update Candid, Charity Navigator, LinkedIn, Facebook, Instagram, YouTube, GreatNonprofits, and ReliefWeb.
7. Request recrawls and valid removals only after live source verification.
8. Begin the 12-week monitoring log.

This batch addresses both the strongest root causes and the highest-authority reinforcing sources.

## 16. Remaining access inputs

Public evidence collection and the first owned-site change no longer depend on Dr. Hany. The Search and Images baseline, current website and Linktree references, and public authority-profile evidence were captured independently.

- Wix homepage custom structured-data editing access
- Search Console access
- Google Business Profile owner/manager access through the masked `li...@gmail.com` manager or an approved transfer
- Separate Knowledge Panel claim access only if a distinct organization panel appears
- YouTube channel owner/manager access
- Google Ads or Ad Grants account state and approval decision
- WordPress.com ownership or recovery route
- Admin access for official social and nonprofit profiles
- A `lifeusa.org` mailbox authorized for correction outreach

All external messages, access requests, form submissions, and changes to client-controlled accounts are human-gated. The live status page contains a decision-by-decision approval queue; marking an item approved records the decision but does not trigger an external action automatically.

## 17. July 15 execution update

- Captured and published the repeatable Google Search and Google Images baseline.
- Verified the first 20 broad Google Images results: 14 official, four unrelated same-name results, two current-branded marketplace results, and no retired crescent mark in that exact sample.
- Uploaded the verified 1800 by 1800 current square asset to LifeUSA's Wix Media Manager and assigned it to the Wix Business Profile logo field.
- Uploaded the approved 4101 by 1201 horizontal logo to the same LifeUSA Wix Media Manager. The public file returns `200`, and its remote SHA-256 exactly matches the approved local source. The canonical square and horizontal asset kit is now complete.
- Confirmed July 20 that the manually published homepage `NGO` node now uses the canonical colored square, stable `@id`, `alternateName`, verified `sameAs`, address, and contact point. The former white-logo URL is absent from the fetched homepage HTML. Two `WebSite` nodes remain for later consolidation.
- Reverified the retired crescent mark on the old WordPress archive, Kids That Do Good, and Arab Info Mall.
- Verified the blue-globe mark on Candid/GuideStar, GreatNonprofits, LinkedIn, the English Facebook page, Instagram, YouTube, X, and the Somali Facebook page linked from the English Linktree. On July 19, the client confirmed this is an acceptable current variant, not an outdated mark.
- Verified that Charity Navigator and ReliefWeb expose no LifeUSA logo, so they are enhancement targets rather than stale-logo sources.
- Published the authority-profile matrix, source evidence, correction drafts, owned-social checklist, and expanded `sameAs` specification on the live status page.
- Captured the exact Southfield entity query and verified that the right-hand result is the established Google Business Profile, with 4.3 stars, 20 reviews, the correct address, and a stale HTTP website link.
- Verified through Google's claim flow that the existing profile is managed by a masked `li...@gmail.com` account. The current Google session is not authorized, and no request was sent from the user's personal account.
- Captured the public Google Maps media inventory and preserved a blue-globe Life avatar used by a contributor account associated with listing media. This is acceptable when it matches the approved current variant.
- Confirmed that a sponsored LifeUSA result visibly serves the acceptable current blue-globe variant; this is no longer classified as a logo defect.
- Audited the available Google Ads CLI hierarchy read-only. It contains no LifeUSA Ads or Ad Grants customer, so the serving logo asset requires the LifeUSA ads administrator account.
- Published the complete Google property audit and four dated evidence files on the live status page.
- Sent the Kids That Do Good correction request to `info@kidsthatdogood.com` and recorded Zoho message ID `1784122643723013500`.
- Sent the GreatNonprofits correction request to `support@greatnonprofits.org` and recorded Zoho message ID `1784122678410013500`.
- Established a human-approval gate for all remaining communication and account-changing work. The approval queue contains the exact official route, prepared copy or action package, access dependency, and acceptance check for Arab Info Mall, Candid, ReliefWeb, Google Business Profile, social profiles, WordPress, Wix editor changes, and Google Ads.
- Verified the official Arab Info Mall contact addresses and kiosk administrator workflow. No Arab Info Mall message was sent.
- Confirmed that the Wix REST API can manage uploaded media and the Site Properties logo but not these existing-page editor changes. The user subsequently completed the NGO markup, public brand-resources page, navigation link, and visible logo placements manually in Wix. Only the duplicate `WebSite` node cleanup remains open within APR-007.
- Activated the recurring `lifeusa-logo-signal-monitor` for Sundays at 10:00 Europe/Istanbul. It is read-only for Zoho and public platforms, preserves APR-001 through APR-008 as human-gated, and updates only evidence-backed status artifacts.
- Completed the July 15 monitoring control check. Zoho confirms both sent messages were delivered successfully, with no publisher reply found. Kids That Do Good and GreatNonprofits still reference their old public image files.
- Verified that the GreatNonprofits CDN image is byte-for-byte unchanged and that the Kids That Do Good image is pixel-identical to the captured retired logo despite harmless PNG encoding differences.
- Reverified both canonical Wix files: each returns `200`, retains the approved dimensions, and exactly matches the local master SHA-256.
- Ran the exact Google Images query for `Life for Relief and Development logo` with English, United States, and personalization disabled. The initial result set still includes Kids That Do Good and the old WordPress archive, confirming that live retired-logo sources remain discoverable by Google.
- Verified July 21 that the live header and footer use a byte-identical copy of the approved 4101 by 1201 horizontal master, the favicon source is byte-identical to the approved 1800 by 1800 square, and both visible logo placements expose descriptive alt text. `LOGO-006` is complete.
- Verified July 21 that `Brand Resources` is present in the public About submenu and its destination returns `200`.

## 18. Research confidence and limitations

### High confidence

- Dr. Hany’s request and Saiaf’s response were verified directly in Zoho Mail.
- The homepage’s live structured data and logo URLs were inspected directly.
- The repaired NGO node uses the approved colored square, while the visible header, footer, and favicon sources are byte-identical to their approved canonical masters. Two `WebSite` nodes remain for consolidation.
- The old WordPress, Kids That Do Good, and Arab Info Mall pages visibly publish the retired crescent logo.
- Candid/GuideStar, GreatNonprofits, LinkedIn, Facebook, Instagram, YouTube, and X visibly publish the blue-globe logo, which the client confirmed is an acceptable current variant.
- The English Linktree avatar is current, and its Facebook destination opens a Somali-language page. The destination mismatch remains a profile-integrity issue; the Somali page's blue-globe logo is acceptable.
- Google already has an established LifeUSA Business Profile for the Southfield location; it should be updated, not recreated.
- The current Business Profile manager is a different masked account, and the available Google account cannot edit the listing.
- A sponsored LifeUSA result visibly uses the acceptable current blue-globe variant. The available Google Ads credentials do not include a LifeUSA customer, but replacement is optional consistency work rather than a correctness blocker.
- The exact Southfield query showed the local Business Profile rather than a separate nonprofit Knowledge Panel.
- Google’s official documentation supports the distinct workflows described for Images, Organization markup, Business Profile, Knowledge Panel, favicon, Search Console, and Ads.

### Medium confidence

- The exact result Dr. Hany originally saw may differ from the sponsored result, local profile, or Maps media captured independently. Only confirmed retired-crescent surfaces require logo correction; acceptable current variants do not.
- Glassdoor and ShareDetroit require a final visual and account-access audit before their logo state is classified.

### Collection note

The research began with Firecrawl search and eleven page-level extractions. The Firecrawl workspace then reached its credit limit. The remaining primary sources were reviewed directly from official Google, Schema.org, Candid, Charity Navigator, LinkedIn, Facebook, YouTube, and current LifeUSA profile pages. No recommendation depends on a community forum as its authority.

## 19. Primary sources

### Google Search and Images

- [Organization structured data](https://developers.google.com/search/docs/appearance/structured-data/organization) - Logo eligibility, white-background requirement, and no display guarantee.
- [Google Image SEO](https://developers.google.com/search/docs/appearance/google-images) - Image discovery, context, stable URLs, and quality guidance.
- [Image sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/image-sitemaps) - Discovery rules for images and CDN verification.
- [Remove hosted images](https://developers.google.com/search/docs/crawling-indexing/prevent-images-on-your-page) - Googlebot-Image and image noindex options.
- [Remove owned information](https://developers.google.com/search/docs/crawling-indexing/remove-information) - Temporary versus permanent removal.
- [Search Console Removals](https://support.google.com/webmasters/answer/9689846?hl=en) - Temporary removal duration and permanent-source requirements.
- [Refresh Outdated Content](https://support.google.com/webmasters/answer/7041154?hl=en) - Third-party outdated image and page refresh rules.
- [Ask Google to recrawl](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl) - URL Inspection, sitemap, timing, and limits.
- [Favicon in Search](https://developers.google.com/search/docs/appearance/favicon-in-search) - Favicon size, crawlability, and refresh timing.

### Google entity and local surfaces

- [About Knowledge Panels](https://support.google.com/knowledgepanel/answer/9163198?hl=en) - Automated source model and representative feedback.
- [Submit Knowledge Panel feedback](https://support.google.com/knowledgepanel/answer/7534842?hl=en) - Featured image replacement requirements.
- [Get verified on Google](https://support.google.com/knowledgepanel/answer/7534902?hl=en) - Claim and verification routes.
- [How the Knowledge Graph works](https://support.google.com/knowledgepanel/answer/9787176?hl=en) - Public sources, automation, and correction paths.
- [Manage Business Profile photos](https://support.google.com/business/answer/6103862?hl=en) - Logo, cover, and owner-media management.
- [Business Profile photo guidelines](https://support.google.com/business/answer/6123536?hl=en) - File and quality requirements.
- [Report Business Profile photos](https://support.google.com/business/answer/6130451?hl=en) - Customer-media policy reports.

### Google Ads

- [Business information assets](https://support.google.com/google-ads/answer/12497613?hl=en) - Logo uploads, dynamic assets, review, and no serving guarantee.
- [Brand verification](https://support.google.com/google-ads/answer/13819790?hl=en) - Trademark and advertiser-verification route.
- [Performance Max brand guidelines](https://support.google.com/google-ads/answer/15829354?hl=en) - Campaign-level brand control.

### Entity and profile sources

- [Schema.org Organization](https://schema.org/Organization) - Organization identity properties.
- [Schema.org sameAs](https://schema.org/sameAs) - Unambiguous entity reference links.
- [Candid profile claim/update](https://candid.org/claim-nonprofit-profile/) - Nonprofit profile management and syndication.
- [Charity Navigator Nonprofit Portal](https://intercom.help/charity-navigator/en/articles/8695464-the-nonprofit-portal-and-portal-representatives) - Representative access and profile updates.
- [LinkedIn Page logo update](https://www.linkedin.com/help/linkedin/answer/a1399545) - Super-admin logo replacement.
- [Facebook Page profile image](https://www.facebook.com/help/284445998278828) - Page image update route.
- [YouTube channel branding](https://support.google.com/youtube/answer/10456525) - Channel profile image and brand management.

### Current LifeUSA footprint

- [LifeUSA official website](https://www.lifeusa.org/)
- [Old LifeUSA WordPress site](https://lifeusaorg.wordpress.com/where-we-are/)
- [Kids That Do Good profile](https://kidsthatdogood.com/causes/life-relief-development/)
- [Arab Info Mall profile](https://arabinfomall.bibalex.org/En/Index.aspx?orgid=879&sectionid=1)
- [Charity Navigator profile](https://www.charitynavigator.org/ein/954402149)
- [GreatNonprofits profile](https://greatnonprofits.org/org/life-for-relief-and-development)
- [Candid / GuideStar profile](https://www.guidestar.org/profile/95-4402149)
- [ReliefWeb profile](https://reliefweb.int/organization/life)
- [LinkedIn page](https://www.linkedin.com/company/life-for-relief-and-development)
- [Facebook page](https://www.facebook.com/Life4ReliefEN/)
- [Instagram profile](https://www.instagram.com/life4relief/)
- [YouTube channel](https://www.youtube.com/channel/UCRTkW2TMw344eC562GSK1nA)
- [X profile](https://x.com/LIFEforRELIEF)
- [Official English Linktree](https://linktr.ee/LIFEUSA)

## Rerun inputs

```text
workflow: firecrawl-deep-research
topic: Replace and suppress LifeUSA's retired logo across Google and public entity sources
depth: thorough
output: markdown goal specification and execution plan
location: United States
baseline date: 2026-07-14
```
