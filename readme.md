Regen Finder FC25 🕵️‍♂️

Un outil simple avec une interface graphique pour retrouver les joueurs originaux de vos "regens" dans le mode Carrière de FC 25.

(Pensez à remplacer cette image par une vraie capture d'écran de votre application !)

Fonctionnalités ✨

    Recherche inversée : Entrez les informations d'un jeune joueur (nationalité, poste, date de naissance) pour découvrir de quelle star retraitée il est la réincarnation.

    Interface graphique simple : Plus besoin de terminal, tout se fait via des champs de saisie et des boutons.

    Tri des résultats : Les joueurs originaux potentiels sont triés par note générale pour identifier rapidement le plus célèbre.

🚀 Installation et Utilisation

Vous avez deux options pour utiliser cet outil.

Option 1 : Utiliser l'application directement (.exe)

C'est la méthode la plus simple, recommandée pour la plupart des utilisateurs.

    Rendez-vous dans la section Releases de ce dépôt.

    Téléchargez le dernier fichier .zip (par exemple, RegenFinder.v1.0.zip).

    Décompressez le fichier où vous le souhaitez.

    Important : Placez votre fichier de données players.csv dans le même dossier que RegenApp_GUI.exe.

    Double-cliquez sur RegenApp_GUI.exe pour lancer l'application.

Option 2 : Lancer depuis le code source

Si vous êtes un développeur ou si vous préférez ne pas utiliser l'exécutable.

    Clonez ou téléchargez ce dépôt.
    Bash

git clone https://github.com/VOTRE_NOM_UTILISATEUR/VOTRE_DEPOT.git

Installez les dépendances nécessaires.
Bash

pip install -r requirements.txt

Placez votre fichier players.csv à la racine du projet.

Lancez l'application.
Bash

    python RegenApp_GUI.py

⚠️ Avertissement Antivirus

L'exécutable (.exe) fourni dans les "Releases" est créé avec l'outil PyInstaller. Certains antivirus (y compris Windows Defender) peuvent le détecter comme une menace.

Ceci est un faux positif. Cela est dû à la manière dont PyInstaller empaquète le code Python en un seul fichier. Le code de ce projet est 100% open-source, vous pouvez l'inspecter vous-même pour vérifier qu'il est totalement inoffensif.

📄 Fichier de Données

Pour fonctionner, l'application a besoin d'un fichier players.csv contenant la base de données des joueurs. Ce fichier n'est pas inclus dans ce dépôt et doit être obtenu séparément.

🛠️ Technologies Utilisées

    Python

    CustomTkinter pour l'interface graphique.# Regen Finder FC25 🕵️‍♂️

Un outil simple avec une interface graphique pour retrouver les joueurs originaux de vos "regens" dans le mode Carrière de FC 25.

![Aperçu de l'application]((https://media.discordapp.net/attachments/1046165968952492222/1394126906583945216/image.png?ex=6875ad5c&is=68745bdc&hm=804ae578bb6cc1d97b7a943643c764e04c86cd12dfda3fc2e8071b9453a10437&=&format=webp&quality=lossless)


---

## Fonctionnalités ✨

- **Recherche inversée** : Entrez les informations d'un jeune joueur (nationalité, poste, date de naissance) pour découvrir de quelle star retraitée il est la réincarnation.
- **Interface graphique simple** : Plus besoin de terminal, tout se fait via des champs de saisie et des boutons.
- **Tri des résultats** : Les joueurs originaux potentiels sont triés par note générale pour identifier rapidement le plus célèbre.

---

## 🚀 Installation et Utilisation

Vous avez deux options pour utiliser cet outil.

### Option 1 : Utiliser l'application directement (.exe)

C'est la méthode la plus simple, recommandée pour la plupart des utilisateurs.

1.  Rendez-vous dans la section **[Releases](https://github.com/VOTRE_NOM_UTILISATEUR/VOTRE_DEPOT/releases)** de ce dépôt.
2.  Téléchargez le dernier fichier `.zip` (par exemple, `RegenFinder.v1.0.zip`).
3.  Décompressez le fichier où vous le souhaitez.
4.  **Important :** Placez votre fichier de données `players.csv` dans le même dossier que `RegenApp_GUI.exe`.
5.  Double-cliquez sur `RegenApp_GUI.exe` pour lancer l'application.

### Option 2 : Lancer depuis le code source

Si vous êtes un développeur ou si vous préférez ne pas utiliser l'exécutable.

1.  Clonez ou téléchargez ce dépôt.
    ```bash
    git clone [https://github.com/VOTRE_NOM_UTILISATEUR/VOTRE_DEPOT.git](https://github.com/VOTRE_NOM_UTILISATEUR/VOTRE_DEPOT.git)
    ```
2.  Installez les dépendances nécessaires.
    ```bash
    pip install -r requirements.txt
    ```
3.  Placez votre fichier `players.csv` à la racine du projet.
4.  Lancez l'application.
    ```bash
    python RegenApp_GUI.py
    ```

---

## ⚠️ Avertissement Antivirus

L'exécutable (`.exe`) fourni dans les "Releases" est créé avec l'outil **PyInstaller**. Certains antivirus (y compris Windows Defender) peuvent le détecter comme une menace.

**Ceci est un faux positif.** Cela est dû à la manière dont PyInstaller empaquète le code Python en un seul fichier. Le code de ce projet est 100% open-source, vous pouvez l'inspecter vous-même pour vérifier qu'il est totalement inoffensif.

---

## 📄 Fichier de Données

Pour fonctionner, l'application a besoin d'un fichier `players.csv` contenant la base de données des joueurs. Ce fichier n'est pas inclus dans ce dépôt et doit être obtenu séparément.

---

## 🛠️ Technologies Utilisées

- **Python**
- **CustomTkinter** pour l'interface graphique.
