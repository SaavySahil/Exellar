/**
 * project-detail.js
 * Powers "Project Page.html" — reads ?slug= from the URL,
 * fetches the project from the API, and populates the page.
 */
;(function () {
  'use strict'

  const API_BASE = window.EXELLAR_API || 'http://localhost:5000'

  function getSlug() {
    return new URLSearchParams(window.location.search).get('slug')
  }

  function setTextAll(selector, value) {
    document.querySelectorAll(selector).forEach(el => {
      el.textContent = value || ''
    })
  }

  function setAttr(selector, attr, value) {
    const el = document.querySelector(selector)
    if (el && value) el.setAttribute(attr, value)
  }

  function populate(project) {
    document.title = `${project.title} — Exellar Construction LLP`

    setTextAll('[data-field="title"]',              project.title)
    setTextAll('[data-field="category"]',           project.category || '')
    setTextAll('[data-field="status"]',             project.status === 'completed' ? 'Completed' : 'Ongoing')
    setTextAll('[data-field="location"]',           project.location || '')
    setTextAll('[data-field="scope"]',              project.scope || '')
    setTextAll('[data-field="size"]',               project.size || '')
    setTextAll('[data-field="client_name"]',        project.client_name || '')
    setTextAll('[data-field="services"]',           project.services || '')
    setTextAll('[data-field="story_headline"]',     project.story_headline || '')
    setTextAll('[data-field="story_body"]',         project.story_body || '')
    setTextAll('[data-field="client_testimonial"]', project.client_testimonial || '')

    // Thumbnail / hero image
    if (project.thumbnail) {
      const src = `${API_BASE}/api/uploads/images/${project.thumbnail}`
      document.querySelectorAll('[data-field="thumbnail"]').forEach(el => {
        if (el.tagName === 'IMG') {
          el.src = src
          el.removeAttribute('data-src')
          el.classList.remove('b-lazy')
        } else {
          el.style.backgroundImage = `url('${src}')`
        }
      })
    }

    // Gallery
    const galleryContainer = document.querySelector('[data-field="gallery"]')
    if (galleryContainer && project.gallery && project.gallery.length) {
      galleryContainer.innerHTML = project.gallery.map(f => `
        <div class="inline_block col-d-33 col-t-50 col-m-100 v-top" style="padding-right:16px; box-sizing:border-box; margin-bottom:16px;">
          <img class="radius w-100" src="${API_BASE}/api/uploads/images/${f}" alt="${project.title}" loading="lazy">
        </div>
      `).join('')
    }

    if (window.ScrollTrigger) window.ScrollTrigger.refresh()
    document.dispatchEvent(new CustomEvent('dynamicContentLoaded'))
  }

  function showError(msg) {
    const el = document.querySelector('[data-field="title"]')
    if (el) el.textContent = msg
  }

  function init() {
    const slug = getSlug()
    if (!slug) { showError('No project specified.'); return }

    fetch(`${API_BASE}/api/projects/${slug}`)
      .then(r => {
        if (!r.ok) throw new Error('Not found')
        return r.json()
      })
      .then(populate)
      .catch(() => showError('Project not found.'))
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init)
  } else {
    init()
  }
})()
