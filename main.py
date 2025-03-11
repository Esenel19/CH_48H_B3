from src.data_loader import load_data, save_data
from src.data_cleaning import clean_data
from src.text_cleaning import clean_text
from src.sentiment_analysis import get_sentiment
from src.kpi_extraction import prepare_date_features, extract_kpi

# Chargement des données brutes
file_path = "data/filtered_tweets_engie.csv"
data = load_data(file_path)

# Nettoyage des données
data = clean_data(data)

# Nettoyage du texte et analyse de sentiment
data['full_text'] = data['full_text'].apply(clean_text)
data['sentiment'] = data['full_text'].apply(get_sentiment)

# Extraction des KPI et Ajout au CSV
data = prepare_date_features(data)
kpi_results = extract_kpi(data)

# Ajout des KPI directement dans le CSV nettoyé
data['text_length'] = data['full_text'].apply(len)
data['contains_keywords'] = data['full_text'].str.contains(
    r'\b(?:délai|panne|urgence|scandale|honteux)\b', case=False, na=False
)

#   Sauvegarde du fichier final prêt pour Power BI
output_path = "output/filtered_tweets_engie_final.csv"
save_data(data, output_path)

# Affichage des KPI
print(f" Données nettoyées et enregistrées dans : `{output_path}`")
print(f" Nombre total de tweets : {kpi_results['total_tweets']}")
print(f" Tweets par jour :\n{kpi_results['tweets_per_day']}")
print(f" Tweets par semaine :\n{kpi_results['tweets_per_week']}")
print(f" Tweets par mois :\n{kpi_results['tweets_per_month']}")
print(f" Répartition par heure :\n{kpi_results['tweets_per_hour']}")
print(f" Répartition par jour de la semaine :\n{kpi_results['tweets_per_day_of_week']}")
print(f" Nombre de tweets critiques : {kpi_results['critical_tweets']}")
print(f" Score d'inconfort : {kpi_results['discomfort_score']}%")
