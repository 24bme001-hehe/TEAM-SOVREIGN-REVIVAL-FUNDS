#!/bin/bash
echo ""
echo " Installing dependencies..."
pip install flask gunicorn -q
echo " Starting ATV eBaja Sponsor Collage..."
echo ""
python app.py
