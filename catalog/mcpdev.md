# MCP · coding & browsers

[← All categories](../CATALOG.md) · [Starter recipes](../guides/starter-recipes.md) · 14 resources

Checked **2026-11-21**. Source-checked, not runtime-tested. Setup, access, and pricing can change; follow the owning source.

## Resources

| Resource | Use it for | Setup | Before choosing |
| --- | --- | --- | --- |
| [GitHub MCP Server](https://github.com/github/github-mcp-server)<br>MCP | Let an agent work with GitHub repository and collaboration tools. | GitHub account and scoped auth. | Review write permissions before enabling mutations. |
| [Playwright MCP](https://github.com/microsoft/playwright-mcp)<br>MCP | Inspect and interact with websites through a browser. | Node and browser; MCP client. | Browser access can expose session data; constrain the task. |
| [Chrome DevTools MCP](https://github.com/ChromeDevTools/chrome-devtools-mcp)<br>MCP | Give a coding agent browser debugging tools. | Node and Chrome; MCP client. | Use a dedicated development browser context. |
| [Context7](https://github.com/upstash/context7)<br>MCP | Retrieve library documentation for coding tasks. | MCP client; hosted/local setup varies. | Confirm library version and source applicability. |
| [GitMCP](https://github.com/idosal/git-mcp)<br>MCP | Expose repository documentation to an assistant. | MCP client; target repository. | Documentation retrieval does not execute or verify code. |
| [MCP Inspector](https://github.com/modelcontextprotocol/inspector)<br>Tool | Inspect and debug MCP servers during development. | Node; a server to inspect. | Developer diagnostic tool, not a trust certification. |
| [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)<br>SDK | Build an MCP client or server in TypeScript. | Node and TypeScript. | Follow current protocol and SDK documentation. |
| [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)<br>SDK | Build an MCP client or server in Python. | Python. | Runtime and transport requirements depend on the project. |
| [FastMCP](https://github.com/PrefectHQ/fastmcp)<br>Framework | Build Python MCP tools and servers. | Python. | Review authentication and deployment configuration. |
| [Filesystem reference server](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)<br>MCP | Study file-access tools with directory restrictions. | Node; explicitly permitted directories. | Reference implementation; never point it at unrelated personal folders. |
| [Git reference server](https://github.com/modelcontextprotocol/servers/tree/main/src/git)<br>MCP | Study repository inspection and manipulation tools. | Python and Git; a chosen repository. | Review operations that can modify repository state. |
| [Memory reference server](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)<br>MCP | Explore persistent knowledge-graph memory. | Node; local storage. | Do not store secrets or sensitive facts without a clear need. |
| [Playwright CLI](https://github.com/microsoft/playwright-cli)<br>Tool | Explore browser automation for coding-agent workflows. | Node and browser setup. | Choose CLI or MCP according to the host and workflow. |
| [MCP Apps extension](https://github.com/modelcontextprotocol/ext-apps)<br>SDK | Explore interactive app interfaces over MCP. | Compatible MCP host and app tooling. | Host support and trust boundaries matter. |

## Put one resource to work

1. Pick one entry whose purpose matches the task.
2. Read the owning source and confirm requirements for your client.
3. Supply a small, permitted input or synthetic example.
4. Define the output and check the result before expanding scope.

Use a [reference pack](../templates/reference-pack.md) for context. For connections, read [choosing an MCP server](../guides/choosing-mcp.md).
