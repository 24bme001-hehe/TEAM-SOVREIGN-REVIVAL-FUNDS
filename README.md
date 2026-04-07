# 🏎️ ATV eBaja — Sponsor Collage

## ▶️ Run in VS Code (2 steps only)

### Step 1 — Open terminal in VS Code
Press `Ctrl + `` ` `` (backtick) to open the terminal.

### Step 2 — Run the app

**Windows:**
```
run.bat
```

**Mac / Linux:**
```
bash run.sh
```

Then open your browser and go to → **http://localhost:5000**

---

## 📝 To update sponsors

Edit the `sponsors.csv` file — it has two columns:

```
Name,Amount
Rahul Sharma,5000
Priya Patel,3500
```

Save the file, then **refresh your browser**. Done!

- Bigger amount = bigger font on the collage
- The page auto-refreshes every 5 minutes

---

## 📁 Project Structure
```
ebaja-sponsors/
├── app.py              ← Flask server
├── sponsors.csv        ← Edit this with real names & amounts
├── run.bat             ← Windows one-click launcher
├── run.sh              ← Mac/Linux one-click launcher
├── requirements.txt
├── templates/
│   └── index.html      ← The collage page
└── static/
    └── images/
        └── atv.png     ← ATV background image
```
