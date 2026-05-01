/**
 * articles-dynamic.js
 * Populates the insights.html article grid from /api/articles.
 * Replaces hardcoded cards with live published articles.
 */
;(function () {
  'use strict'

  var API_BASE = window.EXELLAR_API || 'http://localhost:5000'

  function imgSrc(a) {
    return a.thumbnail
      ? API_BASE + '/api/uploads/images/' + a.thumbnail
      : 'images/project-placeholder.jpg'
  }

  function fmtDate(iso) {
    if (!iso) return ''
    return new Date(iso).toLocaleDateString('en-IN', { day: 'numeric', month: 'long', year: 'numeric' })
  }

  function cardHTML(a) {
    var slug = encodeURIComponent(a.slug || a.id)
    var href = 'Article Template.html?slug=' + slug
    return '<div class="inline_block col-d-25 col-t-50 col-m-100 anim-elem top">'
      + '<h2 class="section-label">' + (a.category || '') + '</h2>'
      + '<a href="' + href + '" class="proj-list-img radius to-be-scaled">'
      + '<img class="w-100 radius" src="' + imgSrc(a) + '" alt="' + a.title + '">'
      + '</a>'
      + '<a href="' + href + '" class="proj-list-txt">'
      + '<h2 class="title fs-30">' + a.title + '</h2>'
      + (a.published_at
          ? '<p class="para black90 fs-16 article-date-txt upper"><strong>' + fmtDate(a.published_at) + '</strong></p>'
          : '')
      + '</a>'
      + '</div>'
  }

  function init() {
    var grid = document.getElementById('articles-grid')
    if (!grid) return

    fetch(API_BASE + '/api/articles')
      .then(function (r) { return r.ok ? r.json() : [] })
      .then(function (articles) {
        if (!Array.isArray(articles) || !articles.length) return
        grid.innerHTML = articles.map(cardHTML).join('')
        if (window.bLazy && typeof window.bLazy.revalidate === 'function') window.bLazy.revalidate()
        if (window.ScrollTrigger) window.ScrollTrigger.refresh()
        document.dispatchEvent(new CustomEvent('dynamicContentLoaded'))
      })
      .catch(function () { /* keep hardcoded fallback */ })
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init)
  } else {
    init()
  }
})()
