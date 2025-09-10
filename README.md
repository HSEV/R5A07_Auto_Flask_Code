# Mini-projet Flask + MySQL

Ce projet minimal crée une application Flask avec une seule route et une base MySQL initialisée via un script Python. La page affiche :
- "Votre page marche parfaitement vous avez reussi"
- Quelques données extraites de la base MySQL pour prouver la connexion.

## Structure
- `app.py` — Application Flask.
- `db_init.py` — Script d'initialisation (création BD, table, et insertion de données).
- `templates/index.html` — Modèle HTML pour l’affichage des données.
- `requirements.txt` — Dépendances Python.

## Prérequis
- Python 3.9+
- MySQL Server accessible (local ou distant)

## Configuration
Définissez les variables d’environnement MySQL avant de lancer les scripts :

- `MYSQL_HOST` (par défaut: `127.0.0.1`)
- `MYSQL_PORT` (par défaut: `3306`)
- `MYSQL_USER` (par défaut: `root`)
- `MYSQL_PASSWORD` (par défaut: vide)
- `MYSQL_DB` (par défaut: `demo_flask`)

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Initialiser la base

```bash
python db_init.py
```

## Lancer l’app

```bash
python app.py
```

Ensuite ouvrez http://127.0.0.1:5000/ dans votre navigateur.

## Dépannage
- Si la connexion MySQL échoue, vérifiez les identifiants et que le serveur tourne.
- Vous pouvez changer le nom de la BD via `MYSQL_DB` puis relancer `db_init.py`.
