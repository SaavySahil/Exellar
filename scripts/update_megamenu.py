import os, glob

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Megamenu About Us
    old_about = "Turner is a North America-based, international construction services company and is a leading builder in diverse market segments."
    new_about = "Exellar Construction LLP is a premium master builder and developer based in Mumbai & Pune, shaping Maharashtra's skyline for over 60 years."
    content = content.replace(old_about, new_about)

    # Update Megamenu Services
    old_services = "Our people bring their technical knowledge, experience, and resourcefulness to the delivery of our construction services. Our expertise and value-added offerings support our clients throughout the lifespan of the construction process."
    new_services = "We bring unmatched zero-compromise execution to every development. From structural rehabilitation to high-rise turnkey execution, we control the entire supply chain."
    content = content.replace(old_services, new_services)

    # Update Megamenu Projects
    old_portfolio = "As the largest general contractor in the country, Exellar is a leader in all major market segments, including healthcare, education, commercial, sports, aviation, pharmaceutical, retail and green building."
    new_portfolio = "As a dominant player in Maharashtra, Exellar leads the construction and premium development of high-rises, commercial parks, and structural rehabilitation projects."
    content = content.replace(old_portfolio, new_portfolio)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated global megamenu content.")
