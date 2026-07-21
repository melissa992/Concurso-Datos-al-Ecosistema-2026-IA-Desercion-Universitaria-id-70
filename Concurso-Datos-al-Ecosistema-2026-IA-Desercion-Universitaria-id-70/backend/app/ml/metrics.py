from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix


def compute_metrics(y_true, y_pred):
    # target_col (NOMBRE_ESTADO) tiene más de 2 clases, por lo que se debe
    # promediar por clase ('weighted') en lugar de usar el default 'binary',
    # que lanza ValueError cuando hay más de 2 clases.
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, average="weighted", zero_division=0),
        "recall": recall_score(y_true, y_pred, average="weighted", zero_division=0),
        "f1": f1_score(y_true, y_pred, average="weighted", zero_division=0),
        "confusion_matrix": confusion_matrix(y_true, y_pred).tolist(),
    }
