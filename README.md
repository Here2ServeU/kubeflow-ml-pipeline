# Kubeflow ML Pipeline

This repository provides a complete example of an **end-to-end machine learning pipeline** using **Kubeflow** Pipelines. The pipeline includes **data loading, preprocessing, model training, evaluation, conditional deployment** using **KFServing,** and **CI/CD** integration with **GitHub Actions**.

## Project Structure and File Descriptions

### The components/ Directory

- **data_load.py**: Loads a dataset (Pima Indians Diabetes Dataset) from a public URL and saves it as a CSV file. This component is the entry point of the pipeline.
- **preprocess.py**: Reads the raw CSV, scales numerical features using `StandardScaler`, and outputs a preprocessed CSV with features and labels.
- **train.py**: Trains a `RandomForestClassifier` using the preprocessed data. The trained model is serialized using `joblib` and saved to a file.
- **evaluate.py**: Loads the trained model and evaluates it on a test set split from the same preprocessed dataset. Outputs evaluation metrics (accuracy) as a JSON file.
- **deploy.py**: Reads the evaluation metrics and conditionally simulates model deployment if accuracy exceeds a defined threshold (e.g., 0.85). You can integrate KFServing manifest application logic here.

### The Dockerfiles/ Directory

- **Dockerfile.train**: Builds the Docker image required for the `train.py` component, installing necessary dependencies like `scikit-learn`, `pandas`, and `joblib`.
- **Dockerfile.deploy**: Builds the Docker image used for the `deploy.py` component. Installs dependencies including `pandas` and `kfp`.

### The pipeline.py file

Defines the full pipeline using the Kubeflow Pipelines SDK. It connects the components in sequence:
1. Load data
2. Preprocess data
3. Train model
4. Evaluate model
5. Conditionally deploy model

You can compile this script using:
```bash
python pipeline.py
```

This generates a `pipeline.yaml` file that can be uploaded to a Kubeflow Pipelines UI or automated with CI/CD.

### The kfserving.yaml file

YAML manifest defining a `KFServing InferenceService` resource. This file is used to deploy a trained model (such as a scikit-learn model) as a REST endpoint. Replace the `storageUri` with your actual model location (e.g., S3 bucket or PVC path).

### The .github/workflows/kfp-pipeline.yml file

A GitHub Actions workflow for automating pipeline compilation and upload. On every push to the `main` branch, it:
1. Checks out the code
2. Sets up Python
3. Installs `kfp` SDK
4. Compiles the pipeline using `pipeline.py`

You can extend it to upload the compiled pipeline to a Kubeflow endpoint using the KFP client.

### The README.md file

This file. Explains the project, structure, and usage instructions.

---

## How the Components Work Together

1. **data_load.py** feeds raw data to **preprocess.py**.
2. **preprocess.py** cleans and normalizes the data for **train.py**.
3. **train.py** saves a model that is evaluated by **evaluate.py**.
4. **evaluate.py** calculates accuracy which is used by **deploy.py**.
5. **deploy.py** conditionally deploys the model based on the threshold.
6. **kfserving.yaml** can be applied when actual deployment is ready.

---

## Setup and Usage

### Local Setup
1. Install dependencies:
```bash
pip install kfp scikit-learn pandas joblib
```

2. Compile pipeline:
```bash
python pipeline.py
```

3. Upload to Kubeflow via UI or SDK.

### CI/CD Setup
- Commit and push to GitHub.
- GitHub Actions will trigger `.github/workflows/kfp-pipeline.yml`.
- Customize the workflow to include Kubeflow endpoint authentication and automatic upload.

### Deploying the Model
To deploy a trained model using KFServing:
1. Update the `kfserving.yaml` with the correct `storageUri`.
2. Apply using `kubectl`:
```bash
kubectl apply -f kfserving.yaml
```

## Requirements
- Python 3.9+
- Kubernetes Cluster with Kubeflow Pipelines
- Optional: KFServing installed and configured

## Next Steps
- Add Hyperparameter tuning with Katib
- Integrate ML metadata tracking
- Monitor using Prometheus/Grafana

This project provides a strong foundation for building scalable ML workflows using modern MLOps tools and principles.

---
## <div align="center">About the Author</div>

<div align="center">
  <img src="assets/emmanuel-naweji.jpg" alt="Emmanuel Naweji" width="120" height="120" style="border-radius: 50%;" />
</div>

**Emmanuel Naweji** is a seasoned Cloud and DevOps Engineer with years of experience helping companies architect and deploy secure, scalable infrastructure. He is the founder of initiatives that train and mentor individuals seeking careers in IT and has helped hundreds transition into Cloud, DevOps, and Infrastructure roles.

- Book a free consultation: [https://here4you.setmore.com](https://here4you.setmore.com)
- Connect on LinkedIn: [https://www.linkedin.com/in/ready2assist/](https://www.linkedin.com/in/ready2assist/)

Let's connect and discuss how I can help you build reliable, automated infrastructure the right way.


——

MIT License © 2025 Emmanuel Naweji

You are free to use, copy, modify, merge, publish, distribute, sublicense, or sell copies of this software and its associated documentation files (the “Software”), provided that the copyright and permission notice appears in all copies or substantial portions of the Software.

This Software is provided “as is,” without any warranty — express or implied — including but not limited to merchantability, fitness for a particular purpose, or non-infringement. In no event will the authors be liable for any claim, damages, or other liability arising from the use of the Software.

