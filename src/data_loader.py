import pandas as pd

def load_data(file_path):
    #Charge les données.
    return pd.read_csv(file_path, sep=';', encoding='utf-8')

def save_data(data, output_path):
    #Sauvegarde les données nettoyées ou modifiées dans le dossier output.
    data.to_csv(output_path, sep=';', index=False, encoding='utf-8')
