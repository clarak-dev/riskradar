import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Carrega dados a partir de um CSV."""
    df = pd.read_csv(path)
    return df

def split_X_y(df: pd.DataFrame, target: str = "inadimplente"):
    """
    Separa features (X) e target (y).
    Remove colunas que não devem entrar no modelo, como id_cliente.
    """
    colunas_remover = [target]
    if "id_cliente" in df.columns:
        colunas_remover.append("id_cliente")

    X = df.drop(columns=colunas_remover)
    y = df[target]
    return X, y
