from sklearn.model_selection import train_test_split

from src.preprocessing import load_data, split_X_y
from src.model import train_model, save_model

# 1. Carregar base de dados
df = load_data("data/credit_data.csv")

# 2. Separar features e target
X, y = split_X_y(df, target="inadimplente")

# 3. Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# 4. Treinar modelo
model = train_model(X_train, y_train)

# 5. Salvar modelo
save_model(model)

print("✅ Modelo treinado e salvo em models/model.pkl")
