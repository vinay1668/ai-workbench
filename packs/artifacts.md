# Artifact pack

**Use when:** a small interactive output would be more useful than another prose answer.

An artifact can be a calculator, decision matrix, diagram, explorable explanation, report, checklist, or prototype. Preview and execution support vary by assistant; a standalone HTML file is a portable deliverable for many small interactive tools.

## 1. Turn a repetitive calculation into a tool

```text
Create a standalone HTML calculator for [task].
Inputs: [names, units, ranges, defaults].
Formula and assumptions: [explicit rules].
Expected examples: [input → output, including an edge case].

Use inline CSS and JavaScript, semantic labels, visible focus states,
and responsive layout. Keep it usable without external dependencies.
Validate inputs, explain units, and handle zero or missing values.
Show the formula and assumptions beside the result.
Use only synthetic defaults. Make no network requests and include
no analytics, credentials, or persistence unless explicitly requested.
Deliver the complete HTML file. Check the example calculations.
```

**Invented example:** weekly study planner. Inputs: hours available and subject weights. Output: hours per subject. Reject negative hours and handle a zero total weight explicitly.

## 2. Compare options interactively

```text
Build a decision matrix for these synthetic options: [options].
Criteria: [criteria]. Each score is between 1 and 5; higher is better.
Weights are nonnegative and may be edited. Rank by
sum(weight × score) / sum(weights). If all weights are zero,
show an explanation instead of a ranking. Explain ties.

Show the input table, editable weights, ranked results, and assumptions.
Make it clear that scores are user judgments, not objective facts.
Provide a reset button and a responsive keyboard-accessible interface.
Deliver one standalone HTML file without network requests.
Verify at least two example rankings, a tie, and the all-zero case.
```

## 3. Explain something with controls

```text
Explain [concept] to [audience] through an interactive artifact.
Let the reader change [two meaningful variables] and observe [outcome].
Include a default worked example, units, accessible descriptions,
and a short explanation of what the model simplifies or excludes.
Use the supplied facts; distinguish assumptions from established facts.
Deliver the artifact and verify that controls change the displayed result.
```

**Check:** the output opens; controls work; formulas match worked examples; invalid inputs are understandable; assumptions are visible; synthetic content stays synthetic.

**Explore:** [Awesome Claude Artifacts](https://github.com/madewithclaude/awesome-claude-artifacts) for historical inspiration. The recipes above are original and independent of that collection.
