/**
 * config.js — Exellar API URL + nuclear visibility fix
 * Placed before </body> on every page.
 */
;(function () {
  'use strict'

  /* ── 1. API base URL ─────────────────────────────────────────────────── */
  var h = window.location.hostname
  window.EXELLAR_API = (h === 'localhost' || h === '127.0.0.1')
    ? 'http://localhost:5000'
    : 'https://exellar-api.onrender.com'

  /* ── 2. NUCLEAR VISIBILITY FIX ──────────────────────────────────────────
     The site CSS sets .anim-elem { opacity:0 } and JS is supposed to add
     .done to reveal them via scroll. That JS fails on every page except
     the homepage. Fix: force inline opacity:1 on every .anim-elem element
     right now, bypassing the entire animation system.
     Inline styles beat stylesheet rules (even !important), so this wins.
  ─────────────────────────────────────────────────────────────────────── */
  function nukeHidden() {
    var elems = document.querySelectorAll('.anim-elem')
    for (var i = 0; i < elems.length; i++) {
      elems[i].style.opacity    = '1'
      elems[i].style.transform  = 'none'
      elems[i].style.visibility = 'visible'
    }
  }

  /* Run RIGHT NOW — config.js is at bottom of <body> so DOM is parsed */
  nukeHidden()

  /* Run again after 100 ms in case any elements were added by other scripts */
  setTimeout(nukeHidden, 100)

  /* Run again after full page load (images etc.) */
  window.addEventListener('load', nukeHidden)

  /* Scroll: reveal any elements dynamically injected after load */
  window.addEventListener('scroll', nukeHidden, { passive: true })
})()
