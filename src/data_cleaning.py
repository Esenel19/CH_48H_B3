import pandas as pd


def clean_data(data):
    # Remplacement de la colonne 'id' par une séquence ordonnée
    data['id'] = range(1, len(data) + 1)

    # Conversion de la colonne 'created_at' en format datetime avec gestion UTC
    data['created_at'] = pd.to_datetime(data['created_at'], errors='coerce', utc=True)

    # Suppression de la colonne 'name'
    data.drop('name', axis=1, inplace=True)

    # Suppression des doublons dans la colonne 'full_text'
    data.drop_duplicates(subset='full_text', keep='first', inplace=True)

    return data