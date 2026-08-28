@echo off
setlocal

title JXR UltraHDR Converter

cd /d "%~dp0"

echo ============================================
echo       JXR UltraHDR Converter v1.0
echo ============================================
echo.

if not exist "Input" (
    mkdir "Input"
)

if not exist "Output" (
    mkdir "Output"
)

if not exist "Logs" (
    mkdir "Logs"
)

if not exist "Logs\tracker.json" (
    echo {}>"Logs\tracker.json"
)

echo Starting converter...
echo.

python -m src.main

echo.
echo ============================================
echo Finished.
echo ============================================
pause

endlocal
