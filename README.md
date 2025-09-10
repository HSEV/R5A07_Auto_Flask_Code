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

## Lancer en Docker (recommandé)

Prérequis: Docker Desktop (macOS/Windows) ou Docker Engine (Linux).

```bash
# Construire et démarrer l’app + MySQL
docker compose up -d --build

# Ouvrir l’app
open http://127.0.0.1:5000  # macOS
# ou: xdg-open http://127.0.0.1:5000 # Linux
```

Le service `web` attend que MySQL soit healthy, initialise la base (script `db_init.py`), puis lance Flask sur `0.0.0.0:5000`.

## CI/CD: Build & Push sur Docker Hub

Un workflow GitHub Actions (`.github/workflows/docker-image.yml`) build et push l’image à chaque push sur `main`.
Configurez deux secrets dans GitHub repo → Settings → Secrets and variables → Actions:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN` (un Access Token Docker Hub)

Par défaut, l’image est poussée en `DOCKERHUB_USERNAME/r5a07_auto_flask:latest`.

## Déploiement sur une VM Linux (ex: Kali)

```bash
# 1) Installer Docker Engine si nécessaire
# 2) Récupérer l’image (si déjà poussée)
docker pull DOCKERHUB_USERNAME/r5a07_auto_flask:latest

# 3) Lancer MySQL + Web via docker compose
docker compose up -d

# 4) Accéder à http://<IP_VM>:5000
```

Si vous ne souhaitez pas builder localement, vous pouvez référencer dans `docker-compose.yml` directement l’image du Hub au lieu de `build: .`.

## Dépannage
- Si la connexion MySQL échoue, vérifiez les identifiants et que le serveur tourne.
- Vous pouvez changer le nom de la BD via `MYSQL_DB` puis relancer `db_init.py`.
