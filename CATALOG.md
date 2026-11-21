# Curated resource catalog

Checked: **2026-11-21**. “Read” means the public repository page or listed file was retrieved using TinyFish Fetch. It does not mean the software was installed, the demo was reproduced, or performance claims were verified. Recommendations below are editorial judgments based on the material read.

## Websites and visual design

| Resource | What you get | Use it when | Practical limit |
| --- | --- | --- | --- |
| [Anthropic frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md) | Guidance for deliberate visual direction, typography, and layout | Starting or redesigning a frontend | Still needs a concrete brief, relevant content, and visual inspection |
| [Impeccable](https://github.com/pbakaus/impeccable) | Design vocabulary, targeted refinements, critique and audit workflows | An existing interface needs a specific improvement | Review current live-mode behavior before enabling it; the README describes an Apply fallback that can launch a CLI with approvals and sandboxing disabled. Prefer ordinary critique/manual changes unless that behavior is understood |
| [UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Searchable design guidance, styles, palettes, and typography choices | Choosing an initial design direction | A suggested palette or style is not evidence of usability or accessibility |
| [Superdesign prompts](https://github.com/superdesigndev/superdesign-prompts) | Design specifications, interaction prompts, and previews | You want a visual starting point you can inspect before using | Author-reported rankings and usage are not independent quality benchmarks |
| [Awesome Claude Design](https://github.com/rohitg00/awesome-claude-design) | Design directions by aesthetic family and related references | Translating an aesthetic preference into usable instructions | Read as a discovery collection; its feature comparisons and launch commentary need separate verification |
| [design.skill](https://github.com/iamnigellee/design.skill) | A procedure for extracting design rules and reference boards | You have a permitted website or screenshot to study | Inferred rules may be wrong; verify against the reference and respect asset rights |
| [Google DESIGN.md](https://github.com/google-labs-code/design.md) | A format for visual identity, token values, and rationale | Keeping a visual system consistent between tasks | Merely placing a file in a folder does not ensure every client will load it |
| [Google Stitch Skills](https://github.com/google-labs-code/stitch-skills) | Design and build procedures for Stitch workflows | You already use Stitch and its integrations | Setup and tool availability are client-specific |
| [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills) | React performance and interface review procedures | Reviewing an app built with the relevant stack | Some guidance is React/Next.js or Vercel-specific |
| [Vercel Web Interface Guidelines](https://github.com/vercel-labs/web-interface-guidelines) | A reusable interface quality checklist | Checking keyboard access, forms, motion, and responsive behavior | A checklist complements browser and user testing |

**Suggested starter combination:** one annotated reference pack + your own design rules + one design procedure + a browser review. Do not paste ten overlapping skills into every task.

## Prompts, skills, and work procedures

| Resource | What you get | Use it when | Practical limit |
| --- | --- | --- | --- |
| [Anthropic Skills](https://github.com/anthropics/skills) | Official skill examples across design, development, documents, and communication | You need a repeatable procedure with supporting resources | Read the license and requirements for the particular skill; repository examples are not a guarantee of identical hosted behavior |
| [Fabric](https://github.com/danielmiessler/fabric) | Task-oriented reusable prompt patterns and a CLI framework | Summarizing material, extracting ideas, or standardizing repeated work | You can inspect patterns without installing the framework; CLI use requires setup |
| [prompts.chat](https://github.com/f/prompts.chat) | Broad searchable community prompt collection | Finding a first draft for a familiar task | Rewrite generic roles around your actual inputs, output, and success criteria |
| [Superpowers](https://github.com/obra/superpowers) | Structured development skills and workflows | Work benefits from explicit planning, debugging, and verification | Installation and workflow behavior vary by coding environment; disproportionate for tiny edits |
| [travisvn / Awesome Claude Skills](https://github.com/travisvn/awesome-claude-skills) | A skills discovery index | Exploring possible procedures | An index entry is not a code or security audit |
| [Composio / Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills) | A large skills/plugins collection and app-integration material | Exploring work automation possibilities | App integrations can require accounts and permissions; none were connected for this collection |

## Artifacts and learning

| Resource | What you get | Use it when | Practical limit |
| --- | --- | --- | --- |
| [Awesome Claude Artifacts](https://github.com/madewithclaude/awesome-claude-artifacts) | An early collection and contribution guide for artifacts | Looking for artifact formats and ideas | The fetched page is sparse and historically framed; use as inspiration, not a comprehensive current gallery |
| [Anthropic Prompt Engineering Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Exercises covering clarity, examples, output formatting, and related techniques | Learning why a prompt succeeds or fails | Its model examples are historical; use current model documentation for current behavior |
| [Anthropic Courses](https://github.com/anthropics/courses) | Historical material on prompting, evaluation, and tools | Studying examples and evaluation ideas | GitHub marked this repository archived on 2026-09-15 when fetched; do not treat its setup as current |

## What to collect next

Contribute worked examples with a public or synthetic input, an exact prompt, a usable output, and a check of that output. Reference libraries for motion, components, slides, spreadsheets, and research belong here when there is a clear task they improve. See [CONTRIBUTING.md](CONTRIBUTING.md).

Avoid collecting supposed secret phrases, leaked system prompts, unverified “100x” claims, or giant lists with no explanation of how to use the entries.
