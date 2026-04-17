import glob

html_files = glob.glob('*.html')
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Safely rebrand without hitting classnames like 'turner-slider'
    content = content.replace('images/turner-logo.svg', 'images/exellar-logo.png')
    content = content.replace('images/turner-logo-dark.svg', 'images/exellar-logo.png')
    content = content.replace('turner-mega.png', 'project-placeholder.jpg')
    
    content = content.replace('Turner Construction Company', 'Exellar Construction LLP')
    content = content.replace('Turner Construction', 'Exellar Construction')
    content = content.replace('>Turner<', '>Exellar<')
    content = content.replace(' Turner ', ' Exellar ')
    content = content.replace('Turner,', 'Exellar,')
    content = content.replace('Turner.', 'Exellar.')
    
    # Minimal Sitemap naming adjustments (target >Text< inside tags)
    content = content.replace('>Our Company<', '>About Us<')
    content = content.replace('>News &amp; Insights<', '>Case Studies<')
    content = content.replace('>News & Insights<', '>Case Studies<')
    content = content.replace('>Life At Turner<', '>Careers<')
    content = content.replace('>Life at Turner<', '>Careers<')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

print("Safely rebranded text without breaking HTML classes!")
