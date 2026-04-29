# 📊 Projet de Fin d’Année

## Automatisation des Ventes


## 👨‍🎓 Auteurs

* Islem Zaidi
* Islem Selmi
* Khadija Zitouni

🎓 Classe : LMI2 – Groupe 2


## 🎯 Objectif du projet

Ce projet a pour objectif de développer un script Python permettant d’automatiser l’analyse des ventes d’une entreprise e-commerce à partir d’un fichier CSV.

L’objectif principal est de remplacer l’utilisation d’Excel lorsque le volume de données devient important, en proposant une solution plus rapide, fiable et automatisée.


## ⚙️ Fonctionnalités principales

Le programme permet de :

* 📥 Lire un fichier CSV contenant les données de ventes
* 🧮 Calculer le chiffre d’affaires brut (CA Brut)
* 💸 Appliquer les remises pour obtenir le chiffre d’affaires net (CA Net)
* 🧾 Calculer la TVA (20%)
* 📊 Calculer le chiffre d’affaires total
* 🏆 Identifier le produit le plus rentable
* 💾 Exporter les résultats dans un nouveau fichier CSV
* 📈 Générer 5 visualisations graphiques :

Histogramme : CA Net par produit

Diagramme circulaire : parts de marché

Barres groupées : Brut vs Net

Nuage de points : remise vs quantité

Boîte à moustaches : distribution du CA Net



## 📁 Structure du fichier CSV

Le fichier CSV doit contenir les colonnes suivantes :

| Colonne  | Description               |
| -------- | ------------------------- |
| ID       | Identifiant du produit    |
| Prix     | Prix unitaire             |
| Quantite | Quantité vendue           |
| Remise   | Remise en pourcentage (%) |

### 📌 Exemple :

```csv
ID,Prix,Quantite,Remise
101,15,3,10
102,25,2,5
103,10,5,0
```


## 🧮 Détails des calculs

* **CA Brut** = Prix × Quantité
* **CA Net** = CA Brut × (1 - Remise / 100)
* **TVA** = CA Net × 0.2
* **CA Total** = Somme des CA Net


## ▶️ Instructions d’utilisation

### 1️⃣ Installer les dépendances

```bash
pip install pandas matplotlib
```


### 2️⃣ Lancer le programme

```bash
python pfa_ventes.py
```


### 3️⃣ Entrer le nom du fichier

Lorsque le programme démarre, entrer :

```
ventes.csv
```


## 📊 Résultats générés

Après exécution, le programme :

* Affiche le chiffre d’affaires total
* Affiche l’ID du produit le plus rentable
* Crée un fichier `resultats_final.csv` contenant :

  * Données initiales
  * CA Brut
  * CA Net
  * TVA
  * Affiche les 5 graphes 


## 🧠 Technologies utilisées

* **Python** : langage principal
* **Pandas** : manipulation et analyse des données
* **Matplotlib** : visualisation graphique
* **NumPy**: Calculs mathématiques et génération de données aléatoires.

## 🚀 Améliorations apportées (Version Pro)

* ✔️ Lecture dynamique de n’importe quel fichier CSV
* ✔️ Vérification de l’existence du fichier
* ✔️ Validation des colonnes obligatoires
* ✔️ Gestion des erreurs
* ✔️ Code structuré et réutilisable


## 🔮 Perspectives d’amélioration

* Interface graphique (GUI)
* Analyse statistique avancée
* Gestion de grandes bases de données
* Export vers Excel ou base de données


## 📌 Conclusion

Ce projet démontre l’intérêt de l’automatisation dans le traitement des données.
Grâce à Python, il est possible de remplacer efficacement des outils classiques comme Excel, tout en améliorant la rapidité, la précision et la flexibilité du traitement des données.


## 📅 Année universitaire

2025 – 2026
