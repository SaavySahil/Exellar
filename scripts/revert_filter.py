from pathlib import Path

path = Path("C:/Users/Shabbir Shaikh/Downloads/Proj/.claude/worktrees/ecstatic-cray/Projects.html")
html = path.read_text(encoding='utf-8')

# ── 1. Remove the filter CSS block ───────────────────────────────────────────
css_start = '\n        /* ===== Projects Filter System ===== */'
css_end = '        /* Project cards spacing fix */'
s = html.find(css_start)
e = html.find(css_end)
if s != -1 and e != -1:
    html = html[:s] + '\n        ' + css_end + html[e + len(css_end):]
    print("Filter CSS removed")
else:
    print(f"CSS block not found: s={s}, e={e}")

# ── 2. Restore original filter bar + sticky-refine-cta ───────────────────────
old_filter = '''    <div class="projects-filter">
        <div class="proj-filter-bar anim-block">
            <!-- Top: search + count -->
            <div class="proj-filter-top">
                <div class="proj-filter-search-wrap">
                    <img src="images/search-black.svg" alt="search">
                    <input type="text" id="proj-quick-search" placeholder="Search projects by name...">
                </div>
                <p class="proj-results-count" id="proj-results-count">26 projects</p>
            </div>
            <!-- Status Tabs -->
            <div class="proj-status-tabs">
                <button class="proj-tab" data-filter="all">All <span class="tab-count">26</span></button>
                <button class="proj-tab active" data-filter="ongoing">Ongoing <span class="tab-count">6</span></button>
                <button class="proj-tab" data-filter="completed">Completed <span class="tab-count">20</span></button>
            </div>
            <!-- Category Chips -->
            <div class="proj-category-chips">
                <button class="proj-chip active" data-category="all">All Types</button>
                <button class="proj-chip" data-category="high-rise">High-Rise</button>
                <button class="proj-chip" data-category="structural">Structural Works</button>
                <button class="proj-chip" data-category="institutional">Institutional</button>
                <button class="proj-chip" data-category="infrastructure">Infrastructure</button>
                <button class="proj-chip" data-category="community">Community</button>
                <button class="proj-chip" data-category="commercial">Commercial</button>
                <button class="proj-chip" data-category="landscaping">Landscaping</button>
                <button class="proj-chip" data-category="residential">Residential</button>
                <button class="proj-chip" data-category="industrial">Industrial</button>
            </div>
        </div>
    </div>
        <div class="proj-holder-section prel ov-hidden">
        <div class="proj-holder-replace ov-hidden">'''

new_filter = '''    <div class="projects-filter">
        <div class="proj-filter-groups anim-block">
            <div class="proj-search col-d-50 col-t-50 col-m-100">
                <form action="/projects" method="post" id="search-form" class="proj-filter-search prel anim-elem">
                    <div class="form-field search-input prel">
                        <img class="filter-search-icon" src="images/search-black.svg" alt="search icon">
                        <label class="input-label" for="proj-quick-search">Find A Project</label>
                        <input type="text" name="search" value="" id="proj-quick-search" class="proj-search-input input-field">
                        <div class="search-submit">
                            <img src="images/horiz-arrow-small.svg" alt="arrow">
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
    <!--  -->
        <div class="proj-holder-section prel ov-hidden">
        <div class="proj-holder-replace ov-hidden">'''

if old_filter in html:
    html = html.replace(old_filter, new_filter)
    print("Filter bar restored")
else:
    print("ERROR: filter bar not found")

# ── 3. Restore section headings (remove proj-section-heading class) ───────────
html = html.replace(
    '<div class="inline_block proj-section-heading"',
    '<div class="inline_block"'
)
print("Section headings restored")

# ── 4. Remove no-results div ─────────────────────────────────────────────────
html = html.replace(
    '\n    <div id="proj-no-results" style="font-size:initial;width:100%;text-align:center;padding:80px 20px;">\n        <p class="title fs-30" style="color:#888;margin-bottom:12px;">No projects found</p>\n        <p class="para fs-19" style="color:#aaa;">Try adjusting your filters or search term.</p>\n    </div>',
    ''
)
print("No-results div removed")

# ── 5. Remove JS block ────────────────────────────────────────────────────────
js_start = '\n<script>\n(function () {\n    var cards = document.querySelectorAll'
js_end = '})();\n</script>\n</body>'
s = html.find(js_start)
e = html.find(js_end)
if s != -1 and e != -1:
    html = html[:s] + '\n</body>'
    print("JS removed")
else:
    print(f"JS block not found: s={s}, e={e}")

path.write_text(html, encoding='utf-8')
print("\nRevert complete.")
