import pandas as pd
import json

# Fichiers
csv_file = "Data/filtered_tweets_engie_final_with_id.csv"  # Fichier CSV existant
json_file = "responses.json"  # Fichier JSON contenant les informations supplémentaires
output_file = "Data/filtered_tweets_engie_final_fusion_json_csv.csv"  # Fichier de sortie

# 📂 Fichiers

# 📌 Charger le CSV
df_csv = pd.read_csv(csv_file, sep=';')

# 📌 Charger le JSON
with open(json_file, "r", encoding="utf-8") as f:
    json_data = json.load(f)

df_json = pd.DataFrame(json_data)

# 🔹 Vérifier que 'id' existe bien
if "id" not in df_json.columns:
    print("❌ Erreur : La colonne 'id' n'existe pas dans le JSON")
    print("Colonnes disponibles :", df_json.columns)
    exit()

# 🛠️ Convertir `id` en entier dans les deux DataFrames pour éviter les problèmes de type
df_csv["json_id"] = pd.to_numeric(df_csv["json_id"], errors="coerce").astype("Int64")
df_json["id"] = pd.to_numeric(df_json["id"], errors="coerce").astype("Int64")

# 🔄 Fusionner sur `json_id` <-> `id`
df_fusion = df_csv.merge(df_json[['id', 'Inconfort', 'Catégorie']], 
                         left_on="json_id", right_on="id", 
                         how="left")

# 🚨 Supprimer la colonne `id_x` et `id_y` après fusion
df_fusion.drop(columns=["id", "id_y"], inplace=True)

# 💾 Sauvegarder le nouveau CSV enrichi
df_fusion.to_csv(output_file, sep=';', index=False, encoding="utf-8")

print(f"✅ Nouveau fichier CSV enregistré : {output_file}")
