import os
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from src.datascience.entity.config_entity import ModelTrainerConfig
from src.datascience import logger


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        # 1) Load train + test data
        logger.info("Loading train and test data for model training")
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)

        # 2) Split into X, y
        X_train = train_df.drop("target", axis=1)
        y_train = train_df["target"]

        X_test = test_df.drop("target", axis=1)
        y_test = test_df["target"]

        # 3) Train model (Logistic Regression for Iris)
        logger.info("Training LogisticRegression model")
        model = LogisticRegression(max_iter=200)
        model.fit(X_train, y_train)

        # 4) Evaluate
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        logger.info(f"Model accuracy on test set: {acc:.4f}")

        # 5) Save model
        model_path = os.path.join(self.config.root_dir, self.config.model_name)
        joblib.dump(model, model_path)
        logger.info(f"Saved model to: {model_path}")
