from kfp.components import InputPath
import json

def deploy_op(metrics_path: InputPath(str)):
    with open(metrics_path, "r") as f:
        metrics = json.load(f)
    if metrics["accuracy"] > 0.85:
        print("Deploying model...")
        # Simulate deployment logic or trigger KFServing manifest apply
    else:
        print("Model did not meet accuracy threshold.")
