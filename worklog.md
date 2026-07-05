# Worklog: LifeUSA (Life for Relief and Development)

Append-only; newest at top. Source for reports, invoices, and closeout. Entries
through 2026-06-09 reconstructed from the "Lifeusa | SEO Services | Thread" email
thread (meeting-intake), not live-tracked at the time.

## 2026-07-05
- **Done:** Completed the approved four-package orphan-cluster outline batch after correcting the topic logic: two Saiaf-owned enrichment plans for existing articles and two Saiaf-owned new informational guide plans.
- **Done:** Created source notes at `Content Framework/60-corpus/source-notes/orphan-cluster-four-outline-packages-2026-07-05.md`, documenting the user decision that rewrite means enriching the existing article with keywords, depth, links, and structure, not deleting the article, forcing a new title, or assigning it to Angela.
- **Done:** Created MD briefs, MD outlines, and HTML handoff files for: `Gaza Orphans: How War Leaves Children Without Care, Safety, and Support`; `Why Gifts for Orphans Matter: Joy, Dignity, and the Right to Childhood`; `Orphan Education After Loss: Why School Stability Matters`; and `Mental Health Support for Orphaned Children: Routine, Safety, and Care After Trauma`.
- **Done:** Generated local article-plans previews under `article-plans-and-outlines/` and updated the local article-plans index/source mapping. These are local vault/generated previews; they have not been pushed to GitHub in this pass.
- **Decision:** Rejected `Creating Beautiful Tomorrows in Orphans Today` as a broad `orphan relief` rewrite because it duplicates the planned `How To Help Orphans` pillar. Rejected a full rewrite of `Rebuilding After Loss`; only internal-link improvement is allowed unless Saiaf chooses a different angle later.
- **Done:** Prepared the writer-ready SEO brief, outline, and HTML handoff for `What Does Orphan Sponsorship Cover? A Guide for Donors`, targeting `orphans sponsorship` / `orphan sponsorship` as the next supporting article in the orphan cluster.
- **Done:** Published the noindex GitHub Pages preview at `https://saiaf25.github.io/lifeusa/article-plans-and-outlines/what-does-orphan-sponsorship-cover/` and added it to the article-plans index.
- **Done:** Corrected the sponsorship outline's internal-link guidance to include Gaza orphan support pages, including the Gaza orphan campaign, `Who Will Watch Over the Orphans of Gaza?`, Gaza food packs, Gaza mothers/orphans essentials, and Gaza winter relief.
- **Scheduled:** User confirmed the update email to Angela Joyce was prepared/scheduled on 2026-07-05 at about 02:53 Türkiye time, scheduled to send in roughly 3 hours (~05:53 Türkiye time). Treat as scheduled outgoing mail until the sent folder is verified after the send time.
- **Open:** [CLIENT: Angela] draft `What Does Orphan Sponsorship Cover? A Guide for Donors` from the outline. [ME] verify the scheduled mail after send time if needed, then review Angela's draft for SEO structure, internal links, keyword usage, donor clarity, child-privacy language, and LifeUSA-specific claim safety before publishing.
- **Done:** Created the public noindex technical SEO fixes index at `technical-seo-fixes/index.html`, intended to publish at `https://saiaf25.github.io/lifeusa/technical-seo-fixes/`. The page mirrors the article-plans index style and records verified or tracked website fixes: orphan slug redirect, Wix Blog body CSS, robots.txt cleanup, `/programsss` redirect, copy-of gallery cleanup blocker, and the GSC-driven technical workstream.
- **Done:** Added the source handoff file at `Content Framework/70-outputs/handoff/technical-seo-fixes-index.html` and registered it in `tools/sync_article_outline.py` as `technical-seo-fixes-index` so future sync runs can regenerate the live GitHub Pages file.
- **Done:** Verified in Zoho Mail that the article update email was sent from `hello@saiaf.me` in the existing `LifeUSA | Article Planning and Publishing | Ongoing Thread` to Angela Joyce, cc Dr. Hany Saqr, at 2026-07-05 00:19 Türkiye time. Subject in thread: `RE: LifeUSA | Article Planning and Publishing | Ongoing Thread`.
- **Done:** The sent update referenced the Wednesday meeting about rewriting the old orphan guide, and summarized the completed workflow: research and outline, rewrite and live page, slug change, redirect from the old URL, and Wix blog-body CSS setup.
- **Done:** Published/live URL shared in the sent email: `https://www.lifeusa.org/post/what-is-an-orphan`. Outline URL shared: `https://saiaf25.github.io/lifeusa/article-plans-and-outlines/what-is-an-orphan-causes-statistics-how-you-can-help/`. Redirect proof was also shared via CleanShot link.
- **Done:** Published the full evergreen rewrite of the old LifeUSA blog post `The Leading Causes of Orphans Today` as `What Is an Orphan? Causes, Statistics, and How You Can Help`.
- **Done:** Changed the Wix Blog slug from `/post/the-leading-causes-of-orphans-today` to `/post/what-is-an-orphan` and preserved a redirect from the old URL to the new URL.
- **Verified:** `https://www.lifeusa.org/post/the-leading-causes-of-orphans-today` returns `301` to `https://www.lifeusa.org/post/what-is-an-orphan`; following redirects returns `status=200`, `redirects=1`, `final_url=https://www.lifeusa.org/post/what-is-an-orphan`.
- **Verified:** The live rewritten page exposes the new title, updated schema URL/headline, fresh orphan definition/culture/statistics/help content, and restored internal links to the widowhood article, orphan support examples, and the orphan support donation page.
- **Decision:** The rewritten page is now the evergreen context article for the orphan cluster targeting `what is an orphan`; the future `How To Help Orphans` post remains the practical pillar once published.
- **Done:** Added and tested a Wix Custom Code / Custom Embed approach for LifeUSA blog post reading styles on the Wix Blog post template. The embed is named `LifeUSA Blog Post Reading Spacing` and uses Wix custom embed ID `aea11c11-3ab2-4974-9cc9-59a3ac2dead5`.
- **Done:** User corrected the Wix page scope from all pages to the blog post page type (`pageFilter.pageIds: ["txdi5"]`). This keeps the styling constrained to `/post/` blog pages rather than homepage, donation, or other non-blog pages.
- **Done:** Verified the first saved CSS was present on the live post but ineffective because Wix Blog rendered article `h2`, `h3`, and `p` nodes with zero computed margins. Browser testing confirmed the working fix requires targeting Wix blog viewer nodes with selectors such as `main :is(h1,h2,h3,h4,h5,h6)[id^="viewer-"]` and `main p[id^="viewer-"]`, plus `!important`.
- **Done:** Final working CSS pattern sets comfortable heading and paragraph spacing, colors `h2` headings `#0a2b47`, and styles body links in the guide with `color: #0a2b47 !important` and `font-weight: 700 !important`.
- **Verified:** On the live article `https://www.lifeusa.org/post/the-leading-causes-of-orphans-today`, temporary browser injection changed paragraph spacing from `0px` margins to about `15.3px` top/bottom and changed an `h2` sample to about `43.4px` top / `18.2px` bottom. User confirmed the stronger spacing code was working before requesting the link and `h2` color additions.
- **Decision:** Future LifeUSA Wix Blog styling should use one named Custom Code entry on the post page type, update that existing entry instead of creating duplicates, and verify computed styles in the live browser because Wix Blog generated classes and resets can override normal element selectors.

## 2026-06-27
- **Done:** Built the second orphan-cluster writer-ready SEO brief, outline, and HTML handoff: `Can Zakat Be Used To Sponsor an Orphan?`.
- **Done:** Published the shareable noindex preview at `https://saiaf25.github.io/lifeusa/article-plans-and-outlines/can-zakat-be-used-to-sponsor-an-orphan/`.
- **Done:** Cleaned client/team-facing preview pages so internal technical appendices and adversarial-review material do not appear in the shared HTML. Added sync guardrails in `tools/sync_article_outline.py` so future article previews strip internal sections before GitHub Pages publishing.
- **Done:** Drafted the Zoho reply in the existing `LifeUSA | Article Planning and Publishing | Ongoing Thread` from `hello@saiaf.me` to Angela Joyce, cc Tasneem Elridi, Hala Sanyurah, and Hany Saqr. User confirmed the reply was sent manually after the draft was saved in Zoho.
- **Decision:** This article is a supporting cluster article under the `How To Help Orphans` pillar, not a replacement for the pillar. It answers the narrower donor question of whether orphan sponsorship can be treated as zakat and what needs to be clear before making that claim.
- **Decision:** Zakat wording must remain cautious until LifeUSA confirms the final policy, fund designation, eligibility assessment, and distribution mechanism. The draft should avoid claiming that a specific LifeUSA orphan donation designation is zakat-eligible before internal confirmation.
- **State change:** Deliverable 9 `Can Zakat Be Used To Sponsor an Orphan? supporting cluster brief, outline, live handoff, and team email` moved to `delivered / writer review pending`.
- **Open:** [CLIENT: Angela] draft the supporting cluster article from the outline. [ME] review the draft for SEO structure, internal links, keyword usage, donor-facing clarity, and zakat-related policy safety before publishing.
- **Notes:** Main artifacts live at `Content Framework/70-outputs/briefs/orphans/can-zakat-be-used-to-sponsor-an-orphan.md`, `Content Framework/70-outputs/outlines/orphans/can-zakat-be-used-to-sponsor-an-orphan.md`, and `Content Framework/70-outputs/handoff/orphans/can-zakat-be-used-to-sponsor-an-orphan.html`.

## 2026-06-26
- **Done:** Built the first writer-ready SEO brief, outline, and HTML handoff for the LifeUSA orphan content cluster: `How To Help Orphans`.
- **Done:** Published the shareable noindex preview at `https://saiaf25.github.io/lifeusa/article-plans-and-outlines/how-to-help-orphans/`.
- **Done:** Created reusable LifeUSA SEO article-outline playbook at `Content Framework/90-ops/playbook-lifeusa-seo-article-outline.md` so future LifeUSA article briefs follow the same source hierarchy, Alraedah-style structure, URL checks, keyword-volume rules, Ahrefs SERP-feature checks, internal-link guidance, writer notes, and adversarial review.
- **Done:** Drafted the Zoho email from `hello@saiaf.me` to Angela Joyce, cc Tasneem Elridy, Hala Sanyurah, and Dr. Hany Saqr. User confirmed the email was sent manually.
- **Decision:** Saiaf framed `How To Help Orphans` as a pillar page and the starting point for a broader orphans and widows content cluster, not only a follow-up from the Wednesday SEO and Web Copy meeting.
- **Decision:** Angela should treat the article as a practical list-style guide and use the outline structure as the starting point for the full draft. Angela is also invited to share feedback on the outline structure because it will be reused for future LifeUSA articles.
- **State change:** Deliverable 8 `Content workflow: How To Help Orphans pillar brief, outline, and live handoff` moved to `delivered`. It is not `accepted`; client/writer feedback is still pending.
- **Open:** [CLIENT: Angela] write the first full draft from the outline and share feedback on the outline structure. [ME] review Angela's draft for SEO structure, keyword usage, internal links, and alignment with the cluster plan before publishing.
- **Notes:** Main handoff artifacts live under `Content Framework/70-outputs/briefs/orphans/`, `Content Framework/70-outputs/outlines/orphans/`, and `Content Framework/70-outputs/handoff/orphans/`. GitHub Pages preview uses the team-share path `article-plans-and-outlines/how-to-help-orphans/` and is noindex.

## 2026-06-23
- **Done:** Found LifeUSA finance/payment-process email from Sharon Leonard (`Payment for your Services`, 2026-06-23). She requested monthly invoices including day/date/service description plus completed and signed attached forms. Created first-month retainer invoice `LIFEUSA-2026-06` for US$600, service period 2026-06-05 to 2026-07-04, payment due on receipt. Payment is not marked paid.
- **Done:** Checked the connected Zoho Mail account `hello@saiaf.me` for LifeUSA threads and updated `meetings/mail-threads.md` from Zoho evidence.
- **Found:** New content/copywriter training thread with Angela Joyce, Tasneem Elridi, and Hala Sanyurah. Calendar invitation is accepted for **2026-06-24 17:00-17:40 Türkiye time** ("SEO & Web Copy Discussion"). First-session focus should be choosing blog topics and keywords from real search demand; future topics requested/outlined include AI visibility, article structure, report-to-blog workflows, clearer web copy, image visibility, topic clusters, and pillar pages.
- **Found:** Gallery URL cleanup thread. Angela reviewed the classification sheet but explicitly deferred exception and classification decisions to Humza because she is not familiar enough with URL usage across website, campaigns, or workflows. Saiaf replied that he is waiting for Humza to review the file. Do not proceed with redirects/noindex/removals from Angela's reply alone.
- **Found:** Salesforce-hosting access request sent to Humza on 2026-06-20 for robots, minor redirects, and XML sitemap optimization on subdomains mentioned in a meeting. No reply found in Zoho during this check.
- **Open:** [ME] prepare 2026-06-24 content/copywriter session; [CLIENT: Humza] review gallery classification sheet; [CLIENT: Humza] respond to Salesforce-hosting access request.

## 2026-06-20
- **Done by Saiaf in Wix:** Updated and verified the live `https://www.lifeusa.org/robots.txt` through Wix SEO Tools / Robots.txt Editor. Current live file allows the main site, blocks Wix lightbox/internal gallery crawl traps, keeps PetalBot blocked, applies crawl delay for Dotbot and AhrefsBot, and declares both `https://www.lifeusa.org/ar_ar-sitemap.xml` and `https://www.lifeusa.org/sitemap.xml`.

## 2026-06-13
- **Done:** Updated communication logs after user confirmed GoDaddy access and shared Gmail access are both available. This closes the previous `lifeusa3@gmail.com` 2FA access blocker from the local engagement tracker.
- **Done:** Checked Gmail MCP against LifeUSA terms and known thread ids. The connector can see a mailbox, but LifeUSA searches returned no results and the recorded thread ids returned `NOT_FOUND`; do not treat Gmail MCP as current evidence for this thread until the correct mailbox/scope is reconnected.
- **Done:** Installed and configured `gogcli` for `sgamal2593@gmail.com` Gmail read access. OAuth succeeded after Gmail API was enabled for the OAuth project. Verified read-only search with `--gmail-no-send`; `gogcli` can see LifeUSA threads that Gmail MCP cannot.
- **Done:** Confirmed from `gogcli` that the LifeUSA Gmail thread continued on 2026-06-12: Humza helped with Google login verification and Saiaf replied that access was available. No verification codes or credentials recorded.
- **Done:** Found Google platform notifications: Search Console Domain property `lifeusa.org` was recently verified; Search Console property `lifeusa.org` is associated with GA4 property `lifeusa.org - GA4`; Google Analytics account `LifeUSA` (`397813274`) was moved to the rubbish bin and is scheduled for permanent deletion in 35 days from 2026-06-12.
- **Done:** Checked Cloudflare MCP accounts for `lifeusa.org`. No `lifeusa.org` zone exists under `Sgamal2593@gmail.com's Account` or the `Alsabeel.org` account. This supports the existing conclusion that LifeUSA DNS/registrar work is through GoDaddy, not Cloudflare.
- **Open:** [ME] restore or intentionally confirm deletion of GA account `LifeUSA` (`397813274`); [ME] verify that the active GA4 property `lifeusa.org - GA4` matches the known live tag `G-5BSK8SRF9B`; [CLIENT] confirm GTM access/ownership for known container `GTM-TM7G4WZ`; [ME] continue from GoDaddy, Wix, shared Gmail, GSC, and GA4 access for domain/site investigation.

## 2026-06-10
- **Done:** Accepted both access invites. Wix collaborator + GoDaddy account access now active.
- **Done:** Identified the website host (DNS + HTTP header fingerprint). Website is hosted on **Wix** (A records `185.230.63.x`, `www` CNAME -> `cdn1.wixdns.net`, `Pepyaka` server + `x-wix-request-id`, Fastly/Google CDN fronting). **GoDaddy** is only the domain registrar / DNS manager (nameservers `ns31/ns32.domaincontrol.com`). Email is on **Microsoft 365** (MX -> outlook.com, SPF spf.protection.outlook.com). ⇒ Humza's "is hosting on GoDaddy" question resolved: no separate host; Wix is the host, GoDaddy holds the domain/DNS. Wix + GoDaddy access fully covers the hosting/domain side.
- **Done:** Drafted a thread reply to Humza (Gmail draft `r8237027351866630171`, awaiting manual send) confirming GoDaddy access received, stating the Wix-vs-GoDaddy split, and asking (a) help past 2FA on lifeusa3@gmail.com, (b) whether GA4/GTM/GSC already exist.
- **Notes (from thread, correcting earlier reconstruction):**
  - Contract IS signed. 2026-06-09 07:02 `hello@saiaf.me` -> Dr. Saqr thanked him for signing and sent first-month payment details. The "countersigned PDF not returned" open item is closed.
  - 2026-06-09 14:12 Humza -> Saiaf: invites sent; shared Google account provided: `lifeusa3@gmail.com` with credential in the email thread. Do not store or repeat the credential in vault notes. Historical blocker: 2FA blocked login at this point.
  - 2026-06-10 11:01 `hello@saiaf.me` -> Humza: thanked for Wix access, flagged still waiting on hosting access and needing Google login support. (Superseded by the 2026-06-13 access update.)
- **Superseded open item:** Google login support for `lifeusa3@gmail.com` and broad GA4/GTM/GSC confirmation were still open on 2026-06-10. As of 2026-06-13, shared Gmail access is confirmed, GSC is verified and associated with GA4, and the current open items are GA account restore/cleanup, active GA4/tag verification, and GTM access/ownership confirmation.

## 2026-06-09
- **Done:** Replied to Humza Amir. Confirmed Wix + GoDaddy access is sufficient if hosting is on GoDaddy; asked whether GTM + GA4 already exist (access if yes, set up from scratch if no). Asked access be sent to sgamal2593@gmail.com.
- **Historical blocker, superseded 2026-06-13:** Access had not yet been provisioned by Humza Amir at this point. Current state: Wix, GoDaddy, shared Gmail, GSC, and GA4 association are available; GA cleanup and GTM access/ownership remain open.
- **Notes:** Full audit sheet shared with client as a Google Sheet (Drive link in thread).

## 2026-06-08
- **Decision:** Engagement authorized. Dr. Hany Saqr (CEO) emailed his web team: "We hired a consultant, Mr. Sayaf, to help us with digital marketing." Humza Amir (Web Master) agreed to grant Wix + GoDaddy access.
- **State change:** Engagement effectively active (CEO authorization). Historical note: the countersigned agreement PDF had not been returned at this point; later thread reconstruction marked the contract signed.
- **Notes:** Implementation contact established: Humza Amir `<mamir@lifeusa.org>`.

## 2026-06-07
- **Done:** Follow-up email to Dr. Saqr chasing (a) contract signature status and (b) access (Search Console, GA4, GTM, Wix admin, DNS/hosting), and requesting a dev-team working session to begin.
- **Historical blocker, superseded 2026-06-13:** Awaiting client response on signature + access at this point. Current state: contract signed; Wix, GoDaddy, shared Gmail, GSC, and GA4 association are available; GA cleanup and GTM access/ownership remain open.

## 2026-06-05
- **Done:** Sent the prepared and consultant-signed SEO consulting agreement to Dr. Saqr for countersignature. Sent a plain-language site-status summary (the 5 confirmed gaps) and the full audit sheet link. Notified client that future email comes from hello@saiaf.me.
- **Decision:** Verbal/email go-ahead; Dr. Saqr replied "I hope we can work together."
- **Notes (audit summary sent to client):** strong authority (963 referring domains) but only ~33 pages rank; ~35% of crawled pages carry noindex; 5 parallel subdomains (www, donate, donation, staff, arabic) splitting equity + donor data (arabic. dead in DNS, staff. a public WordPress, donation. duplicates donate.); /ar reports itself as English with hreflang ar-jo (Jordan-only); schema marks the org as for-profit "ProfessionalService" not "NGO"; 463 blog posts lack Article schema; ~90% of images lack dimensions/alt (CWV + image search). ⚠️ Donor-data fragmentation is a charity-specific concern.
- **Billable:** retainer (US$600/mo flat); pre-engagement audit + setup not separately billed.

## Pre-engagement (2026-05-07 to 05-08, before signing)
- Technical SEO audit of lifeusa.org: Screaming Frog crawl, 54 issues logged. Built the Technical SEO master sheet (delivered). Produced the kickoff agenda and bilingual reality-check 1-pager. These are grounding/sales artifacts, delivered before the retainer started.
