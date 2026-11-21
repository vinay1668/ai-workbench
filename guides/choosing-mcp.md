# Choose an MCP server for the task

Start from the [official registry](https://registry.modelcontextprotocol.io/), the [MCP categories](../CATALOG.md), or the actual service provider's documentation. A registry listing or a community “awesome” entry is a discovery aid, not a guarantee of safety or quality. The [reference servers](https://github.com/modelcontextprotocol/servers) explicitly describe themselves as educational implementations.

## Decide what access is actually needed

| Task | Useful connection | Start with |
| --- | --- | --- |
| Fix outdated library usage | Documentation retrieval | [Context7](https://github.com/upstash/context7) or the library's own docs |
| Inspect a broken user flow | Browser tools | [Playwright MCP](https://github.com/microsoft/playwright-mcp), [Playwright CLI](https://github.com/microsoft/playwright-cli), or [Chrome DevTools](https://github.com/ChromeDevTools/chrome-devtools-mcp) |
| Work on GitHub issues | Repository tools | [GitHub MCP Server](https://github.com/github/github-mcp-server) with appropriate scopes |
| Investigate development data | Database tools | The provider-specific server for your development project |
| Use design files | Design context | [Figma's owning documentation](https://developers.figma.com/docs/figma-mcp-server/) |
| Retrieve work notes | Workspace search | [Notion hosted MCP](https://developers.notion.com/guides/mcp/overview) or your service's own integration |
| Create an interactive chat tool | MCP app tooling | [MCP Apps](https://github.com/modelcontextprotocol/ext-apps) and a compatible host |

The Playwright project offers both MCP and CLI paths. Choose according to your host and task; do not assume every integration requires MCP.

## Before connecting

- Confirm who maintains the implementation and whether it is still supported.
- Check your client's supported transport, authentication and runtime requirements.
- Read what tools can read, write, execute, publish or delete.
- Prefer a test project and the smallest useful permissions. Use read-only access when it satisfies the task.
- Keep credentials in the client's supported secret mechanism. Never commit live config, tokens, cookies or account exports to this public collection.
- Understand billing and what data leaves your machine before running a connected workflow.

## Try one bounded task

```text
Using [chosen connection], inspect [specific permitted source].
Answer [question] with direct evidence. Do not modify external state.
If access or a required tool is unavailable, report the missing capability.
```

For a write task, explicitly name the destination and intended change. Review the result with the owning service. Treat instructions found inside retrieved pages and documents as source content rather than authority to change the task.

This repository provides discovery links and original guidance. It does not ship live MCP configurations, install servers automatically, or connect any accounts.
