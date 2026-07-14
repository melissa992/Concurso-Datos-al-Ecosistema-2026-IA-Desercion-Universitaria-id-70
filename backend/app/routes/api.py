from fastapi import APIRouter, HTTPException
from app.ml.data_loader import get_dataset_summary, load_dataset
from app.ml.training import train_model
from app.ml.model_loader import load_model
from app.ml.predict import predict
from app.ml.metrics import compute_metrics

router = APIRouter()


@router.get("/dashboard")
def get_dashboard():
    try:
        summary = get_dataset_summary()
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Dataset not available")

    model = load_model()
    return {
        "total_records": summary["total_records"],
        "total_datasets": 1,
        "total_variables": summary["total_variables"],
        "model": "trained" if model is not None else "not trained",
        "last_update": None,
        "columns": summary["columns"],
    }


@router.get("/statistics")
def get_statistics():
    try:
        summary = get_dataset_summary()
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Dataset not available")

    return {
        "status": "ok",
        "statistics": {
            "total_records": summary["total_records"],
            "total_variables": summary["total_variables"],
            "unique_values": summary["n_unique"],
        },
    }


@router.get("/features")
def get_features():
    try:
        summary = get_dataset_summary()
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Dataset not available")

    return {"features": summary["columns"]}


@router.get("/model")
def get_model():
    model = load_model()
    return {"model": "random_forest", "trained": model is not None}


@router.post("/model/train")
def train_model_route(target_col: str = "NOMBRE_ESTADO"):
    try:
        df = load_dataset()
        result = train_model(df, target_col=target_col)
        return result
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Dataset not available")
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.post("/model/predict")
def predict_model(payload: dict):
    try:
        result = predict(payload)
        return result
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="Model not available")
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))


@router.get("/model/metrics")
def model_metrics():
    return {"metrics": {}}


@router.get("/report")
def get_report():
    return {"report": "not ready"}
