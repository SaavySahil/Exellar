# DEPLOYMENT.md — Zero-Defect Deployment Guide
## Exellar Construction LLP — Production VPS

> **This file must be read in full before touching the server.**
> **For every AI prompt involving deployment, paste this file or reference it explicitly.**

---

## ARCHITECTURE OVERVIEW

```
exellar.co.in          → Nginx → /var/www/exellar/html/       (Static HTML)
api.exellar.com        → Nginx → Gunicorn → Flask :5000        (Backend API)
admin.exellar.com      → Nginx → /var/www/exellar/admin/       (React dist)
```

Server: Hostinger VPS, Ubuntu 22.04 LTS
All three on the same server. SSL via Certbot (Let's Encrypt).

---

## BEFORE YOU TOUCH THE SERVER — PREFLIGHT

```
[ ] Backend code passes local tests (all API endpoints return correct responses)
[ ] React admin panel builds without errors (npm run build)
[ ] All placeholder images replaced with real images
[ ] API_BASE changed from localhost:5000 to https://api.exellar.com in:
      - js/projects-dynamic.js
      - js/project-detail.js
      - js/careers-dynamic.js
      - exellar-admin/src/api/client.js
[ ] .env file prepared with all production values (see Section 4)
[ ] Git repo is clean — no uncommitted changes
[ ] You have VPS root/sudo SSH access
```

---

## SECTION 1 — VPS Initial Setup (one-time only)

### 1.1 Connect to VPS
```bash
ssh root@YOUR_VPS_IP
```

### 1.2 Update system
```bash
apt update && apt upgrade -y
```

### 1.3 Install dependencies
```bash
# Python
apt install -y python3.11 python3.11-venv python3-pip

# Node.js 18
curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
apt install -y nodejs

# MySQL
apt install -y mysql-server
mysql_secure_installation

# Nginx
apt install -y nginx

# Certbot
apt install -y certbot python3-certbot-nginx

# Git
apt install -y git

# Screen (optional, useful for monitoring)
apt install -y screen
```

### 1.4 Create deploy user (recommended — don't run everything as root)
```bash
adduser exellar
usermod -aG sudo exellar
# Add your SSH key to /home/exellar/.ssh/authorized_keys
```

---

## SECTION 2 — MySQL Database Setup

```bash
mysql -u root -p
```

```sql
CREATE DATABASE exellar_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'exellar_user'@'localhost' IDENTIFIED BY 'STRONG_PASSWORD_HERE';
GRANT ALL PRIVILEGES ON exellar_db.* TO 'exellar_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

**Save these values** — you will need them in `.env`.

---

## SECTION 3 — Clone Repository

```bash
mkdir -p /var/www/exellar
cd /var/www/exellar
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git .
```

Directory structure after clone:
```
/var/www/exellar/
├── Home.html              ← and all other HTML pages
├── css/
├── js/
├── images/
├── exellar-backend/
├── exellar-admin/
└── ...
```

---

## SECTION 4 — Backend Environment Setup

### 4.1 Create .env file
```bash
cd /var/www/exellar/exellar-backend
nano .env
```

```env
# Flask
FLASK_ENV=production
SECRET_KEY=GENERATE_A_STRONG_RANDOM_KEY_HERE_64_CHARS_MIN
DEBUG=False

# Database
DATABASE_URL=mysql+pymysql://exellar_user:STRONG_PASSWORD_HERE@localhost/exellar_db

# File uploads
UPLOAD_FOLDER=/var/www/exellar/uploads
MAX_CONTENT_LENGTH=16777216

# CORS
CORS_ORIGINS=https://exellar.co.in,https://admin.exellar.com

# JWT
JWT_EXPIRY_HOURS=24
```

Generate a secure SECRET_KEY:
```bash
python3 -c "import secrets; print(secrets.token_hex(64))"
```

### 4.2 Create uploads directory
```bash
mkdir -p /var/www/exellar/uploads/resumes
mkdir -p /var/www/exellar/uploads/images
chmod 755 /var/www/exellar/uploads
```

### 4.3 Python virtual environment
```bash
cd /var/www/exellar/exellar-backend
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4.4 Database migration
```bash
cd /var/www/exellar/exellar-backend
source venv/bin/activate
export FLASK_APP=run.py
flask db upgrade
```

**Verify migration succeeded:**
```bash
mysql -u exellar_user -p exellar_db -e "SHOW TABLES;"
```

Expected tables: `admin_user`, `project`, `job`, `job_application`, `content_field`, `alembic_version`

### 4.5 Test Flask runs
```bash
source venv/bin/activate
python run.py
# Should print: Running on http://127.0.0.1:5000
# Press Ctrl+C to stop
```

---

## SECTION 5 — Gunicorn Systemd Service

### 5.1 Install Gunicorn
```bash
source /var/www/exellar/exellar-backend/venv/bin/activate
pip install gunicorn
```

### 5.2 Create systemd service
```bash
nano /etc/systemd/system/exellar-api.service
```

```ini
[Unit]
Description=Exellar Construction API (Gunicorn)
After=network.target

[Service]
User=exellar
Group=www-data
WorkingDirectory=/var/www/exellar/exellar-backend
Environment="PATH=/var/www/exellar/exellar-backend/venv/bin"
EnvironmentFile=/var/www/exellar/exellar-backend/.env
ExecStart=/var/www/exellar/exellar-backend/venv/bin/gunicorn \
    --workers 4 \
    --bind 127.0.0.1:5000 \
    --timeout 120 \
    --access-logfile /var/log/exellar/api-access.log \
    --error-logfile /var/log/exellar/api-error.log \
    run:app
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
mkdir -p /var/log/exellar
chown exellar:www-data /var/log/exellar
systemctl daemon-reload
systemctl enable exellar-api
systemctl start exellar-api
systemctl status exellar-api    # Should show: active (running)
```

---

## SECTION 6 — Admin Panel Build

```bash
cd /var/www/exellar/exellar-admin

# Install dependencies
npm install

# Build for production
npm run build

# Move dist to serve location
cp -r dist/* /var/www/exellar/admin/
```

Or set Nginx to serve directly from `/var/www/exellar/exellar-admin/dist/`.

---

## SECTION 7 — Nginx Configuration

### 7.1 Main site — exellar.co.in

```bash
nano /etc/nginx/sites-available/exellar-frontend
```

```nginx
server {
    listen 80;
    server_name exellar.co.in www.exellar.co.in;
    root /var/www/exellar;
    index Home.html;

    # Serve static files
    location / {
        try_files $uri $uri/ $uri.html =404;
    }

    # Cache images, CSS, JS
    location ~* \.(jpg|jpeg|png|gif|ico|svg|css|js|mp4|webm|woff|woff2|ttf)$ {
        expires 30d;
        add_header Cache-Control "public, no-transform";
    }

    # Serve uploads
    location /uploads/ {
        alias /var/www/exellar/uploads/;
        expires 7d;
    }

    access_log /var/log/nginx/exellar-frontend-access.log;
    error_log /var/log/nginx/exellar-frontend-error.log;
}
```

### 7.2 API — api.exellar.com

```bash
nano /etc/nginx/sites-available/exellar-api
```

```nginx
server {
    listen 80;
    server_name api.exellar.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 120;
        proxy_connect_timeout 120;
    }

    # Resume uploads — larger body size
    location /api/applications {
        client_max_body_size 16M;
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    access_log /var/log/nginx/exellar-api-access.log;
    error_log /var/log/nginx/exellar-api-error.log;
}
```

### 7.3 Admin Panel — admin.exellar.com

```bash
nano /etc/nginx/sites-available/exellar-admin
```

```nginx
server {
    listen 80;
    server_name admin.exellar.com;
    root /var/www/exellar/exellar-admin/dist;
    index index.html;

    # React Router — all routes serve index.html
    location / {
        try_files $uri $uri/ /index.html;
    }

    # Cache static assets
    location ~* \.(js|css|png|jpg|ico|svg|woff|woff2)$ {
        expires 7d;
        add_header Cache-Control "public, no-transform";
    }

    access_log /var/log/nginx/exellar-admin-access.log;
    error_log /var/log/nginx/exellar-admin-error.log;
}
```

### 7.4 Enable sites and test
```bash
ln -s /etc/nginx/sites-available/exellar-frontend /etc/nginx/sites-enabled/
ln -s /etc/nginx/sites-available/exellar-api /etc/nginx/sites-enabled/
ln -s /etc/nginx/sites-available/exellar-admin /etc/nginx/sites-enabled/

# Remove default
rm /etc/nginx/sites-enabled/default

# Test config
nginx -t    # Must say: syntax is ok / test is successful

# Reload
systemctl reload nginx
```

---

## SECTION 8 — SSL Certificates (Certbot)

**DNS must be pointing to VPS IP before running this.**

```bash
# All three domains in one command
certbot --nginx \
    -d exellar.co.in \
    -d www.exellar.co.in \
    -d api.exellar.com \
    -d admin.exellar.com \
    --email info@exellar.co.in \
    --agree-tos \
    --non-interactive
```

Certbot will automatically update Nginx configs to redirect HTTP → HTTPS.

**Verify auto-renewal:**
```bash
certbot renew --dry-run    # Should say: success
```

---

## SECTION 9 — DNS Records (Hostinger Domain Panel)

Set these A records in your domain registrar:

| Type | Name | Value | TTL |
|---|---|---|---|
| A | @ | YOUR_VPS_IP | 3600 |
| A | www | YOUR_VPS_IP | 3600 |
| A | api | YOUR_VPS_IP | 3600 |
| A | admin | YOUR_VPS_IP | 3600 |

DNS propagation can take up to 24 hours. Check with:
```bash
nslookup exellar.co.in
nslookup api.exellar.com
nslookup admin.exellar.com
```

---

## SECTION 10 — Post-Deployment Verification

Run these checks **in order** after deployment. Do not skip any.

```bash
# 1. API health check
curl https://api.exellar.com/api/projects
# Expected: JSON array (empty [] is fine if no projects added yet)

# 2. Auth check
curl -X POST https://api.exellar.com/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"admin@exellar.co.in","password":"Admin@123"}'
# Expected: {"token": "eyJ..."}

# 3. Gunicorn running
systemctl status exellar-api
# Expected: active (running)

# 4. Nginx running
systemctl status nginx
# Expected: active (running)

# 5. SSL valid
curl -I https://exellar.co.in
# Expected: HTTP/2 200

# 6. Frontend loads
curl -I https://exellar.co.in/Home.html
# Expected: 200 OK

# 7. Admin panel loads
curl -I https://admin.exellar.com
# Expected: 200 OK

# 8. Check logs for errors
tail -50 /var/log/exellar/api-error.log
tail -50 /var/log/nginx/exellar-api-error.log
```

---

## SECTION 11 — Updating the Site (after changes)

### Update frontend HTML/JS/CSS:
```bash
cd /var/www/exellar
git pull origin master
# No restart needed — Nginx serves static files directly
```

### Update backend Python code:
```bash
cd /var/www/exellar
git pull origin master
cd exellar-backend
source venv/bin/activate
pip install -r requirements.txt    # if requirements changed
flask db upgrade                   # if models changed
systemctl restart exellar-api
systemctl status exellar-api
```

### Update admin panel:
```bash
cd /var/www/exellar/exellar-admin
git pull origin master
npm install
npm run build
# dist/ is already served by Nginx
```

---

## SECTION 12 — Security Hardening (do not skip)

```bash
# Change default admin password immediately after first login
# In admin panel: Settings → Change Password

# Firewall
ufw allow OpenSSH
ufw allow 'Nginx Full'
ufw --force enable
ufw status

# Disable root SSH login
nano /etc/ssh/sshd_config
# Set: PermitRootLogin no
# Set: PasswordAuthentication no
systemctl restart sshd

# MySQL — ensure only localhost access
mysql -u root -p -e "SELECT user, host FROM mysql.user;"
# exellar_user should only have localhost, not %
```

---

## SECTION 13 — Backup Strategy

```bash
# Database backup (run daily via cron)
mysqldump -u exellar_user -p exellar_db > /backups/exellar_db_$(date +%Y%m%d).sql

# Uploads backup
tar -czf /backups/uploads_$(date +%Y%m%d).tar.gz /var/www/exellar/uploads/

# Set up cron
crontab -e
# Add:
# 0 2 * * * mysqldump -u exellar_user -pPASSWORD exellar_db > /backups/exellar_db_$(date +\%Y\%m\%d).sql
# 0 3 * * * tar -czf /backups/uploads_$(date +\%Y\%m\%d).tar.gz /var/www/exellar/uploads/
```

---

## COMMON ERRORS & FIXES

| Error | Cause | Fix |
|---|---|---|
| `502 Bad Gateway` on api.exellar.com | Gunicorn not running | `systemctl restart exellar-api` |
| `404` on admin routes | React Router not configured | Check Nginx `try_files $uri /index.html` |
| `413 Request Entity Too Large` | Resume upload too big | Add `client_max_body_size 16M;` to Nginx |
| `CORS error` in browser | CORS_ORIGINS in .env wrong | Check origin includes `https://exellar.co.in` |
| SSL certificate expired | Auto-renewal failed | `certbot renew --force-renewal` |
| DB migration fails | Missing alembic version | `flask db stamp head` then `flask db upgrade` |
| `ModuleNotFoundError` | Venv not activated | `source venv/bin/activate` |

---

## EMERGENCY ROLLBACK

If deployment breaks production:

```bash
cd /var/www/exellar
git log --oneline -10         # Find last working commit hash
git checkout COMMIT_HASH       # Roll back to that commit
systemctl restart exellar-api  # Restart API if backend changed
```
