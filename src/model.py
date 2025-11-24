import joblib
from sklearn.linear_model import LogisticRegression

MODEL_PATH = "models/model.pkl"

def train_model(X_train, y_train):
    """Treina o modelo de Regressão Logística."""
    model = LogisticRegression(max_iter=2000)
    model.fit(X_train, y_train)
    return model

def save_model(model, path: str = MODEL_PATH):
    """Salva o modelo treinado em disco."""
    joblib.dump(model, path)

def load_model(path: str = MODEL_PATH):
    """Carrega o modelo treinado a partir do disco."""
    return joblib.load(path)

