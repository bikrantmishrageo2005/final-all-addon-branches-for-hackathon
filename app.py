import os
import pandas as pd
import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AetherVision Omega – Geo-AI SmartCity Guardian",
    layout="wide"
)

OUTPUT_ROOT = "outputs"


def safe_read_csv(path):
    if os.path.exists(path):
        try:
            return pd.read_csv(path)
        except:
            return None
    return None


def safe_show_html(path, height=600):
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                components.html(f.read(), height=height, scrolling=True)
        except:
            pass


def section(title):
    st.subheader(title)
    st.markdown("---")


st.sidebar.title("AetherVision Omega")
st.sidebar.write("Geo-AI SmartCity Guardian System")

branch = st.sidebar.radio(
    "Select Module",
    [
        "Home",
        "Branch 1 – Core Digital Twin",
        "Branch 2 – Environmental Analytics",
        "Branch 3 – Geo-AI Fusion Risk Engine",
        "Branch 4 – Real-Time Urban Risk",
        "Branch 5 – 7-Day Urban Hazard Forecast",
        "Branch 6 – GeoHealth Dashboard",
        "Branch 7 – Early Warning Alerts",
        "Branch 8 – Smart-City Decision Engine"
    ]
)

# --------------------------------------------------------------
# HOME
# --------------------------------------------------------------
if branch == "Home":
    st.title("AetherVision Omega – Geo-AI SmartCity Guardian")

    st.write("""
AetherVision Omega is a Geo-AI Smart City Guardian System with 8 integrated modules:
1. Core Digital Twin  
2. Environmental Analytics  
3. Geo-AI Fusion Risk Engine  
4. Real-Time Urban Risk  
5. 7-Day Hazard Forecast  
6. GeoHealth Dashboard  
7. Early Warning Alerts  
8. Smart-City Decision Engine  
""")


# --------------------------------------------------------------
# BRANCH 1
# --------------------------------------------------------------
elif branch == "Branch 1 – Core Digital Twin":
    section("Branch 1 – Core GeoAI Digital Twin")

    base_html = os.path.join(OUTPUT_ROOT, "branch1", "digital_twin_base.html")
    env_html = os.path.join(OUTPUT_ROOT, "branch1", "india_env_layers.html")
    geo_html = os.path.join(OUTPUT_ROOT, "branch1", "geology_layers.html")

    view = st.radio(
        "Select View",
        ["Digital Twin Base", "Environmental Layers", "Geological Layers", "Full Dashboard"],
        horizontal=True
    )

    if view == "Digital Twin Base":
        safe_show_html(base_html)

    elif view == "Environmental Layers":
        safe_show_html(env_html)

    elif view == "Geological Layers":
        safe_show_html(geo_html)

    else:
        col1, col2 = st.columns(2)
        with col1:
            safe_show_html(base_html, 300)
            safe_show_html(env_html, 300)
        with col2:
            safe_show_html(geo_html, 600)


# --------------------------------------------------------------
# BRANCH 2
# --------------------------------------------------------------
elif branch == "Branch 2 – Environmental Analytics":
    section("Branch 2 – Environmental Analytics")

    csv_path = os.path.join(OUTPUT_ROOT, "branch2", "env_analytics.csv")
    df = safe_read_csv(csv_path)

    if df is not None:
        st.dataframe(df)

        lat = st.selectbox("Latitude column", df.columns)
        lon = st.selectbox("Longitude column", df.columns)
        color = st.selectbox("Color column", df.columns)

        fig = px.scatter_mapbox(
            df, lat=lat, lon=lon, color=color,
            mapbox_style="carto-positron", zoom=4, height=600
        )
        st.plotly_chart(fig, use_container_width=True)


# --------------------------------------------------------------
# BRANCH 3
# --------------------------------------------------------------
elif branch == "Branch 3 – Geo-AI Fusion Risk Engine":
    section("Branch 3 – Geo-AI Fusion Risk Engine")

    fusion_csv = os.path.join(OUTPUT_ROOT, "branch3", "fusion_risk_scores.csv")
    fusion_html = os.path.join(OUTPUT_ROOT, "branch3", "fusion_risk_heatmap.html")

    df = safe_read_csv(fusion_csv)

    tab1, tab2 = st.tabs(["Risk Heatmap", "Risk Scores"])

    with tab1:
        safe_show_html(fusion_html)

    with tab2:
        if df is not None:
            st.dataframe(df)
            if "risk_score" in df.columns:
                st.plotly_chart(
                    px.histogram(df, x="risk_score", nbins=20),
                    use_container_width=True
                )


# --------------------------------------------------------------
# BRANCH 4
# --------------------------------------------------------------
elif branch == "Branch 4 – Real-Time Urban Risk":
    section("Branch 4 – Real-Time Urban Risk Model")

    risk_csv = os.path.join(OUTPUT_ROOT, "branch4", "risk_scores.csv")
    risk_html = os.path.join(OUTPUT_ROOT, "branch4", "risk_map.html")
    report = os.path.join(OUTPUT_ROOT, "branch4", "hazard_report.txt")

    df = safe_read_csv(risk_csv)

    tab1, tab2, tab3 = st.tabs(["Risk Map", "City Risk Scores", "Report"])

    with tab1:
        safe_show_html(risk_html)

    with tab2:
        if df is not None:
            st.dataframe(df)
            if "risk_level" in df.columns:
                st.plotly_chart(
                    px.bar(df, x="city", y="risk_score", color="risk_level"),
                    use_container_width=True
                )

    with tab3:
        if os.path.exists(report):
            with open(report, "r") as f:
                st.text(f.read())


# --------------------------------------------------------------
# BRANCH 5
# --------------------------------------------------------------
elif branch == "Branch 5 – 7-Day Urban Hazard Forecast":
    section("Branch 5 – 7-Day Hazard Forecast")

    csv1 = os.path.join(OUTPUT_ROOT, "branch5", "7_day_hazard_forecast.csv")
    csv2 = os.path.join(OUTPUT_ROOT, "branch5", "forecast_with_scores.csv")
    html = os.path.join(OUTPUT_ROOT, "branch5", "forecast_heatmap.html")
    report = os.path.join(OUTPUT_ROOT, "branch5", "forecast_report.txt")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Forecast Heatmap", "Trend Graph", "Forecast Table", "Report"]
    )

    with tab1:
        safe_show_html(html)

    with tab2:
        df_scores = safe_read_csv(csv2)
        if df_scores is not None:
            if {"day", "risk_score"}.issubset(df_scores.columns):
                st.plotly_chart(
                    px.line(df_scores, x="day", y="risk_score"),
                    use_container_width=True
                )

    with tab3:
        df_fore = safe_read_csv(csv1)
        if df_fore is not None:
            st.dataframe(df_fore)

    with tab4:
        if os.path.exists(report):
            with open(report, "r") as f:
                st.text(f.read())


# --------------------------------------------------------------
# BRANCH 6
# --------------------------------------------------------------
elif branch == "Branch 6 – GeoHealth Dashboard":
    section("Branch 6 – GeoHealth Dashboard")

    csv_path = os.path.join(OUTPUT_ROOT, "branch6", "geohealth_scores.csv")
    df = safe_read_csv(csv_path)

    if df is not None:
        st.dataframe(df)

        if "city" in df.columns and "health_risk_score" in df.columns:
            st.plotly_chart(
                px.bar(df, x="city", y="health_risk_score"),
                use_container_width=True
            )


# --------------------------------------------------------------
# BRANCH 7
# --------------------------------------------------------------
elif branch == "Branch 7 – Early Warning Alerts":
    section("Branch 7 – Early Warning Alerts")

    csv_path = os.path.join(OUTPUT_ROOT, "branch7", "early_alerts.csv")
    df = safe_read_csv(csv_path)

    if df is not None:
        st.dataframe(df)
        if "alert_level" in df.columns:
            st.plotly_chart(
                px.histogram(df, x="alert_level"),
                use_container_width=True
            )


# --------------------------------------------------------------
# BRANCH 8
# --------------------------------------------------------------
elif branch == "Branch 8 – Smart-City Decision Engine":
    section("Branch 8 – Smart-City Decision Engine")

    csv_path = os.path.join(OUTPUT_ROOT, "branch8", "city_decisions.csv")
    df = safe_read_csv(csv_path)

    if df is not None:
        st.dataframe(df)

        if "status" in df.columns:
            status_count = df["status"].value_counts().reset_index()
            status_count.columns = ["status", "count"]

            st.plotly_chart(
                px.bar(status_count, x="status", y="count"),
                use_container_width=True
            )

        if "city" in df.columns:
            city = st.selectbox("Select City", df["city"].unique())
            st.table(df[df["city"] == city])
