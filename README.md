
# HHEMM Dashboard

🏟️ **HHEMM** (Hard-Hit Expected Metric Model) is a scoring model built on advanced Statcast metrics to identify elite offensive performers.

## 🚀 Features

- Filters hitters using Statcast metrics (xBA, xSLG, Contact%, K%, Barrel%, etc.)
- Scores and ranks players using a weighted algorithm
- Tags players with roles like:
  - "Crush Specialist"
  - "Lead-Off Contact"
  - "Low-Variance Magnet"
- Interactive Streamlit dashboard to upload data and view results

## 📂 CSV Format

Upload a CSV with the following columns (example):

```
Player,Team,xBA,xSLG,xwOBA,HardHit%,Contact%,K%,Barrel%,EV,Chase%,LineupSpot,xBA_vs_SameHandedPitching,RosterStatus
```

You can use `preprocess_statcast.py` to generate this format from live Statcast data using the `pybaseball` package.

## 🧪 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📦 Requirements

- streamlit
- pandas
- numpy
- pybaseball (optional, for Statcast data pull)

## 📬 Contact

Built by ripbookie. For support or ideas, open an issue or fork the repo!
