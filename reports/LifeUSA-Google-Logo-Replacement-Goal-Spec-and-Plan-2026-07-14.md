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

The proposed directory and third-party profile campaign is valid, but it should not run alone. The fastest credible approach is a coordinated four-track program:

1. Fix the canonical logo signals on `lifeusa.org`.
2. Remove or replace the retired logo at the specific pages and image URLs that still publish it.
3. Update Google-owned surfaces separately: Business Profile, Knowledge Panel if present, favicon/Search, Search Console, and Google Ads if used.
4. Align high-trust, already-indexed nonprofit and social profiles with one approved logo package.

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
- Every LifeUSA-controlled website and Tier 1 profile uses the approved current logo package.
- Every confirmed retired-logo source is either corrected, removed, blocked from Google Images, or recorded as an unresolved third-party dependency with proof of outreach.

These are campaign targets, not guarantees about Google’s algorithm.

### Non-goals

- Do not claim that directory submissions directly force Google to select a logo. Google does not document such a guarantee.
- Do not create dozens of low-quality directory listings.
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

- One approved square logo and one approved horizontal logo, with no competing “official” variants.
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

### 4.4 Important interpretation

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

Prioritize existing, authoritative, relevant profiles that already rank for LifeUSA. Do not optimize for the number of submissions. Optimize for entity consistency, control, and actual branded visibility.

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
| GreatNonprofits | Already indexed and currently uses a modern logo variant | Align with approved master and verify website/social links |
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
- Current visual classification: approved, retired, uncertain
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

## 8. Phased execution plan

### Phase 0: Confirm the exact problem and approve assets

**Target:** Day 0 to Day 2
**Gate:** No production changes until completed

- Obtain Dr. Hany’s screenshot or reproduce the exact result with him.
- Record query, Google tab/surface, device, location, signed-in state, image URL, and landing page.
- Obtain the authoritative current logo in vector and high-resolution PNG formats.
- Obtain written confirmation of which logo is retired.
- Decide whether the approved current mark includes the tagline and which tagline punctuation is correct.
- Name the LifeUSA brand approver, Wix administrator, Business Profile owner, Search Console owner, social admin, and Ads admin.
- Approve the canonical asset matrix and public brand-page wording.

**Deliverables:** Baseline evidence pack, approved brand kit, access matrix, signed decision record.

### Phase 1: Repair owned canonical signals

**Target:** Day 2 to Day 5
**Dependency:** Approved brand kit and Wix access

- Publish the brand page and canonical square logo URL.
- Replace the homepage `NGO.logo` value.
- Add stable `@id`, approved `alternateName`, and verified `sameAs` links.
- Consolidate duplicate `WebSite` graph nodes if Wix permits.
- Align favicon, header, and footer variants.
- Confirm no retired logo is referenced by owned pages, schema, CSS, media galleries, PDFs, or hidden components.
- Add the logo to an image sitemap or confirm Wix’s sitemap discovery path.
- Validate HTML, structured data, dimensions, content type, crawlability, and white-background appearance.
- Request indexing for homepage and brand page.

**Acceptance criteria:** Live source contains one approved entity graph; canonical logo is `200`, visible on white, and crawlable; validation screenshots saved.

### Phase 2: Remove the strongest retired-logo sources

**Target:** Day 3 to Day 14
**Can run in parallel with Phase 1 after asset approval**

- Recover or confirm ownership of `lifeusaorg.wordpress.com`.
- Decide whether to modernize it, make it private, or retire it.
- Delete or replace the old WordPress media file and confirm its final HTTP state.
- Contact Kids That Do Good with the canonical square logo and correction evidence.
- Contact Arab Info Mall for a full profile correction, not logo-only, because contact data is stale.
- Verify and correct Glassdoor and ShareDetroit.
- Submit Google refresh/removal requests only after source changes are live.

**Acceptance criteria:** Each P0 old image is changed at source or has a documented owner/contact blocker and dated outreach evidence.

### Phase 3: Align Google properties

**Target:** Day 3 to Day 10
**Dependencies:** Approved square asset and access

- Verify and update Google Business Profile logo and photo inventory.
- Distinguish Business Profile from Knowledge Panel.
- Claim the Knowledge Panel if available and submit a supported featured-image correction.
- Update YouTube channel branding and official site links.
- Review Search Console ownership and removal/indexing tools.
- Audit Google Ads business-information assets and advertiser verification.

**Acceptance criteria:** Each accessible Google property uses the approved asset; inaccessible properties have a named access owner and request date.

### Phase 4: Align authoritative profiles

**Target:** Day 5 to Day 21

- Update Candid/GuideStar.
- Update Charity Navigator.
- Verify GreatNonprofits.
- Update ReliefWeb.
- Update LinkedIn, Facebook, Instagram, and YouTube.
- Update relevant employment and humanitarian directories already ranking for LifeUSA.
- Use identical canonical website, organization name, current logo family, address, phone, and short description.

**Acceptance criteria:** All Tier 1 profiles are verified and consistent; Tier 2 work is at least 80% resolved or documented.

### Phase 5: Optional paid visibility bridge

**Target:** After Phase 1; 30-day controlled test
**Approval gate:** Separate budget or Ad Grants approval

- Launch only if the team wants immediate paid brand consistency while organic sources recrawl.
- Use Search business-information assets with the approved logo.
- Target organization-name queries in the US.
- Keep landing pages and message factual and donor-focused.
- Do not represent the campaign as a method for changing organic images.
- Stop or revise if asset serving is inconsistent or the campaign adds no measurable value.

### Phase 6: Monitor and close

**Target:** Weekly for 12 weeks

- Repeat the branded query set on US desktop and mobile.
- Record image position, landing page, direct image URL, and visual classification.
- Check Search Console indexing and removal status.
- Check Business Profile, Knowledge Panel, favicon, and ad assets.
- Follow up with unresolved publishers at 7, 14, and 30 days.
- Close only after the primary targets are satisfied for three consecutive weekly checks or the sponsor accepts documented third-party exceptions.

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
| Multiple current variants compete | Ambiguous entity signal | Approve one canonical square and one canonical horizontal version |
| Third party does not respond | Old result remains | Follow-up schedule, escalation contact, document exception, strengthen higher-authority sources |
| Business Profile user photo is old but not policy-violating | Removal request rejected | Add strong current owner media and report only genuine policy violations |
| Removal request submitted too early | Request rejected or image returns | Change source first, verify response, then submit |
| Ads show a dynamic old logo | Paid inconsistency | Audit, pause/remove dynamic assets, upload manual approved logo |
| Team mistakes ads for an organic fix | Wrong expectations | Separate paid and organic KPIs in reporting |
| Search results vary by location or personalization | Misleading progress | Use repeatable US signed-out desktop/mobile protocol |
| Mass directory submissions create spam | Brand and SEO risk | Use the tiered authority/relevance filter |
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

## 16. Open inputs required before execution

- Screenshot or exact reproduction of Dr. Hany’s Google result
- Approved current square logo and horizontal logo
- Explicit confirmation of the retired mark
- Approved organization name, abbreviations, and tagline punctuation
- Wix admin access
- Search Console access
- Google Business Profile owner/manager access
- Knowledge Panel claim state
- YouTube channel owner/manager access
- Google Ads or Ad Grants account state and approval decision
- WordPress.com ownership or recovery route
- Admin access for official social and nonprofit profiles
- A `lifeusa.org` mailbox authorized for correction outreach

## 17. Research confidence and limitations

### High confidence

- Dr. Hany’s request and Saiaf’s response were verified directly in Zoho Mail.
- The homepage’s live structured data and logo URLs were inspected directly.
- The structured-data logo is white-on-transparent and fails the white-background appearance test.
- The old WordPress, Kids That Do Good, and Arab Info Mall pages visibly publish the retired crescent logo.
- Google’s official documentation supports the distinct workflows described for Images, Organization markup, Business Profile, Knowledge Panel, favicon, Search Console, and Ads.

### Medium confidence

- The CEO likely meant Google Images, based on his wording and the current image-result evidence, but the exact surface is not confirmed without his screenshot.
- Glassdoor and ShareDetroit require a final visual and account-access audit before their logo state is classified.

### Collection note

The research began with Firecrawl search and eleven page-level extractions. The Firecrawl workspace then reached its credit limit. The remaining primary sources were reviewed directly from official Google, Schema.org, Candid, Charity Navigator, LinkedIn, Facebook, YouTube, and current LifeUSA profile pages. No recommendation depends on a community forum as its authority.

## 18. Primary sources

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
- [ReliefWeb profile](https://reliefweb.int/organization/life)
- [LinkedIn page](https://www.linkedin.com/company/life-for-relief-and-development)
- [Facebook page](https://www.facebook.com/Life4ReliefEN/)

## Rerun inputs

```text
workflow: firecrawl-deep-research
topic: Replace and suppress LifeUSA's retired logo across Google and public entity sources
depth: thorough
output: markdown goal specification and execution plan
location: United States
baseline date: 2026-07-14
```
