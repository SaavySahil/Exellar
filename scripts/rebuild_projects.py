from pathlib import Path
import re

path = Path("C:/Users/Shabbir Shaikh/Downloads/Proj/.claude/worktrees/ecstatic-cray/Projects.html")
html = path.read_text(encoding='utf-8')

# ── 1. Remove section heading divs ────────────────────────────────────────────
html = re.sub(
    r'\s*<!-- ONGOING PROJECTS HEADING -->.*?</div>\s*',
    '\n',
    html, flags=re.DOTALL
)
html = re.sub(
    r'\s*<!-- COMPLETED PROJECTS HEADING -->.*?</div>\s*',
    '\n',
    html, flags=re.DOTALL
)
print("Section headings removed")

# ── 2. Add data attributes to all 26 project cards ───────────────────────────
# Map: comment marker → (status, location, scope, industry)
card_data = {
    '<!-- 1. Multistar Autograph -->':           ('ongoing',   'mumbai',      'high-rise',     'residential'),
    '<!-- 2. Concrete 3D Printing IIT Mumbai -->': ('ongoing',  'mumbai',      'institutional', 'institutional'),
    '<!-- 3. Lodha Evergreen -->':               ('ongoing',   'mumbai',      'high-rise',     'residential'),
    '<!-- 4. Raheja Solaris -->':                ('ongoing',   'navi-mumbai', 'high-rise',     'residential'),
    '<!-- 5. Rustomjee Aden -->':                ('ongoing',   'mumbai',      'high-rise',     'residential'),
    '<!-- 6. Rustomjee Ashiana -->':             ('ongoing',   'mumbai',      'high-rise',     'residential'),
    '<!-- 7. General Aviation Terminal -->':     ('completed', 'mumbai',      'infrastructure','commercial'),
    '<!-- 8. Lodha Casa Supremo -->':            ('completed', 'mumbai',      'high-rise',     'residential'),
    '<!-- 9. Ayan Residency -->':                ('completed', 'mumbai',      'high-rise',     'residential'),
    '<!-- 10. NL Aryavarta -->':                 ('completed', 'mumbai',      'high-rise',     'residential'),
    '<!-- 11. Crescent Nexus -->':               ('completed', 'mumbai',      'high-rise',     'residential'),
    '<!-- 12. Rustomjee Crown -->':              ('completed', 'mumbai',      'infrastructure','commercial'),
    '<!-- 13. KSI Community Center Wanowrie -->': ('completed','pune',        'rehabilitation', 'community'),
    '<!-- 14. Crescent SkyHeights -->':          ('completed', 'mumbai',      'high-rise',     'residential'),
    '<!-- 15. Crescent Heritage -->':            ('completed', 'mumbai',      'high-rise',     'residential'),
    '<!-- 16. Omkar 1973 Tower -->':             ('completed', 'mumbai',      'rehabilitation', 'residential'),
    '<!-- 17. St Francis Hotel Management Institute -->': ('completed','mumbai','institutional','institutional'),
    '<!-- 18. KSI Community Center Kurla -->':   ('completed', 'mumbai',      'rehabilitation', 'community'),
    '<!-- 19. Kantharia Lake View -->':          ('completed', 'mumbai',      'high-rise',     'residential'),
    '<!-- 20. Kalpataru Primus -->':             ('completed', 'mumbai',      'infrastructure','commercial'),
    '<!-- 21. Omkar Alta Monte -->':             ('completed', 'mumbai',      'rehabilitation', 'residential'),
    '<!-- 22. Bramha Sky City -->':              ('completed', 'pune',        'high-rise',     'residential'),
    '<!-- 23. 1973 Sales Pavilion -->':          ('completed', 'mumbai',      'commercial',    'commercial'),
    '<!-- 24. KSI Arambaug -->':                 ('completed', 'mumbai',      'rehabilitation', 'community'),
    '<!-- 25. K. S. Floritech Park -->':         ('completed', 'pune',        'industrial',    'industrial'),
    '<!-- 26. B3 Mantralay -->':                 ('completed', 'mumbai',      'landscaping',   'commercial'),
}

old_div = '<div class="inline_block col-d-25 col-t-50 col-m-100 anim-elem top">'
for comment, (status, loc, scope, industry) in card_data.items():
    new_div = f'<div class="inline_block col-d-25 col-t-50 col-m-100 anim-elem top proj-card" data-status="{status}" data-location="{loc}" data-scope="{scope}" data-industry="{industry}">'
    html = html.replace(
        comment + '\n        ' + old_div,
        comment + '\n        ' + new_div,
        1
    )
print("Data attributes added to all 26 cards")

# ── 3. Replace flyout filter content ─────────────────────────────────────────
old_flyout_body = html[html.find('<div class="refine-filter-groups">'):html.find('<!--  -->\n                </div>\n            </div>\n        </form>') + len('<!--  -->\n                </div>\n            </div>\n        </form>')]

new_flyout_body = '''<div class="refine-filter-groups">

                    <div class="clear-contries clear-all">Clear All Filters</div>

                    <!-- Status -->
                    <div class="faq-element">
                        <div class="faq-row">
                            <p class="para fs-16 upper"><b>By Status</b></p>
                            <img class="faq-arrow" src="images/orange-arrow.svg" alt="arrow faq open">
                        </div>
                        <div class="faq-answer">
                            <div class="filter-block">
                                Ongoing
                                <input type="checkbox" name="status[]" value="ongoing">
                            </div>
                            <div class="filter-block">
                                Completed
                                <input type="checkbox" name="status[]" value="completed">
                            </div>
                        </div>
                    </div>

                    <!-- Location -->
                    <div class="faq-element">
                        <div class="faq-row">
                            <p class="para fs-16 upper"><b>By Location</b></p>
                            <img class="faq-arrow" src="images/orange-arrow.svg" alt="arrow faq open">
                        </div>
                        <div class="faq-answer">
                            <div class="filter-block">
                                Mumbai
                                <input type="checkbox" name="location[]" value="mumbai">
                            </div>
                            <div class="filter-block">
                                Navi Mumbai
                                <input type="checkbox" name="location[]" value="navi-mumbai">
                            </div>
                            <div class="filter-block">
                                Pune
                                <input type="checkbox" name="location[]" value="pune">
                            </div>
                        </div>
                    </div>

                    <!-- Scope of Work -->
                    <div class="faq-element">
                        <div class="faq-row">
                            <p class="para fs-16 upper"><b>By Scope of Work</b></p>
                            <img class="faq-arrow" src="images/orange-arrow.svg" alt="arrow faq open">
                        </div>
                        <div class="faq-answer">
                            <div class="filter-block">
                                High-Rise Construction
                                <input type="checkbox" name="scope[]" value="high-rise">
                            </div>
                            <div class="filter-block">
                                Structural Rehabilitation
                                <input type="checkbox" name="scope[]" value="rehabilitation">
                            </div>
                            <div class="filter-block">
                                Infrastructure Works
                                <input type="checkbox" name="scope[]" value="infrastructure">
                            </div>
                            <div class="filter-block">
                                Institutional Construction
                                <input type="checkbox" name="scope[]" value="institutional">
                            </div>
                            <div class="filter-block">
                                Commercial Works
                                <input type="checkbox" name="scope[]" value="commercial">
                            </div>
                            <div class="filter-block">
                                Landscaping
                                <input type="checkbox" name="scope[]" value="landscaping">
                            </div>
                            <div class="filter-block">
                                Industrial
                                <input type="checkbox" name="scope[]" value="industrial">
                            </div>
                        </div>
                    </div>

                    <!-- Industry -->
                    <div class="faq-element">
                        <div class="faq-row">
                            <p class="para fs-16 upper"><b>By Industry</b></p>
                            <img class="faq-arrow" src="images/orange-arrow.svg" alt="arrow faq open">
                        </div>
                        <div class="faq-answer">
                            <div class="filter-block">
                                Residential
                                <input type="checkbox" name="industry[]" value="residential">
                            </div>
                            <div class="filter-block">
                                Commercial
                                <input type="checkbox" name="industry[]" value="commercial">
                            </div>
                            <div class="filter-block">
                                Institutional
                                <input type="checkbox" name="industry[]" value="institutional">
                            </div>
                            <div class="filter-block">
                                Community / Social
                                <input type="checkbox" name="industry[]" value="community">
                            </div>
                            <div class="filter-block">
                                Industrial
                                <input type="checkbox" name="industry[]" value="industrial">
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </form>'''

if '<div class="refine-filter-groups">' in html:
    start = html.find('<div class="refine-filter-groups">')
    end = html.find('</form>', start) + len('</form>')
    html = html[:start] + new_flyout_body + html[end:]
    print("Flyout filters replaced")
else:
    print("ERROR: flyout not found")

# ── 4. Restore pagination + add no-results div ───────────────────────────────
old_spacer = '<div style="height: 60px;"></div>'
new_pagination = '''<div id="proj-no-results" style="display:none;width:100%;font-size:initial;text-align:center;padding:60px 20px;">
        <p class="title fs-30" style="color:#888;margin-bottom:8px;">No projects found</p>
        <p class="para fs-19" style="color:#aaa;">Try adjusting your filters.</p>
    </div>

        <div class="wrapper-960 proj-list-pagination" id="proj-pagination">
            <div class="inline_block col-d-50 col-t-50 col-m-100">
                <div class="proj-paging proj-page-submit" id="proj-page-numbers"></div>
            </div>
            <div class="inline_block col-d-50 col-t-50 col-m-100">
                <div class="proj-show-more" id="proj-next-wrap">
                    <a href="#" id="proj-next-btn" class="">
                        <p class="para fs-16 black90 upper">Next page</p>
                    </a>
                    <img src="images/orange-arrow.svg" alt="arrow down">
                </div>
            </div>
        </div>
    <div style="height: 20px;"></div>'''

html = html.replace(old_spacer, new_pagination, 1)
print("Pagination restored")

# ── 5. Add functional JS before </body> ──────────────────────────────────────
js = '''
<script>
(function () {
    var CARDS_PER_PAGE = 8;
    var allCards = Array.prototype.slice.call(document.querySelectorAll('.proj-card'));
    var currentPage = 1;
    var filteredCards = allCards.slice();

    // ── Filter state ──────────────────────────────────────────────────────
    function getChecked(name) {
        var checked = [];
        document.querySelectorAll('input[name="' + name + '"]:checked').forEach(function (cb) {
            checked.push(cb.value);
        });
        return checked;
    }

    function applyFilters() {
        var statuses  = getChecked('status[]');
        var locations = getChecked('location[]');
        var scopes    = getChecked('scope[]');
        var industries = getChecked('industry[]');
        var search    = (document.getElementById('proj-search') || {}).value || '';
        search = search.trim().toLowerCase();

        filteredCards = allCards.filter(function (card) {
            var s  = card.getAttribute('data-status')   || '';
            var l  = card.getAttribute('data-location')  || '';
            var sc = card.getAttribute('data-scope')     || '';
            var ind = card.getAttribute('data-industry') || '';
            var name = (card.querySelector('.title.fs-30') || {}).textContent || '';
            name = name.trim().toLowerCase();

            if (statuses.length   && statuses.indexOf(s)   === -1) return false;
            if (locations.length  && locations.indexOf(l)  === -1) return false;
            if (scopes.length     && scopes.indexOf(sc)    === -1) return false;
            if (industries.length && industries.indexOf(ind)=== -1) return false;
            if (search            && name.indexOf(search)  === -1) return false;
            return true;
        });

        currentPage = 1;
        renderPage();
    }

    // ── Render current page ───────────────────────────────────────────────
    function renderPage() {
        var start = (currentPage - 1) * CARDS_PER_PAGE;
        var end   = start + CARDS_PER_PAGE;
        var pageCards = filteredCards.slice(start, end);
        var totalPages = Math.ceil(filteredCards.length / CARDS_PER_PAGE);

        allCards.forEach(function (c) { c.style.display = 'none'; });
        pageCards.forEach(function (c) { c.style.display = 'inline-block'; });

        var noRes = document.getElementById('proj-no-results');
        if (noRes) noRes.style.display = filteredCards.length === 0 ? 'block' : 'none';

        renderPagination(totalPages);
    }

    // ── Pagination controls ───────────────────────────────────────────────
    function renderPagination(totalPages) {
        var numWrap  = document.getElementById('proj-page-numbers');
        var nextWrap = document.getElementById('proj-next-wrap');
        var paginWrap = document.getElementById('proj-pagination');
        if (!numWrap) return;

        if (paginWrap) paginWrap.style.display = totalPages <= 1 ? 'none' : '';

        numWrap.innerHTML = '';
        for (var i = 1; i <= totalPages; i++) {
            var a = document.createElement('a');
            a.href = '#projects-section';
            a.textContent = i;
            a.className = i === currentPage ? 'active' : '';
            (function (page) {
                a.addEventListener('click', function (e) {
                    e.preventDefault();
                    currentPage = page;
                    renderPage();
                    document.getElementById('projects-section').scrollIntoView({ behavior: 'smooth' });
                });
            })(i);
            numWrap.appendChild(a);
        }

        if (nextWrap) {
            nextWrap.style.display = currentPage >= totalPages ? 'none' : '';
            var nextBtn = document.getElementById('proj-next-btn');
            if (nextBtn) {
                nextBtn.onclick = function (e) {
                    e.preventDefault();
                    if (currentPage < totalPages) {
                        currentPage++;
                        renderPage();
                        document.getElementById('projects-section').scrollIntoView({ behavior: 'smooth' });
                    }
                };
            }
        }
    }

    // ── Clear All Filters ─────────────────────────────────────────────────
    var clearAll = document.querySelector('.clear-all');
    if (clearAll) {
        clearAll.addEventListener('click', function () {
            document.querySelectorAll('.specs-filter input[type="checkbox"]').forEach(function (cb) {
                cb.checked = false;
            });
            var s = document.getElementById('proj-search');
            if (s) s.value = '';
            applyFilters();
        });
    }

    // ── View Results button ───────────────────────────────────────────────
    var refineSubmit = document.getElementById('refine-form-submit');
    if (refineSubmit) {
        refineSubmit.addEventListener('click', function (e) {
            e.preventDefault();
            applyFilters();
            // Close the flyout
            var popup = document.querySelector('.specs-filter');
            if (popup) popup.classList.remove('specs-open-active', 'is-open', 'active');
            document.body.classList.remove('specs-open');
        });
    }

    // Also apply on any checkbox change for live feedback
    document.querySelectorAll('.specs-filter input[type="checkbox"]').forEach(function (cb) {
        cb.addEventListener('change', function () { /* live, triggered on View Results */ });
    });

    // Search input inside flyout
    var searchInput = document.getElementById('proj-search');
    if (searchInput) {
        searchInput.addEventListener('keydown', function (e) {
            if (e.key === 'Enter') { e.preventDefault(); applyFilters(); }
        });
    }

    // ── Init ──────────────────────────────────────────────────────────────
    renderPage();
})();
</script>
</body>'''

html = html.replace('</body>', js, 1)
print("JS added")

path.write_text(html, encoding='utf-8')
print("\n✅ Done.")
