# Resume Sorting API

This project provides a RESTful API that categorizes resumes in PDF format into predefined classes using a machine learning model. It is built using **FastAPI** and **Docker**, and is deployed on **Google Cloud Platform (GCP)**. The model used for classification is trained on a limited dataset of 16 classes, and the project provides endpoints for resume categorization.

Link for accessing the WebApp version of the API: [Resume Sorting App](https://resumenlp-api-1-0-0-496910431430.us-central1.run.app/)

You can test the WebApp with demo pdf files [Resume PDFs](link)

## Features

- Categorize resumes in PDF format into 16 predefined classes.
- Built with **FastAPI** for easy integration and scalability.
- Dockerized for deployment and pushed to **Google Cloud Platform (GCP)**.
- Includes a pre-trained model (`state_dict_model.pt`) for immediate use.
- The webapp is hardcoded to run index.html on startup for easy use.


![Python](https://img.shields.io/badge/python-v3.9.0-green) ![API](https://img.shields.io/badge/API-Fast%20Api-teal) ![GCP](https://img.shields.io/badge/Cloud-Google%20Cloud%20Platform-orange) 

![Platform](https://img.shields.io/badge/Repository-Docker%20Hub-blue) ![Platform](https://img.shields.io/badge/Platform-Windows10%20Pro%20version%20%2022H2-blue)


### Web Interface

You can access the Web App deployed on GCP via the following link:

[Resume Sorting API](https://resumenlp-api-1-0-0-496910431430.us-central1.run.app/)

For using the API as a stand alone app, an `index.html` file is hardcoded to load on startup. This allows you to interact with the API through a simple web interface, making it easier to upload PDF files and view the results as a web application.

### Note:
The first request to the API might take longer (up to 30 seconds) due to cold start. Please be patient.
The current GCP account is a free version which might expire, in any worse case please use the dockerized [Image](link).

## Dataset
The model is trained on a dataset of resumes classified into 16 categories. Due to the limited size of the dataset, it is recommended to test the API with PDF files from the following categories:

AGRICULTURE, SALES, ACCOUNTANT, AVIATION, BANKING, CONSULTANT, FINANCE, PUBLIC-RELATIONS, BUSINESS-DEVELOPMENT, CHEF, AUTOMOBILE, INFORMATION-TECHNOLOGY, DIGITAL-MEDIA, ENGINEERING, ARTS, HR.

You can test the WebApp with demo pdf files at [Resume PDFs](link)


## API Endpoint 
### Endpoint

- **POST /classify_resume**  
  Input: PDF file  
  Output: Category of the resume.

### Response Example

```json
{
    "category": "ACCOUNTANT"
}
```


## Setup Instructions (Locally)
The project is fully containerized and comes with a pre-built Docker image to run the API in a container.

## Use the Pre-Built Docker Image
### Prerequisites
Docker: Make sure you have Docker installed on your machine.

Pull the pre-built Docker image from [DockerHub](linkk). For example:
```bash
docker pull yourusername/resume-sorting-api:latest
```
Run the pulled image in a container:

```bash
docker run -p 8000:8000 yourusername/resume-sorting-api:latest
```

## Project Structure (Files inside the docker image)

- `main.py`: The entry point of the FastAPI application.
- `model.py`: Contains the logic for loading the pre-trained model.
- `script.py`: Script used for PDF processing and categorization.
- `requirements.txt`: List of dependencies needed to run the project.
- `state_dict_model.pt`: The pre-trained model file [Drive](link).
- `Dockerfile`: The configuration for building the Docker image.
- `index.html`: A simple web interface for interacting with the API.

## Model Creation
If you're interested in understanding how the model was built, including data preprocessing and training steps, refer to the separate repository for the ResumeSorter project: [ResumeSorter](https://github.com/hrafid/ResumeSorter).


#
## 🔗 Links

[![linkedin](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rakibul-haque/)

