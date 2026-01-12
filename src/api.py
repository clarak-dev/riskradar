from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import joblib
import json

from src.database import salvar_previsao, create_table

app = FastAPI(title="RiskRadar API (v2)")

# Garantir tabela do banco
create_table()

# Carregar modelo v2 e scaler v2
MODEL_PATH = "models/model_v2.pkl"
SCALER_PATH = "models/scaler_v2.pkl"
FEATURES_PATH = "models/feature_columns_v2.json"

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

with open(FEATURES_PATH, "r", encoding="utf-8") as f:
    FEATURE_COLS = json.load(f)


# Modelo de entrada (JSON)
class Cliente(BaseModel):
    idade: int = Field(..., ge=18, le=100)
    renda: float = Field(..., gt=0)
    tempo_emprego_anos: float = Field(..., ge=0)
    valor_divida: float = Field(..., ge=0)
    num_atrasos_12m: int = Field(..., ge=0)
    utilizacao_credito: float = Field(..., ge=0, le=1)
    possui_cartao_credito: int = Field(..., ge=0, le=1)
    score_interno: int = Field(..., ge=300, le=900)
    relacao_divida_renda: float = Field(..., ge=0)


@app.get("/")
def healthcheck():
    return {"status": "ok", "model": "v2"}


@app.post("/prever_risco")
def prever_risco_api(cliente: Cliente):
    dados = cliente.dict()

    # DataFrame com 1 linha (cliente)
    df = pd.DataFrame([dados])

    # Garantir que as colunas e a ordem são exatamente as do treino
    df = df[FEATURE_COLS]

    # Aplicar o mesmo scaler usado no treino
    X_scaled = scaler.transform(df)

    # Prever probabilidade de inadimplência
    risco = model.predict_proba(X_scaled)[0][1]

    # Salvar no banco
    salvar_previsao(dados, risco)

    return {
        "risco_previsto": float(risco),
        "mensagem": "Previsão registrada no banco com sucesso!"
    }
