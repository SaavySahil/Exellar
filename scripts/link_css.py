import os, glob

# For all .html files, ensure exellar-theme.css is linked right after style.css
for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if it's already there
    if 'css/exellar-theme.css' not in content:
        # Find where style.css is linked
        content = content.replace(
            '<link rel="stylesheet" href="css/style.css" crossorigin="anonymous">',
            '<link rel="stylesheet" href="css/style.css" crossorigin="anonymous">\n        <link rel="stylesheet" href="css/exellar-theme.css" crossorigin="anonymous">'
        )
        
        # If the file uses a different pattern for style.css
        if 'css/exellar-theme.css' not in content:
             content = content.replace(
                '<link rel="stylesheet" href="css/style.css">',
                '<link rel="stylesheet" href="css/style.css">\n    <link rel="stylesheet" href="css/exellar-theme.css" crossorigin="anonymous">'
            )
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

print("Injected exellar-theme.css into HTML head")
