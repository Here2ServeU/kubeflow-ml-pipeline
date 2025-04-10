import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from kfp.components import InputPath, OutputPath

def train_op(preprocessed_csv: InputPath(str), model_path: OutputPath(str)):
    df = pd.read_csv(preprocessed_csv)
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)
    joblib.dump(clf, model_path)
