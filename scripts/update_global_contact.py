import os, glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update the contact email
    content = content.replace('turner@tcco.com', 'info@exellar.co.in')
    
    # 2. Update address
    content = content.replace('66 Hudson Boulevard East', 'Mumbai &amp; Pune, Maharashtra')
    content = content.replace('New York, NY 10001', 'India')
    content = content.replace('New York, New York 10001', 'India')
    # If the address is split:
    # <p class="para fs-19 white">66 Hudson Boulevard East</p>
    # <p class="para fs-19 white">New York, NY 10001</p>
    
    # 3. Update telephone
    # <a href="tel:+1-212-229-6000" class="para fs-20 white block">
    #     (212) 229-6000
    # </a>
    content = content.replace('tel:+1-212-229-6000', 'mailto:info@exellar.co.in')
    content = content.replace('(212) 229-6000', 'info@exellar.co.in')
    content = content.replace('855-214-7480', 'info@exellar.co.in')
    
    # Remove random social links to turner
    content = content.replace('https://www.facebook.com/turnerconstruction', '#')
    content = content.replace('https://www.instagram.com/turnerconstructioncompany/', '#')
    content = content.replace('https://www.linkedin.com/company/turner-construction-company', '#')
    content = content.replace('https://www.youtube.com/@TurnerConstructionCo', '#')
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated global contact info and removed Turner social links.")
