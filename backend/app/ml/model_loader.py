import joblib

MODEL_PATH = "backend/models/model.joblib"

def load_model():
    try:
        return joblib.load(MODEL_PATH)
    except Exception:
        return None
