# CHALL 48H IA - Analyse des Tweets Engie

## 🚀 Objectif du Projet
L'objectif de ce projet est d'analyser des tweets concernant Engie afin d'extraire des indicateurs clés de performance (KPIs), d'évaluer les sentiments exprimés et de visualiser les résultats à l'aide d'un tableau de bord interactif.

---

## 🗂️ Structure du Projet

```
📂 CHALL 48H IA
├── 📂 Data                    # Données brutes et nettoyées
│   ├── filtered_tweets_engie.csv
│   └── filtered_tweets_engie_cleaned.csv
├── 📂 output                  # Données finales avec KPIs et sentiments
│   └── filtered_tweets_engie_final.csv
├── 📂 src                     # Scripts principaux
│   ├── data_cleaning.py       # Nettoyage des données
│   ├── data_loader.py         # Chargement des données
│   ├── kpi_extraction.py      # Calcul des KPIs
│   ├── sentiment_analysis.py  # Analyse de sentiments
│   ├── text_cleaning.py       # Nettoyage du texte
│   └── app.py                 # Tableau de bord interactif (Streamlit)
├── .gitignore
├── requirements.txt           # Dépendances Python nécessaires
└── README.md                  # Guide du projet
```

---

## 🔧 Installation

1. **Cloner le dépôt**
```bash
git clone <url_du_repositoire>
cd CHALL-48H-IA
```

2. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

3. **Lancer l'application Streamlit**
```
    1. Aller sur https://streamlit.io/
    2. Se créer un compte et le lier à son github
    3. Créer une nouvelle app
    4. Ajouter ce repo git
    5. Sélectionner le fichier app.py
```

## 📊 Fonctionnalités

### 🧹 **Nettoyage des données**
✅ Suppression des doublons  
✅ Conversion des dates et identifiants au bon format  
✅ Extraction d'informations utiles (heure, longueur du texte, mots-clés critiques)  

### 📈 **Calcul des KPIs**
✅ Nombre de tweets par jour/semaine/mois  
✅ Fréquence des mentions du compte Engie  
✅ Détection des tweets critiques avec mots-clés spécifiques  

### 😊 **Analyse de Sentiments**
✅ Classification des tweets en Positif, Neutre ou Négatif  
✅ Affichage des proportions dans les KPIs  

### 🤖 **Agent IA pour la catégorisation des plaintes** *(À implémenter)*
❗ Détection automatique des types de réclamations (facturation, urgences, service client, etc.)  
❗ Utilisation potentielle de modèles comme **Mistral** ou **Gemini**  
❗ Génération de réponses automatiques basées sur les patterns identifiés (Bonus)  

### 📋 **Tableau de bord interactif (Streamlit)**
✅ Visualisation dynamique des KPIs  
✅ Filtres avancés (plage de dates, granularité temporelle)  
✅ Affichage des données brutes pour une meilleure transparence  

## 🚨 Fonctionnalités à Améliorer / à Implémenter

❗ Implémentation d'un modèle IA (Mistral/Gemini) pour détecter les types de réclamations  
❗ Automatisation des réponses basées sur les patterns détectés  

## 🛠️ Dépendances Principales
- **Python 3.8** (ou version supérieure)  
- **Pandas** (pour le traitement des données)  
- **Plotly** (pour la visualisation des données)  
- **Streamlit** (pour l'interface utilisateur)  
- **TextBlob** (pour l'analyse des sentiments)  

## 👥 Équipe du Projet
- HOUBLOP Alexy  
- FRANCISCO Kenett  
- SENEL Elodie  
- AYITE Ekué Etienne  
- DE CARVALHO Hugo  
- ALCARAZ Hugo  

"# CH_48H_B3" 
"# CH_48H_B3" 
