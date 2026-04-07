# app/security/sanitizer.py

import re

INJECTION_PATTERNS = [
    r"ignore previous instructions",
    r"reveal system prompt",
    r"bypass security",
    r"act as",
    r"you are now",
]

def sanitize_input(user_input: str) -> str:
    cleaned = user_input.lower()

    for pattern in INJECTION_PATTERNS:
        cleaned = re.sub(pattern, "", cleaned, flags=re.IGNORECASE)

    return cleaned.strip()