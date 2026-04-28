# app/security/ensemble.py

HIGH_RISK_KEYWORDS = [
    "bypass",
    "hacker",
    "ignore instructions",
    "system prompt",
    "override",
]


def mock_model_1(text):
    return "UNSAFE" if any(x in text.lower() for x in ["ignore", "reveal", "system prompt"]) else "SAFE"

def mock_model_2(text):
    return "UNSAFE" if any(x in text.lower() for x in ["bypass", "hacker", "admin"]) else "SAFE"

def mock_model_3(text):
    return "UNSAFE" if any(x in text.lower() for x in ["instructions", "act as", "override"]) else "SAFE"

def contains_high_risk(text: str):
    text = text.lower()
    return any(keyword in text for keyword in HIGH_RISK_KEYWORDS)

def ensemble_vote(text: str):
    votes = [
        mock_model_1(text),
        mock_model_2(text),
        mock_model_3(text),
    ]

    unsafe_count = votes.count("UNSAFE")
    high_risk = contains_high_risk(text)

    # Hard override: high-risk keywords are treated as unsafe even with split votes.
    final = "UNSAFE" if unsafe_count >= 2 or high_risk else "SAFE"

    confidence = unsafe_count / len(votes)
    if high_risk and final == "UNSAFE":
        confidence = max(confidence, 1.0)

    return final, votes, confidence
