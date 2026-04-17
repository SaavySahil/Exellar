# Exellar — Free Tier Deployment Guide

## Architecture (Demo)

```
exellar.pages.dev          →  Cloudflare Pages  (static HTML website)
exellar-admin.vercel.app   →  Vercel             (React admin panel)
exellar-api.onrender.com   →  Render.com         (Flask backend API)
                           →  Render PostgreSQL   (free DB, 90-day limit)
```

---

## Step 1 — Push to GitHub

```bash
# In your terminal, from C:\Users\Shabbir Shaikh\Downloads\Welcome:
gh auth login                         # if not already logged in
gh repo create exellar --public --source=. --remote=origin --push
```

That's it. One command creates the repo under SaavySahil/exellar and pushes master.

---

## Step 2 — Deploy Backend (Render.com)

1. Go to **https://render.com** → Sign up with GitHub
2. Click **New → Blueprint** → Connect your GitHub → Select `SaavySahil/exellar`
3. Render auto-reads `render.yaml` → click **Apply**
4. It will create:
   - `exellar-api` (web service, free)
   - `exellar-db` (PostgreSQL, free 90 days)
5. Wait ~3 min for first deploy → note your URL: `https://exellar-api.onrender.com`

---

## Step 3 — Deploy Admin Panel (Vercel)

1. Go to **https://vercel.com** → Sign up with GitHub
2. Click **Add New → Project** → import `SaavySahil/exellar`
3. Set **Root Directory** → `exellar-admin`
4. Vercel auto-reads `vercel.json` → click **Deploy**
5. Your admin panel: `https://exellar-admin.vercel.app`

---

## Step 4 — Deploy Static Website (Cloudflare Pages)

1. Go to **https://pages.cloudflare.com** → Sign up (free)
2. Click **Create application → Pages → Connect to Git**
3. Select `SaavySahil/exellar`
4. Settings:
   - **Build command**: *(leave empty)*
   - **Build output directory**: `/` (root)
   - **Root directory**: *(leave empty)*
5. Deploy → Your site: `https://exellar.pages.dev`

---

## Step 5 — Update CORS on Render

After Cloudflare and Vercel are deployed, update CORS in Render:

1. Render dashboard → `exellar-api` → **Environment**
2. Edit `CORS_ORIGINS`:
   ```
   https://exellar.pages.dev,https://exellar-admin.vercel.app
   ```
3. Save → auto-redeploys

---

## CI/CD (Auto-deploy on push)

All three platforms watch your `master` branch automatically:
- Push code → GitHub → Cloudflare Pages rebuilds in ~30s
- Push code → GitHub → Vercel rebuilds in ~1 min  
- Push code → GitHub → Render rebuilds in ~2 min

No extra setup needed.

---

## Local Development (unchanged)

Run `start.bat` — same as before.

| Service | URL |
|---------|-----|
| Website | http://localhost:3000/Home.html |
| Admin   | http://localhost:5173 |
| Backend | http://localhost:5000 |
| Login   | admin@exellar.co.in / Admin@123 |

---

## Later: Migrate to Hostinger VPS

See `DEPLOYMENT.md` for the Nginx + Gunicorn + Certbot setup on Ubuntu 22.04.
