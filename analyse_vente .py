import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1. GÉNÉRATION OU SAISIE DES DONNÉES ---
print("--- Système d'Analyse de Ventes (Scalable) ---")
mode = input("Voulez-vous (1) Saisir manuellement ou (2) Simuler X lignes ? ")

if mode == "1":
    nb_produits = int(input("Combien de produits ? "))
    liste_donnees = []
    for i in range(nb_produits):
        print(f"\nProduit n°{i+1}:")
        liste_donnees.append({
            'ID': input("ID : "),
            'Prix': float(input("Prix (TND) : ")),
            'Quantite': int(input("Quantité : ")),
            'Remise': float(input("Remise (%) : "))
        })
    df = pd.DataFrame(liste_donnees)
else:
    # Simulation pour 5000 lignes ou plus
    n = int(input("Combien de lignes voulez-vous générer (ex: 5000) ? "))
    data = {
        'ID': [f"P_{i}" for i in range(1, n + 1)],
        'Prix': np.random.uniform(10, 500, size=n).round(2),
        'Quantite': np.random.randint(1, 100, size=n),
        'Remise': np.random.choice([0, 5, 10, 15, 20], size=n)
    }
    df = pd.DataFrame(data)

# --- 2. CALCULS FINANCIERS (VECTEURS) ---
df["CA_Brut"] = df["Prix"] * df["Quantite"]
df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise"] / 100)
df["TVA"] = df["CA_Net"] * 0.20 # TVA 20%

# --- 3. PRÉPARATION DES DONNÉES POUR LES GRAPHES ---
# Si on a beaucoup de lignes, on prend le Top 10 pour la clarté
if len(df) > 15:
    df_top = df.nlargest(10, 'CA_Net')
    suffixe = "(Top 10)"
else:
    df_top = df
    suffixe = ""

# --- 4. TOUS LES GRAPHIQUES ---

# Graphe 1 : CA Net par produit (Barres)
plt.figure(figsize=(10, 5))
plt.bar(df_top["ID"], df_top["CA_Net"], color='skyblue')
plt.title(f"Chiffre d'Affaires Net par Produit {suffixe}")
plt.ylabel("TND")
plt.show()

# Graphe 2 : Répartition (%) (Pie Chart)
plt.figure(figsize=(8, 8))
plt.pie(df_top["CA_Net"], labels=df_top["ID"], autopct='%1.1f%%', startangle=140)
plt.title(f"Répartition du CA {suffixe}")
plt.show()

# Graphe 3 : Comparaison Brut vs Net
df_top.plot(x="ID", y=["CA_Brut", "CA_Net"], kind="bar", figsize=(10, 5))
plt.title(f"Impact des Remises {suffixe}")
plt.ylabel("TND")
plt.show()

# Graphe 4 : Relation Remise vs Quantité (Scatter Plot)
# Ici on peut afficher plus de points car c'est un nuage
sample_size = min(len(df), 500) 
df_sample = df.sample(n=sample_size)
plt.figure(figsize=(10, 6))
plt.scatter(df_sample["Remise"], df_sample["Quantite"], alpha=0.5, color='purple')
plt.title(f"Analyse de Corrélation (Échantillon de {sample_size} lignes)")
plt.xlabel("Remise (%)")
plt.ylabel("Quantité vendue")
plt.show()

# Graphe 5 : Distribution Statistique (Boxplot)
# Le boxplot est parfait pour 5000 lignes !
plt.figure(figsize=(7, 5))
plt.boxplot(df["CA_Net"], patch_artist=True, boxprops=dict(facecolor="lightgreen"))
plt.title(f"Dispersion Statistique du CA Net ({len(df)} lignes)")
plt.ylabel("TND")
plt.show()
