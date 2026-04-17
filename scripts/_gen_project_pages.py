"""
ZDD Phase 3 — Acid Test Script
Generates Ongoing-Projects.html, Completed-Projects.html from Projects.html
with exactly the surgical changes described. Run from within the Proj directory.
"""

import re
import sys

SRC = "Projects.html"

def load(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def save(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[✓] Wrote {path}")

def make_page(html, status, hero_title, empty_msg, page_title_tag):
    # ── 1. Update <title> tag ────────────────────────────────────────────────
    html = html.replace(
        "<title>Projects | Exellar Construction LLP</title>",
        f"<title>{page_title_tag} | Exellar Construction LLP</title>"
    )

    # ── 2. Change hero h1 text content only ──────────────────────────────────
    # Original multiline hero title block:
    #   <h1 class="title fs-90 white hero-title anim-elem top">
    #       Delivering On What
    #       <span class="prel underlined-word" style="...">Matters</span>
    #   </h1>
    # Use regex for hero h1 — match opening tag through closing tag regardless of internal whitespace
    h1_pattern = re.compile(
        r'<h1 class="title fs-90 white hero-title anim-elem top">.*?</h1>',
        re.DOTALL
    )
    new_h1 = f'<h1 class="title fs-90 white hero-title anim-elem top">{hero_title}</h1>'
    new_html_h1, h1_count = h1_pattern.subn(new_h1, html, count=1)
    if h1_count:
        html = new_html_h1
        print(f"  [✓] Hero h1 updated to '{hero_title}'")
    else:
        print(f"  [!] WARN: Could not find hero h1 pattern — may need manual check", file=sys.stderr)

    # ── 3. Hide the refine-search trigger ────────────────────────────────────
    old_refine = '<div class="refine-search-col specs-open anim-elem" data-popup=".specs-filter">'
    new_refine = '<div class="refine-search-col specs-open anim-elem" data-popup=".specs-filter" style="display:none">'
    html = html.replace(old_refine, new_refine)
    print(f"  [✓] Refine filter trigger hidden")

    # ── 4. Modify project-list-holder: add id, clear children, inject loading/empty ──
    old_holder_open = '<div class="project-list-holder f0 anim-block">'
    new_holder_open = '<div class="project-list-holder f0 anim-block" id="projects-grid-container">'
    html = html.replace(old_holder_open, new_holder_open)
    print(f"  [✓] Added id='projects-grid-container'")

    # Remove all child divs inside project-list-holder up to the closing comment/div
    # The holder block runs from the open tag to:  <!--  -->  \r\n    </div>
    # Use regex to match the entire inner content of the holder div
    # We target: everything from the open tag through "<!--  -->\r\n    </div>"
    holder_pattern = re.compile(
        r'(<div class="project-list-holder f0 anim-block" id="projects-grid-container">)'
        r'.*?'
        r'(\s*<!--\s*-->\s*\r?\n?\s*</div>)',
        re.DOTALL
    )
    loading_empty = (
        '\r\n        <div id="projects-loading" style="padding:40px 0; width:100%">'
        '\r\n          <p class="para fs-19 black90">Loading projects...</p>'
        '\r\n        </div>'
        '\r\n        <div id="projects-empty" style="display:none; padding:40px 0; width:100%">'
        f'\r\n          <p class="para fs-23 black90">{empty_msg}</p>'
        '\r\n        </div>'
        '\r\n    </div>'
    )
    new_html, count = holder_pattern.subn(r'\1' + loading_empty, html, count=1)
    if count:
        html = new_html
        print(f"  [✓] Project cards cleared; loading/empty injected")
    else:
        print(f"  [!] WARN: Could not auto-clear project cards — check regex", file=sys.stderr)

    # ── 5. Hide pagination wrapper ────────────────────────────────────────────
    old_pag = '<div class="wrapper-960 proj-list-pagination">'
    new_pag = '<div class="wrapper-960 proj-list-pagination" style="display:none">'
    if old_pag in html:
        html = html.replace(old_pag, new_pag)
        print(f"  [✓] Pagination hidden")
    else:
        print(f"  [!] WARN: Pagination div not found", file=sys.stderr)

    # ── 6. Add dynamic scripts before </body> ────────────────────────────────
    injection = (
        f'\t<script>var PROJECTS_STATUS = "{status}";</script>\r\n'
        f'\t<script src="js/projects-dynamic.js"></script>\r\n'
    )
    html = html.replace("</body></html>", injection + "</body></html>")
    print(f"  [✓] Dynamic scripts injected (status='{status}')")

    return html


# ── Build Ongoing-Projects.html ──────────────────────────────────────────────
print("\n[BUILD] Ongoing-Projects.html")
ongoing_html = load(SRC)
ongoing_html = make_page(
    ongoing_html,
    status="ongoing",
    hero_title="Ongoing Projects",
    empty_msg="No ongoing projects at this time.",
    page_title_tag="Ongoing Projects"
)
save("Ongoing-Projects.html", ongoing_html)

# ── Build Completed-Projects.html ────────────────────────────────────────────
print("\n[BUILD] Completed-Projects.html")
completed_html = load(SRC)
completed_html = make_page(
    completed_html,
    status="completed",
    hero_title="Completed Projects",
    empty_msg="No completed projects at this time.",
    page_title_tag="Completed Projects"
)
save("Completed-Projects.html", completed_html)

print("\n[DONE] Both pages generated.")
