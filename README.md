# Student Management System

This project is a Student Management System built with Streamlit for the frontend and Flask for the backend. The backend uses PostgreSQL for data storage. The project is containerized using Docker, allowing the frontend and backend to run in separate containers. The system allows for managing student data and interacting with the database through natural language instructions processed by OpenAI's GPT models.

## Getting Started

### Prerequisites
- Docker and Docker Compose installed on your machine.

### Clone the Repository
```bash
git clone https://github.com/Tanmay1903/student-management.git
cd task-manager
```

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

### Testing and Functionality
#### 1. Testing the Script
The system allows you to manage student data using natural language instructions, which are processed by an AI model and executed by the backend API. Below are some key functionalities and how you can test them:

- **Adding a New Student**
  - Instruction: "Add a new student named John Doe with ID 12345."
  - Expected Behavior: The system should add the student to the database and return a confirmation message: "Student added successfully."
  - Test: Enter the instruction in the Streamlit interface and check the backend database to ensure the student was added correctly.

- **Adding a Score for a Student**
  - Instruction: "Add a score of 95 for John Doe in Math."
  - Expected Behavior: The system should update the student's record with the new score for the specified subject.
  - Test: Enter the instruction and verify that the score has been added by checking the student's record in the backend database.

- **Querying a Student's Subjects**
  - Instruction: "What subject did John Doe take?"
  - Expected Behavior: The system should return the subject(s) associated with the student.
  - Test: Enter the instruction and verify the response matches the data stored in the database.

- **Summarizing Student Scores for a Subject**
  - Instruction: "Summarize all student scores in Math."
  - Expected Behavior: The system should provide a summary of all scores for the specified subject.
  - Test: Enter the instruction and verify that the summary includes all relevant data from the database.

#### 2. Edge Cases and Limitations
- **Invalid Instructions:**
  - If an instruction is unclear or contains an error (e.g., "Add a student without a name"), the system should handle it gracefully by either asking for more information or returning an appropriate error message.
  - Test: Try ambiguous or incomplete instructions and ensure the system either requests clarification or handles the error appropriately.

- **Non-existent Entities:**
  - Instructions referencing non-existent students or subjects should return a meaningful error message (e.g., "Student not found").
  - Test: Query or update records that don't exist in the database to see how the system handles these cases.

- **Instruction Parsing:**
  - The accuracy of instruction parsing relies heavily on the AI model's ability to understand natural language. Some edge cases may not be handled perfectly, especially if the instruction is highly ambiguous or grammatically incorrect.
