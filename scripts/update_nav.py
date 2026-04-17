import os
import re
import glob

html_files = glob.glob('*.html')

new_header = """<header class="header" id="header">
    <div class="header-holder">
        <div class="header-logo-col">
            <a href="Home.html" class="light-header" style="font-weight: bold; font-size: 24px; color: var(--primary-blue); font-family: 'Montserrat', sans-serif;">EXELLAR</a>
            <a href="Home.html" class="dark-header" style="font-weight: bold; font-size: 24px; color: #fff; font-family: 'Montserrat', sans-serif;">EXELLAR</a>
        </div>
        <div class="header-nav-col desktop-only" style="display: flex; gap: 20px; align-items: center; justify-content: flex-end; width: 100%; padding-right: 20px;">
            <a class="header-link" href="Home.html">Home</a>
            <a class="header-link" href="About-us.html">About Us</a>
            <a class="header-link" href="Services.html">Services</a>
            <a class="header-link" href="Projects.html">Projects</a>
            <a class="header-link" href="Clients.html">Clients</a>
            <a class="header-link" href="certifications.html">Credentials</a>
            <a class="header-link" href="Careers.html">Careers</a>
            <a class="header-link" href="contact-us.html">Contact</a>
        </div>
        <div class="header-menu-col">
            <button class="header-menu-contact contact-popup-open" tabindex="0">
                <div class="header-contact-txt">
                    <p>Get a Quote</p>
                </div>
            </button>
            <div class="header-menu-contact subcont">
                <div class="header-contact-txt"><a href="vendor-registration.html">Vendor Registration</a></div>
            </div>
            <button class="header-menu-icon mobile-only" tabindex="0" aria-haspopup="true" aria-expanded="false" aria-label="open megamenu">
                <div class="menu-button">
                    <span class="menu-button-line"></span>
                    <span class="menu-button-line"></span>
                    <span class="menu-button-line"></span>
                </div>
            </button>
        </div>
    </div>
</header>
<!-- Mobile megamenu simplified -->
<div class="megamenu">
    <div class="megamenu-header">
        <div class="megamenu-logo prel">
            <span style="font-weight: bold; font-size: 24px; color: #fff;">EXELLAR</span>
        </div>
        <div class="megamenu-search">
            <div class="search-holder">
                <button class="megamenu-close">
                    <div class="megamenu-close-holder">
                        <span class="mega-close-arm"></span><span class="mega-close-arm"></span>
                    </div>
                </button>
            </div>
        </div>
    </div>
    <div class="megamenu-body">
        <div class="megamenu-menu" data-lenis-prevent="" style="width: 100%;">
            <div class="menu-dropdown" style="padding: 40px; display: flex; flex-direction: column; gap: 20px;">
                <a href="Home.html" class="title fs-45 white">Home</a>
                <a href="About-us.html" class="title fs-45 white">About Us</a>
                <a href="Services.html" class="title fs-45 white">Services</a>
                <a href="Projects.html" class="title fs-45 white">Projects</a>
                <a href="Clients.html" class="title fs-45 white">Clients</a>
                <a href="certifications.html" class="title fs-45 white">Credentials</a>
                <a href="insights.html" class="title fs-45 white">Case Studies / Blog</a>
                <a href="Careers.html" class="title fs-45 white">Careers</a>
                <a href="contact-us.html" class="title fs-45 white">Contact</a>
                <a href="vendor-registration.html" class="title fs-45 white">Vendor Registration</a>
            </div>
        </div>
    </div>
</div>
"""

new_footer = """<footer class="footer anim-block" style="background-color: var(--primary-blue); padding: 60px 0;">
    <div class="footer-wrapper prel" style="max-width: 1400px; margin: 0 auto; padding: 0 40px;">
        <div class="footer-first-row" style="display: flex; flex-wrap: wrap; gap: 40px; justify-content: space-between;">
            <div class="first-row-col anim-elem top">
                <a href="Home.html" class="f0 inline_block" style="font-weight: bold; font-size: 32px; color: #fff; font-family: 'Montserrat', sans-serif; text-decoration: none;">
                    EXELLAR <span style="display:block; font-size: 14px; font-weight: normal; color: var(--primary-orange); letter-spacing: 2px; margin-top: 5px;">CONSTRUCTION LLP</span>
                </a>
                <p style="color: #94a3b8; max-width: 300px; margin-top: 20px; font-size: 14px;">Building Mumbai's Skyline with 50+ Years of Engineering Excellence. Trusted civil contractors for high-rise construction, structural repairs, and redevelopment projects.</p>
            </div>
            
            <div class="first-row-col-2 anim-elem top" style="flex: 1; display: flex; gap: 40px; justify-content: flex-end;">
                <div>
                    <h4 style="color: #fff; margin-bottom: 20px; font-weight: 600;">Navigation</h4>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px;">
                        <li><a href="Home.html" style="color: #cbd5e1; text-decoration: none; font-size: 14px;">Home</a></li>
                        <li><a href="About-us.html" style="color: #cbd5e1; text-decoration: none; font-size: 14px;">About Us</a></li>
                        <li><a href="Services.html" style="color: #cbd5e1; text-decoration: none; font-size: 14px;">Services</a></li>
                        <li><a href="Projects.html" style="color: #cbd5e1; text-decoration: none; font-size: 14px;">Projects</a></li>
                        <li><a href="insights.html" style="color: #cbd5e1; text-decoration: none; font-size: 14px;">Case Studies</a></li>
                    </ul>
                </div>
                <div>
                    <h4 style="color: #fff; margin-bottom: 20px; font-weight: 600;">Information</h4>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px;">
                        <li><a href="Clients.html" style="color: #cbd5e1; text-decoration: none; font-size: 14px;">Clients</a></li>
                        <li><a href="certifications.html" style="color: #cbd5e1; text-decoration: none; font-size: 14px;">Credentials</a></li>
                        <li><a href="Careers.html" style="color: #cbd5e1; text-decoration: none; font-size: 14px;">Careers</a></li>
                        <li><a href="contact-us.html" style="color: #cbd5e1; text-decoration: none; font-size: 14px;">Contact Us</a></li>
                        <li><a href="vendor-registration.html" style="color: #cbd5e1; text-decoration: none; font-size: 14px;">Vendor Registration</a></li>
                    </ul>
                </div>
                <div>
                    <h4 style="color: #fff; margin-bottom: 20px; font-weight: 600;">Contact</h4>
                    <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 10px; color: #cbd5e1; font-size: 14px;">
                        <li>Mumbai, Maharashtra</li>
                        <li>Pune, Maharashtra</li>
                        <li>info@exellarconstruction.com</li>
                        <li>+91 XXXXX XXXXX</li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="footer-last-row" style="margin-top: 60px; padding-top: 20px; border-top: 1px solid #1e293b; display: flex; justify-content: space-between; color: #64748b; font-size: 12px;">
            <p>&copy; 2024 Exellar Construction LLP. All Rights Reserved.</p>
        </div>
    </div>
</footer>"""

for file_path in html_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace Header and Megamenu
        if '<header class="header" id="header">' in content and '</div>\n</div>\n\n            \n            <button class="header-menu-icon"' in content:
            # We will use regex to capture the whole header block and megamenu
            content = re.sub(r'<header class="header" id="header">.*?</header>\s*<div class="megamenu">.*?<div class="mega-search-mobile">.*?<!-- mobile nav ends -> or similar', new_header, content, flags=re.DOTALL)
            # Actually, standard regex might safely just match to the end of <div class="total-wrapper">?
            # Let's find exactly what to replace.
            
        # Using simple string splits
        head_start = content.find('<header class="header" id="header">')
        mega_end = content.find('<div class="total-wrapper">')
        if mega_end == -1:
            mega_end = content.find('<main')
        
        if head_start != -1 and mega_end != -1 and head_start < mega_end:
            content = content[:head_start] + new_header + "\n" + content[mega_end:]
            
        footer_start = content.find('<footer class="footer anim-block">')
        footer_end = content.find('</footer>') + len('</footer>')
        if footer_start != -1 and footer_end != -1:
            content = content[:footer_start] + new_footer + "\n" + content[footer_end:]
            
        # Replace title
        content = re.sub(r'<title>.*?</title>', '<title>Exellar Construction LLP | Building Mumbai\'s Skyline</title>', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Failed {file_path}: {e}")
