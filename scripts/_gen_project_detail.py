"""
_gen_project_detail.py
Generates Project-Detail.html from "Project Page.html" with surgical changes only.
Safe to re-run: idempotent — always re-reads the original source.
"""

import re
import shutil
from pathlib import Path

SRC  = Path('Project Page.html')
DEST = Path('Project-Detail.html')

print(f"Reading: {SRC}")
raw = SRC.read_bytes()
html = raw.decode('utf-8-sig')  # handle BOM if present

# ── 1. <title> tag ────────────────────────────────────────────────────────────
html = re.sub(
    r'<title>[^<]*<\/title>',
    '<title>Project | Exellar</title>',
    html, count=1
)
print("  ✓ <title> updated")

# ── 2. specs-body: add id + clear all specs-row children ─────────────────────
# The div opens at <div class="specs-body"> and ends just before </div>\n</div>
# Strategy: match the whole specs-body block and replace its contents
html = re.sub(
    r'(<div class="specs-body">)\s*(.*?)\s*(</div>\s*</div>\s*<!-- project detail hero|</div>\n</div>)',
    lambda m: m.group(1) + '\n\n    </div>',
    html,
    count=1,
    flags=re.DOTALL
)

# Now add id="specs-body" to the opening tag
html = html.replace(
    '<div class="specs-body">',
    '<div class="specs-body" id="specs-body">',
    1
)
print("  ✓ specs-body id added + contents cleared")

# ── 3. project-landscape-img: clear style and data-src ───────────────────────
html = re.sub(
    r'(<div class="project-landscape-img img-parallax b-lazy")[^>]*>',
    r'\1 data-src="" style="">',
    html, count=1
)
print("  ✓ project-landscape-img cleared")

# ── 4. proj-widget-txt: clear location h2 + title h1 ────────────────────────
# h2.section-label inside proj-widget-txt
html = re.sub(
    r'(<div class="proj-widget-txt">.*?<h2 class="section-label">)[^<]*(</h2>)',
    r'\1\2',
    html, count=1, flags=re.DOTALL
)
html = re.sub(
    r'<h2 class="section-label">(</h2>)',
    r'<h2 class="section-label" id="project-location">\1',
    html, count=1
)

# h1.title.fs-45 inside proj-widget-txt
html = re.sub(
    r'(<h1 class="title fs-45">)[^<]*(</h1>)',
    r'\1\2',
    html, count=1
)
html = html.replace(
    '<h1 class="title fs-45"></h1>',
    '<h1 class="title fs-45" id="project-title"></h1>',
    1
)
print("  ✓ project-location + project-title IDs added, text cleared")

# ── 5. detail-two-col-txt: headline h2 + story p ─────────────────────────────
html = re.sub(
    r'<h2 class="title fs-90 anim-elem top">[^<]*</h2>',
    '<h2 class="title fs-90 anim-elem top" id="project-headline"></h2>',
    html, count=1
)
html = re.sub(
    r'<p class="para fs-32">\s*(.*?)\s*</p>',
    '<p class="para fs-32" id="project-story"></p>',
    html, count=1, flags=re.DOTALL
)
print("  ✓ project-headline + project-story IDs added, text cleared")

# ── 6. Share links: add IDs and clear hrefs ──────────────────────────────────
html = html.replace(
    '<a class="fb-share" href="">',
    '<a class="fb-share" id="share-facebook" href="">',
    1
)
html = html.replace(
    '<a class="twitter-share" href="">',
    '<a class="twitter-share" id="share-twitter" href="">',
    1
)
html = html.replace(
    '<a class="linkedin-share" href="">',
    '<a class="linkedin-share" id="share-linkedin" href="">',
    1
)
# Mail share anchor has data-title and mailto href  — clear href + add id
html = re.sub(
    r'<a class="" href="mailto:[^"]*"([^>]*)>(<img src="images/mail-share\.svg")',
    r'<a class="" id="share-email" href=""\1>\2',
    html, count=1
)
print("  ✓ share link IDs added, hrefs cleared")

# ── 7. article-cta-section: hide ──────────────────────────────────────────────
html = html.replace(
    '<section class="article-cta-section prel">',
    '<section class="article-cta-section prel" style="display:none">',
    1
)
print("  ✓ article-cta-section hidden")

# ── 8. Inject <script src="js/project-detail.js"> before </body></html> ───────
html = html.replace(
    '</body></html>',
    '\t<script src="js/project-detail.js"></script>\r\n</body></html>',
    1
)
print("  ✓ project-detail.js script tag injected")

# ── Write output ──────────────────────────────────────────────────────────────
DEST.write_bytes(html.encode('utf-8'))
print(f"\n✅ Written: {DEST}  ({DEST.stat().st_size:,} bytes)")
