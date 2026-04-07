@echo off
echo.
echo  Installing dependencies...
pip install flask gunicorn > nul 2>&1
echo  Starting ATV eBaja Sponsor Collage...
echo.
python app.py
pause
