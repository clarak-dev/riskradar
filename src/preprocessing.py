"""
Módulo de pré-processamento de dados para o projeto RiskRadar.

Responsável por:
- carregar a base de dados
- limpar e tratar valores ausentes
- criar variáveis derivadas (feature engineering)
- separar variáveis de entrada (X) e alvo (y)
"""

import pandas as pd
from sklearn.model_selection import train_test_split


def load_data(path: str) -> pd.DataFrame:
    """Carrega a base de dados a partir de um arquivo CSV."""
    df = pd.read_csv(path)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Realiza uma limpeza simples nos dados (ex.: remoção de nulos)."""
    df = df.dropna()
    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cria variáveis derivadas.
    Exemplo: relação dívida/renda, se as colunas existirem.
    """
    if "valor_divida" in df.columns and "renda" in df.columns:
        df["divida_renda"] = df["valor_divida"] / (df["renda"] + 1)
    return df


def split_features_target(df: pd.DataFrame, target_col: str):
    """Separa o dataframe em conjuntos de treino e teste."""
    X = df.drop(columns=[target_col])
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    return X_train, X_test, y_train, y_test
