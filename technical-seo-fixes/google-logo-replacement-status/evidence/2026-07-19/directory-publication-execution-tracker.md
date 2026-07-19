# LifeUSA directory publication execution tracker

Started July 19, 2026 under goal `Publish approved new directory and business profiles`.

## Goal

Publish and verify at least 20 genuinely relevant **new** LifeUSA directory or business profiles. A profile counts as done only when its logged-out public page displays an approved current logo and links to `https://www.lifeusa.org/`.

No credential or password is stored in this tracker. Paid plans, memberships, fundraising contracts, and account recovery remain separately gated.

## Status definitions

- **Research:** Fit and public-profile capability still need verification.
- **New candidate:** No existing LifeUSA record found and a legitimate creation route exists.
- **Existing:** A LifeUSA record already exists; do not create a duplicate and do not count it as new.
- **Access blocked:** The platform or mailbox requires access not currently available.
- **Submitted:** A profile was submitted but is not publicly verified.
- **Moderation pending:** The platform confirmed review is pending.
- **Done:** Logged-out public profile, approved logo, and canonical HTTPS backlink all verified.
- **Conditional:** Fee, membership, fundraising agreement, or another material decision is required.

## Verified browser findings

| ID | Platform | Status | Browser evidence | Counts toward 20 |
|---|---|---|---|---:|
| DIR-001 | Every.org | Existing | EIN `95-4402149` resolves to `https://www.every.org/lifeusa`; Every.org says the profile already has an administrator | No |
| DIR-003 | Benevity Causes | Existing | Public profile `https://causes.benevity.org/causes/840-954402149` is already registered to a masked `lifeusa.org` owner; it exposes stale mission copy and an HTTP website link | No |
| DIR-004 | Idealist | Access blocked | Exact organization-plus-Southfield search returned zero results, so it is a legitimate new candidate. Account creation could not continue because Google rejected the supplied mailbox password | No |
| DIR-005 | VolunteerMatch | Existing platform merged | VolunteerMatch now routes organization onboarding through Idealist and is not a second independent directory | No |
| DIR-006 | Yelp for Business | Existing | Google returned the established public record at `https://www.yelp.com/biz/life-for-relief-and-development-southfield`; Yelp's device-verification screen prevented a deeper logged-out field audit | No |
| DIR-007 | Manta | Existing data record | Manta-indexed category results already reference “Life For Relief And Development Inc.” in Southfield, so a new listing would risk duplication; the direct record still needs owner-route resolution | No |
| DIR-008 | ChamberofCommerce.com | Research | Google returned no exact record, but the platform's own exact-name and city search produced repeated unrelated placeholder-like results. Do not submit until the duplicate-search defect and free logo capability are resolved | No |
| DIR-009 | Hotfrog US | New candidate, access blocked | Google returned no exact record. The active U.S. owner route redirects to `https://admin.hotfrog.com/add/index-card`, requires an account, and explicitly says verified profiles can add images, a logo, and other details | No |
| DIR-010 | Brownbook | Access blocked | Google returned no exact record, but the public site remained behind a Cloudflare security-verification screen, so owner registration and branding fields could not be verified | No |
| DIR-011 | Cylex US | New candidate, CAPTCHA blocked | Google returned no exact record. Cylex confirms free business profiles and an active registration route; the authorized flow reached account creation but stopped at reCAPTCHA. No account was created | No |

## New-profile execution pool

This is a quality-controlled research pool, not a claim that every route is already eligible or free. Each row must pass duplicate search, logo support, website-link support, and terms review before submission.

| ID | Platform | Profile type | Current state | Gate before submission |
|---|---|---|---|---|
| NEW-001 | Idealist | Nonprofit and volunteer organization | New candidate, access blocked | Working mailbox authentication and email verification |
| NEW-002 | Apple Business Connect | Local business and brand profile | Research | Apple business account, company verification, and location ownership |
| NEW-003 | Bing Places | Local business profile | Research | Duplicate search, Microsoft or approved Google sign-in, and business verification |
| NEW-004 | Yelp for Business | Local business profile | Existing | Established Southfield record found; resolve its owner route instead of creating a duplicate |
| NEW-005 | Foursquare | Location and entity profile | Research | Duplicate venue search and authorized claim route |
| NEW-006 | Manta | Business directory profile | Existing data record | Resolve the indexed Southfield record and owner route; do not create a duplicate |
| NEW-007 | ChamberofCommerce.com | Local business directory profile | Research, unreliable search | Its direct search returned unrelated repeated results; verify data quality and free logo support before use |
| NEW-008 | Hotfrog US | Business directory profile | New candidate, access blocked | Active U.S. registration and logo support verified; working account and email verification are required |
| NEW-009 | MerchantCircle | Local business profile | Research | Duplicate search and active free account route |
| NEW-010 | Brownbook | Global business listing | Access blocked | Cloudflare verification prevented direct registration and branding-field inspection |
| NEW-011 | Cylex US | Business directory profile | New candidate, CAPTCHA blocked | Free registration and no exact indexed record verified; account creation requires reCAPTCHA completion |
| NEW-012 | Cybo | Global organization listing | Research | Duplicate search and public-logo capability |
| NEW-013 | Nextdoor Business | Local organization profile | Research | Eligibility for nonprofit office and location verification |
| NEW-014 | Alignable | Local business network profile | Research | Nonprofit fit, public profile, and no mandatory outreach behavior |
| NEW-015 | Better Business Bureau | Charity or business profile | Conditional | BBB eligibility and any accreditation or review distinction; no paid accreditation without approval |
| NEW-016 | Dun & Bradstreet | Business identity profile | Conditional | Existing D-U-N-S record search; logo is a paid-tier feature under current published terms |
| NEW-017 | PayPal Giving Fund | Charity profile | Research | Enrollment state, charity-account owner, fundraising terms, and logo field |
| NEW-018 | GlobalGiving | Humanitarian fundraising profile | Conditional | Program eligibility, application documents, and fundraising agreement |
| NEW-019 | Pledge | Nonprofit giving profile | Research | Existing EIN record, claim route, and public branding capability |
| NEW-020 | Double the Donation | Matching-gift nonprofit profile | Research | Existing record, nonprofit verification, and public organization page |
| NEW-021 | AARP Create the Good | Volunteer organization profile | Research | Organization eligibility and live public profile capability |
| NEW-022 | Taproot Plus | Skilled-volunteer nonprofit profile | Research | 501(c)(3) eligibility, organization review, and public profile |
| NEW-023 | Catchafire | Skills-based volunteering profile | Conditional | Service agreement, eligibility, and any participation cost |
| NEW-024 | Points of Light Engage | Volunteer organization profile | Research | Organization onboarding route and public branding fields |
| NEW-025 | Deed | Workplace giving and volunteering profile | Research | Nonprofit enrollment and public profile capability |
| NEW-026 | Michigan Nonprofit Association | State nonprofit directory | Conditional | Existing membership or separately approved membership value and cost |
| NEW-027 | Southfield Area Chamber of Commerce | Local member directory | Conditional | Existing membership or separately approved membership value and cost |
| NEW-028 | Great Lakes Business Network or verified local equivalent | Regional business profile | Research | Exact platform identity, authority, free profile, and genuine nonprofit fit |
| NEW-029 | MapQuest business listing provider | Maps and local profile | Research | Current authorized data-provider route; do not create a duplicate via a reseller |
| NEW-030 | Local.com or current successor | Local business directory profile | Research | Confirm platform is active, indexed, and permits authoritative owner updates |

## Standard public data

- Legal name: Life for Relief and Development
- Public name: LifeUSA, where supported
- EIN: `95-4402149`
- Website: `https://www.lifeusa.org/`
- Address: `17300 W 10 Mile Rd, Southfield, MI 48075`
- Mailing address: `PO BOX 236, Southfield, MI 48037`
- Main phone: `1-800-827-3543`
- Public email: `info@lifeusa.org`
- Founded: 1992; nonprofit status recorded in 1993
- Canonical square logo: `https://static.wixstatic.com/media/af2a6c_49a4190c354746b493c123d311222fb5~mv2.png`
- Canonical horizontal logo: `https://static.wixstatic.com/media/af2a6c_1bd1137d792b44c3855d26ee4cfcced0~mv2.png`

## Source description variants

### Nonprofit directory

Life for Relief and Development USA, also known as LifeUSA, is a global humanitarian nonprofit founded in 1992. It provides emergency relief, health care, education, clean water, orphan support, and community-development assistance without discrimination based on race, religion, color, or cultural background.

### Volunteer directory

LifeUSA connects people with humanitarian service that supports communities affected by disasters, conflict, hunger, limited access to clean water, and other crises. Volunteers help extend programs in emergency relief, health, education, orphan support, and community development.

### Local business profile

Life for Relief and Development is a Southfield, Michigan-based nonprofit humanitarian organization serving communities in crisis in the United States and internationally. Founded in 1992, LifeUSA provides emergency relief and long-term programs in health, education, clean water, orphan support, and community development.

## Current blocker

The supplied mailbox password was rejected by Google during authorized Idealist sign-in. It was tried once and was not retried. Cylex also reached an account-creation form but stopped at reCAPTCHA; no CAPTCHA interaction or account creation occurred. Until working mailbox access is available, email-verification profiles cannot reach **Done** status. Duplicate research and no-login public verification can continue.
