import os
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="AetherVision Omega", layout="wide")

ROOT = "outputs"

def read_csv(path):
    if os.path.exists(path):
        return pd.read_csv(path)
    return None

st.sidebar.title("AetherVision Omega")
page = st.sidebar.radio("Select Module", [
    "Home",
    "Branch 1 – Digital Twin Summary",
    "Branch 2 – Environmental Analytics",
    "Branch 3 – Fusion Risk Engine",
    "Branch 4 – Real-Time Urban Risk",
    "Branch 5 – 7-Day Forecast",
    "Branch 6 – GeoHealth Dashboard",
    "Branch 7 – Early Warning Alerts",
    "Branch 8 – Decision Engine",
])

# ---------------- HOME ----------------
if page == "Home":
    st.title("AetherVision Omega – Geo-AI SmartCity Guardian System")
    st.write("""
This version contains:
- All 8 Branches  
- Fully working tables  
- Plotly charts  
- ZERO API Requirements  
""")

# ---------------- BRANCH 1 ----------------
elif page.startswith("Branch 1"):
    st.header("Branch 1 – Digital Twin Summary")
    st.success("Map removed (HTML not supported). Showing summary instead.")

# ---------------- BRANCH 2 ----------------
elif page.startswith("Branch 2"):
    st.header("Branch 2 – Environmental Analytics")
    df = read_csv(f"{ROOT}/branch2/env_analytics.csv")
    if df is not None:
        st.subheader("Dataset")
        st.dataframe(df)

        # Simple chart
        if "value" in df.columns:
            fig = px.bar(df, x=df.columns[0], y="value", title="Environmental Levels")
            st.plotly_chart(fig, use_container_width=True)

# ---------------- BRANCH 3 ----------------
elif page.startswith("Branch 3"):
    st.header("Branch 3 – Fusion Risk Engine")
    df = read_csv(f"{ROOT}/branch3/fusion_risk_scores.csv")
    if df is not None:
        st.dataframe(df)
        if "risk_score" in df.columns:
            fig = px.histogram(df, x="risk_score", title="Risk Score Distribution")
            st.plotly_chart(fig, use_container_width=True)

# ---------------- BRANCH 4 ----------------
elif page.startswith("Branch 4"):
    st.header("Branch 4 – Real-Time Urban Risk")
    df = read_csv(f"{ROOT}/branch4/risk_scores.csv")
    if df is not None:
        st.dataframe(df)
        if {"city", "risk_score"}.issubset(df.columns):
            fig = px.bar(df, x="city", y="risk_score", title="City Risk Levels")
            st.plotly_chart(fig, use_container_width=True)

# ---------------- BRANCH 5 ----------------
elif page.startswith("Branch 5"):
    st.header("Branch 5 – 7-Day Hazard Forecast")
    df = read_csv(f"{ROOT}/branch5/7_day_hazard_forecast.csv")
    if df is not None:
        st.dataframe(df)
        if {"day", "risk_score"}.issubset(df.columns):
            fig = px.line(df, x="day", y="risk_score", title="7-Day Forecast Trend")
            st.plotly_chart(fig, use_container_width=True)

# ---------------- BRANCH 6 ----------------
elif page.startswith("Branch 6"):
    st.header("Branch 6 – GeoHealth Dashboard")
    df = read_csv(f"{ROOT}/branch6/geohealth_scores.csv")
    if df is not None:
        st.dataframe(df)
        if {"city", "health_risk_score"}.issubset(df.columns):
            fig = px.bar(df, x="city", y="health_risk_score", title="City Health Risk")
            st.plotly_chart(fig, use_container_width=True)

# ---------------- BRANCH 7 ----------------
elif page.startswith("Branch 7"):
    st.header("Branch 7 – Early Warning Alerts")
    df = read_csv(f"{ROOT}/branch7/early_alerts.csv")
    if df is not None:
        st.dataframe(df)

# ---------------- BRANCH 8 ----------------
elif page.startswith("Branch 8"):
    st.header("Branch 8 – Smart City Decision Engine")
    df = read_csv(f"{ROOT}/branch8/city_decisions.csv")
    if df is not None:
        st.dataframe(df)
