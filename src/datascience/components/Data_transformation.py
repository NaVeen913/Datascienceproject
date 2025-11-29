from src.datascience.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split_data(self):

        print("DataTransformation.train_test_split_data() called")
