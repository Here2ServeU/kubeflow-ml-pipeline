import pandas as pd
from kfp.components import OutputPath

def data_load_op(output_csv_path: OutputPath(str)):
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    column_names = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"]
    df = pd.read_csv(url, names=column_names)
    df.to_csv(output_csv_path, index=False)
