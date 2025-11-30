import os
import pandas as pd
import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components

# -------------------------------------------------------------------
# BASIC CONFIG
# -------------------------------------------------------------------
st.set_page_config(page_title="AetherVision Omega", layout="wide")
OUTPUT_ROOT = "outputs"

# -------------------------------------------------------------------
# SAFE LOAD FUNCTIONS
# -------------------------------------------------------------------
def read_csv(path):
    if os.path.exists(path):
        return pd.read_csv(path)
    else:
        st.warning(f"Missing file: {path}")
        return None

def show_html(path):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()
        components.html(html, height=600, scrolling=True)
    else:
        st.warning(f"Missing HTML file: {path}")

def map_from_csv(df, lat_col="lat", lon_col="lon", color=None, title="Map"):
    if df is None:
        st.info("No data available.")
        return

    if lat_col not in df.columns or lon_col not in df.columns:
        st.error("Latitude/Longitude columns not found.")
        st.dataframe(df.head())
        return

    fig = px.scatter_mapbox(
        df,
        lat=lat_col,
        lon=lon_col,
        color=color if color else None,
        zoom=4,
        height=600,
        hover_data=df.columns
    )

    # ⭐ NO MAPBOX TOKEN — USE FREE OSM
    fig.update_layout(mapbox_style="open-street-map")

    st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------------------------
# SIDEBAR MENU
# -------------------------------------------------------------------
menu = st.sidebar.radio(
    "Select Module",
    [
        "Home",
        "Branch 1 – Digital Twin",
        "Branch 2 – Environmental Analytics",
        "Branch 3 – Fusion Risk Engine",
        "Branch 4 – Real-Time Urban Risk",
        "Branch 5 – 7-Day Forecast",
        "Branch 6 – GeoHealth Dashboard",
        "Branch 7 – Early Warning Alerts",
        "Branch 8 – Decision Engine"
    ]
)

# -------------------------------------------------------------------
# HOME
# -------------------------------------------------------------------
if menu == "Home":
    st.title("AetherVision Omega – Geo-AI SmartCity Guardian System")
    st.markdown("""
AetherVision Omega combines eight Geo-AI modules:

1. Core Digital Twin  
2. Environmental Analytics  
3. Fusion Risk Engine  
4. Real-Time Urban Risk Monitor  
5. 7-Day Hazard Forecast  
6. GeoHealth Dashboard  
7. Early Warning Alerts  
8. Decision Engine  
""")

# -------------------------------------------------------------------
# BRANCH 1 – DIGITAL TWIN (HTML Maps)
# -------------------------------------------------------------------
elif menu == "Branch 1 – Digital Twin":
    st.header("Branch 1 – Core Digital Twin")

    show_html(os.path.join(OUTPUT_ROOT, "branch1/digital_twin_base.html"))
    st.subheader("Environmental Layers")
    show_html(os.path.join(OUTPUT_ROOT, "branch1/india_env_layers.html"))
    st.subheader("Geology Layers")
    show_html(os.path.join(OUTPUT_ROOT, "branch1/geology_layers.html"))

# -------------------------------------------------------------------
# BRANCH 2 – ENVIRONMENTAL ANALYTICS
# -------------------------------------------------------------------
elif menu == "Branch 2 – Environmental Analytics":
    st.header("Branch 2 – Environmental Analytics")
    df = read_csv(os.path.join(OUTPUT_ROOT, "branch2/env_analytics.csv"))

    if df is not None:
        st.dataframe(df)
        lat_col = st.selectbox("Latitude Column", df.columns)
        lon_col = st.selectbox("Longitude Column", df.columns)
        col = st.selectbox("Color Column", df.columns)
        map_from_csv(df, lat_col, lon_col, col, "Environmental Hotspots")

# -------------------------------------------------------------------
# BRANCH 3 – FUSION RISK ENGINE
# -------------------------------------------------------------------
elif menu == "Branch 3 – Fusion Risk Engine":
    st.header("Branch 3 – Fusion Risk Engine")

    show_html(os.path.join(OUTPUT_ROOT, "branch3/fusion_risk_heatmap.html"))
    df = read_csv(os.path.join(OUTPUT_ROOT, "branch3/fusion_risk_scores.csv"))

    if df is not None:
        st.dataframe(df)

# -------------------------------------------------------------------
# BRANCH 4 – REAL-TIME URBAN RISK
# -------------------------------------------------------------------
elif menu == "Branch 4 – Real-Time Urban Risk":
    st.header("Branch 4 – Real-Time Urban Risk")

    show_html(os.path.join(OUTPUT_ROOT, "branch4/risk_map.html"))
    df = read_csv(os.path.join(OUTPUT_ROOT, "branch4/risk_scores.csv"))

    st.subheader("City Risk Table")
    if df is not None:
        st.dataframe(df)

    st.subheader("Hazard Report")
    report_path = os.path.join(OUTPUT_ROOT, "branch4/hazard_report.txt")
    if os.path.exists(report_path):
        st.text(open(report_path).read())

# -------------------------------------------------------------------
# BRANCH 5 – 7-DAY FORECAST
# -------------------------------------------------------------------
elif menu == "Branch 5 – 7-Day Forecast":
    st.header("Branch 5 – 7-Day Hazard Forecast")

    show_html(os.path.join(OUTPUT_ROOT, "branch5/forecast_heatmap.html"))
    df1 = read_csv(os.path.join(OUTPUT_ROOT, "branch5/7_day_hazard_forecast.csv"))
    df2 = read_csv(os.path.join(OUTPUT_ROOT, "branch5/forecast_with_scores.csv"))

    if df1 is not None:
        st.subheader("Forecast Table")
        st.dataframe(df1)

    if df2 is not None:
        st.subheader("Risk Trend")
        fig = px.line(df2, x="day", y="risk_score", title="7-Day Risk Trend")
        st.plotly_chart(fig)

    report_path = os.path.join(OUTPUT_ROOT, "branch5/forecast_report.txt")
    if os.path.exists(report_path):
        st.subheader("Forecast Report")
        st.text(open(report_path).read())

# -------------------------------------------------------------------
# BRANCH 6 – GEOHEALTH DASHBOARD
# -------------------------------------------------------------------
elif menu == "Branch 6 – GeoHealth Dashboard":
    st.header("Branch 6 – GeoHealth Dashboard")

    df = read_csv(os.path.join(OUTPUT_ROOT, "branch6/geohealth_scores.csv"))
    if df is not None:
        st.dataframe(df)
        fig = px.bar(df, x="city", y="health_risk_score", title="Health Risk by City")
        st.plotly_chart(fig)

# -------------------------------------------------------------------
# BRANCH 7 – EARLY WARNING ALERTS
# -------------------------------------------------------------------
elif menu == "Branch 7 – Early Warning Alerts":
    st.header("Branch 7 – Early Warning Alerts (48-Hr)")

    df = read_csv(os.path.join(OUTPUT_ROOT, "branch7/early_alerts.csv"))
    if df is not None:
        st.dataframe(df)

# -------------------------------------------------------------------
# BRANCH 8 – DECISION ENGINE
# -------------------------------------------------------------------
elif menu == "Branch 8 – Decision Engine":
    st.header("Branch 8 – Smart-City Decision Engine")

    df = read_csv(os.path.join(OUTPUT_ROOT, "branch8/city_decisions.csv"))
    if df is not None:
        st.dataframe(df)

        cities = df["city"].unique()
        selected = st.selectbox("Select City", cities)
        st.subheader(f"Recommendations for {selected}")
        st.table(df[df["city"] == selected])
