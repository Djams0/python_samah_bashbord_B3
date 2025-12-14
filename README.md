# **README.md**

# 📊 Dashboard Analytique — Dashaalia

Projet EPSI • B3 DEV IA
Atelier : *Coder avec l’IA Générative*

---

## 🚀 **1. Présentation du projet**

Ce projet consiste à développer un **dashboard analytique complet** permettant de visualiser, analyser et explorer les données des sessions d’interprétariat médical de **Dashaalia**, une plateforme enrichie par Intelligence Artificielle.

Le tableau de bord permet :

* d’explorer les comportements des utilisateurs,
* d’analyser les performances par service médical,
* de suivre l’évolution du nombre de sessions,
* de mesurer la qualité des interactions et de la reconnaissance vocale,
* d’obtenir des KPIs métier essentiels.

⚙️ **Technologie utilisée :** Python + Streamlit
📁 **Dataset :** `sessions_dataset_320.csv` (320 lignes)

---

## 📂 **2. Arborescence du projet**

```
dashboard-analytics/
│
├── data/
│   └── sessions_dataset_320.csv
│
├── src/
│   ├── app.py                # Application principale Streamlit
│   ├── data_loader.py        # Chargement & nettoyage du dataset
│   ├── charts.py             # Fonctions de visualisation Plotly
│   ├── filters.py            # Gestion des filtres Streamlit
│   ├── utils.py              # Calculs & KPIs
│
├── assets/
│   └── logo.png              # Logo Dashaalia (optionnel)
│
├── tests/
│   └── test_data.py          # Tests unitaires (bonus)
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🧠 **3. Fonctionnalités principales**

### 🎯 **A. KPIs (indicateurs clés)**

* Total de sessions
* Durée moyenne des sessions
* Score moyen de qualité (0–1)
* % de segments non reconnus
* Ratio interactions patient / praticien

---

### 📈 **B. Visualisations interactives**

Toutes les visualisations utilisent **Plotly** (zoom, hover, export PNG).

| Visualisation                         | Description                               |
| ------------------------------------- | ----------------------------------------- |
| **Top des langues**                   | Classement des langues les plus utilisées |
| **Évolution du nombre de sessions**   | Série temporelle journalière/mensuelle    |
| **Répartition par service**           | Pie chart des services médicaux           |
| **Analyse des interactions**          | Scatter patient vs praticien              |
| **Distribution des notes praticiens** | Histogrammes & statistiques               |
| **Segments non reconnus**             | Analyse qualité audio & anomalies         |

---

### 🎚️ **C. Filtres disponibles**

Les filtres appliquent un sous-ensemble dynamique sur l’intégralité du dashboard :

* Plage de dates
* Service médical
* Langue
* Type de device (webapp / mobile)

Les filtres mettent automatiquement à jour :

* tous les graphiques
* tous les KPIs
* le tableau final
* l’export CSV filtré

---

### 📤 **D. Export**

* Export CSV des sessions filtrées
* Téléchargement direct

---

### 📄 **E. Tableau des données**

Un tableau filtrable et triable affichant un échantillon ou l’ensemble du dataset filtré.

---

## 🧩 **4. Fonctionnement des modules**

### 🔹 **`app.py`**

Fichier principal :

* gère la structure de la page
* charge les modules
* contient la logique Streamlit (sidebar, mise en page, KPIs)
* appelle les fonctions de `charts.py`, `filters.py`, `utils.py`

### 🔹 **`data_loader.py`**

* Chargement CSV avec pandas
* Nettoyage des données (dates, types, valeurs manquantes)
* Ajout de colonnes : `year`, `month`, `ratio_interactions`, etc.
* Exposé via une fonction `load_data()` avec cache Streamlit

### 🔹 **`charts.py`**

Contient **toutes** les visualisations :

* bar chart top langues
* time series sessions
* pie des services
* scatter interactions
* histogramme notes
* boxplots / KPIs avancés

### 🔹 **`filters.py`**

* Définit tous les filtres Streamlit (date, langue, service...)
* Applique les filtres au dataframe
* Retourne un dataframe filtré (`dff`)

### 🔹 **`utils.py`**

* KPI calculs (durée moyenne, qualité, ratios)
* Fonctions pour conversions / nettoyage
* Fonctions d’agrégation (groupby dates, services, langues)

### 🔹 **`tests/test_data.py`**

Tests unitaires (bonus) :

* validité du chargement
* absence de colonnes manquantes
* typage cohérent
* dates valides converties

---

## 🛠️ **5. Installation & exécution**

### ✔️ **Prérequis**

* Python 3.9+
* pip
* Streamlit installé

### ✔️ **Installation**

```bash
git clone https://github.com/.../dashboard-analytics.git
cd dashboard-analytics
pip install -r requirements.txt
```

---

### ▶️ **Lancement du dashboard**

```bash
streamlit run src/app.py
```

Le dashboard sera disponible sur :
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 🧪 **6. Dataset utilisé**

Le fichier **sessions_dataset_320.csv** contient les colonnes suivantes :

| Colonne                | Description                |
| ---------------------- | -------------------------- |
| session_id             | Identifiant unique         |
| date                   | Date de la session         |
| service                | Service médical            |
| langue                 | Langue parlée              |
| duree_minutes          | Durée totale               |
| interactions_patient   | Nb interactions du patient |
| interactions_praticien | Nb interactions praticien  |
| interactions_totales   | Total interactions         |
| note_praticien         | Note (0–5)                 |
| qualite_score          | Score (0–1)                |
| segments_non_reconnus  | Segments mal reconnus      |
| device                 | webapp / mobile            |

---

## 🧠 **7. Utilisation de l’IA Générative (à mettre dans votre rapport)**

L’IA a été utilisée pour :

* générer une partie du code (visualisations, nettoyage de données)
* proposer une architecture modulaire
* créer le README
* expliquer les choix de visualisation
* rédiger automatiquement des tests
* proposer des améliorations avancées (detector anomalies, comparateur hebdo)

Ces captures d’écran doivent être ajoutées dans le rapport (obligatoire dans le barème).

---

## 📦 **8. Déploiement (optionnel mais conseillé)**

### 🚀 **Déploiement Streamlit Cloud**

1. Pousser votre repo sur GitHub
2. Aller sur : [https://share.streamlit.io](https://share.streamlit.io)
3. Sélectionner le repo
4. Point d’entrée : `src/app.py`
5. Déploiement auto

### 🌐 Autres options

* Render.com
* HuggingFace Spaces
* Docker + serveur nginx

---

## ⭐ **9. Améliorations possibles**

* Détection des anomalies (sessions très longues)
* Analyse cross-service (corrélations)
* Heatmap heure/jour si timestamps disponibles
* Système d’alertes qualité
* NLP sur les notes/commentaires (si fournis plus tard) 

---

## 📚 **10. Auteurs**

Projet réalisé dans le cadre du module **"Coder avec l’IA Générative" — EPSI B3 DEV IA**, par :

* *[Noms des membres du groupe]*

Encadré par :

* *[Nom du professeur]*
