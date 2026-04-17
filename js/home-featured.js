/**
 * home-featured.js
 * Fetches featured projects from the API and injects them into the
 * #featured-projects-grid container on Home.html.
 * Triggers Blazy re-init and ScrollTrigger.refresh() after injection.
 */
;(function () {
  'use strict'

  const API_BASE = window.EXELLAR_API || 'http://localhost:5000'
  const GRID_ID  = 'featured-projects-grid'
  const MAX      = 3

  function cardHTML(project, index) {
    const isLast    = index === MAX - 1
    const padding   = isLast ? '' : 'padding-right:20px; box-sizing:border-box;'
    const imgSrc    = project.thumbnail
      ? `${API_BASE}/api/uploads/images/${project.thumbnail}`
      : 'images/project-placeholder.jpg'
    const status    = project.status === 'completed' ? 'Completed' : 'Ongoing'
    const category  = project.category || 'Construction'
    const slug      = project.slug || project.id

    return `
      <div class="inline_block col-d-33 col-t-50 col-m-100 v-top anim-elem top" style="${padding}">
        <a href="Projects.html?slug=${slug}" class="to-be-scaled radius">
          <img class="radius w-100 b-lazy" data-src="${imgSrc}" src="" alt="${project.title}">
        </a>
        <h3 class="title fs-40">${project.title}</h3>
        <p class="para fs-19">${category}&nbsp;·&nbsp;${status}</p>
        <a href="Projects.html?slug=${slug}" class="btn-link">
          View Project
          <img aria-hidden="true" src="images/btn-arrow.svg" alt="arrow" width="35" height="14">
        </a>
      </div>
    `
  }

  function inject(projects) {
    const grid = document.getElementById(GRID_ID)
    if (!grid) return

    const featured = projects.filter(p => p.is_featured).slice(0, MAX)
    const toShow   = featured.length ? featured : projects.slice(0, MAX)

    if (!toShow.length) {
      grid.closest('section').style.display = 'none'
      return
    }

    grid.innerHTML = toShow.map((p, i) => cardHTML(p, i)).join('')

    // Re-init Blazy for lazy images
    if (window.bLazy && typeof window.bLazy.revalidate === 'function') {
      window.bLazy.revalidate()
    }

    // Refresh GSAP ScrollTrigger so new elements animate correctly
    if (window.ScrollTrigger) {
      window.ScrollTrigger.refresh()
    }

    // Fire custom event so other scripts can react
    document.dispatchEvent(new CustomEvent('dynamicContentLoaded'))
  }

  function init() {
    fetch(`${API_BASE}/api/projects?is_featured=true`)
      .then(function (res) { return res.ok ? res.json() : [] })
      .then(function (data) {
        if (!data.length) {
          // Fallback: fetch all and take first 3
          return fetch(`${API_BASE}/api/projects`).then(r => r.ok ? r.json() : [])
        }
        return data
      })
      .then(inject)
      .catch(function () {
        // On error, keep the static placeholder cards already in HTML
      })
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init)
  } else {
    init()
  }
})()
