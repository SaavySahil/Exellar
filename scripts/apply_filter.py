from pathlib import Path

path = Path("C:/Users/Shabbir Shaikh/Downloads/Proj/.claude/worktrees/ecstatic-cray/Projects.html")
html = path.read_text(encoding='utf-8')

# ── 1. Add CSS to existing <style> block ──────────────────────────────────────
new_css = """
        /* ===== Projects Filter System ===== */
        .projects-filter { background: #fff; padding: 32px 40px 0; border-bottom: 1px solid rgba(0,0,0,0.08); }
        .proj-filter-top { display: flex; align-items: center; justify-content: space-between; margin-bottom: 28px; gap: 16px; flex-wrap: wrap; }
        .proj-filter-search-wrap { position: relative; flex: 1; max-width: 400px; }
        .proj-filter-search-wrap img { position: absolute; left: 14px; top: 50%; transform: translateY(-50%); width: 17px; pointer-events: none; }
        #proj-quick-search { width: 100%; padding: 11px 16px 11px 44px; border: 1.5px solid #ddd; border-radius: 6px; font-size: 15px; color: #2E2E2E; background: #fff; transition: border-color 0.2s; box-sizing: border-box; font-family: inherit; }
        #proj-quick-search:focus { border-color: #3E5BA9; outline: none; }
        #proj-quick-search::placeholder { color: #aaa; }
        .proj-results-count { font-size: 14px; color: #888; white-space: nowrap; }
        .proj-status-tabs { display: flex; border-bottom: 2px solid #eee; margin-bottom: 20px; }
        .proj-tab { padding: 13px 28px; font-size: 13px; font-weight: 600; letter-spacing: 0.8px; text-transform: uppercase; color: #888; background: none; border: none; border-bottom: 2px solid transparent; margin-bottom: -2px; cursor: pointer; transition: color 0.2s, border-color 0.2s; font-family: inherit; }
        .proj-tab:hover { color: #2E2E2E; }
        .proj-tab.active { color: #3E5BA9; border-bottom-color: #3E5BA9; }
        .proj-tab .tab-count { display: inline-flex; align-items: center; justify-content: center; min-width: 22px; height: 20px; padding: 0 6px; background: #eee; border-radius: 100px; font-size: 11px; font-weight: 700; margin-left: 8px; transition: background 0.2s, color 0.2s; }
        .proj-tab.active .tab-count { background: #3E5BA9; color: #fff; }
        .proj-category-chips { display: flex; flex-wrap: wrap; gap: 8px; padding-bottom: 28px; }
        .proj-chip { padding: 7px 16px; font-size: 13px; font-weight: 500; color: #555; background: #f5f5f5; border: 1.5px solid transparent; border-radius: 100px; cursor: pointer; transition: all 0.2s; white-space: nowrap; font-family: inherit; }
        .proj-chip:hover { background: #eaeaea; color: #2E2E2E; }
        .proj-chip.active { background: #fff; border-color: #3E5BA9; color: #3E5BA9; font-weight: 600; }
        .proj-section-heading { display: none !important; }
        #proj-no-results { display: none; text-align: center; padding: 80px 20px; width: 100%; font-size: initial; }
        @media (max-width: 1024px) { .projects-filter { padding: 24px 20px 0; } }
        @media (max-width: 767px) { .proj-filter-search-wrap { max-width: 100%; } .proj-tab { padding: 10px 14px; font-size: 12px; } .proj-chip { font-size: 12px; padding: 6px 12px; } }
"""
html = html.replace('        /* Project cards spacing fix */', new_css + '        /* Project cards spacing fix */')
print("CSS block added")

# ── 2. Replace filter bar + remove sticky-refine-cta ─────────────────────────
# Find the filter bar section by unique markers
start_marker = '    <div class="projects-filter">'
end_marker = '        <div class="proj-holder-replace ov-hidden">'

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx == -1 or end_idx == -1:
    print(f"ERROR: markers not found. start={start_idx}, end={end_idx}")
else:
    old_section = html[start_idx:end_idx]
    new_filter = '''    <div class="projects-filter">
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
        '''
    html = html[:start_idx] + new_filter + end_marker + html[end_idx + len(end_marker):]
    print("Filter bar replaced")

# ── 3. Add class to section heading divs ─────────────────────────────────────
html = html.replace(
    '        <!-- ONGOING PROJECTS HEADING -->\n        <div class="inline_block" style="width:100%;font-size:initial;padding:48px 0 24px;border-bottom:2px solid #3E5BA9;margin-bottom:32px;">',
    '        <!-- ONGOING PROJECTS HEADING -->\n        <div class="inline_block proj-section-heading" style="width:100%;font-size:initial;padding:48px 0 24px;border-bottom:2px solid #3E5BA9;margin-bottom:32px;">'
)
html = html.replace(
    '        <!-- COMPLETED PROJECTS HEADING -->\n        <div class="inline_block" style="width:100%;font-size:initial;padding:56px 0 24px;border-bottom:2px solid #2E2E2E;margin-bottom:32px;margin-top:16px;">',
    '        <!-- COMPLETED PROJECTS HEADING -->\n        <div class="inline_block proj-section-heading" style="width:100%;font-size:initial;padding:56px 0 24px;border-bottom:2px solid #2E2E2E;margin-bottom:32px;margin-top:16px;">'
)
print("Section headings updated")

# ── 4. Add no-results div + JS ────────────────────────────────────────────────
js_block = '''
<script>
(function () {
    var cards = document.querySelectorAll('.project-list-holder .inline_block.col-d-25');
    var searchInput = document.getElementById('proj-quick-search');
    var statusTabs = document.querySelectorAll('.proj-tab');
    var categoryChips = document.querySelectorAll('.proj-chip');
    var countEl = document.getElementById('proj-results-count');
    var noResults = document.getElementById('proj-no-results');

    var activeStatus = 'ongoing';
    var activeCategory = 'all';
    var searchTerm = '';

    var categoryKeywords = {
        'high-rise': 'high-rise',
        'structural': 'structural',
        'institutional': 'institutional',
        'infrastructure': 'infrastructure',
        'community': 'community',
        'commercial': 'commercial',
        'landscaping': 'landscaping',
        'residential': 'residential',
        'industrial': 'industrial'
    };

    function getStatus(card) {
        var el = card.querySelector('.proj-list-city');
        if (!el) return '';
        var t = el.textContent.toLowerCase();
        return t.indexOf('ongoing') > -1 ? 'ongoing' : 'completed';
    }

    function getCategory(card) {
        var el = card.querySelector('.para.fs-20.black90');
        return el ? el.textContent.trim().toLowerCase() : '';
    }

    function getName(card) {
        var el = card.querySelector('.title.fs-30');
        return el ? el.textContent.trim().toLowerCase() : '';
    }

    function filterCards() {
        var visible = 0;
        cards.forEach(function (card) {
            var status = getStatus(card);
            var cat = getCategory(card);
            var name = getName(card);

            var statusOk = activeStatus === 'all' || status === activeStatus;
            var catOk = activeCategory === 'all' || (categoryKeywords[activeCategory] && cat.indexOf(categoryKeywords[activeCategory]) > -1);
            var searchOk = !searchTerm || name.indexOf(searchTerm) > -1;

            if (statusOk && catOk && searchOk) {
                card.style.display = 'inline-block';
                visible++;
            } else {
                card.style.display = 'none';
            }
        });

        if (countEl) countEl.textContent = visible + ' project' + (visible !== 1 ? 's' : '');
        if (noResults) noResults.style.display = visible === 0 ? 'block' : 'none';
    }

    statusTabs.forEach(function (tab) {
        tab.addEventListener('click', function () {
            statusTabs.forEach(function (t) { t.classList.remove('active'); });
            this.classList.add('active');
            activeStatus = this.getAttribute('data-filter');
            filterCards();
        });
    });

    categoryChips.forEach(function (chip) {
        chip.addEventListener('click', function () {
            categoryChips.forEach(function (c) { c.classList.remove('active'); });
            this.classList.add('active');
            activeCategory = this.getAttribute('data-category');
            filterCards();
        });
    });

    if (searchInput) {
        searchInput.addEventListener('input', function () {
            searchTerm = this.value.trim().toLowerCase();
            filterCards();
        });
    }

    // Init: show Ongoing
    filterCards();
})();
</script>
</body>'''

html = html.replace('</body>', js_block, 1)
print("JS added")

# Add no-results div before closing project-list-holder
html = html.replace(
    '\n    </div>\n\n            <div style="height: 60px;"></div>',
    '\n    <div id="proj-no-results" style="font-size:initial;width:100%;text-align:center;padding:80px 20px;">\n        <p class="title fs-30" style="color:#888;margin-bottom:12px;">No projects found</p>\n        <p class="para fs-19" style="color:#aaa;">Try adjusting your filters or search term.</p>\n    </div>\n    </div>\n\n            <div style="height: 60px;"></div>'
)

path.write_text(html, encoding='utf-8')
print("\nAll changes applied to Projects.html")
