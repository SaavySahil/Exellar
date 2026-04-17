"""
Phase 2 — Rewrite body content for key pages.
Only text/content changes. No class or style changes.
"""
import re

# ─────────────────────────────────────────────────────────────────────────────
# Helper: replace the total-wrapper body in a file
# ─────────────────────────────────────────────────────────────────────────────
def replace_body(filepath, new_body_html):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    tw_start = content.find('<div class="total-wrapper">')
    footer_start = content.find('<footer')
    if tw_start == -1 or footer_start == -1:
        print(f"SKIP {filepath} — markers not found")
        return
    new_content = content[:tw_start] + new_body_html + '\n\n' + content[footer_start:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"[DONE] {filepath}")


# ─────────────────────────────────────────────────────────────────────────────
# 1. LEADERSHIP PAGE
# ─────────────────────────────────────────────────────────────────────────────
LEADERSHIP_BODY = '''<div class="total-wrapper">

<section class="leadership-hero prel ov-hidden blur-overlay">
    <div class="abs-bg bgc img-parallax b-lazy" data-src="images/project-placeholder.jpg"></div>
    <div class="grid-lines">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <div class="leadership-hero-txt">
            <h3 class="section-label white anim-elem top">Who We Are</h3>
            <h1 class="title fs-90 white anim-elem top">Our Leadership</h1>
            <p class="para fs-32 white anim-elem top">Six decades of expertise, guided by a founding family committed to quality, integrity, and lasting relationships.</p>
        </div>
    </div>
</section>

<section class="projects-list-filter prel">
    <div class="executive-leadership leadership-intro">
        <div class="grid-lines gray">
            <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
        </div>
        <div class="wrapper-40pad anim-block executive-flex">
            <div class="exec-big-col inline_block col-d-50 col-t-50 col-m-100 anim-elem top">
                <h2 class="cols-txt title fs-70 black"><span>Founding</span><br>Leadership</h2>
                <p class="cols-txt para fs-23">Exellar Construction LLP is led by the Solanki family — second-generation builders who have grown the company from a small contracting firm into one of Mumbai's most trusted civil construction organisations. Their hands-on involvement in every major project has defined Exellar's culture of accountability and excellence.</p>
            </div>
            <div class="exec-big-col inline_block col-d-50 col-t-50 col-m-100 anim-elem top">
                <div class="exec-profile-holder">
                    <div class="exec-img">
                        <img src="images/project-placeholder.jpg" alt="Abdul Jabbar Solanki">
                    </div>
                    <div class="exec-profile-txt">
                        <h2 class="title fs-30">Abdul Jabbar Solanki</h2>
                        <div class="flex-exec-controls">
                            <div>
                                <p class="para fs-23 black90 person-position">Chairman &amp; Managing Partner</p>
                                <div class="regional-info">
                                    <a href="mailto:info@exellar.co.in" class="para fs-16 mar-top-10 black90 block light">info@exellar.co.in</a>
                                </div>
                            </div>
                            <button class="open-exec-bio">
                                <img src="images/orange-arrow.svg" alt="open more information">
                            </button>
                        </div>
                        <div class="exec-bio-big exec-more-bio">
                            <p>Abdul Jabbar Solanki is the Chairman and Managing Partner of Exellar Construction LLP. Son of the company's founder Haji Idu Solanki, he joined the business in the early 1980s and has led it through its most significant period of growth — transforming a single-contractor operation into a full-service civil construction company active across Mumbai and Pune.<br><br>Under his leadership, Exellar has completed over 150 projects including high-rise residential towers, structural rehabilitation works, and infrastructure development across Maharashtra. Abdul Jabbar is known for his direct involvement on project sites and his insistence on delivering work that stands the test of time.<br><br>He holds deep relationships with Maharashtra's leading developers and has built Exellar's reputation on the principles his father established: trust, quality, and fair dealing.</p>
                        </div>
                        <button class="close-exec-bio">
                            <img src="images/orange-arrow.svg" alt="close">
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="executive-leadership">
        <div class="grid-lines gray">
            <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
        </div>
        <div class="wrapper-40pad anim-block">
            <h2 class="title fs-70 anim-elem top">Directors</h2>
            <div class="f0 anim-block">

                <div class="inline_block col-d-33 col-t-50 col-m-100 v-top anim-elem top">
                    <div class="exec-profile-holder">
                        <div class="exec-img">
                            <img src="images/project-placeholder.jpg" alt="Abdul Gaffar Solanki">
                        </div>
                        <div class="exec-profile-txt">
                            <h2 class="title fs-30">Abdul Gaffar Solanki</h2>
                            <div class="flex-exec-controls">
                                <div>
                                    <p class="para fs-23 black90 person-position">Director — Operations</p>
                                </div>
                                <button class="open-exec-bio">
                                    <img src="images/orange-arrow.svg" alt="open more information">
                                </button>
                            </div>
                            <div class="exec-bio-big exec-more-bio">
                                <p>Abdul Gaffar Solanki oversees all project operations at Exellar Construction LLP. He is responsible for site execution, subcontractor management, and ensuring that every project meets the quality and safety standards the company is known for. With over 30 years of field experience, he brings practical expertise to every project Exellar undertakes.</p>
                            </div>
                            <button class="close-exec-bio">
                                <img src="images/orange-arrow.svg" alt="close">
                            </button>
                        </div>
                    </div>
                </div>

                <div class="inline_block col-d-33 col-t-50 col-m-100 v-top anim-elem top">
                    <div class="exec-profile-holder">
                        <div class="exec-img">
                            <img src="images/project-placeholder.jpg" alt="Abdul Sattar Solanki">
                        </div>
                        <div class="exec-profile-txt">
                            <h2 class="title fs-30">Abdul Sattar Solanki</h2>
                            <div class="flex-exec-controls">
                                <div>
                                    <p class="para fs-23 black90 person-position">Director — Business Development</p>
                                </div>
                                <button class="open-exec-bio">
                                    <img src="images/orange-arrow.svg" alt="open more information">
                                </button>
                            </div>
                            <div class="exec-bio-big exec-more-bio">
                                <p>Abdul Sattar Solanki leads business development and client relationships at Exellar. He has been instrumental in building long-term partnerships with Mumbai's major residential and commercial developers, including Lodha Group, Rustomjee, Omkar Realtors, and Kalpataru. His network and reputation for honest dealing have been central to Exellar's sustained growth.</p>
                            </div>
                            <button class="close-exec-bio">
                                <img src="images/orange-arrow.svg" alt="close">
                            </button>
                        </div>
                    </div>
                </div>

                <div class="inline_block col-d-33 col-t-50 col-m-100 v-top anim-elem top">
                    <div class="exec-profile-holder">
                        <div class="exec-img">
                            <img src="images/project-placeholder.jpg" alt="Abdul Kadar Solanki">
                        </div>
                        <div class="exec-profile-txt">
                            <h2 class="title fs-30">Abdul Kadar Solanki</h2>
                            <div class="flex-exec-controls">
                                <div>
                                    <p class="para fs-23 black90 person-position">Director — Finance &amp; Compliance</p>
                                </div>
                                <button class="open-exec-bio">
                                    <img src="images/orange-arrow.svg" alt="open more information">
                                </button>
                            </div>
                            <div class="exec-bio-big exec-more-bio">
                                <p>Abdul Kadar Solanki manages financial planning, compliance, and internal governance at Exellar. He ensures that the company maintains clean books, timely vendor payments, and full regulatory compliance across all projects. His attention to financial discipline has supported Exellar's ability to take on larger and more complex projects without compromising on delivery commitments.</p>
                            </div>
                            <button class="close-exec-bio">
                                <img src="images/orange-arrow.svg" alt="close">
                            </button>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </div>

    <div class="executive-leadership">
        <div class="grid-lines gray">
            <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
        </div>
        <div class="wrapper-40pad anim-block">
            <h2 class="title fs-70 anim-elem top">Our Founder</h2>
            <div class="office-cols f0 anim-block">
                <div class="inline_block col-d-50 col-t-100 col-m-100 v-top anim-elem left">
                    <div class="img-credit has-credit prel inline_block ov-hidden radius">
                        <span class="img-wrapper img-parallax aspect-ratio-880-688">
                            <img class="b-lazy" width="880" height="688" data-src="images/project-placeholder.jpg" src="" alt="Haji Idu Solanki">
                        </span>
                    </div>
                </div>
                <div class="office-txt-col inline_block col-d-50 col-t-100 col-m-100 vm">
                    <h2 class="section-label anim-elem left">Est. 1964</h2>
                    <h3 class="title fs-70 anim-elem left">Haji Idu Solanki</h3>
                    <p class="para fs-32 anim-elem left">Haji Idu Solanki founded BuildTech Engineering Services in 1964 with nothing more than a strong work ethic, deep knowledge of construction, and an unshakeable commitment to delivering what he promised. Over the following decades, he built the company's reputation one project at a time — earning the trust of Mumbai's builders and developers through quality work and honest dealing. That foundation is what Exellar Construction LLP stands on today.</p>
                    <a href="About-us.html" class="btn-link anim-elem left">Our Story <img aria-hidden="true" src="images/btn-arrow.svg" alt="arrow"></a>
                </div>
            </div>
        </div>
    </div>

</section>

</div>'''

replace_body('Leadship.html', LEADERSHIP_BODY)


# ─────────────────────────────────────────────────────────────────────────────
# 2. LIFE AT COMPANY
# ─────────────────────────────────────────────────────────────────────────────
LIFE_BODY = '''<div class="total-wrapper">

<section class="commitments-hero prel ov-hidden blur-overlay">
    <div class="abs-bg bgc img-parallax b-lazy" data-src="images/project-placeholder.jpg"></div>
    <div class="wrapper-1419">
        <div class="commitment-hero-txt anim-block">
            <h2 class="section-label white anim-elem top">Life At Exellar</h2>
            <h1 class="title fs-90 white hero-title commitments anim-elem top">
                <strong>Ambitious People. Lasting Structures.</strong>
            </h1>
            <p class="para fs-32 white anim-elem top delay-01">At Exellar, you work alongside people who take their craft seriously — on projects that shape the skylines of Mumbai and Pune.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-70 black anim-elem">A place where your work is <strong>visible, valued, and lasting.</strong></h2>
        <div class="two-col-txt anim-elem">
            <p class="para fs-32 black">Construction is not a desk job. At Exellar, your work is physical, real, and permanent. The buildings you help build will stand for decades. The relationships you build with your team will last just as long. We are a company of approximately 50 dedicated professionals who work closely together, learn from each other, and take ownership of what we deliver.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-50 black anim-elem top"><strong>Growth From Day One</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">Whether you are a junior engineer stepping onto your first site or a seasoned foreman managing a full crew, Exellar gives you real responsibility from the start. Our team members are trusted with meaningful work — not paperwork. Site managers, engineers, and supervisors all report directly to leadership, which means decisions are fast and learning is constant.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-50 black anim-elem top"><strong>The Exellar Way</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">We believe in showing up, doing the work, and doing it right. Our culture is straightforward: if you deliver quality, you are respected. If you spot a problem, you raise it. If you need support, you ask for it. There is no hierarchy of silence at Exellar — leadership walks the site, knows your name, and values your input.</p>
        </div>
    </div>
</section>

<section class="home-office life-at-turner prel">
    <div class="width-960"></div>
    <div class="home-wrapper w2100">
        <div class="office-cols f0 anim-block">
            <div class="inline_block col-d-50 col-t-50 col-m-100 vm anim-elem left">
                <div class="img-credit has-credit prel inline_block ov-hidden radius">
                    <img class="radius w-100 b-lazy img-parallax" data-src="images/project-placeholder.jpg" src="" alt="Life at Exellar Construction">
                    <span class="credit-txt"></span>
                </div>
            </div>
            <div class="office-txt-col inline_block col-d-50 col-t-50 col-m-100 vm">
                <h2 class="section-label anim-elem left">Join The Team</h2>
                <h3 class="title fs-70 anim-elem left">Build Your Future With Exellar</h3>
                <p class="para fs-32 anim-elem left life-at-turner-para">We are always looking for committed engineers, site supervisors, skilled tradespeople, and construction professionals who want to do meaningful work on real projects across Maharashtra.</p>
                <a href="Careers.html" class="btn-link anim-elem left">Explore Opportunities <img aria-hidden="true" src="images/btn-arrow.svg" alt="arrow"></a>
            </div>
        </div>
    </div>
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
</section>

</div>'''

replace_body('Life at Company.html', LIFE_BODY)


# ─────────────────────────────────────────────────────────────────────────────
# 3. INSIGHTS PAGE — replace Turner news with Exellar news
# ─────────────────────────────────────────────────────────────────────────────
with open('insights.html', 'r', encoding='utf-8', errors='replace') as f:
    insights = f.read()

# Replace Turner insight news article links in the megamenu mobile nav
insights = insights.replace(
    'Walsh-Turner Joint Venture Completes New $1.5 Billion Ohio State University Hospital',
    'Exellar Completes Structural Rehabilitation of Rustomjee Urbania, Vikhroli'
)
insights = insights.replace(
    'Turner to Begin Work on $224 Million Northern Chautauqua Hospital',
    'Exellar Breaks Ground on New High-Rise Residential Tower in Andheri, Mumbai'
)
insights = insights.replace(
    'Johns Hopkins and Turner-Mahogany Joint Venture Celebrate Topping Out of Henrietta Lacks Building',
    'Exellar Delivers Waterproofing & Rehabilitation for Kalpataru Society, Pune'
)

with open('insights.html', 'w', encoding='utf-8') as f:
    f.write(insights)
print("[DONE] insights.html — nav news updated")


# ─────────────────────────────────────────────────────────────────────────────
# 4. INNOVATION PAGE — replace Turner innovation content
# ─────────────────────────────────────────────────────────────────────────────
with open('innovation.html', 'r', encoding='utf-8', errors='replace') as f:
    innov = f.read()

tw = innov.find('<div class="total-wrapper">')
footer = innov.find('<footer')

INNOV_BODY = '''<div class="total-wrapper">

<section class="commitments-hero prel ov-hidden blur-overlay">
    <div class="abs-bg bgc img-parallax b-lazy" data-src="images/project-placeholder.jpg"></div>
    <div class="wrapper-1419">
        <div class="commitment-hero-txt anim-block">
            <h2 class="section-label white anim-elem top">Our Commitments</h2>
            <h1 class="title fs-90 white hero-title commitments anim-elem top">
                <strong>Innovation</strong>
            </h1>
            <p class="para fs-32 white anim-elem top delay-01">Applying better methods, smarter planning, and emerging technologies to deliver projects with greater precision and less waste.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-70 black anim-elem">Innovation at Exellar means doing the <strong>right thing better</strong> — every time.</h2>
        <div class="two-col-txt anim-elem">
            <p class="para fs-32 black">We are not a technology company. We are builders — and our innovation is rooted in construction. Over six decades, Exellar has refined its methods for high-rise construction, structural rehabilitation, and waterproofing. We invest in better planning tools, adopt modern structural analysis techniques, and train our teams in the latest industry practices to ensure every project benefits from the best available approach.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>Better Planning, Better Outcomes</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">Exellar uses modern project planning tools and scheduling software to ensure accurate timelines, efficient resource allocation, and early identification of risks. Our pre-construction planning process has significantly reduced on-site delays and cost overruns across our project portfolio.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>Modern Structural Techniques</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">Our rehabilitation and structural strengthening works use the latest IS-code compliant techniques including fibre-reinforced polymer (FRP) wrapping, micro-concrete overlays, and epoxy injection systems. These methods extend building life while minimising disruption to occupants — an increasingly important requirement in Mumbai's dense urban environment.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>Continuous Team Training</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">We invest in our people by providing regular technical training, safety awareness programmes, and exposure to new construction methodologies. Our site supervisors and engineers are encouraged to stay current with industry developments — and their learning directly improves the quality of work on every Exellar project.</p>
        </div>
    </div>
</section>

</div>'''

innov_new = innov[:tw] + INNOV_BODY + '\n\n' + innov[footer:]
with open('innovation.html', 'w', encoding='utf-8') as f:
    f.write(innov_new)
print("[DONE] innovation.html")


# ─────────────────────────────────────────────────────────────────────────────
# 5. SAFETY & WELLNESS
# ─────────────────────────────────────────────────────────────────────────────
with open('safety-and-wellness.html', 'r', encoding='utf-8', errors='replace') as f:
    safety = f.read()
tw = safety.find('<div class="total-wrapper">')
footer = safety.find('<footer')

SAFETY_BODY = '''<div class="total-wrapper">

<section class="commitments-hero prel ov-hidden blur-overlay">
    <div class="abs-bg bgc img-parallax b-lazy" data-src="images/project-placeholder.jpg"></div>
    <div class="wrapper-1419">
        <div class="commitment-hero-txt anim-block">
            <h2 class="section-label white anim-elem top">Our Commitments</h2>
            <h1 class="title fs-90 white hero-title commitments anim-elem top">
                <strong>Safety &amp; Wellness</strong>
            </h1>
            <p class="para fs-32 white anim-elem top delay-01">Every Exellar employee goes home safe. That is not a target — it is our standard.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-70 black anim-elem">Safety is the <strong>first conversation</strong> on every Exellar site.</h2>
        <div class="two-col-txt anim-elem">
            <p class="para fs-32 black">Construction is inherently demanding work. We take that responsibility seriously. Exellar maintains rigorous safety protocols across all project sites in Mumbai and Pune — from daily toolbox talks and PPE compliance checks to structured emergency response planning. Our goal is zero incidents, and we work toward that goal every single day.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>Site Safety Standards</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">All Exellar project sites operate under a mandatory safety framework that includes daily site inspections, mandatory PPE for all workers, height safety protocols, scaffolding certification, and regular equipment checks. Safety officers are present on all active sites and have full authority to halt work if standards are not met.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>Worker Welfare</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">We provide all site workers with access to clean drinking water, rest facilities, first-aid kits, and site medical support. Labour welfare is not a compliance checkbox for us — it is a reflection of how we value the people who build our projects. Timely wage payment, fair treatment, and a respectful work environment are non-negotiable at Exellar.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>Training &amp; Awareness</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">New workers receive mandatory safety induction before stepping onto any Exellar site. Regular toolbox talks — conducted in local languages — keep safety top of mind throughout the project. Supervisors are trained in emergency response, and first-aid-certified personnel are maintained on all active sites.</p>
        </div>
    </div>
</section>

</div>'''

safety_new = safety[:tw] + SAFETY_BODY + '\n\n' + safety[footer:]
with open('safety-and-wellness.html', 'w', encoding='utf-8') as f:
    f.write(safety_new)
print("[DONE] safety-and-wellness.html")


# ─────────────────────────────────────────────────────────────────────────────
# 6. ENVIRONMENTAL SUSTAINABILITY
# ─────────────────────────────────────────────────────────────────────────────
with open('environmental-sustainability-and-resiliency.html', 'r', encoding='utf-8', errors='replace') as f:
    env = f.read()
tw = env.find('<div class="total-wrapper">')
footer = env.find('<footer')

ENV_BODY = '''<div class="total-wrapper">

<section class="commitments-hero prel ov-hidden blur-overlay">
    <div class="abs-bg bgc img-parallax b-lazy" data-src="images/project-placeholder.jpg"></div>
    <div class="wrapper-1419">
        <div class="commitment-hero-txt anim-block">
            <h2 class="section-label white anim-elem top">Our Commitments</h2>
            <h1 class="title fs-90 white hero-title commitments anim-elem top">
                <strong>Environmental Sustainability</strong>
            </h1>
            <p class="para fs-32 white anim-elem top delay-01">Building responsibly — reducing waste, conserving resources, and protecting the communities we work in.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-70 black anim-elem">We build for today <strong>without compromising</strong> tomorrow.</h2>
        <div class="two-col-txt anim-elem">
            <p class="para fs-32 black">Environmental responsibility is embedded in how Exellar plans and executes every project. From minimising construction waste to managing water runoff and controlling dust on urban sites, we take a practical, disciplined approach to reducing our environmental footprint — one that respects the neighbourhoods and communities our projects are located in.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>Waste Reduction</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">We plan material quantities carefully at the pre-construction stage to avoid over-ordering and reduce waste. Excavated soil is reused where possible within the site. Concrete debris from demolition or rehabilitation works is properly segregated and disposed of through licensed waste contractors in compliance with Maharashtra Pollution Control Board regulations.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>Urban Site Management</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">Most of our projects are located in dense urban areas of Mumbai and Pune, often adjacent to occupied residential buildings. We take extra care to control dust, noise, and vibration — and we schedule high-impact work to avoid peak hours wherever possible. Hoarding and barricading are maintained to protect pedestrians and neighbouring properties throughout construction.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>Sustainable Rehabilitation</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">Rehabilitation and structural strengthening — two of Exellar's core service areas — are inherently sustainable activities. By extending the life of existing buildings, we help reduce the environmental cost of new construction. Every building we repair is one fewer building that needs to be demolished and rebuilt — saving materials, energy, and landfill capacity.</p>
        </div>
    </div>
</section>

</div>'''

env_new = env[:tw] + ENV_BODY + '\n\n' + env[footer:]
with open('environmental-sustainability-and-resiliency.html', 'w', encoding='utf-8') as f:
    f.write(env_new)
print("[DONE] environmental-sustainability-and-resiliency.html")


# ─────────────────────────────────────────────────────────────────────────────
# 7. ETHICS & COMPLIANCE
# ─────────────────────────────────────────────────────────────────────────────
with open('ethics-and-compliance.html', 'r', encoding='utf-8', errors='replace') as f:
    ethics = f.read()
tw = ethics.find('<div class="total-wrapper">')
footer = ethics.find('<footer')

ETHICS_BODY = '''<div class="total-wrapper">

<section class="commitments-hero prel ov-hidden blur-overlay">
    <div class="abs-bg bgc img-parallax b-lazy" data-src="images/project-placeholder.jpg"></div>
    <div class="wrapper-1419">
        <div class="commitment-hero-txt anim-block">
            <h2 class="section-label white anim-elem top">Our Commitments</h2>
            <h1 class="title fs-90 white hero-title commitments anim-elem top">
                <strong>Ethics &amp; Compliance</strong>
            </h1>
            <p class="para fs-32 white anim-elem top delay-01">We do business the right way — with transparency, accountability, and respect for every person we work with.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-70 black anim-elem">Our unwavering commitment to <strong>doing what is right</strong> is the foundation of everything we build.</h2>
        <div class="two-col-txt anim-elem">
            <p class="para fs-32 black">Exellar Construction LLP has built its reputation over six decades by being straightforward and honest — with clients, subcontractors, vendors, and the communities we work in. Our ethical standards are not a compliance document written for a regulator. They are the operating principles that guide every decision made at every level of the company.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>Fair Dealing With All Parties</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">We pay our subcontractors and vendors on time, every time. We provide transparent billing to our clients — with clear breakdowns of work done, materials used, and costs incurred. We do not engage in price manipulation, bid rigging, or any form of corrupt practice. Our word is our bond, and our contracts reflect that.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>Zero Tolerance for Misconduct</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">Exellar maintains a zero-tolerance policy for workplace misconduct, discrimination, harassment, and exploitation. This applies to every person on our sites — full-time employees, contract workers, and visiting consultants. Any concern can be raised directly with leadership or through our confidential reporting channel at ethics@exellar.co.in.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>Regulatory Compliance</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">We operate in full compliance with all applicable laws and regulations, including Maharashtra labour laws, RERA requirements for residential projects, GST obligations, and MPCB environmental standards. Our finance and compliance function, led by Director Abdul Kadar Solanki, ensures that all statutory filings and regulatory requirements are met without exception.</p>
        </div>
    </div>
</section>

</div>'''

ethics_new = ethics[:tw] + ETHICS_BODY + '\n\n' + ethics[footer:]
with open('ethics-and-compliance.html', 'w', encoding='utf-8') as f:
    f.write(ethics_new)
print("[DONE] ethics-and-compliance.html")


# ─────────────────────────────────────────────────────────────────────────────
# 8. FRAUD ALERT
# ─────────────────────────────────────────────────────────────────────────────
with open('Fruad-alert.html', 'r', encoding='utf-8', errors='replace') as f:
    fraud = f.read()
tw = fraud.find('<div class="total-wrapper">')
footer = fraud.find('<footer')

FRAUD_BODY = '''<div class="total-wrapper">

<section class="team-directory-hero prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 team-hero-wrapper">
        <div class="col-d-50 col-t-100 col-m-100">
            <h2 class="section-label">Important Notice</h2>
            <h1 class="title fs-110">Fraud Alert</h1>
        </div>
        <div class="team-hero-para col-d-50 col-t-100 col-m-100">
            <p class="para fs-32">Exellar Construction LLP is aware of fraudulent job offers and business solicitations being made using our company name. Please read this notice carefully.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-70 black anim-elem">Protecting Our Name &amp; <strong>Your Safety</strong></h2>
        <div class="two-col-txt anim-elem">
            <p class="para fs-32 black">Exellar Construction LLP has become aware of fraudulent activities in which individuals or groups are misrepresenting themselves as Exellar representatives to solicit money, personal information, or advance payments from job seekers and business contacts. We take this seriously and want to help you identify and avoid these scams.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>How to Identify a Scam</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">Exellar Construction LLP will never ask job applicants or vendors to pay any fees, deposits, or charges as part of a hiring or onboarding process. We will never request your Aadhaar, PAN, or bank account information over WhatsApp or email without a formal process. All legitimate communication from Exellar comes from @exellar.co.in email addresses only.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>Report a Fraud Attempt</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">If you have received a suspicious communication claiming to be from Exellar Construction LLP, please report it immediately to our team at info@exellar.co.in. Include any messages, names, or contact details you received. We also encourage you to report the incident to your local police cyber crime cell.</p>
        </div>
    </div>
</section>

</div>'''

fraud_new = fraud[:tw] + FRAUD_BODY + '\n\n' + fraud[footer:]
with open('Fruad-alert.html', 'w', encoding='utf-8') as f:
    f.write(fraud_new)
print("[DONE] Fruad-alert.html")


# ─────────────────────────────────────────────────────────────────────────────
# 9. PRIVACY POLICY
# ─────────────────────────────────────────────────────────────────────────────
with open('Privacy Policy.html', 'r', encoding='utf-8', errors='replace') as f:
    priv = f.read()
tw = priv.find('<div class="total-wrapper">')
footer = priv.find('<footer')

PRIV_BODY = '''<div class="total-wrapper">

<section class="team-directory-hero prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 team-hero-wrapper">
        <div class="col-d-50 col-t-100 col-m-100">
            <h2 class="section-label">Legal</h2>
            <h1 class="title fs-110">Privacy Policy</h1>
        </div>
        <div class="team-hero-para col-d-50 col-t-100 col-m-100">
            <p class="para fs-32">Exellar Construction LLP respects your privacy and is committed to protecting the personal information you share with us.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>Information We Collect</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">When you contact us through our website, apply for a job, or engage with us as a vendor or client, we may collect your name, email address, phone number, and details relevant to your inquiry. We do not collect sensitive personal information unless it is necessary for the purpose you have engaged with us for.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>How We Use Your Information</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">Information you provide is used solely to respond to your inquiry, process your job application, or manage our professional relationship with you. We do not sell, share, or rent your personal information to third parties. We may share information with our internal teams or professional advisors where required to fulfil your request.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>Cookies &amp; Website Analytics</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">Our website may use cookies and analytics tools to understand how visitors interact with our pages. This data is aggregated and anonymous — it is used only to improve our website and does not identify individual users. You can disable cookies in your browser settings at any time.</p>
        </div>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h2 class="title fs-45 black anim-elem top"><strong>Your Rights &amp; Contact</strong></h2>
        <div class="two-col-txt anim-elem top">
            <p class="para fs-32 black">You have the right to request access to, correction of, or deletion of any personal information we hold about you. To exercise these rights or if you have any questions about this policy, please contact us at info@exellar.co.in. This policy was last updated in April 2026.</p>
        </div>
    </div>
</section>

</div>'''

priv_new = priv[:tw] + PRIV_BODY + '\n\n' + priv[footer:]
with open('Privacy Policy.html', 'w', encoding='utf-8') as f:
    f.write(priv_new)
print("[DONE] Privacy Policy.html")

print("\nPhase 2 complete.")
EOF
