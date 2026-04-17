import glob
import re

# Step 1: Normalize all variant labels to canonical versions (matching screenshot)
label_normalizations = {
    'Our Excellence Strategy':                  'Our ESG Strategy',
    'Integrity and Citizenship':                'Community and Citizenship',
    'Workforce First Sustainability and Resiliency': 'Environmental Sustainability and Resiliency',
    'Life At Turner':                           'Life at Exellar',
    'Turner Careers':                           'Exellar Careers',
    'Exellar Careers':                          'Exellar Careers',  # keep
}

# Step 2: Map canonical label → correct HTML file
nav_link_map = {
    'About Us':                                   'About-us.html',
    'Our Leadership':                             'Leadship.html',
    'Market Sectors':                             'market-sectors.html',
    'Affiliates':                                 'affiliates.html',
    'Locations':                                  'locations.html',
    'Our ESG Strategy':                           'our-esg-strategy.html',
    'Community and Citizenship':                  'community-citizenship.html',
    'Diversity, Equity, and Inclusion':           'diversity-equity-inclusion.html',
    'Environmental Sustainability and Resiliency':'environmental-sustainability-and-resiliency.html',
    'Ethics and Compliance':                      'ethics-and-compliance.html',
    'Innovation':                                 'innovation.html',
    'Safety and Wellness':                        'safety-and-wellness.html',
    'General Inquiries':                          'contact-us.html',
    'Learn How':                                  'contact-us.html',
    'Become a Subcontractor':                     'contact-us.html',
    'Preconstruction':                            'preconstruction.html',
    'Construction Management':                    'construction-management.html',
    'Project Management':                         'project-management.html',
    'Lean Construction':                          'lean-construction.html',
    'Life at Exellar':                            'Life at Company.html',
    'Exellar Careers':                            'Careers.html',
    'Students & Entry Level':                     'Careers.html',
    'Experienced Professionals':                  'Careers.html',
    'Labor & Skilled Trade':                      'Careers.html',
    'Military Professionals':                     'Careers.html',
}

html_files = glob.glob('*.html')
total_changes = 0

for filepath in sorted(html_files):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    original = content

    # Step 1: Normalize labels (text replacement inside <a> tags)
    for old_label, new_label in label_normalizations.items():
        if old_label == new_label:
            continue
        # Replace inside anchor tags (handles both desktop and mobile menus)
        pattern = r'(>)\s*' + re.escape(old_label) + r'\s*(<)'
        content, n = re.subn(pattern, r'\g<1>' + new_label + r'\2', content)
        if n:
            total_changes += n

    # Step 2: Fix hrefs based on link text
    for label, target in nav_link_map.items():
        # Pattern: <a href="ANYTHING">WHITESPACE label WHITESPACE</a>
        pattern = r'(<a\s[^>]*href=")[^"]*("(?:[^>]*)>\s*)' + re.escape(label) + r'(\s*</a>)'
        replacement = r'\g<1>' + target + r'\2' + label + r'\3'
        new_content, n = re.subn(pattern, replacement, content, flags=re.IGNORECASE)
        if n:
            total_changes += n
            content = new_content

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'[{filepath}] updated')

print(f'\nTotal changes: {total_changes}')
