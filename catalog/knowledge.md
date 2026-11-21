# Knowledge, RAG & local AI

[← All categories](../CATALOG.md) · [Starter recipes](../guides/starter-recipes.md) · 8 resources

Checked **2026-11-21**. Source-checked, not runtime-tested. Setup, access, and pricing can change; follow the owning source.

## Resources

| Resource | Use it for | Setup | Before choosing |
| --- | --- | --- | --- |
| [Ollama](https://github.com/ollama/ollama)<br>Local runtime | Run supported models locally. | Compatible hardware and model downloads. | Local inference does not make every connected tool private. |
| [llama.cpp](https://github.com/ggml-org/llama.cpp)<br>Local runtime | Run supported language models with local inference tooling. | Build/runtime and suitable model files. | Hardware, quantization and licenses affect suitability. |
| [Open WebUI](https://github.com/open-webui/open-webui)<br>Workbench | Use a web interface for AI models and related workflows. | Local/server deployment and model backend. | Review network, account and data settings. |
| [AnythingLLM](https://github.com/Mintplex-Labs/anything-llm)<br>Workbench | Explore document-oriented AI workflows. | Desktop/server and model setup. | Validate retrieval quality on your own documents. |
| [Dify](https://github.com/langgenius/dify)<br>Workbench | Build AI applications with visual workflow tooling. | Hosted or self-hosted setup. | Review licensing, hosting and provider costs. |
| [Haystack](https://github.com/deepset-ai/haystack)<br>Framework | Build retrieval and document-processing pipelines. | Python and data/model setup. | Evaluate retrieval and answers separately. |
| [Langflow](https://github.com/langflow-ai/langflow)<br>Workbench | Explore visual AI application and agent flows. | Local/server runtime and provider setup. | Review access control before deploying. |

## Historical or superseded — read before choosing

| Resource | Use it for | Setup | Before choosing |
| --- | --- | --- | --- |
| [Flowise](https://github.com/FlowiseAI/Flowise)<br>Workbench · **historical** | Prototype AI flows visually. | Node/server and provider setup. | Archived upstream on 2026-08-13. Historical reference; evaluate current alternatives such as Langflow. |

## Put one resource to work

1. Pick one entry whose purpose matches the task.
2. Read the owning source and confirm requirements for your client.
3. Supply a small, permitted input or synthetic example.
4. Define the output and check the result before expanding scope.

Use a [reference pack](../templates/reference-pack.md) for context. For connections, read [choosing an MCP server](../guides/choosing-mcp.md).
