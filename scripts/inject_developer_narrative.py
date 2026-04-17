import os

target_file = 'Home.html'

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Update the About Strip (Mumbai & Pune) to include the Developer Narrative and Client dropping
old_about_title = "Building Across Maharashtra's Most Iconic Skylines"
new_about_title = "From Master Builders to Visionary Developers"

old_about_para = "From high-rise towers in Andheri to rehabilitation projects in Pune, Exellar Construction has been shaping Maharashtra's built environment for over six decades."
new_about_para = "For over 60 years, we have been the execution engine behind Mumbai and Pune's skyline, trusted by titans like Lodha, Rustomjee, and Kalpataru. Now, we are leveraging our zero-compromise contracting expertise to transition into premium real estate development. We build for the best—soon, we build for you."

content = content.replace(old_about_title, new_about_title)
content = content.replace(old_about_para, new_about_para)

# Update the CTA popup "A Project" to pitch JVs/Development
old_cta_para = "We undertake high-rise construction, rehabilitation, and infrastructure projects across Mumbai and Pune with precision and commitment."
new_cta_para = "We undertake turnkey real estate development, high-rise construction, and complex JVs across Mumbai and Pune with unmatched precision."

content = content.replace(old_cta_para, new_cta_para)

# Update the Hero CTA text from "What do you want to build?" to something more JV/Developer focused?
# Let's leave that for now, "What do you want to build?" is still an excellent hook.

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully injected the Developer Narrative and BRD facts into Home.html!")
