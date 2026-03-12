import sqlite3
import requests
from datetime import datetime

DB_PATH = "/app/datos/usuarios.db"
URL = "https://hotfix.cifraeducacion.com/health"

def health_check():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS health_checks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            status_code INTEGER,
            response_text TEXT
        )
    ''')

    ahora = datetime.now().isoformat()

    try:
        r = requests.get(URL, timeout=10)
        status = r.status_code
        texto = r.text.strip()[:500]  # guardamos máximo 500 caracteres
    except Exception as e:
        status = 0
        texto = f"Error: {str(e)}"

    cursor.execute(
        "INSERT INTO health_checks (timestamp, status_code, response_text) VALUES (?, ?, ?)",
        (ahora, status, texto)
    )
    conn.commit()
    conn.close()

    print(f"[{ahora}] Health check → Status: {status}")

if __name__ == "__main__":
    health_check()