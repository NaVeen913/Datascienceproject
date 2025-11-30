import joblib
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self):
        self.model_path = Path("artifacts/model_trainer/model.joblib")
        self.model = joblib.load(self.model_path)

    def predict(self, input_data: dict):
        df = pd.DataFrame([input_data])
        prediction = self.model.predict(df)[0]
        return prediction

