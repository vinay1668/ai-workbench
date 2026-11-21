# Review and debugging pack

**Use when:** an output looks plausible but fails to meet the actual need.

## 1. Debug from evidence

```text
Expected behavior: [specific result].
Observed behavior: [specific failure].
Reproduction steps and relevant errors: [sanitized evidence].
Relevant files and recent changes: [context].

Investigate the cause before changing code. State a testable hypothesis,
inspect the relevant path, and make the smallest complete fix.
Verify the original failure and a nearby edge case.
Report the cause, fix, checks actually run, and remaining uncertainty.
Do not claim a test passed unless you ran it and observed its result.
```

## 2. Review a draft against a rubric

```text
Review this [deliverable] for [audience and purpose].
Rubric: correctness, completeness, clarity, usability, and [task criterion].
For each important finding, cite a concrete part of the output,
explain the consequence, and propose a specific correction.
Separate observed problems from preference-based suggestions.
Revise the output to resolve the highest-impact findings in scope.
```

## 3. Rescue a bloated conversation

```text
Create a compact handoff containing the objective, decisions,
constraints, relevant files/sources, current state, verified results,
failed attempts that still matter, and the next concrete action.
Exclude credentials, private personal details, and irrelevant history.
Preserve unresolved uncertainties. Do not convert plans into completed work.
```

**Check:** the original failure is resolved; the main objective still holds; evidence matches the completion claim. A model reviewing its own work is useful but is not independent verification.
