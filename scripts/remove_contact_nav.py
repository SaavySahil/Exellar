import os, glob, re

files = glob.glob('*.html')
pattern = r'[ \t]*<div class="header-li">\s*<a class="header-link" href="contact-us\.html"[^>]*>\s*Contact Us\s*</a>\s*</div>'

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    new_content, count = re.subn(pattern, '', content)
    
    if count > 0:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Removed from {f}")
