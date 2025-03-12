# Phishing Detection ML Pipeline

A machine learning system that detects phishing websites by analyzing URL and website features.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-5.0+-green.svg)
![AWS](https://img.shields.io/badge/AWS-S3%20|%20ECR-yellow.svg)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-red.svg)

## Overview

This project builds a complete machine learning pipeline that helps identify malicious phishing websites. It analyzes 30+ features extracted from URLs and website content to distinguish between legitimate websites and phishing attempts.

## Problem Statement

Phishing websites mimic legitimate sites to steal sensitive information like passwords and credit card details. This project creates an automated system to detect such threats.

## Dataset

The dataset contains 11,000+ website samples with 30 features including:
- URL structure (length, special characters, IP addresses)
- Domain properties (age, registration)
- Security indicators (SSL certificates)
- Content behavior (JavaScript events, iframes)
- External metrics (Google indexing, traffic)

## Project Structure

```
networksecurity/
│
├── cloud/                   # S3 sync functionality
├── components/              # Pipeline components
│   ├── data_ingestion.py    # Fetch data from MongoDB
│   ├── data_validation.py   # Validate data quality and schema
│   ├── data_transformation.py # Process and prepare features
│   └── model_trainer.py     # Train and evaluate models
│
├── constants/               # Configuration constants
├── entity/                  # Data classes for configuration
├── exception/               # Custom exception handling
├── logging/                 # Logging configuration
├── pipeline/                # Main pipeline workflow
│   └── training_pipeline.py # Orchestrates the ML workflow
│
└── utils/                   # Utility functions
    ├── main_utils/          # General utilities
    └── ml_utils/            # ML specific functions
```

## Pipeline Workflow

1. **Data Ingestion**:
   - Connect to MongoDB database
   - Extract data and create feature store
   - Split data into training and testing sets

2. **Data Validation**:
   - Validate data against schema
   - Check for drift between training and testing data
   - Create validation report

3. **Data Transformation**:
   - Handle missing values with KNN imputation
   - Process features for model training
   - Save transformation objects for inference

4. **Model Training**:
   - Train multiple classification models:
     - Random Forest
     - Decision Tree
     - Gradient Boosting
     - Logistic Regression
     - AdaBoost
   - Automatically tune hyperparameters with GridSearchCV
   - Select best model based on performance

5. **Model Evaluation**:
   - Evaluate using F1 score, precision, and recall
   - Track experiments with MLflow
   - Save model artifacts

## Technology Stack

- **Python**: Primary programming language
- **scikit-learn**: Machine learning algorithms and pipelines
- **MongoDB**: Data storage
- **AWS S3**: Artifact storage
- **MLflow**: Experiment tracking
- **DagsHub**: Collaboration and ML experiment management
- **Docker**: Containerization
- **GitHub Actions**: CI/CD pipeline

## Deployment

The system is deployed using a CI/CD pipeline with GitHub Actions:

1. Code changes trigger the workflow
2. Integration tests are run
3. Docker image is built and pushed to AWS ECR
4. New image is deployed to production server

## Getting Started

### Prerequisites
- Python 3.8+
- MongoDB
- AWS account with S3 and ECR access
- Docker

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/phishing-detection.git
cd phishing-detection

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
export MONGO_DB_URL="your_mongodb_connection_string"
export AWS_ACCESS_KEY_ID="your_aws_access_key"
export AWS_SECRET_ACCESS_KEY="your_aws_secret_key"
export AWS_REGION="your_aws_region"
```

### Running the Pipeline
```bash
python main.py
```
