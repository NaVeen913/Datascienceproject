from pathlib import Path
from src.datascience.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig,
)
from src.datascience.utils.common import read_yaml, create_directories
from src.datascience.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.datascience import logger


class ConfigurationManager:

    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
        schema_file_path=SCHEMA_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_file_path)

        create_directories([self.config.artifact_root])

    # ------------------------- STAGE 1: DATA INGESTION -------------------------
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )
        return data_ingestion_config

    # ------------------------- STAGE 2: DATA VALIDATION -------------------------
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation    
        schema = self.schema                   

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=Path(config.root_dir),
            STATUS_FILE=Path(config.STATUS_FILE),
            unzip_data_dir=Path(config.unzip_data_dir),
            all_schema=schema.COLUMNS       
        )
        return data_validation_config

    # ------------------------- STAGE 3: DATA TRANSFORMATION -------------------------
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=Path(config.root_dir),
            data_path=Path(config.data_path),
            train_data_path=Path(config.train_data_path),
            test_data_path=Path(config.test_data_path)
        )
        return data_transformation_config
    

    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=Path(config.root_dir),
            train_data_path=Path(config.train_data_path),
            test_data_path=Path(config.test_data_path),
            model_name=config.model_name,
        )
        return model_trainer_config

