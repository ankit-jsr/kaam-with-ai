from pathlib import Path
from html.parser import HTMLParser
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1] / "site"
errors = []
required = ["index.html", "styles.css", "robots.txt", "sitemap.xml", "about.html", "privacy.html"]
for name in required:
    if not (ROOT / name).is_file():
        errors.append(f"Missing required file: {name}")

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src"):
            value = attrs.get(key)
            if value:
                self.links.append(value)

for page in ROOT.rglob("*.html"):
    source = page.read_text(encoding="utf-8")
    if re.search(r"\{(?:article_title|slug|description|body)\}", source):
        errors.append(f"Unresolved template placeholder: {page.relative_to(ROOT)}")
    parser = LinkParser()
    parser.feed(source)
    for link in parser.links:
        if link.startswith(("http://", "https://", "mailto:", "tel:", "data:", "#", "javascript:")):
            continue
        local = link.split("#", 1)[0].split("?", 1)[0]
        if not local:
            continue
        target = (ROOT / local.lstrip("/")) if local.startswith("/") else (page.parent / local)
        if not target.exists():
            errors.append(f"Broken local link in {page.relative_to(ROOT)}: {link}")

try:
    sitemap = ET.parse(ROOT / "sitemap.xml")
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locations = [item.text or "" for item in sitemap.findall(".//sm:loc", ns)]
    if not locations:
        errors.append("Sitemap contains no URLs")
    for url in locations:
        if not url.startswith("https://kaamwithai.pages.dev/"):
            errors.append(f"Unexpected sitemap URL: {url}")
        path = url.removeprefix("https://kaamwithai.pages.dev/")
        if path and not (ROOT / path).is_file():
            errors.append(f"Sitemap URL does not map to a file: {url}")
except Exception as exc:
    errors.append(f"Invalid sitemap.xml: {exc}")

robots = (ROOT / "robots.txt").read_text(encoding="utf-8") if (ROOT / "robots.txt").exists() else ""
if "Sitemap: https://kaamwithai.pages.dev/sitemap.xml" not in robots:
    errors.append("robots.txt does not reference the production sitemap")

if errors:
    print("\n".join(f"ERROR: {item}" for item in errors))
    sys.exit(1)
print("KaamWithAI validation passed.")
