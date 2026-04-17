"""
Rewrite body content of the 4 service detail pages for Exellar Construction LLP.
Replaces everything between the contact-popup close and </footer> with fresh Exellar content.
All classes are taken from Turner's existing CSS only.
"""
import re

# ── Helper: replace content between first <section (page body) and </footer ──
def replace_body(filepath, new_body):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    # Find first <section that appears after the contact-popup block
    contact_popup_end = content.rfind('</div>', 0, content.find('<section'))
    section_start = content.find('<section', content.find('contact-popup'))
    footer_start  = content.rfind('<footer')
    if section_start == -1 or footer_start == -1:
        print(f'[SKIP] {filepath} — markers not found')
        return
    new_content = content[:section_start] + new_body + '\n' + content[footer_start:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f'[DONE] {filepath}')


# ══════════════════════════════════════════════════════════════════════════════
# 1. construction-management.html
# ══════════════════════════════════════════════════════════════════════════════
cm_body = """
<section class="team-directory-hero prel ov-hidden">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 team-hero-wrapper anim-block">
        <div class="col-d-50 col-t-100 col-m-100">
            <h1 class="title fs-110 anim-elem top">Construction Management</h1>
        </div>
        <div class="team-hero-para col-d-50 col-t-100 col-m-100">
            <p class="para fs-32 anim-elem top">Exellar Construction LLP delivers end-to-end construction management services — from project inception to final handover — with precision, accountability, and a relentless focus on quality.</p>
        </div>
    </div>
</section>

<section class="img-txt-block-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-40pad f0 anim-block">
        <div class="img-txt-img-right inline_block col-d-50 col-t-100 col-m-100 vm anim-elem top">
            <div class="img-credit prel inline_block radius ov-hidden">
                <div class="video-holder prel ov-hidden radius">
                    <img class="w-100 b-lazy img-parallax" data-src="images/project-placeholder.jpg" alt="Construction Management">
                </div>
            </div>
        </div>
        <div class="img-txt-txt inline_block col-d-50 col-t-100 col-m-100 vm anim-elem top">
            <h3 class="title fs-45">Your single point of responsibility</h3>
            <p class="para fs-23">We act as your owner's representative and on-site construction manager — coordinating contractors, subcontractors, consultants, and material suppliers under a single umbrella of accountability.<br><br>With Exellar as your CM partner, you receive transparent reporting, strict cost controls, and a dedicated project team that treats your project as our own.</p>
        </div>
    </div>
</section>

<section class="careers-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h3 class="title fs-90 anim-elem top">Proven expertise to navigate complex projects with confidence</h3>
        <p class="para fs-32 anim-elem top">Every project presents unique risks. Our seasoned construction managers bring decades of hands-on experience in high-rise residential, commercial, and infrastructure works across Maharashtra — giving you the confidence to make critical decisions backed by real-world data.</p>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <div class="col-d-50 col-t-100 col-m-100 anim-elem top">
            <h3 class="title fs-70">Our CM capabilities</h3>
        </div>
        <div class="col-d-50 col-t-100 col-m-100 anim-elem top">
            <p class="para fs-32">From pre-design planning through commissioning, our construction management practice covers every phase of the project lifecycle.</p>
        </div>
    </div>
    <div class="wrapper-1419 anim-block" style="">
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Cost Management</h4>
            <p class="para fs-23">Detailed BOQ preparation, value engineering, and real-time cost tracking to keep projects within budget.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Schedule Control</h4>
            <p class="para fs-23">Baseline scheduling, look-ahead planning, and critical-path monitoring to ensure on-time delivery.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Quality Assurance</h4>
            <p class="para fs-23">Site inspections, material testing, and non-conformance management aligned with IS codes and client specifications.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Subcontractor Coordination</h4>
            <p class="para fs-23">End-to-end procurement, evaluation, and management of trade contractors and specialist vendors.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Safety Management</h4>
            <p class="para fs-23">Site-specific safety plans, daily toolbox talks, and zero-tolerance enforcement of HSE standards.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Reporting & Handover</h4>
            <p class="para fs-23">Weekly progress reports, photographic documentation, and punch-list driven project close-outs.</p>
        </div>
    </div>
</section>

<section class="careers-type-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h3 class="title fs-70 anim-elem top">Delivery methods we support</h3>
    </div>
    <div class="careers-type-slider-wrap">
        <div class="swiper careers-type-slider">
            <div class="swiper-wrapper">
                <div class="swiper-slide">
                    <div class="careers-type-txt anim-elem top">
                        <h3 class="title fs-45 anim-elem top">Design-Build</h3>
                        <p class="para fs-23 anim-elem top">We integrate design and construction under one contract, reducing interface risk and accelerating delivery timelines for clients who need certainty.</p>
                    </div>
                </div>
                <div class="swiper-slide">
                    <div class="careers-type-txt anim-elem top">
                        <h3 class="title fs-45 anim-elem top">CM at Risk</h3>
                        <p class="para fs-23 anim-elem top">We assume construction risk while providing early cost certainty through a Guaranteed Maximum Price — giving owners financial predictability from day one.</p>
                    </div>
                </div>
                <div class="swiper-slide">
                    <div class="careers-type-txt anim-elem top">
                        <h3 class="title fs-45 anim-elem top">Traditional (Item Rate)</h3>
                        <p class="para fs-23 anim-elem top">For public sector and institutional clients, we execute item-rate contracts with full compliance to tender conditions, BOQ adherence, and regulatory requirements.</p>
                    </div>
                </div>
                <div class="swiper-slide">
                    <div class="careers-type-txt anim-elem top">
                        <h3 class="title fs-45 anim-elem top">EPC Contracts</h3>
                        <p class="para fs-23 anim-elem top">We deliver Engineering, Procurement, and Construction contracts for infrastructure and industrial clients requiring complete turnkey solutions.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
"""

replace_body('construction-management.html', cm_body)


# ══════════════════════════════════════════════════════════════════════════════
# 2. preconstruction.html
# ══════════════════════════════════════════════════════════════════════════════
pre_body = """
<section class="team-directory-hero prel ov-hidden">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 team-hero-wrapper anim-block">
        <div class="col-d-50 col-t-100 col-m-100">
            <h1 class="title fs-110 anim-elem top">Preconstruction</h1>
        </div>
        <div class="team-hero-para col-d-50 col-t-100 col-m-100">
            <p class="para fs-32 anim-elem top">Getting the details right before breaking ground is the most important investment you can make. Exellar's preconstruction services give you accurate cost forecasts, constructability reviews, and schedule confidence — before a single rupee is committed to construction.</p>
        </div>
    </div>
</section>

<section class="img-txt-block-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-40pad f0 anim-block">
        <div class="img-txt-img-right inline_block col-d-50 col-t-100 col-m-100 vm anim-elem top">
            <div class="img-credit prel inline_block radius ov-hidden">
                <div class="video-holder prel ov-hidden radius">
                    <img class="w-100 b-lazy img-parallax" data-src="images/project-placeholder.jpg" alt="Preconstruction Planning">
                </div>
            </div>
        </div>
        <div class="img-txt-txt inline_block col-d-50 col-t-100 col-m-100 vm anim-elem top">
            <h3 class="title fs-45">Plan precisely. Build confidently.</h3>
            <p class="para fs-23">Our preconstruction team works hand-in-hand with architects, structural consultants, and owners during the design phase to identify risks early, optimise scope, and produce reliable budgets that hold through construction.<br><br>We bring market intelligence, subcontractor relationships, and decades of site experience to every preconstruction engagement.</p>
        </div>
    </div>
</section>

<section class="careers-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h3 class="title fs-90 anim-elem top">Reduce risk before the first brick is laid</h3>
        <p class="para fs-32 anim-elem top">The majority of construction cost and schedule risk is determined during the design phase. Our preconstruction engagement allows clients to make informed go/no-go decisions, optimise design for buildability, and lock in competitive pricing — all before mobilisation begins.</p>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <div class="col-d-50 col-t-100 col-m-100 anim-elem top">
            <h3 class="title fs-70">Preconstruction services</h3>
        </div>
        <div class="col-d-50 col-t-100 col-m-100 anim-elem top">
            <p class="para fs-32">We offer a comprehensive suite of preconstruction services tailored to the complexity and scale of each project.</p>
        </div>
    </div>
    <div class="wrapper-1419 anim-block">
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Cost Estimating</h4>
            <p class="para fs-23">Concept, schematic, and design development estimates with line-item detail and market-benchmarked rates.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Constructability Review</h4>
            <p class="para fs-23">Design review for buildability, sequence optimisation, and conflict identification before construction documents are finalised.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Value Engineering</h4>
            <p class="para fs-23">Structured analysis to identify cost-saving alternatives that preserve project intent, quality, and compliance.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Master Scheduling</h4>
            <p class="para fs-23">Integrated project schedules covering design, procurement, construction, and commissioning milestones.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Procurement Strategy</h4>
            <p class="para fs-23">Packaging and tendering strategy to maximise market competition and secure best-value subcontractor pricing.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Site Logistics Planning</h4>
            <p class="para fs-23">Detailed mobilisation plans including hoisting, phasing, access, and temporary works to minimise on-site disruption.</p>
        </div>
    </div>
</section>

<section class="careers-type-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h3 class="title fs-70 anim-elem top">Why clients choose Exellar for preconstruction</h3>
    </div>
    <div class="careers-type-slider-wrap">
        <div class="swiper careers-type-slider">
            <div class="swiper-wrapper">
                <div class="swiper-slide">
                    <div class="careers-type-txt anim-elem top">
                        <h3 class="title fs-45 anim-elem top">Market Knowledge</h3>
                        <p class="para fs-23 anim-elem top">Deep familiarity with Mumbai and Pune construction market rates, material lead times, and subcontractor capacity gives our estimates real-world accuracy.</p>
                    </div>
                </div>
                <div class="swiper-slide">
                    <div class="careers-type-txt anim-elem top">
                        <h3 class="title fs-45 anim-elem top">Early Involvement</h3>
                        <p class="para fs-23 anim-elem top">We engage at concept stage, embedding construction expertise into design decisions that are otherwise locked in before the CM is appointed.</p>
                    </div>
                </div>
                <div class="swiper-slide">
                    <div class="careers-type-txt anim-elem top">
                        <h3 class="title fs-45 anim-elem top">Budget Reliability</h3>
                        <p class="para fs-23 anim-elem top">Our preconstruction estimates have a proven track record of landing within ±5% of final contract values, giving lenders and boards the confidence to proceed.</p>
                    </div>
                </div>
                <div class="swiper-slide">
                    <div class="careers-type-txt anim-elem top">
                        <h3 class="title fs-45 anim-elem top">Seamless Transition</h3>
                        <p class="para fs-23 anim-elem top">Because the same team transitions from preconstruction to construction, there is no knowledge gap, no re-learning curve, and no delay at project start.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
"""

replace_body('preconstruction.html', pre_body)


# ══════════════════════════════════════════════════════════════════════════════
# 3. lean-construction.html
# ══════════════════════════════════════════════════════════════════════════════
lean_body = """
<section class="team-directory-hero prel ov-hidden">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 team-hero-wrapper anim-block">
        <div class="col-d-50 col-t-100 col-m-100">
            <h1 class="title fs-110 anim-elem top">Lean Construction</h1>
        </div>
        <div class="team-hero-para col-d-50 col-t-100 col-m-100">
            <p class="para fs-32 anim-elem top">Exellar applies Lean Construction principles to eliminate waste, improve workflow reliability, and deliver more value to clients — on time and within budget.</p>
        </div>
    </div>
</section>

<section class="img-txt-block-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-40pad f0 anim-block">
        <div class="img-txt-img-right inline_block col-d-50 col-t-100 col-m-100 vm anim-elem top">
            <div class="img-credit prel inline_block radius ov-hidden">
                <div class="video-holder prel ov-hidden radius">
                    <img class="w-100 b-lazy img-parallax" data-src="images/project-placeholder.jpg" alt="Lean Construction">
                </div>
            </div>
        </div>
        <div class="img-txt-txt inline_block col-d-50 col-t-100 col-m-100 vm anim-elem top">
            <h3 class="title fs-45">Less waste. More value. Better outcomes.</h3>
            <p class="para fs-23">Lean is not just a methodology — it is a culture of continuous improvement embedded in every Exellar project. By focusing on flow, pull planning, and last-planner collaboration, we consistently outperform traditional construction schedules while reducing rework and material waste.<br><br>Our site teams are trained in Lean principles and use visual management tools to keep every trade aligned and productive.</p>
        </div>
    </div>
</section>

<section class="careers-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h3 class="title fs-90 anim-elem top">Delivering more with less — by design</h3>
        <p class="para fs-32 anim-elem top">The Last Planner System and pull planning sessions bring all trade partners together to build reliable weekly work plans. The result: higher plan-percent-complete scores, fewer delays, and projects that stay on schedule even when conditions change.</p>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <div class="col-d-50 col-t-100 col-m-100 anim-elem top">
            <h3 class="title fs-70">Our Lean practices</h3>
        </div>
        <div class="col-d-50 col-t-100 col-m-100 anim-elem top">
            <p class="para fs-32">We apply a consistent set of Lean tools and practices across all Exellar project sites.</p>
        </div>
    </div>
    <div class="wrapper-1419 anim-block">
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Last Planner System</h4>
            <p class="para fs-23">Collaborative weekly work planning with all subcontractors to build reliable, commitment-based schedules.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Pull Planning</h4>
            <p class="para fs-23">Milestone-back planning sessions that identify predecessor activities and remove constraints before they impact production.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Daily Huddles</h4>
            <p class="para fs-23">Short, structured daily stand-ups at the point of work to resolve constraints, coordinate trades, and maintain momentum.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Visual Management</h4>
            <p class="para fs-23">Site-level dashboards, obeya rooms, and workflow boards that make project status transparent to every team member.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Continuous Improvement</h4>
            <p class="para fs-23">Structured after-action reviews (retrospectives) and lessons-learned sessions applied across project phases.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Waste Reduction</h4>
            <p class="para fs-23">Identification and elimination of the 8 wastes (TIMWOOD) from construction workflows, material handling, and on-site logistics.</p>
        </div>
    </div>
</section>

<section class="careers-type-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h3 class="title fs-70 anim-elem top">Lean in action at Exellar</h3>
    </div>
    <div class="careers-type-slider-wrap">
        <div class="swiper careers-type-slider">
            <div class="swiper-wrapper">
                <div class="swiper-slide">
                    <div class="careers-type-txt anim-elem top">
                        <h3 class="title fs-45 anim-elem top">Faster Cycle Times</h3>
                        <p class="para fs-23 anim-elem top">By eliminating waiting and batching inefficiencies, our Lean sites achieve 15–25% faster floor-cycle times compared to traditional approaches.</p>
                    </div>
                </div>
                <div class="swiper-slide">
                    <div class="careers-type-txt anim-elem top">
                        <h3 class="title fs-45 anim-elem top">Reduced Rework</h3>
                        <p class="para fs-23 anim-elem top">Root-cause analysis and first-time quality checklists reduce rework incidents, saving time and preventing budget overruns.</p>
                    </div>
                </div>
                <div class="swiper-slide">
                    <div class="careers-type-txt anim-elem top">
                        <h3 class="title fs-45 anim-elem top">Trade Partner Alignment</h3>
                        <p class="para fs-23 anim-elem top">Our collaborative planning model creates a shared ownership culture among all subcontractors — everyone commits, everyone delivers.</p>
                    </div>
                </div>
                <div class="swiper-slide">
                    <div class="careers-type-txt anim-elem top">
                        <h3 class="title fs-45 anim-elem top">Material Flow Optimisation</h3>
                        <p class="para fs-23 anim-elem top">Just-in-time delivery coordination and vertical transportation planning reduce on-site storage congestion and material handling delays.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
"""

replace_body('lean-construction.html', lean_body)


# ══════════════════════════════════════════════════════════════════════════════
# 4. project-management.html
# ══════════════════════════════════════════════════════════════════════════════
pm_body = """
<section class="team-directory-hero prel ov-hidden">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 team-hero-wrapper anim-block">
        <div class="col-d-50 col-t-100 col-m-100">
            <h1 class="title fs-110 anim-elem top">Project Management</h1>
        </div>
        <div class="team-hero-para col-d-50 col-t-100 col-m-100">
            <p class="para fs-32 anim-elem top">Exellar's project management practice brings structure, discipline, and clear communication to every project — ensuring that scope, time, cost, and quality targets are met without exception.</p>
        </div>
    </div>
</section>

<section class="img-txt-block-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-40pad f0 anim-block">
        <div class="img-txt-img-right inline_block col-d-50 col-t-100 col-m-100 vm anim-elem top">
            <div class="img-credit prel inline_block radius ov-hidden">
                <div class="video-holder prel ov-hidden radius">
                    <img class="w-100 b-lazy img-parallax" data-src="images/project-placeholder.jpg" alt="Project Management">
                </div>
            </div>
        </div>
        <div class="img-txt-txt inline_block col-d-50 col-t-100 col-m-100 vm anim-elem top">
            <h3 class="title fs-45">Structure that delivers results</h3>
            <p class="para fs-23">Our project managers are experienced professionals who combine technical knowledge with strong stakeholder communication skills. They serve as the single point of contact for the client, coordinating all internal and external parties to ensure seamless project execution.<br><br>From project charter through final account settlement, every project at Exellar follows a structured PM framework aligned with industry best practices.</p>
        </div>
    </div>
</section>

<section class="careers-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h3 class="title fs-90 anim-elem top">Visibility, control, and accountability at every stage</h3>
        <p class="para fs-32 anim-elem top">Our project management systems give clients real-time visibility into project health through structured reporting, earned value metrics, and risk registers — so issues are surfaced and addressed before they become problems.</p>
    </div>
</section>

<section class="commitments-intro-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <div class="col-d-50 col-t-100 col-m-100 anim-elem top">
            <h3 class="title fs-70">PM capabilities</h3>
        </div>
        <div class="col-d-50 col-t-100 col-m-100 anim-elem top">
            <p class="para fs-32">Our project management services span every knowledge area required to deliver complex construction projects successfully.</p>
        </div>
    </div>
    <div class="wrapper-1419 anim-block">
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Scope Management</h4>
            <p class="para fs-23">Clear scope definition, change order management, and scope creep prevention through robust contract administration.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Time Management</h4>
            <p class="para fs-23">Baseline scheduling, progress monitoring, delay analysis, and recovery planning using industry-standard scheduling tools.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Cost Management</h4>
            <p class="para fs-23">Budget establishment, cash flow forecasting, earned value analysis, and final account reconciliation.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Risk Management</h4>
            <p class="para fs-23">Proactive risk identification, quantification, mitigation planning, and contingency management throughout the project lifecycle.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Stakeholder Management</h4>
            <p class="para fs-23">Regular client reporting, authority liaison, community communication, and multi-party coordination across complex project environments.</p>
        </div>
        <div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">
            <h4 class="title fs-40">Document Control</h4>
            <p class="para fs-23">Structured drawing register management, RFI tracking, submittal logs, and complete project documentation for handover.</p>
        </div>
    </div>
</section>

<section class="careers-type-section prel">
    <div class="grid-lines gray">
        <div class="line-25"></div><div class="line-50"></div><div class="line-25"></div>
    </div>
    <div class="wrapper-1419 anim-block">
        <h3 class="title fs-70 anim-elem top">What sets our PMs apart</h3>
    </div>
    <div class="careers-type-slider-wrap">
        <div class="swiper careers-type-slider">
            <div class="swiper-wrapper">
                <div class="swiper-slide">
                    <div class="careers-type-txt anim-elem top">
                        <h3 class="title fs-45 anim-elem top">Site Experience</h3>
                        <p class="para fs-23 anim-elem top">Every Exellar PM has hands-on site experience — they understand the practical realities of construction, not just the theory of project management.</p>
                    </div>
                </div>
                <div class="swiper-slide">
                    <div class="careers-type-txt anim-elem top">
                        <h3 class="title fs-45 anim-elem top">Proactive Communication</h3>
                        <p class="para fs-23 anim-elem top">Clients are never left guessing. Weekly reports, monthly reviews, and real-time issue escalation keep every stakeholder informed and aligned.</p>
                    </div>
                </div>
                <div class="swiper-slide">
                    <div class="careers-type-txt anim-elem top">
                        <h3 class="title fs-45 anim-elem top">Technology Integration</h3>
                        <p class="para fs-23 anim-elem top">We use digital tools for scheduling, document control, and progress tracking — giving clients a live view of project performance at any time.</p>
                    </div>
                </div>
                <div class="swiper-slide">
                    <div class="careers-type-txt anim-elem top">
                        <h3 class="title fs-45 anim-elem top">Dispute Avoidance</h3>
                        <p class="para fs-23 anim-elem top">Our rigorous contract administration and documentation practices prevent disputes from arising and protect clients in the rare event they do.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
"""

replace_body('project-management.html', pm_body)

print('\nAll 4 service pages complete.')
