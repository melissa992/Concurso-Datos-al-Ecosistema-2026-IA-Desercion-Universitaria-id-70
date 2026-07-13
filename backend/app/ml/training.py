from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import pandas as pd
from .preprocessing import prepare_features

MODEL_PATH = "backend/models/model.joblib"

def train_model(df: pd.DataFrame, target_col: str = "target") -> dict:
    df = prepare_features(df)
    X = df.drop(columns=[target_col])
    y = df[target_col]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, MODEL_PATH)
    return {"status": "trained", "model_path": MODEL_PATH}
