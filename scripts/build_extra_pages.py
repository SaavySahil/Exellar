import os

template_file = "Home.html"
with open(template_file, "r", encoding="utf-8") as f:
    template_content = f.read()

# Replace <div class="total-wrapper">...</div>
start_idx = template_content.find('<div class="total-wrapper">')
end_idx = template_content.find('<footer class="footer')

clients_content = """<div class="total-wrapper">
    <section class="section-padding bg-grey" style="text-align: center; padding-top: 120px;">
        <p class="section-label">OUR PARTNERS</p>
        <h1 class="title" style="font-size: 56px; margin-top: 20px;">Clients & Societies</h1>
        <p class="para" style="max-width: 800px; margin: 20px auto; font-size: 20px;">Trusted by Maharashtra's leading developers, renowned consultants, and prestigious cooperative housing societies.</p>
    </section>

    <section class="section-padding">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 40px; text-align: center;">
            <div style="padding: 40px; background: #fff; border: 1px solid #e2e8f0; border-radius: 8px;">
                <h3 style="color: var(--primary-blue); font-size: 24px; font-weight: bold; font-family: 'Montserrat', sans-serif;">Rustomjee</h3>
                <p style="color: #64748b; margin-top: 10px;">Developer Partner</p>
            </div>
            <div style="padding: 40px; background: #fff; border: 1px solid #e2e8f0; border-radius: 8px;">
                <h3 style="color: var(--primary-blue); font-size: 24px; font-weight: bold; font-family: 'Montserrat', sans-serif;">Kalpataru</h3>
                <p style="color: #64748b; margin-top: 10px;">Developer Partner</p>
            </div>
            <div style="padding: 40px; background: #fff; border: 1px solid #e2e8f0; border-radius: 8px;">
                <h3 style="color: var(--primary-blue); font-size: 24px; font-weight: bold; font-family: 'Montserrat', sans-serif;">Lodha Group</h3>
                <p style="color: #64748b; margin-top: 10px;">Developer Partner</p>
            </div>
            <div style="padding: 40px; background: #fff; border: 1px solid #e2e8f0; border-radius: 8px;">
                <h3 style="color: var(--primary-blue); font-size: 24px; font-weight: bold; font-family: 'Montserrat', sans-serif;">JW Consultants</h3>
                <p style="color: #64748b; margin-top: 10px;">Engineering Consultant</p>
            </div>
        </div>
    </section>
</div>"""

certifications_content = """<div class="total-wrapper">
    <section class="section-padding bg-grey" style="text-align: center; padding-top: 120px;">
        <p class="section-label">QUALITY ASSURED</p>
        <h1 class="title" style="font-size: 56px; margin-top: 20px;">Certifications & Credentials</h1>
        <p class="para" style="max-width: 800px; margin: 20px auto; font-size: 20px;">Our rigorous processes and compliance standards have earned us industry-leading credentials.</p>
    </section>

    <section class="section-padding">
        <div style="max-width: 800px; margin: 0 auto; padding: 0 20px;">
            <div style="display: flex; gap: 40px; align-items: center; border-bottom: 1px solid #e2e8f0; padding-bottom: 40px; margin-bottom: 40px;">
                <div style="font-size: 60px;">🏆</div>
                <div>
                    <h3 class="title" style="font-size: 24px; margin-bottom: 15px;">ISO 9001:2015</h3>
                    <p class="para">Certified Quality Management Systems, ensuring consistent quality and processes in every project phase.</p>
                </div>
            </div>
            <div style="display: flex; gap: 40px; align-items: center; border-bottom: 1px solid #e2e8f0; padding-bottom: 40px; margin-bottom: 40px;">
                <div style="font-size: 60px;">🛡️</div>
                <div>
                    <h3 class="title" style="font-size: 24px; margin-bottom: 15px;">ISO 45001:2018</h3>
                    <p class="para">Certified Occupational Health & Safety Management Systems. We maintain zero-compromise safety protocols.</p>
                </div>
            </div>
            <div style="display: flex; gap: 40px; align-items: center;">
                <div style="font-size: 60px;">📜</div>
                <div>
                    <h3 class="title" style="font-size: 24px; margin-bottom: 15px;">MCGM / BMC Licenses</h3>
                    <p class="para">Class I Registered Civil Contractor with the Municipal Corporation of Greater Mumbai.</p>
                </div>
            </div>
        </div>
    </section>
</div>"""

contact_content = """<div class="total-wrapper">
    <section class="section-padding bg-grey" style="text-align: center; padding-top: 120px;">
        <p class="section-label">GET IN TOUCH</p>
        <h1 class="title" style="font-size: 56px; margin-top: 20px;">Contact Us</h1>
        <p class="para" style="max-width: 800px; margin: 20px auto; font-size: 20px;">Ready to build something great or need specialized structural repairs? Reach out to our team.</p>
    </section>

    <section class="section-padding">
        <div style="max-width: 1200px; margin: 0 auto; padding: 0 20px; display: grid; grid-template-columns: 1fr 1fr; gap: 60px;">
            <div>
                <h3 class="title" style="font-size: 32px; margin-bottom: 30px;">Send Us a Message</h3>
                <form style="display: flex; flex-direction: column; gap: 20px;">
                    <div>
                        <label style="font-weight: 600; color: var(--primary-blue); display: block; margin-bottom: 8px;">Name</label>
                        <input type="text" style="width: 100%; padding: 15px; border: 1px solid #cbd5e1; border-radius: 4px; font-family: 'Inter', sans-serif;">
                    </div>
                    <div>
                        <label style="font-weight: 600; color: var(--primary-blue); display: block; margin-bottom: 8px;">Email</label>
                        <input type="email" style="width: 100%; padding: 15px; border: 1px solid #cbd5e1; border-radius: 4px; font-family: 'Inter', sans-serif;">
                    </div>
                    <div>
                        <label style="font-weight: 600; color: var(--primary-blue); display: block; margin-bottom: 8px;">Company / Society</label>
                        <input type="text" style="width: 100%; padding: 15px; border: 1px solid #cbd5e1; border-radius: 4px; font-family: 'Inter', sans-serif;">
                    </div>
                    <div>
                        <label style="font-weight: 600; color: var(--primary-blue); display: block; margin-bottom: 8px;">Project Requirements</label>
                        <textarea rows="5" style="width: 100%; padding: 15px; border: 1px solid #cbd5e1; border-radius: 4px; font-family: 'Inter', sans-serif; resize: vertical;"></textarea>
                    </div>
                    <button type="submit" class="btn-link" style="border: none; cursor: pointer; width: 100%; justify-content: center; font-size: 16px;">Submit Inquiry</button>
                </form>
            </div>
            
            <div style="background: var(--primary-blue); border-radius: 8px; padding: 60px; color: #fff;">
                <h3 class="title white" style="font-size: 32px; margin-bottom: 30px;">Our Offices</h3>
                
                <div style="margin-bottom: 40px;">
                    <h4 style="font-size: 20px; margin-bottom: 10px; font-weight: 600; color: var(--primary-orange);">Mumbai Headquarters</h4>
                    <p style="color: #cbd5e1; line-height: 1.8;">Exellar Construction LLP<br>123 Corporate Avenue, Andheri East<br>Mumbai, Maharashtra 400059</p>
                </div>
                
                <div style="margin-bottom: 40px;">
                    <h4 style="font-size: 20px; margin-bottom: 10px; font-weight: 600; color: var(--primary-orange);">Pune Regional Office</h4>
                    <p style="color: #cbd5e1; line-height: 1.8;">Exellar Engineering Services<br>45 Business Park, Baner<br>Pune, Maharashtra 411045</p>
                </div>
                
                <div>
                    <h4 style="font-size: 20px; margin-bottom: 10px; font-weight: 600; color: var(--primary-orange);">Contact Details</h4>
                    <p style="color: #cbd5e1; line-height: 1.8;">Email: info@exellarconstruction.com<br>Phone: +91 22 1234 5678</p>
                </div>
            </div>
        </div>
    </section>
</div>"""

careers_content = """<div class="total-wrapper">
    <section class="section-padding bg-grey" style="text-align: center; padding-top: 120px;">
        <p class="section-label">JOIN EXELLAR</p>
        <h1 class="title" style="font-size: 56px; margin-top: 20px;">Build Your Career</h1>
        <p class="para" style="max-width: 800px; margin: 20px auto; font-size: 20px;">Work alongside industry veterans on Maharashtra's most challenging high-rise and rehabilitation projects.</p>
    </section>

    <section class="section-padding">
        <div style="max-width: 1000px; margin: 0 auto; padding: 0 20px;">
            <h2 class="title" style="font-size: 36px; margin-bottom: 40px; text-align: center;">Open Positions</h2>
            
            <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 30px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
                <div>
                    <h3 class="title" style="font-size: 24px; margin-bottom: 10px;">Senior Site Engineer</h3>
                    <p style="color: #64748b;">📍 Mumbai • Minimum 5 Years Experience • High-Rise</p>
                </div>
                <a href="contact-us.html" class="btn-link">Apply Now</a>
            </div>
            
            <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 30px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
                <div>
                    <h3 class="title" style="font-size: 24px; margin-bottom: 10px;">Structural Repair Specialist</h3>
                    <p style="color: #64748b;">📍 Pune • Minimum 3 Years Experience • Rehabilitation</p>
                </div>
                <a href="contact-us.html" class="btn-link">Apply Now</a>
            </div>
            
            <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 30px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 20px;">
                <div>
                    <h3 class="title" style="font-size: 24px; margin-bottom: 10px;">Quantity Surveyor</h3>
                    <p style="color: #64748b;">📍 Mumbai • Minimum 2 Years Experience • Billing & Estimation</p>
                </div>
                <a href="contact-us.html" class="btn-link">Apply Now</a>
            </div>
        </div>
    </section>
</div>"""

def create_page(filename, content):
    new_content = template_content[:start_idx] + content + "\n\n" + template_content[end_idx:]
    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_content)
    print(f"Created/Updated {filename}")

create_page("Clients.html", clients_content)
create_page("certifications.html", certifications_content)
create_page("contact-us.html", contact_content)
create_page("Careers.html", careers_content)
