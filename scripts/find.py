#!/usr/bin/env python3
"""Search the local resource directory without installing dependencies."""
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("query", nargs="?", default="", help="words to match in resource descriptions")
parser.add_argument("--category", help="category key, e.g. design, skills, mcpdev")
parser.add_argument("--kind", help="exact kind, e.g. MCP, Skill, Directory")
parser.add_argument("--include-history", action="store_true", help="include historical/superseded entries")
parser.add_argument("--json", action="store_true", help="machine-readable results")
args = parser.parse_args()
data = json.loads((Path(__file__).resolve().parents[1] / "data/resources.json").read_text())
if args.category and args.category not in data["categories"]:
    parser.error("unknown category; choose: " + ", ".join(data["categories"]))
terms = args.query.casefold().split()
results = []
for r in data["resources"]:
    searchable = " ".join(str(r[k]) for k in ["name", "kind", "use", "setup", "note", "category"]).casefold()
    if all(term in searchable for term in terms) and (not args.category or r["category"] == args.category) and (not args.kind or r["kind"].casefold() == args.kind.casefold()) and (args.include_history or r["lifecycle"] == "current"):
        results.append(r)
if args.json:
    print(json.dumps(results, indent=2, ensure_ascii=False))
else:
    for r in results:
        print(f"{r['name']} [{r['kind']} · {r['category']} · {r['lifecycle']}]\n  {r['use']}\n  {r['url']}\n  Setup: {r['setup']}\n")
    print(f"{len(results)} results. Checked {data['checked']}; source-checked, not runtime-tested.")
