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
| DIR-008 | ChamberofCommerce.com | Superseded by DIR-018 | The initial platform search was unreliable; later evidence from Cybo exposed the exact existing Southfield ChamberofCommerce.com record documented in DIR-018 | No |
| DIR-009 | Hotfrog US | New candidate, access blocked | Google returned no exact record. The active U.S. owner route redirects to `https://admin.hotfrog.com/add/index-card`, requires an account, and explicitly says verified profiles can add images, a logo, and other details | No |
| DIR-010 | Brownbook | Access blocked | Google returned no exact record, but the public site remained behind a Cloudflare security-verification screen, so owner registration and branding fields could not be verified | No |
| DIR-011 | Cylex US | New candidate, CAPTCHA blocked | Google returned no exact record. Cylex confirms free business profiles and an active registration route; the authorized flow reached account creation but stopped at reCAPTCHA. No account was created | No |
| DIR-012 | MerchantCircle | New candidate, access blocked | Google returned no exact record. MerchantCircle confirms a free basic listing with editable information and photos, but its observed `/signup` route returned 403 in the browser | No |
| DIR-013 | Cybo | Existing | Cybo's add-business duplicate step found the exact Southfield record at `https://www.cybo.com/US-biz/life-for-relief-development`; the public page links to LifeUSA but exposes stale contact data and no approved logo | No |
| DIR-014 | Nextdoor Business | New candidate, access blocked | Google returned no exact page. Nextdoor confirms a free Business Page with contact information and photos, but the claim CTA did not advance to a usable owner flow in the current browser session | No |
| DIR-015 | Alignable | New candidate, CAPTCHA blocked | Google returned no exact profile. The authorized free-signup flow accepted the mailbox and terms selection, then required reCAPTCHA. No CAPTCHA was handled and no account was created | No |
| DIR-016 | AARP Create the Good | New candidate, access blocked | Google returned no exact organization result. AARP explicitly offers nonprofits free volunteer-opportunity publication, but an AARP account is required and public logo/backlink fields remain unverified | No |
| DIR-017 | Taproot Plus | New candidate, representative details needed | Google returned no exact organization result. Taproot confirms a free nonprofit profile, publicly displays organization logos with opportunities, and exposes a valid nonprofit signup form; it requires a real representative first and last name | No |
| DIR-018 | ChamberofCommerce.com | Existing reference found | Cybo's exact Southfield record links to `chamberofcommerce.com/southfield-mi/4559853-life-for-relief-development`; resolve and claim that record instead of creating a duplicate | No |
| DIR-019 | MapQuest | Existing reference found | Cybo's exact Southfield record links to `mapquest.com/us/michigan/life-for-relief-development-6299633`; resolve the current owner/data-provider route instead of creating a duplicate | No |
| DIR-020 | Points of Light Engage | New candidate, access blocked | Google returned no exact indexed organization result. Points of Light offers nonprofit organization registration and volunteer-opportunity management, but the observed login route requires an emailed magic link; public logo and backlink fields remain unverified | No |
| DIR-021 | Bonterra Deed | Existing data record | Deed's nonprofit registration search returned the exact legal name, EIN `95-4402149`, and Southfield address. The free claim flow says claimed profiles can add a mission, logo, and verified team members, so this record must be claimed or maintained rather than counted as new | No |
| DIR-022 | Pledge | Conditional fundraising platform | Google returned no exact indexed LifeUSA page. Pledge offers free fundraising pages and maintains a charity database, but the verified route is a fundraising product rather than a routine public directory profile; any campaign or service enrollment remains separately gated | No |
| DIR-023 | Double the Donation | Existing | Google returned the exact public record at `https://doublethedonation.com/lifeusa`, including EIN `95-4402149`, the Southfield address, and a LifeUSA website link. It cannot count as new and no approved logo was visible in the logged-out page state | No |
| DIR-024 | PayPal Giving Fund | Existing | PayPal's logged-out charity search returned the exact LifeUSA record at `https://www.paypal.com/us/fundraiser/charity/2268883`. The profile exposes EIN `95-4402149` and an HTTP LifeUSA website link but no approved visible logo; enrollment also requires a charity PayPal Business account and Giving Fund terms | No |

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
| NEW-007 | ChamberofCommerce.com | Local business directory profile | Existing reference found | Cybo exposes a Southfield ChamberofCommerce.com record; resolve that record instead of creating a duplicate |
| NEW-008 | Hotfrog US | Business directory profile | New candidate, access blocked | Active U.S. registration and logo support verified; working account and email verification are required |
| NEW-009 | MerchantCircle | Local business profile | New candidate, access blocked | Free basic listing and photos verified; the signup endpoint returned 403 in the current browser session |
| NEW-010 | Brownbook | Global business listing | Access blocked | Cloudflare verification prevented direct registration and branding-field inspection |
| NEW-011 | Cylex US | Business directory profile | New candidate, CAPTCHA blocked | Free registration and no exact indexed record verified; account creation requires reCAPTCHA completion |
| NEW-012 | Cybo | Global organization listing | Existing | Exact Southfield record found with stale contact data and no approved logo; claim/update rather than duplicate |
| NEW-013 | Nextdoor Business | Local organization profile | New candidate, access blocked | Free page, photos, and contact details verified; owner claim route did not advance in the current session |
| NEW-014 | Alignable | Local business network profile | New candidate, CAPTCHA blocked | Free signup reached reCAPTCHA; no account was created and no contacts were imported |
| NEW-015 | Better Business Bureau | Charity or business profile | Conditional | BBB eligibility and any accreditation or review distinction; no paid accreditation without approval |
| NEW-016 | Dun & Bradstreet | Business identity profile | Conditional | Existing D-U-N-S record search; logo is a paid-tier feature under current published terms |
| NEW-017 | PayPal Giving Fund | Charity profile | Existing | Exact public profile `2268883` found; update its HTTP website link and logo only through the authorized charity PayPal Business account and Giving Fund terms |
| NEW-018 | GlobalGiving | Humanitarian fundraising profile | Conditional | Program eligibility, application documents, and fundraising agreement |
| NEW-019 | Pledge | Nonprofit giving profile | Conditional fundraising platform | No exact indexed LifeUSA page found, but the available route creates fundraising products rather than a routine directory profile; service enrollment remains separately gated |
| NEW-020 | Double the Donation | Matching-gift nonprofit profile | Existing | Exact public `/lifeusa` record found with the legal name, EIN, address, and LifeUSA website link; maintain rather than duplicate |
| NEW-021 | AARP Create the Good | Volunteer organization profile | New candidate, access blocked | Free nonprofit opportunity publishing is verified; AARP account and public branding fields remain gated |
| NEW-022 | Taproot Plus | Skilled-volunteer nonprofit profile | New candidate, representative details needed | Free nonprofit profile and public organization-logo display verified; signup requires a real representative name |
| NEW-023 | Catchafire | Skills-based volunteering profile | Conditional | Service agreement, eligibility, and any participation cost |
| NEW-024 | Points of Light Engage | Volunteer organization profile | New candidate, access blocked | No exact indexed record found and nonprofit registration is active; email magic-link access and public logo/backlink-field verification remain required |
| NEW-025 | Deed | Workplace giving and volunteering profile | Existing data record | Exact legal name, EIN, and Southfield record found in the free claim search; claim and enhance the existing record rather than count it as new |
| NEW-026 | Michigan Nonprofit Association | State nonprofit directory | Conditional | Existing membership or separately approved membership value and cost |
| NEW-027 | Southfield Area Chamber of Commerce | Local member directory | Conditional | Existing membership or separately approved membership value and cost |
| NEW-028 | Great Lakes Business Network or verified local equivalent | Regional business profile | Research | Exact platform identity, authority, free profile, and genuine nonprofit fit |
| NEW-029 | MapQuest business listing provider | Maps and local profile | Existing reference found | Cybo exposes the existing Southfield MapQuest record; resolve the current data-provider route |
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

The supplied mailbox password was rejected by Google during authorized Idealist sign-in. It was tried once and was not retried. Points of Light requires an emailed magic link. Cylex and Alignable reached account-creation forms but stopped at reCAPTCHA; no CAPTCHA interaction or account creation occurred. MerchantCircle's signup route returned 403. Taproot requires a real representative first and last name before account creation. Pledge and PayPal Giving Fund add fundraising or charity-account terms and are not routine free-directory submissions. Until working mailbox access is available, email-verification profiles cannot reach **Done** status. Duplicate research and no-login public verification can continue.
