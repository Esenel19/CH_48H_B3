import pandas as pd

def prepare_date_features(data):
    #Ajoute les colonnes 'date', 'hour' et 'day_of_week' à partir de 'created_at'.
    data['created_at'] = pd.to_datetime(data['created_at'], errors='coerce', utc=True)
    data['date'] = data['created_at'].dt.date
    data['hour'] = data['created_at'].dt.hour
    data['day_of_week'] = data['created_at'].dt.day_name()
    return data

def extract_kpi(data):
    #Extrait les principaux KPI à partir des données.
    total_tweets = len(data)
    tweets_per_day = data['date'].value_counts().sort_index()
    tweets_per_week = data['created_at'].dt.to_period('W').value_counts().sort_index()
    tweets_per_month = data['created_at'].dt.to_period('M').value_counts().sort_index()

    tweets_per_hour = data['hour'].value_counts().sort_index()
    tweets_per_day_of_week = data['day_of_week'].value_counts()

    critical_tweets = data['full_text'].str.contains(r'\b(?:délai|panne|urgence|scandale)\b',
                                                      case=False, na=False).sum()

    discomfort_score = round((critical_tweets / total_tweets) * 100, 2)

    return {
        "total_tweets": total_tweets,
        "tweets_per_day": tweets_per_day,
        "tweets_per_week": tweets_per_week,
        "tweets_per_month": tweets_per_month,
        "tweets_per_hour": tweets_per_hour,
        "tweets_per_day_of_week": tweets_per_day_of_week,
        "critical_tweets": critical_tweets,
        "discomfort_score": discomfort_score
    }
