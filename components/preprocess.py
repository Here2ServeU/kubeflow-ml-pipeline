import pandas as pd
from sklearn.preprocessing import StandardScaler
from kfp.components import InputPath, OutputPath

def preprocess_op(input_csv_path: InputPath(str), output_csv_path: OutputPath(str)):
    df = pd.read_csv(input_csv_path)
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    df_scaled = pd.DataFrame(X_scaled, columns=X.columns)
    df_scaled["Outcome"] = y
    df_scaled.to_csv(output_csv_path, index=False)
