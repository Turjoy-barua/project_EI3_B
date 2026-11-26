import uvicorn
import mysql.connector

from datetime import datetime
import sqlite3

DB_NAME = "somnia.db"


def get_connection():
    # check_same_thread=False permet d'utiliser la connexion avec FastAPI et le thread des capteurs
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS mesures_capteurs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date_heure TEXT NOT NULL,
                temperature REAL NOT NULL,
                humidite REAL NOT NULL,
                lumiere INTEGER NOT NULL,
                son INTEGER NOT NULL
            )
        """)
        # Index sur date_heure pour accélérer l'affichage des graphiques et moyennes
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_date_heure
            ON mesures_capteurs (date_heure)
        """)


def inserer_mesure(temperature: float, humidite: float, lumiere: int, son: int):
    maintenant = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with get_connection() as conn:
        conn.execute(
            """
            INSERT INTO mesures_capteurs (date_heure, temperature, humidite, lumiere, son)
            VALUES (?, ?, ?, ?, ?)
            """,
            (maintenant, temperature, humidite, lumiere, son),
        )


def recuperer_dernieres_mesures(limite: int = 20):
    with get_connection() as conn:
        lignes = conn.execute(
            """
            SELECT date_heure, temperature, humidite, lumiere, son
            FROM mesures_capteurs
            ORDER BY id DESC
            LIMIT ?
            """,
            (limite,),
        ).fetchall()
    # Remettre dans l'ordre chronologique (du plus ancien au plus récent) pour les graphiques
    return [dict(ligne) for ligne in reversed(lignes)]


def recuperer_moyennes():
    with get_connection() as conn:
        res = conn.execute("""
            SELECT
                ROUND(AVG(temperature), 1) AS avg_temp,
                ROUND(AVG(humidite), 1) AS avg_humi,
                ROUND(AVG(son), 0) AS avg_sound,
                ROUND(AVG(lumiere), 0) AS avg_light,
                COUNT(*) AS total
            FROM mesures_capteurs
        """).fetchone()
    return dict(res)


init_db()