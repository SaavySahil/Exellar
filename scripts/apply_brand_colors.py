"""
Apply Exellar brand colors to style.css by replacing Turner's hardcoded hex values.

Turner → Exellar mapping:
  #0b5dd0  (Turner interactive blue, 68x) → #3E5BA9  (Exellar secondary brand)
  #17171b  (Turner near-black text, 73x)  → #2E2E2E  (Exellar primary text)
  #012471  (Turner dark navy, 4x)         → #23235F  (Exellar primary brand)
  #ff4026  (Turner orange-red CTA, 26x)   → #C62828  (Exellar accent/CTA)
  #f6f6f6  (Turner off-white bg, 13x)     → #F6F5F3  (Exellar secondary bg)
  #dcdcdc  (Turner neutral grey, 74x)     → #DBDBDB  (Exellar structural neutral)
  #bfd2e4  (Turner footer link blue, 7x)  → #a8bbd8  (muted version of #3E5BA9)
  #a90707  (Turner dark red, 2x)          → #C62828  (Exellar accent)
  #cb2027  (Turner dark red variant, 1x)  → #C62828  (Exellar accent)
  #0d66e3  (Turner link blue variant, 1x) → #3E5BA9  (Exellar secondary)
  #106dc3  (Turner link blue variant, 1x) → #3E5BA9  (Exellar secondary)
  #4285f4  (Google blue — leave)
  #0d0a0a  (near black, 2x)              → #2E2E2E  (Exellar primary text)
  #73737b  (mid grey — keep)
"""

import re, shutil

CSS_FILE = 'css/style.css'

# Make backup once
shutil.copy(CSS_FILE, CSS_FILE + '.bak')

with open(CSS_FILE, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

orig = content

# Order matters: do longer/more-specific matches first to avoid partial replacements
replacements = [
    # Turner interactive / link blue → Exellar secondary brand blue
    ('#0b5dd0', '#3E5BA9'),
    ('#0B5DD0', '#3E5BA9'),
    # Turner near-black text → Exellar primary text
    ('#17171b', '#2E2E2E'),
    ('#17171B', '#2E2E2E'),
    # Turner dark navy → Exellar primary brand navy
    ('#012471', '#23235F'),
    # Turner orange-red CTA → Exellar red CTA
    ('#ff4026', '#C62828'),
    ('#FF4026', '#C62828'),
    # Turner off-white → Exellar secondary background
    ('#f6f6f6', '#F6F5F3'),
    ('#F6F6F6', '#F6F5F3'),
    # Turner neutral grey → Exellar structural neutral (very close, safe swap)
    ('#dcdcdc', '#DBDBDB'),
    ('#DCDCDC', '#DBDBDB'),
    # Turner footer link blue → muted Exellar blue (keeps legibility on dark footer)
    ('#bfd2e4', '#a8bbd8'),
    ('#BFD2E4', '#a8bbd8'),
    # Turner dark red variants → Exellar accent red
    ('#a90707', '#C62828'),
    ('#A90707', '#C62828'),
    ('#cb2027', '#C62828'),
    ('#CB2027', '#C62828'),
    # Turner blue link variants → Exellar secondary blue
    ('#0d66e3', '#3E5BA9'),
    ('#0D66E3', '#3E5BA9'),
    ('#106dc3', '#3E5BA9'),
    ('#106DC3', '#3E5BA9'),
    # Near black → Exellar primary text
    ('#0d0a0a', '#2E2E2E'),
    ('#0D0A0A', '#2E2E2E'),
    # Swiper theme color → Exellar secondary blue
    ('#007aff', '#3E5BA9'),
    ('#007AFF', '#3E5BA9'),
]

for old, new in replacements:
    before = content.count(old)
    content = content.replace(old, new)
    after_count = content.count(old.lower()) + content.count(old.upper())
    if before:
        print(f'  {old} -> {new}  ({before}x replaced)')

with open(CSS_FILE, 'w', encoding='utf-8') as f:
    f.write(content)

changes = sum(1 for a, b in zip(orig, content) if a != b)
print(f'\nstyle.css updated. Backup saved as style.css.bak')
