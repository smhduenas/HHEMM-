
# ⚾ HHEMM: Hitter Evaluation & Matchup Model

This project powers a full Statcast-based dashboard to:
- 📊 Score MLB hitters using advanced metrics (xBA, xwOBA, Hard Hit %, etc.)
- ⚾ Display upcoming MLB matchups & probable pitchers
- 🎯 Help identify prop betting edges (Hits, TBs, HRs)

---

## 🚀 How to Run

1. Clone this repo  
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run hhemm_system.py
```

---

## 📂 Files

| File | Purpose |
|------|---------|
| `hhemm_system.py` | All-in-one Streamlit app + slate fetcher + scorer |
| `requirements.txt` | Required packages |
| `data/` | (Optional) Store your downloaded statcast CSVs |

---

## 📥 Input Data

Upload a CSV from Baseball Savant with columns like:
- `xBA`, `xSLG`, `xwOBA`, `Barrel%`, `Hard Hit %`, `K%`, `BB%`, `EV`, etc.

---

## 🧠 Model Logic

Hitters are scored using a custom weighted model based on:
- Contact quality
- Discipline
- Speed
- Swing tendencies

---

## 🌐 Streamlit Deployment

If deploying to [streamlit.io](https://streamlit.io):
- Just push to GitHub
- Point Streamlit Cloud to `hhemm_system.py`
- Done!

