from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_ingestion import DataIngestion
from src.datascience import logger


class DataIngestionTrainingPipeline:
    def run(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)

        logger.info(">>>> Data Ingestion started <<<<")
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
        logger.info(">>>> Data Ingestion completed <<<<")

