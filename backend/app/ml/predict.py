import joblib
import pandas as pd
from pathlib import Path
from .preprocessing import prepare_features

MODEL_PATH = Path(__file__).resolve().parents[2] / "models" / "model.joblib"

def predict(data: dict) -> dict:
    model = joblib.load(MODEL_PATH)
    df = pd.DataFrame([data])
    X = prepare_features(df)
    preds = model.predict(X)
    return {"predictions": preds.tolist()}
