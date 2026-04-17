import glob

html_files = glob.glob('*.html')
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Text replacements to safely rebrand without breaking elements
    content = content.replace('images/turner-logo.svg', 'images/exellar-logo.png')
    content = content.replace('images/turner-logo-dark.svg', 'images/exellar-logo.png')
    content = content.replace('turner-mega.png', 'project-placeholder.jpg')
    content = content.replace('Turner Construction Company', 'Exellar Construction LLP')
    content = content.replace('Turner Construction', 'Exellar Construction')
    content = content.replace('Turner', 'Exellar')
    content = content.replace('turner', 'exellar')
    content = content.replace('Our Company', 'About Us')
    content = content.replace('News & Insights', 'Case Studies')
    content = content.replace('Life At Exellar', 'Careers')
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print("Rebranding done!")
