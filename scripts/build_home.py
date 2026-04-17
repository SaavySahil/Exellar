import os

with open("Home.html", "r", encoding="utf-8") as f:
    content = f.read()

start_idx = content.find('<div class="total-wrapper">')
end_idx = content.find('<footer class="footer')

home_content = """<div class="total-wrapper">
    <!-- Hero Section -->
    <section class="home-hero-section ov-hidden" style="position: relative; overflow: hidden; height: 100vh; min-height: 600px;">
        <div class="home-hero-holder prel anim-block" style="height: 100%; display: flex; align-items: center; justify-content: center; position: relative;">
            <div class="home-hero-img img-parallax" style="position: absolute; top:0; left:0; width:100%; height:100%; z-index:-1;">
                <img src="images/project-placeholder.jpg" alt="Exellar High-Rise Construction" style="object-fit: cover; width:100%; height:100%;">
                <div style="position: absolute; top:0; left:0; width:100%; height:100%; background: linear-gradient(rgba(15, 32, 39, 0.8), rgba(15, 32, 39, 0.9));"></div>
            </div>
            
            <div class="hero-content" style="text-align: center; max-width: 1000px; padding: 0 30px; z-index: 10;">
                <div class="hero-title" style="margin-bottom: 40px;">
                    <p class="section-label white" style="margin-bottom: 20px; font-size: 16px; letter-spacing: 2px;">EXELLAR CONSTRUCTION LLP</p>
                    <h1 class="title white anim-elem top" style="font-size: clamp(40px, 6vw, 75px); line-height: 1.1; margin-bottom: 30px;">
                        Building Mumbai’s Skyline with <strong style="color: var(--primary-orange);">50+ Years</strong> of Engineering Excellence
                    </h1>
                    <p class="para white anim-elem top" style="font-size: clamp(18px, 2vw, 24px); max-width: 800px; margin: 0 auto; opacity: 0.9;">
                        Trusted civil contractors for high-rise construction, structural repairs, and redevelopment projects.
                    </p>
                </div>
                
                <div class="hero-buttons anim-elem top" style="display: flex; gap: 20px; justify-content: center; margin-top: 40px;">
                    <a href="Projects.html" class="btn-link">View Projects</a>
                    <a href="contact-us.html" class="btn-link white">Get a Quote</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Legacy / Quick Stats -->
    <section class="section-padding bg-grey">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; flex-wrap: wrap; justify-content: space-around; gap: 40px; text-align: center;">
            <div>
                <h3 class="title" style="font-size: 48px; color: var(--primary-orange); margin-bottom: 10px;">1964</h3>
                <p class="para" style="font-weight: 600; font-size: 18px;">Established Since</p>
            </div>
            <div>
                <h3 class="title" style="font-size: 48px; color: var(--primary-orange); margin-bottom: 10px;">100+</h3>
                <p class="para" style="font-weight: 600; font-size: 18px;">Major Projects Completed</p>
            </div>
            <div>
                <h3 class="title" style="font-size: 48px; color: var(--primary-orange); margin-bottom: 10px;">2</h3>
                <p class="para" style="font-weight: 600; font-size: 18px;">Cities Served (Mumbai, Pune)</p>
            </div>
            <div>
                <h3 class="title" style="font-size: 48px; color: var(--primary-orange); margin-bottom: 10px;">Zero</h3>
                <p class="para" style="font-weight: 600; font-size: 18px;">Compromise on Safety</p>
            </div>
        </div>
    </section>

    <!-- Services Snapshot -->
    <section class="section-padding">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
            <div style="text-align: center; margin-bottom: 60px;">
                <p class="section-label">OUR SERVICES</p>
                <h2 class="title" style="font-size: 40px; margin-top: 15px;">What We Build</h2>
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
                <div style="padding: 40px; background: var(--bg-grey); border-radius: 8px;">
                    <h3 class="title" style="font-size: 24px; margin-bottom: 15px;">High-Rise Construction</h3>
                    <p class="para" style="margin-bottom: 20px;">Premium residential and commercial towers executing specialized structural challenges.</p>
                    <a href="Services.html" style="font-weight: 600; color: var(--primary-orange); text-decoration: none;">Learn More →</a>
                </div>
                <div style="padding: 40px; background: var(--bg-grey); border-radius: 8px;">
                    <h3 class="title" style="font-size: 24px; margin-bottom: 15px;">Repairs & Rehab</h3>
                    <p class="para" style="margin-bottom: 20px;">Structural strengthening, retrofitting and extending the lifecycle of aging buildings.</p>
                    <a href="Services.html" style="font-weight: 600; color: var(--primary-orange); text-decoration: none;">Learn More →</a>
                </div>
                <div style="padding: 40px; background: var(--bg-grey); border-radius: 8px;">
                    <h3 class="title" style="font-size: 24px; margin-bottom: 15px;">Waterproofing</h3>
                    <p class="para" style="margin-bottom: 20px;">End-to-end robust waterproofing for basements, terraces and complex facades.</p>
                    <a href="Services.html" style="font-weight: 600; color: var(--primary-orange); text-decoration: none;">Learn More →</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Featured Projects -->
    <section class="section-padding bg-grey">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 40px; flex-wrap: wrap; gap: 20px;">
                <div>
                    <p class="section-label">PORTFOLIO EXCERPT</p>
                    <h2 class="title" style="font-size: 40px; margin-top: 15px;">Featured Projects</h2>
                </div>
                <a href="Projects.html" class="btn-link">View All Projects</a>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px;">
                <div style="border-radius: 8px; overflow: hidden; background: #fff; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
                    <img src="images/project-placeholder.jpg" alt="Rustomjee Urbania" style="width: 100%; height: 250px; object-fit: cover;">
                    <div style="padding: 30px;">
                        <h3 class="title" style="font-size: 22px; margin-bottom: 10px;">Rustomjee Urbania</h3>
                        <p style="color: #64748b; margin-bottom: 0;">📍 Thane, Mumbai</p>
                    </div>
                </div>
                <div style="border-radius: 8px; overflow: hidden; background: #fff; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">
                    <img src="images/project-placeholder.jpg" alt="Lodha Altamount" style="width: 100%; height: 250px; object-fit: cover;">
                    <div style="padding: 30px;">
                        <h3 class="title" style="font-size: 22px; margin-bottom: 10px;">Lodha Altamount</h3>
                        <p style="color: #64748b; margin-bottom: 0;">📍 South Mumbai</p>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <!-- Client Logos -->
    <section class="section-padding" style="border-bottom: 1px solid #e2e8f0;">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px; text-align: center;">
            <p class="section-label" style="margin-bottom: 40px;">TRUSTED BY MAHARASHTRA'S BEST</p>
            <div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 60px; font-weight: bold; font-family: 'Montserrat', sans-serif; font-size: 28px; color: #94a3b8;">
                <span>Rustomjee</span>
                <span>Kalpataru</span>
                <span>Lodha Group</span>
                <span>JW Consultants</span>
            </div>
        </div>
    </section>
</div>"""

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + home_content + "\\n\\n" + content[end_idx:]
    with open("Home.html", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Updated Home.html successfully!")
