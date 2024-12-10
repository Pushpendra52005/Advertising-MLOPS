from training.pipeline.final_train.feature_engineering import FeatureEngineeringTrainingPipeline
from training.pipeline.final_train.model_training import ModelTrainingPipeline
from training.pipeline.final_train.model_evaluation import ModelEvaluationTrainingPipeline

from training.custom_logging import info_logger





PIPELINE = " Feature Engineering Pipeline"
info_logger.info(f">>>>> {PIPELINE} started <<<<")
feature_engineering = FeatureEngineeringTrainingPipeline()
feature_engineering.main()
info_logger.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")


PIPELINE = " Model Training Pipeline"
info_logger.info(f">>>>> {PIPELINE} started <<<<")
model_training = ModelTrainingPipeline()
model_training.main()
info_logger.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")



PIPELINE = " Model Evaluation Pipeline"
info_logger.info(f">>>>> {PIPELINE} started <<<<")
model_evaluation = ModelEvaluationTrainingPipeline()
model_evaluation.main()
info_logger.info(f">>>>>>>> {PIPELINE} completed <<<<<<<<<")



