"""
Phase 1 — Global batch fixes across all HTML pages.
Rules: content text only, no class/style changes.
"""
import re, glob

files = glob.glob('*.html')
total = 0

# ── Page title map ──────────────────────────────────────────────────────────
title_map = {
    'Home.html':                                        'Home | Exellar Construction LLP',
    'About-us.html':                                    'About Us | Exellar Construction LLP',
    'Services.html':                                    'Our Services | Exellar Construction LLP',
    'Projects.html':                                    'Our Projects | Exellar Construction LLP',
    'Careers.html':                                     'Careers | Exellar Construction LLP',
    'contact-us.html':                                  'Contact Us | Exellar Construction LLP',
    'insights.html':                                    'Insights | Exellar Construction LLP',
    'Leadship.html':                                    'Our Leadership | Exellar Construction LLP',
    'Life at Company.html':                             'Life at Exellar | Exellar Construction LLP',
    'Fruad-alert.html':                                 'Fraud Alert | Exellar Construction LLP',
    'Privacy Policy.html':                              'Privacy Policy | Exellar Construction LLP',
    'certifications.html':                              'Certifications | Exellar Construction LLP',
    'Clients.html':                                     'Our Clients | Exellar Construction LLP',
    'Article Template.html':                            'Insights | Exellar Construction LLP',
    'Business Unit page.html':                          'Business Units | Exellar Construction LLP',
    'Project Page.html':                                'Project Detail | Exellar Construction LLP',
    'Project Page 2.html':                              'Project Detail | Exellar Construction LLP',
    'construction-management.html':                     'Construction Management | Exellar Construction LLP',
    'preconstruction.html':                             'Preconstruction | Exellar Construction LLP',
    'project-management.html':                          'Project Management | Exellar Construction LLP',
    'lean-construction.html':                           'Lean Construction | Exellar Construction LLP',
    'innovation.html':                                  'Innovation | Exellar Construction LLP',
    'safety-and-wellness.html':                         'Safety & Wellness | Exellar Construction LLP',
    'environmental-sustainability-and-resiliency.html': 'Environmental Sustainability | Exellar Construction LLP',
    'ethics-and-compliance.html':                       'Ethics & Compliance | Exellar Construction LLP',
    'market-sectors.html':                              'Market Sectors | Exellar Construction LLP',
    'affiliates.html':                                  'Affiliates | Exellar Construction LLP',
    'locations.html':                                   'Our Locations | Exellar Construction LLP',
    'our-esg-strategy.html':                            'Our ESG Strategy | Exellar Construction LLP',
    'community-citizenship.html':                       'Community & Citizenship | Exellar Construction LLP',
    'diversity-equity-inclusion.html':                  'Diversity, Equity & Inclusion | Exellar Construction LLP',
}

for filepath in sorted(files):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    orig = content

    # 1. Fix page title
    if filepath in title_map:
        content = re.sub(r'<title>[^<]+</title>', f'<title>{title_map[filepath]}</title>', content)

    # 2. Fix JS root variables — remove Turner-specific values
    content = re.sub(
        r"var _webroot\s*=\s*'[^']*';",
        "var _webroot = '';",
        content
    )
    content = re.sub(
        r"var _here\s*=\s*'[^']*';",
        "var _here = '';",
        content
    )
    content = re.sub(
        r"var _controller\s*=\s*'[^']*';",
        "var _controller = '';",
        content
    )
    content = re.sub(
        r"var _action\s*=\s*'[^']*';",
        "var _action = '';",
        content
    )

    # 3. Fix contact form action endpoint
    content = content.replace(
        'action="/contact-us/handle-contact-form-request"',
        'action="https://formspree.io/f/exellar" method="POST"'
    )

    # 4. Fix Turner email in contact popup / body
    content = content.replace('turner@tcco.com', 'info@exellar.co.in')
    content = content.replace('Turner@tcco.com', 'info@exellar.co.in')

    # 5. Fix remaining CDN images in body (data-src and src attributes)
    content = re.sub(
        r'(data-src|src)="https://ep-turnerconstruction-prod[^"]*"',
        r'\1="images/project-placeholder.jpg"',
        content
    )
    # Also background-image inline style from Turner CDN (in body only)
    content = re.sub(
        r"background-image:\s*url\('https://ep-turnerconstruction-prod[^']*'\)",
        "background-image: url('images/project-placeholder.jpg')",
        content
    )

    # 6. Fix Turner phone numbers in contact popup
    content = content.replace('(212) 229-6000', '+91 22 6600 0000')
    content = content.replace('+1-212-229-6000', '+91-22-6600-0000')
    content = content.replace('href="tel:+1-212-229-6000"', 'href="tel:+912266000000"')
    content = content.replace('(888) 738-1924', '+91 98200 00000')
    content = content.replace('+1-888-738-1924', '+91-98200-00000')
    content = content.replace('href="tel:+1-888-738-1924"', 'href="tel:+919820000000"')

    # 7. Fix Turner HQ address in contact popup
    content = content.replace('Turner Construction Company', 'Exellar Construction LLP')
    content = content.replace('66 Hudson Boulevard East', 'Andheri West')
    content = content.replace('New York, NY 10001', 'Mumbai, Maharashtra 400053')
    content = content.replace('Headquarters', 'Head Office')

    # 8. Fix Ethics hotline reference in contact popup
    content = content.replace(
        "Report issues 24 hours a day, 7 days a week to Turner's Confidential Reporting System",
        "Report concerns to our Ethics & Compliance team, available Monday to Saturday."
    )
    content = content.replace(
        'https://turnerconstruction.ethicspoint.com',
        'mailto:ethics@exellar.co.in'
    )

    # 9. Fix GTM container ID comment text (not removing GTM, just leaving it)
    # Keep GTM as-is — removing would affect analytics structure

    # 10. Fix remaining "Turner Construction Company" text in <p> body tags
    content = re.sub(
        r'<p([^>]*)>\s*Turner Construction Company\s*</p>',
        r'<p\1>Exellar Construction LLP</p>',
        content
    )

    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        changes = sum([
            content.count('Exellar Construction LLP') - orig.count('Exellar Construction LLP'),
        ])
        print(f'[UPDATED] {filepath}')
        total += 1

print(f'\nPhase 1 complete: {total} files updated')
