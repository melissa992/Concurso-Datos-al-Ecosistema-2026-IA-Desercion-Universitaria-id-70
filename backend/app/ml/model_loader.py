import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parents[2] / "models" / "model.joblib"

def load_model():
    try:
        return joblib.load(MODEL_PATH)
    except Exception:
        return None
