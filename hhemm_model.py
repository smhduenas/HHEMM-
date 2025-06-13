
import pandas as pd

# --- HHEMM Filtering Logic ---
def filter_hhemm(df, xba_min=0.275, hh_min=35, contact_min=75, k_max=22, barrel_min=5, xslg_min=0.450):
    required_columns = ['xBA', 'HardHit%', 'Contact%', 'K%', 'Barrel%', 'xSLG', 'RosterStatus']
    df = df.dropna(subset=required_columns)
    df = df[
        (df['RosterStatus'] == 'Active') &
        (df['xBA'] >= xba_min) &
        (df['HardHit%'] >= hh_min) &
        (df['Contact%'] >= contact_min) &
        (df['K%'] <= k_max) &
        (df['Barrel%'] >= barrel_min) &
        (df['xSLG'] >= xslg_min)
    ]
    return df

# --- HHEMM Scoring ---
def score_hhemm(row):
    score = 0
    score += row['xBA'] * 10                        # 25% weight
    score += row['xSLG'] * 6                        # 15% weight
    score += row['xwOBA'] * 10                      # 25% weight
    score += (row['Contact%'] / 100) * 8            # 10% weight
    score += (row['HardHit%'] / 100) * 8            # 10% weight
    score += (row['Barrel%'] / 100) * 6             # 10% weight
    score += (1 - row['K%'] / 100) * 6              # 5% weight
    return round(score, 2)

# --- HHEMM Role Classification ---
def tag_role(row):
    if row['LineupSpot'] == 1 and row['Contact%'] >= 78 and row['Barrel%'] < 5:
        return "Soft Contact Leadoff"
    elif row['LineupSpot'] <= 3 and row['xBA'] > 0.300:
        return "Lead-Off Contact"
    elif row['xBA_vs_SameHandedPitching'] > 0.290:
        return "Reverse Platoon Edge"
    elif row['LineupSpot'] in [3, 4, 5] and row['xSLG'] > 0.475:
        return "Middle Anchor"
    elif row['Barrel%'] > 9 and row['EV'] > 91:
        return "Crush Specialist"
    elif row['Contact%'] > 80 and row['Chase%'] < 22:
        return "Low-Variance Magnet"
    return "Unclassified"

# --- Full HHEMM Pipeline ---
def run_hhemm_model(df):
    df = filter_hhemm(df)
    df['Score'] = df.apply(score_hhemm, axis=1)
    df['Role'] = df.apply(tag_role, axis=1)
    df = df[df['Score'] >= 8.0]  # model gate
    return df.sort_values(by='Score', ascending=False)
