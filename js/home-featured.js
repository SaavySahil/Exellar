/**
 * home-featured.js
 * Loads the 3 most-recent projects from the API and updates the
 * "Our Projects" featured grid on the homepage.
 * Also updates the mega-menu "Featured Project" slider.
 */
;(function () {
  'use strict'

  var API_BASE = window.EXELLAR_API || 'http://localhost:5000'

  function imgSrc(p) {
    return p.thumbnail
      ? API_BASE + '/api/uploads/images/' + p.thumbnail
      : 'images/project-placeholder.jpg'
  }

  function card(p) {
    var cat    = p.category || 'Construction'
    var status = p.status === 'completed' ? 'Completed' : 'Ongoing'
    var loc    = p.location ? p.location + ' \u00b7\u00a0' : ''
    var slug   = p.slug || p.id
    return '<div class="inline_block col-d-33 col-t-50 col-m-100 anim-elem top">'
      + '<span class="para fs-20 black90">' + cat + '</span>'
      + '<a href="Project Page.html?slug=' + slug + '" class="proj-list-img to-be-scaled radius">'
      + '<img class="w-100 radius" src="' + imgSrc(p) + '" alt="' + p.title + '">'
      + '</a>'
      + '<a href="Project Page.html?slug=' + slug + '" class="proj-list-txt">'
      + '<h3 class="proj-list-city">' + loc + status + '</h3>'
      + '<h2 class="title fs-30">' + p.title + '</h2>'
      + '</a>'
      + '</div>'
  }

  function init() {
    fetch(API_BASE + '/api/projects')
      .then(function (r) { return r.ok ? r.json() : [] })
      .then(function (data) {
        if (!Array.isArray(data) || !data.length) return

        // Update featured grid
        var grid = document.getElementById('home-featured-grid')
        if (grid) grid.innerHTML = data.slice(0, 3).map(card).join('')

        // Update megamenu slider
        var sw = document.querySelector('.megamenu-slider .swiper-wrapper')
        if (sw) {
          sw.innerHTML = data.slice(0, 3).map(function (p) {
            return '<div class="swiper-slide">'
              + '<a href="Project Page.html?slug=' + (p.slug || p.id) + '" class="to-be-scaled radius">'
              + '<img class="radius w-100" src="' + imgSrc(p) + '" alt="' + p.title + '">'
              + '</a>'
              + '<h3 class="title fs-40">' + p.title + '</h3>'
              + '</div>'
          }).join('')
        }

        // Trigger animation reveal on freshly injected cards
        if (document.dispatchEvent)
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
