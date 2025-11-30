import json
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience import logger


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate(self):
        # 1) Read test data
        logger.info(f"Reading test data from: {self.config.test_data_path}")
        df = pd.read_csv(self.config.test_data_path)

        X_test = df.drop("target", axis=1)
        y_test = df["target"]

        # 2) Load trained model
        logger.info(f"Loading model from: {self.config.model_path}")
        model = joblib.load(self.config.model_path)

        # 3) Predict and calculate accuracy
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        logger.info(f"Model evaluation accuracy: {acc}")

        # 4) Save metrics to JSON file
        metrics = {"accuracy": acc}
        self.config.metric_file_name.parent.mkdir(parents=True, exist_ok=True)

        with open(self.config.metric_file_name, "w") as f:
            json.dump(metrics, f, indent=4)

        logger.info(f"Saved evaluation metrics to: {self.config.metric_file_name}")
        return metrics
