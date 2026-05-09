@echo off

echo =========================
echo UPDATE START
echo =========================

git checkout main

git pull origin main

python generate.py

git add .

git commit -m "auto update"

git push origin main

echo.
echo =========================
echo UPDATE SUCCESS
echo =========================

pause