@echo off
cd /d %~dp0

py -3.4 build.py py2exe

pause