# app/security/pipeline.py

from app.security.sanitizer import sanitize_input
from app.security.ensemble import ensemble_vote
from app.security.logger import log_event


def run_security_pipeline(user_input: str):
    final, votes, confidence = ensemble_vote(user_input)

    cleaned = sanitize_input(user_input)

    result = {
        "status": final,
        "cleaned_input": cleaned,
        "votes": votes,
        "confidence": confidence,
        "reason": "Potential prompt injection" if final == "UNSAFE" else "Clean",
    }

    if final == "UNSAFE":
        log_event(result)

    return result
