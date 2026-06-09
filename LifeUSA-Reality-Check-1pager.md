# Lifeusa.org SEO Reality Check

**Prepared by:** Saiaf Gamal
**For:** Life for Relief and Development
**Date:** 2026-05-08
**Evidence captured:** 2026-05-07, ~22:30 UTC, via curl + Screaming Frog crawl + Ahrefs site structure export

---

## What is working / ما الذي يعمل بشكل جيد

- The main site has authority. 963 referring domains, 1,069 monthly organic visits, 33 ranking pages.
- The donations subdomain has its own backlink base. 214 referring domains and good security setup.
- The Arabic-English structure exists. Hreflang tags are there. They just need fixing, not building from scratch.

الموقع الرئيسي لديه سلطة جيدة وروابط خلفية قوية. الهيكل ثنائي اللغة موجود ويحتاج فقط إلى ضبط، وليس إعادة بناء.

> **Evidence: Ahrefs site structure (May 2026, file: `site structure.png`)**
>
> | Subdomain | Ref domains | Organic traffic | Organic pages |
> |---|---|---|---|
> | www.lifeusa.org | 963 | 1,069 | 33 |
> | donate.lifeusa.org | 214 | 4 | 1 |
> | arabic.lifeusa.org | 1 | 0 | 0 |
> | donation.lifeusa.org | 4 | 0 | 0 |
> | staff.lifeusa.org | 10 | 0 | 0 |
> | lifeusa.org (apex) | 805 | 0 | 0 |

> **Evidence: hreflang exists in homepage HTML**
> ```html
> <link rel="alternate" href="https://www.lifeusa.org/" hreflang="x-default"/>
> <link rel="alternate" href="https://www.lifeusa.org/ar" hreflang="ar-jo"/>
> <link rel="alternate" href="https://www.lifeusa.org/" hreflang="en-us"/>
> ```

---

## ما هي المشاكل الأهم

### 1. Your subdomains are fragmenting you / تفكك النطاقات الفرعية يضعفك

You have five subdomains running in parallel. arabic.lifeusa.org is dead in DNS. donation.lifeusa.org is a second donations platform that duplicates donate.lifeusa.org. staff.lifeusa.org is a public WordPress site that should not be publicly visible. Each one splits your visitor data, your SEO equity, and your donor experience.

أنت تشغل خمسة نطاقات فرعية بالتوازي. أحدها ميت تماما، وثانٍ يكرر الأول، وثالث يكشف محتوى داخلي للجمهور. كل نطاق يفتت بياناتك وقوتك في محركات البحث.

**In plain terms / بالعربية**

- **The problem:** Five subdomains run on different platforms, one is fully dead in DNS, two duplicate each other, and one exposes internal staff content publicly.
- **How we found out:** A direct DNS + HTTP probe showed arabic. does not resolve, donate. and donation. run on two different donation platforms (donorportal vs. Givecloud), and staff. is a public WordPress install. Ahrefs confirmed backlinks and traffic are fragmented across all of them.
- **Why it hurts SEO:** Google treats each subdomain as its own site, so authority earned in one place does not lift the others. Backlinks pointing to a dead subdomain are wasted. Two donation platforms split donor data so you cannot see the full conversion picture. A public staff site competes with the main domain for brand keywords and burns crawl budget.

- **المشكلة:** خمسة نطاقات فرعية تعمل على منصات مختلفة، واحد منها ميت تماما، اثنان يكرران بعضهما، وواحد يكشف محتوى داخلي للموظفين أمام الجمهور.
- **كيف اكتشفناها:** فحص مباشر لـ DNS وترويسات HTTP أظهر أن arabic. لا يستجيب، وأن donate. و donation. يعملان على منصتي تبرع مختلفتين (donorportal مقابل Givecloud)، وأن staff. موقع ووردبريس مكشوف للعامة. أداة Ahrefs أكدت أن الروابط الخلفية والزيارات مشتتة بينهم.
- **لماذا تضر بترتيبك في البحث:** جوجل يعامل كل نطاق فرعي كموقع منفصل، فالسلطة المكتسبة في واحد لا ترفع الآخرين. الروابط التي تشير لنطاق ميت تذهب هدرا. منصتا تبرع تقسمان بيانات المتبرعين فلا ترين الصورة الكاملة. وموقع الموظفين العام ينافس موقعك الرئيسي على الكلمات المفتاحية للعلامة ويستهلك ميزانية الزحف.

> **Evidence: subdomain probe (curl, 2026-05-07)**
>
> arabic.lifeusa.org does not resolve:
> ```
> $ curl -sIv https://arabic.lifeusa.org/
> * Could not resolve host: arabic.lifeusa.org
> $ dig +short arabic.lifeusa.org
> (empty)
> ```
>
> donation.lifeusa.org runs Givecloud (different platform from donate.):
> ```
> $ curl -sI https://donation.lifeusa.org/
> HTTP/2 200
> x-givecloud-app: 30e6db6e4f1287f56931e5f5ae6a5cf6648e5bee
> x-givecloud-domain: life
> x-site-id: 426
> server: cloudflare
> ```
>
> staff.lifeusa.org is a public WordPress install:
> ```
> $ curl -sI https://staff.lifeusa.org/
> HTTP/2 200
> server: cloudflare
> link: <https://staff.lifeusa.org/wp-json/>; rel="https://api.w.org/"
> ```

### 2. Wix is sending wrong language signals to Google / Wix يرسل إشارات لغة خاطئة لجوجل

We tested five different pages. Each returned a different (and wrong) language code in the HTTP header. The homepage tells Google it is Chinese. Your About page says Turkish. Your Gaza page says French. Your Arabic page says English.

This is the strongest single explanation for why your Arabic articles do not surface when someone searches in English. Google is confused about which language each page is actually in.

This is a Wix bug. We need to escalate it to Wix support together.

اختبرنا خمس صفحات. كل واحدة منها أرسلت رمز لغة خاطئ مختلف لجوجل. الصفحة الرئيسية تقول إنها بالصينية. صفحتك "من نحن" تقول التركية. صفحة غزة تقول الفرنسية.

هذا هو التفسير الأقوى لمشكلتك الأصلية: لماذا لا تظهر مقالاتك العربية عند البحث بالإنجليزية. جوجل لا يعرف لغة كل صفحة.

هذه مشكلة في منصة Wix نفسها. نحتاج لرفعها لدعم Wix معا.

**In plain terms / بالعربية**

- **The problem:** The HTTP language header Wix returns is wrong on every sampled page, and the wrongness is cached.
- **How we found out:** Five identical curls against five different URLs returned five different incorrect language codes (Chinese for the homepage, Turkish for /about, French for /gaza). Repeating the homepage three times kept returning Chinese, which proves the bad value lives in the cache, not in random requests.
- **Why it hurts SEO:** The HTTP header is Google's first language signal and overrides the in-page tag. Pages tagged as Chinese, Turkish, or French cannot rank in English search. This is the most likely single explanation for why Arabic content does not appear when donors search for the brand in English.

- **المشكلة:** ترويسة اللغة التي يرسلها Wix خاطئة على كل صفحة فحصناها، والخطأ مخزن في الذاكرة المؤقتة وليس عشوائيا.
- **كيف اكتشفناها:** خمسة طلبات curl متطابقة على خمس صفحات مختلفة أعادت خمسة رموز لغة خاطئة مختلفة (الصينية للصفحة الرئيسية، التركية لـ /about، الفرنسية لـ /gaza). تكرار طلب الصفحة الرئيسية ثلاث مرات أعاد الصينية في كل مرة، وهذا دليل أن القيمة الخاطئة محفوظة في التخزين المؤقت.
- **لماذا تضر بترتيبك في البحث:** ترويسة HTTP هي الإشارة الأولى التي يقرأها جوجل عن لغة الصفحة وتتجاوز وسم HTML في القرارات الأولية. الصفحات المصنفة كصينية أو تركية أو فرنسية لا يمكن أن تظهر في نتائج البحث بالإنجليزية. هذا هو التفسير الأقوى لمشكلتك الأصلية: لماذا لا يظهر محتواك العربي عند البحث عن المؤسسة بالإنجليزية.

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
> The HTML lang tag on the homepage is correct (for comparison):
> ```html
> <html lang="en">
> ```
>
> The HTTP header takes precedence in many of Google's signals and is what survives the cache layer.

### 3. Your images are invisible to search / صورك غير مرئية لمحركات البحث

451 of your images have no alt text. 20 have no alt attribute at all. When you publish an Arabic article with images, search engines have no way to read what the image is. So they never surface in any language.

This is the second half of your original pain point. The first half was the language signals; this is why the images themselves do not appear.

451 من صورك بدون نص بديل (alt text). 20 صورة بدون خاصية alt تماما. عندما تنشرين مقالة عربية بالصور، محركات البحث لا تستطيع قراءة محتوى الصورة. لذلك لا تظهر بأي لغة.

**In plain terms / بالعربية**

- **The problem:** 451 images on your site have no alt text and 20 more have no alt attribute at all.
- **How we found out:** A full Screaming Frog crawl of the site flagged both issues with exact URL lists for every affected image and the pages those images live on.
- **Why it hurts SEO:** Search engines read alt text to understand what an image shows. With no alt, your images cannot be indexed for image search in any language, donors using screen readers cannot consume the content, and Google loses one of its strongest signals about what each page is about. This is the second half of your original concern about images not appearing in search.

- **المشكلة:** 451 صورة على موقعك بدون نص بديل (alt text)، و20 صورة إضافية بدون خاصية alt تماما.
- **كيف اكتشفناها:** فحص شامل بأداة Screaming Frog لكامل الموقع رصد المشكلتين وأخرج قائمة دقيقة بكل صورة متأثرة والصفحات التي تظهر عليها.
- **لماذا تضر بترتيبك في البحث:** محركات البحث تقرأ النص البديل لتفهم ما تحتويه الصورة. بدون alt، صورك لا يمكن فهرستها في بحث الصور بأي لغة، والمتبرعون الذين يستخدمون قارئات الشاشة لا يمكنهم الوصول للمحتوى، وجوجل يفقد واحدة من أقوى إشاراته لفهم موضوع الصفحة. هذا هو النصف الثاني من مخاوفك الأصلية حول عدم ظهور الصور في البحث.

> **Evidence: Screaming Frog issues overview (file: `screaming frog issues/issues_overview_report.csv`)**
> ```
> "Images: Missing Alt Text","Issue","Low","451","39.420"
> "Images: Missing Alt Attribute","Issue","Low","20","1.750"
> ```
> Affected URL exports:
> - `screaming frog issues/images_missing_alt_text.csv` (451 images)
> - `screaming frog issues/images_missing_alt_attribute.csv` (20 images)
> - `screaming frog issues/images_images_missing_alt_text_inlinks.csv` (which pages they appear on)

### 4. Your page experience is degraded / تجربة الصفحات متراجعة

90% of images on your site (1,035 images) have no width or height defined. This causes the page layout to jump as it loads, which Google flags as bad user experience and which makes donors lose trust. 47% of images are over 100KB, slowing the page.

90% من صورك بدون أبعاد محددة (1,035 صورة). هذا يسبب اهتزاز الصفحة أثناء التحميل، مما يضعف ثقة المتبرع وترتيبك في جوجل.

**In plain terms / بالعربية**

- **The problem:** 1,035 images (90%) have no width or height defined, and 543 images (47%) are over 100KB in file size.
- **How we found out:** Screaming Frog flagged both as Core Web Vitals opportunities and exported the affected URLs and the pages they appear on.
- **Why it hurts SEO:** Without dimensions, the page layout jumps as images load, which is measured as Cumulative Layout Shift, a Core Web Vitals ranking signal. Heavy images slow down Largest Contentful Paint, another ranking signal. Both pull down rankings on every page of the domain and make donors on slow mobile connections leave before the donate button appears.

- **المشكلة:** 1,035 صورة (90%) بدون أبعاد محددة، و543 صورة (47%) أكبر من 100 كيلوبايت في الحجم.
- **كيف اكتشفناها:** أداة Screaming Frog رصدت كلا المشكلتين كفرص لتحسين Core Web Vitals وأخرجت قوائم بالعناوين المتأثرة والصفحات التي تظهر عليها.
- **لماذا تضر بترتيبك في البحث:** بدون أبعاد، تخطيط الصفحة يهتز أثناء التحميل وهذا ما يقاس بـ Cumulative Layout Shift، أحد إشارات Core Web Vitals لترتيب جوجل. والصور الثقيلة تبطئ Largest Contentful Paint، وهو إشارة ترتيب أخرى. كلاهما يخفض الترتيب لكل صفحات الموقع ويجعل المتبرعين على الإنترنت البطيء يغادرون قبل ظهور زر التبرع.

> **Evidence: Screaming Frog issues overview**
> ```
> "Images: Missing Size Attributes","Opportunity","Low","1035","90.470"
> "Images: Over 100 KB","Opportunity","Medium","543","47.470"
> ```
> Affected URL exports:
> - `screaming frog issues/images_missing_size_attributes.csv`
> - `screaming frog issues/images_over_100_kb.csv`
> - `screaming frog issues/images_images_over_x_kb_inlinks.csv` (which pages they appear on)
>
> Reference (Google official): https://web.dev/articles/optimize-cls and https://web.dev/articles/optimize-lcp

### 5. Your schema markup is generic, not nonprofit / البيانات المنظمة عامة وليست خيرية

You are marked up as a "ProfessionalService" in Google's eyes, which implies a for-profit business. The correct schema for a registered nonprofit is "NGO". Your 441 blog posts also have no Article schema, which is the largest single fix.

موقعك مصنف كـ "ProfessionalService" أمام جوجل، وهذا يعني نشاط ربحي. التصنيف الصحيح للمؤسسة الخيرية هو "NGO". مقالاتك الـ 441 بدون تصنيف Article schema، وهذا أكبر إصلاح فردي.

**In plain terms / بالعربية**

- **The problem:** The homepage tells Google you are a `ProfessionalService` (a for-profit business type), and your 441 blog posts have no `Article` schema at all.
- **How we found out:** Direct extraction of the JSON-LD code from your homepage HTML showed the wrong organization type. A count of your blog sitemap returned 441 posts, and spot-checks on individual posts confirmed none of them carry `Article` markup.
- **Why it hurts SEO:** The wrong organization type blocks nonprofit-specific Google features like the donations panel, charity disambiguation, and trust badges. Missing `Article` schema on 441 posts blocks the largest single rich-result opportunity on the site (publish date, author, headline image in search results). You are leaving your biggest schema win unclaimed.

- **المشكلة:** الصفحة الرئيسية تخبر جوجل أنك "ProfessionalService" (تصنيف لنشاط ربحي)، ومقالاتك الـ 441 بدون أي تصنيف Article schema.
- **كيف اكتشفناها:** استخراج مباشر لكود JSON-LD من HTML الصفحة الرئيسية أظهر التصنيف الخاطئ. عدّ سايت ماب المدونة أعاد 441 مقالة، والفحص العشوائي لمقالات منفردة أكد أن لا واحدة منها تحمل تصنيف Article.
- **لماذا تضر بترتيبك في البحث:** التصنيف الخاطئ للمؤسسة يحجب ميزات جوجل الخاصة بالجمعيات الخيرية مثل لوحة التبرعات وعلامات الثقة وتمييز المؤسسات الخيرية. وغياب Article schema على 441 مقالة يحجب أكبر فرصة منفردة للنتائج المنسقة في الموقع (تاريخ النشر، الكاتب، صورة العنوان في نتائج البحث). أنت تترك أكبر مكسب schema بدون استغلال.

> **Evidence: homepage JSON-LD (extracted with curl)**
> ```json
> {
>   "@context": "http://www.schema.org",
>   "@type": "ProfessionalService",
>   "name": "Life for Relief and Development",
>   "url": "https://www.lifeusa.org/",
>   "description": "Founded in 1992, LIFE for Relief and Development is a global humanitarian relief and development organization...",
>   "address": {
>     "@type": "PostalAddress",
>     "addressLocality": "Southfield",
>     "addressRegion": "Michigan",
>     "postalCode": "48075",
>     "addressCountry": "United States"
>   }
> }
> ```
> `ProfessionalService` is a Schema.org subclass of `LocalBusiness` (for-profit context). The semantically correct type for a registered nonprofit is `NGO` (subclass of Organization). Reference: https://schema.org/NGO and https://schema.org/ProfessionalService
>
> Blog post count from Wix sitemap:
> ```
> $ curl -s https://www.lifeusa.org/blog-posts-sitemap.xml | grep -c "<loc>"
> 441
> ```
> Spot-check on a top-traffic blog post (`/post/what-causes-earthquakes-and-how-they-affect-people`) returned no `Article` JSON-LD block.

---

## What to do first / الأولويات

1. **Sunset the dead subdomains** (arabic., donation.) and lock down staff. so it is not public. Pick one donations platform.
2. **Open a Wix support ticket** for the language header bug. We will draft it together with the curl evidence.
3. **Fix the hreflang locale** from ar-jo to ar, in Wix Multilingual settings.
4. **Image program**: alt text on the top 50 traffic pages, then site-wide. Add image dimensions.
5. **Schema upgrade**: switch homepage to NGO, add Article schema on blog posts.

---

## How this maps to your original concerns / كيف يربط هذا بمخاوفك الأصلية

You said: "When I search Life for Relief and Development in English, my Arabic articles do not appear, and the images do not appear."

This audit shows three reasons stacked on top of each other:

1. Google cannot tell what language your pages are in (Wix HTTP header bug, Section 2 evidence above).
2. Your hreflang tells Google your Arabic content is specifically Jordanian Arabic, narrowing your match surface (Section "What is working" hreflang block above).
3. Your images have no descriptive text, so they cannot be indexed for image search in any language (Section 3 evidence above).

Fixing these three (1 platform escalation, 1 settings change, 1 content workflow change) is the leverage point.

قلتي: "عندما أبحث عن Life for Relief and Development بالإنجليزية، مقالاتي العربية لا تظهر، والصور لا تظهر."

هذا التدقيق يظهر ثلاثة أسباب متراكمة: جوجل لا يعرف لغة صفحاتك، وعلامة hreflang تخبره أن المحتوى عربي أردني فقط، وصورك بدون نص وصفي. إصلاح الثلاثة معا هو نقطة التحول.

---

## What we need from you / ما نحتاجه منك

- Google Search Console access (sgamal2593@gmail.com, Owner or Full user) for www.lifeusa.org and any other verified subdomains.
- GA4 access (Viewer level).
- Wix admin access or a 30-minute screen-share.
- Decisions on the subdomain consolidation (we will discuss in the kickoff call).
- Confirmation of EIN/501(c)(3) registration details for NGO schema markup.

دخول Google Search Console، دخول GA4، صلاحيات Wix أو جلسة مشاركة شاشة، قرارات بشأن دمج النطاقات، وتفاصيل تسجيل المؤسسة لإضافة بيانات NGO schema.

---

*Reference document: LifeUSA Technical SEO [Master Sheet].xlsx contains the full audit findings with priority and Screaming Frog evidence per row. The kickoff agenda (LifeUSA-Kickoff-Agenda.md) contains a full evidence index in its appendix.*
