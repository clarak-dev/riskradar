# RiskRadar – Sistema de Análise de Risco de Crédito

O **RiskRadar** é um projeto de estudo e simulação de um motor de análise de risco de crédito, inspirado em cenários reais utilizados por bancos e fintechs.

O objetivo principal é demonstrar, de forma prática, como dados financeiros e comportamentais podem ser utilizados para estimar a probabilidade de inadimplência de um cliente, integrando **Machine Learning**, **API** e **visualização de dados** em um único fluxo.

Este projeto foi construído de forma incremental, priorizando clareza, organização e evolução técnica ao longo do tempo.

---

## Motivação

Em ambientes financeiros reais, decisões de crédito precisam ser:

- rápidas
- consistentes
- explicáveis
- integradas a sistemas

O RiskRadar nasce como um laboratório para explorar essas ideias, indo além de um modelo isolado e chegando a um **pipeline funcional**, com persistência em banco de dados e interface para simulação.

---

## Evolução do Modelo Preditivo

### Modelo v1 – Modelo inicial

A primeira versão do projeto utilizou um **modelo de Regressão Logística** treinado diretamente sobre os dados originais, com foco em:

- validação do problema
- entendimento das variáveis
- construção do primeiro pipeline de previsão

Esse modelo serviu como base conceitual e técnica para o restante do projeto.

---

### Modelo v2 – Modelo atual (em uso)

A segunda versão do modelo representa uma evolução importante do projeto.

Nesta etapa foram introduzidos:

- **Feature Engineering**
  - criação e padronização de variáveis relevantes
  - uso explícito da relação dívida/renda
- **Normalização dos dados**
  - aplicação de `StandardScaler`
  - scaler treinado apenas no conjunto de treino
- **Persistência completa**
  - modelo salvo em arquivo (`model_v2.pkl`)
  - scaler salvo separadamente (`scaler_v2.pkl`)
  - ordem das features registrada em `feature_columns_v2.json`

Essa abordagem garante consistência entre treino e inferência, aproximando o projeto de um cenário real de produção.

📌 **Atualmente, a API do RiskRadar utiliza exclusivamente o modelo v2.**

---

## Arquitetura Geral do Projeto

O projeto é organizado de forma modular, separando responsabilidades:

- **Dados**: base simulada de clientes
- **Modelagem**: scripts de treino e avaliação
- **API**: serviço de previsão de risco
- **Banco de dados**: persistência das previsões
- **Dashboard**: visualização e simulação interativa

A comunicação entre os componentes segue um fluxo simples e claro:

entrada de dados → pré-processamento → modelo → persistência → visualização

---

## API de Previsão de Risco

A API foi desenvolvida com **FastAPI** e tem como responsabilidade:

- receber os dados do cliente
- aplicar o mesmo pré-processamento do treino (scaler)
- calcular a probabilidade de inadimplência
- registrar a previsão no banco SQLite

A documentação interativa é disponibilizada via Swagger, facilitando testes e validações.

---

## Dashboard e Simulação

O dashboard foi construído com **Streamlit** e permite:

- visualizar previsões registradas
- acompanhar métricas agregadas de risco
- simular novos clientes e consultar o risco via API
- analisar graficamente a distribuição de risco da carteira simulada

Essa camada reforça a visão de negócio do projeto, indo além do código.

---

## Próximos Passos

Os próximos passos planejados para o projeto incluem:

- comparação formal entre o modelo v1 e v2 (AUC, F1-score)
- inclusão de explicabilidade do modelo (ex: SHAP)
- definição de thresholds de decisão (aprovação, revisão, recusa)
- simulações de estresse da carteira de crédito
- refinamento visual do dashboard

Essas evoluções serão feitas mantendo o foco em clareza, explicabilidade e aplicabilidade prática.

---

## Considerações Finais

O RiskRadar não tem como objetivo ser um produto final, mas sim um **projeto evolutivo**, que demonstra capacidade técnica, visão de sistema e entendimento do problema de crédito de ponta a ponta.

Ele reflete decisões conscientes ao longo do desenvolvimento, valorizando mais a construção sólida do que soluções excessivamente complexas.


