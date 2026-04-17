import os, glob

# 1. Remove exellar-theme.css linking from all HTML files
for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove lines containing exellar-theme.css
    lines = content.split('\n')
    filtered_lines = [line for line in lines if 'exellar-theme.css' not in line]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(filtered_lines))

# 2. Append ONLY the critical spacing/trust-bar fix to style.css so the layout doesn't break
css_path = 'css/style.css'
if os.path.exists(css_path):
    with open(css_path, 'r', encoding='utf-8') as f:
        style_css_content = f.read()
        
    trust_bar_fix = """
/* Critical Spacing Fixes */
.trust-bar-logos {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    gap: 40px;
    padding: 30px 0 60px 0;
}
.trust-bar-logos span {
    opacity: 0.7;
    transition: opacity 0.3s;
}
.trust-bar-logos span:hover {
    opacity: 1;
}

.home-slider-txt-before {
    margin-bottom: 50px;
}
"""
    if ".trust-bar-logos" not in style_css_content:
        with open(css_path, 'a', encoding='utf-8') as f:
            f.write(trust_bar_fix)

print("Removed exellar-theme.css linking and migrated structural fixes to style.css")
