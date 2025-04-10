import pandas as pd
import joblib
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from kfp.components import InputPath, OutputPath
import json

def evaluate_op(preprocessed_csv: InputPath(str), model_path: InputPath(str), metrics_path: OutputPath(str)):
    df = pd.read_csv(preprocessed_csv)
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = joblib.load(model_path)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    metrics = {"accuracy": accuracy}
    with open(metrics_path, "w") as f:
        json.dump(metrics, f)
