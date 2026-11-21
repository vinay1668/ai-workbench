#!/usr/bin/env python3
"""Render the Markdown directory from the public resource manifest (stdlib only)."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render():
    data = json.loads((ROOT / "data/resources.json").read_text())
    resources = data["resources"]
    categories = data["categories"]
    counts = {key: sum(r["category"] == key for r in resources) for key in categories}
    outputs = {}
    index = ["# The resource directory", "", f"**{len(resources)} resources · {len(categories)} categories · checked {data['checked']}**", "",
             "Choose a job, open its category, then follow the original source. Every entry explains its purpose, setup, and a practical limitation. Historical and superseded projects are separated within each category.", "",
             "**Source-checked** means a public page or file was retrieved with TinyFish and reviewed for this directory. It does not mean installed, benchmarked, audited, or guaranteed compatible. Some directory pages expose limited content; use them as discovery links. See [source notes](SOURCES.md) and the [public manifest](data/resources.json).", "",
             "| Category | Resources | Good first question |", "| --- | ---: | --- |"]
    questions = {
        "discovery": "Where should I look for the right tool?",
        "skills": "Can I reuse a procedure instead of repeating instructions?",
        "design": "How do I give my app a coherent visual direction?",
        "mcpdev": "Can my agent inspect code, docs, and a browser?",
        "mcpdata": "Which database or infrastructure connection fits my stack?",
        "mcpwork": "Can I bring web or workspace context into the task?",
        "coding": "Which coding environment suits this workflow?",
        "frameworks": "What helps me build an AI feature or workflow?",
        "knowledge": "How do I work with documents or local models?",
        "quality": "How will I know the result works?",
        "artifacts": "Can this become a usable tool, diagram, notebook, or deck?",
        "learning": "Where can I learn the underlying techniques?",
    }
    for key, title in categories.items():
        index.append(f"| [{title}](catalog/{key}.md) | {counts[key]} | {questions[key]} |")
        rows = [r for r in resources if r["category"] == key]
        text = [f"# {title}", "", f"[← All categories](../CATALOG.md) · [Starter recipes](../guides/starter-recipes.md) · {len(rows)} resources", "",
                f"Checked **{data['checked']}**. Source-checked, not runtime-tested. Setup, access, and pricing can change; follow the owning source.", ""]
        for lifecycle, heading in [("current", "Resources"), ("other", "Historical or superseded — read before choosing")]:
            selected = [r for r in rows if (r["lifecycle"] == "current") == (lifecycle == "current")]
            if not selected:
                continue
            text.extend([f"## {heading}", "", "| Resource | Use it for | Setup | Before choosing |", "| --- | --- | --- | --- |"])
            for r in selected:
                status = f" · **{r['lifecycle']}**" if r["lifecycle"] != "current" else ""
                text.append(f"| [{r['name']}]({r['url']})<br>{r['kind']}{status} | {r['use']} | {r['setup']} | {r['note']} |")
            text.append("")
        text.extend(["## Put one resource to work", "", "1. Pick one entry whose purpose matches the task.", "2. Read the owning source and confirm requirements for your client.", "3. Supply a small, permitted input or synthetic example.", "4. Define the output and check the result before expanding scope.", "",
                     "Use a [reference pack](../templates/reference-pack.md) for context. For connections, read [choosing an MCP server](../guides/choosing-mcp.md).", ""])
        outputs[f"catalog/{key}.md"] = "\n".join(text)
    index.extend(["", "## Fast paths", "", "- [Eight practical starter recipes](guides/starter-recipes.md)", "- [Choose a prompt, skill, MCP, CLI, or artifact](guides/choose-your-tool.md)", "- [Choose an MCP server](guides/choosing-mcp.md)", "- Search locally: `python3 scripts/find.py browser`", "- Search by kind: `python3 scripts/find.py --kind Skill`", "", "This is a curated starting set, not a claim to list every server or tool. Directory entries lead to much larger upstream collections. External projects retain their own licenses and terms.", ""])
    outputs["CATALOG.md"] = "\n".join(index)
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated files differ")
    args = parser.parse_args()
    changed = []
    for relative, content in render().items():
        path = ROOT / relative
        if not path.exists() or path.read_text() != content:
            changed.append(relative)
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
    if args.check and changed:
        raise SystemExit("Regenerate catalog: " + ", ".join(changed))
    print("Catalog is current." if args.check else f"Rendered catalog; {len(changed)} files updated.")


if __name__ == "__main__":
    main()
