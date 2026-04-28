from app.security.ensemble import ensemble_vote
from app.security.logger import log_event
from app.security.sanitizer import sanitize_input


def run_security_pipeline(user_input: str) -> dict:
    """
    Run the full security pipeline on raw user input.

    Order matters: detection runs on the original text before sanitisation.
    Sanitising first would strip the injection phrases the classifiers look for,
    causing all attacks to silently pass through as SAFE.
    """
    final, votes, confidence = ensemble_vote(user_input)
    cleaned = sanitize_input(user_input)

    result = {
        "status": final,
        "cleaned_input": cleaned,
        "votes": votes,
        "confidence": round(confidence, 4),
        "reason": "Potential prompt injection" if final == "UNSAFE" else "Clean",
    }

    if final == "UNSAFE":
        log_event(result)

    return result
