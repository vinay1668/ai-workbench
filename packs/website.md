# Website pack

**Use when:** building a landing page, portfolio, content site, or a visual redesign.

**Attach:** a filled [product brief](../templates/product-brief.md), one or two annotated screenshots, a [reference pack](../templates/reference-pack.md), and existing components if applicable. Use assets you have permission to use. A screenshot without an explanation leaves the agent guessing which details matter.

## 1. Translate references into design decisions

```text
Study the attached references for [product and audience].
Reference A: borrow [type hierarchy and generous spacing].
Reference B: borrow [navigation density and interaction feedback].
Do not copy their logos, brand names, copy, or distinctive artwork.

Propose two different visual directions that fit our subject matter.
For each, specify type choices, color roles, spacing, page structure,
one signature detail, and why it helps the user's main task.
Recommend one direction. Do not write implementation code yet.
Label anything inferred from a screenshot as an inference.
```

## 2. Build from a chosen direction

```text
Build [page] using direction [name] and the attached design rules.
Audience: [specific people]. Main action: [specific action].
Required sections and real content: [list]. Stack: [existing stack].

Use the project's existing components and conventions where applicable.
Deliver the actual implementation and any new asset attribution.
Every visible control must have defined behavior. For integrations
outside scope, show an explicit demo state and explain the boundary.
Include mobile navigation, clear focus states, useful empty/error states,
and reduced-motion behavior. Avoid fabricated customer quotes or metrics.

If browser tools are available, inspect at 390px and 1440px widths,
test the main action and keyboard navigation, and fix visible defects.
Otherwise say that visual verification is pending.
```

## 3. Improve one weak section

```text
Review this [hero / pricing section / navigation] against the attached brief.
Identify the three most consequential problems with hierarchy, clarity,
spacing, contrast, or interaction. Explain each with a visible example.
Implement the fixes while preserving the chosen design direction.
Show what changed and how you checked it. Do not redesign unrelated sections.
```

**Check:** main message is understandable in a glance; primary action works; small screens do not overflow; keyboard focus is visible; actual content fits; assets and claims are legitimate.

**Good starting sources:** [Anthropic frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md), [Superdesign prompts](https://github.com/superdesigndev/superdesign-prompts), [Vercel guidelines](https://github.com/vercel-labs/web-interface-guidelines). These prompts are original recipes, not copied upstream instructions.
