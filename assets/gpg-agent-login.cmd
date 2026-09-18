@echo off
REM Runs after every Windows login.
REM Restarts gpg-agent: kill the old one, then start a fresh one.

set "GPG_CONNECT=C:\Program Files\GnuPG\bin\gpg-connect-agent.exe"

REM Give the user session a moment to finish starting.
timeout /t 3 /nobreak >nul

"%GPG_CONNECT%" killagent /bye
"%GPG_CONNECT%" /bye