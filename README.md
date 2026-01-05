# 📊 Dashboard Analytique — Dashaalia

**Projet EPSI • B3 DEV IA**
Atelier : *Coder avec l’IA Générative*

---

## 🚀 1. Présentation du projet

Ce projet consiste à développer un **dashboard analytique interactif** permettant de visualiser, analyser et interpréter les données issues des sessions d’interprétariat médical de **Dashaalia**, une plateforme d’interprétariat augmentée par Intelligence Artificielle.

L’application propose :

* une **analyse quantitative** des sessions,
* des **indicateurs métier (KPIs)** clairs,
* des **visualisations interactives**,
* des **filtres dynamiques globaux**,
* une page **“Insights IA”** générant automatiquement des analyses textuelles simulant une IA générative.

🎯 L’objectif pédagogique est de démontrer la capacité à :

* concevoir une application de **data analytics maintenable**,
* exploiter un dataset réel de bout en bout,
* intégrer l’IA générative comme **assistant de développement et d’analyse**.

⚙️ **Technologie utilisée :** Python • Streamlit • Plotly
📁 **Dataset :** `sessions_dataset_320.csv` (320 lignes)

---

## 📂 2. Arborescence du projet

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
│   ├── utils.py              # Calculs, KPIs & Insights IA
│
├── assets/
│   └── logo.png              # Logo Dashaalia (optionnel)
│
├── tests/
│   └── test_data.py          # Tests unitaires sur les données (bonus)
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🧠 3. Fonctionnalités principales

### 🎯 A. KPIs (Indicateurs clés)

Les indicateurs sont calculés dynamiquement selon les filtres appliqués :

* Nombre total de sessions
* Durée moyenne des sessions (minutes)
* Score moyen de qualité (0–1)
* Pourcentage de segments audio non reconnus
* Ratio interactions patient / praticien

---

### 📈 B. Visualisations interactives

Toutes les visualisations utilisent **Plotly**, offrant :

* zoom,
* survol (hover),
* export d’images.

| Visualisation                  | Description                               |
| ------------------------------ | ----------------------------------------- |
| Top des langues                | Classement des langues les plus utilisées |
| Évolution des sessions         | Série temporelle (jours / mois)           |
| Répartition par service        | Diagramme circulaire                      |
| Interactions patient/praticien | Scatter plot comparatif                   |
| Notes des praticiens           | Histogrammes et statistiques              |
| Segments non reconnus          | Analyse qualité & détection visuelle      |

---

### 🎚️ C. Filtres globaux

Les filtres s’appliquent **à l’ensemble de l’application** :

* Plage de dates
* Service médical
* Langue
* Type de device (webapp / mobile)

Ils mettent automatiquement à jour :

* KPIs
* graphiques
* tableau de données
* export CSV
* page **Insights IA**

---

### 🧠 D. Page “Insights IA” (Analyse automatique)

Une page dédiée **🧠 Insights IA** génère automatiquement des analyses textuelles à partir des données filtrées.

Exemples d’insights :

* langue la plus utilisée sur la période,
* service dominant,
* évolution des sessions (hausse / baisse),
* niveau de qualité global,
* alertes sur les segments non reconnus,
* équilibre des interactions patient / praticien.

📌 Ces insights sont produits via des **règles analytiques simulant un raisonnement d’IA générative**, illustrant l’usage de l’IA pour :

* interpréter des données,
* produire des conclusions lisibles métier,
* assister la prise de décision.

---

### 📄 E. Tableau & export

* Tableau interactif des données filtrées
* Tri et inspection des lignes
* Export CSV du dataset filtré

---

## 🧩 4. Fonctionnement des modules

### 🔹 `app.py`

* Point d’entrée Streamlit
* Gestion de la navigation (Dashboard / Insights IA)
* Application globale des filtres
* Affichage KPIs, graphiques, tableaux

### 🔹 `data_loader.py`

* Chargement CSV avec cache Streamlit
* Nettoyage des types et dates
* Création de colonnes dérivées :

  * `year`, `month`
  * `ratio_interactions`

### 🔹 `charts.py`

* Centralise toutes les visualisations Plotly
* Garantit une logique claire et réutilisable

### 🔹 `filters.py`

* Définit les filtres Streamlit
* Applique les conditions au dataframe
* Retourne le dataframe filtré unique (`dff`)

### 🔹 `utils.py`

* Calcul des KPIs
* Fonctions d’agrégation
* Génération des **Insights IA automatiques**

### 🔹 `tests/test_data.py`

* Tests unitaires (bonus) :

  * chargement du dataset
  * cohérence des colonnes
  * types de données
  * validité des dates

---

## 🛠️ 5. Installation & exécution

### ✔️ Prérequis

* Python 3.9+
* pip
* Streamlit

### ✔️ Installation

```bash
git clone https://github.com/.../dashboard-analytics.git
cd dashboard-analytics
pip install -r requirements.txt
```

### ▶️ Lancement

```bash
python -m streamlit run src/app.py
```

📍 Application accessible sur :
👉 [http://localhost:8501](http://localhost:8501)

---

## 🧪 6. Dataset utilisé

| Colonne                | Description                 |
| ---------------------- | --------------------------- |
| session_id             | Identifiant unique          |
| date                   | Date de la session          |
| service                | Service médical             |
| langue                 | Langue parlée               |
| duree_minutes          | Durée totale                |
| interactions_patient   | Interactions patient        |
| interactions_praticien | Interactions praticien      |
| interactions_totales   | Total interactions          |
| note_praticien         | Note (0–5)                  |
| qualite_score          | Score (0–1)                 |
| segments_non_reconnus  | Segments audio non reconnus |
| device                 | webapp / mobile             |

---

## 🤖 7. Utilisation de l’IA Générative (élément clé du barème)

L’IA générative a été utilisée pour :

* concevoir l’architecture modulaire du projet
* générer et améliorer le code Python
* proposer les visualisations pertinentes
* corriger les erreurs (debug assisté)
* générer automatiquement les **Insights IA**
* rédiger la documentation et les tests unitaires

📸 Des **captures d’écran des échanges avec l’IA** doivent être intégrées dans le rapport (exigence du barème).

---

## ⭐ 8. Améliorations possibles

* Détection automatique d’anomalies
* Comparaison période N / N-1
* Alertes qualité
* Analyse prédictive
* Intégration future d’un vrai LLM (API)

---

## 📚 9. Auteurs

Projet réalisé dans le cadre du module
**« Coder avec l’IA Générative » — EPSI B3 DEV IA**

👥 Équipe :

* **Mansour Djamil NDIAYE**
* **Arsene Arayi Mbengue**
* **Mamadou Seck**

👩‍🏫 Encadré par :

* **Ghalloussi Samah**
