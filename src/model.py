"""
Módulo de modelagem do RiskRadar.

Responsável por:
- treinar o modelo de classificação (Regressão Logística)
- avaliar o modelo com métricas como AUC e F1-score
- salvar e carregar o modelo treinado
"""

import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, f1_score, confusion_matrix

MODEL_PATH = "models/model.pkl"


def train_model(X_train, y_train):
    """Treina um modelo de Regressão Logística."""
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test):
    """Calcula métricas básicas de desempenho do modelo."""
    y_prob = model.predict_proba(X_test)[:, 1]
    y_pred = model.predict(X_test)

    auc = roc_auc_score(y_test, y_prob)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    return {"auc": auc, "f1": f1, "confusion_matrix": cm.tolist()}


def save_model(model):
    """Salva o modelo treinado em disco."""
    joblib.dump(model, MODEL_PATH)


def load_model():
    """Carrega o modelo treinado a partir do disco."""
    return joblib.load(MODEL_PATH)


def predict_risk(model, input_data: np.ndarray):
    """
    Retorna a probabilidade prevista de inadimplência
    para um ou mais clientes.
    """
    prob = model.predict_proba(input_data)[:, 1]
    return prob
