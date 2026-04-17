# PATTERNS.md — Exellar Construction HTML Pattern Library
## Copy these exactly. Never invent new HTML structures.

> **Rule:** Every time you need to add something to an HTML page, find the closest pattern here and copy it. Modify only the content (text, href, src). Never modify the CSS classes.

---

## 1. SECTION — Image Left, Text Right

```html
<section class="home-office prel">
    <div class="width-960"></div>
    <div class="home-wrapper w2100">
        <div class="office-cols f0 anim-block">
            <div class="inline_block col-d-50 col-t-50 col-m-100 vm anim-elem left">
                <div class="img-credit has-credit prel inline_block ov-hidden radius">
                    <span class="img-wrapper img-parallax aspect-ratio-880-688">
                        <img class="b-lazy" width="880" height="688" data-src="images/FILENAME.jpg" src="" alt="DESCRIPTION">
                    </span>
                </div>
            </div>
            <div class="office-txt-col inline_block col-d-50 col-t-50 col-m-100 vm">
                <h2 class="section-label anim-elem left">LABEL</h2>
                <h3 class="title fs-70 anim-elem left">HEADING</h3>
                <p class="para fs-32 anim-elem left">BODY TEXT</p>
                <a href="PAGE.html" class="btn-link anim-elem left">CTA TEXT <img aria-hidden="true" src="images/btn-arrow.svg" alt="arrow"></a>
            </div>
        </div>
    </div>
    <div class="grid-lines gray">
        <div class="line-25"></div>
        <div class="line-50"></div>
        <div class="line-25"></div>
    </div>
</section>
```

---

## 2. SECTION — Text Left, Image Right

```html
<section class="home-office prel">
    <div class="width-960"></div>
    <div class="home-wrapper w2100">
        <div class="office-cols f0 anim-block">
            <div class="office-txt-col inline_block col-d-50 col-t-50 col-m-100 vm">
                <h2 class="section-label anim-elem left">LABEL</h2>
                <h3 class="title fs-70 anim-elem left">HEADING</h3>
                <p class="para fs-32 anim-elem left">BODY TEXT</p>
                <a href="PAGE.html" class="btn-link anim-elem left">CTA TEXT <img aria-hidden="true" src="images/btn-arrow.svg" alt="arrow"></a>
            </div>
            <div class="inline_block col-d-50 col-t-50 col-m-100 vm anim-elem left">
                <div class="img-credit has-credit prel inline_block ov-hidden radius">
                    <span class="img-wrapper img-parallax aspect-ratio-880-688">
                        <img class="b-lazy" width="880" height="688" data-src="images/FILENAME.jpg" src="" alt="DESCRIPTION">
                    </span>
                </div>
            </div>
        </div>
    </div>
    <div class="grid-lines gray">
        <div class="line-25"></div>
        <div class="line-50"></div>
        <div class="line-25"></div>
    </div>
</section>
```

---

## 3. SECTION — Full Width Heading + 3 Cards

```html
<section class="home-office prel">
    <div class="width-960"></div>
    <div class="home-wrapper w2100">
        <h2 class="section-label anim-elem top">LABEL</h2>
        <h3 class="title fs-70 anim-elem top">HEADING</h3>
        <p class="para fs-32 anim-elem top">SUBHEADING TEXT</p>
        <div class="office-cols f0 anim-block" style="margin-top:40px;">
            <!-- CARD × 3 — use Pattern #6 below -->
        </div>
        <div class="offices-cta anim-block">
            <a href="PAGE.html" class="btn-link anim-elem">VIEW ALL <img aria-hidden="true" src="images/btn-arrow.svg" alt="arrow"></a>
        </div>
    </div>
    <div class="grid-lines gray">
        <div class="line-25"></div>
        <div class="line-50"></div>
        <div class="line-25"></div>
    </div>
</section>
```

---

## 4. SECTION — Stats Row (inside office-txt-col)

```html
<div class="f0 anim-block">
    <div class="inline_block col-d-33 col-t-33 col-m-33 v-top anim-elem top">
        <p class="title fs-70" style="line-height:1;">NUMBER</p>
        <p class="section-label">LABEL</p>
    </div>
    <div class="inline_block col-d-33 col-t-33 col-m-33 v-top anim-elem top">
        <p class="title fs-70" style="line-height:1;">NUMBER</p>
        <p class="section-label">LABEL</p>
    </div>
    <div class="inline_block col-d-33 col-t-33 col-m-33 v-top anim-elem top">
        <p class="title fs-70" style="line-height:1;">NUMBER</p>
        <p class="section-label">LABEL</p>
    </div>
</div>
```

---

## 5. SECTION — Client Logos Text Strip

```html
<section class="home-office prel">
    <div class="home-wrapper w2100">
        <div class="anim-block">
            <h2 class="section-label anim-elem top" style="text-align:center;">LABEL</h2>
            <div class="f0 anim-block">
                <div class="inline_block col-d-16 col-t-33 col-m-50 vm anim-elem top" style="text-align:center; padding:32px 0;">
                    <p class="title fs-30" style="opacity:0.45;">CLIENT NAME</p>
                </div>
                <!-- repeat for each client -->
            </div>
        </div>
    </div>
    <div class="grid-lines gray">
        <div class="line-25"></div>
        <div class="line-50"></div>
        <div class="line-25"></div>
    </div>
</section>
```

When logo images are available, replace `<p class="title fs-30">` with:
```html
<img class="b-lazy" data-src="images/client-NAME.png" src="" alt="CLIENT NAME" style="max-height:48px; max-width:130px; filter:grayscale(1); opacity:0.55; display:inline-block;">
```

---

## 6. CARD — Project Card (3-column)

```html
<div class="inline_block col-d-33 col-t-50 col-m-100 v-top anim-elem top" style="padding-right:20px; box-sizing:border-box;">
    <a href="PROJECT-DETAIL-URL" class="to-be-scaled radius">
        <img class="radius w-100 b-lazy" data-src="images/FILENAME.jpg" src="" alt="PROJECT NAME">
    </a>
    <h3 class="title fs-40">PROJECT NAME</h3>
    <p class="para fs-19">CATEGORY &nbsp;·&nbsp; STATUS</p>
    <a href="PROJECT-DETAIL-URL" class="btn-link">View Project <img aria-hidden="true" src="images/btn-arrow.svg" alt="arrow" width="35" height="14"></a>
</div>
```

**Last card in a row — no padding-right:**
```html
<div class="inline_block col-d-33 col-t-50 col-m-100 v-top anim-elem top">
```

---

## 7. CARD — Project Card (4-column, for listing pages)

```html
<div class="inline_block col-d-25 col-t-50 col-m-100 v-top anim-elem top">
    <a href="PROJECT-DETAIL-URL" class="to-be-scaled radius">
        <img class="radius w-100 b-lazy" data-src="images/FILENAME.jpg" src="" alt="PROJECT NAME">
    </a>
    <h3 class="title fs-40">PROJECT NAME</h3>
    <p class="para fs-19">CATEGORY &nbsp;·&nbsp; STATUS</p>
    <a href="PROJECT-DETAIL-URL" class="btn-link">View Project <img aria-hidden="true" src="images/btn-arrow.svg" alt="arrow" width="35" height="14"></a>
</div>
```

---

## 8. CARD — Insight / News Card (Large)

```html
<div class="innovation-big-col inline_block col-d-50 col-t-100 col-m-100 v-top anim-elem left">
    <a href="insights.html" class="to-be-scaled radius">
        <img class="radius w-100 b-lazy" data-src="images/FILENAME.jpg" alt="TITLE">
    </a>
    <h3 class="title fs-40">TITLE</h3>
    <a href="insights.html" class="btn-link">Read More <img aria-hidden="true" src="images/btn-arrow.svg" alt="arrow" width="35" height="14"></a>
</div>
```

---

## 9. CARD — Insight / News Card (Small)

```html
<div class="accents-slider-item inline_block col-d-50 col-t-50 col-m-100 vm">
    <a href="insights.html" class="to-be-scaled radius">
        <img class="radius w-100" src="images/FILENAME.jpg" alt="TITLE">
    </a>
    <h3 class="title fs-30">TITLE</h3>
    <a href="insights.html" class="btn-link">Read More <img aria-hidden="true" src="images/btn-arrow.svg" alt="arrow" width="35" height="14"></a>
</div>
```

---

## 10. BUTTON — CTA Link (Arrow)

```html
<a href="PAGE.html" class="btn-link anim-elem">
    CTA TEXT <img aria-hidden="true" src="images/btn-arrow.svg" alt="arrow" width="35" height="14">
</a>
```

White variant (on dark background):
```html
<a href="PAGE.html" class="btn-link white anim-elem">
    CTA TEXT <img aria-hidden="true" src="images/btn-arrow-white.svg" alt="arrow">
</a>
```

---

## 11. SECTION LABEL + HEADING + BODY (standard)

```html
<h2 class="section-label anim-elem left">LABEL</h2>
<h3 class="title fs-70 anim-elem left">HEADING</h3>
<p class="para fs-32 anim-elem left">BODY TEXT</p>
```

Centered variant:
```html
<h2 class="section-label anim-elem top" style="text-align:center;">LABEL</h2>
<h3 class="title fs-70 anim-elem top" style="text-align:center;">HEADING</h3>
```

---

## 12. IMAGE — Lazy Loaded (b-lazy)

```html
<img class="radius w-100 b-lazy" data-src="images/FILENAME.jpg" src="" alt="DESCRIPTION">
```

**Never use `src="images/..."` directly on dynamic images. Always use `data-src` + `b-lazy` class.**

After dynamically inserting b-lazy images via JS:
```js
if (window.bLazy) window.bLazy.revalidate();
else if (window.Blazy) new Blazy({ selector: '#CONTAINER_ID .b-lazy' });
```

---

## 13. IMAGE — Parallax with Aspect Ratio

```html
<div class="img-credit has-credit prel inline_block ov-hidden radius">
    <span class="img-wrapper img-parallax aspect-ratio-880-688">
        <img class="b-lazy" width="880" height="688" data-src="images/FILENAME.jpg" src="" alt="DESCRIPTION">
    </span>
</div>
```

---

## 14. NAV — Header Link (desktop nav)

```html
<div class="header-li">
    <a class="header-link" href="PAGE.html" target="">
        NAV LABEL
    </a>
</div>
```

With dropdown submenu:
```html
<div class="header-li">
    <a class="header-link" href="PAGE.html" target="">NAV LABEL</a>
    <div class="submenu">
        <div class="submenu-holder">
            <div class="submenu-left">
                <div class="submenu-title-holder">
                    <h3 class="submenu-title white">NAV LABEL</h3>
                </div>
                <div class="submenu-left-description">
                    <p class="txt-24">DESCRIPTION</p>
                    <a href="PAGE.html" class="btn-link white">CTA <img aria-hidden="true" src="images/btn-arrow-white.svg" alt="arrow"></a>
                </div>
            </div>
            <div class="submenu-center">
                <div class="inline_block col-d-50 col-t-100 col-m-100">
                    <div class="submenu-title-holder">
                        <h3 class="submenu-title">GROUP TITLE</h3>
                    </div>
                    <ul class="submenu-ul-tag">
                        <li><a href="PAGE.html">Link 1</a></li>
                        <li><a href="PAGE.html">Link 2</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
```

---

## 15. FOOTER — Footer Nav Column

```html
<div class="inline_block col-d-33 col-t-100 col-m-50 vt">
    <ul class="footer-ul">
        <li class="footer-li open-footer-li">
            <a href="PAGE.html" target="" class="footer-a prel">
                <span class="link-underline"></span>SECTION TITLE
            </a>
            <ul class="footer-sub-ul" style="display:none;">
                <li class="footer-sub-li"><a href="PAGE.html" target="">Sub Link</a></li>
            </ul>
        </li>
    </ul>
</div>
```

---

## 16. DYNAMIC JS FILE — Boilerplate

```js
(function () {
    'use strict';

    var API_BASE = 'http://localhost:5000'; // Change to https://api.exellar.com before go-live

    function init() {
        // fetch and render
    }

    function refreshAnimations() {
        if (window.ScrollTrigger) window.ScrollTrigger.refresh();
        document.dispatchEvent(new CustomEvent('dynamicContentLoaded'));
        if (window.bLazy) window.bLazy.revalidate();
        else if (window.Blazy) new Blazy({ selector: '#CONTAINER .b-lazy' });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
```

---

## 17. MODAL — Apply / Action Modal (no new CSS)

```html
<div id="MODAL_ID" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.7); z-index:9999;">
    <div style="background:#fff; max-width:600px; margin:80px auto; padding:40px; position:relative;">
        <button id="MODAL_CLOSE_ID" style="position:absolute; top:20px; right:20px; background:none; border:none; cursor:pointer; font-size:24px;">×</button>
        <h2 class="title fs-40">MODAL TITLE</h2>
        <!-- form fields -->
        <div class="form-field">
            <label class="input-label" for="FIELD_ID">LABEL</label>
            <input class="input-field" type="text" id="FIELD_ID">
        </div>
        <div class="proj-show-more" id="SUBMIT_BTN_ID" style="cursor:pointer; margin-top:20px;">
            <p class="para fs-16 upper">SUBMIT</p>
            <img src="images/btn-arrow.svg" alt="arrow">
        </div>
    </div>
</div>
```

Scroll lock (use Lenis — never overflow:hidden):
```js
document.getElementById('OPEN_BTN').addEventListener('click', function() {
    document.getElementById('MODAL_ID').style.display = 'block';
    if (window.lenis) window.lenis.stop();
});
document.getElementById('MODAL_CLOSE_ID').addEventListener('click', function() {
    document.getElementById('MODAL_ID').style.display = 'none';
    if (window.lenis) window.lenis.start();
});
```

---

## 18. FORM — FormData Submission (no form tag)

```js
var btn = document.getElementById('SUBMIT_BTN');
btn.addEventListener('click', function() {
    var data = new FormData();
    data.append('name', document.getElementById('name').value);
    data.append('email', document.getElementById('email').value);
    // DO NOT set Content-Type manually

    fetch(API_BASE + '/api/ENDPOINT', {
        method: 'POST',
        body: data
    })
    .then(function(r) { return r.json(); })
    .then(function(res) {
        // handle success
    })
    .catch(function(err) {
        // handle error
    });
});
```

---

## 19. ADMIN — Resume Download (window.open with token)

```js
function downloadResume(applicationId) {
    var token = localStorage.getItem('token');
    window.open(API_BASE + '/api/admin/applications/' + applicationId + '/resume?token=' + token);
}
```

---

## 20. PAGE HERO SECTION (inner pages)

```html
<section class="page-header prel anim-block">
    <div class="page-header-img">
        <img class="b-lazy img-parallax w-100" data-src="images/FILENAME.jpg" src="" alt="PAGE TITLE">
    </div>
    <div class="page-header-content">
        <div class="page-header-txt">
            <h1 class="title fs-90 white anim-elem top">PAGE TITLE</h1>
        </div>
    </div>
    <div class="grid-lines">
        <div class="line-25"></div>
        <div class="line-50"></div>
        <div class="line-25"></div>
    </div>
</section>
```
