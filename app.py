import os
from flask import Flask, render_template

# 1. Get the absolute path to the directory this file is in
base_dir = os.path.abspath(os.path.dirname(__file__))

# 2. Append the 'templates' folder to that path
template_dir = os.path.join(base_dir, 'templates')

# 3. Tell Flask exactly where to look
app = Flask(__name__, template_folder=template_dir)

# ... the rest of your app.py code ...from flask import Flask, render_template, jsonify
import os, csv

app = Flask(__name__)

DEMO_SPONSORS = [
    {"name": "Rahul Sharma",  "amount": 5000},
    {"name": "Priya Patel",   "amount": 3500},
    {"name": "Arjun Mehta",   "amount": 2000},
    {"name": "Sneha Desai",   "amount": 1500},
    {"name": "Karan Joshi",   "amount": 1000},
    {"name": "Nisha Gupta",   "amount": 800},
    {"name": "Vikram Singh",  "amount": 600},
    {"name": "Ananya Rao",    "amount": 500},
    {"name": "Rohan Kapoor",  "amount": 400},
    {"name": "Divya Nair",    "amount": 250},
    {"name": "Siddharth K",   "amount": 200},
    {"name": "Meera Iyer",    "amount": 150},
]

CSV_FILE = os.path.join(os.path.dirname(__file__), "sponsors.csv")

def get_sponsors():
    if os.path.exists(CSV_FILE):
        sponsors = []
        with open(CSV_FILE, newline="", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0 and row and row[0].strip().lower() in ("name", "names"):
                    continue
                if len(row) < 2:
                    continue
                try:
                    name   = str(row[0]).strip()
                    amount = float(str(row[1]).replace(",", "").replace("\u20b9", "").strip())
                    if name and amount > 0:
                        sponsors.append({"name": name, "amount": amount})
                except (ValueError, IndexError):
                    continue
        if sponsors:
            sponsors.sort(key=lambda x: x["amount"], reverse=True)
            return sponsors
    return sorted(DEMO_SPONSORS, key=lambda x: x["amount"], reverse=True)

@app.route("/")
def index():
    return render_template("index.html", sponsors=get_sponsors())

@app.route("/api/sponsors")
def api_sponsors():
    return jsonify(get_sponsors())

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print("\n" + "="*52)
    print("  ATV eBaja Sponsor Collage is RUNNING!")
    print("  Open your browser and go to:")
    print(f"  >>>  http://localhost:{port}  <<<")
    print("="*52 + "\n")
    app.run(host="0.0.0.0", port=port, debug=True)
