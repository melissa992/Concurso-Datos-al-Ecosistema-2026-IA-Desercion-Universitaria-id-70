import joblib

MODEL_PATH = "backend/models/model.joblib"

def get_feature_importance():
    model = joblib.load(MODEL_PATH)
    if hasattr(model, "feature_importances_"):
        return model.feature_importances_.tolist()
    return []
