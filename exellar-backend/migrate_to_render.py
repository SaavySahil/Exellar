#!/usr/bin/env python3
"""
migrate_to_render.py
Pushes all projects from migrate_data.json to the live Render API.

Usage:
  cd exellar-backend
  python migrate_to_render.py

The script skips:
  - "TEST" / "Test" entries (id index 0 and 1)
  - Projects whose slug already exists on Render

Requires: requests  (pip install requests)
"""

import json, sys
try:
    import requests
except ImportError:
    sys.exit("ERROR: run  pip install requests  first")

API   = "https://exellar-api.onrender.com"
EMAIL = "admin@exellar.co.in"
PASSW = "Admin@123"

# ── 1. Login ─────────────────────────────────────────────────────────────────
print("Logging in…", end=" ", flush=True)
r = requests.post(f"{API}/api/auth/login",
                  json={"email": EMAIL, "password": PASSW},
                  timeout=30)
if not r.ok:
    sys.exit(f"FAIL ({r.status_code}): {r.text[:300]}")
resp_json = r.json()
token = resp_json.get("access_token") or resp_json.get("token")
if not token:
    sys.exit(f"No token in response: {resp_json}")
print("OK")

headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}

# ── 2. Fetch already-existing slugs ─────────────────────────────────────────
print("Fetching existing projects…", end=" ", flush=True)
existing_r = requests.get(f"{API}/api/projects", timeout=30)
existing_slugs = set()
if existing_r.ok:
    for p in existing_r.json():
        existing_slugs.add(p.get("slug", ""))
print(f"{len(existing_slugs)} already on server")

# ── 3. Load local data ────────────────────────────────────────────────────────
with open("migrate_data.json", "r", encoding="utf-8") as f:
    projects = json.load(f)

SKIP_TITLES = {"TEST", "Test - 2"}

created, skipped, errors = 0, 0, 0

for p in projects:
    title = p.get("title", "")
    slug  = p.get("slug", "")

    if title in SKIP_TITLES:
        print(f"  SKIP  {title!r}  (test entry)")
        skipped += 1
        continue

    if slug in existing_slugs:
        print(f"  SKIP  {title!r}  (slug already exists)")
        skipped += 1
        continue

    payload = {
        "title":             p.get("title"),
        "slug":              slug,
        "category":          p.get("category"),
        "status":            p.get("status", "ongoing"),
        "location":          p.get("location"),
        "scope":             p.get("scope"),
        "size":              str(p.get("size", "")) if p.get("size") else None,
        "client_name":       p.get("client_name"),
        "services":          p.get("services"),
        "partners":          p.get("partners"),
        "story_headline":    p.get("story_headline"),
        "story_body":        p.get("story_body"),
        "client_testimonial":p.get("client_testimonial"),
        "is_featured":       bool(p.get("is_featured", False)),
        # thumbnail/gallery are file paths from the old DB — skip them
        # (images need to be re-uploaded manually via the admin panel)
    }

    try:
        cr = requests.post(f"{API}/api/admin/projects",
                           json=payload, headers=headers, timeout=30)
        if cr.ok:
            print(f"  OK    {title!r}")
            created += 1
            existing_slugs.add(slug)
        else:
            print(f"  ERR   {title!r}  ({cr.status_code}) {cr.text[:200]}")
            errors += 1
    except Exception as e:
        print(f"  EXCEPTION  {title!r}: {e}")
        errors += 1

print(f"\n{'='*50}")
print(f"Created: {created}  |  Skipped: {skipped}  |  Errors: {errors}")
print("Done.")
