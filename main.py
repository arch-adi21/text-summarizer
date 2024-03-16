from textSummarizer.pipeline.step_01_data_ingestion import DataIngestionTrainingPipeline
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