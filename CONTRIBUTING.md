# Contributing

Add resources that make a real task easier. One well-explained example is more useful than twenty unexplained links.

For a resource entry, include:

- Original public source URL and author/project.
- Task it helps with and when to choose it.
- What to attach and how to use the result.
- Prerequisites and limitations.
- Date checked and whether you read, installed, or tested it.
- License and attribution if you copy any upstream material.

For a worked example, include sanitized inputs, the exact reusable prompt, the resulting deliverable, and observed checks. Use invented data and assets you have rights to share. Label mock outputs and untested claims.

Never contribute credentials, tokens, cookies, private URLs, account exports, local configuration, personal files, customer records, or chat-history dumps. Do not add leaked prompts, bypass instructions, or unsubstantiated productivity claims. Review both the files and commit history before publishing.

Original contributions are MIT licensed unless explicitly documented otherwise. External links retain upstream terms. Avoid adding dependencies or automated downloads for a documentation-only contribution.

## Editing the directory

The canonical resource list is `data/resources.json`. Add an entry with a unique ID, category, original source URL, purpose, setup, limitation, review date, and lifecycle status. Keep historical or superseded tools labeled. Record a redirect in `discovered_url` when the owning repository has moved, and use the current source URL for the entry.

Read the owning source before marking an entry `source-checked`. That status means source review, not that you installed or tested the tool. If the source is inaccessible or only a description is exposed, document the limitation rather than inventing details.

```bash
python3 scripts/build_catalog.py
python3 scripts/check.py
python3 scripts/find.py --category design
```

Category pages are generated; change their content through the manifest. Use `--include-history` with the search command to include retired or superseded entries. Check local links, visual assets, and the exact staged files before publication. The built-in checker catches common patterns and unexpected file types; it is not an exhaustive secret scanner.
