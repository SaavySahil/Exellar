import os
import re

projects_content = """<div class="total-wrapper">
    <!-- Hero Section -->
    <section class="section-padding bg-grey" style="text-align: center; padding-top: 120px;">
        <p class="section-label">OUR PORTFOLIO</p>
        <h1 class="title" style="font-size: 56px; margin-top: 20px;">Featured Projects</h1>
        <p class="para" style="max-width: 700px; margin: 20px auto; font-size: 20px;">Showcasing 50+ years of engineering excellence across Mumbai and Pune's skyline.</p>
    </section>

    <!-- Filters Section (Static for now, but structured for JS) -->
    <section class="section-padding" style="padding: 40px 0; border-bottom: 1px solid #e2e8f0;">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; flex-wrap: wrap; gap: 20px; justify-content: space-between; align-items: center;">
            <div style="display: flex; gap: 15px; align-items: center;">
                <span style="font-weight: 600; color: var(--primary-blue);">Filter by City:</span>
                <select style="padding: 10px; border: 1px solid #cbd5e1; border-radius: 4px; font-family: 'Inter', sans-serif;">
                    <option value="all">All Cities</option>
                    <option value="mumbai">Mumbai</option>
                    <option value="pune">Pune</option>
                </select>
            </div>
            
            <div style="display: flex; gap: 15px; align-items: center;">
                <span style="font-weight: 600; color: var(--primary-blue);">Service Type:</span>
                <select style="padding: 10px; border: 1px solid #cbd5e1; border-radius: 4px; font-family: 'Inter', sans-serif;">
                    <option value="all">All Services</option>
                    <option value="high-rise">High-Rise Construction</option>
                    <option value="repairs">Repairs & Rehabilitation</option>
                    <option value="infrastructure">Infrastructure</option>
                </select>
            </div>
        </div>
    </section>

    <!-- Project Gallery -->
    <section class="section-padding">
        <div style="max-width: 1400px; margin: 0 auto; padding: 0 20px; display: grid; grid-template-columns: repeat(auto-fill, minmax(400px, 1fr)); gap: 40px;">
            
            <!-- Project 1 -->
            <div class="project-card" style="box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden; background: #fff; transition: transform 0.3s ease;">
                <div style="height: 250px; background: #94a3b8; position: relative;">
                    <img src="images/project-placeholder.jpg" alt="Rustomjee Urbania" style="width: 100%; height: 100%; object-fit: cover;">
                    <div style="position: absolute; top: 10px; right: 10px; background: var(--primary-orange); color: #fff; padding: 4px 12px; font-size: 12px; font-weight: bold; border-radius: 20px;">REHABILITATION</div>
                </div>
                <div style="padding: 30px;">
                    <h3 class="title" style="font-size: 24px; margin-bottom: 10px;">Rustomjee Urbania</h3>
                    <p style="color: #64748b; margin-bottom: 20px; font-weight: 500;">📍 Thane, Mumbai</p>
                    <div style="margin-bottom: 20px;">
                        <span style="font-weight: 600; color: var(--text-dark);">Scope of Work:</span>
                        <p class="para" style="font-size: 15px;">Complete structural rehabilitation and retrofitting without disrupting residential occupancy.</p>
                    </div>
                </div>
            </div>

            <!-- Project 2 -->
            <div class="project-card" style="box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden; background: #fff; transition: transform 0.3s ease;">
                <div style="height: 250px; background: #94a3b8; position: relative;">
                    <img src="images/project-placeholder.jpg" alt="Lodha Altamount" style="width: 100%; height: 100%; object-fit: cover;">
                    <div style="position: absolute; top: 10px; right: 10px; background: var(--primary-orange); color: #fff; padding: 4px 12px; font-size: 12px; font-weight: bold; border-radius: 20px;">HIGH-RISE</div>
                </div>
                <div style="padding: 30px;">
                    <h3 class="title" style="font-size: 24px; margin-bottom: 10px;">Lodha Altamount</h3>
                    <p style="color: #64748b; margin-bottom: 20px; font-weight: 500;">📍 South Mumbai</p>
                    <div style="margin-bottom: 20px;">
                        <span style="font-weight: 600; color: var(--text-dark);">Scope of Work:</span>
                        <p class="para" style="font-size: 15px;">Advanced structural framework and high-grade concrete pouring for luxury residential skyscraper.</p>
                    </div>
                </div>
            </div>

            <!-- Project 3 -->
            <div class="project-card" style="box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); border-radius: 8px; overflow: hidden; background: #fff; transition: transform 0.3s ease;">
                <div style="height: 250px; background: #94a3b8; position: relative;">
                    <img src="images/project-placeholder.jpg" alt="Kalpataru Estate" style="width: 100%; height: 100%; object-fit: cover;">
                    <div style="position: absolute; top: 10px; right: 10px; background: var(--primary-orange); color: #fff; padding: 4px 12px; font-size: 12px; font-weight: bold; border-radius: 20px;">WATERPROOFING</div>
                </div>
                <div style="padding: 30px;">
                    <h3 class="title" style="font-size: 24px; margin-bottom: 10px;">Kalpataru Estate</h3>
                    <p style="color: #64748b; margin-bottom: 20px; font-weight: 500;">📍 Pune</p>
                    <div style="margin-bottom: 20px;">
                        <span style="font-weight: 600; color: var(--text-dark);">Scope of Work:</span>
                        <p class="para" style="font-size: 15px;">Targeted basement and terrace waterproofing, along with extensive compound development.</p>
                    </div>
                </div>
            </div>

        </div>
    </section>
</div>
"""

about_content = """<div class="total-wrapper">
    <!-- Hero Section -->
    <section class="section-padding bg-grey" style="text-align: center; padding-top: 120px;">
        <p class="section-label">OUR LEGACY</p>
        <h1 class="title" style="font-size: 56px; margin-top: 20px;">About Exellar Construction</h1>
        <p class="para" style="max-width: 800px; margin: 20px auto; font-size: 20px;">We are a legacy civil contractor specializing in high-rise construction, structural repairs, and redevelopment support across Mumbai and Pune.</p>
    </section>

    <!-- Company History & The Advantage -->
    <section class="section-padding">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px; display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center;">
            <div>
                <img src="images/project-placeholder.jpg" alt="Exellar Legacy" style="width: 100%; border-radius: 8px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);">
            </div>
            <div>
                <h2 class="title" style="font-size: 36px; margin-bottom: 20px;">50+ Years of Trust</h2>
                <p class="para" style="margin-bottom: 20px;">Since our foundation in 1964, Exellar Construction LLP has grown from a specialized local builder into one of Maharashtra's most trusted commercial and high-rise construction firms. We have worked closely with the leading developers, societies, and consultants in the region.</p>
                
                <h3 class="title" style="font-size: 24px; margin-top: 40px; margin-bottom: 15px;">The Exellar Advantage</h3>
                <ul style="list-style: none; padding: 0; display: flex; flex-direction: column; gap: 15px;">
                    <li style="display: flex; align-items: flex-start; gap: 10px;">
                        <span style="color: var(--primary-orange); font-size: 20px;">✓</span>
                        <p class="para" style="margin: 0;"><strong>Safety First:</strong> Zero-compromise safety standards on every site.</p>
                    </li>
                    <li style="display: flex; align-items: flex-start; gap: 10px;">
                        <span style="color: var(--primary-orange); font-size: 20px;">✓</span>
                        <p class="para" style="margin: 0;"><strong>Timeline Strictness:</strong> Proven track record of on-time delivery across 100+ major projects.</p>
                    </li>
                    <li style="display: flex; align-items: flex-start; gap: 10px;">
                        <span style="color: var(--primary-orange); font-size: 20px;">✓</span>
                        <p class="para" style="margin: 0;"><strong>Engineering Expertise:</strong> In-house structural experts tackling the most complex repairs.</p>
                    </li>
                </ul>
            </div>
        </div>
    </section>
    
    <!-- PDF Download CTA -->
    <section class="section-padding bg-grey" style="text-align: center;">
        <div style="max-width: 800px; margin: 0 auto;">
            <h2 class="title" style="font-size: 36px; margin-bottom: 20px;">Exellar Corporate Profile</h2>
            <p class="para" style="margin-bottom: 30px;">Download our comprehensive corporate overview detailing our capabilities, certifications, and portfolio.</p>
            <a href="#" class="btn-link">Download Company Profile (PDF)</a>
        </div>
    </section>
</div>
"""

services_content = """<div class="total-wrapper">
    <!-- Hero Section -->
    <section class="section-padding bg-grey" style="text-align: center; padding-top: 120px;">
        <p class="section-label">OUR EXPERTISE</p>
        <h1 class="title" style="font-size: 56px; margin-top: 20px;">Comprehensive Construction Services</h1>
        <p class="para" style="max-width: 800px; margin: 20px auto; font-size: 20px;">Delivering specialized civil engineering, construction, and repair works for commercial clients, developers, and societies.</p>
    </section>

    <!-- Services Grid -->
    <section class="section-padding">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px; display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 40px;">
            
            <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 40px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
                <div style="width: 60px; height: 60px; background: var(--bg-grey); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px; color: var(--primary-orange); font-size: 24px; font-weight: bold;">01</div>
                <h3 class="title" style="font-size: 24px; margin-bottom: 15px;">High-Rise Construction</h3>
                <p class="para" style="margin-bottom: 0;">End-to-end civil execution for residential towers and commercial complexes. We specialize in fast-paced structural completions and premium core & shell construction.</p>
            </div>

            <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 40px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
                <div style="width: 60px; height: 60px; background: var(--bg-grey); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px; color: var(--primary-orange); font-size: 24px; font-weight: bold;">02</div>
                <h3 class="title" style="font-size: 24px; margin-bottom: 15px;">Structural Repairs</h3>
                <p class="para" style="margin-bottom: 0;">Specialized rehabilitation, retrofitting, micro-concreting, and guniting. We restore the integrity of aging structures with minimal disruption to occupants.</p>
            </div>

            <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 40px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
                <div style="width: 60px; height: 60px; background: var(--bg-grey); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px; color: var(--primary-orange); font-size: 24px; font-weight: bold;">03</div>
                <h3 class="title" style="font-size: 24px; margin-bottom: 15px;">Waterproofing Solutions</h3>
                <p class="para" style="margin-bottom: 0;">Advanced injection grouting, crystalline waterproofing, and comprehensive protections for basements, terraces, and facades against heavy monsoons.</p>
            </div>

            <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 40px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
                <div style="width: 60px; height: 60px; background: var(--bg-grey); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 20px; color: var(--primary-orange); font-size: 24px; font-weight: bold;">04</div>
                <h3 class="title" style="font-size: 24px; margin-bottom: 15px;">Civil & Infrastructure</h3>
                <p class="para" style="margin-bottom: 0;">Compound development, hardscaping, retaining walls, and related civil infrastructure support for large housing societies and township developers.</p>
            </div>

        </div>
    </section>
</div>
"""

def update_file(filename, replacement_content):
    if not os.path.exists(filename):
        # We handle missing files gracefully by creating them based on a template
        # Let's clone Home.html to get the header and footer
        import shutil
        shutil.copyfile("Home.html", filename)
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace content inside <div class="total-wrapper">
    start_tag = '<div class="total-wrapper">'
    if start_tag in content:
        start_idx = content.find(start_tag)
        # Find the footer to know where `total-wrapper` ends. Note the script above replaced it with `<footer class="footer anim-block" style=` 
        end_idx = content.find('<footer class="footer')
        
        if start_idx != -1 and end_idx != -1:
            # We want to replace from start_idx up to the closing div of total-wrapper, right before footer
            # The closing div is hard to find reliably, so we will replace up to the start of the footer
            # By replacing it with the new content, we need to ensure the closing </div> is maintained if it wasn't part of new content, 
            # wait, my new content above *includes* the `<div class="total-wrapper">` and a closing `</div>`.
            content = content[:start_idx] + replacement_content + "\\n\\n" + content[end_idx:]
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Updated {filename}")
        else:
            print(f"Failed to find bounds in {filename}")
    else:
        print(f"Failed to find start tag in {filename}")

update_file("Projects.html", projects_content)
update_file("About-us.html", about_content)
update_file("Services.html", services_content)
