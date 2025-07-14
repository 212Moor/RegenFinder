import csv
import os
import platform

FICHIER_CSV = 'players.csv'

def nettoyer_ecran():
    """Efface le terminal pour un affichage plus propre."""
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def afficher_logo():
    """Affiche un en-tête pour l'outil."""
    print("=" * 70)
    print("      QUI EST LE REGEN ? - Recherche de Joueur Original".center(70))
    print("=" * 70)
    print("\nEntrez les caractéristiques de votre jeune regen pour trouver qui il était.\n")

def trouver_joueur_original(nationalite, poste, jour, mois, fichier_csv):
    """
    Recherche le joueur âgé et célèbre qui correspond au profil d'un regen.
    """
    joueurs_originaux_trouves = []
    
    try:
        with open(fichier_csv, 'r', encoding='utf-8') as csvfile:
            lecteur_csv = csv.DictReader(csvfile)
            for ligne in lecteur_csv:
                if 'age' in ligne and ligne['age'] and int(ligne['age']) < 33:
                    continue 
                conditions = []
                if nationalite:
                    conditions.append(ligne['nationality_name'].lower() == nationalite.lower())
                if poste:
                    conditions.append(all(p.strip().upper() in ligne['preferred_position'].upper() for p in poste.split(',')))
                if jour and mois:
                    if 'birthdate' in ligne and ligne['birthdate']:
                        try:
                            jour_naissance = int(ligne['birthdate'].split('-')[2])
                            mois_naissance = int(ligne['birthdate'].split('-')[1])
                            conditions.append(jour_naissance == jour and mois_naissance == mois)
                        except (ValueError, IndexError):
                            continue
                
                if all(conditions):
                    joueurs_originaux_trouves.append(ligne)

    except FileNotFoundError:
        print(f"ERREUR : Le fichier est introuvable. Vérifiez le chemin dans FICHIER_CSV.")
        return None
    except KeyError as e:
        print(f"ERREUR : Colonne manquante dans le CSV : {e}.")
        return None

    return joueurs_originaux_trouves

def main():
    """Fonction principale de l'outil."""
    while True:
        nettoyer_ecran()
        afficher_logo()

        print("--- Entrez le profil du jeune regen que vous avez trouvé ---")
        nationalite = input("Sa Nationalité : ")
        poste = input("Son ou ses Poste(s) (ex: ST, CF) : ")
        jour_input = input("Son Jour de naissance (1-31) : ")
        mois_input = input("Son Mois de naissance (1-12) : ")
        
        jour = int(jour_input) if jour_input.isdigit() else None
        mois = int(mois_input) if mois_input.isdigit() else None
        
        resultat = trouver_joueur_original(nationalite, poste, jour, mois, FICHIER_CSV)

        print("\n" + "-" * 70)
        if resultat is None:
            break
        elif resultat:
            print(f"✅ Votre regen est probablement la réincarnation de l'un de ces joueurs :\n")
            resultat.sort(key=lambda x: int(x['overall']), reverse=True)
            for joueur in resultat:
                print(f"  - {joueur.get('first_name', '')} {joueur.get('last_name', '')}")
                print(f"    Date de naissance: {joueur.get('birthdate', 'N/A')}")
                print(f"    Note: {joueur['overall']} | Potentiel: {joueur['potential']}")
                print(f"    Club: {joueur['owner_team']} | Poste(s): {joueur['preferred_position']}\n")
        else:
            print("❌ Aucun joueur original trouvé pour ce profil.")
        
        print("-" * 70)
        
        recherche_suivante = input("Appuyez sur Entrée pour une nouvelle recherche, ou tapez 'q' pour quitter : ")
        if recherche_suivante.lower() == 'q':
            break

if __name__ == "__main__":
    main()
