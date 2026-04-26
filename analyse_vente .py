import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Saisie des données de ventes ---
print("--- Saisie des données de ventes ---")
nb_produits = int(input("Combien de produits voulez-vous saisir ? "))

liste_donnees = []

for i in range(nb_produits):
    print(f"\nProduit n°{i+1}:")
    id_p = input("ID du produit : ")
    prix = float(input("Prix unitaire (TND) : "))
    quantite = int(input("Quantité : "))
    remise = float(input("Remise accordée (%) : "))
    
    # Ajout à la liste de données
    liste_donnees.append({
        'ID': id_p,
        'Prix': prix,
        'Quantite': quantite,
        'Remise': remise
    })

# Création du tableau (DataFrame) à partir de tes entrées
df = pd.DataFrame(liste_donnees)

# --- 2. Calculs des indicateurs financiers ---
# Calcul du Chiffre d'Affaires Brut (Prix unitaire * Quantité)
df["CA_Brut"] = df["Prix"] * df["Quantite"]

# Calcul du CA Net après application de la remise (Remise en %)
df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise"] / 100)

# Calcul de la TVA (fixée à 20% ici)
df["TVA"] = df["CA_Net"] * 0.2

# --- 3. Affichage des résultats & Export ---
print("\n" + "="*30)
print("TABLEAU RÉCAPITULATIF :")
print(df)
print("="*30)

# Somme totale du Chiffre d'Affaires Net
ca_total = df["CA_Net"].sum()
print(f"CA Total de l'entreprise : {ca_total:.2f} TND")

# Identification du produit ayant généré le plus de CA Net
max_produit = df.loc[df["CA_Net"].idxmax()]
print(f"Produit le plus rentable : ID {max_produit['ID']}")

# Exportation des résultats dans un fichier CSV
df.to_csv("resultats_final.csv", index=False)
print("\nFichier resultats_final.csv créé !")

# --- 4. Visualisation des données ---

# Graphique 1 : CA Net par produit
plt.figure(figsize=(8, 5))
plt.bar(df["ID"], df["CA_Net"])
plt.xlabel("ID Produit")
plt.ylabel("CA Net (TND)")
plt.title("Chiffre d'affaires par produit")
plt.show()

# Graphique 2 : Répartition du CA Net en pourcentage
plt.figure(figsize=(8, 6))  
plt.pie(df["CA_Net"], labels=df["ID"], autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title("Répartition du Chiffre d'Affaires par Produit (%)")
plt.axis('equal')  
plt.show()

# Graphique 3 : Comparaison CA Brut et CA Net
df.plot(x="ID", y=["CA_Brut", "CA_Net"], kind="bar", figsize=(10, 5), color=['skyblue', 'teal'])
plt.title("Comparaison du CA Brut et du CA Net après remises")
plt.xlabel("Identifiant du Produit")
plt.ylabel("Montant (TND)")
plt.xticks(rotation=0)  
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.legend(["CA Brut", "CA Net"])
plt.show()

# Graphique 4 : Analyse Remise vs Quantité vendue
plt.figure(figsize=(8, 5))
plt.scatter(df["Remise"], df["Quantite"], color='purple', s=100, alpha=0.7)
plt.title("Relation entre le taux de remise et les quantités vendues")
plt.xlabel("Taux de remise (%)")
plt.ylabel("Quantité vendue")
plt.grid(True, which='both', linestyle='--', alpha=0.5)

# Ajout d'annotations pour chaque point (ID du produit)
for i, txt in enumerate(df["ID"]):
    plt.annotate(txt, (df["Remise"][i], df["Quantite"][i]), xytext=(5,5), textcoords='offset points')

plt.show()

# Graphique 5 : Analyse de la distribution statistique (Boxplot)
plt.figure(figsize=(6, 4))
plt.boxplot(df["CA_Net"], patch_artist=True)
plt.title("Distribution Statistique du CA Net")
plt.ylabel("Valeurs (TND)")
plt.show()
