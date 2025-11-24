# RiskRadar – Sistema de Análise de Risco de Crédito

O **RiskRadar** é um sistema que simula o funcionamento de um motor de crédito usado em bancos para avaliar o risco de inadimplência de clientes.

A partir de dados socioeconômicos e financeiros, o sistema realiza:

- Upload e leitura de base de dados
- Limpeza e tratamento dos dados
- Análise exploratória
- Criação de variáveis derivadas (feature engineering)
- Treinamento de um modelo preditivo de risco (Regressão Logística)
- Geração de score de risco para cada cliente
- Armazenamento das previsões em banco SQL
- Exposição de uma API para consulta de risco
- Dashboard com indicadores de portfólio e performance do modelo

---

## 🎯 Objetivo

Demonstrar um fluxo completo de **análise de risco de crédito**, unindo:

- Python e Machine Learning  
- Banco de dados SQL  
- Exposição via API  
- Visualização em dashboard

Esse projeto foi pensado para simular um contexto real de **motores de crédito** usados em bancos e fintechs.

---

## 🧠 Tecnologias previstas

- **Python**
  - Pandas
  - Scikit-Learn
  - Matplotlib / Seaborn
  - SHAP (interpretabilidade do modelo)

- **Banco de Dados**
  - SQLite (inicialmente)
  - SQLAlchemy para integração

- **API**
  - FastAPI ou Flask

- **Dashboard**
  - Streamlit (primeira versão)
  - Possível integração futura com Power BI

---

## 📂 Estrutura do projeto (inicial)

```bash
riskradar/
├── data/          # Bases de dados (brutas e tratadas)
├── notebooks/     # Notebooks de análise exploratória
├── src/           # Código-fonte principal
│   ├── preprocessing.py
│   ├── model.py
│   ├── database.py
│   └── api.py
├── dashboard/     # Código do dashboard (Streamlit)
├── models/        # Modelos treinados (.pkl, etc.)
├── README.md




## 🚧 Status do projeto

Em desenvolvimento.  
Primeira etapa: organizar estrutura, EDA inicial da base e pipeline de pré-processamento + modelo baseline.
