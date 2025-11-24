from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

from src.model import load_model
from src.database import salvar_previsao, create_table

app = FastAPI(title="RiskRadar API")

# Garantir tabela
create_table()

# Carregar modelo
model = load_model()

# Modelo de entrada (JSON → Python)
class Cliente(BaseModel):
    renda: float
    idade: int
    tempo_emprego_anos: float
    valor_divida: float
    num_atrasos_12m: int
    utilizacao_credito: float
    possui_cartao_credito: int
    score_interno: int
    relacao_divida_renda: float

@app.post("/prever_risco")
def prever_risco_api(cliente: Cliente):

    # Transformar entrada em DataFrame
    dados = cliente.dict()
    df = pd.DataFrame([dados])

    # MESMA ordem de colunas usada no treino
    colunas_ordenadas = [
        "idade",
        "renda",
        "tempo_emprego_anos",
        "valor_divida",
        "num_atrasos_12m",
        "utilizacao_credito",
        "possui_cartao_credito",
        "score_interno",
        "relacao_divida_renda",
    ]
    df = df[colunas_ordenadas]

    # Fazer previsão
    risco = model.predict_proba(df)[0][1]

    # Salvar no banco
    salvar_previsao(dados, risco)

    return {
        "risco_previsto": float(risco),
        "mensagem": "Previsão registrada no banco com sucesso!"
    }
