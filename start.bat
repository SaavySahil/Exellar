@echo off
echo ========================================
echo  Exellar Project - Local Dev Startup
echo ========================================
echo  Website  : http://localhost:3000/Home.html
echo  Admin    : http://localhost:5173
echo  Backend  : http://localhost:5000
echo  Login    : admin@exellar.co.in / Admin@123
echo ========================================

:: Kill anything already on these ports
echo Clearing ports 3000, 5000, 5173...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr /R ":3000 \|:5000 \|:5173 " 2^>nul') do (
    taskkill /F /PID %%a >nul 2>&1
)
timeout /t 3 /nobreak >nul

:: Backend: Flask on port 5000 (no reloader - prevents ghost processes)
echo [1/3] Starting Backend API on :5000 ...
start "Backend :5000" cmd /k "cd /d %~dp0exellar-backend && python -c \"from app import create_app; app = create_app(); app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)\""

timeout /t 4 /nobreak >nul

:: Admin: Vite React on port 5173
echo [2/3] Starting Admin Panel on :5173 ...
start "Admin :5173" cmd /k "cd /d %~dp0exellar-admin && npm run dev -- --host --port 5173"

:: Website: Static files on port 3000
echo [3/3] Starting Website on :3000 ...
start "Website :3000" cmd /k "cd /d %~dp0 && python -m http.server 3000"

timeout /t 5 /nobreak >nul
echo.
echo All services started. Opening browser...
start "" "http://localhost:3000/Home.html"
start "" "http://localhost:5173"
