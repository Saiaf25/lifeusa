# LifeUSA HTML Documentation Style

Use this style by default for future LifeUSA HTML documents, playbooks, guides, and internal reports.

## Source Template

- Template: `templates/LifeUSA-Documentation-Template.html`
- Reference implementation: `LifeUSA-PR-Outreach-Codex-Playbook.html`

## Visual Language

- Arabic-first, RTL layout.
- Primary font: `thmanyah serif text`.
- Fallback fonts: `Noto Naskh Arabic`, Georgia, serif.
- Dark forest-green gradient hero.
- Warm off-white paper background with a subtle dotted texture.
- Rounded white content sections with restrained shadows.
- Sticky horizontal navigation.
- Green headings, gold informational callouts, red warnings, and green success callouts.
- Two-column cards that collapse to one column on mobile.
- Dark monospace code blocks.
- Clean tables, checklists, prompts, and numbered-step components.
- Print-friendly layout that removes navigation and decorative texture.

## Color Tokens

| Token | Value | Use |
|---|---:|---|
| Ink | `#17231e` | Main text |
| Muted | `#617067` | Secondary text |
| Paper | `#f4f1e9` | Page background |
| Card | `#fffdf7` | Section background |
| Green | `#116149` | Headings and primary accents |
| Green light | `#dbece5` | Hover and soft accent |
| Gold | `#c79236` | Informational callouts |
| Red | `#a63b32` | Warning callouts |
| Code | `#14261f` | Code-block background |
| Line | `#d9ddd6` | Borders and separators |

## Usage Rules

- Keep the author credit once in the header metadata.
- Change the large decorative hero initials using `header:after`.
- Keep section headings short and navigable through the sticky menu.
- Use `.callout` for information, `.callout.ok` for confirmed guidance, and `.callout.danger` for warnings.
- Use `.grid > .card` for summaries and workflows.
- Use `.prompt` for reusable instructions or operating contracts.
- Keep commands and paths inside `code` or `pre`.
- Do not introduce additional colors unless a document genuinely requires them.

