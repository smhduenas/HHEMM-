
import streamlit as st
import pandas as pd
from hhemm_model import run_hhemm_model
from preprocess_statcast import fetch_and_prepare_data

st.set_page_config(page_title="HHEMM Dashboard", layout="wide")
st.title("📊 HHEMM Model - Hitter Performance Dashboard")

st.markdown("Upload Statcast data **or** fetch live data to score and classify top hitters using the HHEMM model.")

# Option 1: Upload CSV
uploaded_file = st.file_uploader("📂 Upload Statcast CSV", type="csv")

# Option 2: Fetch live data
with st.sidebar:
    st.markdown("### 🛰️ Fetch Statcast Data")
    start_date = st.date_input("Start date")
    end_date = st.date_input("End date")
    fetch_button = st.button("Fetch & Run HHEMM")

results = None

# Handle CSV upload
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.subheader("📂 Uploaded Data")
        st.dataframe(df.head())

        st.subheader("⚙️ Running HHEMM Model...")
        results = run_hhemm_model(df)
    except Exception as e:
        st.error(f"Error processing uploaded file: {e}")

# Handle live fetch
elif fetch_button and start_date and end_date:
    with st.spinner("Fetching and processing Statcast data..."):
        try:
            df = fetch_and_prepare_data(str(start_date), str(end_date))
            if df is not None and not df.empty:
                st.subheader("📡 Live Statcast Data")
                st.dataframe(df.head())

                st.subheader("⚙️ Running HHEMM Model...")
                results = run_hhemm_model(df)
            else:
                st.warning("⚠️ No Statcast data found for this date range.")
        except Exception as e:
            st.error(f"Failed to fetch or process data: {e}")

# Display results
if results is not None:
    if not results.empty:
        st.success(f"✅ {len(results)} hitters passed the HHEMM model gate.")
        st.dataframe(results[['Player', 'Team', 'Score', 'Role']])
        st.download_button("⬇️ Download Results CSV", results.to_csv(index=False), "hhemm_results.csv")
    else:
        st.warning("No players met the HHEMM model criteria.")
