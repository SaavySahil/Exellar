
import re

with open('css/style.css', 'r') as f:
    content = f.read()

# Using regex to find the .cta-close rule regardless of small character variations
pattern = r'\.cta-close\{[^\}]+\}'
match = re.search(pattern, content)

if match:
    old_css = match.group(0)
    print(f"Found CSS: {old_css}")
    
    # Construct new CSS
    # We want to change left:39px to left:25px
    # and fix the transform
    new_css = old_css.replace('left:39px', 'left:25px')
    
    # Fix transform order
    # Old: transform:rotate(-90deg) translate(-50%,-50%)
    # New: transform:translate(-50%,-50%) rotate(-90deg)
    new_css = new_css.replace('rotate(-90deg) translate(-50%,-50%)', 'translate(-50%,-50%) rotate(-90deg)')
    
    new_content = content.replace(old_css, new_css)
    with open('css/style.css', 'w') as f:
        f.write(new_content)
    print("Successfully replaced.")
else:
    print("CSS pattern not found.")
