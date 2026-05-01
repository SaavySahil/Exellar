
import re

with open('css/style.css', 'r') as f:
    content = f.read()

pattern = r'\.cta-close\{[^\}]+\}'
match = re.search(pattern, content)

if match:
    old_css = match.group(0)
    print(f"Found CSS: {old_css}")
    
    # New values
    new_css = old_css.replace('left:45px', 'left:20px')
    # If it was 39px before (just in case)
    new_css = new_css.replace('left:39px', 'left:20px')
    
    # Ensure transform is correct
    if 'translate(-50%,-50%) rotate(-90deg)' not in new_css:
        new_css = re.sub(r'transform:[^;\}]+', 'transform:translate(-50%,-50%) rotate(-90deg)', new_css)
        new_css = re.sub(r'-webkit-transform:[^;\}]+', '-webkit-transform:translate(-50%,-50%) rotate(-90deg)', new_css)
        new_css = re.sub(r'-ms-transform:[^;\}]+', '-ms-transform:translate(-50%,-50%) rotate(-90deg)', new_css)

    new_content = content.replace(old_css, new_css)
    with open('css/style.css', 'w') as f:
        f.write(new_content)
    print(f"Successfully replaced with: {new_css}")
else:
    print("CSS pattern not found.")
