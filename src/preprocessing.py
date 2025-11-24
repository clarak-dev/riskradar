import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Carrega dados a partir de um CSV."""
    df = pd.read_csv(path)
    return df

def split_X_y(df: pd.DataFrame, target="inadimplente"):
    """Separa features e target."""
    X = df.drop(columns=[target])
    y = df[target]
    return X, y
