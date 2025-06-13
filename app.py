
import streamlit as st
import pandas as pd
from hhemm_model import run_hhemm_model

st.set_page_config(page_title="HHEMM Dashboard", layout="wide")

st.title("📊 HHEMM Model - Hitter Performance Dashboard")
st.markdown("Upload Statcast data with key metrics to score and classify top hitters.")

uploaded_file = st.file_uploader("Upload your Statcast CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        st.subheader("📂 Raw Uploaded Data")
        st.dataframe(df.head(20))

        st.subheader("⚙️ Running HHEMM Model...")
        results = run_hhemm_model(df)

        if not results.empty:
            st.success(f"✅ {len(results)} hitters passed the HHEMM model gate.")
            st.dataframe(results[['Player', 'Team', 'Score', 'Role']])

            st.download_button("⬇️ Download Results", results.to_csv(index=False), "hhemm_results.csv", "text/csv")
        else:
            st.warning("No players met the HHEMM model criteria.")

    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("Please upload a valid CSV file with columns like 'xBA', 'xSLG', 'Barrel%', etc.")
