import streamlit as st
import pandas as pd
import plotly.express as px

# Définir le thème Streamlit
st.set_page_config(
    page_title="Dashboard KPIs - Twitter",
    page_icon=":bar_chart:",
    layout="wide",
)

# Ajouter un titre principal
st.title("Tableau de Bord Interactif des KPIs Twitter :chart_with_upwards_trend:")

# Charger les données
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path, sep=';')
    return df

file_path = "./output/filtered_tweets_engie_final_with_inconfort.csv"
df = load_data(file_path)

# Conversion des dates et gestion des colonnes
if 'created_at' in df.columns:
    df['date'] = pd.to_datetime(df['created_at'], errors='coerce').dt.date
if 'hour' in df.columns:
    df['hour'] = pd.to_numeric(df['hour'], errors='coerce').fillna(0).astype(int)

if 'contains_keywords' in df.columns:
    df['contains_keywords'] = df['contains_keywords'].astype(bool)

# Sidebar pour les filtres
with st.sidebar:
    st.header("Filtres :wrench:")

    # Filtre de la granularité temporelle
    time_granularity = st.selectbox("Granularité Temporelle", ["Heure", "Jour", "Semaine", "Mois"])

    # Filtre pour la plage de dates (uniquement pour la granularité "Jour")
    if time_granularity == "Jour" and 'date' in df.columns:
        min_date = df['date'].min()
        max_date = df['date'].max()
        start_date, end_date = st.date_input(
            "Plage de Dates",
            min_value=min_date,
            max_value=max_date,
            value=(min_date, max_date),
        )
        # Assurez-vous que toutes les dates sont bien au format `datetime.date`
        if 'date' in df.columns:
            df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date

        # Convertir les dates de filtre en format `datetime.date`
        if start_date and end_date:
            start_date = start_date.date() if hasattr(start_date, 'date') else start_date
            end_date = end_date.date() if hasattr(end_date, 'date') else end_date

            # Filtrage des dates avec le bon format
            df = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    else:
        start_date = None
        end_date = None

# KPIs
kpi1, kpi2, kpi3 = st.columns(3)

# KPI 1: Nombre total de tweets
total_tweets = len(df)
kpi1.metric(
    label="Nombre Total de Tweets",
    value=f"{total_tweets:,}",
)

# KPI 2: Nombre de tweets critiques
total_critiques = df['contains_keywords'].sum()
kpi2.metric(
    label="Nombre Total de Tweets Critiques",
    value=f"{total_critiques:,}",
)

# KPI 3: Répartition des sentiments
positive_count = (df['sentiment'] == 'Positif').sum()
negative_count = (df['sentiment'] == 'Négatif').sum()
neutral_count = (df['sentiment'] == 'Neutre').sum()

kpi3.metric(
    label="Répartition des Sentiments",
    value=f"😀 {positive_count} | 😡 {negative_count} | 😐 {neutral_count}"
)

st.markdown("""---""")

# Graphiques
col1, col2 = st.columns(2)

with col1:
    # Graphique 1: Nombre de tweets par granularité temporelle
    if time_granularity == "Heure":
        tweets_per_hour = df.groupby('hour').size().reset_index(name='nombre_tweets')
        fig_tweets = px.bar(tweets_per_hour, x='hour', y='nombre_tweets',
                            title='Nombre de Tweets par Heure',
                            color_discrete_sequence=["#0083B8"])
    elif time_granularity == "Jour":
        tweets_per_day = df.groupby('date').size().reset_index(name='nombre_tweets')
        fig_tweets = px.line(tweets_per_day, x='date', y='nombre_tweets',
                             title='Nombre de Tweets par Jour',
                             color_discrete_sequence=["#0083B8"])
    elif time_granularity == "Semaine":
        df['week'] = pd.to_datetime(df['created_at']).dt.strftime('%Y-%U')
        tweets_per_week = df.groupby('week').size().reset_index(name='nombre_tweets')
        fig_tweets = px.bar(tweets_per_week, x='week', y='nombre_tweets',
                            title='Nombre de Tweets par Semaine',
                            color_discrete_sequence=["#0083B8"])
    else:  # Mois
        df['month'] = pd.to_datetime(df['created_at']).dt.strftime('%Y-%m')
        tweets_per_month = df.groupby('month').size().reset_index(name='nombre_tweets')
        fig_tweets = px.bar(tweets_per_month, x='month', y='nombre_tweets',
                            title='Nombre de Tweets par Mois',
                            color_discrete_sequence=["#0083B8"])
    st.plotly_chart(fig_tweets, use_container_width=True)

with col2:
    # Graphique 2: Nombre de tweets critiques
    if time_granularity == "Heure":
        critiques_par_heure = df[df['contains_keywords']].groupby('hour').size().reset_index(name='tweets_critiques')
        fig_critiques = px.line(critiques_par_heure, x='hour', y='tweets_critiques',
                                title='Nombre de Tweets Critiques par Heure',
                                color_discrete_sequence=["#E377C2"])
    elif time_granularity == "Jour":
        critiques_par_jour = df[df['contains_keywords']].groupby('date').size().reset_index(name='tweets_critiques')
        fig_critiques = px.line(critiques_par_jour, x='date', y='tweets_critiques',
                                title='Nombre de Tweets Critiques par Jour',
                                color_discrete_sequence=["#E377C2"])
    elif time_granularity == "Semaine":
        critiques_par_semaine = df[df['contains_keywords']].groupby('week').size().reset_index(name='tweets_critiques')
        fig_critiques = px.bar(critiques_par_semaine, x='week', y='tweets_critiques',
                                title='Nombre de Tweets Critiques par Semaine',
                                color_discrete_sequence=["#E377C2"])
    else:  # Mois
        critiques_par_mois = df[df['contains_keywords']].groupby('month').size().reset_index(name='tweets_critiques')
        fig_critiques = px.bar(critiques_par_mois, x='month', y='tweets_critiques',
                                title='Nombre de Tweets Critiques par Mois',
                                color_discrete_sequence=["#E377C2"])
    st.plotly_chart(fig_critiques, use_container_width=True)

# --- Nouveaux Graphiques de Catégories et Inconfort ---
col3, col4 = st.columns(2)

with col3:
    # Graphique: Fréquence des Catégories
    category_count = df['Catégorie'].value_counts().reset_index()
    category_count.columns = ['Catégorie', 'Nombre de Tweets']
    fig_category = px.bar(category_count, x='Catégorie', y='Nombre de Tweets',
                          title='Fréquence des Catégories',
                          color='Catégorie', color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig_category, use_container_width=True)

with col4:
    # Graphique: Inconfort Moyen par Catégorie
    inconfort_category_avg = df.groupby('Catégorie')['Inconfort'].mean().reset_index()
    inconfort_category_avg = inconfort_category_avg.sort_values('Inconfort', ascending=False)
    fig_inconfort = px.bar(inconfort_category_avg, x='Catégorie', y='Inconfort',
                           title='Inconfort Moyen par Catégorie',
                           color='Catégorie', color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig_inconfort, use_container_width=True)

# Afficher les données brutes (optionnel)
with st.expander("Afficher les Données Brutes"):
    st.dataframe(df)
