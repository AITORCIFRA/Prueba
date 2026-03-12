import sqlite3
from datetime import datetime

DB_PATH = "/app/datos/registros.db"

def registrar_dato():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            valor TEXT NOT NULL
        )
    ''')
    
    ahora = datetime.now().isoformat()
    valor = f"Prueba automática {ahora}"
    
    cursor.execute("INSERT INTO registros (timestamp, valor) VALUES (?, ?)", (ahora, valor))
    conn.commit()
    
    print(f"[{ahora}] Registro insertado: {valor}")
    
    conn.close()

if __name__ == "__main__":
    registrar_dato()
