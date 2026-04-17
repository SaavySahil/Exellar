# Exellar Codebase — Comprehensive Analysis

## 🏗️ Project Overview

**What it is:** A **static HTML website** for **Turner Construction Company** — one of the largest general contractors in North America. This is a local copy/export of the turnerconstruction.com website front-end, likely extracted for redesign or client handoff purposes ("Exellar" appears to be the project/agency name).

**Type:** Pure static front-end — no framework, no build system, no server-side code.

---

## 📁 Directory Structure

```
Exellar/
├── css/
│   └── style.css          (371 KB — single minified stylesheet)
├── js/
│   ├── app.js             (55 KB — main bundled app logic, Webpack chunk)
│   ├── vendor.js          (503 KB — jQuery, Swiper, GSAP + dependencies)
│   ├── gtm.js             (423 KB — Google Tag Manager bundle)
│   ├── embed.js           (19 KB — third-party embed helper)
│   ├── manifest.js        (3.5 KB — Webpack manifest)
│   ├── additional-polyfills.js
│   ├── api.js             (1 KB)
│   └── 065a0e6a...js      (140 KB — hashed chunk)
├── fonts/                 (Apercu Pro 5 weights + Rockness W05)
├── images/                (253 files — all production images/SVGs/icons)
├── media/
│   ├── 130-8s-peoplehero.mp4
│   └── 302-turner-web-hero-31825.mp4
└── *.html                 (23 pages)
```

---

## 📄 All 23 Pages

| File | Purpose |
|---|---|
| `Home.html` | Main homepage with hero video, sliders, megamenu |
| `About-us.html` | Company overview / who they are |
| `Leadship.html` | Executive & BU leadership profiles |
| `Business Unit page.html` | Regional/division BU page |
| `Services.html` | Service offerings with expandable hover columns |
| `Projects.html` | Portfolio listing with filter/search |
| `Project Page.html` | Individual project detail page |
| `Project Page 2.html` | Alternative project detail layout |
| `Careers.html` | Career listings and entry points |
| `Life at Company.html` | "Life at Turner" culture page |
| `insights.html` | News & insights listing |
| `Article Template.html` | Individual article/insight detail |
| `construction-management.html` | Service detail: Construction Management |
| `preconstruction.html` | Service detail: Preconstruction |
| `project-management.html` | Service detail: Project Management |
| `lean-construction.html` | Service detail: Lean Construction |
| `innovation.html` | Innovation commitment page |
| `safety-and-wellness.html` | Safety commitment page |
| `environmental-sustainability-and-resiliency.html` | ESG page |
| `ethics-and-compliance.html` | Ethics page |
| `contact-us.html` | Contact form page |
| `Privacy Policy.html` | Privacy policy text page |
| `Fruad-alert.html` | Fraud alert notice page |

---

## 🛠️ Tech Stack

### Core
| Layer | Technology |
|---|---|
| Markup | **HTML5** (semantic elements) |
| Styling | **Vanilla CSS** (single minified `style.css`) |
| Logic | **JavaScript (ES6+)** compiled via **Webpack** |
| Module bundler | **Webpack** (self.webpackChunk pattern) |

### JavaScript Libraries
| Library | Role |
|---|---|
| **jQuery** | DOM manipulation, AJAX, events throughout app.js |
| **GSAP 3** | All animations — timelines, tweens, ScrollTrigger |
| **ScrollTrigger** (GSAP plugin) | Scroll-linked animations and pinning |
| **Swiper.js** | All carousels and sliders (15+ instances) |
| **Lenis** | Smooth scroll library |
| **Blazy** | Lazy image loading with breakpoint-aware src switching |
| **LightGallery** v1.6.11 | Lightbox for media galleries |
| **Google Tag Manager** | Analytics/tracking (GTM-M593X6SF) |
| **Google reCAPTCHA** | Contact form spam protection |
| **Google Maps API** | Interactive office locator map |
| **MarkerClusterer** | Map marker clustering |

### Typography
- **Apercu Pro** — Primary typeface, self-hosted in 5 weights (ExtraLight, Light, Regular, Medium, Bold)
- **Rockness W05 Regular** — Decorative script font for accent headings

---

## 🎨 CSS Design System

### Color Palette
| Color | Hex | Usage |
|---|---|---|
| Turner Blue | `#0B5DD0` | Primary brand, links, accents |
| Turner Red/Orange | `#FF4026` | Accent, bullets, hover markers |
| Dark Navy | `#17171B` | Primary text |
| Gray | `#73737B` | Secondary text, labels |
| Light Gray | `#DCDCDC` | Borders, dividers |

### Grid System
Responsive column grid:
- `col-d-{n}` — Desktop columns
- `col-t-{n}` — Tablet (720–1024px)
- `col-m-{n}` — Mobile (< 719px)

### Breakpoints
| Name | Width |
|---|---|
| Mobile | `max-width: 719px` |
| Tablet | `720px – 1024px` |
| Desktop | `min-width: 1025px` |
| Large | `min-width: 1661px` |
| Ultra-wide | `min-width: 1921px` |

### Typography Classes
- `.title.fs-{n}` — Fluid heading sizes (30–160) using `vw` units
- `.para.fs-{n}` — Body text variants
- `.section-label` — Small uppercase label in blue
- `.txt-holder` — Rich text content block

### Animation System
- `.anim-block` / `.anim-elem` — Scroll-triggered animation containers
- Direction modifiers: `.top`, `.left`, `.right`, `.bottom`, `.scale`, `.top-50`, `.top-100`
- Delay modifiers: `.delay-01` through `.delay-3`
- CSS keyframes: `blink`, `slide-left`, `wave-animation`, `rotate-*`, `scale-*`, `top-*`, `x-2`

---

## ⚙️ JavaScript Architecture (`app.js`)

### Initialization Entry Points
- `p()` — General page initializer
- `F()` — Slider/carousel initializer (all Swiper instances)
- `ne()` — Home page specific initializer
- `me()` — Scroll animations and parallax initializer

### Header & Navigation
- **Sticky header**: `.sticky` class added at 77px scroll depth
- **Hide-on-scroll**: `.down-state` class slides header off screen when scrolling down
- **Megamenu**: GSAP animated open/close (y: -100 slide-down effect)
- **Desktop dropdowns**: Hover-driven with opacity + translateY
- **Overlay dimming**: `.total-wrapper.overlay` class pattern

### Sliders (Swiper.js instances)
| Selector | Description |
|---|---|
| `.cta-slider` | Auto-playing hero CTA slides |
| `.megamenu-slider` | Mega menu project slider (vertical on desktop) |
| `.slider-imgs` | Cross-fade image sliders |
| `.common-gallery` | Content galleries |
| `.related-slider` | Related content (4-up on desktop) |
| `.quotes-slider` | Quote/testimonial slider |
| `.flyout-slider` | Flyout panel slider |
| `.proj-hero-slider` | Project page hero slider |
| `.big-col-slider` | Tab-linked content slider |
| `.career-type-slider` | Career chip-controlled slider |
| `.map-info-slider` | Office map info slider |
| `.cost-index-controls` | Cost index navigation |

### Scroll & Parallax
- `.img-parallax` elements with `yPercent: 20` scrub
- `animateOnScroll()` jQuery plugin: watches `.anim-block`, adds `.done` class at 85% viewport
- GSAP ScrollTrigger pins for sidebar filter widget and insights sidebar

### Contact Forms
- `Te()` + `Pe()` — Submission with reCAPTCHA execute + AJAX POST
- `je()` / `Ze()` — Error display and form reset
- Two forms: `#main-contact-form` and `#menu-contact-form`

### AJAX Filtering (Projects/Insights)
- `ke()` — Generic AJAX filter handler
- `Ie()` — Search filter submit
- `ze()` — Pagination click handler
- `De()` — `history.pushState()` for shareable filter URLs
- `Se()` / `Ve()` — Clear all filters / clear location filters

### Google Maps Office Locator
- Custom dark-themed map (navy/blue styling, no road labels)
- Geolocation API to center on user's nearest office
- MarkerClusterer for grouped pins
- Swiper synced to map markers

### Smooth Scroll (Lenis)
- 1.2s duration, exponential easing
- `window.trigger('lenisControl', {val: 'stop'/'start'})` pause/resume events
- `.goto[data-href]` for programmatic scroll

### Rolling Text
- Custom `oe` class for infinite marquee text animation
- IntersectionObserver-controlled (pauses when off screen)
- Supports both horizontal and vertical directions

---

## 🔍 Key Observations

### 1. Live Server Dependencies
Pages reference the live CDN in global JS variables:
```js
var _webroot = 'https://ep-turnerconstruction-prod-...azurefd.net/';
var _here = 'https://turnerconstruction.com/';
```
AJAX calls for filtering, maps, and forms point to live Turner infrastructure.

### 2. No Templating
All 23 HTML files have the **entire header/megamenu and footer duplicated** — no server-side includes or JS templating. Changes must be made across all files.

### 3. Lazy Loading Pattern
Blazy handles image loading with a `data-src-mobile` attribute for images below 1024px breakpoint. Critical images use `.force-load-img` class to bypass lazy loading.

### 4. SEO
- Each page has unique `<title>`, `<meta description>`, and `og:image`
- Google Tag Manager (GTM-M593X6SF) on every page
- Semantic heading hierarchy throughout

### 5. Accessibility
- ARIA: `aria-haspopup`, `aria-expanded`, `aria-label` on nav
- `aria-hidden="true"` on decorative/icon images
- Keyboard: Escape key closes megamenu and all popups
