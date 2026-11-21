# App pack

**Use when:** turning an idea into a working feature or small application.

**Attach:** a user journey, synthetic sample data, existing code conventions, and observable acceptance criteria.

## 1. Make the idea implementable

```text
Turn this idea into the smallest useful app: [idea].
User: [person]. Their main job: [job].
Available stack and integrations: [details].

Write a short implementation brief with:
- the primary end-to-end user journey;
- screens, data model, and state transitions;
- the smallest useful scope and explicit exclusions;
- decisions about persistence, authentication, and demo data;
- five observable acceptance criteria;
- the unknown most likely to change the design.

Ask about a blocking unknown; use stated assumptions for the rest.
Do not invent an external integration or claim a mock is connected.
```

## 2. Build a complete small journey

```text
Implement [one user journey] from the attached brief.
First inspect the relevant project instructions and existing code.
Use the established stack and reusable components.

Include loading, empty, success, and error behavior where relevant.
Use only synthetic example data. Keep secrets out of source and logs.
Validate inputs and define what happens after refresh or navigation.
Run the checks appropriate to this behavior. Test the main journey
in a browser if one is available. Fix failures before reporting completion.

Report the files changed, checks actually run, and material limitations.
```

## 3. Catch the fake-complete app

```text
Audit the app as a user trying to [main goal].
Trace every step from entry to saved or completed result.
Identify dead controls, mock-only flows, missing persistence,
invalid input handling, and states the user cannot recover from.
Rank findings by how much they block the main goal.
Fix the highest-impact issues in scope and verify the journey again.
Separate observed failures from untested concerns.
```

**Synthetic example:** a reading tracker where a user adds a book, changes its status, refreshes, and still sees the saved status. A polished card grid alone does not satisfy that journey.

**Sources to explore:** [Superpowers](https://github.com/obra/superpowers), [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills). Use only the parts proportionate to the task.
