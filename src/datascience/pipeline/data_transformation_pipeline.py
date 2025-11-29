from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.Data_transformation import DataTransformation
from src.datascience import logger




STAGE_NAME = "Data Transformation Stage"


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()

        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_split_data()
        logger.info("Data Transformation completed successfully")
