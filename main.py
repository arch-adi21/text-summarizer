from textSummarizer.pipeline.step_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.step_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.logging import logger

STEP_ = "Data Ingestion"

try:
    logger.info(f"{STEP_} started already ...")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"{STEP_} completed successfully \n<== ==== ==== === ==== ==== ==>")
except Exception as e:
    logger.error(f"{STEP_} failed with error: {e}")
    raise e

STEP_ = "Data Validation"
try:
    logger.info(f"{STEP_} started already...")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f"{STEP_} completed successfully \n<== ==== ==== ==== ==== ==== ==>")
except Exception as e:
    logger.error(f"{STEP_} failed with error: {e}")
    raise e