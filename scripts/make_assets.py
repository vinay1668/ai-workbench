#!/usr/bin/env python3
"""Draw original README artwork. Optional regeneration dependency: Pillow."""
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)
DATA = json.loads((ROOT / "data/resources.json").read_text())
BG, PANEL, LINE = "#0d1623", "#172434", "#2a3b4e"
INK, MUTED, MINT, ORANGE = "#edf5f6", "#afbecb", "#92efc3", "#ffb17d"


def font(size, bold=False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size=size)


def text(draw, xy, value, size, color=INK, bold=False):
    draw.text(xy, value, font=font(size, bold), fill=color)


def pill(draw, rect, value, color=MINT):
    draw.rounded_rectangle(rect, radius=14, fill=PANEL, outline=LINE, width=2)
    text(draw, (rect[0] + 17, rect[1] + 10), value, 18, color, True)


def banner():
    image = Image.new("RGB", (1280, 560), BG)
    d = ImageDraw.Draw(image)
    for x in range(32, 1280, 32):
        for y in range(32, 560, 32):
            d.point((x, y), fill="#263444")
    d.rounded_rectangle((28, 28, 1252, 532), radius=26, outline=LINE, width=2)
    text(d, (66, 66), "AI WORKBENCH", 19, MINT, True)
    text(d, (66, 119), "Less friction.", 65, INK, True)
    text(d, (66, 194), "Better work.", 65, INK, True)
    text(d, (70, 292), "Pick a skill. Connect a tool.", 25, MUTED)
    text(d, (70, 329), "Build something worth using.", 25, MUTED)
    pill(d, (68, 420, 253, 465), f"{len(DATA['resources'])} resources")
    pill(d, (267, 420, 447, 465), f"{len(DATA['categories'])} categories")
    pill(d, (461, 420, 594, 465), "6 packs", ORANGE)
    d.line((767, 197, 923, 271), fill=LINE, width=3)
    d.line((768, 339, 923, 271), fill=LINE, width=3)
    d.rounded_rectangle((690, 104, 902, 233), 18, fill=PANEL, outline=LINE, width=2)
    text(d, (713, 125), "01 / CONTEXT", 16, MINT, True)
    text(d, (713, 158), "A useful reference", 20, INK, True)
    text(d, (713, 191), "Brief + examples", 16, MUTED)
    d.rounded_rectangle((690, 286, 902, 415), 18, fill=PANEL, outline=LINE, width=2)
    text(d, (713, 307), "02 / CAPABILITY", 16, ORANGE, True)
    text(d, (713, 341), "Skills + MCP", 22, INK, True)
    text(d, (713, 376), "The right procedure", 16, MUTED)
    d.rounded_rectangle((933, 173, 1207, 376), 18, fill="#1a332f", outline=MINT, width=2)
    text(d, (958, 197), "03 / DELIVER", 16, MINT, True)
    text(d, (958, 233), "Build. Inspect.", 27, INK, True)
    text(d, (958, 271), "Improve.", 27, INK, True)
    d.line((959, 325, 1175, 325), fill="#39554c", width=2)
    text(d, (960, 338), "A result you can verify", 16, MINT)
    image.save(ASSETS / "banner.png", optimize=True)


def workflow():
    labels = [("BRIEF", "Define the outcome"), ("REFERENCE", "Show what matters"), ("SKILL + TOOL", "Add the capability"), ("BUILD", "Make it usable"), ("CHECK", "Verify the result")]
    frames = []
    for active in range(5):
        im = Image.new("RGB", (1200, 238), BG)
        d = ImageDraw.Draw(im)
        text(d, (28, 22), "FROM IDEA TO SOMETHING USEFUL", 17, MUTED, True)
        for i, (label, subtitle) in enumerate(labels):
            x = 28 + i * 234
            color = MINT if i == active else LINE
            d.rounded_rectangle((x, 76, x + 208, 186), 16, fill="#1a332f" if i == active else PANEL, outline=color, width=2)
            text(d, (x + 16, 91), f"0{i + 1}", 16, MINT if i == active else MUTED, True)
            text(d, (x + 16, 119), label, 19, INK, True)
            text(d, (x + 16, 153), subtitle, 15, MUTED)
            if i < 4:
                d.line((x + 213, 131, x + 229, 131), fill=MUTED, width=2)
                d.line((x + 225, 127, x + 229, 131, x + 225, 135), fill=MUTED, width=2)
        d.line((28, 212, 28 + (active + 1) * 228, 212), fill=MINT, width=3)
        frames.append(im)
    frames[0].save(ASSETS / "workflow-static.png", optimize=True)
    frames[0].save(ASSETS / "workflow.gif", save_all=True, append_images=frames[1:], duration=[1100] * 4 + [1700], loop=0, optimize=True, disposal=2)


def cards():
    configs = [
        ("design", "01", "DESIGN & UI", "Give the interface a point of view.", "#92efc3"),
        ("skills", "02", "REUSABLE SKILLS", "Teach a procedure once. Use it again.", "#ffb17d"),
        ("mcpdev", "03", "MCP & BROWSER TOOLS", "Bring code, docs and tools together.", "#a4c6ff"),
        ("frameworks", "04", "BUILD AI APPLICATIONS", "From an agent loop to a useful feature.", "#e7c1f5"),
        ("quality", "05", "TEST & EVALUATE", "Replace plausible with checked.", "#f3df95"),
        ("artifacts", "06", "MAKE AN ARTIFACT", "Calculators, diagrams, notebooks, decks.", "#93dce8"),
    ]
    for key, number, title, caption, accent in configs:
        safe = title.replace("&", "&amp;")
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="600" height="170" viewBox="0 0 600 170" role="img" aria-label="{safe}">
<rect x="1" y="1" width="598" height="168" rx="18" fill="{BG}" stroke="{LINE}" stroke-width="2"/>
<rect x="25" y="27" width="43" height="33" rx="8" fill="{PANEL}"/>
<g font-family="Arial, sans-serif"><text x="35" y="49" fill="{accent}" font-size="17" font-weight="700">{number}</text>
<text x="25" y="96" fill="{INK}" font-size="24" font-weight="700">{safe}</text>
<text x="25" y="132" fill="{MUTED}" font-size="18">{caption}</text>
<path d="M550 40h20m-7-7 7 7-7 7" stroke="{accent}" stroke-width="2" fill="none"/></g></svg>'''
        (ASSETS / f"card-{key}.svg").write_text(svg + "\n")


if __name__ == "__main__":
    banner()
    workflow()
    cards()
    print("Created original banner, workflow animation, static alternative, and six navigation cards.")
