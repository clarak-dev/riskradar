# RiskRadar — Sistema Inteligente de Avaliação de Risco de Crédito

O **RiskRadar** é um projeto que desenvolvi para simular um sistema real de análise de risco de crédito.  
Ele cobre todo o fluxo: desde a criação e exploração dos dados, passando pelo treinamento de um modelo estatístico, até a disponibilização de uma **API funcional** capaz de receber informações de um cliente e retornar a probabilidade estimada de inadimplência.

Esse projeto nasceu da minha vontade de entender profundamente como soluções de crédito são construídas na prática e, ao mesmo tempo, fortalecer minhas habilidades em **Python, Machine Learning, APIs, organização de projetos e boas práticas de desenvolvimento**.

---

## 🔍 Visão Geral Técnica

O sistema foi construído com foco em clareza, modularidade e evolução futura.  
Principais componentes:

- **Modelo preditivo:** Regressão Logística  
- **Base de dados:** Simulação sintética realista  
- **API:** FastAPI  
- **Banco local:** SQLite (armazenando o histórico de previsões)  
- **Pipeline modular:**  
  - `preprocessing.py` — limpeza e engenharia de atributos  
  - `model.py` — treinamento e carregamento do modelo  
  - `api.py` — rotas e lógica de previsão  
  - `database.py` — registro das previsões na base  

Estrutura preparada para expansão sem quebrar o fluxo atual.

---

## 🎯 O que o Projeto Representa

Além de ser um estudo técnico, o RiskRadar representa minha forma de aprender:

- gosto de entender o processo completo, e não apenas uma etapa isolada  
- escrevo código de forma organizada e fácil de manter  
- construo projetos pensando em crescimento e uso real  
- busco sempre conectar tecnologia com impacto prático  

Ele também demonstra minha evolução como estudante de **Análise e Desenvolvimento de Sistemas** e meu interesse por **dados aplicados ao mercado financeiro**.

---

## 💡 Motivação

Sempre fui curiosa sobre como bancos e fintechs tomam decisões de crédito.  
Criar o RiskRadar foi a maneira que encontrei de transformar essa curiosidade em prática — criando algo que realmente se parece com um sistema inicial de risco utilizado em ambientes reais.

Além disso, é um projeto que reforça minha preparação para oportunidades em:

- dados  
- machine learning aplicado  
- back-end  
- produtos financeiros  
- IA e automações  

---

## 🚀 Próximos Passos

O projeto está preparado para crescer. Os próximos objetivos incluem:

- testar modelos mais avançados (Random Forest, XGBoost, LightGBM)  
- aplicar técnicas de explicabilidade (SHAP, LIME)  
- criar um dashboard analítico interativo  
- adicionar versionamento de modelos  
- hospedar a API em nuvem (Render, Railway, AWS)  
- implementar monitoramento de drift e qualidade do modelo  
- enriquecer a base com dados sintéticos ainda mais realistas  

---

