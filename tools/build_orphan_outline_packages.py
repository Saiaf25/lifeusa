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


def outline_sections_md(topic: Topic) -> str:
    out: list[str] = []
    for idx, section in enumerate(topic.sections, 1):
        out.append(f"## H2 {idx}: {section.title}\n")
        out.append(f"Why this section is here:\n\n{section.why}\n")
        out.append(f"Reader stage:\n\n{section.stage}\n")
        out.append(f"Keyword ownership:\n\n{section.keywords}\n")
        out.append(f"What Saiaf should write:\n\n{section.write}\n")
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

    ## Article Setup

    - **Content type:** {topic.content_type}
    - **Owner:** Saiaf
    - **Proposed/live URL:** `{topic.live_url}`
    - **Status note:** {topic.status_note}
    - **Keyword source:** `{KW_EXACT}` and `{KW_REWRITE}`. Google Ads CLI is the demand source; Ahrefs is helper-only if used later for SERP shape.

    ## Reader Problem

    {topic.reader_problem}

    ## Cluster Boundary

    {topic.cluster_boundary}

    ## Primary Keywords

    {md_table(topic.primary_keywords)}

    ## Secondary Keywords

    {md_table(topic.secondary_keywords)}

    ## Format Decision

    {topic.format_decision}

    ## Intro Guidance

    {topic.intro_guidance}

    ## Internal Links And Proof Examples

    {link_table(topic.links)}

    ## Metadata

    - **Meta title:** {topic.meta_title}
    - **Meta description:** {topic.meta_description}

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

    ## Reader Journey

    ```text
    The reader has a specific orphan-related question -> they need a focused answer, not the broad orphan pillar -> they see LifeUSA proof examples -> they understand the right next step -> they can support through the relevant LifeUSA article, campaign, or donation path.
    ```

    ## Search Demand

    Primary keywords:

    {md_table(topic.primary_keywords)}

    Secondary keywords:

    {md_table(topic.secondary_keywords)}

    ## Non-Cannibalization Rule

    {topic.cluster_boundary}

    ## Intro

    {topic.intro_guidance}

    {outline_sections_md(topic)}

    ## FAQ Targets

    {faqs}

    ## Internal Links

    {link_table(topic.links)}

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
          <p><strong>Write:</strong> {html_escape(section.write)}</p>
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
        <a href="#keywords">Keywords</a>
        <a href="#intent">Intent</a>
        <a href="#links">Links</a>
        <a href="#outline">Outline</a>
        <a href="#faq">FAQ</a>
        <a href="#review">Review</a>
      </nav>

      <section id="setup">
        <h2>Article Setup</h2>
        <div class="grid">
          <div class="card"><h3>Content type</h3><p>{html_escape(topic.content_type)}</p></div>
          <div class="card"><h3>URL</h3><p><code>{html_escape(topic.live_url)}</code></p></div>
          <div class="card"><h3>Demand source</h3><p><code>{html_escape(KW_EXACT)}</code></p></div>
          <div class="card"><h3>Owner</h3><p>{html_escape(owner_card(topic))}</p></div>
        </div>
        <div class="callout ok"><strong>Status:</strong> {html_escape(topic.status_note)}</div>
      </section>

      <section id="keywords">
        <h2>Keywords And Search Demand</h2>
        <p><strong>Google Ads CLI is the source of truth for search demand.</strong> Ahrefs may only be used later as a SERP-shape helper.</p>
        <h3>Primary Keywords</h3>
        <table><thead><tr><th>Keyword</th><th>Avg. monthly searches</th><th>Competition</th><th>Use</th></tr></thead><tbody>{rows_html(topic.primary_keywords)}</tbody></table>
        <h3>Secondary Keywords</h3>
        <table><thead><tr><th>Keyword</th><th>Avg. monthly searches</th><th>Competition</th><th>Use</th></tr></thead><tbody>{rows_html(topic.secondary_keywords)}</tbody></table>
      </section>

      <section id="intent">
        <h2>Intent And Boundary</h2>
        <p class="lede">{html_escape(topic.reader_problem)}</p>
        <div class="callout danger"><strong>Do not cannibalize:</strong> {html_escape(topic.cluster_boundary)}</div>
        <p><strong>Format decision:</strong> {html_escape(topic.format_decision)}</p>
        <p><strong>Intro guidance:</strong> {html_escape(topic.intro_guidance)}</p>
      </section>

      <section id="links">
        <h2>Internal Links And Proof Examples</h2>
        <table><thead><tr><th>Page</th><th>Suggested anchor</th><th>Note</th></tr></thead><tbody>{links_html(topic.links)}</tbody></table>
      </section>

      <section id="outline">
        <h2>Writer Outline For Saiaf</h2>
        {sections_html(topic)}
      </section>

      <section id="faq">
        <h2>FAQ Targets</h2>
        <ul>{faq_items}</ul>
      </section>

      <section id="review">
        <h2>Metadata And Review Checklist</h2>
        <p><strong>Meta title:</strong> {html_escape(topic.meta_title)}</p>
        <p><strong>Meta description:</strong> {html_escape(topic.meta_description)}</p>
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
