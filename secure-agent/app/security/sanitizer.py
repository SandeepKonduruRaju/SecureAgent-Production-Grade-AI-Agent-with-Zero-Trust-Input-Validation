import re

INJECTION_PATTERNS = [
    r"ignore previous instructions",
    r"reveal system prompt",
    r"bypass security",
    r"act as",
    r"you are now",
]


def sanitize_input(user_input: str) -> str:
    """
    Remove known injection phrases from input and return cleaned text.

    Used for producing the cleaned_input field in the response — NOT for
    detection. Detection always runs on the raw input before this function.
    """
    cleaned = user_input
    for pattern in INJECTION_PATTERNS:
        cleaned = re.sub(pattern, "", cleaned, flags=re.IGNORECASE)
    return cleaned.strip()
