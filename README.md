# Mini-projet Flask + MySQL

## Objectif du projet (hébergé via Docker sur Linux)

Ce projet sert d’exemple complet d’un service web Flask connecté à une base MySQL, prêt à être conteneurisé et déployé sur une distribution Linux (ex: Kali) avec Docker. Il illustre :
- la persistance de données MySQL et leur affichage dans une page web,
- l’orchestration multi-conteneurs (application + base) avec Docker Compose,
- un pipeline CI pour construire et publier l’image sur Docker Hub,
- un déploiement reproductible sur n’importe quelle VM Linux.

En pratique, vous pouvez cloner le dépôt sur une VM Linux, exécuter `docker compose up -d` et obtenir immédiatement :
- un conteneur MySQL initialisé (base, table, données d’exemple),
- un conteneur Flask exposé sur le port 5000 qui affiche les données de la base.

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
# Construire et démarrer l’app + MySQL (port 5000 par défaut)
docker compose up -d --build

# Changer le port hôte (expose 5001:5000)
HOST_PORT=5001 docker compose up -d

# Ouvrir l’app
open http://127.0.0.1:5000  # macOS (ou 5001 si changé)
# ou: xdg-open http://127.0.0.1:5000 # Linux
```

Le service `web` attend que MySQL soit healthy, initialise la base (script `db_init.py`), puis lance Flask sur `0.0.0.0:5000`. Le port hôte est contrôlé par la variable `HOST_PORT` (défaut 5000).

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
