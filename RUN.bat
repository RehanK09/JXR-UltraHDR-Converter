@echo off
title JXR → Ultra HDR Converter

cd /d "%~dp0"

echo ============================================
echo      JXR -> Ultra HDR Converter v0.9
echo ============================================
echo.

if not exist Input (
    mkdir Input
)

if not exist Output (
    mkdir Output
)

if not exist Logs (
    mkdir Logs
)

if not exist Logs\tracker.json (
    echo {}>Logs\tracker.json
)

python -m src.main

echo.
echo ============================================
echo Finished.
echo ============================================
pause