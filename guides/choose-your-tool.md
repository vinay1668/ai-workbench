# Choose the smallest tool that fits

| What is missing? | Choose | Example |
| --- | --- | --- |
| Clear instructions for one task | A prompt | Give the audience, inputs, output and success criteria |
| A concrete example or visual direction | A reference pack | Annotated screenshots and design rules |
| The same procedure on repeated tasks | A skill | Reusable document production or UI review instructions |
| Access to a source or external action | An integration such as MCP | Retrieve project context, search docs, inspect a browser |
| A direct operation your agent can already run | A CLI or script | Run a focused browser test or a project build |
| Something a person should use interactively | An artifact | A calculator, decision matrix, diagram, or demo |
| A reusable AI feature inside your own application | An SDK or framework | Tool calls, retrieval, typed outputs, workflow state |

These pieces can be combined. A skill describes a procedure; an MCP server exposes tools and context; a model and host decide how to use them. Adding a server does not automatically improve the brief or prove the result is correct. The [Agent Skills standard](https://agentskills.io/) and [MCP reference project](https://github.com/modelcontextprotocol/servers) are useful primary starting points.

## Example: improve an onboarding screen

1. **Brief:** new users must finish account setup on a small screen.
2. **Reference:** one annotated example of a clear form.
3. **Skill:** a design review procedure, if useful.
4. **Tool:** the existing browser CLI or an MCP browser integration.
5. **Check:** keyboard completion, invalid-input recovery, and a small-screen screenshot.

Start with one workflow. Add another tool only when you can name the missing capability. The [starter recipes](starter-recipes.md) pair a small number of resources with concrete tasks.
