import os

css_path = 'css/exellar-theme.css'

with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Add styling for trust bar
trust_bar_css = """
/* Fix Trust Bar Styling & Spacing */
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

/* Fix Section Spacing & Float Collapse */
.office-cols {
    display: flex !important;
    flex-wrap: wrap;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 50px;
}
.office-cols .inline_block {
    float: none !important;
}
.v-top {
    align-items: flex-start !important;
}

/* Override the old arrow links with solid buttons */
.btn-link, .link-button {
    background-color: var(--primary-orange) !important;
    color: #ffffff !important;
    padding: 14px 28px !important;
    border-radius: 4px !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 12px !important;
    text-transform: uppercase;
    font-size: 14px;
    letter-spacing: 0.5px;
    margin-top: 20px;
}
"""

if ".trust-bar-logos" not in css_content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(trust_bar_css)

html_path = 'Home.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

# Replace trust bar div
html_content = html_content.replace(
    '<div class="anim-block" style="text-align:center;">\n            <span class="inline_block vm bx" style="padding:14px 24px;">',
    '<div class="anim-block trust-bar-logos" style="text-align:center;">\n            <span class="inline_block vm bx" style="padding:14px 24px;">'
)

# Ensure sections have proper bottom padding
html_content = html_content.replace('<section class="section-padding prel" style="border-top:1px solid #e2e8f0;">', '<section class="section-padding prel" style="border-top:1px solid #e2e8f0; margin-bottom: 60px; padding-top: 100px; padding-bottom: 100px;">')
html_content = html_content.replace('<section class="section-padding prel">', '<section class="section-padding prel" style="margin-bottom: 60px; padding-top: 100px; padding-bottom: 100px;">')
html_content = html_content.replace('<section class="section-padding bg-grey prel">', '<section class="section-padding bg-grey prel" style="margin-bottom: 60px; padding-top: 80px; padding-bottom: 80px;">')


with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Fixed spacing and trust bar styling")
