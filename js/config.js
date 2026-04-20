/**
 * config.js — Exellar API URL + animation reveal fix
 */
;(function () {
  'use strict'

  /* ── 1. API base URL ─────────────────────────────────────────────────── */
  var h = window.location.hostname
  window.EXELLAR_API = (h === 'localhost' || h === '127.0.0.1')
    ? 'http://localhost:5000'
    : 'https://exellar-api.onrender.com'

  /* ── 2. ANIMATION REVEAL FIX ─────────────────────────────────────────────
     animateOnScroll runs before browser paints (window.height = 0), so the
     viewport check fires on 0 elements. Fix: re-run reveal after paint using
     rAF, plus add .done class directly and set inline styles as backup.
  ─────────────────────────────────────────────────────────────────────── */
  function revealAll() {
    var elems = document.querySelectorAll('.anim-elem')
    for (var i = 0; i < elems.length; i++) {
      elems[i].classList.add('done')
      elems[i].style.opacity    = '1'
      elems[i].style.transform  = 'none'
      elems[i].style.visibility = 'visible'
    }
  }

  /* Run immediately for any already-parsed elements */
  revealAll()

  /* Run after first paint — window.height is valid here */
  requestAnimationFrame(function () {
    requestAnimationFrame(function () {
      revealAll()
      /* Re-trigger animateOnScroll if jQuery is available */
      if (window.jQuery) {
        var $ = window.jQuery
        $('body .anim-block').each(function () {
          $(this).find('.anim-elem').addClass('done')
        })
      }
    })
  })

  /* Final safety net on full load */
  window.addEventListener('load', function () {
    revealAll()
    /* Also trigger a fake scroll to kick animateOnScroll's scroll handler */
    window.dispatchEvent(new Event('scroll'))
  })

})()
