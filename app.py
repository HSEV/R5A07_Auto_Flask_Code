import os
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Config depuis variables d'environnement avec valeurs par défaut
DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
    "port": int(os.getenv("MYSQL_PORT", "3306")),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
    "database": os.getenv("MYSQL_DB", "demo_flask"),
}

@app.route("/")
def index():
    message = "Votre page marche parfaitement vous avez reussi"

    # Connexion DB et lecture des données
    rows = []
    error = None
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT id, name, info FROM samples ORDER BY id ASC")
        rows = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        error = str(e)

    # La page affiche le message et la preuve via données récupérées
    return render_template("index.html", message=message, rows=rows, error=error)

if __name__ == "__main__":
    app.run(debug=True)
