/**
 * config.js — Exellar API environment detection + animation reveal fallback
 * Placed before </body> on every page.
 */
;(function () {
  'use strict'

  /* ── 1. API base URL ─────────────────────────────────────────────────── */
  var h = window.location.hostname
  window.EXELLAR_API = (h === 'localhost' || h === '127.0.0.1')
    ? 'http://localhost:5000'
    : 'https://exellar-api.onrender.com'

  /* ── 2. Animation reveal fallback ────────────────────────────────────────
     .anim-elem starts at opacity:0 — app.js adds .done to reveal them.
     This fallback ensures every element becomes visible even if app.js
     misses them (happens on inner pages due to scroll-trigger timing).
  ─────────────────────────────────────────────────────────────────────── */

  function addDone(el, delay) {
    if (el.classList.contains('done')) return
    if (delay) {
      setTimeout(function () { el.classList.add('done') }, delay)
    } else {
      el.classList.add('done')
    }
  }

  /* Reveal all .anim-block children that are currently on-screen */
  function revealInView() {
    var vh = window.innerHeight
    var blocks = document.querySelectorAll('.anim-block')
    for (var b = 0; b < blocks.length; b++) {
      var top = blocks[b].getBoundingClientRect().top
      if (top < vh * 0.98) {                        // block is on screen
        var kids = blocks[b].querySelectorAll('.anim-elem')
        for (var k = 0; k < kids.length; k++) {
          addDone(kids[k], k * 60)                   // stagger 60 ms
        }
      }
    }
  }

  /* Reveal orphan .anim-elem elements not inside any .anim-block */
  function revealOrphans() {
    var all = document.querySelectorAll('.anim-elem')
    var vh  = window.innerHeight
    for (var i = 0; i < all.length; i++) {
      if (all[i].getBoundingClientRect().top < vh) addDone(all[i], 0)
    }
  }

  function revealAll() {
    var all = document.querySelectorAll('.anim-elem')
    for (var i = 0; i < all.length; i++) addDone(all[i], 0)
  }

  /* ── Fire order ──────────────────────────────────────────────────────── */

  /* Pass 1 – immediately when this script executes (DOM already exists
     because we're at the bottom of <body>) */
  revealInView()
  revealOrphans()

  /* Pass 2 – 120 ms later: layout is stable, images starting to load */
  setTimeout(function () {
    revealInView()
    revealOrphans()
  }, 120)

  /* Pass 3 – 600 ms deadline: catch anything the passes above missed */
  setTimeout(function () {
    revealInView()
    revealOrphans()
  }, 600)

  /* Hard deadline – 1.5 s: force EVERYTHING visible regardless */
  setTimeout(revealAll, 1500)

  /* On every scroll: reveal newly in-view blocks */
  window.addEventListener('scroll', function () {
    revealInView()
    revealOrphans()
  }, { passive: true })

  /* After images load: refresh positions and reveal again */
  window.addEventListener('load', function () {
    revealInView()
    revealOrphans()
    setTimeout(revealAll, 500)      /* final safety net after load */
  })
})()
