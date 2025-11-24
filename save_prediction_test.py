from src.database import create_table, salvar_previsao
from src.model import load_model
from src.preprocessing import load_data

# 1. Criar tabela se não existir
create_table()

# 2. Carregar modelo
model = load_model()

# 3. Carregar um cliente real da base
df = load_data("data/credit_data.csv")
cliente = df.iloc[0]  # primeiro registro

# 4. Separar apenas as features
X_cliente = cliente.drop(labels=["inadimplente"]).values.reshape(1, -1)

# 5. Prever risco
risco = model.predict_proba(X_cliente)[0][1]

# 6. Converter linha do df para dict
features = cliente.to_dict()

# 7. Salvar no banco
salvar_previsao(features, risco)

print("Previsão salva com sucesso!")
