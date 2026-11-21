# AI Workbench

Reusable prompts, reference packs, artifact recipes, and workflows for getting better work out of AI.

For people building apps and websites, researching a decision, writing a document, or turning a repetitive task into a small tool. Start with a task, add a useful reference, and define how you will judge the result.

**“100x” is an ambition, not a measured claim.** This collection is about reducing avoidable rework. External resources were checked on **2026-11-21** through TinyFish Search and Fetch; their software was not installed or benchmarked.

## Start here

| I want to… | Open this | Send along with the prompt |
| --- | --- | --- |
| Build a distinctive website | [Website pack](packs/website.md) | Product brief, annotated screenshots, design rules |
| Build an app that works | [App pack](packs/app.md) | User journey, sample data, acceptance criteria |
| Turn a task into an interactive artifact | [Artifact pack](packs/artifacts.md) | Inputs, calculation rules, example outputs |
| Research a decision | [Research pack](packs/research.md) | Decision, constraints, source requirements |
| Finish documents and everyday work | [Work pack](packs/everyday-work.md) | Audience, source notes, output example |
| Fix or improve an existing result | [Review pack](packs/review.md) | Current result, failure evidence, target behavior |
| Find existing libraries | [Curated catalog](CATALOG.md) | Choose one relevant resource first |

## The practical recipe

1. **Brief:** explain who the work serves and what success looks like.
2. **Context:** attach only the relevant facts and files.
3. **Reference:** show a good example and explain what to borrow from it.
4. **Constraints:** state the tools, scope, and boundaries.
5. **Output:** name the actual deliverable, including format.
6. **Check:** provide examples, tests, or a review rubric.

Copy this and replace the bracketed fields:

```text
Create [deliverable] for [audience] so they can [specific outcome].

Context: [facts, current state, relevant source files].
References: [attachments or accessible URLs]. Borrow [specific qualities].
Do not copy [brand identity, text, layout, or other unwanted qualities].

Constraints: [stack, scope, deadline, available tools].
Deliver: [files / working artifact / report / table].
Success means: [3–5 observable criteria].

Ask about missing information only when it changes the result materially.
Otherwise state assumptions and proceed. Verify the result using the
available tools, and distinguish verified results from untested claims.
```

## What are these things?

| Term | Practical meaning | Example |
| --- | --- | --- |
| Prompt | Instructions for the current task | “Build this onboarding flow” |
| Few-shot examples | Examples of the output you want | Two good support replies and one counterexample |
| Reference pack | Relevant material supplied with the task | Screenshots, notes, a schema, a style guide |
| Design rules | Reusable visual decisions | Color roles, spacing, type, component states |
| Project instructions | Persistent repository context for a coding agent | Build commands and architectural boundaries |
| Skill | A reusable task procedure, sometimes with scripts and assets | A document production or UI review procedure |
| Artifact | A usable output produced by AI | A calculator, diagram, report, prototype, or HTML tool |
| MCP/tool integration | Access to an external capability or source | Search, a browser, or a connected document system |

You can paste these prompts into a chat assistant. Files, browsing, execution, persistent instructions, and skill discovery depend on the particular app and configuration. A prompt cannot give a model tools it does not have. For skills, consult the upstream installation instructions for your actual client.

## Closest existing collections

- [Anthropic Skills](https://github.com/anthropics/skills): official examples of reusable task procedures, including frontend and document work.
- [Superdesign prompts](https://github.com/superdesigndev/superdesign-prompts): visual directions with design specifications and previews.
- [Awesome Claude Design](https://github.com/rohitg00/awesome-claude-design): aesthetic families, design references, and prompt packs.
- [Fabric](https://github.com/danielmiessler/fabric): reusable patterns organized around real work tasks.
- [prompts.chat](https://github.com/f/prompts.chat): a broad prompt collection, formerly Awesome ChatGPT Prompts.
- [Awesome Claude Skills](https://github.com/travisvn/awesome-claude-skills): a discovery index for skills and related resources.

This repository adds a common way to use those resources: **what to choose, what to attach, what to ask, and how to check the output.** See the [full catalog](CATALOG.md) for limitations and source links.

## Reusable materials

- [Reference pack template](templates/reference-pack.md)
- [Product brief template](templates/product-brief.md)
- [Design rules template](templates/design-rules.md)
- [Project instructions template](templates/project-instructions.md)
- [Build and review workflow](workflows/build-and-review.md)
- [Evaluate a prompt or skill](workflows/evaluate.md)
- [Source and research notes](SOURCES.md)
- [Contribution rules](CONTRIBUTING.md)

All examples use invented data. This repository contains original text and public source links; it does not bundle downloaded third-party skills, screenshots, private files, or credentials. Upstream resources retain their own terms. Original material here is [MIT licensed](LICENSE).
