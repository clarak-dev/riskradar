"""
API do RiskRadar.

Responsável por expor um endpoint para:
- receber dados de um cliente
- calcular o risco de inadimplência usando o modelo treinado
- salvar a previsão no banco
"""

from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

from .model import load_model, predict_risk
from .database import init_db, salvar_predicao


app = FastAPI(title="RiskRadar API")

model = None  # será carregado no startup


class Cliente(BaseModel):
    renda: float
    idade: int
    # futuramente podemos adicionar mais campos aqui


@app.on_event("startup")
def startup_event():
    """Executado quando a API é iniciada."""
    global model
    init_db()
    model = load_model()


def classificar_risco(score: float) -> str:
    """Classifica o risco em faixas a partir do score."""
    if score < 0.33:
        return "baixo"
    elif score < 0.66:
        return "médio"
    else:
        return "alto"


@app.post("/predict")
def predict(cliente: Cliente):
    """
    Recebe os dados de um cliente, calcula o risco e salva no banco.
    """
    input_array = np.array([[cliente.renda, cliente.idade]])
    score = float(predict_risk(model, input_array)[0])
    risco = classificar_risco(score)

    salvar_predicao(cliente.renda, cliente.idade, score, risco)

    return {"score": score, "risco": risco}
