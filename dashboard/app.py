import streamlit as st
import sqlite3
import pandas as pd


# Configurações básicas da página
st.set_page_config(
    page_title="RiskRadar - Dashboard de Risco de Crédito",
    page_icon="📊",
    layout="wide",
)

# Título principal
st.title("RiskRadar - Dashboard de Risco de Crédito")

# Subtítulo
st.markdown(
    """
Este dashboard faz parte do projeto **RiskRadar**, um sistema de análise de risco de crédito
que simula um motor de crédito real, utilizando modelo preditivo, API e banco de dados.

Aqui, a ideia é visualizar os dados e as previsões de forma simples e objetiva, 
e aos poucos ir evoluindo para uma visão mais analítica do portfólio de risco.
"""
)

st.divider()

st.markdown("👈 No próximo passo, vamos conectar este painel ao banco SQLite (`risk.db`) e exibir as previsões.")

# ------------------------------------------------------------------
# Seção: Previsões salvas no banco
# ------------------------------------------------------------------
st.subheader("Previsões registradas no banco de dados")

caminho_banco = "risk.db"

try:
    # Conectar ao SQLite
    conn = sqlite3.connect(caminho_banco)

    # Aqui estou assumindo que a tabela se chama 'previsoes_risco'
    # Se o nome for diferente, depois a gente ajusta.
    df_prev = pd.read_sql_query("SELECT * FROM previsoes_risco", conn)

    conn.close()

    if df_prev.empty:
        st.info("Ainda não há previsões registradas no banco de dados.")
    else:
        # Mostrar um resumo rápido
        st.write(f"Total de previsões registradas: **{len(df_prev)}**")

        # Se existir uma coluna 'risco_previsto', podemos fazer alguns destaques
        if "risco_previsto" in df_prev.columns:
            risco_medio = df_prev["risco_previsto"].mean()
            alto_risco = (df_prev["risco_previsto"] >= 0.5).mean() * 100

            col1, col2 = st.columns(2)
            col1.metric("Risco médio previsto", f"{risco_medio:.2%}")
            col2.metric("% de clientes de alto risco (≥ 0.5)", f"{alto_risco:.1f}%")

        st.markdown("### Últimas previsões")
        st.dataframe(df_prev.tail(20), use_container_width=True)

except Exception as e:
    st.warning(
        "Não foi possível carregar as previsões do banco de dados ainda. "
        "Verifique se o arquivo `risk.db` e a tabela de previsões já foram criados."
    )
