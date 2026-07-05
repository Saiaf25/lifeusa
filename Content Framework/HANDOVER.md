# Handover

Created: 2026-06-26  
Framework: LifeUSA Content Framework  
Location: `/Users/saiaf/Downloads/obsidian/clientops-files/Freelance/lifeusaorg/Content Framework`

## What was created

This folder now contains a populated content framework for LifeUSA using the Makeen operating structure:

- Strategy spine in `00-strategy/`
- Production skill files in `10-skills/`
- Pipeline and pre-publish review checklist in `20-pipeline/`
- Starter inventory, findings, and opportunity map in `30-inventory/`
- Pillar and cluster architecture in `40-clusters/`
- Source corpus plan and URL lists in `60-corpus/`
- Output lifecycle folders in `70-outputs/`
- Cadence, changelog, and daily status review in `90-ops/`

## What source material was used

The first build is grounded in local LifeUSA sources:

- Engagement source of truth: `engagement.md`
- Running work evidence: `worklog.md`
- Gmail and Zoho-derived communications: `meetings/mail-threads.md`
- Live Zoho Mail MCP verification from `hello@saiaf.me` on 2026-06-26
- Performance data: `reports/LifeUSA-GSC-180-day-audit.md`
- Sitemap and duplicate URL evidence: `reports/live-sitemap-urls-2026-06-20.txt`, `reports/copy-url-urgent-action.md`
- Gallery cleanup communications: `reports/gallery-url-review-email-draft.md`
- Existing content architecture work: `LifeUSA-How-To-Help-Orphans-Pillar-Cluster-Plan.md`
- Program extraction work: `LifeUSA-Widow-Campaigns-and-Programs.md`
- Technical audit grounding: `grounding/`, Screaming Frog issue CSVs, and the technical SEO master sheet

## Live Zoho Mail verification

- Zoho Mail MCP was logged in and verified against account `hello@saiaf.me`.
- Live reads confirmed the `Content Creation, SEO and AI` thread, the gallery URL cleanup thread, the Salesforce-hosting access thread, and the Fireflies recap for `SEO & Web Copy Discussion`.
- The currently callable Gmail connector is authenticated as `s.gamal@ttp.sa`, so Gmail was not used as the primary LifeUSA mail source in this final pass.
- No fresh live GSC export was pulled during this framework build. The performance source remains the existing 2026-06-13 GSC audit.

## Assumptions

- LifeUSA content work is currently English-first with Arabic support, not a fully separate Arabic editorial program yet.
- Angela Joyce, Hala Sanyurah, and Tasneem Elridy are the content-training audience; Humza remains the implementation and URL decision contact.
- Donation, sponsorship, program, image visibility, report-to-blog, and AI-readable structure are the main content training needs from the email thread.
- The 2026-06-24 content session covered keyword research, pillar pages and clusters, duplicate-content cleanup, campaign-relevant keywords, backlink routing to campaign pages, and AI-assisted content workflow, based on the Fireflies recap email.

## Human review needed

Review these files first:

1. `00-strategy/01_north-star.md`
2. `00-strategy/02_audience.md`
3. `00-strategy/05_offerings-and-boundaries.md`
4. `40-clusters/cluster-architecture.md`
5. `20-pipeline/review-checklist.md`

The biggest judgment call is how aggressively to separate evergreen program education from campaign-specific donation pages.

## Live mail deltas from Zoho

- Content training: Angela confirmed the topic direction and scheduling. Fireflies recap says the meeting covered keyword research, content clustering, AI tools, duplicate content, backlink strategy, and team workflow.
- Gallery cleanup: Angela deferred exception decisions to Humza. Humza later replied that he was reviewing the sheet and would provide feedback. Treat cleanup as pending Humza feedback, not approved.
- Salesforce: Humza confirmed donation forms are created using Salesforce and said he can CC Mohamad Zamzam because he does not have permissions to create Salesforce users.
- Payment: Sharon requested monthly invoices plus completed and signed forms; a reply with completed forms, signed contract, and invoice was sent.

## Next best content action

Current orphan-cluster state:

- `What Is an Orphan? Causes, Statistics, and How You Can Help`: full rewrite of the old `The Leading Causes of Orphans Today` post is published live at `https://www.lifeusa.org/post/what-is-an-orphan`. The old slug `https://www.lifeusa.org/post/the-leading-causes-of-orphans-today` redirects to the new slug. This is now the evergreen context article for definitions, causes, statistics, cultural-language nuance, and support pathways. Angela Joyce and Dr. Hany Saqr were notified in the existing Zoho article-planning thread on 2026-07-05, with the outline link, live page, redirect proof, and Wix blog-body CSS setup note.
- `How To Help Orphans` pillar: brief, outline, noindex GitHub Pages handoff, and team email delivered on 2026-06-26. Angela draft pending.
- `What Does Orphan Sponsorship Cover? A Guide for Donors`: supporting sponsorship guide prepared with brief, outline, noindex GitHub Pages handoff, and article-plans index entry at `https://saiaf25.github.io/lifeusa/article-plans-and-outlines/what-does-orphan-sponsorship-cover/`. It targets `orphans sponsorship` / `orphan sponsorship`, uses the established orphan sponsorship donation CTA, and includes Gaza orphan support pages plus country sponsorship recaps as internal-link/proof examples. User confirmed the Angela update email was scheduled on 2026-07-05 around 02:53 Türkiye time to send roughly 3 hours later (~05:53 Türkiye time); verify sent mail later before treating it as delivered.
- Saiaf-owned four-package outline batch: source notes, MD briefs, MD outlines, HTML handoffs, and local article-plans previews created for `Gaza Orphans: How War Leaves Children Without Care, Safety, and Support`, `Why Gifts for Orphans Matter: Joy, Dignity, and the Right to Childhood`, `Orphan Education After Loss: Why School Stability Matters`, and `Mental Health Support for Orphaned Children: Routine, Safety, and Care After Trauma`. Rewrite means enrichment of the existing article with keywords, depth, structure, and links; it does not mean deletion, forced title changes, or Angela ownership.
- `Can Zakat Be Used To Sponsor an Orphan?` supporting cluster article: brief, outline, noindex GitHub Pages handoff, and team email delivered on 2026-06-27. Angela draft pending.
- Zakat article guardrail: final publication must not claim a specific LifeUSA orphan donation designation is zakat-eligible until LifeUSA confirms the current policy, fund designation, eligibility assessment, and distribution mechanism.

Next best content action:

- Wait for Angela's pillar, sponsorship-cover, and approved zakat-related drafts.
- Verify the scheduled sponsorship-outline email in sent mail after the scheduled send time if a current proof point is needed.
- Saiaf to review the four Saiaf-owned orphan outline packages and choose which rewrite/new guide to execute first.
- Review each draft for SEO structure, keyword usage, internal links, donor clarity, dignity/accuracy, and LifeUSA-specific claim safety.
- After draft review, update the framework inventory with the final Wix post URL and publication status.

## Verification summary

Run these checks after any future large edit:

```bash
find "Content Framework" -maxdepth 3 -type f | sort
rg -n "Makeen|real estate|Saudi-buyer|renter|housing support" "Content Framework"
rg -n "\\[\\[\\.\\.|\\[\\[60-corpus/" "Content Framework"
```

At creation time, Makeen references should appear only in this handover, the README, and verification notes as structural-reference context.
