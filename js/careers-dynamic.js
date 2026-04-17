/**
 * careers-dynamic.js
 * Powers Careers.html.
 * Fetches active jobs and renders them into #jobs-list.
 * Opens a modal form for applications (no <form> tags — uses FormData).
 */
;(function () {
  'use strict'

  const API_BASE   = window.EXELLAR_API || 'http://localhost:5000'
  const LIST_ID    = 'jobs-list'
  const MODAL_ID   = 'apply-modal'

  let selectedJob  = null

  // ── MODAL HTML ─────────────────────────────────────────────────────────────
  const MODAL_HTML = `
    <div id="${MODAL_ID}" style="
      display:none; position:fixed; inset:0; background:rgba(0,0,0,0.75);
      z-index:9999; align-items:center; justify-content:center;">
      <div style="
        background:#181818; border:1px solid #2e2e2e; border-radius:8px;
        padding:40px; max-width:560px; width:90%; position:relative;
        max-height:90vh; overflow-y:auto;">
        <button id="modal-close" style="
          position:absolute; top:16px; right:20px; background:none; border:none;
          color:#888; font-size:24px; cursor:pointer;">×</button>
        <h3 class="title fs-30" id="modal-job-title" style="margin-bottom:8px;"></h3>
        <p class="para fs-19" id="modal-job-dept" style="opacity:0.6; margin-bottom:28px;"></p>
        <div id="modal-error" style="display:none; background:rgba(224,82,82,0.12);
          border:1px solid #e05252; color:#e05252; padding:10px 14px;
          border-radius:6px; margin-bottom:16px; font-size:14px;"></div>
        <div id="modal-success" style="display:none; text-align:center; padding:20px 0;">
          <p class="title fs-30" style="color:#52b26b; margin-bottom:10px;">Application Sent!</p>
          <p class="para fs-19">We'll be in touch soon.</p>
        </div>
        <div id="modal-form-body">
          <div style="margin-bottom:16px;">
            <p class="para fs-14" style="margin-bottom:6px; opacity:0.7;">Full Name *</p>
            <input id="apply-name" type="text" placeholder="Your full name"
              style="background:#222; border:1px solid #2e2e2e; color:#e8e8e8;
              padding:10px 14px; border-radius:6px; width:100%; font-size:14px; outline:none;">
          </div>
          <div style="margin-bottom:16px;">
            <p class="para fs-14" style="margin-bottom:6px; opacity:0.7;">Email *</p>
            <input id="apply-email" type="email" placeholder="you@example.com"
              style="background:#222; border:1px solid #2e2e2e; color:#e8e8e8;
              padding:10px 14px; border-radius:6px; width:100%; font-size:14px; outline:none;">
          </div>
          <div style="margin-bottom:16px;">
            <p class="para fs-14" style="margin-bottom:6px; opacity:0.7;">Phone</p>
            <input id="apply-phone" type="tel" placeholder="+91 98000 00000"
              style="background:#222; border:1px solid #2e2e2e; color:#e8e8e8;
              padding:10px 14px; border-radius:6px; width:100%; font-size:14px; outline:none;">
          </div>
          <div style="margin-bottom:16px;">
            <p class="para fs-14" style="margin-bottom:6px; opacity:0.7;">Cover Letter</p>
            <textarea id="apply-cover" rows="4" placeholder="Tell us why you're a great fit…"
              style="background:#222; border:1px solid #2e2e2e; color:#e8e8e8;
              padding:10px 14px; border-radius:6px; width:100%; font-size:14px;
              outline:none; resize:vertical; font-family:inherit;"></textarea>
          </div>
          <div style="margin-bottom:24px;">
            <p class="para fs-14" style="margin-bottom:6px; opacity:0.7;">Resume (PDF, DOC, DOCX)</p>
            <input id="apply-resume" type="file" accept=".pdf,.doc,.docx"
              style="color:#888; font-size:13px;">
          </div>
          <button id="apply-submit"
            style="background:#c8a96e; border:none; color:#1a1100;
            padding:12px 32px; border-radius:6px; font-size:14px;
            font-weight:600; cursor:pointer; width:100%;">
            Submit Application
          </button>
        </div>
      </div>
    </div>
  `

  // ── JOB CARD ───────────────────────────────────────────────────────────────
  function jobCardHTML(job) {
    return `
      <div class="anim-elem top" style="
        border:1px solid rgba(255,255,255,0.08); border-radius:8px;
        padding:28px 32px; margin-bottom:16px;
        display:flex; align-items:center; justify-content:space-between;
        flex-wrap:wrap; gap:16px;">
        <div>
          <h3 class="title fs-30" style="margin-bottom:6px;">${job.title}</h3>
          <p class="para fs-19" style="opacity:0.6;">
            ${job.department || ''}
            ${job.department && job.location ? ' &nbsp;·&nbsp; ' : ''}
            ${job.location || ''}
            ${job.type ? ' &nbsp;·&nbsp; ' + capitalise(job.type) : ''}
          </p>
        </div>
        <button class="btn-link apply-btn" data-job-id="${job.id}"
          style="cursor:pointer; background:none; border:none; color:inherit; font-size:inherit;">
          Apply Now
          <img aria-hidden="true" src="images/btn-arrow.svg" alt="arrow" width="35" height="14">
        </button>
      </div>
    `
  }

  function capitalise(str) {
    return str.charAt(0).toUpperCase() + str.slice(1)
  }

  // ── MODAL LOGIC ────────────────────────────────────────────────────────────
  function openModal(job) {
    selectedJob = job
    document.getElementById('modal-job-title').textContent = job.title
    document.getElementById('modal-job-dept').textContent  =
      [job.department, job.location, job.type ? capitalise(job.type) : '']
        .filter(Boolean).join(' · ')

    document.getElementById('modal-error').style.display   = 'none'
    document.getElementById('modal-success').style.display = 'none'
    document.getElementById('modal-form-body').style.display = ''

    ;['apply-name','apply-email','apply-phone','apply-cover'].forEach(id => {
      document.getElementById(id).value = ''
    })

    const modal = document.getElementById(MODAL_ID)
    modal.style.display = 'flex'
    if (window.lenis) window.lenis.stop()
  }

  function closeModal() {
    document.getElementById(MODAL_ID).style.display = 'none'
    if (window.lenis) window.lenis.start()
    selectedJob = null
  }

  function showModalError(msg) {
    const el = document.getElementById('modal-error')
    el.textContent = msg
    el.style.display = 'block'
  }

  async function submitApplication() {
    const name  = document.getElementById('apply-name').value.trim()
    const email = document.getElementById('apply-email').value.trim()

    if (!name || !email) { showModalError('Name and email are required.'); return }

    const btn = document.getElementById('apply-submit')
    btn.disabled   = true
    btn.textContent = 'Submitting…'

    const fd = new FormData()
    fd.append('name',  name)
    fd.append('email', email)
    fd.append('phone', document.getElementById('apply-phone').value.trim())
    fd.append('cover_letter', document.getElementById('apply-cover').value.trim())
    if (selectedJob) fd.append('job_id', selectedJob.id)

    const resumeInput = document.getElementById('apply-resume')
    if (resumeInput.files[0]) fd.append('resume', resumeInput.files[0])

    try {
      const res = await fetch(`${API_BASE}/api/applications`, { method: 'POST', body: fd })
      const data = await res.json()
      if (!res.ok) { showModalError(data.error || 'Submission failed.'); return }
      document.getElementById('modal-form-body').style.display = 'none'
      document.getElementById('modal-success').style.display   = ''
      setTimeout(closeModal, 3000)
    } catch {
      showModalError('Network error. Please try again.')
    } finally {
      btn.disabled    = false
      btn.textContent = 'Submit Application'
    }
  }

  // ── INIT ───────────────────────────────────────────────────────────────────
  function init() {
    // Inject modal
    document.body.insertAdjacentHTML('beforeend', MODAL_HTML)

    document.getElementById('modal-close').addEventListener('click', closeModal)
    document.getElementById(MODAL_ID).addEventListener('click', function (e) {
      if (e.target === this) closeModal()
    })
    document.getElementById('apply-submit').addEventListener('click', submitApplication)

    // Fetch jobs
    const list = document.getElementById(LIST_ID)
    if (!list) return

    fetch(`${API_BASE}/api/jobs`)
      .then(r => r.ok ? r.json() : [])
      .then(jobs => {
        if (!jobs.length) {
          list.innerHTML = '<p class="para fs-19" style="opacity:0.5">No open positions at the moment. Check back soon.</p>'
          return
        }

        list.innerHTML = jobs.map(jobCardHTML).join('')

        list.querySelectorAll('.apply-btn').forEach(btn => {
          btn.addEventListener('click', function () {
            const job = jobs.find(j => j.id === this.dataset.jobId)
            if (job) openModal(job)
          })
        })

        if (window.bLazy && typeof window.bLazy.revalidate === 'function') {
          window.bLazy.revalidate()
        }
        if (window.ScrollTrigger) window.ScrollTrigger.refresh()
        document.dispatchEvent(new CustomEvent('dynamicContentLoaded'))
      })
      .catch(function () {
        if (list) list.innerHTML = '<p class="para fs-19" style="opacity:0.5">Unable to load positions.</p>'
      })
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init)
  } else {
    init()
  }
})()
