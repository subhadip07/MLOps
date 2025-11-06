### Docker command to run MLflow:
docker run -it -p 5001:5000 -v .mlruns/:/basics/mlruns ghcr.io/mlflow/mlflow:v3.5.1 mlflow ui --host 0.0.0.0 --port 5000 --backend-store-uri file:/basics/mlruns