import os

css_path = 'css/exellar-theme.css'

with open(css_path, 'a', encoding='utf-8') as f:
    f.write('''

/* --- EXELLAR COPYRIGHT PROTECTION LAYOUT REVERSALS --- */

/* 1. Center the Hero Content */
.hero-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    height: 100vh;
}
.hero-title {
    text-align: center;
    margin: 0 auto;
}

/* 2. Reverse the Insights/Innovation Split Screen */
.home-innovation .home-wrapper {
    display: flex !important;
    flex-direction: row-reverse !important;
    justify-content: space-between !important;
    gap: 40px;
}
@media (max-width: 1024px) {
    .home-innovation .home-wrapper {
        flex-direction: column !important;
    }
}

/* 3. Reverse the 'About Us' Strip (Mumbai & Pune) */
.home-office .office-cols {
    display: flex !important;
    flex-direction: row-reverse !important;
    align-items: center;
}
.home-office .office-cols .inline_block {
    float: none !important;
}

/* 4. 'Life at Exellar' Strip: Keep it normal, but add custom background to differentiate */
.life-at-turner {
    background-color: var(--primary-blue) !important;
    padding: 100px 0 !important;
}
.life-at-turner h2, .life-at-turner h3, .life-at-turner p {
    color: #ffffff !important;
}

/* 5. Force major images to have rounded corners (Premium Developer Look) */
.img-credit span img, .to-be-scaled img {
    border-radius: 12px !important;
    box-shadow: 0 20px 40px -10px rgba(0,0,0,0.3) !important;
}

/* 6. Change Services Tabs layout on desktop */
.home-commitments .home-wrapper {
    display: flex;
    flex-direction: column;
}
.commitments-small-col {
    width: 100% !important;
    margin-bottom: 40px;
}
.block-slider-container {
    width: 100% !important;
}
.blue-slider-controls-drop {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: wrap;
    gap: 15px;
}
.blue-slider-controls-row {
    flex: 1 1 calc(33% - 15px);
    background: var(--primary-blue) !important;
    border-radius: 8px;
    padding: 15px !important;
    text-align: center;
}
.commitments-big-col {
    width: 100% !important;
}

''')

print("Added Copyright Protection Layout Reversals to css/exellar-theme.css")
