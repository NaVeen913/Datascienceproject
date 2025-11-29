
from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline


if __name__ == "__main__":
    try:
        # Stage 1: Data Ingestion
        ingestion_pipeline = DataIngestionTrainingPipeline()
        ingestion_pipeline.main()

        # Stage 2: Data Validation
        validation_pipeline = DataValidationTrainingPipeline()
        validation_pipeline.main()

        # Stage 3: Data Transformation
        transformation_pipeline = DataTransformationTrainingPipeline()
        transformation_pipeline.main()

    except Exception as e:
        logger.exception(e)
        raise e

    








