@echo off
cd /d %~dp0

if exist start.py (
	set FILE=start.py
) else (
	echo "Couldn't find a valid installation"
	pause
	exit 1
)

py -3.4 %FILE% %*

pause