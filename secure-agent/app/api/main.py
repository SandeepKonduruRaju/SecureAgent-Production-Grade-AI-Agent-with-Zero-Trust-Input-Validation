# app/api/main.py

from fastapi import FastAPI
from app.security.pipeline import run_security_pipeline

app = FastAPI()

@app.post("/validate")
def validate(input: dict):
    return run_security_pipeline(input["text"])