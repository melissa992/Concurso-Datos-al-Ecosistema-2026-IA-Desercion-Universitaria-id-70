from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd
from .preprocessing import prepare_features
from .metrics import compute_metrics
from .model_loader import WRITABLE_MODEL_DIR, WRITABLE_MODEL_PATH, save_model_info

MODEL_DIR = WRITABLE_MODEL_DIR
MODEL_PATH = WRITABLE_MODEL_PATH


def train_model(df: pd.DataFrame, target_col: str = "NOMBRE_ESTADO") -> dict:
    if target_col not in df.columns:
        raise ValueError(f"target column '{target_col}' not found in dataset")

    y = df[target_col].copy()
    X = df.drop(columns=[target_col])
    X = prepare_features(X)
    y_encoded, target_labels = pd.factorize(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42
    )
    # n_estimators/max_depth acotados a propósito: un RandomForest sin límite
    # de profundidad sobre este dataset genera un .joblib de ~50MB, lo que
    # puede exceder el límite de tamaño de función serverless en Vercel
    # (250MB sin comprimir, sumando además pandas/scikit-learn).
    model = RandomForestClassifier(
        n_estimators=60, max_depth=14, random_state=42, n_jobs=-1
    )
    model.fit(X_train, y_train)
    MODEL_DIR.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, MODEL_PATH)

    y_pred = model.predict(X_test)
    metrics = compute_metrics(y_test, y_pred)
    model_info = {
        "trained": True,
        "model_name": "RandomForestClassifier",
        "target_col": target_col,
        "feature_names": X.columns.tolist(),
        "target_labels": [str(label) for label in target_labels.tolist()],
        "record_count": int(df.shape[0]),
        "metrics": metrics,
    }
    save_model_info(model_info)
    return {"status": "trained", "model_path": str(MODEL_PATH), "metrics": metrics}
