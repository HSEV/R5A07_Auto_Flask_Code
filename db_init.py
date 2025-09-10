import os
import mysql.connector

DB_NAME = os.getenv("MYSQL_DB", "demo_flask")

DB_CONFIG_BASE = {
    "host": os.getenv("MYSQL_HOST", "127.0.0.1"),
    "port": int(os.getenv("MYSQL_PORT", "3306")),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
}

DDL_CREATE_DB = f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
DDL_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS samples (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    info VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
"""
DML_INSERT = """
INSERT INTO samples (name, info) VALUES (%s, %s)
"""
SAMPLE_DATA = [
    ("Alice", "Premier enregistrement"),
    ("Bob", "Deuxième enregistrement"),
    ("Charlie", "Troisième enregistrement")
]


def main():
    # 1) Connexion sans base pour créer la base si besoin
    conn = mysql.connector.connect(**DB_CONFIG_BASE)
    cur = conn.cursor()
    cur.execute(DDL_CREATE_DB)
    conn.commit()
    cur.close()
    conn.close()

    # 2) Connexion avec la base pour créer la table et insérer des données
    conn2 = mysql.connector.connect(database=DB_NAME, **DB_CONFIG_BASE)
    cur2 = conn2.cursor()
    cur2.execute(DDL_CREATE_TABLE)

    # Vérifier s'il y a déjà des données
    cur2.execute("SELECT COUNT(*) FROM samples")
    (count,) = cur2.fetchone()
    if count == 0:
        cur2.executemany(DML_INSERT, SAMPLE_DATA)
        conn2.commit()

    cur2.close()
    conn2.close()
    print(f"Base '{DB_NAME}' prête. Table 'samples' initialisée.")


if __name__ == "__main__":
    main()
