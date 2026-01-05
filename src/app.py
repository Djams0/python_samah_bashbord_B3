import streamlit as st
from data_loader import load_data
from filters import apply_filters
from utils import (
    compute_kpis,
    sessions_over_time,
    top_languages,
    service_distribution
)
import charts

st.set_page_config(
    page_title="Dashaalia - Dashboard Analytique",
    layout="wide"
)

st.title("📊 Dashboard Analytique — Dashaalia")

# Chargement données
df = load_data("data/sessions_dataset_320.csv")

# Filtres
dff = apply_filters(df)

# KPIs
kpis = compute_kpis(dff)

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Sessions", kpis["total_sessions"])
c2.metric("Durée moyenne (min)", kpis["duree_moyenne"])
c3.metric("Qualité moyenne", kpis["qualite_moyenne"])
c4.metric("% segments non reconnus", f'{kpis["pct_segments_non_reconnus"]}%')
c5.metric("Ratio patient/praticien", kpis["ratio_interactions"])

st.divider()

# Visualisations
col1, col2 = st.columns(2)

with col1:
    lang_df = top_languages(dff)
    st.plotly_chart(charts.bar_top_languages(lang_df), use_container_width=True)

with col2:
    service_df = service_distribution(dff)
    st.plotly_chart(charts.pie_services(service_df), use_container_width=True)

# Time series
time_df = sessions_over_time(dff)
st.plotly_chart(charts.line_sessions_over_time(time_df), use_container_width=True)

# Interactions
st.plotly_chart(charts.scatter_interactions(dff), use_container_width=True)

# Notes
st.plotly_chart(charts.histogram_notes(dff), use_container_width=True)

st.divider()

# Table + export
st.subheader("📄 Détails des sessions")
st.dataframe(dff, use_container_width=True)

csv = dff.to_csv(index=False)
st.download_button(
    "📥 Exporter les données filtrées",
    csv,
    "sessions_filtrees.csv",
    "text/csv"
)
