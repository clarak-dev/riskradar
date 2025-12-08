import streamlit as st
import requests

st.title("Simulador de risco de crédito")

st.markdown(
    """
Nesta página, você pode simular o risco de crédito de um cliente informando seus dados.
Os dados são enviados para a **API do RiskRadar**, que utiliza o modelo treinado para 
calcular a probabilidade de inadimplência.
"""
)

st.info(
    "Para que o simulador funcione, a API FastAPI precisa estar rodando em "
    "`http://127.0.0.1:8000` (com o comando `uvicorn src.api:app --reload`)."
)

st.divider()

# ------------------------------------------------------------------
# Formulário de entrada de dados do cliente
# ------------------------------------------------------------------
st.subheader("Dados do cliente")

col1, col2, col3 = st.columns(3)

with col1:
    idade = st.number_input("Idade", min_value=18, max_value=100, value=35, step=1)
    renda = st.number_input("Renda mensal (R$)", min_value=0.0, value=3000.0, step=100.0)
    tempo_emprego_anos = st.number_input(
        "Tempo de emprego (anos)", min_value=0.0, value=2.0, step=0.5
    )

with col2:
    valor_divida = st.number_input(
        "Valor total da dívida (R$)", min_value=0.0, value=1500.0, step=100.0
    )
    num_atrasos_12m = st.number_input(
        "Nº de atrasos (últimos 12 meses)", min_value=0, max_value=50, value=1, step=1
    )
    utilizacao_credito = st.number_input(
        "Utilização de crédito (0 a 1)", min_value=0.0, max_value=1.0, value=0.4, step=0.05
    )

with col3:
    possui_cartao_credito = st.selectbox(
        "Possui cartão de crédito?",
        options=[0, 1],
        format_func=lambda x: "Não" if x == 0 else "Sim",
    )
    score_interno = st.number_input(
        "Score interno", min_value=300, max_value=900, value=650, step=10
    )
    relacao_divida_renda = st.number_input(
        "Relação dívida/renda", min_value=0.0, value=0.5, step=0.05
    )

st.divider()

# Monta o payload igual ao esperado pela API
payload = {
    "idade": idade,
    "renda": renda,
    "tempo_emprego_anos": tempo_emprego_anos,
    "valor_divida": valor_divida,
    "num_atrasos_12m": num_atrasos_12m,
    "utilizacao_credito": utilizacao_credito,
    "possui_cartao_credito": possui_cartao_credito,
    "score_interno": score_interno,
    "relacao_divida_renda": relacao_divida_renda,
}

st.markdown("### Enviar simulação para a API")

if st.button("Calcular risco"):
    try:
        resposta = requests.post(
            "http://127.0.0.1:8000/prever_risco",
            json=payload,
            timeout=5,
        )

        if resposta.status_code == 200:
            dados = resposta.json()
            risco = dados.get("risco_previsto", None)
            mensagem = dados.get("mensagem", "")

            if risco is not None:
                risco_pct = risco * 100

                if risco_pct < 20:
                    st.success(
                        f"Risco previsto: **{risco_pct:.2f}%** — Perfil considerado de **baixo risco**."
                    )
                elif risco_pct < 50:
                    st.warning(
                        f"Risco previsto: **{risco_pct:.2f}%** — Perfil considerado de **risco moderado**."
                    )
                else:
                    st.error(
                        f"Risco previsto: **{risco_pct:.2f}%** — Perfil considerado de **alto risco**."
                    )

                if mensagem:
                    st.info(mensagem)
            else:
                st.warning("A API respondeu, mas não retornou o campo `risco_previsto`.")
        else:
            st.error(
                f"Erro ao chamar a API. Código de status: {resposta.status_code}"
            )

    except requests.exceptions.ConnectionError:
        st.error(
            "Não foi possível conectar à API. "
            "Verifique se ela está rodando em `http://127.0.0.1:8000`."
        )
    except Exception as e:
        st.error(f"Ocorreu um erro ao processar a requisição: {e}")
