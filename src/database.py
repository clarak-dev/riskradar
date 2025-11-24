"""
Módulo de integração com o banco de dados do RiskRadar.

Responsável por:
- criar a tabela de previsões (se ainda não existir)
- salvar novas previsões realizadas pelo modelo
"""

import sqlite3
from datetime import datetime

DB_PATH = "riskradar.db"


def get_connection():
    """Abre uma conexão com o banco SQLite."""
    conn = sqlite3.connect(DB_PATH)
    return conn


def init_db():
    """Cria a tabela de previsões, caso ainda não exista."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS predicoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            renda REAL,
            idade INTEGER,
            score REAL,
            risco_previsto TEXT,
            timestamp TEXT
        );
        """
    )
    conn.commit()
    conn.close()


def salvar_predicao(renda, idade, score, risco_previsto):
    """Insere uma nova previsão na tabela de predicoes."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO predicoes (renda, idade, score, risco_previsto, timestamp)
        VALUES (?, ?, ?, ?, ?);
        """,
        (renda, idade, score, risco_previsto, datetime.now().isoformat()),
    )
    conn.commit()
    conn.close()
