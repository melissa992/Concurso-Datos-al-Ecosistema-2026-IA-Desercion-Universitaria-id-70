import json
import os
from pathlib import Path
from typing import Optional

import joblib

# Modelo "de fábrica", empaquetado con el repo (solo lectura en Vercel).
PACKAGED_MODEL_DIR = Path(__file__).resolve().parents[2] / "models"
PACKAGED_MODEL_PATH = PACKAGED_MODEL_DIR / "model.joblib"
PACKAGED_MODEL_INFO_PATH = PACKAGED_MODEL_DIR / "model_info.json"

# En Vercel (y en cualquier entorno serverless similar) el resto del
# filesystem del proyecto es de solo lectura; únicamente /tmp admite
# escritura, aunque no persiste entre invocaciones/cold starts. Si se
# reentrena en producción, se guarda ahí; localmente se usa backend/models.
IS_SERVERLESS = bool(os.getenv("VERCEL") or os.getenv("AWS_LAMBDA_FUNCTION_NAME"))
WRITABLE_MODEL_DIR = Path("/tmp/models") if IS_SERVERLESS else PACKAGED_MODEL_DIR
WRITABLE_MODEL_PATH = WRITABLE_MODEL_DIR / "model.joblib"
WRITABLE_MODEL_INFO_PATH = WRITABLE_MODEL_DIR / "model_info.json"


def _first_existing(*paths: Path) -> Optional[Path]:
    for path in paths:
        if path.exists():
            return path
    return None


def load_model():
    path = _first_existing(WRITABLE_MODEL_PATH, PACKAGED_MODEL_PATH)
    if path is None:
        return None
    try:
        return joblib.load(path)
    except Exception:
        return None


def load_model_info():
    path = _first_existing(WRITABLE_MODEL_INFO_PATH, PACKAGED_MODEL_INFO_PATH)
    if path is None:
        return {"trained": False}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"trained": False}


def save_model_info(info: dict):
    WRITABLE_MODEL_DIR.mkdir(parents=True, exist_ok=True)
    with open(WRITABLE_MODEL_INFO_PATH, "w", encoding="utf-8") as f:
        json.dump(info, f, ensure_ascii=False, indent=2)
