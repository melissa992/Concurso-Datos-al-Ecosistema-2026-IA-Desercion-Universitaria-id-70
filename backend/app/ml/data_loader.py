import pandas as pd
from pathlib import Path
from typing import Any, Dict

ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT_DIR / "data"
DATASET_PATH = DATA_DIR / "DATASET_DESERCION_LIMPIO.csv"


def load_dataset() -> pd.DataFrame:
    if not DATASET_PATH.exists():
        raise FileNotFoundError(f"Dataset file not found: {DATASET_PATH}")
    return pd.read_csv(DATASET_PATH)


def get_dataset_summary() -> Dict[str, Any]:
    df = load_dataset()
    return {
        "path": str(DATASET_PATH),
        "total_records": int(df.shape[0]),
        "total_variables": int(df.shape[1]),
        "columns": df.columns.tolist(),
        "n_unique": {col: int(df[col].nunique()) for col in df.columns},
    }
