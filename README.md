# Student Management System

This project is a Student Management System built with Streamlit for the frontend and Flask for the backend. The backend uses PostgreSQL for data storage. The project is containerized using Docker, allowing the frontend and backend to run in separate containers. The system allows for managing student data and interacting with the database through natural language instructions processed by OpenAI's GPT models.

## Getting Started

### Prerequisites
- Docker and Docker Compose installed on your machine.

### Environment Variables
 - Create a .env file in both the student-manager/ and student-manager-backend/ directories with the following content:
   - `student-manager/.env`
     
     ```bash
     OPENAI_API_KEY=your_openai_api_key
     ```
     Replace `your_openai_api_key` with the actual api key.
   - `student-manager-backend/.env`
     
     ```bash
     DATABASE_URL=<POSTGRESQL_DATABASE_URI>
     ```
     Copy this `POSTGRESQL_DATABASE_URI` from the provided .env file

### Docker Setup
#### 1. Build and Start Containers
Use Docker Compose to build and start the frontend and backend containers:

```bash
docker-compose up --build
```
This will build the Docker images for the frontend and backend and start the containers.

#### 2. Access the Application
- Streamlit Frontend: http://localhost:8501
- Flask Backend: http://localhost:5051

Interact with the application through the Streamlit interface to manage student data.

### Stopping the Application
To stop the containers, run:
```bash
docker-compose down
```


