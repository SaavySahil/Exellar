import re

target_file = 'Home.html'

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Flip the 'home-innovation' (Insights) section: Put slider on the left, big image on the right.
# The structure is:
# <div class="home-wrapper f0 anim-block">
#    <div class="innovation-big-col ...">...</div>
#    <div class="innovation-small-col ...">...</div>
# </div>
big_col_match = re.search(r'(<div class="innovation-big-col[^>]*>.*?</a>\s*</div>)', content, re.DOTALL)
small_col_match = re.search(r'(<div class="innovation-small-col[^>]*>.*?</div>\s*</div>\s*</div>)', content, re.DOTALL)

if big_col_match and small_col_match:
    big_col = big_col_match.group(1)
    small_col = small_col_match.group(1)
    
    # We want to replace the whole block with the small col first, then big col.
    # To do this safely, we find the entire wrapper and reconstruct it.
    wrapper_match = re.search(r'(<div class="home-wrapper f0 anim-block">)(.*?)(</section>)', content, re.DOTALL)
    if wrapper_match:
        # Just use some CSS classes to reverse the flex direction instead of risky regex DOM swapping!
        pass

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)
