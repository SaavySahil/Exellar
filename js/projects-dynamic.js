/**
 * projects-dynamic.js
 * Powers the Projects.html listing page.
 * Fetches all projects and renders them into #projects-grid.
 * Supports filter buttons: [data-filter="all|ongoing|completed"]
 */
;(function () {
  'use strict'

  const API_BASE   = window.EXELLAR_API || 'http://localhost:5000'
  const GRID_ID    = 'projects-grid'
  const COUNT_ID   = 'projects-count'

  let allProjects  = []
  let activeFilter = 'all'

  function cardHTML(project) {
    const imgSrc   = project.thumbnail
      ? `${API_BASE}/api/uploads/images/${project.thumbnail}`
      : 'images/project-placeholder.jpg'
    const status   = project.status === 'completed' ? 'Completed' : 'Ongoing'
    const category = project.category || 'Construction'
    const slug     = encodeURIComponent(project.slug || project.id)
    const location = project.location || ''
    const cityLine = location ? `${location}&nbsp;&nbsp;·&nbsp;&nbsp;${status}` : status

    return `<div class="inline_block col-d-25 col-t-50 col-m-100 anim-elem top" data-status="${project.status}">
      <span class="para fs-20 black90">${category}</span>
      <a href="Project Page.html?slug=${slug}" class="proj-list-img to-be-scaled radius">
        <img class="w-100 radius b-lazy" data-src="${imgSrc}" src="images/project-placeholder.jpg" alt="${project.title}">
      </a>
      <a href="Project Page.html?slug=${slug}" class="proj-list-txt">
        <h3 class="proj-list-city">${cityLine}</h3>
        <h2 class="title fs-30">${project.title}</h2>
      </a>
    </div>`
  }

  function render(filter) {
    const grid = document.getElementById(GRID_ID)
    if (!grid) return

    activeFilter = filter
    const visible = filter === 'all'
      ? allProjects
      : allProjects.filter(p => p.status === filter)

    grid.innerHTML = visible.map(cardHTML).join('')

    const countEl = document.getElementById(COUNT_ID)
    if (countEl) countEl.textContent = visible.length

    // Update active filter button state
    document.querySelectorAll('[data-filter]').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.filter === filter)
    })

    if (window.bLazy && typeof window.bLazy.revalidate === 'function') {
      window.bLazy.revalidate()
    }
    if (window.ScrollTrigger) window.ScrollTrigger.refresh()
    document.dispatchEvent(new CustomEvent('dynamicContentLoaded'))
  }

  function bindFilters() {
    document.querySelectorAll('[data-filter]').forEach(btn => {
      btn.addEventListener('click', function () {
        render(this.dataset.filter)
      })
    })
  }

  function init() {
    fetch(`${API_BASE}/api/projects`)
      .then(r => r.ok ? r.json() : [])
      .then(data => {
        allProjects = data
        bindFilters()
        render('all')
      })
      .catch(function () {
        const grid = document.getElementById(GRID_ID)
        if (grid) grid.innerHTML = '<p class="para fs-19" style="opacity:0.5">Unable to load projects.</p>'
      })
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init)
  } else {
    init()
  }
})()
