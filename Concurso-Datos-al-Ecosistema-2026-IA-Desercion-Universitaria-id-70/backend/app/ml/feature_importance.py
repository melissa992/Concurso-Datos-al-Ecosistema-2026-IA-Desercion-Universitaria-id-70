from .model_loader import load_model, load_model_info


def get_feature_importance():
    model = load_model()
    if model is None:
        raise FileNotFoundError("Modelo no disponible: entrena el modelo primero")
    info = load_model_info()
    feature_names = info.get("feature_names", [])
    if hasattr(model, "feature_importances_"):
        importances = model.feature_importances_.tolist()
        if feature_names and len(feature_names) == len(importances):
            return [
                {"feature": name, "importance": float(value)}
                for name, value in zip(feature_names, importances)
            ]
        return [{"feature": str(i), "importance": float(value)} for i, value in enumerate(importances)]
    return []
