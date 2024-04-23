from textSummarizer.pipeline.step_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.step_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.step_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.step_04_model_trainer import ModelTrainerPipeline
from textSummarizer.pipeline.step_05_model_evaluation import ModelEvaluationPipeline
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

STEP_ = "Data Transformation"
try:
    logger.info(f"{STEP_} started already...")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f"{STEP_} completed successfully \n<== ==== ==== ==== ==== ==== ==>")
except Exception as e:
    logger.error(f"{STEP_} failed with error: {e}")
    raise e

STEP_ = "Model Training"
try:
    logger.info(f"{STEP_} started already...")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f"{STEP_} completed successfully \n<== ==== ==== ==== ==== ==== ==>")
except Exception as e:
    logger.error(f"{STEP_} failed with error: {e}")
    raise e

STEP_ = "Model Evaluation"
try:
    logger.info(f"{STEP_} started already...")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f"{STEP_} completed successfully \n<== ==== ==== ==== ==== ==== ==>")
except Exception as e:
    logger.error(f"{STEP_} failed with error: {e}")
    raise e