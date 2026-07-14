from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd
from .preprocessing import prepare_features

MODEL_PATH = Path(__file__).resolve().parents[2] / "models" / "model.joblib"

def train_model(df: pd.DataFrame, target_col: str = "NOMBRE_ESTADO") -> dict:
    if target_col not in df.columns:
        raise ValueError(f"target column '{target_col}' not found in dataset")

    y = df[target_col].copy()
    X = df.drop(columns=[target_col])
    X = prepare_features(X)
    y_encoded, _ = pd.factorize(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42
    )
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, MODEL_PATH)
    return {"status": "trained", "model_path": str(MODEL_PATH)}
