@echo off
cd /d %~dp0

pyinstaller start.spec

pause