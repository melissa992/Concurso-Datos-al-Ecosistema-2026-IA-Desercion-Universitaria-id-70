import pandas as pd
from .preprocessing import prepare_features
from .model_loader import load_model, load_model_info


def predict(data: dict) -> dict:
    model = load_model()
    if model is None:
        raise FileNotFoundError("Modelo no disponible: entrena el modelo primero")

    info = load_model_info()
    feature_names = info.get("feature_names", [])

    df = pd.DataFrame([data])
    X = prepare_features(df)

    # pd.get_dummies sobre una sola fila solo genera UNA columna dummy por
    # cada variable categorica (la del valor recibido), que casi nunca
    # coincide con las columnas que vio el modelo al entrenar. Hay que
    # realinear a las columnas de entrenamiento (mismo orden, 0 en las que
    # no aplican) o el modelo rechaza la prediccion por nombres de columna
    # distintos.
    if feature_names:
        X = X.reindex(columns=feature_names, fill_value=0)

    preds = model.predict(X)
    labels = info.get("target_labels", [])
    mapped = [labels[p] if labels and p < len(labels) else int(p) for p in preds]
    return {"predictions": mapped}
