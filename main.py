from fastapi import FastAPI, Depends, HTTPException
from database import get_db, Base, engine
import schemas

app = FastAPI()  # ← Idi top lo undali

students = [
    {"id": 1, "name": "Ankitha", "role": "Docker Queen"},
    {"id": 2, "name": "Sravan", "role": "Backend Dev"},
    {"id": 3, "name": "laddu", "role": "chinnoda"}
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