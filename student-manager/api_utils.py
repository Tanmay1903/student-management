import requests

API_BASE_URL = "http://backend:5051"

def add_student(name: str, student_id: int):
    data = {'name': name, 'student_id': student_id}
    try:
        response = requests.post(f"{API_BASE_URL}/students", json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)
        return response.json()
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

def add_score(student_name: str, subject: str, score: int):
    data = {'student_name': student_name, 'subject': subject, 'score': score}
    try:
        response = requests.post(f"{API_BASE_URL}/scores", json=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

def get_subject(student_name: str):
    try:
        response = requests.get(f"{API_BASE_URL}/students/{student_name}/subject")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

def summarize_scores(subject: str):
    try:
        response = requests.get(f"{API_BASE_URL}/scores/summary", params={'subject': subject})
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}
