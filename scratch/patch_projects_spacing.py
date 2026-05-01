
import re

with open('css/style.css', 'r') as f:
    content = f.read()

# Target the .offices-cta rule
# Original: .offices-cta{border-bottom:1px solid #DBDBDB;border-top:1px solid #DBDBDB;display:-webkit-box;display:-ms-flexbox;display:flex;margin:0 auto;max-width:50vw}
pattern = r'\.offices-cta\{border-bottom:1px solid #DBDBDB;border-top:1px solid #DBDBDB;display:-webkit-box;display:-ms-flexbox;display:flex;margin:0 auto;max-width:50vw\}'
match = re.search(pattern, content)

if match:
    old_css = match.group(0)
    print(f"Found CSS: {old_css}")
    
    # Add margin-top: 50px
    new_css = old_css.replace('margin:0 auto', 'margin:50px auto 0')
    
    new_content = content.replace(old_css, new_css)
    with open('css/style.css', 'w') as f:
        f.write(new_content)
    print(f"Successfully replaced with: {new_css}")
else:
    print("CSS pattern not found. Trying flexible search...")
    # Flexible search just in case
    pattern_flex = r'\.offices-cta\{[^}]*margin:0 auto;[^}]*\}'
    match_flex = re.search(pattern_flex, content)
    if match_flex:
        old_css = match_flex.group(0)
        print(f"Found flexible CSS: {old_css}")
        new_css = old_css.replace('margin:0 auto', 'margin:50px auto 0')
        new_content = content.replace(old_css, new_css)
        with open('css/style.css', 'w') as f:
            f.write(new_content)
        print("Successfully replaced.")
    else:
        print("Still not found.")
