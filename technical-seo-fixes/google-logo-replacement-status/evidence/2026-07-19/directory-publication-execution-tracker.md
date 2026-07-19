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
- **Published, logo incomplete:** A new public profile and canonical backlink are verified, but the approved logo is absent, so the profile does not count yet.
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
| DIR-025 | Apple Maps | Existing | Apple Maps returned the exact Southfield charity record with the correct address, phone, and a stale HTTP website link. Its claim route resolves to Apple Business Connect claim ID `6959862997556437473`; maintain that record rather than duplicate it | No |
| DIR-026 | Bing Maps | Existing, verified business | Bing Maps returned the exact verified Southfield record under YP ID `YN1AFB07F61C79BF68`. It links through the stale HTTP LifeUSA URL and exposes Facebook-sourced photos, so it is an existing-profile correction route | No |
| DIR-027 | Foursquare | Existing | Foursquare's owner search returned the exact “Life For Relief & Development” nonprofit record at the Southfield address. The active owner route is `https://business.foursquare.com/`; do not create a duplicate | No |
| DIR-028 | EZlocal | Access blocked | Google returned no exact indexed record, but the public site stopped at Cloudflare security verification. Duplicate status, free owner route, and logo support could not be verified without interacting with the challenge | No |
| DIR-029 | CitySquares | Existing | CitySquares' own exact search returned `https://citysquares.com/b/life-for-relief-development-10255230` with the correct address, phone, and an HTTP LifeUSA link but no visible approved logo | No |
| DIR-030 | ShowMeLocal | Access blocked | Google returned no exact indexed record, but the public site rendered an empty document in the browser. Duplicate status, owner route, and logo support remain unverified | No |
| DIR-031 | Opendi | Submitted, public receipt unverified | The authorized free submission flow accepted the organization, canonical website, public contact details, Southfield address, no stated hours, and two relevant categories. The flow returned to a blank first step without a confirmation ID, and an immediate public exact search still returned no result | No |
| DIR-032 | My Local Services | Conditional paid listing | The platform advertises a full-page listing for `$2` and says listings are manually approved. Any payment or paid listing remains separately gated | No |
| DIR-033 | Local.com | Ineligible current platform | The current site is an expert-review and top-ten content publisher, not an active owner-managed local business directory submission route | No |
| DIR-034 | Callupcontact | Published, logo incomplete | A new public profile is live at `https://www.callupcontact.com/b/businessprofile/Life_for_Relief_and_Development/10168407` with the exact name, address, phone, description, and canonical HTTPS backlink. Logged-out inspection found no visible approved logo or canonical image asset, so it does not count | No |
| DIR-035 | Find-Us-Here | Done | New public profile `https://www.find-us-here.com/businesses/Life-for-Relief-and-Development-Southfield-Michigan-USA/34560214/` was verified logged out with the correct name, address, phone, description, canonical HTTPS backlink, and approved current square logo. Its served 300 by 300 image is `https://www.find-us-here.com/images/business_images/300/lifeusa3_main_photo.png?11` | **Yes** |
| DIR-036 | A-Z Business Finder | Done | Find-Us-Here automatically created a distinct new profile at `https://www.a-zbusinessfinder.com/business-directory/Life-for-Relief-and-Development-Southfield-Michigan-USA/34560214/`. Logged-out verification confirmed the canonical backlink and the 1800 by 1800 logo at `https://www.a-zbusinessfinder.com/images/business_images/main/Life-for-Relief-and-Development-Southfield-MI-USA-34560214.png`; decoded-pixel comparison against the canonical square returned AE `0` | **Yes** |
| DIR-037 | Fyple | New candidate, CAPTCHA blocked | Google returned no exact indexed LifeUSA record. Fyple offers a free company listing, but the owner route redirects to authentication and displays reCAPTCHA. No CAPTCHA was handled and no account was created | No |

## New-profile execution pool

This is a quality-controlled research pool, not a claim that every route is already eligible or free. Each row must pass duplicate search, logo support, website-link support, and terms review before submission.

| ID | Platform | Profile type | Current state | Gate before submission |
|---|---|---|---|---|
| NEW-001 | Idealist | Nonprofit and volunteer organization | New candidate, access blocked | Working mailbox authentication and email verification |
| NEW-002 | Apple Business Connect | Local business and brand profile | Existing | Exact Apple Maps record and claim ID found; correct the existing stale HTTP link rather than create a duplicate |
| NEW-003 | Bing Places | Local business profile | Existing, verified | Exact verified Bing Maps record found; resolve ownership and correct the stale HTTP link rather than duplicate it |
| NEW-004 | Yelp for Business | Local business profile | Existing | Established Southfield record found; resolve its owner route instead of creating a duplicate |
| NEW-005 | Foursquare | Location and entity profile | Existing | Exact Southfield nonprofit record found through Foursquare's current business-owner search |
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
| NEW-030 | Local.com or current successor | Local business directory profile | Ineligible current platform | Current site publishes review content rather than owner-managed local business profiles |
| NEW-031 | EZlocal | Local business directory profile | Access blocked | Cloudflare verification prevented duplicate and owner-field inspection |
| NEW-032 | CitySquares | Local business directory profile | Existing | Exact Southfield record found with a stale HTTP link and no visible approved logo |
| NEW-033 | ShowMeLocal | Local business directory profile | Access blocked | Public site rendered an empty document; owner and logo capabilities remain unverified |
| NEW-034 | Opendi | Local business directory profile | Submitted, public receipt unverified | Free submission flow completed, but no confirmation ID or public result was observable |
| NEW-035 | My Local Services | Local business directory profile | Conditional paid listing | Platform requires a `$2` listing payment and manual approval |
| NEW-036 | Callupcontact | Local business directory profile | Published, logo incomplete | New public profile and canonical backlink verified; approved logo still absent |
| NEW-037 | Find-Us-Here | Local business and community directory profile | Done | New logged-out public profile, approved logo, and canonical backlink verified |
| NEW-038 | A-Z Business Finder | Local business and community directory profile | Done | Distinct auto-created public profile, pixel-matched logo, and canonical backlink verified |
| NEW-039 | Fyple | Local business directory profile | New candidate, CAPTCHA blocked | No exact indexed record found; authentication requires reCAPTCHA before company creation |

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

Qualified progress is **2 of 20**. Find-Us-Here and A-Z Business Finder meet every Done criterion. Callupcontact is public but missing the approved logo, and Opendi has no verified public receipt. The supplied mailbox password was rejected by Google during authorized Idealist sign-in; it was tried once and was not retried. Points of Light requires an emailed magic link. Cylex, Alignable, and Fyple stop at reCAPTCHA; no CAPTCHA interaction occurred. MerchantCircle returns 403, and EZlocal remains behind Cloudflare verification. Taproot requires a real representative name. Paid listings, memberships, fundraising enrollment, and external support requests remain separately gated. Duplicate research and no-login public verification can continue.
