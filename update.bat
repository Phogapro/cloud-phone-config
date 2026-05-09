@echo off

title Cloud Phone Config Manager

echo =========================
echo UPDATE START
echo =========================

echo.
echo [1/7] Checkout main branch...
git checkout main

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo CHECKOUT MAIN FAILED
    pause
    exit /b
)

echo.
echo [2/7] Pull latest from GitHub...
git pull origin main

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo GIT PULL FAILED
    pause
    exit /b
)

echo.
echo [3/7] Generate YAML...
python generate.py

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo GENERATE FAILED
    pause
    exit /b
)

echo.
echo [4/7] Add files...
git add .

echo.
echo [5/7] Commit...
git commit -m "auto update"

echo.
echo [6/7] Push...
git push origin main

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo PUSH FAILED
    pause
    exit /b
)

echo.
echo =========================
echo UPDATE SUCCESS
echo =========================

pause