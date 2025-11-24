# RiskRadar – Sistema de Análise de Risco de Crédito

O **RiskRadar** é um projeto que desenvolvi para estudar, na prática, como funcionam modelos de risco de crédito usados por bancos e fintechs.  
Aqui eu simulei um mini motor de decisão capaz de prever a probabilidade de inadimplência de um cliente a partir de variáveis financeiras e comportamentais.

O projeto foi construído do zero: geração da base, EDA, criação das features, modelo, persistência, API e testes no Swagger.

---

## 🚀 Objetivo

Criar um sistema completo de previsão de risco de crédito, passando por:

- análise e preparação de dados  
- feature engineering  
- treinamento de modelo (Regressão Logística)  
- construção de uma API com FastAPI  
- armazenamento das previsões em SQLite  
- testes reais via Swagger UI  

Tudo isso simulando o fluxo real utilizado em motores de crédito.

---

## 📊 Tecnologias utilizadas

- Python 3.11  
- Pandas, NumPy  
- Scikit-Learn  
- Matplotlib e Seaborn  
- FastAPI + Uvicorn  
- SQLite  
- Streamlit (próximos passos)  
- Git e GitHub  

---

## 📁 Estrutura do Projeto

riskradar/
├── data/ # Base de dados sintética
├── notebooks/ # EDA e experimentos
│ └── 01_eda.ipynb
├── models/ # Modelo treinado (model.pkl)
├── src/ # Código principal
│ ├── preprocessing.py
│ ├── model.py
│ ├── api.py
│ └── database.py
├── dashboard/ # (em construção) Streamlit App
├── requirements.txt
└── README.md

yaml
Copiar código

---

## 🧠 Modelo Preditivo

Utilizei a **Regressão Logística**, por ser um modelo clássico e bastante usado para crédito.

Métricas avaliadas:

- AUC  
- F1-score  
- Matriz de confusão  

As features consideradas incluem:

- idade  
- renda  
- tempo de emprego  
- valor da dívida  
- atrasos nos últimos 12 meses  
- utilização de crédito  
- score interno  
- relação dívida/renda  

---

## 🚀 API – FastAPI

A API expõe um endpoint:

POST /prever_risco

css
Copiar código

Envia os dados de um cliente e retorna a probabilidade estimada de inadimplência:

```json
{
  "risco_previsto": 0.12,
  "mensagem": "Previsão registrada no banco com sucesso!"
}
A documentação automática está disponível em:

arduino
Copiar código
http://127.0.0.1:8000/docs
🗄 Armazenamento no SQLite
Cada previsão feita pela API é automaticamente salva no banco local risk.db com:

dados do cliente

risco calculado

timestamp da operação

Isso simula como instituições financeiras registram decisões de crédito.

🙋‍♀️ Minha Motivação
Sempre tive interesse na área de dados e em como bancos tomam decisões baseadas em modelos estatísticos e machine learning.
Decidi criar este projeto para:

aprender conceitos de crédito

reforçar modelagem e EDA

praticar FastAPI

montar um projeto completo para meu portfólio

Foi um desafio, mas também uma experiência muito boa para consolidar o que venho estudando.

🔧 Como executar
bash
Copiar código
git clone https://github.com/clarak-dev/riskradar.git
cd riskradar
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn src.api:app --reload
Depois é só acessar:

arduino
Copiar código
http://127.0.0.1:8000/docs
📌 Próximos passos (roadmap pessoal)
 Criar o dashboard no Streamlit

 Mostrar métricas de modelo e gráficos no front-end

 Página para simular clientes manualmente

 Deploy da API (Render/Railway)

 Deploy do dashboard (Streamlit Cloud)

 Melhorar explicabilidade com SHAP

 Testes automatizados

 Adicionar CI/CD simples

📬 Contato
Se quiser conversar sobre o projeto, ideias ou melhorias:

linkedin.com/in/clarakricia-dev/