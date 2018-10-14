@echo off
TITLE NodeLife: Will you survive ?
cd /d %~dp0

if exist bin\node\node.exe (
    set BINARY=bin\node\node.exe
) else (
    set BINARY=node
)

if exist index.js (
	set FILE=index.js
) else (
	echo "Couldn't find a valid installation"
	exit 1
)

REM pause on exitcode != 0 so the user can see what went wrong
%BINARY% %FILE% %*

pause