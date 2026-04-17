@echo off
title Exellar — Stopping Services

echo.
echo  Stopping all Exellar services...

:: Kill by port
for %%P in (3000 3001 5000 5173) do (
    for /f "tokens=5" %%a in ('netstat -ano 2^>nul ^| findstr ":%%P "') do (
        taskkill /F /PID %%a >nul 2>&1
    )
)

:: Kill by window title
taskkill /FI "WINDOWTITLE eq Exellar Backend :5000" /F >nul 2>&1
taskkill /FI "WINDOWTITLE eq Exellar Admin :5173"   /F >nul 2>&1
taskkill /FI "WINDOWTITLE eq Exellar Website :3000"  /F >nul 2>&1

echo  All services stopped.
echo.
timeout /t 2 /nobreak >nul
