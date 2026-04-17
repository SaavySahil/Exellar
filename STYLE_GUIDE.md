# Exellar Construction — Style Guide

## The Golden Rule

**Never touch the frontend design. Ever.**

The CSS (`css/style.css`), all JS libraries, and all HTML structure are preserved from the Turner Construction base. Every dynamic feature is added by:

- Injecting minimal HTML hooks (`id` attributes, empty containers)
- Writing separate JS files that fetch from the API and render into those containers
- Using **only existing CSS classes** — never writing new ones
- Using inline styles only for functional toggles (`display:none`, modal overlays)

If you feel the urge to add a stylesheet, create a new CSS class, or restructure existing HTML — stop. You're doing it wrong.

---

## Brand Identity

| Token | Value |
|---|---|
| Primary | `#23235F` (deep navy) |
| Accent | `#C62828` (red) |
| Background | `#F6F5F3` (off-white) |
| Border | `#DBDBDB` |
| Text | `#2E2E2E` |

**Company:** Exellar Construction LLP  
**Domain:** exellar.co.in  
**Admin:** admin.exellar.com  
**API:** api.exellar.com (localhost:5000 in dev)

---

## Frontend — HTML Pages

### Grid System

```
col-d-{N}   Desktop columns (out of 100, e.g. col-d-25 = 25%)
col-t-{N}   Tablet columns
col-m-{N}   Mobile columns
inline_block Required wrapper class alongside col-d-* classes
```

**Standard card layout:**
```html
<div class="inline_block col-d-25 col-t-50 col-m-100 anim-elem top">
  <!-- card content -->
</div>
```

### Animation Classes

GSAP + ScrollTrigger watches these — do not omit them on dynamic content.

```
anim-block      Container — triggers the scroll animation group
anim-elem top   Child element — animates in from below on scroll
```

After injecting dynamic content always call:
```js
window.ScrollTrigger.refresh();
document.dispatchEvent(new CustomEvent('dynamicContentLoaded'));
```

### Lazy Images (Blazy)

**Always** use `b-lazy` + `data-src`, never plain `src` on dynamic images:

```html
<img class="b-lazy" data-src="images/project-hero.jpg" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" alt="Project Name">
```

After injecting cards into a container:
```js
// bLazy or Blazy — handle both
if (window.bLazy) window.bLazy.revalidate();
else if (window.Blazy) new Blazy({ selector: '#your-container .b-lazy' });
```

### Scroll Locking (Lenis)

Lenis is active on all pages via `vendor.js`. Never use `overflow: hidden` to lock scroll.

```js
// Lock
if (window.lenis) window.lenis.stop();

// Unlock
if (window.lenis) window.lenis.start();
```

### Forms

**Never use `<form>` tags** on the frontend. Build `FormData` manually:

```js
const data = new FormData();
data.append('name', document.getElementById('name').value);
// Do NOT set Content-Type manually — browser sets it with boundary
fetch('/api/applications', { method: 'POST', body: data });
```

### Dynamic JS File Pattern

Each dynamic page gets its own JS file in `/js/`. File reads a page-scoped variable set inline before the script tag:

```html
<!-- In the HTML page -->
<script>var PROJECTS_STATUS = "ongoing";</script>
<script src="js/projects-dynamic.js"></script>
```

```js
// In the JS file
const status = window.PROJECTS_STATUS || 'ongoing';
fetch(`${API_BASE}/api/projects?status=${status}`)
  .then(r => r.json())
  .then(data => renderCards(data));
```

### Image Paths

Thumbnail field in the API stores **filename only** (e.g. `project-hero.jpg`).  
Frontend always prepends the folder:

```js
const src = project.thumbnail ? 'images/' + project.thumbnail : 'images/project-placeholder.jpg';
```

---

## Backend — Flask API

### Project Structure

```
exellar-backend/
├── app/
│   ├── __init__.py         App factory, CORS, blueprints, auto-seeder
│   ├── config.py           Dev/Prod config from .env
│   ├── extensions.py       db, migrate
│   ├── models/
│   │   ├── admin.py        AdminUser (bcrypt password)
│   │   ├── project.py      Project (auto-slug, JSON gallery)
│   │   ├── job.py          Job (enum type, is_active flag)
│   │   ├── application.py  JobApplication (SET NULL FK, title snapshot)
│   │   └── content.py      ContentField (key-value CMS)
│   ├── routes/
│   │   ├── auth.py         POST /api/auth/login
│   │   ├── projects.py     Public + Admin CRUD
│   │   ├── jobs.py         Public + Admin CRUD
│   │   ├── applications.py Submit + Admin list/download
│   │   └── content.py      Public read + Admin upsert
│   └── utils/
│       ├── auth_middleware.py  JWT decorator + decode_token()
│       └── file_handler.py    save_resume(), get_resume_path()
```

### API Conventions

- All endpoints prefixed `/api/`
- Admin endpoints prefixed `/api/admin/` and require `Authorization: Bearer <token>`
- UUIDs for all primary keys
- JSON responses, snake_case keys
- Resume download accepts **both** `Authorization` header and `?token=` query param (required for `window.open()`)

### Auth

```
POST /api/auth/login        { email, password } → { token }
Default admin: admin@exellar.com / Admin@123
JWT secret in .env as SECRET_KEY
```

### Route Protection

```python
from app.utils.auth_middleware import token_required

@bp.route('/api/admin/projects', methods=['GET'])
@token_required
def list_projects(current_user):
    ...
```

### Data Models — Key Fields

**Project**
```
id, title, slug (auto from title, unique),
category, status (ongoing|completed),
location, scope, size, client_name,
services, partners,
story_headline, story_body,
client_testimonial,
thumbnail (filename only),
gallery (JSON array of filenames),
is_featured (bool),
created_at, updated_at
```

**Job**
```
id, title, department, location,
type (full-time|part-time|contract),
description, requirements,
is_active (bool),
created_at, updated_at
```

**JobApplication**
```
id, job_id (FK nullable SET NULL), job_title (snapshot),
applicant_name, email, phone,
resume_path, cover_note, applied_at
```

**ContentField**
```
key (PK string), value (text), updated_at
```
Seeded keys: `home_hero_tagline`, `about_summary`, `projects_hero_tagline`, `careers_hero_tagline`

---

## Admin Panel — React

### Stack

```
React 18 + Vite
React Router v6
TanStack Query v5
Axios (with JWT interceptor)
Plain CSS Modules only — no Tailwind, no UI libraries
```

### Project Structure

```
exellar-admin/src/
├── api/client.js           Axios instance + auto 401 redirect
├── context/AuthContext.jsx Token in localStorage, login/logout
├── pages/
│   ├── Login.jsx
│   ├── Dashboard.jsx       Stat cards + recent applications
│   ├── Projects.jsx        Table with filter tabs + delete
│   ├── ProjectForm.jsx     Create/edit with slug preview
│   ├── Jobs.jsx            Table with toggle active
│   ├── JobForm.jsx
│   ├── Applications.jsx    Table + resume download
│   └── Content.jsx         4 CMS fields, save individually
└── components/
    ├── Layout.jsx          Fixed sidebar 240px + topbar
    ├── Sidebar.jsx         NavLink active states
    ├── StatusBadge.jsx     Pill badges
    ├── ConfirmModal.jsx    Delete confirmation
    └── Toast.jsx           Auto-dismiss 3s notifications
```

### Admin UI Rules

- **No `<form>` tags** — use `div` wrappers with `button onClick` handlers
- Brand colors from the token table above, applied via CSS Modules
- Sidebar fixed at 240px width
- All data mutations go through TanStack Query's `useMutation`
- 401 responses auto-redirect to `/login` via Axios interceptor

### Resume Download

```js
// Must use ?token= query param — Authorization header doesn't work for window.open()
const token = localStorage.getItem('token');
window.open(`${API_BASE}/api/admin/applications/${id}/resume?token=${token}`);
```

---

## Python Build Scripts

These scripts live at the repo root and mutate HTML files in place. **Run order matters** — always check what a script does before running it on a page that's already been branded.

| Script | Purpose |
|---|---|
| `rebrand.py` | Global text find-and-replace (Turner → Exellar) |
| `safe_reskin.py` | Safer rebrand with backup |
| `safe_text_replace.py` | Targeted string replacement |
| `build_home.py` | Rebuild Home.html sections |
| `build_extra_pages.py` | Build secondary pages |
| `rebuild_pages.py` | Rebuild multiple pages from templates |
| `_gen_project_pages.py` | Generate Ongoing/Completed project pages |
| `_gen_project_detail.py` | Generate Project-Detail.html template |
| `inject_developer_narrative.py` | Add developer-positioning copy |
| `update_nav.py` | Update navigation links across all pages |
| `update_megamenu.py` | Update megamenu across all pages |
| `update_global_contact.py` | Update contact details globally |
| `remove_contact_nav.py` | Strip Turner contact nav items |
| `anti_copyright_layout.py` | Remove Turner copyright from layout |
| `anti_copyright_css.py` | Remove Turner copyright from CSS |
| `fix_spacing.py` | Fix spacing issues post-rebrand |
| `link_css.py` | Re-link CSS after modifications |
| `remove_theme_link.py` | Remove Turner theme stylesheet references |

**Warning:** Running `rebrand.py` or `safe_reskin.py` on an already-branded page will double-process it. Always work from the last committed state.

---

## Deployment (Planned)

```
exellar.co.in         → Nginx → /var/www/exellar/      (static HTML)
api.exellar.com       → Nginx → Gunicorn → Flask :5000
admin.exellar.com     → Nginx → /var/www/exellar-admin/ (React dist/)
```

Server: Hostinger VPS, Ubuntu 22.04, SSL via Certbot.

**Before going live — checklist:**
- [ ] Change `API_BASE` from `http://localhost:5000` to `https://api.exellar.com` in all three JS files (`projects-dynamic.js`, `project-detail.js`, `careers-dynamic.js`)
- [ ] Set `SECRET_KEY`, `DATABASE_URL`, and `UPLOAD_FOLDER` in VPS `.env`
- [ ] Run `flask db upgrade` on VPS
- [ ] Configure Nginx vhosts for all three domains
- [ ] Enable Gunicorn systemd service
- [ ] Run Certbot for SSL on all three domains
- [ ] Wire contact form to Flask endpoint
- [ ] Update megamenu links across all 23 pages to point to new pages
