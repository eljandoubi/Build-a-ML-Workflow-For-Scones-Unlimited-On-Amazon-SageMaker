# Build-a-ML-Workflow-For-Scones-Unlimited-On-Amazon-SageMaker
The primary objective of this project was to build and deploy an image classification model for Scones Unlimited, a scone-delivery-focused logistic company, using AWS SageMaker.

# Project: 
## Deploy and Monitor a Machine Learning Workflow for Image Classification Using Amazon SageMaker
### Source: AWS Machine Learning Engineer Nanodegree Scholarship Program

## 1. Overview

This project was a part of the project assessment in the **'AWS Machine Learning Engineer'**.

## 2. Getting Started

### 2.1. Project files related information:

**1. `Project2_Build-a-ML-Workflow-For-Scones-Unlimited-On-Amazon-SageMaker.ipynb`:** Jupyter notebook showcases a machine learning working workflow for Image Classification. This includes the necessary preprocessing of the scones unlimited image dataser, model training, deployment and monitor using Amazon SageMaker and other associated AWS Services.<br><br>
**2. `Lambda.py` script:** `compilation of the necessary 'lambda.py' scripts used by three AWS Lambda functions to create a Step Functions workflow`. (*Note: The 'lambda.py' file typically has a 'lambda_handler' function, which acts as the entry point for the Lambda function when it is triggered by an event such as an HTTP request or a scheduled cron job. This function takes an 'event' object, which contains information about the triggering event and a 'context' object, which contains information about the current execution environment. The 'lambda_handler' function is where the main logic of the Lambda function is executed, it can interact with other AWS services, perform calculations or process data. The function can also return a response to the service or client that triggered the Lambda function.)*<br><br>
**3. `Screenshot-of-Working-Step-Function.PNG`:** screen capture of working step function. <br><br>
**4. `step-function.json`:** Step Function exported to JSON<br><br>

### 2.2. Dependencies
```
Python 3 (Data Science) - v3.7.10 kernel
ml.t3.medium instance
Python 3.8 runtime for the AWS Lambda Functions
```

### 2.3. Installation

For local development, you will need to setup a jupyter lab instance.
* Follow the [jupyter install](https://jupyter.org/install.html) link for best practices to install and start a jupyter lab instance.
* If you have a python virtual environment already installed you can just `pip` install it.
```
pip install jupyterlab
```
* There are also docker containers containing jupyter lab from [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/index.html).

## 3. Approach:

The project aims to develop an image classification Machine Learning Model using workflows on Amazon SageMaker, automating various Machine Learning tasks such as Data Preparation, Model Training, Deployment, and Inference with the help of AWS Step Functions and Lambda functions.