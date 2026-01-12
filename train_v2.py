import json
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, f1_score, confusion_matrix, classification_report


DATA_PATH = "data/credit_data_fe_scaled.csv"
TARGET_COL = "inadimplente"

MODEL_OUT = "models/model_v2.pkl"
FEATURES_OUT = "models/feature_columns_v2.json"


def main():
    # 1) Carregar dados
    df = pd.read_csv(DATA_PATH)

    # 2) Separar X e y
    if TARGET_COL not in df.columns:
        raise ValueError(f"Coluna alvo '{TARGET_COL}' não encontrada em {DATA_PATH}")

    y = df[TARGET_COL]
    X = df.drop(columns=[TARGET_COL])

    # 3) Garantir que só tem colunas numéricas (porque está escalonada)
    # (Se tiver alguma coluna texto por acidente, removemos aqui)
    X = X.select_dtypes(include=["number"])

    # 4) Guardar ordem das colunas para a API usar exatamente igual
    feature_cols = list(X.columns)
    with open(FEATURES_OUT, "w", encoding="utf-8") as f:
        json.dump(feature_cols, f, ensure_ascii=False, indent=2)

    # 5) Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # 6) Treinar modelo
    model = LogisticRegression(max_iter=2000)
    model.fit(X_train, y_train)

    # 7) Avaliar
    y_proba = model.predict_proba(X_test)[:, 1]
    y_pred = (y_proba >= 0.5).astype(int)

    auc = roc_auc_score(y_test, y_proba)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print("\n=== Avaliação do modelo v2 ===")
    print(f"AUC: {auc:.4f}")
    print(f"F1-score: {f1:.4f}")
    print("\nMatriz de confusão:")
    print(cm)
    print("\nClassification report:")
    print(classification_report(y_test, y_pred))

    # 8) Salvar modelo
    joblib.dump(model, MODEL_OUT)
    print(f"\n✅ Modelo salvo em: {MODEL_OUT}")
    print(f"✅ Colunas salvas em: {FEATURES_OUT}")


if __name__ == "__main__":
    main()
