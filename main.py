import os
import sys
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig


if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)

        #data ingestion
        data_ingestion=DataIngestion(dataingestionconfig)
        logging.info("Data Ingestion Initiated")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(dataingestionartifact)

        #data validation
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the Data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artifact)

        #data transformation
        logging.info("Data Transformation Started")
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)
        data_transformation_artifact = data_transformation.intiate_data_transformation()
        logging.info("Data Transformation Completed")
        print(data_transformation_artifact)

        #model training
        logging.info("Model Training Started")
        model_training_config = ModelTrainerConfig(trainingpipelineconfig)
        model_training = ModelTrainer(model_trainer_config=model_training_config, data_transformation_artifact=data_transformation_artifact)
        model_training_artifact = model_training.intiate_model_trainer()
        logging.info("Model Training Completed")
        print(model_training_artifact)

    except Exception as e:
           raise NetworkSecurityException(e, sys)