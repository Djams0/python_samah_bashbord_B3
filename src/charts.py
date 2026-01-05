import plotly.express as px

def bar_top_languages(df):
    return px.bar(
        df,
        x="langue",
        y="nb_sessions",
        title="🌍 Top des langues",
        text_auto=True
    )


def pie_services(df):
    return px.pie(
        df,
        names="service",
        values="nb_sessions",
        title="🏥 Répartition par service"
    )


def line_sessions_over_time(df):
    return px.line(
        df,
        x="date",
        y="sessions",
        title="📈 Évolution du nombre de sessions"
    )


def scatter_interactions(df):
    return px.scatter(
        df,
        x="interactions_patient",
        y="interactions_praticien",
        color="service",
        title="🤝 Interactions patient vs praticien",
        hover_data=["langue", "device"]
    )


def histogram_notes(df):
    return px.histogram(
        df,
        x="note_praticien",
        nbins=10,
        title="⭐ Distribution des notes praticiens"
    )
