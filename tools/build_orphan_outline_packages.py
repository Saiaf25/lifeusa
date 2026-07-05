#!/usr/bin/env python3
"""Build the approved LifeUSA orphan-cluster outline packages.

This generator keeps the four related brief/outline/handoff files consistent
without hand-editing twelve separate artifacts.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
DATE = "July 5, 2026"
KW_EXACT = "Content Framework/80-Keywords/orphan-cluster-2026-07-05/orphan-nonrepetitive-guides-exact.json"
KW_REWRITE = "Content Framework/80-Keywords/orphan-cluster-2026-07-05/orphan-old-rewrite-candidates-exact.json"
KW_EXPANDED = "Content Framework/80-Keywords/orphan-cluster-2026-07-05/orphan-conflict-geography-expanded.json"


@dataclass(frozen=True)
class Link:
    label: str
    url: str
    anchor: str
    note: str


@dataclass(frozen=True)
class Section:
    title: str
    why: str
    stage: str
    keywords: str
    write: str
    avoid: str
    links: tuple[Link, ...] = ()


@dataclass(frozen=True)
class Topic:
    slug: str
    title: str
    subtitle: str
    content_type: str
    live_url: str
    status_note: str
    primary_keywords: tuple[tuple[str, str, str, str], ...]
    secondary_keywords: tuple[tuple[str, str, str, str], ...]
    reader_problem: str
    cluster_boundary: str
    format_decision: str
    intro_guidance: str
    links: tuple[Link, ...]
    sections: tuple[Section, ...]
    faq: tuple[str, ...]
    meta_title: str
    meta_description: str
    review_note: str
    source_note: str


def is_new_guide(topic: Topic) -> bool:
    return topic.content_type.startswith("New informational guide")


def owner_meta(topic: Topic) -> str:
    return "Writer: Angela" if is_new_guide(topic) else "Owner: Saiaf"


def owner_card(topic: Topic) -> str:
    if is_new_guide(topic):
        return "Angela draft. Saiaf SEO planning/review."
    return "Saiaf rewrite/enrichment. Not Angela."


def owner_risk_note(topic: Topic) -> str:
    if is_new_guide(topic):
        return "this is an Angela draft assignment; Saiaf owns SEO planning and review."
    return "this is Saiaf rewrite/enrichment work, not an Angela draft assignment."


def brief_owner(topic: Topic) -> str:
    if is_new_guide(topic):
        return "Angela draft; Saiaf SEO planning/review"
    return "Saiaf rewrite/enrichment"


def outline_heading(topic: Topic) -> str:
    if is_new_guide(topic):
        return "Writer Outline For Angela"
    return "Rewrite Outline For Saiaf"


def section_write_label(topic: Topic) -> str:
    return "What Angela should write" if is_new_guide(topic) else "What Saiaf should write"


COMMON_LINKS = (
    Link("What Is an Orphan?", "https://www.lifeusa.org/post/what-is-an-orphan", "what an orphan is", "Definition and context article."),
    Link("How To Help Orphans", "https://saiaf25.github.io/lifeusa/article-plans-and-outlines/how-to-help-orphans/", "how to help orphans", "Planned pillar outline until the Wix URL is live."),
    Link("Sponsorship coverage guide", "https://saiaf25.github.io/lifeusa/article-plans-and-outlines/what-does-orphan-sponsorship-cover/", "what orphan sponsorship can cover", "Supporting sponsorship guide."),
    Link("Orphan donation CTA", "https://donate.lifeusa.org/donorportal/project-designations?Program=11WVy000001QlE5MAK", "support orphaned children through LifeUSA", "Established orphan sponsorship/donation CTA."),
)

TOPICS: tuple[Topic, ...] = (
    Topic(
        slug="gaza-orphans-war-care-safety-support",
        title="Gaza Orphans: How War Leaves Children Without Care, Safety, and Support",
        subtitle="Enrichment plan for the existing Gaza orphan article. Keep the existing page unless Saiaf later decides otherwise.",
        content_type="Existing article enrichment; Saiaf-owned rewrite",
        live_url="https://www.lifeusa.org/post/who-will-watch-over-the-orphans-of-gaza",
        status_note="Rewrite means enrich the existing article with search intent, structure, internal links, and depth. It does not mean deleting the page or forcing a new title.",
        primary_keywords=(("war orphans", "390", "Low", "Use for conflict-specific framing and H2 support."), ("gaza orphans", "170", "Low", "Use in intro, Gaza-specific sections, metadata, and FAQ.")),
        secondary_keywords=(("orphan relief", "40", "Medium", "Use in relief/support section."), ("orphan crisis", "10", "Low", "Use carefully in crisis context, not as keyword stuffing.")),
        reader_problem="The reader wants to understand what happens to children who lose parents or caregivers in war, especially in Gaza, and what kind of support is needed beyond a generic donation appeal.",
        cluster_boundary="This page is conflict-specific and Gaza-specific. It must not become the general orphan definition article, the broad how-to-help pillar, or the sponsorship mechanics guide.",
        format_decision="Informational crisis explainer with LifeUSA proof examples and a careful donor next step.",
        intro_guidance="Open with the human problem of war orphanhood: loss of parent or caregiver, family separation, hunger, displacement, interrupted school, and fear. Use `gaza orphans` naturally once and avoid political overreach.",
        links=(
            Link("Gaza orphan campaign", "https://www.lifeusa.org/gaza-orphan-campaign", "support orphans in Gaza", "Campaign CTA/support page."),
            Link("Gaza food packs", "https://www.lifeusa.org/post/life-food-packs-reached-1-200-orphans-during-one-of-the-longest-humanitarian-crises-on-record", "food support for orphaned children in Gaza", "Food proof point."),
            Link("Gaza mothers and orphans essentials", "https://www.lifeusa.org/post/life-supports-mothers-and-orphans-in-gaza-with-critical-baby-formula-and-other-essentials", "mothers and orphans in Gaza", "Caregiver and essentials proof point."),
            Link("Gaza winter relief", "https://www.lifeusa.org/post/strengthening-stability-for-orphaned-children-life-s-ongoing-support-in-gaza", "winter relief for orphaned children in Gaza", "Winter/basic-needs proof point."),
            Link("Gaza Eid support", "https://www.lifeusa.org/post/life-supporting-orphans-families-gaza", "Eid support for Gaza orphans", "Joy/emotional-care proof point."),
            *COMMON_LINKS,
        ),
        sections=(
            Section("What Makes War Orphans Different?", "Distinguish conflict orphanhood from general orphan definitions.", "I know children are orphaned in war, but what does that actually change?", "`war orphans` 390/mo, `gaza orphans` 170/mo.", "Explain caregiver loss, family separation, displacement, hunger, school disruption, and loss of routine.", "Do not turn this into a generic definition of orphanhood; link to the definition article instead."),
            Section("Why Gaza Orphans Face Layered Risks", "Make the page Gaza-specific and useful.", "I need the Gaza context, not a generic crisis paragraph.", "`gaza orphans` 170/mo.", "Discuss unsafe shelter, disrupted aid access, caregiver strain, food scarcity, winter exposure, and emotional distress. Keep claims cautious and source-backed.", "Do not make unsupported casualty/statistical claims unless Saiaf adds current sourced figures before publishing."),
            Section("What Support Can Help In A War Zone?", "Answer the practical support question without becoming a general how-to-help list.", "I want to understand what kind of aid matters.", "`orphan relief` 40/mo.", "Organize support into food, essentials, caregiver support, winter relief, education continuity when possible, and moments of dignity/joy.", "Do not repeat the full `How To Help Orphans` pillar."),
            Section("LifeUSA Gaza Examples To Use", "Give Saiaf concrete internal links and proof points.", "I want evidence that LifeUSA has relevant Gaza work.", "`gaza orphans` 170/mo.", "Use food packs, baby formula and essentials, winter relief, Eid support, and the Gaza orphan campaign.", "Do not list examples mechanically; tie each example to a need category."),
            Section("How Donors Can Respond", "Close with a relevant CTA.", "I understand the crisis and want a next step.", "`support orphans in Gaza` as anchor, not a measured keyword.", "Point to the Gaza orphan campaign and the established orphan support CTA. Keep it direct and relief-focused.", "Do not pivot into broad sponsorship mechanics."),
        ),
        faq=("What are war orphans?", "Why are Gaza orphans especially vulnerable?", "What do orphaned children in Gaza need most?", "How can donors support orphans in Gaza?", "How does emergency relief support orphaned children?"),
        meta_title="Gaza Orphans: How War Leaves Children Without Care and Safety",
        meta_description="Learn how war affects orphaned children in Gaza, what support can help, and how LifeUSA relief work supports food, essentials, winter needs, and dignity.",
        review_note="Before publishing, Saiaf should add any current Gaza facts only from verified sources and avoid unsourced casualty or policy claims.",
        source_note="Google Ads CLI source: war orphans 390/mo, gaza orphans 170/mo. Existing article to enrich: Who Will Watch Over the Orphans of Gaza?",
    ),
    Topic(
        slug="why-gifts-for-orphans-matter",
        title="Why Gifts for Orphans Matter: Joy, Dignity, and the Right to Childhood",
        subtitle="Enrichment plan for the existing gift-focused orphan article. Keep the existing page unless Saiaf later changes the URL/title.",
        content_type="Existing article enrichment; Saiaf-owned rewrite",
        live_url="https://www.lifeusa.org/post/why-one-gift-means-the-world-to-an-orphaned-child",
        status_note="Rewrite means add depth, keyword coverage, and internal links. It does not mean deleting the article or turning it into a generic gift list.",
        primary_keywords=(("gifts for orphans", "20", "Low", "Use in intro, one H2, metadata, and FAQ."),),
        secondary_keywords=(("eid gifts for orphans", "10", "Medium", "Use in Eid/seasonal joy section."),),
        reader_problem="The reader wants to know whether gifts, play, and Eid celebrations are meaningful or secondary compared with urgent needs.",
        cluster_boundary="This page owns emotional care, dignity, joy, play, Eid, and childhood memory. It must not become a food/school/health needs guide or a general how-to-help article.",
        format_decision="Short informational donor guide with emotional-care framing and LifeUSA proof examples.",
        intro_guidance="Start by acknowledging the obvious concern: orphaned children need food, safety, school, and care first. Then explain why joy and gifts still matter when they restore dignity, normalcy, and a sense of being remembered.",
        links=(
            Link("Existing gift article", "https://www.lifeusa.org/post/why-one-gift-means-the-world-to-an-orphaned-child", "one gift can matter to an orphaned child", "Existing article to enrich."),
            Link("Ghana orphan party", "https://www.lifeusa.org/post/a-day-of-laughter-and-hope-for-ghana-s-orphaned-children-at-the-life-global-orphan-party-2026", "a day of laughter and hope for orphaned children", "Joy proof point."),
            Link("Gaza Eid support", "https://www.lifeusa.org/post/life-supporting-orphans-families-gaza", "Eid joy for Gaza orphans", "Eid/Gaza proof point."),
            Link("Global day of joy", "https://www.lifeusa.org/post/life-gives-a-day-of-joy-for-7-660-orphans-across-20-countries", "a day of joy for orphans across 20 countries", "Scale proof point."),
            Link("Let them play", "https://www.lifeusa.org/post/let-them-play-life-gives-every-child-a-chance-to-be-a-child-at-the-global-orphan-eid-parties", "every child deserves a chance to be a child", "Evergreen emotional-care proof point."),
            *COMMON_LINKS,
        ),
        sections=(
            Section("Why Gifts Are Not Just Extras", "Define the article's distinct value.", "I wonder if gifts are less important than basic needs.", "`gifts for orphans` 20/mo.", "Explain that gifts do not replace food, school, or safety, but can restore dignity, normalcy, and belonging.", "Do not imply gifts are more important than survival needs."),
            Section("Joy As Part Of Childhood Stability", "Move beyond material donation.", "I need to understand the emotional reason.", "`gifts for orphans` 20/mo.", "Discuss play, celebration, being remembered, and the emotional weight of ordinary childhood moments.", "Do not claim therapy, trauma recovery, or clinical outcomes."),
            Section("Eid Gifts And Seasonal Care", "Use the measured Eid variant and LifeUSA proof.", "I am thinking about seasonal or religious giving.", "`eid gifts for orphans` 10/mo.", "Explain Eid and seasonal gifts as moments of community, dignity, and shared celebration.", "Do not overuse religious language or make zakat claims."),
            Section("What Makes A Gift Responsible?", "Prevent a shallow gift-list article.", "I want to help without causing harm.", "`gifts for orphans` 20/mo.", "Cover age-appropriate items, dignity, local procurement when possible, safety, privacy, and program coordination.", "Do not recommend direct unsolicited gifts to children or orphanages without program guidance."),
            Section("LifeUSA Gift And Joy Examples", "Ground the article in existing content.", "I want examples, not theory.", "`gifts for orphans` 20/mo.", "Use Ghana, Gaza, global orphan party, Dhaka/Bangladesh, and older Eid party examples selectively.", "Do not list every recap; choose the strongest 3 to 5."),
        ),
        faq=("Are gifts for orphans helpful?", "What gifts can be given to orphans?", "Why do Eid gifts matter for orphaned children?", "Are gifts more important than food or school support?", "How can I support gifts or joy programs responsibly?"),
        meta_title="Why Gifts for Orphans Matter: Joy, Dignity, and Childhood",
        meta_description="Learn why gifts for orphans can support dignity, joy, belonging, and childhood memories alongside food, school, safety, and long-term care.",
        review_note="Keep this as emotional-care enrichment. Do not turn it into a generic gift guide or a replacement for urgent support pages.",
        source_note="Google Ads CLI source: gifts for orphans 20/mo; eid gifts for orphans 10/mo. Existing article to enrich: Why One Gift Means the World to an Orphaned Child.",
    ),
    Topic(
        slug="orphan-education-after-loss",
        title="Orphan Education After Loss: Why School Stability Matters",
        subtitle="New informational guide. It can use existing back-to-school posts as proof, but it does not need to replace them.",
        content_type="New informational guide; Angela-owned draft",
        live_url="https://www.lifeusa.org/post/orphan-education-after-loss",
        status_note="This can be a new guide because it owns school continuity only. Angela drafts it; Saiaf reviews SEO structure, keyword usage, links, and claim safety.",
        primary_keywords=(("orphan education", "10", "Low", "Use in title, intro, one H2, and metadata."),),
        secondary_keywords=(("support orphans education", "10", "Not provided", "Use corrected phrasing as `support orphan education` or `support education for orphans`."), ("sponsoring the education of an orphan", "10", "Low", "Use in sponsorship/education section.")),
        reader_problem="The reader wants to understand why school matters after a child loses a parent or caregiver, and how education support stabilizes more than academics.",
        cluster_boundary="This page owns school continuity, supplies, uniforms, transportation, attendance, routine, and future opportunity. It must not become a broad 10-ways guide or a sponsorship-coverage page.",
        format_decision="New educational guide with program examples and a focused donor angle.",
        intro_guidance="Open with the idea that after loss, school can become one of the few stable structures left in a child's life. Use `orphan education` naturally and explain that the article focuses only on school continuity.",
        links=(
            Link("Syria back-to-school", "https://www.lifeusa.org/post/a-bag-a-notebook-a-second-chance-2-800-orphans-supported-by-life-s-back-to-school-program-in-syri", "back-to-school support for orphans in Syria", "Strong education proof point."),
            Link("Lebanon back-to-school", "https://www.lifeusa.org/post/before-the-first-bell-rang-life-showed-up-and-gave-back-to-school-support-to-500-orphans-in-lebanon", "back-to-school support for orphans in Lebanon", "Education proof point."),
            Link("Afghanistan education", "https://www.lifeusa.org/post/life-for-relief-and-development-usa-life-supports-the-education-of-290-vulnerable-orphans-in-afgha", "education support for vulnerable orphans", "Education proof point."),
            Link("Bangladesh health and school", "https://www.lifeusa.org/post/life-helps-hundreds-of-orphans-stay-healthy-and-in-school-across-bangladesh", "health and school support for orphans", "Education plus health proof point."),
            Link("Kenya classroom", "https://www.lifeusa.org/post/hope-returns-to-the-classroom-through-life-for-relief-and-development-life-s-orphan-sponsorship-in", "classroom support through orphan sponsorship", "Sponsorship/education bridge."),
            *COMMON_LINKS,
        ),
        sections=(
            Section("Why School Stability Matters After Loss", "Define the article's educational scope.", "I know school is important, but why is it urgent after loss?", "`orphan education` 10/mo.", "Explain routine, safety, meals or support structures, adult attention, future opportunity, and social connection.", "Do not turn this into a full list of orphan needs."),
            Section("What Can Interrupt Orphan Education?", "Explain barriers without exaggeration.", "What stops orphaned children from staying in school?", "`orphan education` 10/mo.", "Cover costs, uniforms, supplies, transportation, displacement, caregiver stress, health needs, and documentation barriers where relevant.", "Do not claim LifeUSA solves every barrier in every country."),
            Section("What Education Support Can Include", "Answer the practical donor question.", "What does school support actually pay for?", "`support orphan education` 10/mo variant.", "Discuss backpacks, notebooks, uniforms, school fees where applicable, transportation, tutoring/program support, and health/well-being supports that keep children in class.", "Do not promise tuition or full scholarships unless confirmed."),
            Section("Sponsorship And Education", "Connect to the existing sponsorship guide without duplicating it.", "Can sponsorship help school stability?", "`sponsoring the education of an orphan` 10/mo.", "Explain that sponsorship may support school-related needs depending on program design. Link to sponsorship coverage for details.", "Do not repeat all sponsorship categories."),
            Section("LifeUSA Education Examples", "Ground the guide in real posts.", "I want proof that LifeUSA has supported school continuity.", "`orphan education` 10/mo.", "Use Syria, Lebanon, Afghanistan, Bangladesh, and Kenya examples.", "Do not turn examples into a country-by-country recap dump."),
        ),
        faq=("Why is education important for orphaned children?", "What can interrupt orphan education?", "How can donors support orphan education?", "Can orphan sponsorship help with school?", "Does education support include uniforms and supplies?"),
        meta_title="Orphan Education After Loss: Why School Stability Matters",
        meta_description="Learn why orphan education matters after loss, what barriers can interrupt school, and how support can help children stay equipped, present, and hopeful.",
        review_note="Angela should draft this as a new school-continuity guide. Saiaf should review SEO structure, links, and claim safety before publication.",
        source_note="Google Ads CLI source: orphan education 10/mo, support orphans education 10/mo, sponsoring the education of an orphan 10/mo.",
    ),
    Topic(
        slug="mental-health-support-for-orphaned-children",
        title="Mental Health Support for Orphaned Children: Routine, Safety, and Care After Trauma",
        subtitle="New informational guide. It can use Somaliland and conflict examples as proof, but it does not have to replace the existing Somaliland post.",
        content_type="New informational guide; Angela-owned draft",
        live_url="https://www.lifeusa.org/post/mental-health-support-for-orphaned-children",
        status_note="This should be a new informational guide focused on psychosocial support. Angela drafts it; Saiaf reviews medical-claim safety, SEO structure, links, and keyword use.",
        primary_keywords=(("orphan mental health", "10", "Low", "Use in title, intro, one H2, metadata, and FAQ."),),
        secondary_keywords=(("war orphans", "390", "Low", "Use carefully in trauma/conflict section, not as the main topic."), ("orphan crisis", "10", "Low", "Use only if natural in crisis context.")),
        reader_problem="The reader wants to understand how loss, war, displacement, and instability affect orphaned children emotionally, and what responsible support can look like.",
        cluster_boundary="This page owns psychosocial support, routine, safety, trusted adults, school connection, play, and dignity. It must not become a clinical mental-health article, a general orphan needs guide, or a sponsorship coverage article.",
        format_decision="New informational guide with strong medical-claim guardrails.",
        intro_guidance="Open by saying orphaned children may need more than material support, especially after loss or crisis. Then set the boundary: this article is not medical advice, but explains supportive conditions that can help children feel safer and more stable.",
        links=(
            Link("Somaliland mental health", "https://www.lifeusa.org/post/life-for-relief-and-development-life-cares-for-the-mental-health-of-orphaned-children-in-somalilan", "mental health support for orphaned children", "Primary proof point."),
            Link("Somaliland stability", "https://www.lifeusa.org/post/life-for-relief-and-development-life-sponsorship-program-restored-hope-and-stability-for-134-orpha", "hope and stability for orphaned children", "Stability proof point."),
            Link("Gaza war orphans context", "https://www.lifeusa.org/post/who-will-watch-over-the-orphans-of-gaza", "war orphans and caregiver loss", "Conflict context link."),
            Link("Ghana orphan party", "https://www.lifeusa.org/post/a-day-of-laughter-and-hope-for-ghana-s-orphaned-children-at-the-life-global-orphan-party-2026", "laughter and hope for orphaned children", "Joy/social support proof point."),
            Link("Let them play", "https://www.lifeusa.org/post/let-them-play-life-gives-every-child-a-chance-to-be-a-child-at-the-global-orphan-eid-parties", "a chance to be a child", "Play/dignity support."),
            *COMMON_LINKS,
        ),
        sections=(
            Section("Why Mental Health Support Matters After Loss", "Define the page's unique informational role.", "I understand material needs, but what about emotional needs?", "`orphan mental health` 10/mo.", "Explain grief, fear, disrupted routine, isolation, and the need for safe relationships. Keep this non-clinical.", "Do not diagnose children or describe treatment protocols."),
            Section("How War And Crisis Can Affect Children", "Use high-demand conflict keyword without hijacking the page.", "How is this different for war orphans?", "`war orphans` 390/mo as support.", "Discuss exposure to violence, displacement, caregiver loss, school interruption, and uncertainty.", "Do not make unsourced current-conflict claims."),
            Section("Supportive Conditions That Help Children Feel Safer", "Give practical, non-medical substance.", "What kind of support helps?", "`orphan mental health` 10/mo.", "Cover routine, school attendance, trusted caregivers, safe spaces, play, peer connection, food security, and dignity.", "Do not promise healing, recovery, or therapy outcomes."),
            Section("Where Sponsorship And Program Support Fit", "Connect to LifeUSA without duplicating sponsorship mechanics.", "Can donor support help emotional stability?", "`orphan crisis` 10/mo if natural.", "Explain that material stability can support emotional stability when programs provide consistent care, school support, and safe routines.", "Do not repeat every sponsorship coverage category."),
            Section("LifeUSA Examples To Use Carefully", "Ground the guide in proof while avoiding clinical overclaiming.", "I want real examples.", "`orphan mental health` 10/mo.", "Use the Somaliland mental-health post, stability/sponsorship post, and joy/play examples.", "Do not imply all programs include counseling unless confirmed."),
        ),
        faq=("Why do orphaned children need mental health support?", "How can war affect orphaned children emotionally?", "What helps orphaned children feel safe after trauma?", "Can school and routine support mental health?", "Is this the same as therapy?"),
        meta_title="Mental Health Support for Orphaned Children After Loss",
        meta_description="Learn why orphaned children may need emotional support after loss or crisis, and how routine, safety, school, play, and trusted care can help.",
        review_note="Angela should draft this as a new informational guide. Saiaf should review it for medical-claim safety before publication. Use non-clinical language unless LifeUSA provides program details.",
        source_note="Google Ads CLI source: orphan mental health 10/mo; supported by war orphans 390/mo for conflict-trauma context.",
    ),
)


DEEPENING = {
    "gaza-orphans-war-care-safety-support": {
        "thesis": "War orphanhood is not only the death of a parent; in Gaza it can mean the collapse of the care systems a child depends on: safe shelter, food, school, medical access, family routine, and trusted adults.",
        "promise": (
            "Define war orphans without repeating the general orphan-definition article.",
            "Explain the Gaza-specific layers of risk: caregiver loss, displacement, hunger, school disruption, winter exposure, and fear.",
            "Show how LifeUSA examples map to concrete needs rather than dropping links as decoration.",
            "End with a focused Gaza/orphan support path, not a generic donation close.",
        ),
        "intro": (
            "When people search for war orphans or Gaza orphans, they are usually trying to understand more than a label. They are trying to understand what happens to a child when violence breaks the circle of adults, routines, homes, schools, and community support that normally protects childhood.\n\n"
            "In Gaza, that question becomes painfully concrete. A child may lose a parent, become separated from relatives, move from place to place, miss school, sleep without reliable warmth, or depend on already-overstretched caregivers for food and safety. This article should explain those layers clearly and humanely, then show how relief work can respond to immediate needs while preserving dignity."
        ),
        "depth": (
            ("Define war orphanhood as loss of parental/caregiver protection in conflict, then link out for general orphan definitions.", "Name the specific disruptions war creates: separation, displacement, food insecurity, interrupted school, fear, and unstable caregiving.", "Use `war orphans` and `gaza orphans` once each in natural sentences, not as repeated labels."),
            ("Make Gaza the setting of the risks, not a vague crisis backdrop.", "Use cautious phrasing for facts that may change; leave placeholders for Saiaf to add current verified figures if needed.", "Explain layered vulnerability: a child can have a surviving relative and still lack stable care, shelter, food, or schooling."),
            ("Organize aid by need category: food, essentials, caregiver support, winter relief, education continuity, and moments of dignity.", "Explain why each category matters for a child, not only what the charity provides.", "Link to the broader how-to-help pillar only after this article has answered the Gaza-specific question."),
            ("Use 3 to 5 LifeUSA examples and connect each to a need category.", "Prioritize Gaza food packs, baby formula/essentials, winter relief, Eid support, and the Gaza orphan campaign.", "Avoid a recap dump; each example should prove one point in the argument."),
            ("Close with a clear next step for readers who want to help Gaza orphans.", "Use the Gaza orphan campaign and established orphan donation path.", "Keep the CTA relief-focused and avoid drifting into sponsorship mechanics."),
        ),
    },
    "why-gifts-for-orphans-matter": {
        "thesis": "Gifts for orphans matter when they protect dignity, joy, belonging, and the right to childhood alongside food, safety, school, and long-term care.",
        "promise": (
            "Answer the reader's skepticism: gifts are not replacements for urgent needs, but they are not meaningless extras.",
            "Explain joy, play, Eid, memory, and being remembered as part of emotional care.",
            "Show what responsible gift programs should consider: safety, age, dignity, privacy, and coordination.",
            "Use LifeUSA joy/gift examples without turning the article into a simple event recap.",
        ),
        "intro": (
            "It is reasonable to ask whether gifts for orphans should matter when children also need food, shelter, school, healthcare, and safety. The answer should not pretend that a toy or Eid gift solves loss. It does not.\n\n"
            "But a gift can still carry meaning. For a child who has lost a parent or lives with instability, a thoughtful gift can say: you are remembered, you are included, and your childhood still matters. This article should make that case carefully, showing how joy and dignity fit beside practical support rather than competing with it."
        ),
        "depth": (
            ("Open by acknowledging the basic-needs objection directly.", "Explain gifts as dignity and belonging, not as a substitute for care.", "Use `gifts for orphans` naturally in the first paragraph and one H2."),
            ("Discuss play, celebration, memory, and social connection as childhood needs.", "Avoid clinical claims; say gifts can support normalcy and belonging, not cure trauma.", "Tie this to the phrase 'right to childhood' so the angle is distinct."),
            ("Treat Eid gifts as a concrete seasonal example, not a religious tangent.", "Use `eid gifts for orphans` once in the Eid section.", "Keep religious language light and inclusive for a US donor audience."),
            ("Define responsible gifting: useful, age-appropriate, safe, locally coordinated, and privacy-conscious.", "Warn against uncoordinated direct gifts or photo-driven charity framing.", "Explain that programs should avoid making children feel like props."),
            ("Use LifeUSA joy examples as proof of the argument: Ghana, Gaza Eid, global orphan parties, and play-focused articles.", "Choose examples that illustrate dignity and joy, not just distribution numbers.", "Close by connecting gifts to broader orphan support."),
        ),
    },
    "orphan-education-after-loss": {
        "thesis": "Orphan education is not only about school supplies; after the loss of a parent or caregiver, school can become one of the few stable structures that keeps a child connected to routine, adults, peers, meals, safety, and future possibility.",
        "promise": (
            "Explain why school stability matters after loss.",
            "Identify the barriers that commonly interrupt orphan education.",
            "Show what education support can include without promising unconfirmed scholarships or tuition coverage.",
            "Give Angela a clear article path that links to LifeUSA school-support examples and avoids repeating the broad orphan-help pillar.",
        ),
        "intro": (
            "After a child loses a parent or caregiver, school can become more than a classroom. It can be the place where a child returns to routine, sees familiar adults, connects with other children, receives supplies or support, and keeps a sense of future from disappearing.\n\n"
            "That is why orphan education deserves its own guide. This article should explain what can interrupt school after loss, what support can help a child stay enrolled and prepared, and how donors can think about education as part of stability rather than a separate luxury."
        ),
        "depth": (
            ("Explain school as routine, safety, social connection, and future opportunity.", "Avoid generic 'education is important' language; make it specific to orphaned children after loss.", "Use `orphan education` in the intro and first H2."),
            ("Break barriers into practical categories: costs, supplies, uniforms, transport, displacement, caregiver stress, health, and documentation.", "Use LifeUSA examples later; first make the barrier logic clear.", "Avoid implying every barrier exists in every country."),
            ("List possible support areas: backpacks, notebooks, uniforms, fees where applicable, transport, tutoring/program support, and health support that keeps children in school.", "Use cautious language: 'can include' and 'depending on the program.'", "Do not promise tuition, scholarships, or named benefits unless LifeUSA confirms them."),
            ("Explain how sponsorship may support education indirectly or directly depending on program design.", "Link to the sponsorship coverage guide for the full mechanics.", "Keep this section short enough that it does not cannibalize the sponsorship article."),
            ("Use Syria, Lebanon, Afghanistan, Bangladesh, and Kenya examples as proof points.", "Organize examples by education function: supplies, school access, health/school continuity, classroom stability.", "End with a donor-facing bridge to support orphan education through LifeUSA."),
        ),
    },
    "mental-health-support-for-orphaned-children": {
        "thesis": "Mental health support for orphaned children should be framed as safety, routine, trusted care, school connection, play, and dignity after loss or trauma, while avoiding medical advice or unsupported therapy claims.",
        "promise": (
            "Explain emotional needs after orphanhood without diagnosing children.",
            "Connect conflict and war-orphan contexts to trauma carefully and non-politically.",
            "Define supportive conditions donors can understand: stable adults, routine, school, safe spaces, play, and basic-needs security.",
            "Use Somaliland and joy/play examples as proof while staying inside claim-safe language.",
        ),
        "intro": (
            "When a child loses a parent or caregiver, the need for help is not only material. Food, clothing, shelter, and school matter deeply, but children also need safety, routine, trusted adults, and moments where they can feel like children again.\n\n"
            "This guide should explain mental health support for orphaned children in non-clinical language. It should not diagnose children or promise healing. Instead, it should show how stable care, school connection, play, dignity, and consistent support can help create the conditions children need after loss, displacement, or trauma."
        ),
        "depth": (
            ("Frame emotional support as part of care after loss, not as a clinical treatment article.", "Mention grief, fear, disrupted routine, isolation, and the need for trusted adults.", "Use `orphan mental health` once in a natural sentence."),
            ("Use `war orphans` carefully to explain why conflict can intensify fear, instability, displacement, and school disruption.", "Avoid current casualty claims unless Saiaf adds verified sources.", "Link to the Gaza article for the conflict-specific angle instead of repeating it."),
            ("Define supportive conditions: routine, safe shelter, school attendance, trusted caregivers, peer connection, play, food security, and dignity.", "Make this the most substantial section; it is the article's practical heart.", "Avoid therapy language unless LifeUSA confirms professional services."),
            ("Explain how sponsorship or program support can create consistency around material needs, school, and caregiver support.", "Link to the sponsorship coverage article for details.", "Avoid saying sponsorship provides mental-health treatment."),
            ("Use Somaliland mental-health and stability posts, plus Ghana/play/Eid examples.", "State what each example can support as evidence: care, stability, joy, routine, or social connection.", "Add a final claim-safety reminder before publication."),
        ),
    },
}


TEMPLATE_DATA = {
    "gaza-orphans-war-care-safety-support": {
        "audience": "US donors and supporters trying to understand how war affects orphaned children in Gaza and what kind of aid is relevant.",
        "reader_stage": "Learning and deciding: the reader is trying to understand the crisis before choosing a support path.",
        "trust_blockers": "Unsourced casualty claims, political overreach, generic donation language, or treating Gaza orphans as the same topic as general orphan support.",
        "journey": "I hear about Gaza orphans -> what does war orphanhood actually mean? -> what risks do children face? -> what support helps? -> what LifeUSA proof exists? -> where should I help?",
        "serp_competitors": (
            Link("World Care Foundation - Gaza's Orphans", "https://www.worldcarefoundation.org/appeal/gza-orphans/", "Gaza orphan appeal", "Campaign/sponsorship page with food, shelter, medical care, and essential-needs framing."),
            Link("PCRF - Orphan Sponsorship Helps Children in Gaza", "https://www.pcrf.net/information-you-should-know/how-orphan-sponsorship-helps-children-in-gaza.html", "orphan sponsorship in Gaza", "Explains immediate needs and psychological impact."),
            Link("UNRWA USA - Gaza orphan support", "https://www.unrwausa.org/orphans", "Gaza orphan support", "Donation page with cash-assistance framing and donation amounts."),
            Link("Islamic Relief Worldwide - Sponsor an Orphan in Gaza", "https://islamic-relief.org/orphan-sponsorship-programme/sponsor-an-orphan-in-gaza/", "sponsor an orphan in Gaza", "Sponsorship page with stipend, seasonal distributions, Eid gifts, and winter items."),
            Link("UNICEF - Children in Gaza need life-saving support", "https://www.unicef.org/emergencies/children-gaza-need-lifesaving-support", "children in Gaza need support", "Authoritative crisis context around health, displacement, and basic care."),
        ),
        "serp_features": "SERP snapshot includes charity campaign pages, sponsorship pages, UNICEF crisis context, social posts, and news results. News/current-affairs results appear for Gaza child trauma and education disruption.",
        "paid_ads": "Paid ads were not verified in this browser snapshot. Do not make a paid-ads claim without Ahrefs or live Google Ads preview evidence.",
        "content_pattern": "Ranking/visible pages are mostly donation appeals and sponsorship pages. Strong pages quickly move from crisis description to monthly support, stipend, or emergency relief.",
        "serp_notes": "LifeUSA can win a more useful middle ground: not just a donation page and not just news. The page should explain the child-care problem in Gaza, then prove LifeUSA's relevant relief examples.",
        "current_rank": "Existing LifeUSA Gaza article is the rewrite target. Current ranking for `war orphans` / `gaza orphans` was not verified through GSC in this pass.",
        "image_notes": "Use real Gaza relief or orphan-support imagery only if LifeUSA has publishing rights and child-safety approval. Avoid identifiable child closeups if consent/privacy is unclear.",
        "schema_notes": "Use Article schema. FAQ schema is optional only if Wix allows clean FAQ markup and the final article includes visible FAQs.",
        "info_gain": (
            "Connect war orphanhood to care-system collapse, not only parent death.",
            "Map LifeUSA Gaza examples to concrete needs: food, formula/essentials, winter relief, Eid joy, and the Gaza orphan campaign.",
            "Use claim-safe Gaza language with room for Saiaf to add verified current figures before publishing.",
            "Create a bridge between crisis education and a focused support path.",
        ),
        "appendix_sources": (
            "Google Ads CLI: `war orphans` 390/mo, `gaza orphans` 170/mo.",
            "Existing LifeUSA rewrite target: https://www.lifeusa.org/post/who-will-watch-over-the-orphans-of-gaza",
            "SERP snapshot sources: World Care Foundation, PCRF, UNRWA USA, Islamic Relief Worldwide, UNICEF.",
            "Open question: add current Gaza statistics only from verified sources before publication.",
        ),
    },
    "why-gifts-for-orphans-matter": {
        "audience": "Donors who wonder whether gifts, Eid gifts, and joy programs are meaningful when orphaned children also need urgent practical care.",
        "reader_stage": "Learning and deciding: the reader wants to know whether gift giving is responsible and worth supporting.",
        "trust_blockers": "A shallow gift list, exaggerated emotional claims, implying gifts replace food/school/safety, or using children as donation props.",
        "journey": "I see gifts for orphans -> is this actually helpful? -> what kind of need does joy meet? -> what makes gifting responsible? -> how has LifeUSA done this? -> how can I support it?",
        "serp_competitors": (
            Link("Basmah - Eid Gifts for Children", "https://basmah.org/eid-gifts-for-children/", "Eid gifts for children", "Donation packages for Eid gift packs, toys, clothes, and shoes."),
            Link("Orphans in Need - Eid al-Adha Gifts", "https://www.orphansinneed.org.uk/appeals/eid-al-adha-gifts/", "Eid gifts matter", "Explains gifts as remembered, new outfit, toy, school supplies, and lasting memory."),
            Link("Al Mustafa Welfare Trust - Eid Gift for Orphan", "https://www.almustafausa.org/ramadan/orphan-eid-gift/", "Eid gift for orphan", "Religious/seasonal appeal with celebration framing."),
            Link("LifeUSA - Why One Gift Means the World", "https://www.lifeusa.org/post/why-one-gift-means-the-world-to-an-orphaned-child", "one gift means the world", "Existing LifeUSA article and enrichment target."),
        ),
        "serp_features": "SERP snapshot is dominated by charity/Eid campaign pages, donation cards, seasonal appeals, and social posts about dignity, smiles, and children feeling remembered.",
        "paid_ads": "Paid ads were not verified in this browser snapshot. Treat ad presence as unknown unless checked in Ahrefs or Google.",
        "content_pattern": "Most pages are transactional seasonal gift appeals. Few explain the dignity/childhood argument in depth.",
        "serp_notes": "LifeUSA should not write another generic gift-card page. The information gain is explaining why gifts matter responsibly, then tying that to LifeUSA proof examples.",
        "current_rank": "LifeUSA's existing gift article appeared in the sampled search results for this topic. Exact rank should be checked in GSC/Ahrefs before final prioritization.",
        "image_notes": "Use celebration/gift images that show dignity and group joy. Avoid close-up identifiable child imagery unless LifeUSA has consent and approval.",
        "schema_notes": "Use Article schema. FAQ schema can support gift/Eid questions if the final page includes visible FAQs.",
        "info_gain": (
            "Answer the donor objection that gifts are secondary without dismissing joy and dignity.",
            "Separate responsible gift programs from uncoordinated direct gifting.",
            "Use LifeUSA's Global Orphan Parties, Gaza Eid support, and gift-program examples as proof.",
            "Frame gifts as part of childhood, not as a cure or replacement for urgent needs.",
        ),
        "appendix_sources": (
            "Google Ads CLI: `gifts for orphans` 20/mo, `eid gifts for orphans` 10/mo.",
            "Existing LifeUSA rewrite target: https://www.lifeusa.org/post/why-one-gift-means-the-world-to-an-orphaned-child",
            "SERP snapshot sources: Basmah, Orphans in Need, Al Mustafa Welfare Trust, LifeUSA.",
            "Open question: confirm which LifeUSA gift/donation CTA should be used if separate from the orphan donation designation.",
        ),
    },
    "orphan-education-after-loss": {
        "audience": "Donors and supporters who want to understand why school continuity matters for orphaned children after loss.",
        "reader_stage": "Learning and deciding: the reader understands education matters but needs the orphan-specific case and support path.",
        "trust_blockers": "Generic education-is-important language, overpromising tuition/scholarships, or repeating the broad orphan-help pillar.",
        "journey": "I care about orphan education -> why is school stability urgent after loss? -> what interrupts school? -> what support helps? -> what LifeUSA examples prove this? -> how can donors help responsibly?",
        "serp_competitors": (
            Link("PMC - School Support Intervention", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5693735/", "school support intervention for orphaned adolescents", "Research result showing school support can affect educational outcomes."),
            Link("Restore Hope Today - Orphan Education Program", "https://www.restorehopetoday.org/oep/", "orphan education program", "Program page listing tutoring, vocational training, and college tuition/fees assistance."),
            Link("Pakistan Children Relief - Education for Orphaned Children", "https://www.pakcr.org/blog/the-role-of-education-in-empowering-orphaned-children-for-a-better-future/", "education for orphaned children", "Broad empowerment article with cognitive/social development framing."),
        ),
        "serp_features": "SERP snapshot mixes research, program pages, broad nonprofit articles, and social/forum-style education advice.",
        "paid_ads": "Paid ads were not verified in this browser snapshot.",
        "content_pattern": "Visible pages either sell an education program or explain education broadly. Few focus on school stability after bereavement/loss.",
        "serp_notes": "LifeUSA can make the topic more specific: after loss, school is routine, adult contact, supplies, peers, safety, and future continuity. Use LifeUSA country examples as proof.",
        "current_rank": "This is a proposed new guide. Current LifeUSA ranking for `orphan education` was not verified in GSC in this pass.",
        "image_notes": "Use school supplies, classroom, backpack, or group learning images with consent-safe framing. Alt text should describe the educational support, not exploit child vulnerability.",
        "schema_notes": "Use Article schema and optional FAQ schema. Avoid HowTo schema unless the final article becomes a step-by-step donor process.",
        "info_gain": (
            "Position school as stability after loss, not only academic achievement.",
            "Connect barriers to practical support categories without overpromising tuition.",
            "Use LifeUSA Syria, Lebanon, Afghanistan, Bangladesh, and Kenya examples to prove school-continuity work.",
            "Keep the page narrow enough that it does not cannibalize the orphan-help pillar or sponsorship guide.",
        ),
        "appendix_sources": (
            "Google Ads CLI: `orphan education` 10/mo, `support orphans education` 10/mo, `sponsoring the education of an orphan` 10/mo.",
            "SERP snapshot sources: PMC school support study, Restore Hope Today, Pakistan Children Relief.",
            "LifeUSA proof pages: Syria, Lebanon, Afghanistan, Bangladesh, and Kenya education/orphan posts.",
            "Open question: confirm exact LifeUSA education-related CTA if different from general orphan support.",
        ),
    },
    "mental-health-support-for-orphaned-children": {
        "audience": "Donors and supporters who understand material orphan support but want to understand emotional safety, trauma, routine, and psychosocial support after loss.",
        "reader_stage": "Learning and verifying trust: the reader needs a careful, non-clinical explanation before supporting or sharing.",
        "trust_blockers": "Medical overclaims, therapy promises, diagnosing children, unsupported trauma claims, or turning mental health into a donation slogan.",
        "journey": "I know orphaned children need material support -> what about emotional needs? -> how do loss and war affect stability? -> what support is safe to discuss? -> what LifeUSA examples exist? -> what should be reviewed before publishing?",
        "serp_competitors": (
            Link("Duke Global Health - Mental Health Services Critical for Orphans", "https://globalhealth.duke.edu/news/protective-and-mental-health-services-critical-orphans-worldwide", "mental health services for orphans", "Research/news result emphasizing protection and mental health services."),
            Link("PMC - Childhood trauma and depressive symptoms", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12642290/", "childhood trauma among orphaned children", "Research result linking trauma exposure and depressive symptoms."),
            Link("BMJ Global Health - Care environment and mental health", "https://gh.bmj.com/content/6/3/e003644", "care environment and mental health of orphaned children", "Research result on care environment and mental health risk."),
            Link("A Child's Hope Foundation - Mental Health Needs", "https://achildshopefoundation.org/2021/05/20/addressing-mental-health-needs-of-orphaned-children/", "mental health needs of orphaned children", "Nonprofit page that leans toward counseling/healing language."),
            Link("Embrace Relief - Emotional Well-Being", "https://www.embracerelief.org/mental-health-matters-addressing-emotional-well-being-in-orphaned-children/", "emotional well-being in orphaned children", "Nonprofit article discussing therapeutic support, belonging, and nurturing environments."),
        ),
        "serp_features": "SERP snapshot mixes academic/research pages and nonprofit articles. Some competing pages use clinical or therapy language.",
        "paid_ads": "Paid ads were not verified in this browser snapshot.",
        "content_pattern": "Ranking/visible content often discusses trauma, counseling, protective services, and care environments. The risk is overclaiming beyond LifeUSA's confirmed program details.",
        "serp_notes": "LifeUSA's page should be explicitly non-clinical: safety, routine, trusted adults, school connection, play, dignity, and stable support. That is the safer information gain.",
        "current_rank": "This is a proposed new guide. Current LifeUSA ranking for `orphan mental health` was not verified in GSC in this pass.",
        "image_notes": "Use non-clinical, dignity-first imagery: safe group activities, school, play, or caregiver-supported environments. Avoid sad-child closeups and therapy-implying photos unless program details support them.",
        "schema_notes": "Use Article schema and optional FAQ schema. Do not use MedicalWebPage or medical schema unless LifeUSA publishes clinically reviewed medical content.",
        "info_gain": (
            "Translate mental-health need into donor-safe support conditions rather than medical treatment claims.",
            "Use LifeUSA Somaliland mental-health/stability examples while clearly separating confirmed program details from general psychosocial principles.",
            "Connect war orphans to trauma carefully, then link out to the Gaza-specific page instead of repeating it.",
            "Give Angela explicit claim guardrails so the article stays useful and safe.",
        ),
        "appendix_sources": (
            "Google Ads CLI: `orphan mental health` 10/mo; `war orphans` 390/mo as supporting conflict context.",
            "SERP snapshot sources: Duke Global Health, PMC, BMJ Global Health, A Child's Hope Foundation, Embrace Relief.",
            "LifeUSA proof pages: Somaliland mental-health post, Somaliland stability/sponsorship post, Gaza orphan article, Ghana/global play examples.",
            "Open question: confirm whether LifeUSA provides counseling, psychosocial support, referrals, or only broader stability/mental-health programming before final wording.",
        ),
    },
}


def md_table(rows: tuple[tuple[str, str, str, str], ...]) -> str:
    lines = ["| Keyword | Avg. monthly searches | Competition | Use |", "|---|---:|---|---|"]
    for kw, volume, comp, use in rows:
        lines.append(f"| `{kw}` | {volume} | {comp} | {use} |")
    return "\n".join(lines)


def link_table(links: tuple[Link, ...]) -> str:
    lines = ["| Page | URL | Suggested anchor | Note |", "|---|---|---|---|"]
    for link in links:
        lines.append(f"| {link.label} | `{link.url}` | {link.anchor} | {link.note} |")
    return "\n".join(lines)


def deep(topic: Topic, key: str):
    return DEEPENING[topic.slug][key]


def tdata(topic: Topic, key: str):
    return TEMPLATE_DATA[topic.slug][key]


def bullet_md(items: tuple[str, ...]) -> str:
    return "\n".join(f"- {item}" for item in items)


def depth_plan_md(topic: Topic) -> str:
    out: list[str] = []
    for idx, section in enumerate(topic.sections, 1):
        out.append(f"### {idx}. {section.title}")
        for item in deep(topic, "depth")[idx - 1]:
            out.append(f"- {item}")
        out.append("")
    return "\n".join(out).strip()


def serp_competitors_md(topic: Topic) -> str:
    return link_table(tdata(topic, "serp_competitors"))


def appendix_md(topic: Topic) -> str:
    return bullet_md(tdata(topic, "appendix_sources"))


def outline_sections_md(topic: Topic) -> str:
    out: list[str] = []
    for idx, section in enumerate(topic.sections, 1):
        out.append(f"## H2 {idx}: {section.title}\n")
        out.append(f"Why this section is here:\n\n{section.why}\n")
        out.append(f"Reader stage:\n\n{section.stage}\n")
        out.append(f"Keyword ownership:\n\n{section.keywords}\n")
        out.append(f"{section_write_label(topic)}:\n\n{section.write}\n")
        out.append("Depth requirements:\n")
        for item in deep(topic, "depth")[idx - 1]:
            out.append(f"- {item}")
        out.append("")
        out.append(f"What to avoid:\n\n{section.avoid}\n")
        if section.links:
            out.append("Suggested internal links:\n")
            for link in section.links:
                out.append(f"- [{link.anchor}]({link.url}) - {link.note}")
            out.append("")
    return "\n".join(out).strip()


def build_brief(topic: Topic) -> str:
    return dedent(f"""\
    # Brief: {topic.title}

    ## 1. Article Setup

    - **Content type:** {topic.content_type}
    - **Owner:** {brief_owner(topic)}
    - **Proposed/live URL:** `{topic.live_url}`
    - **Current rank:** {tdata(topic, "current_rank")}
    - **Status note:** {topic.status_note}
    - **Keyword source:** `{KW_EXACT}` and `{KW_REWRITE}`. Google Ads CLI is the demand source; Ahrefs is helper-only if used later for SERP shape.

    ## 2. Audience And Reader Need

    - **Audience:** {tdata(topic, "audience")}
    - **Reader question:** {topic.reader_problem}
    - **Reader stage:** {tdata(topic, "reader_stage")}
    - **What would make them leave:** {tdata(topic, "trust_blockers")}

    ## 3. Keywords And Search Demand

    ### Primary Keywords

    {md_table(topic.primary_keywords)}

    ### Secondary Keywords

    {md_table(topic.secondary_keywords)}

    ## 4. SERP And Competition

    ### Top competing / visible URLs

    {serp_competitors_md(topic)}

    - **Search result features:** {tdata(topic, "serp_features")}
    - **Paid ads:** {tdata(topic, "paid_ads")}
    - **Content pattern:** {tdata(topic, "content_pattern")}
    - **SERP notes:** {tdata(topic, "serp_notes")}

    ## 5. Format Decision

    {topic.format_decision}

    ## Article Thesis

    {deep(topic, "thesis")}

    ## Searcher Promise

    {bullet_md(deep(topic, "promise"))}

    ## 6. Reader Profile And Journey

    - **Who they are:** {tdata(topic, "audience")}
    - **What they already believe:** They care about orphaned children but need a clearer explanation of this specific topic.
    - **What they need next:** {topic.reader_problem}
    - **What could block trust:** {tdata(topic, "trust_blockers")}

    `{tdata(topic, "journey")}`

    ## Non-Cannibalization Rule

    {topic.cluster_boundary}

    ## 7. Intro Guidance

    {topic.intro_guidance}

    ## Working Intro Draft

    {deep(topic, "intro")}

    ## 8. Section Outline / Depth Plan

    {depth_plan_md(topic)}

    ## 9. Internal Links And Next Step

    {link_table(topic.links)}

    ## 10. Metadata, FAQ, Images, And Schema

    - **Meta title:** {topic.meta_title}
    - **Meta description:** {topic.meta_description}
    - **FAQ targets:** {", ".join(topic.faq)}
    - **Image notes:** {tdata(topic, "image_notes")}
    - **Schema notes:** {tdata(topic, "schema_notes")}

    ## 11. Information Gain

    {bullet_md(tdata(topic, "info_gain"))}

    ## 12. Internal Appendix

    {appendix_md(topic)}

    ## Review Note

    {topic.review_note}

    ## Source Note

    {topic.source_note}

    ## Anti-Cannibalization Checklist

    - Does this repeat the `What Is an Orphan?` definition article? If yes, cut the definition section and link out.
    - Does this repeat the broad `How To Help Orphans` pillar? If yes, narrow the article to its approved angle.
    - Does this repeat `What Does Orphan Sponsorship Cover?`? If yes, remove sponsorship mechanics and link out.
    - Does this use Google Ads CLI search volume as demand evidence? If no, do not approve the outline.
    - Does this have a live LifeUSA proof page or a clear existing article to enrich? If no, do not approve the outline.
    """)


def build_outline(topic: Topic) -> str:
    faqs = "\n".join(f"- {q}" for q in topic.faq)
    return dedent(f"""\
    # Outline: {topic.title}

    ## 1. Article Setup

    - **Working title:** {topic.title}
    - **Proposed/live URL:** `{topic.live_url}`
    - **Article type:** {topic.content_type}
    - **Current rank:** {tdata(topic, "current_rank")}
    - **Writer:** {"Angela" if is_new_guide(topic) else "Saiaf"}
    - **Review owner:** Saiaf for SEO, links, sensitive claims, and final LifeUSA fit.

    ## 2. Audience And Reader Need

    - **Audience:** {tdata(topic, "audience")}
    - **Reader question:** {topic.reader_problem}
    - **Reader stage:** {tdata(topic, "reader_stage")}
    - **What would make them leave:** {tdata(topic, "trust_blockers")}

    ## 3. Keywords And Search Demand

    Primary keywords:

    {md_table(topic.primary_keywords)}

    Secondary keywords:

    {md_table(topic.secondary_keywords)}

    ## 4. SERP And Competition

    {serp_competitors_md(topic)}

    - **Search result features:** {tdata(topic, "serp_features")}
    - **Paid ads:** {tdata(topic, "paid_ads")}
    - **Content pattern:** {tdata(topic, "content_pattern")}
    - **Notes about the results page:** {tdata(topic, "serp_notes")}

    ## 5. Format Decision

    {topic.format_decision}

    ## Article Thesis

    {deep(topic, "thesis")}

    ## Searcher Promise

    {bullet_md(deep(topic, "promise"))}

    ## 6. Reader Profile And Journey

    ```text
    {tdata(topic, "journey")}
    ```

    ## Non-Cannibalization Rule

    {topic.cluster_boundary}

    ## 7. Intro Guidance

    Guidance:

    {topic.intro_guidance}

    Draft intro:

    {deep(topic, "intro")}

    ## 8. Section Outline

    {outline_sections_md(topic)}

    ## 9. Internal Links And Next Step

    {link_table(topic.links)}

    ## 10. Metadata, FAQ, Images, And Schema

    - **Meta title:** {topic.meta_title}
    - **Meta description:** {topic.meta_description}
    - **Image notes:** {tdata(topic, "image_notes")}
    - **Schema notes:** {tdata(topic, "schema_notes")}

    FAQ targets:

    {faqs}

    ## 11. Information Gain

    {bullet_md(tdata(topic, "info_gain"))}

    ## 12. Internal Appendix

    {appendix_md(topic)}

    ## Adversarial Review

    - **Repetition risk:** compare against `What Is an Orphan?`, `How To Help Orphans`, and `What Does Orphan Sponsorship Cover?` before drafting.
    - **Claim risk:** avoid medical, legal, adoption, custody, direct-child-contact, or guaranteed-outcome claims unless LifeUSA confirms them.
    - **Keyword risk:** do not force low-volume phrases repeatedly. Use them once where natural and let the article's distinct angle carry the page.
    - **Link risk:** use the planned `How To Help Orphans` GitHub outline until the Wix URL is live; do not link to the 404 Wix URL yet.
    - **Owner risk:** {owner_risk_note(topic)}
    """)


CSS = """
    :root {
      --ink: #17231e; --muted: #617067; --paper: #f4f1e9; --card: #fffdf7;
      --green: #116149; --green2: #dbece5; --gold: #c79236; --red: #a63b32;
      --line: #d9ddd6; --shadow: 0 18px 55px rgba(31,48,40,.10);
    }
    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body { margin: 0; color: var(--ink); background: var(--paper); font-family: "Thmanyah Serif Text", "Noto Naskh Arabic", Georgia, serif; line-height: 1.75; }
    body:before { content: ""; position: fixed; inset: 0; pointer-events: none; opacity: .35; background-image: radial-gradient(#b7b0a1 .6px, transparent .6px); background-size: 10px 10px; }
    .wrap { position: relative; max-width: 1160px; margin: auto; padding: 32px 22px 80px; }
    header { color: white; background: linear-gradient(135deg,#0b4b39,#153126); border-radius: 28px; padding: 52px; box-shadow: var(--shadow); overflow: hidden; position: relative; }
    header:after { content: "L"; position: absolute; right: 28px; bottom: -62px; font: 900 210px/1 Arial; color: rgba(255,255,255,.055); }
    .eyebrow { display: inline-block; padding: 5px 13px; border: 1px solid rgba(255,255,255,.35); border-radius: 99px; font-size: .82rem; letter-spacing: .08em; text-transform: uppercase; }
    h1 { max-width: 930px; margin: 18px 0 8px; font-size: clamp(2.15rem,5vw,4.45rem); line-height: 1.08; }
    header p { max-width: 820px; color: #d9ebe4; font-size: 1.12rem; }
    .meta { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 22px; }
    .meta span { background: rgba(255,255,255,.1); padding: 7px 12px; border-radius: 8px; }
    nav { position: sticky; top: 10px; z-index: 4; display: flex; gap: 8px; overflow: auto; margin: 18px 0 28px; padding: 9px; background: rgba(255,253,247,.92); border: 1px solid var(--line); border-radius: 15px; backdrop-filter: blur(12px); }
    nav a { white-space: nowrap; text-decoration: none; color: var(--green); padding: 7px 12px; border-radius: 8px; font-weight: 700; }
    section { scroll-margin-top: 90px; background: var(--card); border: 1px solid var(--line); border-radius: 22px; padding: 34px; margin: 20px 0; box-shadow: 0 7px 25px rgba(31,48,40,.045); }
    h2 { color: var(--green); margin: 0 0 18px; font-size: 1.8rem; line-height: 1.25; }
    h3 { margin: 28px 0 8px; font-size: 1.18rem; color: #214336; }
    p { margin: 7px 0 14px; }
    a { color: var(--green); overflow-wrap: anywhere; }
    .lede { font-size: 1.13rem; }
    .grid { display: grid; grid-template-columns: repeat(2,minmax(0,1fr)); gap: 15px; }
    .card { border: 1px solid var(--line); border-radius: 15px; padding: 18px; background: #fff; }
    .card h3 { margin: 0 0 6px; color: var(--green); }
    .callout { border-left: 5px solid var(--gold); background: #fff7e7; padding: 15px 18px; border-radius: 12px; margin: 16px 0; }
    .danger { border-color: var(--red); background: #fff0ed; }
    .ok { border-color: var(--green); background: #edf7f2; }
    .way { border-top: 4px solid var(--green); }
    .way h3 { font-size: 1.32rem; color: var(--green); }
    ul, ol { padding-left: 24px; }
    li { margin: 6px 0; }
    code { direction: ltr; unicode-bidi: embed; font-family: "SFMono-Regular", Consolas, monospace; font-size: .88em; }
    table { width: 100%; border-collapse: collapse; text-align: left; font-size: .9rem; }
    th, td { border-bottom: 1px solid var(--line); padding: 10px 8px; vertical-align: top; }
    th { color: var(--green); background: #edf4f0; }
    footer { text-align: center; color: var(--muted); padding: 22px; }
    @media(max-width:760px){ header,section{padding:25px}.grid{grid-template-columns:1fr}h1{font-size:2.35rem} }
"""


def html_escape(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def rows_html(rows: tuple[tuple[str, str, str, str], ...]) -> str:
    return "\n".join(
        f"<tr><td><code>{html_escape(kw)}</code></td><td>{volume}</td><td>{html_escape(comp)}</td><td>{html_escape(use)}</td></tr>"
        for kw, volume, comp, use in rows
    )


def links_html(links: tuple[Link, ...]) -> str:
    return "\n".join(
        f'<tr><td>{html_escape(link.label)}</td><td><a href="{html_escape(link.url)}">{html_escape(link.anchor)}</a></td><td>{html_escape(link.note)}</td></tr>'
        for link in links
    )


def source_links_html(links: tuple[Link, ...]) -> str:
    return "\n".join(
        f'<tr><td><a href="{html_escape(link.url)}">{html_escape(link.label)}</a></td><td>{html_escape(link.note)}</td></tr>'
        for link in links
    )


def bullets_html(items: tuple[str, ...]) -> str:
    return "<ul>" + "\n".join(f"<li>{html_escape(item)}</li>" for item in items) + "</ul>"


def paragraphs_html(text: str, class_name: str = "") -> str:
    class_attr = f' class="{class_name}"' if class_name else ""
    return "".join(
        f"<p{class_attr}>{html_escape(part.strip())}</p>"
        for part in text.strip().split("\n\n")
        if part.strip()
    )


def depth_plan_html(topic: Topic) -> str:
    chunks: list[str] = []
    for idx, section in enumerate(topic.sections, 1):
        chunks.append(
            f"<article class=\"way\"><h3>{idx}. {html_escape(section.title)}</h3>"
            f"{bullets_html(deep(topic, 'depth')[idx - 1])}</article>"
        )
    return "\n".join(chunks)


def sections_html(topic: Topic) -> str:
    chunks: list[str] = []
    for idx, section in enumerate(topic.sections, 1):
        extra = ""
        if section.links:
            extra = "<p><strong>Suggested links:</strong></p><ul>" + "".join(
                f'<li><a href="{html_escape(link.url)}">{html_escape(link.anchor)}</a> - {html_escape(link.note)}</li>'
                for link in section.links
            ) + "</ul>"
        chunks.append(dedent(f"""\
        <article class="way">
          <h3>{idx}. {html_escape(section.title)}</h3>
          <p><strong>Why here:</strong> {html_escape(section.why)}</p>
          <p><strong>Reader stage:</strong> {html_escape(section.stage)}</p>
          <p><strong>Keywords:</strong> {html_escape(section.keywords)}</p>
          <p><strong>{html_escape(section_write_label(topic))}:</strong> {html_escape(section.write)}</p>
          <p><strong>Depth requirements:</strong></p>
          {bullets_html(deep(topic, "depth")[idx - 1])}
          <p><strong>Avoid:</strong> {html_escape(section.avoid)}</p>
          {extra}
        </article>
        """))
    return "\n".join(chunks)


def build_html(topic: Topic) -> str:
    faq_items = "\n".join(f"<li>{html_escape(q)}</li>" for q in topic.faq)
    return dedent(f"""\
    <!doctype html>
    <html lang="en" dir="ltr">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <meta name="robots" content="noindex">
      <title>{html_escape(topic.title)} - LifeUSA Content Brief</title>
      <style>{CSS}</style>
    </head>
    <body>
    <main class="wrap">
      <header>
        <span class="eyebrow">Life for Relief and Development · Content Brief</span>
        <h1>{html_escape(topic.title)}</h1>
        <p>{html_escape(topic.subtitle)}</p>
        <div class="meta">
          <span>Version 1.0</span>
          <span>{DATE}</span>
          <span>Prepared by Saiaf Gamal</span>
          <span>{html_escape(owner_meta(topic))}</span>
        </div>
      </header>

      <nav>
        <a href="#setup">Setup</a>
        <a href="#audience">Audience</a>
        <a href="#keywords">Keywords</a>
        <a href="#serp">SERP</a>
        <a href="#format">Format</a>
        <a href="#journey">Journey</a>
        <a href="#intro">Intro</a>
        <a href="#links">Links</a>
        <a href="#outline">Sections</a>
        <a href="#faq">FAQ</a>
        <a href="#gain">Info Gain</a>
        <a href="#appendix">Appendix</a>
        <a href="#review">Review</a>
      </nav>

      <section id="setup">
        <h2>1. Article Setup</h2>
        <div class="grid">
          <div class="card"><h3>Working title</h3><p>{html_escape(topic.title)}</p></div>
          <div class="card"><h3>Content type</h3><p>{html_escape(topic.content_type)}</p></div>
          <div class="card"><h3>URL</h3><p><code>{html_escape(topic.live_url)}</code></p></div>
          <div class="card"><h3>Current rank</h3><p>{html_escape(tdata(topic, "current_rank"))}</p></div>
          <div class="card"><h3>Demand source</h3><p><code>{html_escape(KW_EXACT)}</code></p></div>
          <div class="card"><h3>Owner</h3><p>{html_escape(owner_card(topic))}</p></div>
        </div>
        <div class="callout ok"><strong>Status:</strong> {html_escape(topic.status_note)}</div>
      </section>

      <section id="audience">
        <h2>2. Audience And Reader Need</h2>
        <div class="grid">
          <div class="card"><h3>Audience</h3><p>{html_escape(tdata(topic, "audience"))}</p></div>
          <div class="card"><h3>Reader stage</h3><p>{html_escape(tdata(topic, "reader_stage"))}</p></div>
        </div>
        <p class="lede"><strong>Reader question:</strong> {html_escape(topic.reader_problem)}</p>
        <div class="callout danger"><strong>What would make them leave:</strong> {html_escape(tdata(topic, "trust_blockers"))}</div>
      </section>

      <section id="keywords">
        <h2>3. Keywords And Search Demand</h2>
        <p><strong>Google Ads CLI is the source of truth for search demand.</strong> Ahrefs may only be used later as a SERP-shape helper.</p>
        <h3>Primary Keywords</h3>
        <table><thead><tr><th>Keyword</th><th>Avg. monthly searches</th><th>Competition</th><th>Use</th></tr></thead><tbody>{rows_html(topic.primary_keywords)}</tbody></table>
        <h3>Secondary Keywords</h3>
        <table><thead><tr><th>Keyword</th><th>Avg. monthly searches</th><th>Competition</th><th>Use</th></tr></thead><tbody>{rows_html(topic.secondary_keywords)}</tbody></table>
      </section>

      <section id="serp">
        <h2>4. SERP And Competition</h2>
        <p class="lede"><strong>SERP means Search Engine Results Page.</strong> This snapshot explains what visible results suggest about reader expectations and article format.</p>
        <table><thead><tr><th>Visible source</th><th>What it shows</th></tr></thead><tbody>{source_links_html(tdata(topic, "serp_competitors"))}</tbody></table>
        <div class="grid">
          <div class="card"><h3>Search result features</h3><p>{html_escape(tdata(topic, "serp_features"))}</p></div>
          <div class="card"><h3>Paid ads</h3><p>{html_escape(tdata(topic, "paid_ads"))}</p></div>
          <div class="card"><h3>Content pattern</h3><p>{html_escape(tdata(topic, "content_pattern"))}</p></div>
          <div class="card"><h3>Writer takeaway</h3><p>{html_escape(tdata(topic, "serp_notes"))}</p></div>
        </div>
      </section>

      <section id="format">
        <h2>5. Format Decision</h2>
        <p><strong>Format decision:</strong> {html_escape(topic.format_decision)}</p>
        <h3>Article Thesis</h3>
        <p>{html_escape(deep(topic, "thesis"))}</p>
        <h3>Searcher Promise</h3>
        {bullets_html(deep(topic, "promise"))}
      </section>

      <section id="journey">
        <h2>6. Reader Profile And Journey</h2>
        <ul>
          <li><strong>Who they are:</strong> {html_escape(tdata(topic, "audience"))}</li>
          <li><strong>What they already believe:</strong> They care about orphaned children but need a clearer explanation of this specific topic.</li>
          <li><strong>What they need next:</strong> {html_escape(topic.reader_problem)}</li>
          <li><strong>What could block trust:</strong> {html_escape(tdata(topic, "trust_blockers"))}</li>
        </ul>
        <p><code>{html_escape(tdata(topic, "journey"))}</code></p>
        <div class="callout danger"><strong>Do not cannibalize:</strong> {html_escape(topic.cluster_boundary)}</div>
      </section>

      <section id="intro">
        <h2>7. Intro Guidance</h2>
        <p><strong>Guidance:</strong> {html_escape(topic.intro_guidance)}</p>
        <h3>Working Intro Draft</h3>
        {paragraphs_html(deep(topic, "intro"), "lede")}
      </section>

      <section id="outline">
        <h2>8. {html_escape(outline_heading(topic))}</h2>
        <h3>Section Depth Requirements</h3>
        {depth_plan_html(topic)}
        {sections_html(topic)}
      </section>

      <section id="links">
        <h2>9. Internal Links And Next Step</h2>
        <table><thead><tr><th>Page</th><th>Suggested anchor</th><th>Note</th></tr></thead><tbody>{links_html(topic.links)}</tbody></table>
      </section>

      <section id="faq">
        <h2>10. Metadata, FAQ, Images, And Schema</h2>
        <p><strong>Meta title:</strong> {html_escape(topic.meta_title)}</p>
        <p><strong>Meta description:</strong> {html_escape(topic.meta_description)}</p>
        <p><strong>Image notes:</strong> {html_escape(tdata(topic, "image_notes"))}</p>
        <p><strong>Schema notes:</strong> {html_escape(tdata(topic, "schema_notes"))}</p>
        <h3>FAQ Targets</h3>
        <ul>{faq_items}</ul>
      </section>

      <section id="gain">
        <h2>11. Information Gain</h2>
        <p>This is what LifeUSA can add beyond the search results instead of producing a rewritten version of competitor pages.</p>
        {bullets_html(tdata(topic, "info_gain"))}
      </section>

      <section id="appendix">
        <h2>12. Internal Appendix</h2>
        {bullets_html(tdata(topic, "appendix_sources"))}
      </section>

      <section id="review">
        <h2>Review Checklist Before Sending To Draft</h2>
        <ul>
          <li>Does the article have a clear job in the orphan cluster?</li>
          <li>Does the format fit the topic, not just the keyword?</li>
          <li>Does the intro answer the reader quickly?</li>
          <li>Does the SERP section explain what the writer should learn from competing pages?</li>
          <li>Does the article add LifeUSA-specific information gain?</li>
          <li>Does each section move the reader forward?</li>
          <li>Are LifeUSA examples specific and sourced?</li>
          <li>Are child, medical, crisis, sponsorship, zakat, or sadaqah claims safe to publish?</li>
          <li>Are internal links live and relevant?</li>
        </ul>
        <p><strong>Suggested slug:</strong> <code>{html_escape(topic.slug)}</code></p>
        <p><strong>Review note:</strong> {html_escape(topic.review_note)}</p>
        <div class="callout"><strong>Source note:</strong> {html_escape(topic.source_note)}</div>
      </section>
    </main>
    <footer>LifeUSA · {html_escape(topic.title)} · Content Brief and Outline · Version 1.0</footer>
    </body>
    </html>
    """)


def write(path: str, content: str) -> None:
    full = ROOT / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(content, encoding="utf-8")
    print(f"wrote {path}")


def build_source_notes() -> str:
    topic_rows = "\n".join(
        f"| {topic.title} | {topic.content_type} | {', '.join(f'`{kw}` {vol}/mo' for kw, vol, _, _ in topic.primary_keywords)} | {topic.live_url} |"
        for topic in TOPICS
    )
    return dedent(f"""\
    # Source Notes: Orphan Cluster Approved Four Outline Packages

    Date: 2026-07-05

    ## User Decision

    Saiaf approved four directions with clarifications:

    - `Gaza Orphans` and `Why Gifts for Orphans Matter` are existing article enrichment/rewrite plans. Rewrite means add depth, keyword targeting, structure, and links. It does not mean deleting the old article or forcing a new title. Saiaf owns these rewrites.
    - `Orphan Education After Loss` and `Mental Health Support for Orphaned Children` are new informational guides for Angela to draft. They do not have to replace existing recap posts.
    - Ownership split: rewrites are done by Saiaf; new guide drafts are done by Angela, with Saiaf handling SEO planning and review.

    ## Keyword Sources

    - `{KW_EXACT}`
    - `{KW_REWRITE}`
    - `{KW_EXPANDED}`
    - `Content Framework/80-Keywords/orphan-cluster-2026-07-05/orphan-basic-needs-gifts-expanded.json`

    Google Ads CLI is the demand source. Ahrefs is helper-only for SERP shape if needed later.

    ## Approved Packages

    | Package | Type | Primary demand | URL |
    |---|---|---|---|
    {topic_rows}

    ## Rejected Ideas

    - `Creating Beautiful Tomorrows in Orphans Today` as `What Orphan Relief Really Means`: rejected because it repeats the planned `How To Help Orphans` pillar's broad need categories.
    - Full rewrite of `Rebuilding After Loss`: rejected. Only internal-link improvement is allowed unless Saiaf later chooses a different angle.
    - Generic `orphanage donation`, `orphans charity`, and `orphan care` pages: rejected as repetitive unless a future preflight proves a distinct reader problem.
    """)


def main() -> None:
    write(
        "Content Framework/60-corpus/source-notes/orphan-cluster-four-outline-packages-2026-07-05.md",
        build_source_notes(),
    )
    for topic in TOPICS:
        write(f"Content Framework/70-outputs/briefs/orphans/{topic.slug}.md", build_brief(topic))
        write(f"Content Framework/70-outputs/outlines/orphans/{topic.slug}.md", build_outline(topic))
        write(f"Content Framework/70-outputs/handoff/orphans/{topic.slug}.html", build_html(topic))


if __name__ == "__main__":
    main()
