import json
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, f1_score, confusion_matrix, classification_report


DATA_PATH = "data/credit_data.csv"
TARGET_COL = "inadimplente"

MODEL_OUT = "models/model_v2.pkl"
SCALER_OUT = "models/scaler_v2.pkl"
FEATURES_OUT = "models/feature_columns_v2.json"


def main():
    df = pd.read_csv(DATA_PATH)

    # Remove id_cliente se existir (identificador não entra no modelo)
    if "id_cliente" in df.columns:
        df = df.drop(columns=["id_cliente"])

    if TARGET_COL not in df.columns:
        raise ValueError(f"Coluna alvo '{TARGET_COL}' não encontrada em {DATA_PATH}")

    # Features exatamente como a API envia
    feature_cols = [
        "idade",
        "renda",
        "tempo_emprego_anos",
        "valor_divida",
        "num_atrasos_12m",
        "utilizacao_credito",
        "possui_cartao_credito",
        "score_interno",
        "relacao_divida_renda",
    ]

    # Se a relação divida/renda não existir, cria
    if "relacao_divida_renda" not in df.columns:
        df["relacao_divida_renda"] = df["valor_divida"] / df["renda"].replace(0, 1)

    X = df[feature_cols].copy()
    y = df[TARGET_COL].copy()

    # Guardar ordem das colunas para a API usar igual
    with open(FEATURES_OUT, "w", encoding="utf-8") as f:
        json.dump(feature_cols, f, ensure_ascii=False, indent=2)

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Fit scaler somente no treino (boa prática)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Treinar modelo
    model = LogisticRegression(max_iter=2000)
    model.fit(X_train_scaled, y_train)

    # Avaliar
    y_proba = model.predict_proba(X_test_scaled)[:, 1]
    y_pred = (y_proba >= 0.5).astype(int)

    auc = roc_auc_score(y_test, y_proba)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print("\n=== Avaliação do modelo v2 (com scaler) ===")
    print(f"AUC: {auc:.4f}")
    print(f"F1-score: {f1:.4f}")
    print("\nMatriz de confusão:")
    print(cm)
    print("\nClassification report:")
    print(classification_report(y_test, y_pred))

    # Salvar modelo e scaler
    joblib.dump(model, MODEL_OUT)
    joblib.dump(scaler, SCALER_OUT)

    print(f"\n✅ Modelo salvo em: {MODEL_OUT}")
    print(f"✅ Scaler salvo em: {SCALER_OUT}")
    print(f"✅ Colunas salvas em: {FEATURES_OUT}")


if __name__ == "__main__":
    main()

