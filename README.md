# Chicken-Disease-Classification-Project

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
---

## Table of Contents
1. Project Scope
2. Audience-Friendly Description
3. Business Impact
4. Project Description
5. Folder Structure
6. Flow Diagram
7. Dashboards & Visualizations
8. Output
9. How to Run & Dependencies
10. Contribution Guidelines
11. License & Credits
12. Next Steps

---

## Project Scope
Develop an AI-powered system to automatically classify chicken diseases from images using Convolutional Neural Networks (CNNs), enabling farmers, veterinarians, and poultry businesses to detect diseases early and prevent outbreaks.

---

## Audience-Friendly Description
This project leverages machine learning to identify diseases in chickens from images. Users can upload a picture of their chicken, and the system predicts whether it is healthy or affected by a disease, providing actionable insights quickly and efficiently.

---

## Business Impact
- Early detection: Prevents disease outbreaks in poultry farms.
- Revenue protection: Reduces loss from livestock mortality.
- Operational efficiency: Automates manual inspection processes.
- Decision support: Provides actionable insights for veterinarians and farm managers.

---

## Project Description
- Technology Stack: Python, TensorFlow/Keras, OpenCV, DVC, Docker, AWS/Azure.
- Model Details: CNN architecture based on VGG16 as a base model with transfer learning.
- Metrics: Accuracy, Loss, Confusion Matrix; evaluated on a validation split of 20–30%.
- Features:
  - Image preprocessing and augmentation (rotation, flipping, zoom, shear).
  - Automated pipeline for ingestion, training, evaluation, and deployment.
- Output & Inference:
  - Predicts the disease class for an input image.
  - Outputs probabilities for each class and saves the trained model.

---

## Folder Structure
<pre>
│
├── app.py # Main app for running inference
├── config.yaml # Project configurations
├── secrets.yaml # Optional secrets
├── params.yaml # Hyperparameters and model parameters
├── src/ # Source code
│ ├── config/ # Configuration management
│ ├── components/ # Individual ML pipeline components
│ ├── pipeline/ # ML pipeline orchestration
│ └── utils/ # Helper functions
├── data/ # Raw and processed datasets
├── models/ # Saved models (base, updated, trained)
├── notebooks/ # Jupyter notebooks
├── dvc.yaml # DVC pipeline
└── requirements.txt # Python dependencies
</pre>
---
## Flow Diagram

Data Ingestion → Preprocessing → Base Model Preparation → Training → Evaluation → Deployment

- Ingestion: Downloads and extracts image dataset.
- Preprocessing: Resizing, rescaling, augmentation.
- Base Model: VGG16 with transfer learning.
- Training: Custom layers added, model trained with augmented images.
- Evaluation: Model accuracy, loss, and metrics stored.
- Deployment: Dockerized app deployed on AWS/Azure for inference.

---

## Dashboards & Visualizations

---

## Output
- Trained CNN model saved in /models.
- Inference output: Predicted class with probability scores.
- Evaluation scores saved as scores.json.

---

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/mappy92/Chicken-Disease-Detection
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  

    ECR_REPOSITORY_NAME = simple-app




# AZURE-CICD-Deployment-with-Github-Actions

## Save pass:

password from azure portal


## Run from terminal:

docker build -t chickenapplication.azurecr.io/chicken:latest .

docker login chickenapplication.azurecr.io

docker push chickenapplication.azurecr.io/chicken:latest


## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run


---

## Dependencies
1. Python 3.8
2. TensorFlow, Keras
3. OpenCV, NumPy, Pandas
4. DVC
5. Docker

---

## Contribution Guidelines
1. Fork the repository
2. Create a new branch
3. Run tests
4. Submit a Pull Request

---

## Next Steps
1. Add more chicken disease classes.
2. Deploy as a hosted web application.
3. Enable real-time video inference.
