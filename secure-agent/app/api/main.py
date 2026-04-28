from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.security.pipeline import run_security_pipeline

app = FastAPI(
    title="SecureAgent",
    description="Production-grade prompt injection detection for LLM applications.",
    version="1.0.0",
)


class ValidateRequest(BaseModel):
    text: str


class ValidateResponse(BaseModel):
    status: str
    cleaned_input: str
    votes: list[str]
    confidence: float
    reason: str


@app.post("/validate", response_model=ValidateResponse)
def validate(request: ValidateRequest):
    """
    Analyse input text for prompt injection attempts.

    Returns UNSAFE + confidence score if an attack is detected,
    SAFE + cleaned input otherwise.
    """
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Input text cannot be empty.")
    return run_security_pipeline(request.text)


@app.get("/health")
def health():
    return {"status": "ok"}
