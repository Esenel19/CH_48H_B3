import re

def clean_text(text):
#Nettoie le texte en supprimant les mentions, liens et caractères spéciaux.
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[^a-zA-Z0-9À-ÿ\s]', '', text)
    return text.strip().lower()
