/**
 * config.js — Exellar API environment detection
 * No build step needed: auto-detects local vs. production based on hostname.
 * Include this BEFORE any other Exellar JS files that call the API.
 */
;(function () {
  'use strict'

  var hostname = window.location.hostname

  if (hostname === 'localhost' || hostname === '127.0.0.1') {
    // Local development
    window.EXELLAR_API = 'http://localhost:5000'
  } else {
    // Production (Render.com free tier)
    window.EXELLAR_API = 'https://exellar-api.onrender.com'
  }
})()
