import streamlit as st
import pandas as pd

def apply_filters(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("🎛️ Filtres")

    # Date
    min_date = df["date"].min()
    max_date = df["date"].max()

    date_range = st.sidebar.date_input(
        "Plage de dates",
        value=(min_date, max_date)
    )

    # Filtres catégoriels
    services = st.sidebar.multiselect(
        "Service médical",
        options=sorted(df["service"].unique())
    )

    langues = st.sidebar.multiselect(
        "Langue",
        options=sorted(df["langue"].unique())
    )

    devices = st.sidebar.multiselect(
        "Device",
        options=sorted(df["device"].unique())
    )

    dff = df.copy()

    # Application filtres
    if date_range:
        start, end = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
        dff = dff[(dff["date"] >= start) & (dff["date"] <= end)]

    if services:
        dff = dff[dff["service"].isin(services)]

    if langues:
        dff = dff[dff["langue"].isin(langues)]

    if devices:
        dff = dff[dff["device"].isin(devices)]

    return dff
