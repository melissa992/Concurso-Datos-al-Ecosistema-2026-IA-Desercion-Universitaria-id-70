import pandas as pd


def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    """Basic preprocessing pipeline for the desercion dataset."""
    df = df.copy()

    if "FECHA_NACIMIENTO" in df.columns:
        df["FECHA_NACIMIENTO"] = pd.to_datetime(
            df["FECHA_NACIMIENTO"], errors="coerce", dayfirst=True
        )
        df["birth_year"] = df["FECHA_NACIMIENTO"].dt.year
        df["birth_month"] = df["FECHA_NACIMIENTO"].dt.month
        df = df.drop(columns=["FECHA_NACIMIENTO"])

    df = df.fillna("missing")
    object_columns = df.select_dtypes(include=["object"]).columns.tolist()
    if object_columns:
        df = pd.get_dummies(df, columns=object_columns, drop_first=True)
    return df
