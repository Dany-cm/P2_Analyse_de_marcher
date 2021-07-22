# Projet python pour l'analyse de marché

Script en python permettant de récupérer des informations sur les livres depuis le site [book toscrape](http://books.toscrape.com/).

Les informations récupérer sont les suivantes :  

- product_page_url = L'url du livre
- universal_product_code = le code UPC
- title = le titre
- price_including_tax = le prix avec la taxe
- price_excluding_tax = le prix sans taxe
- number_available = le nombre de livre disponible
- product_description = la description du livre
- category = la catégorie du livre
- review_rating = la note du livre(avis)
- image_url = l'url de la couverture du livre

Le script permet de sauvegarder les informations des livres dans un fichier csv, il récupère également toutes les catégories et range les livres dans leur propre catégorie. Toutes les images sont des livres sont sauvegarder dans le dossier "images"

## Installation

Installer [Python](https://www.python.org/ftp/python/3.9.6/python-3.9.6-amd64.exe) et suivez les instructions.


Utilisez [pip](https://pip.pypa.io/en/stable/) pour installer les paquets nécessaires.

```bash
pip install -r requirements.txt
```

## Usage

```python
# Crée un environement virtuel
python -m venv venv

# Active l'environement virtuel
venv\Scripts\activate

# Installe les paquets nécessaire
pip install -r requirements.txt

# Lance le programme
python main.py
```


## Auteur
[Danycm1](https://github.com/Danycm1)
