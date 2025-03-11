
import pandas as pd
import json

# Charger le fichier CSV
csv_file_path = "output/filtered_tweets_engie_final copy.csv"
df = pd.read_csv(csv_file_path, sep=";")

# Charger le fichier JSON
json_file_path = "responses.json"
with open(json_file_path, 'r', encoding='utf-8') as f:
    json_data = json.load(f)

# Convertir le JSON en DataFrame
json_df = pd.DataFrame(json_data)

# Fusionner les DataFrames sur la colonne 'id'
merged_df = pd.merge(df, json_df[['id', 'Inconfort', 'Catégorie']], on='id', how='left')

# Sauvegarder le fichier final avec les nouvelles colonnes
output_path = "filtered_tweets_engie_final_with_inconfort.csv"
merged_df.to_csv(output_path, sep=';', index=False)

# Affichage pour confirmation
print(f"Données fusionnées et enregistrées dans : `{output_path}`")
