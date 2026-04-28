"""
Ensemble classifier for prompt injection detection.

Three independent classifiers vote on whether input is SAFE or UNSAFE.
A majority (2 of 3) triggers UNSAFE. Known high-risk keywords hard-override
the vote to UNSAFE regardless of the majority — zero tolerance for known
attack phrases.
"""

HIGH_RISK_KEYWORDS = [
    "bypass",
    "hacker",
    "ignore instructions",
    "system prompt",
    "override",
]

# Each classifier targets a distinct subset of injection patterns so that
# evasion techniques that fool one model are caught by another.

def _classifier_1(text: str) -> str:
    triggers = ["ignore", "reveal", "system prompt"]
    return "UNSAFE" if any(t in text.lower() for t in triggers) else "SAFE"


def _classifier_2(text: str) -> str:
    triggers = ["bypass", "hacker", "admin"]
    return "UNSAFE" if any(t in text.lower() for t in triggers) else "SAFE"


def _classifier_3(text: str) -> str:
    triggers = ["instructions", "act as", "override"]
    return "UNSAFE" if any(t in text.lower() for t in triggers) else "SAFE"


def _contains_high_risk(text: str) -> bool:
    lower = text.lower()
    return any(kw in lower for kw in HIGH_RISK_KEYWORDS)


def ensemble_vote(text: str) -> tuple[str, list[str], float]:
    """
    Run all classifiers and return (verdict, votes, confidence).

    confidence is the fraction of classifiers that voted UNSAFE,
    floored at 1.0 when a high-risk keyword triggers the hard override.
    """
    votes = [_classifier_1(text), _classifier_2(text), _classifier_3(text)]
    unsafe_count = votes.count("UNSAFE")
    high_risk = _contains_high_risk(text)

    final = "UNSAFE" if unsafe_count >= 2 or high_risk else "SAFE"
    confidence = unsafe_count / len(votes)
    if high_risk and final == "UNSAFE":
        confidence = max(confidence, 1.0)

    return final, votes, confidence
