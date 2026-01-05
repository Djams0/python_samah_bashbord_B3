import pandas as pd

def compute_kpis(df: pd.DataFrame) -> dict:
    return {
        "total_sessions": len(df),
        "duree_moyenne": round(df["duree_minutes"].mean(), 2),
        "qualite_moyenne": round(df["qualite_score"].mean(), 3),
        "pct_segments_non_reconnus": round(
            df["has_segments_non_reconnus"].mean() * 100, 2
        ),
        "ratio_interactions": round(df["ratio_patient_praticien"].mean(), 2)
    }


def sessions_over_time(df: pd.DataFrame):
    return (
        df.groupby(df["date"].dt.date)
        .size()
        .reset_index(name="sessions")
    )


def top_languages(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df["langue"]
        .value_counts()
        .rename("nb_sessions")
        .reset_index()
        .rename(columns={"index": "langue"})
    )


def service_distribution(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df["service"]
        .value_counts()
        .rename("nb_sessions")
        .reset_index()
        .rename(columns={"index": "service"})
    )

