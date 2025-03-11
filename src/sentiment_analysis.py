from textblob import TextBlob

# Liste personnalisée de mots négatifs fréquents dans les plaintes
negative_keywords = ['inadmissible', 'honteux', 'scandale', 'délai', 'panne', 'urgence', 'incompétent', 'arnaque', 'chère', 'abusé', 'mauvais', 'froid', 'problème', 'déçu','terrible', 'danger', 'dangereux', 'escroc', 'plainte']

def get_sentiment(text):
    analysis = TextBlob(text)
    if any(word in text.lower() for word in negative_keywords):
        return 'Négatif'
    elif analysis.sentiment.polarity > 0:
        return 'Positif'
    elif analysis.sentiment.polarity < 0:
        return 'Négatif'
    else:
        return 'Neutre'
