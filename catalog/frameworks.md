# Build AI applications

[← All categories](../CATALOG.md) · [Starter recipes](../guides/starter-recipes.md) · 12 resources

Checked **2026-11-21**. Source-checked, not runtime-tested. Setup, access, and pricing can change; follow the owning source.

## Resources

| Resource | Use it for | Setup | Before choosing |
| --- | --- | --- | --- |
| [Vercel AI SDK](https://github.com/vercel/ai)<br>SDK | Build AI application interfaces and tool workflows. | JavaScript/TypeScript and provider setup. | Provider billing and capabilities vary. |
| [LangGraph](https://github.com/langchain-ai/langgraph)<br>Framework | Build stateful agent workflows. | Python/JS ecosystem and model setup. | Add orchestration only when the workflow needs it. |
| [LangChain](https://github.com/langchain-ai/langchain)<br>Framework | Compose model, retrieval and tool integrations. | Python and provider setup. | APIs and integration packages change over time. |
| [LlamaIndex](https://github.com/run-llama/llama_index)<br>Framework | Explore document parsing, extraction and data-oriented AI tooling. | Python and data/model setup. | The current repository emphasizes document processing; check the specific retrieval package you need. |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai)<br>Framework | Build typed Python agent applications. | Python and model setup. | Schema validity does not prove factual correctness. |
| [DSPy](https://github.com/stanfordnlp/dspy)<br>Framework | Program and optimize language-model pipelines. | Python, examples and model access. | Optimization quality depends on evaluation data. |
| [CrewAI](https://github.com/crewAIInc/crewAI)<br>Framework | Prototype role-based agent workflows. | Python and provider setup. | Keep task boundaries and completion checks explicit. |
| [Mastra](https://github.com/mastra-ai/mastra)<br>Framework | Build TypeScript agents and workflows. | Node/TypeScript and provider setup. | Check deployment and persistence requirements. |
| [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)<br>Framework | Explore Microsoft's successor framework for agent applications. | Supported runtime and provider setup. | Check migration guidance when moving from older Microsoft frameworks. |
| [n8n](https://github.com/n8n-io/n8n)<br>Automation | Connect AI steps to event-driven workflows. | Hosted or self-hosted setup and integrations. | Review its license and confirm external writes before executing. |

## Historical or superseded — read before choosing

| Resource | Use it for | Setup | Before choosing |
| --- | --- | --- | --- |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel)<br>SDK · **superseded** | Integrate AI orchestration into applications. | Supported language runtime and provider. | Upstream directs new work toward Microsoft Agent Framework; check the migration guide. |
| [AutoGen](https://github.com/microsoft/autogen)<br>Framework · **historical** | Explore agent collaboration and conversation patterns. | Python and provider setup. | Archived upstream on 2026-11-20. For new work, evaluate Microsoft Agent Framework instead. |

## Put one resource to work

1. Pick one entry whose purpose matches the task.
2. Read the owning source and confirm requirements for your client.
3. Supply a small, permitted input or synthetic example.
4. Define the output and check the result before expanding scope.

Use a [reference pack](../templates/reference-pack.md) for context. For connections, read [choosing an MCP server](../guides/choosing-mcp.md).
