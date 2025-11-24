# RiskRadar – Sistema de Análise de Risco de Crédito

O **RiskRadar** é um projeto que desenvolvi para estudar, na prática, como funcionam modelos de risco de crédito usados por bancos e fintechs.  
Aqui eu simulo um mini motor de decisão capaz de prever a probabilidade de inadimplência de um cliente com base em variáveis financeiras e comportamentais.

O projeto foi construído do zero: geração da base, EDA, criação de features, treinamento do modelo, persistência, API e testes no Swagger.

---

## 🚀 Objetivo

Criar um sistema completo de previsão de risco de crédito, passando por:

- Análise e preparação de dados  
- Feature engineering  
- Treinamento de modelo (Regressão Logística)  
- Construção de uma API com FastAPI  
- Armazenamento das previsões em SQLite  
- Testes reais via Swagger UI  

Tudo isso simulando o fluxo real utilizado em motores de crédito.

---

## 📊 Tecnologias utilizadas

- Python  
- Pandas, NumPy  
- Scikit-Learn  
- Matplotlib e Seaborn  
- FastAPI + Uvicorn  
- SQLite  
- Streamlit *(próximos passos)*  
- Git e GitHub  

---

## 📁 Estrutura do Projeto

riskradar/
├── data/
│ └── credit_data.csv
├── notebooks/
│ └── 01_eda.ipynb
├── models/
│ └── model.pkl
├── src/
│ ├── preprocessing.py
│ ├── model.py
│ ├── api.py
│ └── database.py
├── dashboard/ # (em desenvolvimento)
├── risk.db # gerado pela API automaticamente
├── requirements.txt
└── README.md


---

## 🧠 Modelo Preditivo

Utilizei a **Regressão Logística**, um modelo clássico e amplamente usado em crédito por ser:

- Interpretável  
- Eficiente  
- Adequado para classificação binária  

### **Métricas avaliadas**

- AUC  
- F1-score  
- Matriz de Confusão  

### **Principais variáveis do modelo**

- idade  
- renda  
- tempo de emprego  
- valor total da dívida  
- atrasos nos últimos 12 meses  
- utilização de crédito  
- score interno  
- relação dívida/renda  
- possui cartão de crédito  

---

## 🚀 API – FastAPI

A API recebe os dados de um cliente e retorna a probabilidade estimada de inadimplência.

### 📌 **Endpoint principal**


POST /prever_risco

### **Exemplo de entrada JSON**

```json
{
  "idade": 45,
  "renda": 3200.5,
  "tempo_emprego_anos": 3.5,
  "valor_divida": 1500.9,
  "num_atrasos_12m": 1,
  "utilizacao_credito": 0.42,
  "possui_cartao_credito": 1,
  "score_interno": 650,
  "relacao_divida_renda": 0.46
}

📌 Documentação automática do Swagger

http://127.0.0.1:8000/docs

🗄 Armazenamento no SQLite

Cada previsão feita pela API é salva automaticamente no banco risk.db com:

Dados enviados pelo cliente

Probabilidade prevista

Timestamp da requisição

Essa estrutura simula como motores de crédito reais registram decisões para auditoria e análise posterior.

Minha motivação

Sempre tive interesse em entender como bancos e instituições financeiras usam dados para tomar decisões importantes.
Este projeto foi a minha forma de:

Praticar machine learning aplicado

Consolidar conhecimentos de API e backend

Entender o fluxo completo de um motor de risco

Criar um projeto forte e realista para meu portfólio

Foi um aprendizado enorme, muito próximo da prática do mercado.




📌 Próximos passos

 Criar dashboard no Streamlit

 Visualizar métricas e gráficos do modelo

 Criar página de simulação de clientes

 Deploy da API (Render, Railway ou HuggingFace Spaces)

 Deploy do dashboard

 Adicionar explicabilidade com SHAP

 Criar testes unitários

 Implementar CI/CD simples



📬 Contato

Clara Kricia Araujo de Paulo
linkedin.com/in/clarakricia-dev/