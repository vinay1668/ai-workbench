#!/usr/bin/env python3
"""Check catalog structure, local links, public-file scope and common secret patterns."""
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
data = json.loads((ROOT / "data/resources.json").read_text())
rows = data["resources"]
required = {"id", "category", "name", "url", "kind", "use", "setup", "note", "checked", "review", "lifecycle"}
seen_ids, seen_urls = set(), set()
for row in rows:
    if not required <= row.keys() or any(not row.get(k) for k in required):
        errors.append(f"Missing resource fields: {row.get('id', 'unknown')}")
    if row["id"] in seen_ids or row["url"].rstrip("/").casefold() in seen_urls:
        errors.append(f"Duplicate resource: {row['id']}")
    seen_ids.add(row["id"])
    seen_urls.add(row["url"].rstrip("/").casefold())
    parsed = urlsplit(row["url"])
    if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
        errors.append(f"Invalid public source URL: {row['id']}")
    if row["category"] not in data["categories"] or row["lifecycle"] not in {"current", "historical", "superseded"}:
        errors.append(f"Invalid resource category/status: {row['id']}")
    if row["review"] != "source-checked":
        errors.append(f"Unfinished source review: {row['id']}")

result = subprocess.run([sys.executable, "scripts/build_catalog.py", "--check"], cwd=ROOT, capture_output=True, text=True)
if result.returncode:
    errors.append(result.stdout + result.stderr)

# Inspect only files in this repository; never traverse the parent workspace.
listed = subprocess.run(["git", "ls-files", "-co", "--exclude-standard", "-z"], cwd=ROOT, check=True, capture_output=True).stdout
files = sorted({p for p in listed.decode().split("\0") if p})
patterns = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{25,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{24,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"/(?:Users|home)/[A-Za-z0-9_.-]+/"),
]
for relative in files:
    path = ROOT / relative
    if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
        errors.append(f"Unexpected file indirection: {relative}")
        continue
    if path.suffix.lower() not in {".md", ".json", ".py", ".svg", ".png", ".gif"} and relative not in {"LICENSE", ".gitignore"}:
        errors.append(f"Unexpected public file type: {relative}")
    if path.suffix in {".png", ".gif"}:
        if path.stat().st_size > 1_000_000:
            errors.append(f"Oversized README image: {relative}")
        continue
    body = path.read_text()
    if any(pattern.search(body) for pattern in patterns):
        errors.append(f"Possible secret or personal path: {relative} (value withheld)")
    if path.suffix == ".md":
        targets = re.findall(r"\]\(([^)]+)\)", body) + re.findall(r'(?:src|href)="([^"]+)"', body)
        for target in targets:
            parsed = urlsplit(target)
            if parsed.scheme or not parsed.path:
                continue
            destination = (path.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(ROOT) or not destination.exists():
                errors.append(f"Broken or out-of-repository local link: {relative}: {target}")
    if path.suffix == ".svg":
        ET.fromstring(body)
        if re.search(r"<script|<foreignObject|(?:href|src)=", body, re.I):
            errors.append(f"Unexpected SVG active/external content: {relative}")

if errors:
    print("\n".join(errors))
    raise SystemExit(1)
print(f"Checked {len(rows)} unique resources in {len(data['categories'])} categories and {len(files)} public files.")
print("Generated pages, local file links, SVG structure, file types, and common secret/personal-path patterns passed.")
print("This check does not audit third-party software or detect every possible secret.")
