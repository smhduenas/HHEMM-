
import pandas as pd
from pybaseball import statcast_batter
from pybaseball import playerid_lookup

def fetch_and_prepare_data(start_date, end_date):
    # Step 1: Fetch Statcast data
    print(f"Fetching Statcast data from {start_date} to {end_date}...")
    df = statcast_batter(start_date, end_date)

    # Step 2: Basic sanity check
    if df.empty:
        print("No data found.")
        return None

    # Step 3: Aggregate to per-player metrics (example: xBA, xSLG, etc.)
    df_grouped = df.groupby(['player_name', 'team']).agg({
        'estimated_ba_using_speedangle': 'mean',  # xBA
        'estimated_woba_using_speedangle': 'mean',  # xwOBA
        'launch_speed': 'mean',  # EV
        'launch_angle': 'mean',
        'events': 'count',
        'barrel': 'sum',
        'description': 'count'
    }).reset_index()

    df_grouped.rename(columns={
        'player_name': 'Player',
        'team': 'Team',
        'estimated_ba_using_speedangle': 'xBA',
        'estimated_woba_using_speedangle': 'xwOBA',
        'launch_speed': 'EV',
        'barrel': 'BarrelCount',
        'description': 'PA'
    }, inplace=True)

    # Add mock placeholders for model-required stats not present in pybaseball's statcast_batter
    df_grouped['RosterStatus'] = 'Active'
    df_grouped['HardHit%'] = 37.0 + (df_grouped.index % 5)  # Simulated
    df_grouped['Contact%'] = 78.0 - (df_grouped.index % 6)  # Simulated
    df_grouped['K%'] = 20.0 + (df_grouped.index % 3)        # Simulated
    df_grouped['Barrel%'] = (df_grouped['BarrelCount'] / df_grouped['PA']) * 100
    df_grouped['xSLG'] = df_grouped['xBA'] * 1.5            # Simulated
    df_grouped['Chase%'] = 21.0 + (df_grouped.index % 3)    # Simulated
    df_grouped['LineupSpot'] = 1 + (df_grouped.index % 9)   # Simulated
    df_grouped['xBA_vs_SameHandedPitching'] = df_grouped['xBA'] * 0.98 + 0.01

    # Return a cleaned DataFrame ready for the HHEMM model
    return df_grouped
