with open('innovation.html', 'r', encoding='utf-8', errors='replace') as f:
    full = f.read()

tw_pos = full.find('<div class="total-wrapper">')
footer_pos = full.find('<footer')
after_footer = full.find('</footer>') + len('</footer>')

NAV_HEADER = full[:tw_pos]
FOOTER = full[footer_pos:after_footer]
PAGE_TAIL = full[after_footer:]

pages = [
    {
        'file': 'market-sectors.html',
        'title': 'Market Sectors | Exellar Construction LLP',
        'hero_label': 'Our Expertise',
        'hero_title': 'Market Sectors',
        'hero_sub': 'Delivering specialized construction across the sectors that matter most to Mumbai and Pune.',
        'intro': 'Exellar Construction LLP brings focused expertise to the sectors that drive urban growth in Maharashtra. From high-rise residential towers to institutional buildings and infrastructure rehabilitation, our teams understand the unique requirements of each market we serve.',
        'sections': [
            ('Residential', 'We build premium and affordable high-rise residential projects across Mumbai and Pune. Our track record spans townships, standalone towers, and gated communities delivering quality finishes on schedule.'),
            ('Commercial & Institutional', 'Office complexes, educational institutions, hospitals, and government buildings require precision, compliance, and long-term durability. Exellar brings both to every commercial and institutional project.'),
            ('Rehabilitation & Repair', "Mumbai's aging building stock demands specialists. Our rehabilitation division handles structural repairs, concrete restoration, and waterproofing for residential societies, commercial structures, and public infrastructure."),
            ('Infrastructure Works', 'From podium decks and basements to compound walls, roads, and drainage systems we manage the complete infrastructure scope within large development projects.'),
        ]
    },
    {
        'file': 'affiliates.html',
        'title': 'Affiliates | Exellar Construction LLP',
        'hero_label': 'Our Network',
        'hero_title': 'Affiliates',
        'hero_sub': 'Trusted partners and associates that strengthen every project we deliver.',
        'intro': 'Exellar Construction LLP works with a carefully selected network of specialist subcontractors, vendors, and technical consultants across Maharashtra. Our affiliate relationships are built on shared values: quality workmanship, timely delivery, and transparent communication.',
        'sections': [
            ('Structural Consultants', 'We collaborate with experienced structural engineering firms for design review, load calculations, and site supervision ensuring every structure meets IS code requirements and client expectations.'),
            ('MEP Partners', 'Mechanical, electrical, and plumbing works are executed through vetted specialist firms who integrate seamlessly with our civil teams to deliver complete, ready-to-occupy buildings.'),
            ('Material Suppliers', 'Exellar maintains long-standing relationships with certified material suppliers for cement, steel, aggregates, waterproofing membranes, and finishing materials ensuring consistent quality across all projects.'),
            ('Safety & Environment Consultants', 'Dedicated safety and environmental compliance consultants support our sites, maintaining regulatory standards and promoting a safe working culture across all project locations.'),
        ]
    },
    {
        'file': 'locations.html',
        'title': 'Our Locations | Exellar Construction LLP',
        'hero_label': 'Where We Are',
        'hero_title': 'Our Locations',
        'hero_sub': 'Rooted in Mumbai. Growing across Pune. Serving Maharashtra.',
        'intro': 'Exellar Construction LLP operates from its headquarters in Mumbai with an active project presence in Pune. Our teams are embedded in both cities, enabling us to respond quickly, maintain site supervision standards, and build lasting relationships with local clients and communities.',
        'sections': [
            ('Mumbai - Head Office', 'Our registered office and primary operations hub is located in Mumbai, Maharashtra. Mumbai is the core of our business where we have delivered high-rise construction, rehabilitation, and waterproofing projects for over six decades. For inquiries: info@exellar.co.in'),
            ('Pune - Project Operations', "Exellar's growing presence in Pune reflects the city's booming real estate and infrastructure development. Our Pune-based teams manage projects across the city's expanding residential and commercial belts."),
            ('Active Site Locations', 'Our project teams are currently active across Andheri, Oshiwara, Vikhroli, Juinagar, and Khargar in Mumbai, with additional sites in Pune. Site offices operate with dedicated project managers and safety officers.'),
            ('Reach Us', 'Whether you are a developer, society, or institution looking for a reliable civil contractor in Mumbai or Pune we are close by. Reach out at info@exellar.co.in or visit our Contact page to get in touch.'),
        ]
    },
    {
        'file': 'our-esg-strategy.html',
        'title': 'Our ESG Strategy | Exellar Construction LLP',
        'hero_label': 'Responsibility',
        'hero_title': 'Our ESG Strategy',
        'hero_sub': 'Building responsibly for our people, our communities, and the environment.',
        'intro': 'At Exellar Construction LLP, our approach to Environmental, Social, and Governance (ESG) principles is practical and people-first. We believe that responsible construction is good construction and we embed these principles into every project we take on.',
        'sections': [
            ('Environmental', 'We minimize construction waste through careful material planning, reuse of excavated soil, and proper disposal of debris. On sites where feasible, we incorporate green building practices and energy-efficient construction techniques aligned with IGBC and BIS guidelines.'),
            ('Social', 'Our workforce is our greatest asset. Exellar employs local labor, provides safety training, and ensures timely wage payments. We are committed to maintaining safe, respectful, and inclusive worksites across all our projects.'),
            ('Governance', 'Exellar operates with full transparency with our clients, consultants, and subcontractors. We follow documented processes for procurement, billing, and project reporting and we hold ourselves accountable to the highest standards of professional conduct.'),
            ('Community Impact', 'Our projects contribute to housing availability, infrastructure improvement, and local employment in Mumbai and Pune creating lasting value beyond the structure itself.'),
        ]
    },
    {
        'file': 'community-citizenship.html',
        'title': 'Community and Citizenship | Exellar Construction LLP',
        'hero_label': 'Our Community',
        'hero_title': 'Community & Citizenship',
        'hero_sub': 'We build more than structures. We invest in the communities we serve.',
        'intro': 'Exellar Construction LLP has been part of the Mumbai and Pune community for over six decades. Our commitment to responsible business goes beyond contracts and timelines. It includes how we treat our workers, how we engage with local communities, and how we contribute to the neighbourhoods our projects call home.',
        'sections': [
            ('Local Employment', 'We prioritize hiring skilled and unskilled workers from the communities surrounding our project sites. This ensures that the economic benefit of construction flows to local families and households.'),
            ('Worker Welfare', 'Our sites maintain safe, clean, and respectful working environments. Workers receive timely wages, appropriate safety equipment, and basic welfare facilities including clean drinking water, rest areas, and site medical support.'),
            ('Giving Back', 'Senior members of our leadership team actively participate in community initiatives related to housing rights, construction safety awareness, and vocational training programs for youth entering the construction trades.'),
            ('Ethical Practices', 'We maintain zero tolerance for exploitation, discrimination, or unsafe working conditions. Our internal code of conduct applies to every person on our sites including employees, subcontractors, and vendors alike.'),
        ]
    },
    {
        'file': 'diversity-equity-inclusion.html',
        'title': 'Diversity, Equity, and Inclusion | Exellar Construction LLP',
        'hero_label': 'Our People',
        'hero_title': 'Diversity, Equity & Inclusion',
        'hero_sub': 'A stronger team is a more diverse team. We build both.',
        'intro': 'Exellar Construction LLP believes that our workforce should reflect the diversity of the communities we serve. We are committed to creating an environment where every employee regardless of gender, religion, caste, or background can contribute meaningfully, grow professionally, and feel valued.',
        'sections': [
            ('Equal Opportunity', 'We hire on the basis of skill, attitude, and potential. All open roles at Exellar are filled based on merit, and we actively encourage applications from candidates of all backgrounds including women in construction.'),
            ('Inclusive Worksites', 'Our project sites are governed by a clear code of conduct that prohibits discrimination, harassment, and bias of any kind. Grievance mechanisms are available to all site workers and are taken seriously by our management team.'),
            ('Representation in Leadership', 'We are working to build a leadership pipeline that reflects diverse perspectives. Our next generation of project managers, site engineers, and supervisors comes from a wide range of academic and cultural backgrounds.'),
            ('Supplier Diversity', 'We give fair consideration to women-owned businesses, minority-owned enterprises, and small local contractors when selecting subcontractors and material suppliers for our projects.'),
        ]
    },
]


def build_page(p):
    sections_html = ''
    for heading, body in p['sections']:
        sections_html += f'''
<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-50 black anim-elem top"><strong>{heading}</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">{body}</p>
        </div>
    </div>
</section>
'''

    page_content = f'''<div class="total-wrapper">
    <section class="commitments-hero prel ov-hidden blur-overlay">
        <div class="abs-bg bgc img-parallax b-lazy" data-src="images/project-placeholder.jpg"></div>
        <div class="wrapper-1419">
            <div class="commitment-hero-txt anim-block">
                <h2 class="section-label white anim-elem top">{p["hero_label"]}</h2>
                <h1 class="title fs-90 white hero-title commitments anim-elem top">
                    <strong>{p["hero_title"]}</strong>
                </h1>
                <p class="para fs-32 white anim-elem top delay-01">{p["hero_sub"]}</p>
            </div>
        </div>
    </section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-70 black anim-elem">{p["intro"]}</h2>
    </div>
</section>

{sections_html}

</div>
'''

    header = NAV_HEADER.replace(
        '<title>Innovation | Turner Construction Company</title>',
        f'<title>{p["title"]}</title>'
    )

    return header + page_content + '\n\n' + FOOTER + PAGE_TAIL


for p in pages:
    html = build_page(p)
    with open(p['file'], 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created: {p['file']}")

print("Done!")
