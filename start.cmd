@echo off
cd /d %~dp0

if exist start.py (
	set FILE=start.py
) else (
	echo "Couldn't find a valid Entry point"
	pause
	exit 1
)

py %FILE% %*

pause