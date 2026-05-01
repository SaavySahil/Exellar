
with open('css/style.css', 'r') as f:
    content = f.read()

old_css = '.cta-close{color:#fff;font-family:apercu-medium-pro;font-size:14px;font-weight:500;left:39px;letter-spacing:.04em;position:absolute;text-transform:uppercase;top:50%;-webkit-transform:rotate(-90deg) translate(-50%,-50%);-ms-transform:rotate(-90deg) translate(-50%,-50%);transform:rotate(-90deg) translate(-50%,-50%)}'
new_css = '.cta-close{color:#fff;font-family:apercu-medium-pro;font-size:14px;font-weight:500;left:25px;letter-spacing:.04em;position:absolute;text-transform:uppercase;top:50%;-webkit-transform:translate(-50%,-50%) rotate(-90deg);-ms-transform:translate(-50%,-50%) rotate(-90deg);transform:translate(-50%,-50%) rotate(-90deg)}'

if old_css in content:
    new_content = content.replace(old_css, new_css)
    with open('css/style.css', 'w') as f:
        f.write(new_content)
    print("Successfully replaced.")
else:
    print("Old CSS string not found exactly. Replacement failed.")
    # Fallback: check if it's slightly different
    import re
    # Just in case there are variations in spacing (though it's minified)
    pattern = re.escape(old_css).replace(r'\{', r'\{').replace(r'\}', r'\}')
    if re.search(pattern, content):
        print("Found with regex (wait, regex should match exactly here).")
