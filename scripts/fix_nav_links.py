import glob
import re

# Map nav item text → correct HTML file
# These are anchor tags where the text matches these labels
nav_map = {
    'Our Leadership':                        'Leadship.html',
    'Market Sectors':                        'market-sectors.html',
    'Affiliates':                            'affiliates.html',
    'Locations':                             'locations.html',
    'Our ESG Strategy':                      'our-esg-strategy.html',
    'Community and Citizenship':             'community-citizenship.html',
    'Diversity, Equity, and Inclusion':      'diversity-equity-inclusion.html',
    'Environmental Sustainability and Resiliency': 'environmental-sustainability-and-resiliency.html',
    'Ethics and Compliance':                 'ethics-and-compliance.html',
    'Innovation':                            'innovation.html',
    'Safety and Wellness':                   'safety-and-wellness.html',
    'General Inquiries':                     'contact-us.html',
    'Learn How':                             'contact-us.html',
    'Become a Subcontractor':                'contact-us.html',
}

html_files = glob.glob('*.html')
total_fixed = 0

for filepath in sorted(html_files):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    original = content

    for label, target_file in nav_map.items():
        # Match <a href="...">...<text>...</a> patterns in nav/submenu context
        # Replace href inside <a> tags that contain the label text
        # Pattern: <a href="..."> WHITESPACE label WHITESPACE </a>
        pattern = r'(<a\s[^>]*href=")[^"]*("(?:[^>]*)>\s*' + re.escape(label) + r'\s*</a>)'
        replacement = r'\g<1>' + target_file + r'\2'
        new_content, n = re.subn(pattern, replacement, content, flags=re.IGNORECASE | re.DOTALL)
        if n > 0:
            total_fixed += n
            content = new_content

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'[{filepath}] updated nav links')

print(f'\nTotal link fixes: {total_fixed}')
