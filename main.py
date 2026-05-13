from fastapi import FastAPI

app = FastAPI()
students = [
    {"id": 1, "name": "Ankitha", "role": "Docker Queen"},
    {"id": 2, "name": "Sravan", "role": "Backend Dev"}
]

@app.get("/students")
def get_students():
    return students
@app.get("/")
def read_root():
    return {"message": "Hello from Docker Backend!"}

@app.get("/health")
def health_check():
    return {"status": "Backend is running fine"}