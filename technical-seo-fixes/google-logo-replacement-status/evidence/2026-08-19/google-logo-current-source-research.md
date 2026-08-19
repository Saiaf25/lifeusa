# LifeUSA Google logo current-source research

Checked August 19, 2026 from Europe/Istanbul. This is a read-only public-source review. No message, form, access request, account change, or Google submission was made.

## Reality check

The website-side implementation is healthy, but the wider problem is not finished.

- LifeUSA's canonical yellow-ray square is live in the homepage `NGO` structured data, favicon source, and Brand Resources page.
- The old WordPress archive, Kids That Do Good, and Arab Info Mall still publish the retired crescent logo from live public image URLs.
- Candid/GuideStar and GreatNonprofits still publish the approved blue-globe variant. They are not retired-logo defects.
- LinkedIn, YouTube, X, and Linktree expose approved current identity images. Linktree still sends its Facebook button to the Somali-language Facebook profile instead of the intended English page.
- ReliefWeb still exposes no LifeUSA logo and still links to the HTTP website URL.
- Facebook and Instagram could not be reliably classified in this logged-out retrieval pass. Their public pages either rejected the request or returned a generic shell without a readable account image.
- The August 12 Google Images evidence remains the latest controlled query evidence in this repository. This pass did not produce a new reliable Google result-set capture, so it does not prove that the benchmark query has improved since August 12.

Uploading the current logo to more directories can strengthen entity consistency, but it cannot override a retired logo that remains live at a source. Google documents source correction, crawlable Organization markup, recrawling, and post-change outdated-content refresh as the relevant mechanisms. Google Ads is a separate paid surface and is not an organic logo-removal tool.

## Classification key

- **Verified current:** the public source was fetched on August 19 and exposes an approved yellow-ray or blue-globe logo.
- **Unchanged legacy:** the public source still exposes the retired crescent logo and its decoded pixels match the stored July baseline.
- **No logo:** the public organization page is live but exposes no LifeUSA logo in its public markup.
- **Inaccessible:** the logged-out public response did not expose enough account-specific evidence to classify the logo.
- **Inference:** a conclusion derived from multiple verified facts, explicitly labeled as such.

## Owned LifeUSA signals

| Signal | August 19 verification | Classification |
|---|---|---|
| [Homepage](https://www.lifeusa.org/) | Returned HTTP 200. Three JSON-LD blocks parsed successfully: two `WebSite` nodes and one `NGO` node with `@id` `https://www.lifeusa.org/#organization`. The `NGO.logo` is the approved 1800 by 1800 square at `https://static.wixstatic.com/media/af2a6c_49a4190c354746b493c123d311222fb5~mv2.png`. | **Verified current** |
| Organization identity | The `NGO` node uses the canonical homepage URL, the full organization name, the approved square as both `url` and `contentUrl`, and eight official `sameAs` destinations. | **Verified current** |
| Favicon | The homepage declares `icon`, `shortcut icon`, `apple-touch-icon`, and `mask-icon` renditions based on `6df904_3ba0b63af7e945f0a92fbe9978934569~mv2.png`. The source file returned as an 1800 by 1800 PNG and is byte-for-byte identical to the canonical square. | **Verified current** |
| [Brand Resources](https://www.lifeusa.org/brand-resources) | Returned HTTP 200 and still references both the approved square and horizontal Wix assets. | **Verified current** |
| [Canonical square](https://static.wixstatic.com/media/af2a6c_49a4190c354746b493c123d311222fb5~mv2.png) | 1800 by 1800 PNG; SHA-256 `d3d830b08effb1202b1ded8bc26bec91f78dfb8b89c97ef59f892b2ea88a77cb`. | **Verified current** |
| [Canonical horizontal](https://static.wixstatic.com/media/af2a6c_1bd1137d792b44c3855d26ee4cfcced0~mv2.png) | 4101 by 1201 PNG; SHA-256 `14819312d534ee94bcb625a87a15ab76cd05ad77ec9d09a2b514bf8c308cd867`. | **Verified current** |

### Owned-site interpretation

The core logo implementation no longer needs reinvention. The two remaining `WebSite` nodes are a schema-cleanliness issue, but they do not contradict the current `NGO.logo`. The best owned-site intervention is to keep these URLs stable and use Search Console validation and recrawl after any material schema or image change.

## Retired-logo source verification

| Source | Live August 19 evidence | Comparison | Classification |
|---|---|---|---|
| [Old LifeUSA WordPress archive](https://lifeusaorg.wordpress.com/where-we-are/) | Returned HTTP 200 and still references `https://lifeusaorg.files.wordpress.com/2015/05/life-logo-hd_white.png`. The image returned as a 1500 by 1500 PNG. | SHA-256 `281840637b1241b09371d2c0adf19d4a7b683fbc8683d0af39e4ad42afc66850`; decoded-pixel absolute error against the July retired-logo evidence: `0`. | **Unchanged legacy** |
| [Kids That Do Good](https://kidsthatdogood.com/causes/life-relief-development/) | Returned HTTP 200. The visible image, Open Graph image, and X/Twitter image still reference `https://kidsthatdogood.com/wp-content/uploads/2019/06/life-for-relief-and-development-logo.png`. | Current file SHA-256 `08b45558e7ef49d168b90490f7c8e2644f47337fb950fce15aca50cbc097bf56`; decoded-pixel absolute error against the July retired-logo evidence: `0`. The checksum changed because of encoding or metadata, not because the visible logo changed. | **Unchanged legacy** |
| [Arab Info Mall](https://arabinfomall.bibalex.org/En/Index.aspx?orgid=879&sectionid=1) | Returned HTTP 200 and still references `/Attachments/Logos/10751.gif`. The profile also retains stale address, phone, fax, branch, email, and HTTP website details. | 200 by 200 GIF; SHA-256 `9296fe04f8808f906310433494959417a290d2933d5603362e40e25fce3bcb88`; decoded-pixel absolute error against the July retired-logo evidence: `0`. | **Unchanged legacy** |

### Source-removal interpretation

These three live pages are the primary blockers. A Google removal or refresh request cannot truthfully represent a retired logo as gone while the public source still serves the same pixels. The sequence must be publisher correction first, then Google refresh.

## Authority and social-profile verification

| Surface | August 19 public evidence | Classification | Intervention |
|---|---|---|---|
| [Candid / GuideStar](https://www.guidestar.org/profile/95-4402149) | Returned HTTP 200 and still embeds `https://docs.candid.org/edoc/11078205`. The 1500 by 1500 PNG is byte-for-byte unchanged with SHA-256 `f440247655ec4a13196be3ee40b291c361de42e596a05941395fc22dd42b6328`. Its decoded pixels match the stored approved blue-globe evidence exactly. The website link remains `http://www.lifeusa.org/`. | **Verified current logo; stale HTTP link** | Keep the logo. Update the website and other stale identity fields through an authorized profile owner. |
| [GreatNonprofits](https://greatnonprofits.org/org/life-for-relief-and-development) | Returned HTTP 200. Visible, Open Graph, and X/Twitter image references still use `https://cdn.greatnonprofits.org/images/logos/org_logo_513389_1711518504.png`. The 266 by 266 PNG remains byte-for-byte unchanged with SHA-256 `2d1de086aa753d889f32d05b3fabc232e76f1fe16f4c9a4ad0f64f6d67108117`, and its decoded pixels match the approved blue-globe baseline exactly. | **Verified current** | No logo correction is needed for correctness. Maintain profile accuracy. |
| [ReliefWeb](https://reliefweb.int/organization/life) | Returned HTTP 200, exposed no LifeUSA logo in public markup, and still linked to `http://www.lifeusa.org`. | **No logo; stale HTTP link** | Request the HTTPS website correction and ask whether the profile supports a logo. |
| [LinkedIn](https://www.linkedin.com/company/life-for-relief-and-development/) | Returned HTTP 200. First-party Open Graph metadata exposed a 200 by 200 approved blue-globe company avatar. The public page still references `http://www.lifeusa.org`. | **Verified current logo; stale HTTP link** | Keep the logo unless optional standardization is approved. Correct the website to HTTPS. |
| [YouTube](https://www.youtube.com/channel/UCRTkW2TMw344eC562GSK1nA) | Returned HTTP 200. First-party channel metadata exposed a 900 by 900 approved blue-globe avatar and the LifeUSA website identity. | **Verified current** | Keep or optionally standardize through an authorized channel owner. |
| [X](https://x.com/LIFEforRELIEF) | Returned HTTP 200. First-party Open Graph metadata exposed a 200 by 200 approved blue-globe profile image. | **Verified current** | Keep or optionally standardize through an authorized account owner. |
| [Linktree](https://linktr.ee/LIFEUSA) | Returned HTTP 200. Its 1000 by 1000 profile image is byte-for-byte identical to the stored approved Linktree avatar, SHA-256 `733374fee88028eacc3c96bf2819d782eb159a01f21e4acbb51b3ccd956f66bc`. The Facebook destination remains `https://www.facebook.com/profile.php?id=61563961181765`, the Somali-language profile. | **Verified current avatar; wrong destination** | Repair the English Linktree Facebook button after account-owner approval. |
| [Facebook, English](https://www.facebook.com/Life4ReliefEN/) | The logged-out public request returned HTTP 400 with no account-specific image metadata. | **Inaccessible** | Verify in an authorized or stable logged-out browser before changing anything. |
| [Facebook, Somali](https://www.facebook.com/profile.php?id=61563961181765) | The logged-out public request returned HTTP 400 with no account-specific image metadata. | **Inaccessible** | The destination mismatch is independently verified on Linktree; classify the Facebook image again in an authorized browser. |
| [Instagram](https://www.instagram.com/life4relief/) | Returned HTTP 200, but the response was a generic Instagram shell without a reliable account-specific profile image. | **Inaccessible** | Verify in an authorized or stable logged-out browser before changing anything. |

## What Google's current documentation actually supports

### 1. Organization logo

Google says Organization structured data on the homepage can help it understand the organization and can influence the logo shown in Search and knowledge panels. The logo must be at least 112 by 112, crawlable, indexable, supported by Google Images, and visually correct on white. Eligibility does not guarantee display.

Source: [Google Search Central: Organization structured data](https://developers.google.com/search/docs/appearance/structured-data/organization), accessed August 19, 2026.

**LifeUSA consequence:** the live 1800 by 1800 colored square satisfies the documented technical image requirements. The remaining risk is conflicting external evidence, not a missing homepage logo field.

### 2. Favicon is a separate feature

Google treats the Search favicon separately from the Organization logo. It recommends a stable square favicon larger than 48 by 48, declared on the hostname homepage and crawlable by Googlebot and Googlebot-Image. Updates can take days to weeks and are not guaranteed to display.

Source: [Google Search Central: Define a favicon for Search results](https://developers.google.com/search/docs/appearance/favicon-in-search), accessed August 19, 2026.

**LifeUSA consequence:** the favicon source is already current and stable. Do not use favicon work as a substitute for removing third-party retired-logo pages.

### 3. Google Images follows page and image evidence

Google's image guidance emphasizes useful page context, descriptive metadata, high-quality images, stable discoverable URLs, and representative images. It does not describe bulk directory uploads as a way to force a specific organizational logo. Google also cautions against using a generic logo as every ordinary page's preview image.

Source: [Google Search Central: Image SEO best practices](https://developers.google.com/search/docs/appearance/google-images), accessed August 19, 2026.

**LifeUSA consequence, inference:** genuine authoritative profiles are useful, but multiplying low-value logo placements is weaker than correcting the WordPress, Kids, and Arab Info Mall pages that Google can still crawl.

### 4. Recrawl only after the source is correct

Google permits verified site owners or full Search Console users to request recrawling for a small number of owned URLs through URL Inspection, or to use a sitemap for many URLs. Recrawling can take days to weeks; repeated requests do not accelerate it, and indexing is not guaranteed.

Source: [Google Search Central: Ask Google to recrawl your URLs](https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl), accessed August 19, 2026.

**LifeUSA consequence:** request a homepage and Brand Resources recrawl only if there has been a material change or Google has not yet reflected the already-live implementation. Do not repeatedly resubmit unchanged URLs.

### 5. Third-party outdated-content requests require a changed source

Google's Refresh Outdated Content tool is for pages or images that no longer exist or are significantly different. For images, Google requires the image URL and the containing-page URL, with separate requests for each page where the image appears. It updates Google results, not the publisher's website.

Source: [Google Search Help: Refresh outdated content](https://support.google.com/webmasters/answer/7041154?hl=en), accessed August 19, 2026.

**LifeUSA consequence:** the tool is premature for WordPress, Kids, and Arab Info Mall today because their retired images remain live and pixel-identical. Use it immediately after each publisher removes or materially replaces its image.

### 6. Search Console removals are temporary

Google's Removals tool can temporarily hide an owned page or image for about 180 days. Permanent removal still requires changing the source, returning a removal status, protecting it, or applying an indexing directive.

Source: [Google Search Console Help: Removals tool](https://support.google.com/webmasters/answer/9689846?hl=en), accessed August 19, 2026.

**LifeUSA consequence:** this is relevant only to a LifeUSA-controlled URL. It cannot permanently solve a live third-party retired image.

### 7. Business Profile and Knowledge Panel are separate surfaces

A verified Business Profile manager can add or replace a logo under Photos. Google recommends JPG or PNG, 720 by 720, with a 250 by 250 minimum; review and processing apply. Google does not guarantee that a chosen cover appears first.

Source: [Google Business Profile Help: Manage photos and videos](https://support.google.com/business/answer/6103862?hl=en), accessed August 19, 2026.

A verified Knowledge Panel representative can suggest an image replacement using a public image URL when the panel already has an image. Panels are assembled automatically from public web information, so corrections remain subject to review and corroborating sources.

Sources: [Google Knowledge Panel Help: About knowledge panels](https://support.google.com/knowledgepanel/answer/9163198?hl=en) and [Suggest changes to a Google knowledge panel](https://support.google.com/knowledgepanel/answer/7534842?hl=en), accessed August 19, 2026.

**LifeUSA consequence:** Business Profile and Knowledge Panel actions should be executed as separate approved interventions. Neither one removes the retired source files from Google Images.

### 8. Google Ads does not repair organic logo results

Google Ads supports business logo assets for eligible ad accounts, subject to asset review and serving decisions. The documentation distinguishes these paid business-information assets from organic Search crawling.

Source: [Google Ads Help: About business information](https://support.google.com/google-ads/answer/12497613?hl=en), accessed August 19, 2026.

**LifeUSA consequence:** a paid campaign can show the approved logo in ads, but it is not a corrective mechanism for the retired organic image. Run paid media only for its marketing purpose, not as the technical fix.

## Intervention order supported by the evidence

1. **Recover and correct the old WordPress archive.** Replace the header logo and remove or make unavailable the retired media file, or make the obsolete archive private if leadership approves that disposition.
2. **Escalate Kids That Do Good.** The original correction request has not produced a public change. Prepare a short follow-up that includes the exact page URL, exact old image URL, exact approved replacement URL, and asks for both visible and metadata replacement.
3. **Approve and send the Arab Info Mall correction.** Request replacement of `10751.gif` and a full refresh of the stale organization record, not only the logo.
4. **Repair profile integrity.** Change the Linktree Facebook destination and update HTTP website links on Candid, LinkedIn, and ReliefWeb to canonical HTTPS through authorized owners.
5. **Handle Google-controlled surfaces separately.** Verify Business Profile ownership and the current public logo, then change it only if wrong. Verify or claim the Knowledge Panel and suggest the canonical public image only if its featured image is wrong.
6. **Trigger Google refresh after source changes.** Use Search Console recrawl for owned URLs. Use Refresh Outdated Content separately for each third-party image and containing page only after the publisher has removed or materially replaced the retired logo.
7. **Monitor weekly, not continuously.** Re-run the two controlled Google Images queries and the three retired-source checks once per week. Count stability only when the retired logo is absent from both the live sources and the monitored Google result sets for three consecutive weekly checks.

## Evidence limits

- This review verified public HTTP responses, markup, direct image bytes, dimensions, checksums, and decoded-pixel comparisons.
- It did not use Search Console, Business Profile, Knowledge Panel, Google Ads, social administrator, Wix editor, WordPress owner, or directory-owner access.
- It did not send or prepare a communication for delivery.
- Facebook and Instagram remain unclassified in this pass because their logged-out responses did not expose reliable account-specific images.
- A new controlled Google Search or Google Images capture is still required before claiming any August 19 result-set improvement.
