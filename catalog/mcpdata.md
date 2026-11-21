# MCP · data & infrastructure

[← All categories](../CATALOG.md) · [Starter recipes](../guides/starter-recipes.md) · 10 resources

Checked **2026-11-21**. Source-checked, not runtime-tested. Setup, access, and pricing can change; follow the owning source.

## Resources

| Resource | Use it for | Setup | Before choosing |
| --- | --- | --- | --- |
| [Supabase MCP](https://github.com/supabase/mcp)<br>MCP | Connect an assistant to Supabase development tools. | Supabase project and auth. | Prefer a development project and restricted access. |
| [Neon MCP](https://github.com/neondatabase/mcp-server-neon)<br>MCP | Work with Neon database development workflows. | Neon account and auth. | Database writes and branches have real consequences. |
| [MongoDB MCP](https://github.com/mongodb-js/mongodb-mcp-server)<br>MCP | Use MongoDB tools through an MCP client. | MongoDB setup and credentials. | Scope database permissions and use safe sample data. |
| [Redis MCP](https://github.com/redis/mcp-redis)<br>MCP | Explore Redis data tools for assistants. | Redis instance and auth. | Avoid exposing production data by default. |
| [AWS MCP Servers](https://github.com/awslabs/mcp)<br>MCP suite | Find AWS-focused server implementations. | AWS setup; per-server requirements. | Upstream recommends Agent Toolkit for AWS for production agent development. Follow that link from the README before choosing a server. |
| [Azure MCP](https://github.com/microsoft/mcp)<br>MCP suite | Explore Microsoft and Azure MCP integrations. | Per-server runtime and account setup. | Choose only the services and scopes needed. |
| [Cloudflare MCP Servers](https://github.com/cloudflare/mcp-server-cloudflare)<br>MCP suite | Work with Cloudflare platform tools. | Cloudflare account and auth. | Review deployment and account mutation permissions. |
| [Sentry MCP](https://github.com/getsentry/toolkit)<br>MCP | Investigate application errors with Sentry context. | Sentry account and auth. | Error events may contain sensitive application data. |
| [Docker MCP Gateway](https://github.com/docker/mcp-gateway)<br>Tool | Manage access to MCP servers through Docker tooling. | Docker and gateway setup. | Isolation does not itself establish that a server is trustworthy. |

## Historical or superseded — read before choosing

| Resource | Use it for | Setup | Before choosing |
| --- | --- | --- | --- |
| [Prisma MCP](https://github.com/prisma/mcp)<br>MCP · **historical** | Explore Prisma tooling through MCP. | Prisma-related project and setup. | Archived upstream on 2026-10-26. Read the README for the hosted service; do not start with the retired local server. |

## Put one resource to work

1. Pick one entry whose purpose matches the task.
2. Read the owning source and confirm requirements for your client.
3. Supply a small, permitted input or synthetic example.
4. Define the output and check the result before expanding scope.

Use a [reference pack](../templates/reference-pack.md) for context. For connections, read [choosing an MCP server](../guides/choosing-mcp.md).
