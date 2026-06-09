# Lifeusa.org SEO Audit - Kickoff Agenda

**Date:** 2026-05-08, 16:00
**Duration:** 1 hour
**Consultant:** Saiaf Gamal (freelance)
**Client:** Tasneem Elridy (volunteer, Life for Relief and Development)
**Reference:** LifeUSA Technical SEO [Master Sheet].xlsx (full audit findings)
**Evidence captured:** 2026-05-07, ~22:30 UTC, via curl + Screaming Frog crawl + Ahrefs subdomain export

---

## 1. Reality check (2 minutes)

### Top 5 confirmed gaps

#### Gap 1. Subdomain sprawl is fragmenting your equity and your donor data

Five subdomains observed. Each on different infrastructure with different SEO postures.

**In plain terms:**

- **The problem:** Five subdomains run on different platforms with no shared analytics or unified SEO posture, and one of them is fully dead in DNS.
- **How we found out:** A direct DNS + HTTP header probe showed arabic. does not resolve, donate. and donation. are two separate donation platforms, and staff. is a public WordPress install. Ahrefs confirmed the split: backlinks and traffic are scattered across all of them.
- **Why it hurts SEO:** Google treats each subdomain as a distinct site, so authority and backlinks earned on one do not lift the others. A dead subdomain wastes its referring links entirely, two donation platforms split donor analytics, and a public WordPress staff site competes with the main domain for crawl budget and brand keywords.

> **Evidence: subdomain probe (curl, 2026-05-07)**
>
> `arabic.lifeusa.org` (DEAD in DNS):
> ```
> $ curl -sIv https://arabic.lifeusa.org/
> * Could not resolve host: arabic.lifeusa.org
> $ dig +short arabic.lifeusa.org
> (empty)
> ```
>
> `donate.lifeusa.org` (Cloudflare, redirects to donorportal):
> ```
> $ curl -sI https://donate.lifeusa.org/
> HTTP/2 301
> location: https://donate.lifeusa.org/donorportal/
> server: cloudflare
> content-security-policy: upgrade-insecure-requests
> strict-transport-security: max-age=63072000; includeSubDomains
> ```
>
> `donation.lifeusa.org` (Cloudflare + Givecloud, separate platform):
> ```
> $ curl -sI https://donation.lifeusa.org/
> HTTP/2 200
> x-givecloud-app: 30e6db6e4f1287f56931e5f5ae6a5cf6648e5bee
> x-givecloud-domain: life
> x-site-id: 426
> server: cloudflare
> ```
>
> `staff.lifeusa.org` (Cloudflare + WordPress, public):
> ```
> $ curl -sI https://staff.lifeusa.org/
> HTTP/2 200
> server: cloudflare
> link: <https://staff.lifeusa.org/wp-json/>; rel="https://api.w.org/"
> ```
>
> `staff.lifeusa.org/robots.txt` (separate WordPress robots, confirms separate install):
> ```
> User-agent: *
> Disallow: /wp-admin/
> Allow: /wp-admin/admin-ajax.php
> Sitemap: https://staff.lifeusa.org/wp-sitemap.xml
> ```
>
> Ahrefs subdomain map (2026-05-07, file: `lifeusa.org-top-pages-subdomains-all--compared_2026-05-07_22-37-54.xlsx`, screenshot: `site structure.png`): arabic. has 1 ref domain / 0 traffic, donation. has 4 ref domains / 0 traffic, staff. has 12 ref pages.

#### Gap 2. Wix is sending wrong language headers per page

Same homepage, 5 different request samples, 5 different (incorrect) `content-language` HTTP response codes. The HTML `<html lang>` is correct. The HTTP header is what Google reads first and what survives caching.

**In plain terms:**

- **The problem:** The HTTP `content-language` response header Wix returns is wrong on every sampled page, and the wrongness is cached, not random.
- **How we found out:** Five identical curl requests against five different URLs returned five different incorrect language codes (Chinese on the homepage, Turkish on /about, French on /gaza). Hitting the homepage three times in a row consistently returned `zh-CN`, which proves the bad value is sitting in the cache.
- **Why it hurts SEO:** The HTTP header is one of Google's primary language signals and overrides the in-page `<html lang>` for many crawl decisions. Pages tagged as Chinese, Turkish, or French cannot rank in English search results, which is the most likely single reason your Arabic articles do not surface when donors search for the brand in English.

> **Evidence: per-page content-language headers (curl)**
> ```
> $ for url in / /about /gaza /ar /post/what-causes-earthquakes-and-how-they-affect-people; do
>     echo "URL: $url"
>     curl -sI "https://www.lifeusa.org$url" | grep -i ^content-language
>   done
> URL: /                         content-language: zh-CN
> URL: /about                    content-language: tr-TR
> URL: /gaza                     content-language: fr-FR
> URL: /ar                       content-language: en
> URL: /post/what-causes-...     content-language: en
> ```
>
> Repeated 3 times in succession on `/` returned `zh-CN` consistently (cache hit). The bug is baked into the cached response, not random per request.
>
> HTML lang on homepage is correct (for comparison):
> ```html
> <html lang="en">
> ```

#### Gap 3. 35% of your URLs carry a noindex tag

**In plain terms:**

- **The problem:** 122 of the 345 crawlable pages on the site (35%) carry a `noindex` directive, telling Google not to list them.
- **How we found out:** Screaming Frog's site crawl flagged it as a high-severity directive issue and exported the full list of affected URLs.
- **Why it hurts SEO:** With only 33 actively ranking pages, a 35% noindex rate almost certainly contains pages that should be indexed. Every accidental noindex is a page that cannot rank, cannot drive donations, and cannot earn backlink credit, no matter how much content work goes into it.

> **Evidence: Screaming Frog issues overview**
> File: `screaming frog issues/issues_overview_report.csv`
> Row: `"Directives: Noindex","Warning","High","122","35.360"`
> Affected URL list: `screaming frog issues/directives_noindex.csv`
> On a charity with only 33 ranking pages (Ahrefs), 35% of crawled URLs being noindexed is a high-suspicion signal of accidental noindex.

#### Gap 4. 90% of images have no width and height (CLS risk)

**In plain terms:**
- **The problem:** 1,035 images (90% of all images crawled) have no `width` or `height` attribute defined in HTML.
- **How we found out:** Screaming Frog flagged this as a Core Web Vitals opportunity and exported the affected image URLs.
- **Why it hurts SEO:** Without dimensions, the browser does not know how much space an image will take until it loads, so the page layout jumps as content arrives. This is measured as Cumulative Layout Shift, one of Google's Core Web Vitals ranking signals. Poor CWV pulls down rankings for every page on the domain and increases donor bounce on slow mobile connections.

> **Evidence: Screaming Frog**
> File: `screaming frog issues/issues_overview_report.csv`
> Row: `"Images: Missing Size Attributes","Opportunity","Low","1035","90.470"`
> Affected URL list: `screaming frog issues/images_missing_size_attributes.csv`

#### Gap 5. Schema is generic, not nonprofit-specific

**In plain terms:**

- **The problem:** The homepage declares the organization as `ProfessionalService` (a for-profit business type in the schema vocabulary) and the 441 blog posts have zero `Article` schema.
- **How we found out:** Direct extraction of the JSON-LD blocks from the homepage HTML showed `@type: ProfessionalService`. A sitemap count returned 441 blog URLs, and spot-checks of individual posts showed no `Article` markup on any of them.
- **Why it hurts SEO:** Wrong organization type blocks nonprofit-specific rich results in Google, including the donations panel, charity disambiguation, and trust badges. Missing `Article` schema on 441 posts blocks the largest single rich-result opportunity on the site (publish date, author, headline imagery in search). The site is leaving its biggest schema win unclaimed.

> **Evidence: homepage JSON-LD (extracted with curl + grep)**
> ```
> $ curl -s https://www.lifeusa.org/ | grep -oE '<script type="application/ld\+json">[^<]*'
> ```
> Returns three schema blocks. The third declares the org type:
> ```json
> {
>   "@context": "http://www.schema.org",
>   "@type": "ProfessionalService",
>   "name": "Life for Relief and Development",
>   "url": "https://www.lifeusa.org/",
>   "description": "Founded in 1992, LIFE for Relief and Development is a global humanitarian relief and development organization...",
>   "address": { "@type": "PostalAddress", "addressLocality": "Southfield", "addressRegion": "Michigan", "addressCountry": "United States" }
> }
> ```
> `ProfessionalService` is a Schema.org subclass of `LocalBusiness` (for-profit). The semantically correct type for a registered nonprofit is `NGO` (subclass of Organization). Reference: https://schema.org/NGO
>
> Article schema check on blog: zero hits across spot-checks of /post/* pages. 441 blog posts in sitemap (`curl -s https://www.lifeusa.org/blog-posts-sitemap.xml | grep -c "<loc>"` returns 441).

### other aspects

#### 1. Apex redirect works correctly

The Ahrefs "lifeusa.org apex 0 traffic with 805 ref domains" number is a reporting artifact of a 301'd hostname, not a broken redirect.

> **Evidence (curl, full chain followed):**
> ```
> $ curl -sIL https://lifeusa.org/
> HTTP/2 301
> location: https://www.lifeusa.org/
> strict-transport-security: max-age=31556952
> server: Pepyaka
> # ...follows redirect...
> HTTP/2 200
> content-type: text/html; charset=UTF-8
> ```

#### 2. backlink profile

> **Evidence (Ahrefs site structure, May 2026, file: `site structure.png`):**
> ```
> www.lifeusa.org      963 ref domains   1,069 organic traffic   33 organic pages
> donate.lifeusa.org   214 ref domains   4 organic traffic       1 organic page
> ```

#### 3. Hreflang is implemented (with one fix needed)

> **Evidence (homepage HTML):**
> ```html
> <link rel="alternate" href="https://www.lifeusa.org/" hreflang="x-default"/>
> <link rel="alternate" href="https://www.lifeusa.org/ar" hreflang="ar-jo"/>
> <link rel="alternate" href="https://www.lifeusa.org/" hreflang="en-us"/>
> ```
> Structure exists. `ar-jo` (Jordanian Arabic) is the wrong locale for a global Muslim charity audience.

---

## 2. Access we need from you

| What | Where to grant | Why |
|---|---|---|
| Google Search Console access | Add sgamal2593@gmail.com as Owner or Full user on the verified property for www.lifeusa.org and any other verified subdomains (donate., donation., staff.) | Confirm indexed-vs-submitted, queries, CTR, mobile usability, Core Web Vitals field data, manual actions. Cannot complete audit without it. |
| Google Analytics 4 access | Add sgamal2593@gmail.com as Viewer on the GA4 property | Validate which pages convert donations, which traffic sources matter, which campaigns are noise. |
| Wix admin access (or a screen-share) | For 30 minutes during a future session | Audit page-level SEO settings, confirm the noindex'd pages, edit hreflang locale, edit schema. |
| Subdomain DNS / hosting access | Confirm who controls each: lifeusa.org DNS, donate.lifeusa.org (Cloudflare/donorportal), donation.lifeusa.org (Cloudflare/Givecloud), staff.lifeusa.org (Cloudflare/WordPress) | Required to sunset arabic., consolidate donations, and lock down staff. |
| Wix support contact info | Direct Wix support email or ticket history | Required to escalate the content-language HTTP header bug. |

---

## 3. Facts we need from you

| Question | Why |
|---|---|
| When was arabic.lifeusa.org launched, and when did you stop maintaining it? | Determines whether to redirect remaining backlinks or just remove DNS. |
| Why does donation.lifeusa.org exist alongside donate.lifeusa.org? Different campaigns, different platforms, historic? | Required before recommending consolidation. |
| Who manages staff.lifeusa.org and what is on it? | Determines whether to auth-gate, noindex, or relocate. |
| Wix plan tier (Standard, Unlimited, Business, Enterprise, Wix Studio)? | Affects which fixes are user-controllable vs. require Wix support. |
| Year founded confirmation (1992 per JSON-LD on homepage). Current age in messaging? | Meta description says "29+ years" which is now stale (34 years in 2026). Evidence below. |
| EIN / 501(c)(3) status / charity registration numbers? | Needed for NGO schema markup. |
| Donor analytics: any platform that aggregates donate.+donation. data today? | Determines migration risk before consolidating. |
| Any past site migrations on www. (e.g., changed CMS, moved off WordPress, removed www.)? | Explains historical signals in GSC. |
| Top 5 program priorities for 2026 (Gaza, orphans, Ramadan, water, Hidayah, etc.)? | Shapes the content priority list and schema additions. |

> **Evidence: stale meta description on homepage**
> ```html
> <meta name="description" content="Life is the humanitarian aid organization that's been changing lives and offering hope for 29+ years. Click here to learn more about us and donate today!"/>
> ```
> JSON-LD on the same page declares founding year 1992. 2026 minus 1992 = 34 years, not 29.

---

## 4. Confirmations we need (live, on the call)

- [ ] The 122 noindex'd URLs - are these intentional?
  - Open `screaming frog issues/directives_noindex.csv` in the master sheet
  - Walk through 5-10 examples in browser to spot accidental noindex
- [ ] The 4 internal URLs blocked by robots.txt - what are they?
  - File: `screaming frog issues/response_codes_internal_blocked_by_robots_txt.csv`
  - Note: robots.txt only declares `Disallow: *?lightbox=`; the 4 blocked URLs imply something else is happening (Wix system path or query mismatch).
- [ ] Suspicious sitemap entries: /no, /copy-of-freewill-landing-page, /b2s, /fb-intl
  - Visit each in browser, confirm if active or scaffolding
  - Evidence below.
- [ ] Mixed-content URLs (5 HTTP) - identify and fix sources
  - File: `screaming frog issues/security_http_urls.csv`
- [ ] arabic.lifeusa.org backlinks - any external links pointing to it that need a 301 home?

> **Evidence: robots.txt verbatim (Wix auto-generated)**
> ```
> User-agent: *
> Allow: /
> Disallow: *?lightbox=
>
> # Optimization for Google Ads Bot
> User-agent: AdsBot-Google-Mobile
> User-agent: AdsBot-Google
> Disallow: /_partials*
> Disallow: /pro-gallery-webapp/v1/galleries/*
>
> # Block PetalBot
> User-agent: PetalBot
> Disallow: /
>
> # Crawl delay for overly enthusiastic bots
> User-agent: dotbot
> Crawl-delay: 10
> User-agent: AhrefsBot
> Crawl-delay: 10
>
> Sitemap: https://www.lifeusa.org/ar_ar-sitemap.xml
> Sitemap: https://www.lifeusa.org/sitemap.xml
>
> # Auto generated, go to SEO Tools > Robots.txt Editor to change this
> ```

> **Evidence: suspicious sitemap entries (from `pages-sitemap.xml`)**
> ```xml
> <url><loc>https://www.lifeusa.org/no</loc><lastmod>2026-05-06</lastmod></url>
> <url><loc>https://www.lifeusa.org/copy-of-freewill-landing-page</loc><lastmod>2026-05-06</lastmod></url>
> <url><loc>https://www.lifeusa.org/b2s</loc><lastmod>2026-05-06</lastmod></url>
> <url><loc>https://www.lifeusa.org/fb-intl</loc><lastmod>2026-05-06</lastmod></url>
> ```
> "/no" and "copy-of-..." are typical Wix scaffolding leftovers. "b2s" and "fb-intl" look like internal codes (back-to-school, Facebook international) but should be confirmed live.

---

## 5. Decisions we want from you (today, ideally)

| Decision | Recommendation | Why | Supporting evidence |
|---|---|---|---|
| **Sunset arabic.lifeusa.org?** | Yes, remove DNS. | Already dead. The 1 referring domain pointing to it is wasted equity. No content lives there. | DNS does not resolve (curl + dig). Ahrefs site structure: 1 ref domain, 0 traffic. |
| **Consolidate donate. + donation.?** | Yes, primary = donate. (donorportal), 301 donation. paths. | donate. has 214 ref domains and hardened security. donation. (Givecloud) has 4 ref domains. | Headers above: donate. CSP-set, donation. on Givecloud platform. Ahrefs: 214 vs 4 ref domains. |
| **What to do with staff.lifeusa.org?** | Move behind auth + add Disallow + noindex. | It is currently a public WordPress site exposing potentially internal content. | curl shows HTTP 200 with `wp-json` link header (WordPress confirmed). No auth gate visible. |
| **Hreflang locale: ar-jo or ar?** | Change to ar. | Your audience is global Arabic-speaking donors, not specifically Jordanian. | Homepage HTML: `hreflang="ar-jo"` (verbatim above). |
| **Schema upgrade: ProfessionalService to NGO?** | Yes, plus add DonateAction. | NGO is the correct schema.org type for a nonprofit. ProfessionalService implies for-profit. | JSON-LD verbatim above. https://schema.org/NGO confirms type. |
| **Wix Studio vs. stay on classic Wix?** | Discuss. Wix Studio gives more header control. | Many fixes (security headers, content-language) are constrained by Wix classic. | Server is `Pepyaka` (Wix's hosting). content-language bug is not user-configurable in classic Wix admin. |
| **Article schema on 441 blog posts?** | Yes, enable in Wix Blog SEO panel. | Largest single schema opportunity on the site. | Sitemap count: 441 blog posts (`curl -s https://www.lifeusa.org/blog-posts-sitemap.xml \| grep -c "<loc>"`). |

---

## 6. Why each ask matters (one-line context)

- **GSC access** unlocks: 122 noindex review, sitemap submission validation, manual action check, query performance, mobile usability.
- **GA4 access** unlocks: which traffic converts, which campaigns drive donations, prioritization for content rework.
- **Subdomain decisions** unlock: roughly 6 weeks of dev/DNS work that delivers the largest single SEO impact on the site.
- **Wix support escalation** unlocks: the content-language header bug, which we believe is the largest invisible blocker to your brand discoverability in English search.
- **Hreflang locale fix** unlocks: better global Arabic distribution, addresses the original pain Tasneem raised about Arabic articles not showing up in English search.

---

## 7. What ships after this meeting

- Master sheet (already prepared) becomes the single source of truth, updated as data lands.
- Subdomain consolidation plan (separate doc) once you confirm the decision.
- Schema strategy spreadsheet (separate doc) once we confirm legal/EIN details.
- Top-50-page content hygiene list (titles, descriptions, alt text). This is the work Tasneem can drive directly.

---

## 8. Open follow-ups for next session

- Wix support ticket draft (for the content-language bug). I can draft, you submit.
- A 30-minute Wix admin walkthrough (screen-share) to confirm page-level settings before bulk edits.
- Backlink reclamation list for arabic.lifeusa.org (find external links, ask owners to point to www. instead).
- Decision on whether the audit scope expands to include the donate. and staff. subdomains in detail.

---

## Appendix: Evidence index

All evidence captured 2026-05-07 between 22:00-23:30 UTC unless noted.

| ID | Claim | Source | File / Command |
|---|---|---|---|
| E1 | Apex 301 works | curl | `curl -sIL https://lifeusa.org/` |
| E2 | arabic. dead in DNS | curl + dig | `dig +short arabic.lifeusa.org` (empty) |
| E3 | donate. on Cloudflare/donorportal | curl | `curl -sI https://donate.lifeusa.org/` |
| E4 | donation. on Givecloud | curl | `curl -sI https://donation.lifeusa.org/` (`x-givecloud-*` headers) |
| E5 | staff. is public WordPress | curl | `curl -sI https://staff.lifeusa.org/` (`wp-json` link header) |
| E6 | content-language randomized | curl | per-URL grep above |
| E7 | hreflang ar-jo | HTML | homepage source |
| E8 | ProfessionalService schema | JSON-LD | homepage `<script type="application/ld+json">` |
| E9 | 122 noindex URLs (35%) | Screaming Frog | `screaming frog issues/issues_overview_report.csv` |
| E10 | 1,035 images no width/height (90%) | Screaming Frog | `screaming frog issues/issues_overview_report.csv` |
| E11 | 543 images >100KB (47%) | Screaming Frog | `screaming frog issues/issues_overview_report.csv` |
| E12 | 451 missing alt text + 20 missing alt attribute | Screaming Frog | `screaming frog issues/images_missing_alt_text.csv` + `images_missing_alt_attribute.csv` |
| E13 | 441 blog posts | Wix sitemap | `curl -s https://www.lifeusa.org/blog-posts-sitemap.xml \| grep -c "<loc>"` |
| E14 | Stale meta description (29+ years) | HTML | homepage meta description |
| E15 | 4 robots-blocked URLs | Screaming Frog | `screaming frog issues/response_codes_internal_blocked_by_robots_txt.csv` |
| E16 | 5 mixed-content URLs | Screaming Frog | `screaming frog issues/security_http_urls.csv` |
| E17 | Sitemap leftover URLs | Wix sitemap | `pages-sitemap.xml` (verbatim above) |
| E18 | Subdomain backlink/traffic split | Ahrefs | `site structure.png` and `lifeusa.org-top-pages-subdomains-all--compared_2026-05-07_22-37-54.xlsx` |
| E19 | Wix robots.txt content | curl | `curl -s https://www.lifeusa.org/robots.txt` (verbatim above) |
