from src.datascience import logger
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

if __name__ == "__main__":
    try:
        # Stage 1: Data Ingestion
        ingestion_pipeline = DataIngestionTrainingPipeline()
        ingestion_pipeline.run()

        # Stage 2: Data Validation
        validation_pipeline = DataValidationTrainingPipeline()
        validation_pipeline.main()

    except Exception as e:
        logger.exception(e)
        raise e


    





