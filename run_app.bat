@echo off
echo Call Schedule Generator
echo =====================
echo.
echo Starting application...
echo.

python run_app.py

if errorlevel 1 (
    echo.
    echo Error running the application.
    echo Please make sure Python is installed and in your PATH.
    echo.
    pause
) 