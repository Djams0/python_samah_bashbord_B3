import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path: str):
    df = pd.read_csv(path)

    # Dates
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.to_period("M").astype(str)

    # Nettoyage colonnes numériques
    numeric_cols = [
        "duree_minutes",
        "interactions_patient",
        "interactions_praticien",
        "interactions_totales",
        "note_praticien",
        "qualite_score",
        "segments_non_reconnus"
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Nettoyage texte
    text_cols = ["service", "langue", "device"]
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip().str.lower()

    # Features dérivées
    df["ratio_patient_praticien"] = df["interactions_patient"] / (
        df["interactions_praticien"] + 1e-6
    )

    df["has_segments_non_reconnus"] = df["segments_non_reconnus"] > 0

    return df
