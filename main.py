from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeline

if __name__ == "__main__":
    try:
        pipeline = DataIngestionTrainingPipeline()
        pipeline.run()
    except Exception as e:
        logger.exception(e)
        raise e


