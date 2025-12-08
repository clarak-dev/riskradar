import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

st.title("Análises gráficas de risco de crédito")

st.markdown(
    """
Nesta página, analiso visualmente as previsões geradas pelo modelo do **RiskRadar**.
Os gráficos ajudam a entender a distribuição do risco, a evolução ao longo do tempo
e o comportamento geral da carteira simulada.
"""
)

caminho_banco = "risk.db"

try:
    conn = sqlite3.connect(caminho_banco)
    df_prev = pd.read_sql_query("SELECT * FROM previsoes_risco", conn)
    conn.close()

    if df_prev.empty:
        st.info("Ainda não há dados suficientes para gerar gráficos.")
    else:
        # Garante que o timestamp está em formato de data/hora
        if "timestamp" in df_prev.columns:
            df_prev["timestamp"] = pd.to_datetime(df_prev["timestamp"])

        st.divider()

        # ------------------------------------------------------------------
        # Gráfico 1: Distribuição do risco previsto
        # ------------------------------------------------------------------
        st.subheader("Distribuição do risco previsto")

        col1, col2 = st.columns([2, 1])

        with col1:
            fig, ax = plt.subplots()
            ax.hist(df_prev["risco_previsto"], bins=15)
            ax.set_xlabel("Risco previsto")
            ax.set_ylabel("Quantidade de clientes")
            ax.set_title("Histograma do risco previsto")
            st.pyplot(fig)

        with col2:
            st.markdown(
                """
                Este histograma mostra como os clientes estão distribuídos
                em relação ao risco previsto pelo modelo.  
                É útil para entender se a carteira está concentrada em baixo,
                médio ou alto risco.
                """
            )

        st.divider()

        # ------------------------------------------------------------------
        # Gráfico 2: Evolução do risco ao longo do tempo
        # ------------------------------------------------------------------
        if "timestamp" in df_prev.columns:
            st.subheader("Evolução do risco previsto ao longo do tempo")

            df_plot = df_prev.sort_values("timestamp")

            st.line_chart(
                df_plot.set_index("timestamp")["risco_previsto"],
                use_container_width=True,
            )

            st.markdown(
                """
                Este gráfico ajuda a visualizar se, ao longo do tempo, as previsões
                de risco estão ficando mais altas, mais baixas ou estáveis.
                """
            )
        else:
            st.info(
                "A coluna `timestamp` não está disponível. "
                "Não foi possível gerar a análise temporal."
            )

except Exception as e:
    st.warning(
        "Não foi possível carregar os dados do banco de dados para gerar as análises."
    )
