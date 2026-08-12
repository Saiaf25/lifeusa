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
| DIR-004 | Idealist | CAPTCHA blocked | Exact organization-plus-Southfield search returned zero results. On July 24, the email signup route accepted the approved mailbox and then required reCAPTCHA. The CAPTCHA has not been completed | No |
| DIR-005 | VolunteerMatch | Existing platform merged | VolunteerMatch now routes organization onboarding through Idealist and is not a second independent directory | No |
| DIR-006 | Yelp for Business | Existing | Google returned the established public record at `https://www.yelp.com/biz/life-for-relief-and-development-southfield`; Yelp's device-verification screen prevented a deeper logged-out field audit | No |
| DIR-007 | Manta | Existing data record | Manta-indexed category results already reference “Life For Relief And Development Inc.” in Southfield, so a new listing would risk duplication; the direct record still needs owner-route resolution | No |
| DIR-008 | ChamberofCommerce.com | Superseded by DIR-018 | The initial platform search was unreliable; later evidence from Cybo exposed the exact existing Southfield ChamberofCommerce.com record documented in DIR-018 | No |
| DIR-009 | Hotfrog US | New candidate, broken registration | Google returned no exact record. Hotfrog confirms that verified profiles can add images and a logo. On July 24, the public Add Business page loaded, but its “Sign up here” link opened a Page Not Found screen and the direct administrator route returned 403 | No |
| DIR-010 | Brownbook | Human verification required | Google returned no exact record. On July 24, the public site stopped at a Cloudflare “Verify you are human” screen before owner registration or branding fields could be reached | No |
| DIR-011 | Cylex US | Human verification required | Google returned no exact record. On July 24, the public site stopped at a Cloudflare “Verify you are human” screen before the registration route could be reached | No |
| DIR-012 | MerchantCircle | New candidate, signup blocked | Google returned no exact record. MerchantCircle confirms a free basic listing with editable business information and photos. On July 24, the official `/signup` route again returned 403 | No |
| DIR-013 | Cybo | Existing | Cybo's add-business duplicate step found the exact Southfield record at `https://www.cybo.com/US-biz/life-for-relief-development`; the public page links to LifeUSA but exposes stale contact data and no approved logo | No |
| DIR-014 | Nextdoor Business | Done | On July 24, the account email was verified and authenticated dashboard access was confirmed. The page at `https://nextdoor.com/pages/life-for-relief-and-development-southfield-mi/` shows the correct legal name, address, phone, public email, description, canonical HTTPS backlink, and approved square LifeUSA logo. The logo was uploaded, cropped, saved, and verified visually. The user then explicitly confirmed that the same logo appears without signing in. Evidence screenshot: `../2026-07-24/nextdoor-approved-logo-and-backlink.jpg` | **Yes** |
| DIR-015 | Alignable | CAPTCHA blocked | Google returned no exact profile. On July 24, the free signup accepted the approved mailbox and terms selection, then required reCAPTCHA. The CAPTCHA has not been completed | No |
| DIR-016 | AARP Create the Good | Personal details and CAPTCHA required | Google returned no exact organization result. AARP offers free nonprofit opportunity publication, but its account form requires a real first name, last name, birthday, postal code, and moving-character security challenge. No personal data was invented or submitted | No |
| DIR-017 | Taproot Plus | Organization approved, logo saved | Google returned no exact organization result. On July 24, the authorized account email was verified, nonprofit onboarding was completed with the legal name, EIN `95-4402149`, canonical website, mission, location, and issue areas, and Taproot displayed “Congratulations! You're officially a Taproot nonprofit!” The dashboard marks Life for Relief and Development as `Approved`. The approved square logo was uploaded, cropped, saved, and visually verified beside the canonical website in the organization profile. A logged-out public organization URL has not been exposed, so the profile does not count yet | No |
| DIR-018 | ChamberofCommerce.com | Existing reference found | Cybo's exact Southfield record links to `chamberofcommerce.com/southfield-mi/4559853-life-for-relief-development`; resolve and claim that record instead of creating a duplicate | No |
| DIR-019 | MapQuest | Existing reference found | Cybo's exact Southfield record links to `mapquest.com/us/michigan/life-for-relief-development-6299633`; resolve the current owner/data-provider route instead of creating a duplicate | No |
| DIR-020 | Points of Light Engage | Platform lookup blocked | Google returned no exact indexed organization result. On July 24, the authorized account was completed under Saif Gamal after the user explicitly approved the Terms and age confirmation. The organization search found the exact “Life For Relief & Development” Southfield record. After selection, Points of Light returned “GMB Organization not Found” for Google place ID `ChIJ1wktmlHIJIgRRpRApYo7F9U` and directed the account to Google Business Profile or Points of Light support. No organization profile was created | No |
| DIR-021 | Bonterra Deed | Existing data record | Deed's nonprofit registration search returned the exact legal name, EIN `95-4402149`, and Southfield address. The free claim flow says claimed profiles can add a mission, logo, and verified team members, so this record must be claimed or maintained rather than counted as new | No |
| DIR-022 | Pledge | Conditional fundraising platform | Google returned no exact indexed LifeUSA page. Pledge offers free fundraising pages and maintains a charity database, but the verified route is a fundraising product rather than a routine public directory profile; any campaign or service enrollment remains separately gated | No |
| DIR-023 | Double the Donation | Existing | Google returned the exact public record at `https://doublethedonation.com/lifeusa`, including EIN `95-4402149`, the Southfield address, and a LifeUSA website link. It cannot count as new and no approved logo was visible in the logged-out page state | No |
| DIR-024 | PayPal Giving Fund | Existing | PayPal's logged-out charity search returned the exact LifeUSA record at `https://www.paypal.com/us/fundraiser/charity/2268883`. The profile exposes EIN `95-4402149` and an HTTP LifeUSA website link but no approved visible logo; enrollment also requires a charity PayPal Business account and Giving Fund terms | No |
| DIR-025 | Apple Maps | Existing | Apple Maps returned the exact Southfield charity record with the correct address, phone, and a stale HTTP website link. Its claim route resolves to Apple Business Connect claim ID `6959862997556437473`; maintain that record rather than duplicate it | No |
| DIR-026 | Bing Maps | Existing, verified business | Bing Maps returned the exact verified Southfield record under YP ID `YN1AFB07F61C79BF68`. It links through the stale HTTP LifeUSA URL and exposes Facebook-sourced photos, so it is an existing-profile correction route | No |
| DIR-027 | Foursquare | Existing | Foursquare's owner search returned the exact “Life For Relief & Development” nonprofit record at the Southfield address. The active owner route is `https://business.foursquare.com/`; do not create a duplicate | No |
| DIR-028 | EZlocal | Human verification required | Google returned no exact indexed record. On July 24, the public site again stopped at Cloudflare security verification. Duplicate status, free owner route, and logo support remain unverified | No |
| DIR-029 | CitySquares | Existing | CitySquares' own exact search returned `https://citysquares.com/b/life-for-relief-development-10255230` with the correct address, phone, and an HTTP LifeUSA link but no visible approved logo | No |
| DIR-030 | ShowMeLocal | Site unavailable in browser | Google returned no exact indexed record. On July 24, the public site still rendered a blank page in the browser. Duplicate status, owner route, and logo support remain unverified | No |
| DIR-031 | Opendi | Verification reported, publication pending | On July 24, the authorized free listing flow accepted the legal name, description, Saif Gamal as contact, address, phone, public email, website, no published hours, and Social Services category. The user later reported completing the emailed verification. A fresh exact-name and Southfield search still returned “No results,” so publication, logo support, and the final public page remain unverified | No |
| DIR-032 | My Local Services | Conditional paid listing | The platform advertises a full-page listing for `$2` and says listings are manually approved. Any payment or paid listing remains separately gated | No |
| DIR-033 | Local.com | Ineligible current platform | The current site is an expert-review and top-ten content publisher, not an active owner-managed local business directory submission route | No |
| DIR-034 | Callupcontact | Published, logo incomplete; site temporarily unavailable | A new public profile was previously verified at `https://www.callupcontact.com/b/businessprofile/Life_for_Relief_and_Development/10168407` with the correct organization data and canonical backlink but no approved logo. On July 24, the page returned Cloudflare Tunnel Error 1033, so the logo could not be added or reverified | No |
| DIR-035 | Find-Us-Here | Done | New public profile `https://www.find-us-here.com/businesses/Life-for-Relief-and-Development-Southfield-Michigan-USA/34560214/` was verified logged out with the correct name, address, phone, description, canonical HTTPS backlink, and approved current square logo. Its served 300 by 300 image is `https://www.find-us-here.com/images/business_images/300/lifeusa3_main_photo.png?11` | **Yes** |
| DIR-036 | A-Z Business Finder | Done | Find-Us-Here automatically created a distinct new profile at `https://www.a-zbusinessfinder.com/business-directory/Life-for-Relief-and-Development-Southfield-Michigan-USA/34560214/`. Logged-out verification confirmed the canonical backlink and the 1800 by 1800 logo at `https://www.a-zbusinessfinder.com/images/business_images/main/Life-for-Relief-and-Development-Southfield-MI-USA-34560214.png`; decoded-pixel comparison against the canonical square returned AE `0` | **Yes** |
| DIR-037 | Fyple | Registration under maintenance | Google returned no exact indexed LifeUSA record. Fyple offers a free company listing. On July 24, its registration page displayed “We’ll be back soon” and said the website was being updated, so no account could be created | No |
| DIR-038 | LaCartes | Account form staged, CAPTCHA and Terms pending | No indexed exact LifeUSA result was found. The official free registration form is active and the approved account details were entered on July 24. The platform requires an image CAPTCHA and acceptance of its Terms before account creation. Business-profile logo and backlink fields remain unverified | No |
| DIR-039 | 2FindLocal | Account created, listing staged at mandatory payment | The user completed the account image verification, and the authorized account is active. The official phone lookup returned “Sorry, we could not find any information” for `800-827-3543`, confirming the new-listing route. On July 24, the business form was completed with the legal name, Southfield address, phone, description, and three matching categories. 2FindLocal then required a `$2.50` Stripe payment before submission. Its optional website field was not used because it requires a permanent 2FindLocal badge and an unrelated Promo Codes link on the LifeUSA homepage. Reserved URL `https://www.2findlocal.com/b/15323742` currently shows an empty unclaimed stub. No payment was made, no listing was submitted for moderation, and logo upload support remains unverified | No |
| DIR-040 | iBegin | Cloudflare verification blocked | No indexed exact LifeUSA result was found. The official submission route `https://www.ibegin.com/business-center/submit/` was opened on July 24 but remained on Cloudflare's “Performing security verification” screen, so the form and logo field could not be reached | No |
| DIR-041 | BizHwy | Activated, Brand Resources backlink saved | On July 24, the free listing was submitted with the legal name, Southfield address, phone, and approved mailbox. Both preselected paid upgrades, totaling `$25`, were removed. The exact activation email from `info@bizhwy.com` was opened and the platform confirmed “Business Listing Activated.” Authenticated profile review found no logo or image control. The listing's only website field was therefore updated and verified as `https://www.lifeusa.org/brand-resources`, giving the directory a direct backlink to the approved-logo page. The listing still cannot count toward the 20-logo goal because BizHwy does not display the logo | No |
| DIR-042 | ProvenExpert | Done | The user created the profile on August 12. Logged-out verification confirmed the live public page at `https://www.provenexpert.com/lifeusa/`, the approved LifeUSA square logo, accurate organization identity and Southfield contact details, and a direct canonical HTTPS backlink to `https://www.lifeusa.org/`. ProvenExpert serves the visible 344 by 344 profile image from `https://images.provenexpert.com/35/ed/bf328e88a116cd95a8a11f77ffaf/lifeusa_full_1786508458.jpg`. Evidence: `../2026-08-12/provenexpert-profile-verification.md` | **Yes** |

## Important existing-profile access register

These profiles are not neglected and must not be duplicated. They are valuable existing LifeUSA entity records where an authorized administrator may be able to add or standardize the approved logo, correct the website to `https://www.lifeusa.org/`, and repair other stale fields. They do **not** count toward the 20-new-profile goal. No access request has been sent.

| Priority | Platform and public record | Verified public issue | Access or decision needed | Logo-edit confidence |
|---:|---|---|---|---|
| 1 | Every.org: `https://www.every.org/lifeusa` | Reverified July 19. The exact EIN profile is public, uses a generic “Humans” avatar, and links to `http://www.lifeusa.org` | Existing Every.org nonprofit administrator identified by the platform; Dr. Hani should identify or provide that administrator access | Owner dashboard required to verify the upload field |
| 2 | Bonterra Deed: exact EIN `95-4402149` record in the nonprofit claim flow | The legal name and Southfield address match LifeUSA | Authorized organizational representative must claim or access the existing record | **Verified:** Deed says claimed profiles can add a mission, logo, and team members |
| 3 | Benevity Causes: `https://causes.benevity.org/causes/840-954402149` | Existing profile has stale mission copy and an HTTP website link | Existing masked `lifeusa.org` owner account; identify the current internal administrator | Owner dashboard required to verify the logo field |
| 4 | PayPal Giving Fund: `https://www.paypal.com/us/fundraiser/charity/2268883` | Exact EIN record has an HTTP website link and no approved visible logo | Authorized charity PayPal Business account plus acceptance of Giving Fund terms | Conditional; confirm branding controls after authorized enrollment |
| 5 | Apple Maps / Apple Business Connect claim `6959862997556437473` | Exact Southfield record has the correct address and phone but an HTTP website link | Existing Apple Business Connect owner or authorized claim | Confirm logo and photo controls after owner access |
| 6 | Bing Maps / Bing Places record `YN1AFB07F61C79BF68` | Exact verified business links to HTTP and exposes Facebook-sourced photos | Existing Bing Places owner access | Confirm logo control and source-photo management after access |
| 7 | Foursquare: exact Southfield “Life For Relief & Development” record | Existing nonprofit record found in the owner search | Authorized access through `https://business.foursquare.com/` | Confirm logo field after owner access |
| 8 | Yelp: `https://www.yelp.com/biz/life-for-relief-and-development-southfield` | Established LifeUSA record exists; device verification blocked the deeper field audit | Existing Yelp for Business owner or authorized claim | Confirm logo/photo controls after access |
| 9 | Cybo: `https://www.cybo.com/US-biz/life-for-relief-development` | Exact record links to LifeUSA but has stale contact data and no approved logo | Existing owner access or claim | Logo state is visibly incomplete; edit capability requires owner verification |
| 10 | CitySquares: `https://citysquares.com/b/life-for-relief-development-10255230` | Exact record has the correct address and phone, an HTTP website link, and no visible approved logo | Resolve the listing owner or claim route | Confirm logo field after access |
| 11 | ChamberofCommerce.com: `https://chamberofcommerce.com/southfield-mi/4559853-life-for-relief-development` | Exact existing Southfield record is referenced by the verified Cybo profile | Resolve and claim the existing listing | Confirm logo field after access; do not duplicate |
| 12 | Manta: existing “Life For Relief And Development Inc.” Southfield record | Indexed category evidence proves an existing record, but the direct owner route remains unresolved | Locate the exact public record and authorized owner route | Logo capability not yet verified |
| 13 | Double the Donation: `https://doublethedonation.com/lifeusa` | Exact legal name, EIN, address, and website are public; no approved logo was visible | Identify the organization-maintenance route and authorized administrator | Logo capability not yet verified |

### Message for Dr. Hani

LifeUSA already has important third-party profiles that should be maintained rather than recreated. The immediate access priorities are Every.org, Bonterra Deed, Benevity Causes, PayPal Giving Fund, Apple Business Connect, Bing Places, Foursquare, Yelp, Cybo, and CitySquares. Please identify the current organizational administrator for each platform or provide an authorized owner-level route. After access is available, the acceptance check is: approved current logo or acceptable current blue-globe variant, canonical HTTPS website, correct legal identity and contact fields, and logged-out public verification.

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
| NEW-013 | Nextdoor Business | Local organization profile | Done | Public page, approved square logo, canonical HTTPS backlink, and logged-out visibility are verified |
| NEW-014 | Alignable | Local business network profile | New candidate, CAPTCHA blocked | Free signup reached reCAPTCHA; no account was created and no contacts were imported |
| NEW-015 | Better Business Bureau | Charity or business profile | Conditional | BBB eligibility and any accreditation or review distinction; no paid accreditation without approval |
| NEW-016 | Dun & Bradstreet | Business identity profile | Conditional | Existing D-U-N-S record search; logo is a paid-tier feature under current published terms |
| NEW-017 | PayPal Giving Fund | Charity profile | Existing | Exact public profile `2268883` found; update its HTTP website link and logo only through the authorized charity PayPal Business account and Giving Fund terms |
| NEW-018 | GlobalGiving | Humanitarian fundraising profile | Conditional | Program eligibility, application documents, and fundraising agreement |
| NEW-019 | Pledge | Nonprofit giving profile | Conditional fundraising platform | No exact indexed LifeUSA page found, but the available route creates fundraising products rather than a routine directory profile; service enrollment remains separately gated |
| NEW-020 | Double the Donation | Matching-gift nonprofit profile | Existing | Exact public `/lifeusa` record found with the legal name, EIN, address, and LifeUSA website link; maintain rather than duplicate |
| NEW-021 | AARP Create the Good | Volunteer organization profile | New candidate, access blocked | Free nonprofit opportunity publishing is verified; AARP account and public branding fields remain gated |
| NEW-022 | Taproot Plus | Skilled-volunteer nonprofit profile | Organization approved, logo saved | Taproot marks the organization `Approved`, and the approved square logo and canonical website are saved. A logged-out public organization URL still needs to be identified and verified |
| NEW-023 | Catchafire | Skills-based volunteering profile | Conditional | Service agreement, eligibility, and any participation cost |
| NEW-024 | Points of Light Engage | Volunteer organization profile | Platform lookup blocked | The account is complete and the exact Southfield organization record was selected, but Points of Light rejected Google place ID `ChIJ1wktmlHIJIgRRpRApYo7F9U` as not found |
| NEW-025 | Deed | Workplace giving and volunteering profile | Existing data record | Exact legal name, EIN, and Southfield record found in the free claim search; claim and enhance the existing record rather than count it as new |
| NEW-026 | Michigan Nonprofit Association | State nonprofit directory | Conditional | Existing membership or separately approved membership value and cost |
| NEW-027 | Southfield Area Chamber of Commerce | Local member directory | Conditional | Existing membership or separately approved membership value and cost |
| NEW-028 | Great Lakes Business Network or verified local equivalent | Regional business profile | Research | Exact platform identity, authority, free profile, and genuine nonprofit fit |
| NEW-029 | MapQuest business listing provider | Maps and local profile | Existing reference found | Cybo exposes the existing Southfield MapQuest record; resolve the current data-provider route |
| NEW-030 | Local.com or current successor | Local business directory profile | Ineligible current platform | Current site publishes review content rather than owner-managed local business profiles |
| NEW-031 | EZlocal | Local business directory profile | Access blocked | Cloudflare verification prevented duplicate and owner-field inspection |
| NEW-032 | CitySquares | Local business directory profile | Existing | Exact Southfield record found with a stale HTTP link and no visible approved logo |
| NEW-033 | ShowMeLocal | Local business directory profile | Access blocked | Public site rendered an empty document; owner and logo capabilities remain unverified |
| NEW-034 | Opendi | Local business directory profile | Verification reported, publication pending | User reported completing the emailed verification, but Opendi's fresh exact-name and Southfield search still returns no public result |
| NEW-035 | My Local Services | Local business directory profile | Conditional paid listing | Platform requires a `$2` listing payment and manual approval |
| NEW-036 | Callupcontact | Local business directory profile | Published, logo incomplete | New public profile and canonical backlink verified; approved logo still absent |
| NEW-037 | Find-Us-Here | Local business and community directory profile | Done | New logged-out public profile, approved logo, and canonical backlink verified |
| NEW-038 | A-Z Business Finder | Local business and community directory profile | Done | Distinct auto-created public profile, pixel-matched logo, and canonical backlink verified |
| NEW-039 | Fyple | Local business directory profile | New candidate, CAPTCHA blocked | No exact indexed record found; authentication requires reCAPTCHA before company creation |
| NEW-040 | LaCartes | Business and organization profile | Account form staged | Approved account details are entered; image CAPTCHA and Terms acceptance are required before submission |
| NEW-041 | 2FindLocal | Local business directory profile | Payment decision required | Account registration and the complete listing form are finished. The mandatory `$2.50` Stripe payment is the next step. The reserved public URL is still an empty unclaimed stub, and logo upload support remains unverified |
| NEW-042 | iBegin | Local business directory profile | Access blocked | Cloudflare security verification prevents access to the submission form |
| NEW-043 | BizHwy | Local business directory profile | Activated, Brand Resources backlink saved | Free listing activated. The authenticated editor has no logo or image field, so its single website field now links directly to `https://www.lifeusa.org/brand-resources` |
| NEW-044 | ProvenExpert | Business reputation profile | Done | User-created profile verified logged out with the approved LifeUSA square logo and canonical HTTPS website backlink |

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

Qualified progress is **4 of 20**. Find-Us-Here, A-Z Business Finder, Nextdoor, and ProvenExpert meet every Done criterion.

The July 24 approved batch reached these human gates:

- Idealist and Alignable require reCAPTCHA completion.
- Cylex, Brownbook, and EZlocal require Cloudflare human verification.
- AARP Create the Good requires an account owner's name, birthday, postal code, and security challenge.
- Taproot account verification, nonprofit onboarding, and the approved logo upload are complete. A logged-out public organization URL has not been exposed.
- Points of Light account completion and exact-record selection are complete. Its Google Business Profile lookup rejects the exact place ID, so platform support or Google Business Profile correction is required.
- LaCartes is staged at its human-verification step. The 2FindLocal account and listing form are complete, but the platform requires a `$2.50` payment before submission.
- iBegin remains blocked by Cloudflare security verification.

These platform conditions also prevent completion:

- Callupcontact returned Cloudflare Tunnel Error 1033, so its missing logo could not be added.
- Opendi verification was reported as completed, but a fresh exact-name and Southfield search still returns no public result.
- Hotfrog's advertised registration link returned Page Not Found.
- MerchantCircle's official free-signup route returned 403.
- Fyple's registration page is under maintenance.
- ShowMeLocal rendered a blank page.

BizHwy was activated and verified as not logo-capable in its free editor. Its website field now links directly to the LifeUSA Brand Resources page, but it does not count toward the 20-logo goal because the logo is not displayed. LaCartes is staged at human verification. 2FindLocal is staged at its mandatory `$2.50` payment step. iBegin remains blocked by Cloudflare.
