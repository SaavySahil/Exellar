"""
Phase 3 — Final cleanup of remaining Turner references across all HTML files.
"""
import re, glob

files = glob.glob('*.html')
total = 0

for filepath in sorted(files):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    orig = content

    # 1. Fix offsite manufacturing link (in nav submenu across all pages)
    content = content.replace(
        'https://www.turnerconstruction.com/services/xpl-offsite',
        'Services.html'
    )

    # 2. Fix Turner careers links in contact-us.html and others
    content = content.replace(
        'https://turnerconstruction.com/careers',
        'Careers.html'
    )
    content = re.sub(
        r'https://turnerconstruction\.csod\.com/[^"\'>\s]+',
        'Careers.html',
        content
    )

    # 3. Fix "For more information about working at Turner" text
    content = content.replace(
        'For more information about working at Turner, please visit our',
        'For more information about working at Exellar, please visit our'
    )
    content = content.replace(
        'To search current job openings throughout the United States, Canada and Internationally, visit our job postings',
        'To view current job openings across our Mumbai and Pune operations, visit our'
    )
    content = content.replace(
        'at this link',
        'Careers page'
    )

    # 4. Fix media contact (Chris McFadden / tcco.com PR contact)
    content = re.sub(
        r'Chris McFadden<br>Vice President, Communications<br>cmcfadden@tcco\.com<br>\(212\) 229-6145',
        'Media Relations Team<br>Exellar Construction LLP<br>media@exellar.co.in<br>+91 22 6600 0000',
        content
    )

    # 5. Fix any remaining @tcco.com emails
    content = re.sub(
        r'[a-zA-Z0-9._%+\-]+@tcco\.com',
        'info@exellar.co.in',
        content
    )

    # 6. Fix remaining ethics hotline text in contact-us.html
    content = content.replace(
        "Report issues 24 hours a day, 7 days a week to Turner's <strong>Confidential Reporting System</strong>",
        "Report concerns to our Ethics &amp; Compliance team, available Monday to Saturday"
    )
    content = content.replace(
        '1-888-738-1924',
        '+91 98200 00000'
    )
    # Fix the anchor text that still shows the Turner URL
    content = re.sub(
        r'>turnerconstruction\.ethicspoint\.com<',
        '>ethics@exellar.co.in<',
        content
    )

    # 7. Fix Business Unit page.html contact names (Turner exec names)
    turner_execs = [
        ('dblackwood', 'Solanki, A.J.'),
        ('nsevier',    'Solanki, A.G.'),
        ('amiles',     'Solanki, A.S.'),
        ('josmiller',  'Solanki, A.K.'),
        ('ejanney',    'Team'),
    ]
    for old_name, new_name in turner_execs:
        content = re.sub(
            rf'href="mailto:{old_name}@exellar\.co\.in">{old_name}@exellar\.co\.in',
            f'href="mailto:info@exellar.co.in">info@exellar.co.in',
            content
        )
        # Also catch original tcco form if any slipped through
        content = re.sub(
            rf'href="mailto:{old_name}@tcco\.com">{old_name}@tcco\.com',
            f'href="mailto:info@exellar.co.in">info@exellar.co.in',
            content
        )

    # 8. Fix Careers.html and Article Template.html Turner body text
    content = content.replace(
        "Turner Construction Company is building a world of difference",
        "Exellar Construction LLP is building a stronger India"
    )
    content = content.replace(
        "Turner is an Equal Opportunity Employer",
        "Exellar is an Equal Opportunity Employer"
    )
    content = content.replace(
        "At Turner, we are committed",
        "At Exellar, we are committed"
    )
    content = content.replace(
        "Turner employees",
        "Exellar employees"
    )
    content = content.replace(
        "Turner team",
        "Exellar team"
    )
    content = content.replace(
        "At Turner",
        "At Exellar"
    )
    content = content.replace(
        "Join Turner",
        "Join Exellar"
    )
    content = content.replace(
        "Turner is",
        "Exellar is"
    )
    content = content.replace(
        "Turner has",
        "Exellar has"
    )
    content = content.replace(
        "Turner offers",
        "Exellar offers"
    )
    content = content.replace(
        "Turner provides",
        "Exellar provides"
    )
    content = content.replace(
        "Turner's projects",
        "Exellar's projects"
    )
    content = content.replace(
        "Turner's commitment",
        "Exellar's commitment"
    )
    content = content.replace(
        "Turner's approach",
        "Exellar's approach"
    )
    content = content.replace(
        "Turner's culture",
        "Exellar's culture"
    )
    content = content.replace(
        "Turner's workforce",
        "Exellar's workforce"
    )
    content = content.replace(
        "Turner's safety",
        "Exellar's safety"
    )
    content = content.replace(
        "Turner's values",
        "Exellar's values"
    )
    # Remaining "Turner" standalone references in body text
    content = re.sub(
        r'\bTurner\b(?! Construction LLP)',
        'Exellar',
        content
    )

    # 9. Fix remaining ep-turnerconstruction-prod CDN images
    content = re.sub(
        r'(data-src|src)="https://ep-turnerconstruction-prod[^"]*"',
        r'\1="images/project-placeholder.jpg"',
        content
    )
    content = re.sub(
        r"background-image:\s*url\('https://ep-turnerconstruction-prod[^']*'\)",
        "background-image: url('images/project-placeholder.jpg')",
        content
    )

    # 10. Fix Services.html remaining CDN images
    content = re.sub(
        r'(data-src|src)="https://ep-[^"]*turnerconstruction[^"]*"',
        r'\1="images/project-placeholder.jpg"',
        content
    )

    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'[UPDATED] {filepath}')
        total += 1

print(f'\nPhase 3 complete: {total} files updated')
