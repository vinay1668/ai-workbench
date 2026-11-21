# Eight starter recipes

Each recipe is a suggested starting combination, not an integration tested by this repository. Follow current upstream setup for your client. Use public or synthetic inputs for experimentation.

## 1. Build a distinctive website

**Pick:** [frontend-design](https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md), one [Superdesign specification](https://github.com/superdesigndev/superdesign-prompts), and the [website pack](../packs/website.md).

**Attach:** product brief, one annotated reference, actual page content, and design rules.

**Ask:** “Build this page for this audience. Borrow the reference's typography and spacing; use our own identity. Implement the main action and inspect the small-screen result.”

**Check:** primary action, small-screen overflow, keyboard focus, real content fit.

## 2. Debug a frontend with evidence

**Pick:** [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp) or [Playwright CLI](https://github.com/microsoft/playwright-cli), plus the [review pack](../packs/review.md).

**Attach:** reproduction steps, expected behavior, relevant files and sanitized errors.

**Ask:** “Reproduce this failure, inspect the relevant browser and source evidence, fix the cause, then repeat the failing journey.”

**Check:** the original reproduction and one nearby edge case.

## 3. Implement against the right library version

**Pick:** [Context7](https://github.com/upstash/context7) or primary library docs, plus project instructions.

**Attach:** installed library version, current implementation and required behavior.

**Ask:** “Find documentation matching this version. Implement this behavior using supported APIs, then run the relevant project checks.”

**Check:** actual package version, supported methods, runtime result.

## 4. Build a small app with a real data journey

**Pick:** the [app pack](../packs/app.md), your existing framework, and a development-only database connection if required.

**Attach:** schema, synthetic records, persistence expectations and acceptance criteria.

**Ask:** “Implement add, edit, refresh and recovery for this one journey. Keep demo integrations visibly labeled.”

**Check:** saved state survives refresh; invalid inputs and errors are recoverable.

## 5. Turn a calculation into an interactive artifact

**Pick:** the [artifact pack](../packs/artifacts.md), [Streamlit](https://github.com/streamlit/streamlit), [Marimo](https://github.com/marimo-team/marimo), or standalone HTML.

**Attach:** inputs, units, formula, two worked examples and an edge case.

**Ask:** “Build an editable calculator, show its assumptions and formula, and verify the supplied examples.”

**Check:** calculations, zero values, invalid input, reset behavior.

## 6. Produce a document or presentation

**Pick:** the relevant [DOCX](https://github.com/anthropics/skills/tree/main/skills/docx), [PDF](https://github.com/anthropics/skills/tree/main/skills/pdf), or [PPTX](https://github.com/anthropics/skills/tree/main/skills/pptx) procedure; use [Slidev](https://github.com/slidevjs/slidev) for a developer-oriented Markdown deck.

**Attach:** sanitized source notes, audience, length, output format and permitted style example.

**Ask:** “Create the actual deliverable. Preserve the source facts, mark missing facts, render it, and inspect for layout defects.”

**Check:** facts, pagination, overflow, readability, usable export.

## 7. Add evidence to an AI application

**Pick:** one application framework from the [directory](../catalog/frameworks.md), plus [Promptfoo](https://github.com/promptfoo/promptfoo) or another relevant evaluation tool.

**Attach:** representative sanitized inputs, expected behavior and failure cases.

**Ask:** “Implement the feature and evaluate it against these cases. Separate schema correctness, factual correctness and task completion.”

**Check:** regressions, actual completion, trace contents and observable costs.

## 8. Research and save reusable lessons

**Pick:** the [research pack](../packs/research.md), [TinyFish documentation](https://docs.tinyfish.ai/), or one search connection from the [web/work category](../catalog/mcpwork.md).

**Attach:** decision, constraints, time frame and a source/output example.

**Ask:** “Search, read the owning sources, compare realistic options, and save a concise reusable recipe with direct evidence links.”

**Check:** source supports each claim, dates are clear, uncertainty stays visible. Save the generalized recipe rather than private source material.
