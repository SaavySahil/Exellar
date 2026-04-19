/**
 * config.js — Exellar API environment detection + animation fallback
 * Include this BEFORE closing </body> on every page.
 */
;(function () {
  'use strict'

  /* ── 1. API base URL ── */
  var hostname = window.location.hostname
  if (hostname === 'localhost' || hostname === '127.0.0.1') {
    window.EXELLAR_API = 'http://localhost:5000'
  } else {
    window.EXELLAR_API = 'https://exellar-api.onrender.com'
  }

  /* ── 2. Animation reveal fallback ──────────────────────────────────────
     The site uses .anim-elem { opacity:0 } revealed via JS (.done class).
     If the main app.js scroll trigger misses elements (e.g. on inner pages),
     this fallback guarantees every in-viewport element becomes visible.
  ───────────────────────────────────────────────────────────────────────── */
  function revealInView() {
    var blocks = document.querySelectorAll('.anim-block')
    var vh = window.innerHeight
    var scrollY = window.pageYOffset || document.documentElement.scrollTop

    for (var b = 0; b < blocks.length; b++) {
      var rect = blocks[b].getBoundingClientRect()
      // Reveal if block top is within 95 % of viewport
      if (rect.top < vh * 0.95) {
        var elems = blocks[b].querySelectorAll('.anim-elem')
        for (var e = 0; e < elems.length; e++) {
          if (!elems[e].classList.contains('done')) {
            ;(function (el, delay) {
              setTimeout(function () {
                el.classList.add('done')
              }, delay)
            })(elems[e], e * 80)
          }
        }
      }
    }
  }

  /* Also reveal orphan .anim-elem elements not inside any .anim-block */
  function revealOrphans() {
    var all = document.querySelectorAll('.anim-elem')
    for (var i = 0; i < all.length; i++) {
      if (!all[i].classList.contains('done')) {
        var rect = all[i].getBoundingClientRect()
        if (rect.top < window.innerHeight) {
          all[i].classList.add('done')
        }
      }
    }
  }

  function onScroll() {
    revealInView()
    revealOrphans()
  }

  /* Run after everything has loaded so layout is final */
  window.addEventListener('load', function () {
    // Give app.js's own animateOnScroll a 400 ms head-start
    setTimeout(function () {
      revealInView()
      revealOrphans()
    }, 400)

    // Keep triggering on scroll (native + Lenis both fire scroll events)
    window.addEventListener('scroll', onScroll, { passive: true })
  })

  /* Hard-deadline: after 1.8 s force ALL remaining hidden elems visible */
  window.addEventListener('load', function () {
    setTimeout(function () {
      var stale = document.querySelectorAll('.anim-elem:not(.done)')
      for (var i = 0; i < stale.length; i++) {
        stale[i].classList.add('done')
      }
    }, 1800)
  })
})()
