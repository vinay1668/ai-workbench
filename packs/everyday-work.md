# Everyday work pack

**Use when:** writing, organizing notes, preparing a deliverable, or simplifying repeated work.

## 1. Produce a document from notes and an example

```text
Create [deliverable] for [audience and decision].
Use the attached notes as the factual source.
Use the example only for [structure / tone / level of detail].
Do not copy private names or facts from the example into the output.
Required content: [list]. Length and format: [constraints].

Separate supported facts from proposals. Mark missing facts as
[NEEDS INPUT] rather than inventing them. Lead with what the reader
needs to understand or decide. Remove repeated points and filler.
If creating a formatted file, inspect its rendered output if tools allow.
```

## 2. Turn messy notes into an action plan

```text
Turn these notes into a practical action plan: [notes].
Separate decisions already made, unresolved questions, and actions.
For each action include outcome, owner if explicitly known,
dependencies, and due date if explicitly supplied.
Do not assign people, dates, or commitments without evidence.
Flag contradictions and the one question that most blocks progress.
```

## 3. Find a sensible automation

```text
This task repeats: [steps, inputs, outputs, frequency].
Find the smallest useful way to reduce manual work.
Compare a reusable prompt, a template, a small script/tool,
and a connected workflow only where each is realistic.
Estimate setup effort and identify what still needs human judgment.
Recommend one approach and produce a reusable first version.
Use synthetic sample inputs. Do not connect accounts, send messages,
or schedule anything unless that action is explicitly authorized.
```

## 4. Use examples to fix tone

```text
Here are two examples of the writing I want: [examples].
Extract their reusable qualities: sentence length, structure, specificity,
and tone. Apply those qualities to this draft: [draft].
Preserve factual meaning and required caveats. Do not imitate personal
details or introduce unsupported claims. Return the edited draft and
a brief description of the most consequential edits.
```

**Check:** facts match the sources; names and dates are supported; the reader can act on the result; the output format is usable.

**Explore:** [Fabric](https://github.com/danielmiessler/fabric) for task patterns and [Anthropic Skills](https://github.com/anthropics/skills) for document procedures. The prompts here are original.
