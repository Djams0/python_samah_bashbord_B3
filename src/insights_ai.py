import pandas as pd
import numpy as np

def generate_insights(df: pd.DataFrame) -> list[str]:
    insights = []

    if df.empty:
        return ["⚠️ Aucun insight disponible (aucune donnée après filtrage)."]

    # 1️⃣ Langue dominante
    top_lang = df["langue"].value_counts().idxmax()
    top_lang_pct = round(
        (df["langue"].value_counts().max() / len(df)) * 100, 1
    )

    insights.append(
        f"🌍 La langue la plus utilisée est **{top_lang.upper()}**, représentant **{top_lang_pct}%** des sessions."
    )

    # 2️⃣ Service le plus utilisé
    top_service = df["service"].value_counts().idxmax()
    insights.append(
        f"🏥 Le service médical le plus sollicité est **{top_service.upper()}**."
    )

    # 3️⃣ Qualité globale
    qualite_moy = df["qualite_score"].mean()

    if qualite_moy >= 0.8:
        insights.append(
            "✅ La qualité globale des sessions est **très bonne** (score > 0.8)."
        )
    elif qualite_moy >= 0.6:
        insights.append(
            "🟡 La qualité globale des sessions est **acceptable**, mais peut être améliorée."
        )
    else:
        insights.append(
            "🔴 La qualité globale des sessions est **faible** — une amélioration du modèle IA est recommandée."
        )

    # 4️⃣ Segments non reconnus
    pct_segments = (df["has_segments_non_reconnus"].mean()) * 100

    if pct_segments > 30:
        insights.append(
            f"⚠️ **{round(pct_segments,1)}%** des sessions contiennent des segments audio non reconnus."
        )
    else:
        insights.append(
            f"🎧 Les erreurs de reconnaissance audio restent **limitées** ({round(pct_segments,1)}%)."
        )

    # 5️⃣ Interactions patient vs praticien
    ratio = df["ratio_patient_praticien"].mean()

    if ratio > 1.2:
        insights.append(
            "🗣️ Les patients interagissent **plus que les praticiens**, ce qui peut indiquer des besoins d’assistance accrus."
        )
    elif ratio < 0.8:
        insights.append(
            "👨‍⚕️ Les praticiens dominent les échanges, suggérant des consultations très guidées."
        )
    else:
        insights.append(
            "🤝 Les interactions patient/praticien sont **équilibrées**."
        )

    # 6️⃣ Corrélation durée / qualité
    corr = df["duree_minutes"].corr(df["qualite_score"])

    if corr > 0.4:
        insights.append(
            "📈 Les sessions plus longues tendent à être associées à une **meilleure qualité**."
        )
    elif corr < -0.4:
        insights.append(
            "📉 Les sessions longues semblent associées à une **baisse de qualité**."
        )
    else:
        insights.append(
            "➖ Aucune corrélation forte entre la durée des sessions et la qualité."
        )

    # 7️⃣ Recommandation IA finale
    insights.append(
        "💡 **Recommandation IA** : prioriser l’optimisation des services les plus utilisés "
        "et améliorer la reconnaissance audio pour les langues dominantes."
    )

    return insights
