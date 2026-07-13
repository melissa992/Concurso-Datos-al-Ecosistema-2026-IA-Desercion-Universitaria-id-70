from fastapi import APIRouter, HTTPException

router = APIRouter()


@router.get("/dashboard")
def get_dashboard():
    # Return KPIs placeholders
    return {
        "total_records": 0,
        "total_datasets": 0,
        "total_variables": 0,
        "model": "not trained",
        "last_update": None,
    }


@router.get("/statistics")
def get_statistics():
    return {"status": "ok", "statistics": {}}


@router.get("/features")
def get_features():
    return {"features": []}


@router.get("/model")
def get_model():
    return {"model": "placeholder", "trained": False}


@router.post("/model/train")
def train_model():
    # Trigger training job (placeholder)
    return {"status": "training_started"}


@router.post("/model/predict")
def predict_model(payload: dict):
    # Accept JSON payload for prediction
    return {"predictions": [], "meta": {}}


@router.get("/model/metrics")
def model_metrics():
    return {"metrics": {}}


@router.get("/report")
def get_report():
    return {"report": "not ready"}
