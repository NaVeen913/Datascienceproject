import pandas as pd
from pathlib import Path
from src.datascience.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split_data(self):
        # Load the dataset
        df = pd.read_csv(self.config.data_path)

        # Split into train and test
        train_df = df.sample(frac=0.8, random_state=42)
        test_df = df.drop(train_df.index)

        # Create directory
        Path(self.config.root_dir).mkdir(parents=True, exist_ok=True)

        # Save files
        train_df.to_csv(self.config.train_data_path, index=False)
        test_df.to_csv(self.config.test_data_path, index=False)

        print("Train and Test files created successfully!")
        print(f"Train file: {self.config.train_data_path}")
        print(f"Test file: {self.config.test_data_path}")

