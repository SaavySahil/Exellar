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
    const slug     = project.slug || project.id

    return `
      <div class="inline_block col-d-33 col-t-50 col-m-100 v-top anim-elem top"
           style="padding-right:20px; box-sizing:border-box; margin-bottom:40px;"
           data-status="${project.status}">
        <a href="Project Page.html?slug=${slug}" class="to-be-scaled radius">
          <img class="radius w-100 b-lazy" data-src="${imgSrc}" src="" alt="${project.title}">
        </a>
        <h3 class="title fs-40">${project.title}</h3>
        <p class="para fs-19">${category}&nbsp;·&nbsp;${status}
          ${project.location ? `&nbsp;·&nbsp;${project.location}` : ''}
        </p>
        <a href="Project Page.html?slug=${slug}" class="btn-link">
          View Project
          <img aria-hidden="true" src="images/btn-arrow.svg" alt="arrow" width="35" height="14">
        </a>
      </div>
    `
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
