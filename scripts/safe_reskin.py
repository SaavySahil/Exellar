import os

style_path = os.path.join('css', 'style.css')
with open(style_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace Fonts
css = css.replace('apercu-extralight-pro', 'Montserrat')
css = css.replace('apercu-light-pro', 'Inter')
css = css.replace('apercu-regular-pro', 'Inter')
css = css.replace('apercu-medium-pro', 'Montserrat')
css = css.replace('apercu-bold-pro', 'Montserrat')
# We need to add the import at the top
if "@import url('https://fonts.googleapis.com" not in css:
    css = "@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Montserrat:wght@300;400;500;700&display=swap');\n" + css

# Replace Colors
# Main Blue -> Exellar Dark Blue
css = css.replace('#0b5dd0', '#0f2027')
css = css.replace('#001e6a', '#081317')

# Red/Orange -> Exellar Construction Orange
css = css.replace('#ff4026', '#ea580c')
css = css.replace('255,64,38', '234,88,12')  # if there's rgb

# Write back
with open(style_path, 'w', encoding='utf-8') as f:
    f.write(css)
print("Safely reskinned style.css!")
