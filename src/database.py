import sqlite3
from datetime import datetime

DB_PATH = "risk.db"

def create_connection():
    """Cria uma conexão com o banco SQLite."""
    conn = sqlite3.connect(DB_PATH)
    return conn

def create_table():
    """Cria tabela de previsões se não existir."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS previsoes_risco (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            renda REAL,
            idade INTEGER,
            tempo_emprego REAL,
            valor_divida REAL,
            num_atrasos INTEGER,
            utilizacao_credito REAL,
            possui_cartao INTEGER,
            score_interno INTEGER,
            relacao_divida_renda REAL,
            risco_previsto REAL,
            timestamp TEXT
        );
    """)

    conn.commit()
    conn.close()

def salvar_previsao(features: dict, risco: float):
    """Salva as features e o resultado da previsão no banco."""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO previsoes_risco (
            renda, idade, tempo_emprego, valor_divida,
            num_atrasos, utilizacao_credito, possui_cartao,
            score_interno, relacao_divida_renda,
            risco_previsto, timestamp
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        features["renda"],
        features["idade"],
        features["tempo_emprego_anos"],
        features["valor_divida"],
        features["num_atrasos_12m"],
        features["utilizacao_credito"],
        features["possui_cartao_credito"],
        features["score_interno"],
        features["relacao_divida_renda"],
        risco,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()

