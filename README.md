# Web Scraping des matchs - Yallakora

Ce projet est un script Python qui récupère les résultats de matchs de football depuis le site [Yallakora](https://www.yallakora.com) à une date donnée.  
Les données extraites (en arabe) sont sauvegardées dans un fichier **CSV** (compatible Excel) avec encodage **UTF-8**.

---

## Fonctionnalités
- Scraping automatique des championnats et matchs du jour.
- Extraction des informations :
  - 🏆 Titre du championnat  
  - ⚽ Équipe A  
  - ⚽ Équipe B  
  - ⏱ Temps du match  
  - 🔢 Score final  
- Sauvegarde des données dans un fichier `matches.csv`.

---

## 📦 Prérequis
Avant de lancer le script, assure-toi d’avoir installé **Python 3.8+**.  
Puis installe les dépendances nécessaires :

```bash
pip install requests beautifulsoup4 lxml
