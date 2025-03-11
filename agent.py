import json
from dotenv import load_dotenv
import os
from mistralai import Mistral
import pandas as pd
import time

# Charger les variables d'environnement
load_dotenv('.env')
api_key = os.getenv('MY_API')
agent_id = os.getenv('AGENT_ID')

# Charger le fichier CSV
data = pd.read_csv('csv_modifie.csv')

# Initialiser le client Mistral
client = Mistral(api_key=api_key)

# Définir la taille des lots
batch_size = 1  
total_batches = len(data) // batch_size + (1 if len(data) % batch_size > 0 else 0)  # Nombre total de lots

# Fichier JSON où stocker les résultats
output_file = "responses.json"

# Vérifier si le fichier existe déjà et charger les données existantes
if os.path.exists(output_file):
    with open(output_file, "r", encoding="utf-8") as f:
        try:
            all_responses = json.load(f)
        except json.JSONDecodeError:
            all_responses = []
else:
    all_responses = []

# Compteur pour le timeout
request_count = 0  

# Traitement par lots
for batch_num, i in enumerate(range(0, len(data), batch_size), start=1):
    batch = data.iloc[i:i+batch_size]  # Extraire 1 ligne
    csv_content = batch.to_csv(index=False)  # Convertir en CSV sans index

    # Affichage de l'avancement
    print(f"\n🚀 Envoi du lot {batch_num}/{total_batches}...")

    # Envoyer à l'agent Mistral
    chat_response = client.agents.complete(
        agent_id=agent_id,
        messages=[
            {
                "role": "user",
                "content": f"Voici un lot de données CSV :\n\n{csv_content}"
            },
        ]
    )

    # Récupérer la réponse
    response_content = chat_response.choices[0].message.content

    try:
        # Désérialiser la réponse en JSON
        response_json = json.loads(response_content)
    except json.JSONDecodeError:
        print(f"⚠️ Erreur : la réponse du lot {batch_num} n'est pas un JSON valide.")
        continue  # Passer au lot suivant

    # Ajouter un ID unique
    response_json["id"] = batch_num  

    # Ajouter la réponse avec ID
    all_responses.append(response_json)

    # Sauvegarde progressive dans un fichier JSON
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_responses, f, ensure_ascii=False, indent=4)

    # Affichage immédiat du résultat du lot
    print(f"✅ Réponse du lot {batch_num} enregistrée dans {output_file}")

    # Incrémenter le compteur de requêtes
    request_count += 1  

    # Timeout de 3 secondes toutes les 15 requêtes
    if request_count % 1 == 0:
        print("\n⏳ Pause de 3 secondes pour éviter la surcharge de l'API...")
        time.sleep(5)
    
    # Pause normale de 1 seconde entre chaque requête
    time.sleep(1)
