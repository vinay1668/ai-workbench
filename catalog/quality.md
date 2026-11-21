# Testing, evaluation & observability

[← All categories](../CATALOG.md) · [Starter recipes](../guides/starter-recipes.md) · 8 resources

Checked **2026-11-21**. Source-checked, not runtime-tested. Setup, access, and pricing can change; follow the owning source.

## Resources

| Resource | Use it for | Setup | Before choosing |
| --- | --- | --- | --- |
| [Promptfoo](https://github.com/promptfoo/promptfoo)<br>Evaluation | Compare prompts and model behavior with repeatable cases. | Node and configured providers. | Use representative, sanitized evaluation inputs. |
| [DeepEval](https://github.com/confident-ai/deepeval)<br>Evaluation | Test LLM application outputs against chosen criteria. | Python; models/services depend on metrics. | Model-scored metrics are estimates, not ground truth. |
| [Ragas](https://github.com/vibrantlabsai/ragas)<br>Evaluation | Evaluate retrieval and language-model workflows. | Python and evaluation data. | Metric definitions and judge models influence scores. |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix)<br>Observability | Inspect and evaluate AI application traces. | Python/server setup. | Traces can capture sensitive prompts and outputs. |
| [Langfuse](https://github.com/langfuse/langfuse)<br>Observability | Trace and evaluate AI application behavior. | Hosted or self-hosted setup. | Control what data is captured and retained. |
| [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai)<br>Evaluation | Build structured model evaluation tasks. | Python and model setup. | Use current project documentation after redirects. |
| [Playwright](https://github.com/microsoft/playwright)<br>Testing | Exercise a generated app in a real browser. | Node and browser installation. | Test meaningful user journeys, not just page existence. |
| [Vitest](https://github.com/vitest-dev/vitest)<br>Testing | Run focused JavaScript and TypeScript tests. | Node and project setup. | Passing unit tests do not prove the whole app works. |

## Put one resource to work

1. Pick one entry whose purpose matches the task.
2. Read the owning source and confirm requirements for your client.
3. Supply a small, permitted input or synthetic example.
4. Define the output and check the result before expanding scope.

Use a [reference pack](../templates/reference-pack.md) for context. For connections, read [choosing an MCP server](../guides/choosing-mcp.md).
