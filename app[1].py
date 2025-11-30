
import os
import pandas as pd
import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components

st.set_page_config(page_title="AetherVision Omega", layout="wide")

root = "outputs"

def read(path):
    return pd.read_csv(path) if os.path.exists(path) else None

def show_html(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            components.html(f.read(), height=600, scrolling=True)

menu = st.sidebar.radio("Modules", [
    "Home",
    "Branch 1",
    "Branch 2",
    "Branch 3",
    "Branch 4",
    "Branch 5",
    "Branch 6",
    "Branch 7",
    "Branch 8"
])

if menu == "Home":
    st.title("AetherVision Omega – Geo-AI SmartCity Guardian System")

if menu == "Branch 1":
    st.header("Branch 1 – Digital Twin")
    show_html(os.path.join(root, "branch1/digital_twin_base.html"))

if menu == "Branch 2":
    st.header("Branch 2 – Environmental Analytics")
    df = read(os.path.join(root, "branch2/env_analytics.csv"))
    if df is not None: st.dataframe(df)

if menu == "Branch 3":
    st.header("Branch 3 – Fusion Risk Engine")
    df = read(os.path.join(root, "branch3/fusion_risk_scores.csv"))
    if df is not None: st.dataframe(df)

if menu == "Branch 4":
    st.header("Branch 4 – Real-Time Urban Risk")
    df = read(os.path.join(root, "branch4/risk_scores.csv"))
    if df is not None: st.dataframe(df)

if menu == "Branch 5":
    st.header("Branch 5 – 7-Day Forecast")
    df = read(os.path.join(root, "branch5/7_day_hazard_forecast.csv"))
    if df is not None: st.dataframe(df)

if menu == "Branch 6":
    st.header("Branch 6 – GeoHealth Dashboard")
    df = read(os.path.join(root, "branch6/geohealth_scores.csv"))
    if df is not None: st.dataframe(df)

if menu == "Branch 7":
    st.header("Branch 7 – Early Warning Alerts")
    df = read(os.path.join(root, "branch7/early_alerts.csv"))
    if df is not None: st.dataframe(df)

if menu == "Branch 8":
    st.header("Branch 8 – Decision Engine")
    df = read(os.path.join(root, "branch8/city_decisions.csv"))
    if df is not None: st.dataframe(df)
