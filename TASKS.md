# TASKS.md — Exellar Construction LLP
## Master Task Checklist — One Task at a Time

> **Rule for AI:** Pick the FIRST unchecked task in the current phase. Do it. Stop. Confirm with user. Then move to next.
> **Rule for user:** Never give an AI more than one task at a time. One checkbox = one prompt.

**Legend:** ✅ Done | 🔄 In Progress | ⬜ Not Started | 🔴 Blocked

---

## PHASE 1 — Home Page (Home.html)
*File: `Home.html`*

- ✅ Replace all Turner branding with Exellar branding (title, meta, logo, copy)
- ✅ Fix navigation — remove duplicate "Contact Us" from header-li
- ✅ Add client logos strip section (after hero)
- ✅ Add About Exellar section (image left, stats right)
- ✅ Add Featured Projects section (3-column cards)
- ✅ Add Latest Insights section (existing Turner section preserved)
- ✅ Add Our Services section (existing Turner slider preserved)
- ✅ Add Life at Exellar section (existing Turner section preserved)
- ⬜ Replace hero video — swap `media/302-turner-web-hero-31825.mp4` with Exellar site video when provided
- ⬜ Replace About section image — swap `images/project-placeholder.jpg` with real Exellar photo
- ⬜ Replace client logos text with real PNG logo images (when client provides files — add to `images/client-*.png`)
- ⬜ Wire Featured Projects to API — fetch `GET /api/projects?is_featured=true` in `js/home-featured.js`
- ⬜ Replace all 3 project card placeholders with real project images

---

## PHASE 2 — Other HTML Pages (Branding & Nav)
*Run Python scripts then verify each page*

- ⬜ Run `python update_nav.py` — updates nav links across all pages to point to Exellar pages
- ⬜ Run `python update_megamenu.py` — updates megamenu across all pages
- ⬜ Verify `About-us.html` — check all content is Exellar branded
- ⬜ Verify `Services.html` — check all content is Exellar branded
- ⬜ Verify `Projects.html` — check all content is Exellar branded
- ⬜ Verify `Careers.html` — check careers dynamic JS is linked correctly
- ⬜ Verify `contact-us.html` — form exists, needs API wiring (Phase 5)
- ⬜ Verify `insights.html` — content is Exellar branded
- ⬜ Rename `Fruad-alert.html` → `Fraud-alert.html` and update any links to it
- ⬜ Create `Ongoing-Projects.html` — inject `var PROJECTS_STATUS = "ongoing"` before `projects-dynamic.js`
- ⬜ Create `Completed-Projects.html` — inject `var PROJECTS_STATUS = "completed"` before `projects-dynamic.js`
- ⬜ Create `Project-Detail.html` — template page that `project-detail.js` hydrates from `?slug=`
- ⬜ Update footer across all pages — email, address, social links

---

## PHASE 3 — Backend (Build from scratch)
*Folder: `exellar-backend/`*

### 3A — Project Structure
- ⬜ Create `exellar-backend/app/__init__.py` — app factory, CORS, register blueprints, auto-seed admin
- ⬜ Create `exellar-backend/app/config.py` — Dev/Prod config from `.env`
- ⬜ Create `exellar-backend/app/extensions.py` — db, migrate
- ⬜ Create `exellar-backend/run.py` — entry point
- ⬜ Create `exellar-backend/requirements.txt`
- ⬜ Create `exellar-backend/.env.example`
- ⬜ Create `exellar-backend/.env` (local, gitignored)

### 3B — Models
- ⬜ Create `exellar-backend/app/models/__init__.py`
- ⬜ Create `exellar-backend/app/models/admin.py` — AdminUser (bcrypt password)
- ⬜ Create `exellar-backend/app/models/project.py` — Project (auto-slug, JSON gallery, is_featured)
- ⬜ Create `exellar-backend/app/models/job.py` — Job (enum type, is_active)
- ⬜ Create `exellar-backend/app/models/application.py` — JobApplication (SET NULL FK, job_title snapshot)
- ⬜ Create `exellar-backend/app/models/content.py` — ContentField (key-value CMS)

### 3C — Routes
- ⬜ Create `exellar-backend/app/routes/__init__.py`
- ⬜ Create `exellar-backend/app/routes/auth.py` — `POST /api/auth/login`
- ⬜ Create `exellar-backend/app/routes/projects.py` — Public + Admin CRUD
- ⬜ Create `exellar-backend/app/routes/jobs.py` — Public + Admin CRUD
- ⬜ Create `exellar-backend/app/routes/applications.py` — Submit + Admin list/download
- ⬜ Create `exellar-backend/app/routes/content.py` — Public read + Admin upsert

### 3D — Utils
- ⬜ Create `exellar-backend/app/utils/__init__.py`
- ⬜ Create `exellar-backend/app/utils/auth_middleware.py` — JWT decorator + `decode_token()`
- ⬜ Create `exellar-backend/app/utils/file_handler.py` — `save_resume()`, `get_resume_path()`

### 3E — DB Setup
- ⬜ Run `flask db init` then `flask db migrate` then `flask db upgrade` locally
- ⬜ Test all API endpoints with Postman/curl locally
- ⬜ Seed initial admin user (admin@exellar.co.in / Admin@123 — CHANGE after first login)
- ⬜ Seed ContentField keys: `home_hero_tagline`, `about_summary`, `projects_hero_tagline`, `careers_hero_tagline`

---

## PHASE 4 — Admin Panel (Build from scratch)
*Folder: `exellar-admin/src/`*

### 4A — Setup
- ⬜ Create `exellar-admin/package.json` — React 18, Vite, React Router v6, TanStack Query v5, Axios
- ⬜ Create `exellar-admin/vite.config.js`
- ⬜ Create `exellar-admin/index.html`
- ⬜ Create `exellar-admin/src/main.jsx`
- ⬜ Create `exellar-admin/src/App.jsx` — routes setup

### 4B — API & Auth
- ⬜ Create `exellar-admin/src/api/client.js` — Axios instance + JWT interceptor + auto 401 redirect
- ⬜ Create `exellar-admin/src/context/AuthContext.jsx` — token in localStorage, login/logout

### 4C — Layout Components
- ⬜ Create `exellar-admin/src/components/Layout.jsx` — fixed sidebar 240px + topbar
- ⬜ Create `exellar-admin/src/components/Sidebar.jsx` — NavLink active states
- ⬜ Create `exellar-admin/src/components/StatusBadge.jsx` — pill badges
- ⬜ Create `exellar-admin/src/components/ConfirmModal.jsx` — delete confirmation
- ⬜ Create `exellar-admin/src/components/Toast.jsx` — auto-dismiss 3s notification

### 4D — Pages
- ⬜ Create `exellar-admin/src/pages/Login.jsx`
- ⬜ Create `exellar-admin/src/pages/Dashboard.jsx` — stat cards + recent applications
- ⬜ Create `exellar-admin/src/pages/Projects.jsx` — table + filter tabs + delete
- ⬜ Create `exellar-admin/src/pages/ProjectForm.jsx` — create/edit with slug preview
- ⬜ Create `exellar-admin/src/pages/Jobs.jsx` — table + toggle active
- ⬜ Create `exellar-admin/src/pages/JobForm.jsx`
- ⬜ Create `exellar-admin/src/pages/Applications.jsx` — table + resume download
- ⬜ Create `exellar-admin/src/pages/Content.jsx` — 4 CMS fields, save individually

### 4E — CSS
- ⬜ Create CSS module for each component (plain CSS, no Tailwind, no UI libs)
- ⬜ Apply brand colors: Primary `#23235F`, Accent `#C62828`, BG `#F6F5F3`, Border `#DBDBDB`

---

## PHASE 5 — Frontend Dynamic Wiring
*Files in root `js/` folder*

- ⬜ Create `js/home-featured.js` — fetch `GET /api/projects?is_featured=true`, render 3 cards into `#home-projects-grid`
- ⬜ Verify `js/projects-dynamic.js` — test against live backend
- ⬜ Verify `js/project-detail.js` — test against live backend
- ⬜ Verify `js/careers-dynamic.js` — test against live backend
- ⬜ Wire contact form in `contact-us.html` — POST to `POST /api/contact` (after creating that route)
- ⬜ Change `API_BASE` in all 3 JS files from `http://localhost:5000` → `https://api.exellar.com`

---

## PHASE 6 — Image Upload (Admin Panel)

- ⬜ Add `POST /api/admin/upload` route to Flask — accepts image, saves to `/uploads/images/`, returns filename
- ⬜ Add drag-and-drop upload UI to `ProjectForm.jsx` — uploads image, stores returned filename in `thumbnail` field
- ⬜ Ensure Nginx serves `/uploads/` directory on VPS

---

## PHASE 7 — VPS Deployment
*See `DEPLOYMENT.md` for full step-by-step instructions*

- ⬜ SSH into Hostinger VPS
- ⬜ Install system dependencies (Python 3.11, Node 18, MySQL, Nginx, Certbot)
- ⬜ Clone repo to `/var/www/`
- ⬜ Set up MySQL database and user
- ⬜ Create `.env` file on VPS with production values
- ⬜ Set up Python venv and install requirements
- ⬜ Run `flask db upgrade` on VPS
- ⬜ Configure Gunicorn systemd service
- ⬜ Build React admin panel (`npm run build`)
- ⬜ Configure Nginx for all 3 domains
- ⬜ Run Certbot SSL for all 3 domains
- ⬜ Test all endpoints on production
- ⬜ Change admin password from default

---

## PHASE 8 — Go-Live Checklist
*Do not skip any item*

- ⬜ All placeholder images replaced with real Exellar photos
- ⬜ Hero video replaced with Exellar video
- ⬜ Client logos replaced with real PNG files
- ⬜ `API_BASE` changed to `https://api.exellar.com` in all JS files
- ⬜ `SECRET_KEY` in `.env` is a strong random string (not default)
- ⬜ Admin password changed from default
- ⬜ `reCAPTCHA` keys set for contact form
- ⬜ SSL certificates installed for all 3 domains
- ⬜ All 23 pages load without console errors
- ⬜ Forms submit successfully
- ⬜ Job applications save to DB and resume uploads work
- ⬜ Admin panel login works and all CRUD operations function
- ⬜ Mobile responsive — test on iPhone and Android
- ⬜ Google Analytics / GTM firing (update GTM ID from Turner's to Exellar's)
- ⬜ Remove Turner GTM ID `GTM-M593X6SF` from all pages — replace with Exellar's
- ⬜ `sitemap.xml` and `robots.txt` created
- ⬜ Canonical URLs updated to `exellar.co.in` across all pages
