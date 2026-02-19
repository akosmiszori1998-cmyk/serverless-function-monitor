# serverless-function-monitor
A cloud-native monitoring microservice project focusing on Python, FastAPI, and Docker containerization.
# Serverless Function Monitor

Production-ready microservice built with Python and FastAPI to monitor the health and status of serverless functions. This project is fully containerized using Docker for easy deployment and scalability.

## Features
- **FastAPI**: High-performance, asynchronous web framework.
- **Health Checks**: Simple endpoints to verify system status.
- **Dockerized**: Ready to run in any environment.
- **Auto-Documentation**: Interactive API docs via Swagger UI.

## Technology Stack
- **Language**: Python 3.13-slim
- **Web Framework**: FastAPI
- **Web Server**: Uvicorn
- **Containerization**: Docker

## How to Run

### 1. Build the Docker Image
docker build -t serverless-monitor .

### 2. Run the Container
docker run -d -p 8000:8000 --name monitor-app serverless-monitor

### 3. Access the API
- **API Home**: http://localhost:8000
- **Interactive Docs (Swagger)**: http://localhost:8000/docs

## 📁 Project Structure
- `api.py`: The core FastAPI application.
- `Dockerfile`: Instructions for building the Docker image.
- `requirements.txt`: Python dependencies.
- `.gitignore`: Files and folders to be ignored by Git.
